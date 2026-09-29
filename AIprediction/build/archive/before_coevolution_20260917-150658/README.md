# 2강 · MSA와 단백질 구조 예측

생물학 배경 석사생을 위한 한국어 3시간 강의입니다. 1강의 구조 읽기에 이어, 진화 관계를 이해하고 MSA 입력을 비교하여 대안 구조 가설을 탐색합니다.

## 강의 자료

- `output/msa_structure_prediction_3h_ko.pptx`: 편집 가능한 62장 강의. 발표자 노트에 설명·답안·출처가 있습니다.
- `output/msa_structure_prediction_3h_ko.pdf`: 같은 내용의 배포용 PDF.
- `output/msa_structure_prediction_worksheet_ko.pdf`: 학생 활동지 4쪽. 컴퓨터 없이도 가능합니다.
- `content/teacher_notes.md`: 강사용 진행·설명 노트. 활동지 해설은 `content/worksheet_answers.md`에 있습니다.
- `practice/README.md`: GPU 없이 실행하는 A3M 실습과 학생 문제·교사용 답안.
- `examples/afcluster_guide.md`: 실제 AF-Cluster clustering과 cluster별 ColabFold 실행 안내.
- `examples/README.md`: 실제 calmodulin 서열로 ColabFold·AF3·Boltz·Chai·ESMFold를 사용하는 선택 시연 안내.

## 180분 진행표

| 시간 | 내용 | 슬라이드 |
|---|---|---|
| 0–55분 | Homology, ortholog/paralog, 유전자 중복·종분화, 계통수, MSA 읽기 | 1–22 |
| 55–65분 | 휴식 | 23 |
| 65–85분 | 기본 예측, custom MSA, AF2·AF3 및 다른 도구, 대조 조건 | 24–30 |
| 85–130분 | Depth, AF-Cluster, masking, SPEACH_AF·AFsample2, 결과 해석 | 31–48 |
| 130–140분 | 휴식 | 49 |
| 140–180분 | 진화·MSA 실습, 실행 시연, 가상 결과 판단, 정리 | 50–62 |

`practice/student_questions.md`의 전체 30분 문제는 확장 실습으로도 사용할 수 있습니다. 3시간 수업에서는 활동지의 핵심 문항을 선택하고 마지막 40분에 교사 시연과 함께 진행합니다. 웹/GPU 대기 시간이 길면 실제 예측은 강의 전후에 실행하고, 수업 중에는 A3M 실습과 결과 판독을 진행합니다.

## 수업의 핵심 구분

Ortholog와 paralog는 종 이름·서열 유사도보다 분기 사건을 기준으로 판단합니다. MSA의 서열 cluster는 물리적 구조 상태와 일대일 대응하지 않습니다. 예측 개수의 비율과 pLDDT/PAE를 평형 점유율로 읽지 않습니다. AF2 기반 기법의 결과를 AF3에 적용할 때는 별도의 검증이 필요합니다.

`practice/`의 정렬과 비교 숫자는 모두 명시된 가상 학습 자료입니다. 실제 예측 결과가 아닙니다. `examples/calmodulin_P0DP23.fasta`는 UniProt에서 가져온 실제 인간 calmodulin-1 서열입니다. 실제 예측은 설치된 모델·가중치·적합한 계산 환경에서 별도로 실행해야 합니다.

## 수정과 재생성

원본 슬라이드 내용은 `content/evolution_msa.json`, `content/core_workflow.json`, `content/alternative_methods.json`에 있습니다. 출처는 같은 폴더의 세 `*_sources.json` 파일에서 수정합니다. 합본 JSON·노트는 생성 파일입니다.

```sh
cd AIprediction
python3 build/build_deck.py
python3 build/build_worksheet.py
osascript build/export_pdf.applescript "$PWD/build/msa_structure_prediction_3h_ko.pptx" "$PWD/build/msa_structure_prediction_3h_ko.pdf"
python3 build/verify_materials.py
```

Python 의존성은 기존 1강과 같은 `python-pptx`, Pillow, PyMuPDF입니다. 글꼴은 `/Library/Fonts/Arial Unicode.ttf`와 시스템 Courier New를 사용합니다. PDF 강의본은 macOS Microsoft PowerPoint로 내보냅니다. `build/`에는 소스 코드가 포함되어 있으므로 통째로 정리하지 않습니다. 다시 만든 자료는 PDF 렌더링을 확인한 뒤 `output/`에 복사합니다. 이전 버전은 `archive/` 또는 `build/archive/`에 보관합니다.

논문 그림 원본과 CC BY 4.0 출처는 `assets/figures/attribution.json`에 기록했습니다. 강의 슬라이드는 해당 그림의 패널을 확대해 표시합니다. 도구 문서 확인일: 2026-09-17.
