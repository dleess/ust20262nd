# 3강 · Molecular dynamics(MD) 입문

생물학 배경 석사생을 위한 60분 개념 강의입니다. 설명은 한국어로, 전문용어는 영어로 씁니다. 1강에서 잰 2ITY의 거리(Met793 N – gefitinib N3, 2.670 Å)가 물속에서도 유지될지 묻는 데서 출발해, 이어지는 2시간 실습 전에 MD의 원리와 준비 순서, 결과 읽는 법을 다룹니다.

## 강의 자료

- `output/md_intro_1h_ko.pptx`: 편집 가능한 23장 강의. 발표자 노트에 설명과 출처가 있습니다.
- `output/md_intro_1h_ko.pdf`: 같은 내용의 배포용 PDF.
- `content/teacher_notes.md`: 강사용 진행 노트(빌더가 생성).

## 60분 진행표

| 시간 | 내용 | 슬라이드 |
|---|---|---|
| 0–4분 | 오늘의 질문 · 1·2·3강 연결 | 1–2 |
| 4–13분 | 시간 척도 · force field · MD 반복 | 3–5 |
| 13–33분 | 계산 상자 · NVT와 NPT · 준비 4단계 → 실습 ①과 해설 · NVT 다음 NPT인 이유 → 실습 ②와 해설 | 6–13 |
| 33–48분 | RMSD · RMSF · 거리와 H-bond → 실습 ③과 해설 | 14–18 |
| 48–57분 | MD의 한계 · 최종 활동과 해설 | 19–21 |
| 57–60분 | 2시간 실습 연결 · 참고 자료 | 22–23 |

RMSD·RMSF 그래프와 실습 ③의 10 frame은 가상 교육용 데이터입니다. 명령 이름과 기본값은 GROMACS 기준입니다.

## 수정과 재생성

슬라이드 원고는 `content/md_intro.json`, 출처는 `content/sources.json`에서 고칩니다.

```sh
cd MDintro
python3 build/build_deck.py
osascript build/export_pdf.applescript "$PWD/build/md_intro_1h_ko.pptx" "$PWD/build/md_intro_1h_ko.pdf"
```

빌더는 60분 구성, 실습 바로 다음 장의 정답 배치, 핵심 용어가 설명 슬라이드보다 먼저 나오지 않는지, H-bond 실습 값과 정답의 일치, 글자 넘침 추정치와 슬라이드 경계를 검사합니다. 의존성은 1·2강과 같은 python-pptx와 Pillow이고, 글꼴은 `/Library/Fonts/Arial Unicode.ttf`를 씁니다. PDF는 macOS Microsoft PowerPoint로 내보내고, 렌더링을 확인한 뒤 `output/`에 복사합니다.
