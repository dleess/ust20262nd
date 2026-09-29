# 2강 · MSA와 단백질 구조 예측

생물학 배경 석사생을 위한 한국어 3시간 강의입니다. 1강의 구조 읽기에 이어, 진화 관계와 coevolution을 연결해 이해하고 MSA 입력을 비교하여 대안 구조 가설을 탐색합니다. 각 설명 직후 짧은 실습을 진행합니다.

## 강의 자료

- `output/msa_structure_prediction_3h_ko.pptx`: 편집 가능한 75장 강의. 발표자 노트에 설명·답안·출처가 있습니다.
- `output/msa_structure_prediction_3h_ko.pdf`: 같은 내용의 배포용 PDF.
- `output/msa_structure_prediction_worksheet_ko.pdf`: 학생 활동지 6쪽. 컴퓨터 없이도 가능합니다.
- `content/teacher_notes.md`: 강사용 진행·설명 노트. 활동지 해설은 `content/worksheet_answers.md`에 있습니다.
- `practice/README.md`: GPU 없이 실행하는 A3M 실습과 학생 문제·교사용 답안.
- `examples/colabfold_walkthrough.md`: 공식 노트북 접속부터 GPU·서열 입력·다운로드·custom MSA까지 단계별 브라우저 실습.
- `examples/afcluster_guide.md`: 실제 AF-Cluster clustering과 cluster별 ColabFold 실행 안내.
- `examples/README.md`: 실제 calmodulin 서열로 ColabFold·AF3를 사용하는 선택 시연 안내.

## 180분 진행표

| 시간 | 설명과 바로 실습 | 슬라이드 |
|---|---|---|
| 0–45분 | Ortholog/paralog → 계통수 실습 · A3M → 열 읽기 · coverage → 계산 | 1–19 |
| 45–55분 | Coevolution·보상적 제약·두 열의 빈도 → 계산 실습 | 20–23 |
| 55–65분 | 휴식 | 24 |
| 65–83분 | Ortholog의 계통 효과·paralog 혼합 → 해석 실습 · pairing·Neff | 25–31 |
| 83–99분 | 기본 예측 · ColabFold 접속·GPU·서열 입력·결과 저장 | 32–40 |
| 99–117분 | pLDDT 색·잔기별 그래프 → 실습 · PAE 기준·표·함께 읽기 → 실습 | 41–48 |
| 117–127분 | 휴식 | 49 |
| 127–146분 | Custom MSA · 공정한 비교 → 실습 · depth → 행 선택·웹 비교 | 50–58 |
| 146–171분 | Clustering → 그룹 실습 · masking → 열 가리기 실습 · 기법 비교 | 59–71 |
| 171–180분 | 입력 조건별 후보 판독 실습 · 설명과 정리 | 72–75 |

ColabFold 브라우저 실습은 슬라이드 36–40, 50, 58입니다. [공식 노트북 열기](https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb) · [상세 클릭 안내](examples/colabfold_walkthrough.md). 실제 예측은 단백질 길이·GPU·서버 대기에 따라 달라지므로, 슬라이드 시간은 설명과 조작 연습 시간입니다.

### 활동지 사용 시점

- 1쪽: ortholog/paralog 설명 직후, 슬라이드 9에서 풉니다.
- 2쪽: A3M 설명 직후, 슬라이드 16에서 풉니다. 행 중복 문항은 Neff 설명 직후 구두로 확인합니다.
- 3쪽: 빈도 계산은 슬라이드 23, 진화 관계와 계통 효과 해석은 슬라이드 27에서 나누어 풉니다.
- 4쪽: 비교 설계(53) → depth(56) → clustering(61) → masking(66) 순으로 해당 문항을 풉니다.
- 5쪽: pLDDT 설명 직후 슬라이드 44, PAE 설명 직후 슬라이드 48에서 나누어 풉니다.
- 6쪽: 슬라이드 72에서 MSA 조건별 후보를 신뢰도와 함께 판단합니다.

Coverage 계산은 슬라이드 18의 화면 예제로 진행합니다. 짧은 실습 시간에는 핵심 문항을 먼저 풀고 나머지는 교사 해설·확장 문항으로 사용합니다. `practice/student_questions.md`의 30분 문제는 수업 후 확장용이며 강의 마지막에 추가하는 일정이 아닙니다.

웹/GPU 대기 시간이 길면 실제 예측은 강의 전후에 실행합니다. 수업 중에는 종이 활동 또는 GPU 없는 A3M 실습으로 같은 개념을 확인할 수 있습니다. 실제 예측 도구의 실행 경로도 관련 설명 직후 시연하도록 배치했습니다.

## 수업의 핵심 구분

Ortholog와 paralog는 종 이름·서열 유사도보다 분기 사건을 기준으로 판단합니다. 두 열의 공변화(covariation)는 관측 패턴이고, coevolution은 진화적 제약의 연결을 묻습니다. Ortholog만 모아도 공통 조상 효과가 남으며, paralog 하위군을 섞으면 집단 간 차이가 두 열의 상관처럼 보일 수 있습니다. 단일 단백질 MSA를 무조건 ortholog만으로 제한하는 규칙은 없습니다. MSA의 서열 cluster는 물리적 구조 상태와 일대일 대응하지 않습니다. pLDDT는 잔기별 국소 정확도를 추정한 0–100 점수이고, PAE는 한 잔기의 국소 좌표계를 기준으로 다른 잔기 위치에 예상되는 오차(Å)입니다. 높은 pLDDT와 낮은 PAE가 각각 더 높은 모델 신뢰도를 뜻합니다. PAE는 잔기 사이 거리와 다르며, 방향에 따라 값이 다를 수 있습니다. 예측 개수의 비율과 pLDDT/PAE를 평형 점유율로 읽지 않습니다. AF2 기반 기법의 결과를 AF3에 적용할 때는 별도의 검증이 필요합니다.

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
