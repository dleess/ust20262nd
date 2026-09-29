# ColabFold 웹 실습 · 접속부터 MSA 조건 비교까지

목표는 **실제 CALM1 서열로 baseline 예측을 한 번 수행하고, 받은 MSA를 재사용하여 입력 조건을 비교하는 것**입니다. ColabFold의 AlphaFold2 노트북을 사용합니다. AlphaFold Server의 사용법이 아닙니다. `practice/fictional_learning.a3m`은 12열짜리 문법 예제이므로 여기에 제출하지 않습니다.

확인일: 2026-09-17. 공식 노트북은 **ColabFold v1.6.3**으로 표시됩니다. 아래 필드·선택지는 현재 노트북 코드: `https://github.com/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb`와 [Colab 공식 FAQ](https://research.google.com/colaboratory/faq.html)를 확인했습니다. 이 자료를 만드는 과정에서 Google 로그인이나 원격 예측을 실행하지는 않았습니다. 한국어 메뉴 표기는 언어 설정에 따라 다를 수 있어 영어 이름을 함께 적었습니다.

## 1. 어디로 들어가나요?

1. 아래 전체 URL을 복사해 브라우저 주소창에 붙여 넣습니다. 주소에 `sokrypton/ColabFold`와 `AlphaFold2.ipynb`가 있는지 확인합니다.

   ```text
   https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb
   ```
2. 실행을 위해 본인의 Google 계정으로 로그인합니다. 내용을 보관하려면 **File → Save a copy in Drive**(파일 → Drive에 사본 저장)를 사용할 수 있습니다. 사본 저장과 계산 결과 ZIP 저장은 별개입니다. [Google의 사본 저장 안내](https://github.com/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb)
3. **Runtime → Change runtime type**(런타임 → 런타임 유형 변경)를 엽니다. **Hardware accelerator**(하드웨어 가속기)에서 사용 가능한 GPU를 선택하고 저장합니다. T4가 제공되면 사용할 수 있지만, 특정 GPU 배정을 보장하지는 않습니다. 이 노트북은 GPU 런타임을 요구합니다. [공식 GPU 안내](https://research.google.com/colaboratory/faq.html)
4. 아래 입력과 설정을 먼저 채운 뒤 실행합니다. 아직 어떤 셀도 실행할 필요는 없습니다.

무료 GPU의 제공 여부·사용 한도·실행 시간은 일정하지 않습니다. GPU를 받지 못하면 강사가 준비한 결과를 읽거나 [오프라인 실습](../practice/README.md)을 진행합니다. 수업 시간 안에 완료될 것이라고 가정하지 않습니다.

## 2. 무엇을 붙여 넣나요?

예제 파일을 따로 받으려면 아래 **UniProt 공식 FASTA URL**을 브라우저 주소창에 입력합니다. 사람 calmodulin-1(CALM1), UniProt **P0DP23**입니다.

```text
https://rest.uniprot.org/uniprotkb/P0DP23.fasta
```

- 자동 다운로드되면 파일 이름을 `calmodulin_P0DP23.fasta`로 맞춥니다.
- 서열 텍스트가 화면에 보이면 **Ctrl+S / macOS Cmd+S**로 같은 이름으로 저장합니다. 최종 확장자가 `.fasta`인지 확인합니다.
- 첫 줄이 `>sp|P0DP23|CALM1_HUMAN`으로 시작하고 서열 길이가 149인지 확인합니다. HTML 페이지를 FASTA로 저장하지 않습니다.
- 파일 저장 없이 제목 줄 아래의 서열만 복사해 입력해도 됩니다. 수업 폴더의 `examples/calmodulin_P0DP23.fasta`도 같은 서열입니다.

첫 입력 셀의 **`query_sequence`**에 [calmodulin_P0DP23.fasta](calmodulin_P0DP23.fasta)의 **서열만** 붙여 넣습니다. `>sp|...`로 시작하는 설명 줄은 제외합니다. 이번 예제는 단량체이므로 `:`를 넣지 않습니다. 시작 Met를 포함해 149잔기입니다.

```text
MADQLTEEQIAEFKEAFSLFDKDGDGTITTKELGTVMRSLGQNPTEAELQDMINEVDADGNGTIDFPEFLTMMARKMKDTDSEEEIREAFRVFDKDGNGYISAAELRHVMTNLGEKLTDEEVDEMIREADIDGDGQVNYEEFVQMMTAK
```

첫 실행은 다음 설정으로 시작합니다.

| 위치 | 필드 | 첫 실행 값 |
|---|---|---|
| 첫 입력 셀 | `jobname` | `CALM1_baseline_01` |
| 첫 입력 셀 | `num_relax` | `0` |
| 첫 입력 셀 | `template_mode` | `none` |
| MSA options | `msa_mode` | `mmseqs2_uniref_env` |
| Advanced settings | `model_type` | `auto` |
| Advanced settings | `num_recycles` | `3` |
| Advanced settings | `recycle_early_stop_tolerance` | `auto` |
| Sample settings | `max_msa` | `auto` |
| Sample settings | `num_seeds` | `1` |
| Sample settings | `use_dropout` | 체크하지 않음 |

다른 설정은 기본값을 유지합니다. 단량체에서 `auto`는 `alphafold2_ptm`을 선택합니다. `pair_mode`는 이번 단량체 실습의 조작 변수가 아닙니다. `save_to_google_drive`는 선택 사항이며, 체크하면 별도 Google Drive 인증을 요구할 수 있습니다. 체크하지 않아도 결과 ZIP을 내려받을 수 있습니다. 설정과 실행 코드: `https://github.com/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb`

이 입력에는 calcium이나 결합 상대가 명시되어 있지 않습니다. 나온 모양을 특정 calcium 결합 상태의 재현으로 단정하지 않습니다. 서열 출처와 잔기 번호 주의점은 [실제 입력 안내](README.md#서열-출처)를 참고합니다.

## 3. 실행 버튼은 어디에 있나요?

1. 위쪽 메뉴에서 **Runtime → Run all**(런타임 → 모두 실행)을 누릅니다.
2. 처음 받은 노트북 실행 확인 창이 나오면, 방금 확인한 공식 노트북인지 확인하고 실행을 진행합니다.
3. 셀은 입력 처리 → 의존성 설치 → MSA 설정 → 고급 설정 → **Run Prediction** 순으로 실행됩니다. 처음에는 설치와 모델 파라미터 다운로드가 포함됩니다.
4. 첫 입력 셀 출력의 `length`가 **149**인지 확인합니다. MSA 검색 뒤에는 coverage 그림, 예측 과정에는 confidence 그림과 구조가 나타납니다.
5. 실행 중인 셀의 정지 아이콘은 계속 계산 중이라는 뜻입니다. 오류가 나면 오류 문구와 해당 셀을 기록하고 다음 단계로 넘어가지 않습니다. 입력을 바꾼 뒤에는 다시 **Run all**을 실행해야 값이 반영됩니다. 공식 실행 안내: `https://github.com/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb`

이 노트북의 현재 실행 코드는 모델 5개를 사용하며, `num_seeds=1`은 모델 하나만 만든다는 뜻이 아닙니다. 웹 폼에는 개별 `random_seed` 입력칸이 없습니다. 지정한 seed·모델 수를 엄밀히 맞추는 실습은 [로컬 CLI 안내](README.md#3-같은-colabfold-모델에서-msa-cap-비교)를 사용합니다.

## 4. 무엇을 내려받고 어디를 보나요?

마지막 **Package and download results** 셀이 `<jobname>.result.zip`을 내려받습니다. 브라우저가 다운로드를 막으면 Colab 왼쪽의 **폴더 아이콘**을 열고 해당 ZIP을 찾아 우클릭 → **Download**를 선택합니다. 여기서 `jobname`에는 서열에서 만든 짧은 해시와 충돌 방지 접미사가 붙을 수 있습니다. 공식 다운로드 코드: `https://github.com/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb`

ZIP을 `CALM1_baseline_01/`처럼 조건별 새 폴더에 풀고 다음 파일을 보관합니다. 기존 결과를 덮어쓰지 않습니다.

| 파일·화면 | 확인할 것 |
|---|---|
| `.a3m` | 이번 검색에서 얻은 실제 MSA. 이후 조건 비교의 원본으로 보관 |
| `*_unrelaxed_*.pdb` | 모델 좌표. 첫 실행은 `num_relax=0`이므로 unrelaxed 파일 사용 |
| `*_coverage.png` | 어느 잔기 구간에 homolog 정보가 있는가 |
| `*_plddt.png` | 어느 구간의 국소 confidence가 낮은가 |
| `*_pae.png`, `*_scores_*.json` | 구간 간 상대 배치의 불확실성. 실제 오차 측정값은 아님 |
| 설정·로그·인용 파일 | 모델/버전, 입력, 설정, 사용한 도구 기록 |

화면의 **Display 3D structure**에서 `rank_num`을 바꾸어 후보를 비교합니다. `color=lDDT`는 confidence를 색으로 보여 줍니다. CALM1 두 부분의 모양이 각각 그럴듯해도 두 부분 사이의 배치가 확실한지는 PAE를 함께 보아야 합니다. 후보의 수나 rank를 물리적 상태의 점유율로 읽지 않습니다.

### 결과 화면의 pLDDT와 PAE 읽기

`*_plddt.png`는 가로축이 잔기 번호, 세로축이 0–100 점수입니다. 관심 부위의 값과 구간별 차이를 확인합니다. 전체 평균이 높아도 특정 loop·연결부의 신뢰도는 낮을 수 있습니다. 보통 90 이상은 매우 높음, 70–90은 대체로 믿을 만한 골격, 50–70은 낮음, 50 미만은 매우 낮은 신뢰도로 읽되 이를 절대적 경계로 쓰지는 않습니다. 낮은 점수만으로 disorder나 움직임을 확정하지 않습니다. [공식 pLDDT 해설](https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/)

lDDT와 pLDDT는 구별합니다. lDDT-Cα는 기준 구조와 예측 구조에서 같은 Cα쌍의 거리가 얼마나 보존되는지 직접 채점한 값입니다. AF2는 학습 중 이 값을 계산해 신뢰도 head의 정답으로 사용하고, 새 표적에서는 정답 구조 없이 잔기별 lDDT 구간 분포를 예측합니다. 그 확률가중 평균을 100점 척도로 표시한 것이 pLDDT입니다. 여러 seed의 모델이 서로 비슷한 정도로 계산한 값이 아닙니다. 직접 계산과 학습·추론 차이는 강의 50–57번 및 활동지 5쪽에서 다룹니다. [AF2 공식 학습 구현](https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/modules.py#L998-L1089) · [점수 출력 구현](https://github.com/google-deepmind/alphafold/blob/main/alphafold/common/confidence.py)

`*_pae.png`는 두 잔기 위치를 축으로 갖는 표입니다. 축 설명과 색 범례를 먼저 읽습니다. PAE(i,j)는 j의 국소 좌표계에 맞췄다고 가정할 때 i의 예상 위치 오차이며, 단위는 Å입니다. 잔기 사이 거리가 아니고 실제 정답과 비교해 측정한 값도 아닙니다. 강의 표는 행=i, 열=j로 정했으며 실제 뷰어는 축 표기를 확인해야 합니다. 도메인 내부 블록과 두 도메인 사이의 양방향 블록을 따로 봅니다. 내부 PAE가 낮아도 도메인 사이 PAE가 높으면 상대 배치는 불확실할 수 있습니다. [공식 PAE 해설](https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/)

활동지 6쪽의 예제는 이러한 읽기 방법을 익히기 위한 가상 수치이며 CALM1 예측 결과가 아닙니다. 낮은 PAE·높은 pLDDT도 실제 결합이나 상태 점유율을 보장하지 않습니다.

## 5. 원본 MSA를 다시 검색하지 않고 쓰는 법

비교의 출발점은 **같은 검색 결과 파일**입니다. baseline ZIP의 CALM1 `.a3m`을 별도 원본으로 보존하고, 수정 조건은 복사본에 만듭니다.

1. `jobname`을 `CALM1_custom_full_01`처럼 새 이름으로 바꿉니다. `query_sequence`에는 같은 149잔기 서열을 유지합니다.
2. **MSA options**의 `msa_mode`를 **`custom`**으로 바꿉니다. `template_mode=custom`과 혼동하지 않습니다. Template는 계속 `none`입니다.
3. 다른 설정을 baseline과 맞추고 **Runtime → Run all**을 누릅니다.
4. **MSA options 셀이 실행될 때** 그 아래에 업로드 창이 나타납니다. 실제 원본 `.a3m` **한 파일만** 선택합니다. 드롭다운 값만 바꾸고 실행하지 않으면 업로드 창이 나오지 않습니다.
5. 업로드가 끝나면 예측과 ZIP 다운로드까지 진행합니다. Custom MSA 처리 코드: `https://github.com/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb`

**중요한 확인:** 업로드한 A3M의 첫 서열이 query가 됩니다. 현재 코드는 이 첫 서열로 `query_sequence`를 다시 설정하므로, 입력칸이 맞더라도 엉뚱한 첫 서열을 업로드하면 표적이 바뀝니다. 첫 서열을 gap 없는 대문자 149잔기 한 줄로 유지하고, 제공 FASTA와 정확히 같은지 확인합니다. Homolog의 소문자 insertion과 `-`를 임의로 지우거나 대문자로 바꾸지 않습니다.

로컬에서 확인할 수 있으면 `AIprediction/`에서 아래 입력 검사를 실행합니다. `target.a3m`은 방금 받은 실제 파일의 복사본 이름입니다. 이 명령은 예측을 하지 않으며, 기존 `checked_full` 폴더가 있으면 새 이름을 사용해야 합니다.

```sh
python3 examples/prepare_inputs.py examples/calmodulin_P0DP23.fasta target.a3m --out checked_full
```

## 6. 설명을 듣고 바로 한 조건씩 바꾸기

한 번에 한 요소만 바꿉니다. 매번 새 `jobname`으로 실행하고 ZIP·입력 A3M·설정을 함께 보관합니다. 강의의 웹 비교에서는 `model_type=alphafold2_ptm`, `num_recycles=3`, `num_seeds=1`, `use_dropout` 해제, `template_mode=none`으로 고정하고 `recycle_early_stop_tolerance=auto`를 유지합니다. 먼저 같은 원본 custom MSA에서 `max_msa=64:128` 조건을 실행한 다음 `32:64`와 비교합니다.

| 설명 직후 | 실제 ColabFold 조작 | 관찰·기록 |
|---|---|---|
| Depth | 같은 원본을 `custom` 업로드. **Advanced settings → Sample settings → `max_msa`**를 `64:128`에서 `32:64`로 바꾸기 | 같은 query·원본 MSA를 사용했는가? cap, 실제 행 수, coverage, 구조·PAE 기록 |
| Clustering | 실제 MSA를 외부에서 clustering한 뒤, query를 첫 행에 둔 cluster `.a3m` 하나를 `custom` 업로드 | cluster ID·포함 서열·행 수 기록. 구조 상태나 ortholog 집합이라는 뜻은 아님 |
| Masking | 실제 MSA 복사본의 선택 homolog 정렬 열을 X로 가린 파일을 검증한 뒤 `custom` 업로드 | query·insertion·gap 보존, 가린 열·비율·방법 기록 |

`max_msa`의 현재 UI 선택지는 **`auto`, `512:1024`, `256:512`, `64:128`, `32:64`, `16:32`**입니다. `32:64`는 대표 MSA/extra MSA의 상한 설정이며, 원본 파일에서 32행을 직접 뽑는 명령이 아닙니다. 원본이 얕으면 cap을 바꿔도 유효 입력이 같을 수 있습니다. 로컬 CLI에서 사용하는 `128:256`은 현재 이 드롭다운의 선택지가 아닙니다. 현재 선택지와 전달 코드: `https://github.com/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb`

ColabFold 폼에는 AF-Cluster 실행 버튼이나 임의 열 X 마스킹 버튼이 없습니다. 실제 clustering은 [AF-Cluster 실행 안내](afcluster_guide.md)로 별도 수행합니다. 이 자료의 `practice/msa_lab.py`는 허구 A/B 라벨을 요구하는 문법 실습이므로 실제 CALM1 MSA 처리에 그대로 사용하지 않습니다. X로 가린 파일 업로드는 입력 조작을 비교하는 것이며 AFsample2 전체 방법을 재현한 것은 아닙니다.

Clustering·masking 비교에서는 `max_msa`를 원본 custom 조건과 같게 맞춥니다. `model_type`, `num_recycles`, `recycle_early_stop_tolerance`, `num_seeds`, `use_dropout`, template 조건도 유지합니다. 여러 cluster를 돌리면 총 생성 모델 수가 늘어나므로, 그에 맞춘 baseline 반복도 필요합니다. 구조가 달라졌다는 관찰과 그 구조가 실제 상태라는 주장을 구분합니다.

## 실행 기록

`jobname` / 실행 날짜 / ColabFold 버전 / query 길이 / MSA 파일명·검색 출처 / query 포함 행 수 / `max_msa` / `num_seeds` / recycle·dropout·template 설정 / ZIP 저장 위치 / 관찰한 구조 차이와 PAE를 기록합니다.

문제가 생기면 ColabFold 공식 README: `https://github.com/sokrypton/ColabFold`와 노트북의 Instructions를 확인합니다. 계산 자원 문제는 [Colab FAQ](https://research.google.com/colaboratory/faq.html)를 확인합니다. 오래된 안내의 메뉴명이나 결과를 지우는 초기화 절차를 그대로 따라 하기 전에 입력과 결과 ZIP을 보관합니다.
