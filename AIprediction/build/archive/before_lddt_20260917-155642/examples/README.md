# 실제 CALM1 입력 준비와 선택 실습

브라우저로 처음 실습한다면 [ColabFold 단계별 안내](colabfold_walkthrough.md)를 먼저 사용하세요. 공식 노트북 접속, GPU 설정, 서열 입력과 custom MSA 업로드 순서가 있습니다. 아래는 ColabFold와 AF3의 로컬 실행 참고입니다.

이 폴더의 `prepare_inputs.py`는 **입력 파일만 준비**합니다. 실제 MSA 검색이나 구조 예측은 실행하지 않았습니다. 아래 예측 명령은 해당 도구·모델 파라미터·적합한 계산 환경이 이미 설치된 경우에 사용하는 선택 실습입니다. 오프라인 문법 실습은 `../practice/README.md`를 사용합니다.

## 서열 출처

`calmodulin_P0DP23.fasta`는 UniProt의 **human CALM1 / Calmodulin-1, P0DP23**, 원문 149잔기입니다. 공식 FASTA를 2026-09-17에 받아 확인했습니다. [UniProt 항목](https://www.uniprot.org/uniprotkb/P0DP23/entry), [공식 FASTA endpoint](https://rest.uniprot.org/uniprotkb/P0DP23.fasta).

첫 Met를 포함한 전체 서열을 그대로 사용합니다. 구조 파일의 성숙 단백질 사슬·누락 잔기·잔기 번호가 이 FASTA와 같다고 가정하지 않습니다. 이 예제는 단백질 단량체 입력이며 calcium·결합 상대·수정 잔기를 명시하지 않습니다. 따라서 결과를 특정 calcium 결합 상태의 재현으로 간주할 수 없습니다.

## 1. 실제 MSA 얻기

명령은 `AIprediction/`에서 실행합니다. ColabFold가 설치된 환경에서는 다음과 같이 실제 MSA 검색과 baseline 예측을 실행할 수 있습니다. FASTA 입력은 공개 MSA 서버로 전달될 수 있습니다.

```sh
colabfold_batch examples/calmodulin_P0DP23.fasta results/baseline
```

MSA만 먼저 준비하려면 위 명령 대신 `--msa-only`를 붙입니다. 공식 [ColabFold README](https://github.com/sokrypton/ColabFold)의 설치·환경 안내를 따릅니다. GPU가 준비되지 않았다면 수업 중 설치를 시도하기보다 오프라인 실습을 진행합니다.

```sh
colabfold_batch examples/calmodulin_P0DP23.fasta results/baseline --msa-only
```

결과 폴더의 해당 `.a3m` 파일을 `target.a3m`이라는 새 파일로 복사합니다. 아래 복사 명령은 `results/baseline/`에 **이 단일 query의 `.a3m`이 하나만 있고 `target.a3m`이 없을 때** 사용하는 예입니다. 기존 파일이 있으면 새 이름을 선택합니다.

```sh
cp -n results/baseline/*.a3m target.a3m
```

로컬 설치가 없으면 [공식 ColabFold 노트북](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb)에 FASTA의 **서열만** 붙여 검색하고, 결과 ZIP의 대응 A3M을 받아 같은 위치에 둡니다. 수정한 실제 MSA가 있다면 노트북의 `msa_mode=custom` 입력을 사용합니다. 옵션 위치·계산 자원·완료 시간은 환경에 따라 달라집니다. `practice/fictional_learning.a3m`을 실제 예측 입력으로 제출하지 않습니다.

## 2. AF3 입력 파일 준비

```sh
python3 examples/prepare_inputs.py --self-test
python3 examples/prepare_inputs.py examples/calmodulin_P0DP23.fasta target.a3m --out prepared
```

표준 Python 3.8 이상만 필요합니다. 첫 query가 FASTA와 **정확히 같은지**, 소문자 삽입을 제외한 각 행의 정렬 길이가 같은지 검사합니다. 지원 문자는 20개 표준 아미노산+X의 대·소문자와 gap `-`입니다. query는 대문자만 허용합니다. `.` padding·기타 모호 문자·복합체 A3M은 거부하며 내용을 추정해 고치지 않습니다. FASTA는 서열 하나만 허용하고 여러 줄로 나눠 써도 됩니다. **이 스크립트가 지원하는 A3M은 각 서열을 한 줄로 저장한 형식입니다.** query 한 행만 있는 A3M도 문법상 유효하지만 homolog 정보가 없는 조건입니다.

ColabFold의 선두 `#149<TAB>1`처럼 단량체 길이·복제수를 표시하는 행은 검증 후 그대로 보존합니다. sequence 검색 여부나 상동관계의 진위를 검증하는 도구는 아니므로 검색 도구·DB·날짜·설정을 별도로 기록합니다. 그룹 라벨은 요구하지 않습니다.

| 생성 파일 | 용도 |
|---|---|
| `prepared/target.a3m` | 검증한 원본 바이트 그대로 복사; query·소문자·gap 보존 |
| `prepared/alphafold3.json` | 로컬 AF3 dialect/version 2, seed 0·1·2, 단백질 A, custom unpaired MSA, paired MSA 없음, template 없음 |

이미 존재하는 `--out` 폴더는 덮어쓰지 않고 종료 코드 2로 거부합니다. 다시 실행할 때는 `--out prepared_run2`처럼 새 이름을 사용합니다. AF3의 `unpairedMsaPath`는 JSON 파일 기준 상대경로이므로 두 파일을 함께 보관합니다. 프로그램은 복사본 SHA-256을 출력하고 저장 내용을 재검사합니다.

## 3. 같은 ColabFold 모델에서 MSA cap 비교

다음 두 명령은 동일한 `target.a3m`으로 AF2-ptm, 모델 수 1, 예측 seed 0·1·2, recycle 설정을 유지하면서 MSA cap만 바꿉니다. `32:64`는 대표 MSA/extra MSA 각각의 상한 설정이며 파일에서 무작위 32행을 뽑는다는 뜻이 아닙니다. 실제 원시 MSA가 작으면 두 설정의 유효 입력이 같을 수 있습니다. 모델이 사용한 입력과 로그를 확인합니다. [공식 CLI 소스](https://github.com/sokrypton/ColabFold/blob/main/colabfold/batch.py).

```sh
colabfold_batch target.a3m results/msa_32_64 \
  --model-type alphafold2_ptm --num-models 1 --num-seeds 3 \
  --random-seed 0 --num-recycle 3 --recycle-early-stop-tolerance 0.0 \
  --max-msa 32:64

colabfold_batch target.a3m results/msa_128_256 \
  --model-type alphafold2_ptm --num-models 1 --num-seeds 3 \
  --random-seed 0 --num-recycle 3 --recycle-early-stop-tolerance 0.0 \
  --max-msa 128:256
```

별도로 만든 실제 부분집합 A3M을 비교하려면 query와 삽입 문법을 유지하고 파일 이름·행 선택 seed·선택 ID를 기록합니다. `target.a3m` 대신 해당 파일을 지정해 위와 같은 모델 설정으로 실행합니다. 두 경우의 cap과 실제 행 수를 모두 기록합니다. `prepare_inputs.py`에 각 부분집합을 전달하면 같은 query인지 다시 검증할 수 있습니다. 사전 그룹 분리는 AF-Cluster의 실제 알고리즘을 구현한 것이 아닙니다.

## 4. 로컬 AF3 실행

**다음 명령은 이미 설치된 환경에서만 실행합니다.** ColabFold와 AF3는 모델·MSA 처리·샘플 수가 달라 두 도구의 결과 차이를 MSA 효과만으로 해석할 수 없습니다. 이 자료 생성 과정에서는 명령을 실행하지 않았습니다.

AlphaFold 3는 **로컬 AF3 코드용 JSON**이며 AlphaFold Server 업로드 형식과 다릅니다. 아래 `/path/to/...`는 설치 위치와 접근 가능한 모델 파라미터 경로로 바꿔야 하는 자리표시자입니다. 설치·모델 접근·GPU 설정까지 해결해 주는 명령은 아닙니다. custom MSA와 빈 template를 이미 지정했으므로 아래는 데이터 검색을 끈 inference-only 형태입니다. [공식 입력 형식](https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md), [공식 실행 구분](https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md#featurisation-and-model-inference-only).

```sh
python /path/to/alphafold3/run_alphafold.py \
  --json_path="$PWD/prepared/alphafold3.json" \
  --model_dir=/path/to/af3/model_parameters \
  --output_dir="$PWD/results/af3" \
  --run_data_pipeline=false
```

AF3에는 seed 0·1·2가 전달되며 seed당 diffusion sample 수 등 나머지 설정은 설치된 버전의 기본값을 사용합니다. ColabFold와 반복 수·seed 의미가 같다고 간주하지 않습니다. 비교 시 도구/모델 버전, 샘플 수, 실제 MSA, template/ligand 조건, 구조의 잔기 대응과 같은 거리 지표를 기록합니다. pLDDT가 높거나 구조들이 일치한다는 사실만으로 특정 상태의 실험적 존재나 점유율이 증명되지는 않습니다.

문서와 CLI 형식 확인일: 2026-09-17. self-test는 허구 임시 자료로 파일 형식·경로·query·길이·기존 자료 보존을 확인하며, 실제 예측기 실행 성공을 검증하지 않습니다.

실제 서열 clustering 단계와 각 cluster의 구조 예측은 [AF-Cluster 실행 안내](afcluster_guide.md)를 참고하세요.
