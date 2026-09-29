# 2강 · MSA와 단백질 구조 예측

생물학 배경 석사생을 위한 한국어 3시간 강의입니다. 1강의 구조 읽기에 이어, 먼저 AlphaFold 입력에서 MSA의 역할과 보존·공변화 예제를 살펴봅니다. 이어 진화 관계와 coevolution을 연결해 이해하고 MSA 입력을 비교하여 대안 구조 가설을 탐색합니다. 각 설명 직후 짧은 실습을 진행하고, 바로 다음 강의 화면에서 정답·해설을 확인합니다.

## 강의 자료

- `output/msa_structure_prediction_3h_ko.pptx`: 편집 가능한 102장 강의. 문제 바로 뒤에 정답·해설이 있고 발표자 노트에 보충 설명·출처가 있습니다.
- `output/msa_structure_prediction_3h_ko.pdf`: 같은 내용의 배포용 PDF.
- `output/msa_structure_prediction_worksheet_ko.pdf`: 정답을 채우지 않은 학생 활동지 7쪽. 컴퓨터 없이도 가능합니다.
- `content/teacher_notes.md`: 강사용 진행·설명 노트. 활동지 해설은 `content/worksheet_answers.md`에 있습니다.
- `practice/README.md`: GPU 없이 실행하는 A3M 실습과 학생 문제·교사용 답안.
- `examples/colabfold_walkthrough.md`: 공식 노트북 접속부터 GPU·서열 입력·다운로드·custom MSA까지 단계별 브라우저 실습.
- `examples/afcluster_guide.md`: 실제 AF-Cluster clustering과 cluster별 ColabFold 실행 안내.
- `examples/README.md`: 실제 calmodulin 서열로 ColabFold·AF3를 사용하는 선택 시연 안내.

예제 FASTA 다운로드(P0DP23, human CALM1, 149 aa): 아래 주소에서 받아 `calmodulin_P0DP23.fasta`로 저장합니다. 자세한 저장·입력 방법은 슬라이드 46 및 `examples/colabfold_walkthrough.md`에 있습니다.

```text
https://rest.uniprot.org/uniprotkb/P0DP23.fasta
```

공진화가 구조 정보를 주는 이유는 슬라이드 4의 MSA → 구조 추론 그림과 슬라이드 29의 측쇄 전하 조합 그림으로 설명합니다. 그림은 PowerPoint에서 편집 가능한 도식이며 가상 예시입니다.

## 180분 진행표

| 시간 | 설명과 바로 실습 | 슬라이드 |
|---|---|---|
| 0–7분 | AlphaFold에서 MSA의 위치 · 보존·공변화 예제 · 왜 진화를 배우는가 | 1–4 |
| 7–47분 | Ortholog/paralog → 계통수 실습 · A3M → 열 읽기 · coverage → 계산·해설 | 5–27 |
| 47–57분 | Coevolution·보상적 제약·두 열의 빈도 → 계산 실습·해설 | 28–32 |
| 57–67분 | 휴식 | 33 |
| 67–82분 | Ortholog의 계통 효과·paralog 혼합 → 해석 실습·해설 · pairing·Neff | 34–40 |
| 82–95분 | 기본 예측 · ColabFold 접속·GPU·서열 입력·결과 저장·실행 확인 | 41–49 |
| 95–104분 | lDDT 직접 계산 → 실습·해설 · pLDDT의 학습 정답·추론 과정 | 50–55 |
| 104–120분 | pLDDT 색·잔기별 그래프 → 실습·해설 · PAE 표·함께 읽기 → 실습·해설 | 56–65 |
| 120–130분 | 휴식 | 66 |
| 130–149분 | Custom MSA · 공정한 비교 → 실습·해설 · depth → 행 선택·웹 비교·확인 | 67–79 |
| 149–171분 | Clustering → 그룹 실습·해설 · masking → 열 가리기 실습·해설 · 기법 비교 | 80–95 |
| 171–180분 | 입력 조건별 후보 판독 실습·해설 · 설명과 정리 | 96–102 |

풀이와 해설 시간을 나누어 배치했으며 총 180분(휴식 20분 포함)은 유지합니다. 분 단위 진행표는 이 문서와 강사 노트를 사용합니다.

ColabFold 브라우저 실습과 실행 확인은 슬라이드 44–49, 67–68, 78–79입니다. 공식 노트북 주소를 복사해 브라우저 주소창에 입력하세요.

```text
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb
```

[상세 실행 안내](examples/colabfold_walkthrough.md). 실제 예측은 단백질 길이·GPU·서버 대기에 따라 달라지므로, 슬라이드 시간은 설명과 조작 연습 시간입니다.

### 문제 → 정답·해설 찾기

학생 활동지의 빈칸은 유지합니다. 화면의 문제를 먼저 푼 뒤 바로 다음 정답·해설을 확인합니다. ColabFold에는 실행 결과를 확인하는 화면이 이어집니다.

| 활동·자료 | 문제 또는 실행 슬라이드 | 바로 다음 정답·해설 |
|---|---:|---:|
| Ortholog/paralog · 활동지 1쪽 | 12 | 13–14 |
| A3M · 활동지 2쪽 | 21 | 22–23 |
| Coverage/identity · 화면 예제 | 25 | 26 |
| 공동 빈도 · 활동지 3쪽 | 31 | 32 |
| 계열과 공진화 · 활동지 3쪽 | 36 | 37 |
| ColabFold 기본 결과 저장 | 48 | 49 |
| lDDT 거리 변경 · 활동지 5쪽 | 52 | 53 |
| pLDDT · 활동지 6쪽 | 58 | 59 |
| PAE · 활동지 6쪽 | 63 | 64–65 |
| Custom MSA 업로드 | 67 | 68 |
| 공정한 비교 · 활동지 4쪽 | 71 | 72 |
| Depth · 활동지 4쪽 | 75 | 76 |
| ColabFold depth 비교 | 78 | 79 |
| Clustering · 활동지 4쪽 | 82 | 83 |
| Masking · 활동지 4쪽 | 88 | 89–90 |
| 후보 판독 · 활동지 7쪽 | 96 | 97–98 |
| 최종 설명 활동 · 화면 문제 | 99 | 100 |

활동지 5쪽 표는 슬라이드 51의 lDDT 계산 설명과 함께 채웁니다. 거리 변경은 52–53에서 풀이·해설을 합해 1분으로 진행합니다. pLDDT 학습·추론 확장 문항은 54–55 뒤에 선택합니다. 활동지 2쪽의 행 중복 문항은 Neff 설명(40) 직후 구두로 확인합니다. 짧은 실습 시간에는 핵심 문항을 먼저 풀고 나머지는 교사 해설·확장 문항으로 사용합니다. `practice/student_questions.md`의 30분 문제는 수업 후 확장용이며 강의 마지막에 추가하는 일정이 아닙니다.

웹/GPU 대기 시간이 길면 실제 예측은 강의 전후에 실행합니다. 수업 중에는 종이 활동 또는 GPU 없는 A3M 실습으로 같은 개념을 확인할 수 있습니다. 실제 예측 도구의 실행 경로도 관련 설명 직후 시연하도록 배치했습니다.

## 수업의 핵심 구분

Ortholog와 paralog는 종 이름·서열 유사도보다 분기 사건을 기준으로 판단합니다. 두 열의 공변화(covariation)는 관측 패턴이고, coevolution은 진화적 제약의 연결을 묻습니다. Ortholog만 모아도 공통 조상 효과가 남으며, paralog 하위군을 섞으면 집단 간 차이가 두 열의 상관처럼 보일 수 있습니다. 단일 단백질 MSA를 무조건 ortholog만으로 제한하는 규칙은 없습니다. MSA의 서열 cluster는 물리적 구조 상태와 일대일 대응하지 않습니다. lDDT는 기준 구조와 예측 구조의 국소 거리 보존을 직접 평가합니다. AF2는 잔기별 lDDT-Cα를 학습 정답으로 삼아 50개 점수 구간을 예측하도록 신뢰도 head를 학습합니다. 추론에서는 기준 구조 없이 구간 확률의 가중평균을 계산하여 pLDDT를 출력합니다. pLDDT는 잔기별 국소 정확도를 추정한 0–100 점수이고, PAE는 한 잔기의 국소 좌표계를 기준으로 다른 잔기 위치에 예상되는 오차(Å)입니다. 높은 pLDDT와 낮은 PAE가 각각 더 높은 모델 신뢰도를 뜻합니다. PAE는 잔기 사이 거리와 다르며, 방향에 따라 값이 다를 수 있습니다. 예측 개수의 비율과 pLDDT/PAE를 평형 점유율로 읽지 않습니다. AF2 기반 기법의 결과를 AF3에 적용할 때는 별도의 검증이 필요합니다.

`practice/`의 정렬과 비교 숫자는 모두 명시된 가상 학습 자료입니다. 실제 예측 결과가 아닙니다. `examples/calmodulin_P0DP23.fasta`는 UniProt에서 가져온 실제 인간 calmodulin-1 서열입니다. 실제 예측은 설치된 모델·가중치·적합한 계산 환경에서 별도로 실행해야 합니다.

## 수정과 재생성

원본 슬라이드 내용은 `content/evolution_msa.json`, `content/coevolution.json`, `content/core_workflow.json`, `content/alternative_methods.json`, `content/confidence.json`에 있습니다. 출처는 같은 폴더의 다섯 `*_sources.json` 파일에서 수정합니다. 합본 JSON·노트는 생성 파일입니다.

```sh
cd AIprediction
python3 build/build_deck.py
python3 build/build_worksheet.py
osascript build/export_pdf.applescript "$PWD/build/msa_structure_prediction_3h_ko.pptx" "$PWD/build/msa_structure_prediction_3h_ko.pdf"
python3 build/verify_materials.py
```

Python 의존성은 기존 1강과 같은 `python-pptx`, Pillow, PyMuPDF입니다. 글꼴은 `/Library/Fonts/Arial Unicode.ttf`와 시스템 Courier New를 사용합니다. PDF 강의본은 macOS Microsoft PowerPoint로 내보냅니다. `build/`에는 소스 코드가 포함되어 있으므로 통째로 정리하지 않습니다. 다시 만든 자료는 PDF 렌더링을 확인한 뒤 `output/`에 복사합니다. 이전 버전은 `archive/` 또는 `build/archive/`에 보관합니다.

논문 그림 원본과 CC BY 4.0 출처는 `assets/figures/attribution.json`에 기록했습니다. 강의 슬라이드는 해당 그림의 패널을 확대해 표시합니다. 도구 문서 확인일: 2026-09-17.
