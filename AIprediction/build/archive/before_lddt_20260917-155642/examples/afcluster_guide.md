# AF-Cluster의 서열 cluster에서 구조 후보까지

2026-09-17 공식 코드 확인 기준. 아래 명령은 **문서·소스 대조를 마친 실행 예시**이며, 이 강의 자료 제작 중 설치나 GPU 추론을 실행하지 않았습니다. 논문의 모든 결과를 그대로 재현하는 설정은 아닙니다.

준비물: 실제 단량체의 ColabFold baseline에서 저장한 `target.a3m`, Git·Python·venv, 별도로 설치된 `colabfold_batch`와 AF2 모델 파일·적합한 GPU 환경. 첫 서열은 전체 query이고, 소문자 insertion을 제외한 각 행의 길이가 query와 같아야 합니다. 가상 실습 정렬을 실제 단백질 MSA와 섞지 않습니다.

아래는 같은 **bash 세션**에서 순서대로 실행합니다. 경로를 실제 A3M의 절대 경로로 바꾸세요. 새 임시 이름의 작업 폴더를 만들어 원본과 이전 결과를 보존합니다. 설치는 [AF-Cluster 의존성](https://github.com/HWaymentSteele/AF_Cluster/blob/main/requirements.txt)과 [ColabFold 공식 안내](https://github.com/sokrypton/ColabFold)를 따릅니다.

```bash
set -euo pipefail
MSA_INPUT="/absolute/path/to/target.a3m"
test -f "$MSA_INPUT"
AFCLUSTER_RUN=$(mktemp -d "$PWD/afcluster-run.XXXXXX")
git clone --depth 1 https://github.com/HWaymentSteele/AF_Cluster.git "$AFCLUSTER_RUN/AF_Cluster"
cp "$MSA_INPUT" "$AFCLUSTER_RUN/target.a3m"
python3 -m venv "$AFCLUSTER_RUN/cluster-env"
"$AFCLUSTER_RUN/cluster-env/bin/python" -m pip install -r "$AFCLUSTER_RUN/AF_Cluster/requirements.txt"
cd "$AFCLUSTER_RUN"
git -C AF_Cluster rev-parse HEAD > afcluster_commit.txt
cluster-env/bin/python AF_Cluster/scripts/ClusterMSA.py TARGET -i target.a3m -o msas --n_controls 0
```

`TARGET`는 출력 이름용 필수 positional 인자입니다. `--n_controls 0`은 추가 무작위 대조 MSA 생성을 생략합니다. 기본 명령은 DBSCAN의 epsilon을 탐색합니다. 매우 얕거나 gap이 많은 MSA에서는 탐색·clustering이 실패할 수 있습니다.

- `msas/TARGET_000.a3m` 등: 각 서열 cluster의 별도 입력. 원래 query를 맨 앞에 다시 넣습니다.
- `msas/TARGET_clustering_assignments.tsv`: 각 homolog의 배정값; `-1`은 미배정입니다.
- `msas/TARGET_cluster_metadata.tsv`: cluster 정보. `size`는 query를 포함합니다.
- 현재 코드는 lowercase insertion을 제거하고 gap 비율이 기본 0.25 미만인 homolog를 남깁니다. 이 전처리도 기록합니다.
- README에 기재된 `TARGET_REF.a3m`은 확인한 코드에서 생성되지 않으므로 원본 `target.a3m`을 기준선으로 직접 보존했습니다.

파일 생성은 구조 예측 성공이 아닙니다. 먼저 query·열 수와 실제 cluster 파일 존재를 확인합니다.

```bash
cluster-env/bin/python - <<'PY'
from pathlib import Path
from Bio import SeqIO
query = str(next(SeqIO.parse("target.a3m", "fasta")).seq)
files = sorted(Path("msas").glob("TARGET_[0-9]*.a3m"))
assert files, "서열 cluster 출력 없음: 로그와 MSA 품질을 확인하세요"
for path in files:
    rows = [str(record.seq) for record in SeqIO.parse(path, "fasta")]
    assert rows[0] == query and all(len(row) == len(query) for row in rows), path
print(f"{len(files)} clusters; 다음 단계는 각 조건 {3 * len(files)}개, 총 {6 * len(files)}개 구조 예측")
PY
```

다음 루프는 생성된 A3M 디렉터리를 읽어 **cluster마다 결과 폴더를 분리**합니다. 각 cluster와 원본 baseline에 같은 모델 1개와 동일한 seed 3개를 사용합니다. 다음 cluster에서는 seed 시작값을 3씩 늘려, K개 cluster와 baseline에 각각 3K개 예측을 배정합니다. 실행 전 K와 계산 예산을 확인하세요. 같은 ColabFold 버전을 사용하며 아래 설정은 template·dropout을 켜지 않습니다.

```bash
seed_start=0
for cluster_msa in msas/TARGET_[0-9]*.a3m; do
  test -f "$cluster_msa"
  cluster_name=$(basename "$cluster_msa" .a3m)
  colabfold_batch "$cluster_msa" "results/clusters/$cluster_name" \
    --model-type alphafold2_ptm --model-order 1 --num-models 1 \
    --random-seed "$seed_start" --num-seeds 3 --num-recycle 3
  colabfold_batch target.a3m "results/baseline/$cluster_name" \
    --model-type alphafold2_ptm --model-order 1 --num-models 1 \
    --random-seed "$seed_start" --num-seeds 3 --num-recycle 3
  seed_start=$((seed_start + 3))
done
```

A3M 입력은 ColabFold의 MSA 검색 설정을 대신합니다. 내부 MSA 한도·조기 종료 등 설치 버전의 기본값도 로그에 보관하고 조건 간 동일하게 유지하세요. 실제 완료한 모델 수를 확인합니다. 이 예시는 전처리를 포함한 전체 방법과 원본 baseline의 비교입니다. **Clustering 자체의 효과**를 분리하려면 같은 전처리·깊이의 무작위 subset 대조가 추가로 필요합니다. 예측 seed는 clustering 난수까지 고정하지 않으므로 생성한 A3M도 보관합니다.

완료한 좌표·pLDDT·PAE와 로그를 확인한 뒤, 같은 core를 정렬해 구조 차이와 기하학적 품질을 비교합니다. 다른 후보를 얻으면 독립 검증할 가설이 늘어난 것이고, 비슷한 구조만 나오면 그 조건에서 차이를 찾지 못한 것입니다. 어느 결과도 상태의 존재·부재, 점유율, 전환 속도를 단독으로 증명하지 않습니다.

공식 근거: [AF-Cluster README](https://github.com/HWaymentSteele/AF_Cluster), [확인한 ClusterMSA.py](https://github.com/HWaymentSteele/AF_Cluster/blob/6b22451c5a9def576f43824bb5573a9c1faf6c55/scripts/ClusterMSA.py), [ColabFold CLI](https://github.com/sokrypton/ColabFold/blob/main/colabfold/batch.py). 저자는 [ColabDesign 통합 노트북](https://colab.research.google.com/github/HWaymentSteele/AF_Cluster/blob/main/AF_cluster_in_colabdesign.ipynb)도 제공합니다.

열 마스킹은 별도 방법입니다. [AFsample2 공식 저장소](https://github.com/wallnerlab/AFsample2)는 query를 유지하는 X 마스킹과 dropout 경로를 제공합니다. [SPEACH_AF 공식 저장소](https://github.com/RSvan/SPEACH_AF)는 A 편집을 사용하며 원 notebook은 query도 편집합니다. 두 방법을 같은 조작으로 부르지 말고 각 버전의 입력·실행 문서를 따르세요.
