# 오프라인 MSA 실습

필요한 것은 Python 3.8 이상과 이 폴더뿐입니다. 인터넷, GPU, 설치 패키지가 필요 없습니다. 검색·학습·구조 예측을 실행하지 않습니다.

**`fictional_learning.a3m`은 문법 학습을 위해 만든 12열·7행의 허구 데이터입니다. 실제 단백질이나 상동서열 검색 결과가 아니며 예측 표적으로 쓰지 않습니다.** 첫 행은 query, 나머지 행은 homolog 역할을 하는 예시입니다. `synthetic_comparison.json`도 사람이 만든 숫자이며 실제 예측·실험 결과가 아닙니다. 비교표의 가상 180잔기 표적은 A3M의 12잔기 문자열과 별개입니다.

## 실행

저장소 루트에서 실행합니다.

```sh
cd AIprediction/practice
sh run_practice.sh
```

`SELF-TEST PASS`와 `출력/저장 검증 완료`가 표시됩니다. 결과는 매번 새 `runs/날짜_시간/` 폴더에 저장됩니다. 입력 파일과 기존 폴더는 덮어쓰지 않습니다. Windows에서는 다음 두 명령을 실행합니다.

```sh
python msa_lab.py --self-test
python msa_lab.py
```

설정을 직접 바꾸려면 다음과 같이 실행합니다. `--depth`는 **query를 포함한 행 수**입니다. `--seed`는 **행 추출 seed**이며 예측 seed가 아닙니다. `--out`에 이미 존재하는 폴더를 지정하면 종료 코드 2로 거부합니다.

```sh
python3 msa_lab.py --depth 4 --seed 7 --mask-columns 5,7,10 --out runs/demo01
python3 msa_lab.py --depth 2 --seed 11 --mask-columns 4,5 --out runs/demo02
python3 -m json.tool runs/demo01/report.json
python3 -m json.tool synthetic_comparison.json
```

재실행은 새 폴더 이름을 사용하거나 `--out`을 생략합니다. 결과를 지우기보다 보관합니다.

## 출력 파일 읽기

| 파일 | 의미 |
|---|---|
| `report.json` | 원본/정렬 문자열, gap/X 개수, 소문자 삽입 길이, 입력 SHA-256, 설정, 출력별 행 ID |
| `subsample.a3m` | query 1행 + 무작위 homolog 3행(default); 원래 행 순서를 유지 |
| `group_A.a3m`, `group_B.a3m` | header의 사전 지정 `group=A/B` 라벨별 분리 + 동일 query |
| `masked.a3m` | homolog의 지정 정렬 열을 `X`로 바꾼 자료; query·소문자·gap 보존 |

`ACDeeEFGHIKLMN`은 원문 14글자지만 정렬 열은 12개입니다. `ee`는 query 기준 삽입이므로 정렬 행렬의 새 열이 아닙니다. `report.json`은 각 정렬 열 직전의 소문자 길이와 끝부분 삽입 길이를 따로 기록합니다. `-`는 해당 정렬 위치의 gap, `X`는 아미노산 정체가 알려지지 않았거나 이 실습에서 가린 위치입니다. `X`도 열 하나를 차지합니다. 소문자를 대문자로 변환하거나 `-`와 `X`를 서로 바꾸면 의미가 달라집니다.

열 번호는 첫 query 잔기를 1로 셉니다. 기본 masking은 5·7·10열의 **homolog 대문자 잔기만 `X`로 치환**합니다. 기존 `X`는 그대로이며, 선택 열이 `-`면 유지합니다. 이것은 정렬을 보존하는 문자열 조작 연습이고 예측기 내부의 mask token과 같은 연산이라고 가정하지 않습니다.

**A/B는 임의의 수업 라벨입니다.** 거리 계산, 군집 추정, 진화 계통 추정이나 AF-Cluster 알고리즘을 구현하지 않습니다. 두 그룹을 닫힘/열림 구조 상태로 해석할 수 없습니다. 마스킹도 AFsample2를 재현하는 구현이 아닙니다. 정해진 열 선택은 정보를 줄이는 개념을 눈으로 확인하려는 교육적 단순화입니다.

## 수업 순서와 한계

정규 3시간 강의에서는 각 설명 직후 활동지를 풉니다. A3M 설명 뒤 활동지 2쪽, coevolution 설명 뒤 3쪽, depth·clustering·masking 설명 뒤 4쪽의 해당 문항, confidence·구조 비교 설명 뒤 5쪽을 사용합니다. 진화 관계 활동은 1쪽입니다. 강사는 `../content/worksheet_answers.md`를 별도로 사용합니다.

Depth 단계에서 스크립트를 한 번 실행하고 `subsample.a3m`을 확인합니다. Clustering 단계에서는 같은 출력 폴더의 `group_A/B.a3m`, masking 단계에서는 `masked.a3m`을 이어서 읽습니다. 세 종류 파일은 모두 원본 7행에서 각각 생성한 조건이며, 앞 조건의 결과에 다음 조작을 누적한 것이 아닙니다. 컴퓨터가 없으면 출력한 A3M에 손으로 표시합니다.

`student_questions.md`는 수업 후 확장용 30분 문제입니다(문법 8분·입력 조작 12분·결과 해석 10분). 정규 수업 마지막에 이 30분을 추가하는 일정이 아닙니다. 상세 답은 `instructor_answers.md`에 있습니다. Coevolution 활동지 3쪽 A/B에는 가상 진화 이력이 주어져 있지만, 이 폴더의 `group=A/B` 라벨에는 그런 근거가 없습니다.

이 파서는 단일 단백질 교육용 부분집합만 지원합니다. 20개 표준 아미노산+`X`의 대·소문자와 `-`를 허용하고, query에는 소문자와 gap을 허용하지 않습니다. 여러 줄 FASTA는 허용합니다. `.` insertion padding, 다른 모호 문자, `#` 복합체 메타데이터, paired/multimer A3M은 의도적으로 오류를 냅니다. 범용 A3M 변환기로 사용하지 않습니다. 모든 homolog는 A/B 라벨 하나를 가져야 합니다.

원시 행 수는 서열 다양성이나 유효 서열 수(Neff)와 다릅니다. 같은 query와 같은 전처리 seed를 유지하면 입력 조작을 비교할 수 있지만 실제 예측은 모델·버전·예측 seed·template·recycle·MSA 설정까지 기록해야 합니다. 작은 MSA 또는 masking이 대체 구조를 보장하지 않습니다. 가상 비교표는 pLDDT 하나만으로 상태를 선택하지 않고 거리·PAE·독립 근거를 함께 검토하는 연습용입니다.

## 형식 근거

- [AlphaFold 공식 `parse_a3m`](https://github.com/google-deepmind/alphafold/blob/main/alphafold/data/parsers.py): 첫 행 query, 소문자 제외 정렬 문자열, 삽입 길이 처리의 기준을 확인했습니다.
- [ColabFold 공식 README](https://github.com/sokrypton/ColabFold): 실제 도구의 MSA 생성·예측 실행 안내입니다.
- [ColabFold 공식 배치 노트북](https://github.com/sokrypton/ColabFold/blob/main/batch/AlphaFold2_batch.ipynb): `.a3m` custom MSA 입력을 안내합니다. 이 실습의 허구 파일을 제출하라는 뜻은 아닙니다.
- [EMBL-EBI의 AlphaFold confidence 해설](https://www.ebi.ac.uk/training/online/courses/analysing-evaluating-macromolecular-models/global-quality-assessment/key-global-validation-metrics/metrics-based-on-experimental-data-fit/key-things-alphafold/): pLDDT는 국소 신뢰도, PAE는 상대적 배치의 예상 오차를 해석하는 지표입니다.

공식 자료 확인일: 2026-09-17. 이 폴더에는 실제 predictor나 그 의존성을 설치하지 않습니다.
