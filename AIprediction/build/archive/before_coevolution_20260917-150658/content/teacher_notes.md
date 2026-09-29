# MSA와 단백질 구조 예측 · 강사용 노트

총 180분, 휴식 20분 포함. 활동 답안은 이 강사용 노트와 practice/instructor_answers.md에 수록합니다.

## 1. MSA와 단백질 구조 예측 (0–1분)

이 강의에서는 생물학에서 익숙한 공통 조상과 유전자 중복을 출발점으로 삼습니다. 먼저 ortholog와 paralog를 사건에 따라 구분하고, 실제 파일처럼 보이는 짧은 정렬을 직접 읽겠습니다. 이후에는 MSA의 어떤 정보를 바꾸면 구조 예측 결과가 달라질 수 있는지 살펴봅니다. 교육용 가상 서열과 가상 계통수는 개념 학습용이며 실제 단백질이나 실제 진화 역사를 나타내지 않습니다.

[evo_ebi_msa] EMBL-EBI Training: Multiple sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/multiple-sequence-alignment/

## 2. Homology: 얼마나 닮았나보다 어디에서 왔나 (1–3분)

상동성은 두 서열의 진화적 기원에 대한 관계이고, 동일성은 정렬에서 측정하는 양입니다. 실제 분석에서는 상동 여부의 근거가 강하거나 약할 수 있지만, 상동성을 백분율로 표시하지 않습니다. 높은 서열 동일성은 상동성 추론의 근거가 될 수 있으나 짧은 구간의 우연한 일치만으로 전체 단백질의 기원을 판단하지 않습니다. Similarity는 어떤 치환을 비슷하다고 볼지 점수 체계에 의존한다는 점도 구분합니다.

[evo_ncbi_glossary] NCBI BLAST Glossary
https://www.ncbi.nlm.nih.gov/books/NBK62051/?report=reader
[evo_ebi_sequence] EMBL-EBI Training: Primary structure—Why sequence matters
https://www.ebi.ac.uk/training/online/courses/foundations-protein-structure/fundamentals-of-protein-composition/the-peptide-bond-and-primary-structure/ss/

## 3. Ortholog와 paralog: 갈라진 사건을 묻는다 (3–5분)

오늘은 유전자 중복과 종 분화를 중심으로 한 단순한 진화 모형을 사용합니다. 두 유전자를 거슬러 올라가 만나는 가장 최근 공통 조상 노드가 종 분화이면 ortholog, 유전자 중복이면 paralog입니다. 서로 다른 종에 존재하는 paralog도 있으므로 종이 다르다는 이유만으로 ortholog라고 부르면 안 됩니다. 이 관계는 기능 실험 결과가 아니라 진화 사건으로 정의됩니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_ensembl_tree] Ensembl: Protein trees
https://www.ensembl.org/info/docs/compara/homology_method.html

## 4. Species tree와 gene tree는 다른 질문 (5–7분)

종 계통수의 말단은 종이고 유전자 계통수의 말단은 개별 유전자입니다. 따라서 한 종에서 유전자가 중복되면 gene tree에는 같은 종 이름을 가진 말단이 여러 개 나타납니다. 실제 연구에서는 유전자 계통수를 종 계통수와 대조하는 reconciliation을 통해 중복과 종 분화를 추론합니다. 여기서는 분기 길이와 시간 축은 생략하고 사건의 순서만 읽습니다.

[evo_ensembl_tree] Ensembl: Protein trees
https://www.ensembl.org/info/docs/compara/homology_method.html

## 5. 예제 1: 종 분화보다 먼저 중복되었다면 (7–10분)

먼저 조상 유전자가 1번과 2번 계열로 중복되고, 이후 A와 B가 종 분화한 가상 사례입니다. A_1과 B_1의 가장 최근 공통 조상은 왼쪽 S이므로 ortholog입니다. A_1과 A_2 또는 A_1과 B_2를 거슬러 올라가면 가장 최근 공통 조상은 맨 위 D이므로 두 쌍 모두 paralog입니다. 특히 A_1과 B_2는 다른 종에 있는 paralog라는 점을 손가락으로 경로를 짚어 설명합니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_ensembl_loss] Ensembl archived documentation: Gene Orthology/Paralogy prediction method
https://may2009.archive.ensembl.org/info/docs/compara/homology_method.html

## 6. 예제 2: 종 분화 뒤에 중복되었다면 (10–13분)

이번에는 종 분화가 먼저 발생하고 A 계통 안에서만 유전자가 중복되었습니다. A_1과 A_2를 비교하면 D에서 만나지만, 어느 쪽을 B_1과 비교하든 S에서 만나므로 각각 ortholog입니다. 따라서 orthology는 반드시 일대일 관계일 필요가 없으며 여기서는 일대다 관계입니다. Co-ortholog라는 표현은 무엇에 대한 관계인지 기준 상대인 B_1을 함께 말해야 정확합니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_ensembl_types] Ensembl: Homology types
https://mart.ensembl.org/info/genome/compara/homology_types.html

## 7. Paralog는 종 안에도, 종 사이에도 있다 (13–15분)

이 표는 앞의 두 계통수를 한 번 더 정리하는 장입니다. Within-species와 between-species는 현재 유전자가 어느 종에 있는지를 말하고, inparalog와 outparalog는 기준 종 분화보다 중복이 나중인지 이전인지를 말합니다. 따라서 같은 종에 있는 paralog라는 사실만으로 중복이 그 종에서 최근에 일어났다고 결론 내릴 수 없습니다. 초보 단계에서는 세부 명칭 암기보다 D와 S의 순서를 먼저 설명하게 합니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_ensembl_loss] Ensembl archived documentation: Gene Orthology/Paralogy prediction method
https://may2009.archive.ensembl.org/info/docs/compara/homology_method.html

## 8. 유전자 소실: 남은 하나끼리 비교하면 생기는 착시 (15–18분)

고대 중복 후 A에서는 2번 계열, B에서는 1번 계열이 사라진 가상 사례입니다. 현재 남은 A_1과 B_2만 보면 각 종에 하나씩 있는 대응처럼 보이지만, 이들의 가장 최근 공통 조상은 D입니다. 그러므로 서로 paralog이며 단순한 일대일 검색 결과로 진화 역사를 확정할 수 없습니다. 실제 자료에서는 소실뿐 아니라 불완전한 조립이나 주석 누락도 유전자가 없어 보이는 이유가 될 수 있음을 덧붙입니다.

[evo_ensembl_loss] Ensembl archived documentation: Gene Orthology/Paralogy prediction method
https://may2009.archive.ensembl.org/info/docs/compara/homology_method.html
[evo_ensembl_tree] Ensembl: Protein trees
https://www.ensembl.org/info/docs/compara/homology_method.html

## 9. 실습 1: 가장 최근 공통 조상에 표시하기 (18–22분)

개인 풀이 1분, 짝 토론 1분, 전체 해설 2분으로 운영합니다. 정답은 A_x–A_y가 D에서 만나는 paralog, A_x–B_z와 A_y–B_z가 각각 S에서 만나는 ortholog입니다. A_x와 A_y는 B_z에 대한 co-orthologs이며, 서로가 ortholog라는 뜻은 아닙니다. 종이 다르다는 이유만 쓴 답에는 가장 최근 공통 조상 노드를 표시하도록 다시 요청하고, 화면을 읽기 어려운 학생에게는 동일 내용을 구두로 설명합니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf

## 10. Ortholog여도 기능이 완전히 같지는 않다 (22–24분)

Ortholog는 기능을 추론할 때 유용하지만 모든 생물학적 기능이 동일하다는 정의는 아닙니다. 기능은 촉매 작용, 기질, 발현 조직, 상호작용 상대 등 여러 층위로 나뉘므로 어느 층위의 유사성을 말하는지 명시해야 합니다. 실제 기능 자료를 비교한 연구도 ortholog와 paralog의 차이를 통계적 경향으로 다루며 절대 규칙으로 다루지 않습니다. 구조 예측용 MSA에는 목적에 따라 여러 상동 계열이 포함될 수 있으므로 ortholog만 남겨야 한다는 규칙도 자동으로 적용하지 않습니다.

[evo_function] Altenhoff et al. (2012). Resolving the Ortholog Conjecture. PLOS Computational Biology.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002514
[evo_ensembl_tree] Ensembl: Protein trees
https://www.ensembl.org/info/docs/compara/homology_method.html

## 11. 유전자 가족에서 MSA로: 대응 위치를 제안한다 (24–26분)

계통수를 통해 누가 누구와 관련되는지 생각했다면, 이제 각 서열의 어느 위치끼리 비교할지 정해야 합니다. MSA는 삽입과 결실을 고려해 대응한다고 보는 잔기들을 같은 열에 배치합니다. 특히 짧은 반복, 매우 다른 길이, 도메인 구성이 다른 서열에서는 정렬의 불확실성이 커질 수 있습니다. 이후 구조 예측에서 사용되는 정보는 이런 대응 관계에 영향을 받으므로 행 수를 세기 전에 정렬 자체를 읽는 습관을 들입니다.

[evo_ebi_msa] EMBL-EBI Training: Multiple sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/multiple-sequence-alignment/
[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki

## 12. MSA 읽기: 행·열·query·gap (26–29분)

가상 정렬에서 한 행을 가로로 읽으면 하나의 단백질 서열을, 한 열을 세로로 읽으면 대응한다고 본 위치들의 상태를 읽습니다. Query의 세 번째 열에는 잔기가 없으므로 이 열의 정렬 번호와 query의 잔기 번호는 다릅니다. Gap은 이 위치에 정렬된 잔기가 없다는 표시이지 미지의 아미노산이라는 기호가 아닙니다. 이 짧은 예시는 MSA 문법을 위한 것이며 실제 단백질의 구조나 기능을 예측할 수 있는 자료가 아닙니다.

[evo_ebi_msa] EMBL-EBI Training: Multiple sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/multiple-sequence-alignment/

## 13. Gap 하나가 잔기 번호를 바꾼다 (29–31분)

같은 정렬을 다시 사용해 query의 D가 정렬에서는 4열이지만 원래 서열에서는 3번 잔기임을 확인합니다. 구조 파일의 잔기 번호나 실험에서 사용한 construct 번호는 여기서도 다시 달라질 수 있으므로 별도 대응이 필요합니다. 또한 seq_A의 Q를 query 대비 삽입으로 표현할 수 있어도 어느 조상에서 실제 삽입 또는 결실이 일어났는지는 이 정렬만으로 결정하지 못합니다. 이후 마스킹 위치를 정할 때 번호 체계를 혼동하지 않도록 기록 단위를 명시합니다.

[evo_ebi_pairwise] EMBL-EBI Training: Pairwise sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/pairwise-sequence-alignment/

## 14. FASTA: 이름 줄과 서열 줄부터 읽기 (31–33분)

헤더와 서열을 분리해 읽는 것만으로 많은 입력 실수를 줄일 수 있습니다. 첫 번째 줄의 synthetic이라는 말은 자료의 출처 설명이며 단백질 서열에 포함되지 않습니다. 서열 길이가 서로 다를 수 있는 일반 FASTA와 gap을 넣어 대응 열을 맞춘 aligned FASTA를 구분합니다. 일반 FASTA에서 대소문자가 가지는 의미는 도구에 따라 다를 수 있으므로 다음 장의 A3M 규칙을 모든 FASTA 파일에 그대로 적용하지 않습니다.

[evo_ncbi_fasta] NCBI: BLAST QuickStart—Query and Database Sequence Formats
https://www.ncbi.nlm.nih.gov/books/NBK1734/?report=reader

## 15. A3M: 대문자와 소문자는 서로 다른 역할 (33–36분)

A3M에서는 삽입 열의 빈칸을 생략할 수 있어 텍스트 줄의 길이가 달라 보입니다. 예시의 소문자 q는 삽입 잔기이고 대문자 Y는 query의 F와 다른 잔기지만 같은 match 열에 대응합니다. 소문자를 제외해 읽으면 각 행의 match와 deletion 위치는 여덟 개이며 query의 위치와 맞출 수 있습니다. 삽입 정보의 처리 방식은 예측 파이프라인마다 다르므로 파일 원본을 무조건 대문자로 바꾸거나 모든 소문자를 임의 삭제해서 저장하지 않습니다.

[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki

## 16. Coverage와 identity: 분모를 함께 적는다 (36–39분)

이 강의의 계산 예에서는 coverage를 query 전체 잔기 중 상대 잔기와 짝지어진 위치의 비율로 정의합니다. Identity는 두 서열 모두 잔기가 있는 비교 위치 중 같은 잔기의 비율로 계산합니다. 실제 프로그램은 gap 포함 여부나 길이 기준이 달라질 수 있으므로 출력 문서를 확인하고 숫자만 비교하지 않습니다. 100% identity라도 query의 아주 짧은 부분만 덮는 hit는 전체 단백질이 동일한 특징을 가진다는 근거가 되지 않습니다.

[evo_ncbi_glossary] NCBI BLAST Glossary
https://www.ncbi.nlm.nih.gov/books/NBK62051/?report=reader
[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki

## 17. 실습 2: 짧고 완벽한 hit와 길고 다른 hit (39–42분)

개인 계산 1분 후 짝과 분모를 확인하고 1분 동안 해설합니다. 정답은 A가 비교 위치 4개 모두 같으므로 coverage 4/8=50%, identity 4/4=100%입니다. B는 비교 위치 8개 중 6개가 같으므로 coverage 8/8=100%, identity 6/8=75%입니다. 어느 하나가 무조건 더 좋은 MSA 입력이라고 정하기보다는 길이, 상동성 근거, 정렬 신뢰도와 분석 목적을 함께 확인한다는 답으로 마무리합니다.

[evo_ncbi_glossary] NCBI BLAST Glossary
https://www.ncbi.nlm.nih.gov/books/NBK62051/?report=reader

## 18. Conservation: 한 열에서 무엇이 유지되는가? (42–44분)

각 열을 세로로 읽고 어떤 잔기가 얼마나 자주 나타나는지 확인합니다. 예시에서 첫 번째 열은 모두 A이지만 두 번째 열은 C와 S로 달라집니다. 보존은 구조 안정성이나 기능적 제약과 관련될 수 있지만 표집된 서열이 서로 너무 비슷해 보존적으로 보이는 경우도 있습니다. 네 개의 짧은 가상 서열만으로 생물학적 중요도를 추정하지 않고 개념을 익히는 데만 사용합니다.

[evo_ebi_sequence] EMBL-EBI Training: Primary structure—Why sequence matters
https://www.ebi.ac.uk/training/online/courses/foundations-protein-structure/fundamentals-of-protein-composition/the-peptide-bond-and-primary-structure/ss/
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957

## 19. Covariation: 두 열의 조합을 읽는다 (44–47분)

이 가상 표에서 한 열만 보면 K와 E가 각각 두 번, 다른 열에서는 D와 R이 각각 두 번 나타납니다. 두 열을 함께 보면 K-D와 E-R 조합만 관찰되어 독립적인 조합과는 다른 패턴을 보입니다. 이는 공변이를 이해하기 위한 예시이며 두 잔기가 직접 접촉하거나 보상 돌연변이를 겪었다는 증명은 아닙니다. 실제 구조 예측에서는 많은 열과 서열에서 얻은 정보를 모형이 통합하므로 이 네 줄의 단순 상관계산과 동일시하지 않습니다.

[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957
[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108

## 20. 공통 조상도 함께 변하는 패턴을 만든다 (47–49분)

앞의 K-D와 E-R 패턴이 두 계통에서 각각 한 번 생긴 뒤 후손에게 전달되었다고 가정해 봅니다. 후손을 많이 모아도 실제 변화가 여러 번 독립적으로 반복된 것은 아닙니다. 따라서 공변이를 바로 물리적 접촉이라고 해석하면 계통적 교란과 간접 관계를 놓칠 수 있습니다. 재가중과 통계 모형이 이러한 영향을 줄이려 하지만 완전히 제거하거나 직접 접촉을 보장하는 것은 아닙니다.

[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957
[evo_weighting] Hockenberry & Wilke (2019). Phylogenetic Weighting Does Little to Improve the Accuracy of Evolutionary Coupling Analyses.
https://www.mdpi.com/1099-4300/21/10/1000

## 21. Raw depth와 Neff: 행 수와 다양성은 다르다 (49–52분)

가중치 합으로 정의하는 한 방식에서는 각 서열과 충분히 비슷한 이웃 수를 자기 자신까지 포함해 센 뒤 그 역수를 가중치로 사용합니다. 모두 같은 서열 100개라면 각 가중치는 1/100이므로 합은 1입니다. 이것은 교육용 재가중 예시이며 HH-suite의 엔트로피 기반 Neff 등 다른 정의와 수치를 그대로 비교할 수 없습니다. Neff는 실제 독립 표본 수의 정답도 아니고 구조 예측 정확도를 보장하는 점수도 아닙니다.

[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki
[evo_weighting] Hockenberry & Wilke (2019). Phylogenetic Weighting Does Little to Improve the Accuracy of Evolutionary Coupling Analyses.
https://www.mdpi.com/1099-4300/21/10/1000

## 22. 다음 단계: MSA의 어떤 정보를 바꿀 것인가? (52–55분)

지금까지의 개념을 다음 구조 예측 실습의 관찰 항목으로 연결합니다. Depth 변경은 몇 행을 제공하는지, clustering은 어떤 서열 집단을 선택하는지, masking은 어떤 위치의 정보를 감추는지에 관한 조작입니다. 어떤 변경이든 정보가 줄거나 치우칠 수 있으므로 무조건 정확도를 높이는 방법으로 소개하지 않습니다. 학생에게 앞으로 결과를 비교할 때 구조가 달라졌다는 관찰과 실제 생물학적 상태가 존재한다는 결론을 구분하도록 안내하고 휴식으로 넘어갑니다.

[evo_ebi_msa] EMBL-EBI Training: Multiple sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/multiple-sequence-alignment/
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957

## 23. 휴식 (55–65분)

55–65분 휴식. 다음 구간에서는 서열 파일, MSA, 예측 구조를 구분하고 입력을 바꿀 때 고정할 항목을 정한다.



## 24. 서열에서 예측 구조까지 (65–68분)

1강에서 본 PDB/mmCIF와 연결한다. FASTA는 입력 서열, A3M은 정렬, PDB/mmCIF는 좌표를 담는다. 구조 예측기는 MSA를 3차원 사진처럼 읽지 않는다. 각 위치의 보존과 상관관계, 학습한 구조적 규칙을 함께 사용한다. Template은 기존 구조에서 얻는 추가 정보이며 MSA와 구분한다. 모델이 반환한 파일은 실험에서 직접 측정한 좌표가 아니다. 학생에게 어떤 파일에 원자 좌표가 들어 있는지 질문한다.

[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2
[core_af3] Abramson et al. (2024), Accurate structure prediction of biomolecular interactions with AlphaFold 3
https://www.nature.com/articles/s41586-024-07487-w

## 25. AlphaFold2와 AlphaFold3 (68–71분)

AF2와 AF3를 단순한 정확도 순위로 소개하지 않는다. AF2의 monomer 모델은 단백질 중심이며 복합체용 AlphaFold-Multimer가 별도로 있다. AF3는 단백질 외 분자들을 함께 다루고 diffusion 기반 좌표 생성을 사용한다. 단백질 MSA는 AF3에도 사용된다. AF2에서 관찰한 MSA 조작 효과가 AF3에서도 동일한 크기와 방식으로 나타난다고 가정하면 안 된다. 모델을 바꾸면 MSA 처리 방식과 점수의 의미도 함께 확인한다.

[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2
[core_af3] Abramson et al. (2024), Accurate structure prediction of biomolecular interactions with AlphaFold 3
https://www.nature.com/articles/s41586-024-07487-w

## 26. 웹 서버와 로컬 실행 (71–74분)

AlphaFold Server와 공개 AF3 로컬 코드는 입력 기능과 실행 환경이 같지 않다. 웹 화면에서 로컬 JSON의 모든 항목을 조절할 수 있다고 설명하지 않는다. 초보자는 ColabFold 노트북에서 서열 입력과 결과 파일을 먼저 경험한다. 교사는 강의 전에 접속 가능 여부와 GPU 할당을 확인하고 동일한 실습 파일을 준비한다. 수업은 오프라인 정렬 실습과 결과 판독만으로도 끝낼 수 있으며, 실제 예측 시연은 사전 준비한 환경에서 선택적으로 진행한다. 실행법은 examples/README.md에 제공한다.

[core_cf] ColabFold official repository
https://github.com/sokrypton/ColabFold
[core_af3_input] AlphaFold 3 official input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 27. Custom MSA의 기본 조건 (74–77분)

같은 단백질의 대안 구조를 비교하는 실습이므로 query를 고정한다. 소문자를 대문자로 바꾸면 삽입이 정렬 열로 오해되어 열 대응이 깨질 수 있다. 줄마다 문자열 길이가 달라도 lowercase insertion을 제외한 정렬 길이는 같아야 한다. Gap과 unknown X의 의미는 다르다. 헤더는 서열 식별과 일부 파이프라인의 종 정보 해석에 쓰일 수 있으므로 무작위로 바꾸는 것을 구조 제어 방법이라고 가르치지 않는다. 복합체 pairing은 별도의 대응 문제다.

[core_cf] ColabFold official repository
https://github.com/sokrypton/ColabFold
[core_af3_input] AlphaFold 3 official input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 28. AF3에서 custom MSA 지정 (77–80분)

이 예시는 필드의 뜻을 읽는 용도다. sequence 자리에는 실제 query 전체가 필요하다. unpairedMsaPath는 JSON 파일 기준 상대 경로나 절대 경로다. pairedMsa의 빈 문자열은 paired MSA를 쓰지 않는다는 뜻이며 templates의 빈 목록은 template을 제공하지 않는다는 뜻이다. 필드를 생략하는 것과 명시적으로 빈 값으로 만드는 것은 처리 결과가 다를 수 있다. Path 필드는 입력 포맷 version 2부터 지원한다. examples/prepare_inputs.py가 실제 서열과 MSA의 일치를 확인하고 실행용 JSON을 만든다.

[core_af3_input] AlphaFold 3 official input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 29. 다른 예측 모델의 역할 (80–83분)

사용 목적에 따라 모델을 고른다. ColabFold는 AF2를 사용하기 쉽게 만든 워크플로이며 별도의 독립 구조 모델 이름과 혼동하지 않는다. Boltz-2와 Chai-1은 여러 종류의 생체분자를 함께 다룰 수 있다. ESMFold는 언어 모델을 활용해 단일 서열에서 구조를 예측하며 별도의 입력 MSA가 필요하지 않다. 서로 다른 모델도 학습 데이터나 구조 선호를 공유할 수 있다. 한 모델에서 나온 상태가 다른 모델에서 보이지 않는다는 이유만으로 존재를 부정할 수 없다.

[core_cf] ColabFold official repository
https://github.com/sokrypton/ColabFold
[core_boltz] Boltz official prediction documentation
https://github.com/jwohlwend/boltz/blob/main/docs/prediction.md
[core_chai] Chai-1 official repository
https://github.com/chaidiscovery/chai-lab
[core_esm] ESM / ESMFold official repository
https://github.com/facebookresearch/esm

## 30. 한 번에 한 조건씩 비교 (83–85분)

표본 수가 다르면 더 많은 계산을 한 방법이 유리할 수 있다. 방법 간 생성 구조 수, seed 목록, template 유무, 모델 버전과 recycling 설정을 맞춘다. Depth는 query를 포함하는지 기록한다. 입력 MSA 행 수와 모델 내부 max-msa의 두 한도는 구분한다. 어느 조건이 대안 구조를 더 잘 회수하는지는 동일한 평가 기준으로 비교한다. 이 실습에서는 결과를 예상해서 서열을 골라 넣기보다 조작의 의미와 대조군을 설명하는 데 중점을 둔다.

[core_cf] ColabFold official repository
https://github.com/sokrypton/ColabFold

## 31. 기준 예측부터 기록한다 (85–87분)

이 단원의 질문은 같은 단백질에 대해 다른 구조 후보를 얻을 수 있는가이다. 첫 결과를 지우지 말고 baseline으로 보관한다. 학생에게 서열 길이까지 달라지면 무엇을 비교한 것인지 물어본다. MSA 조작의 효과를 비교할 때 query와 모델 버전, template 조건, 반복 수를 맞춘다. 뒤에서 소개할 원래 SPEACH_AF는 query도 편집하는 예외이므로, 오늘의 query 유지 실습과 구분한다.

[ebi_inputs] EMBL-EBI / Google DeepMind training: AlphaFold2 inputs and outputs recap
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap/
[afcluster_code] AF-Cluster author repository and ClusterMSA.py
https://github.com/HWaymentSteele/AF_Cluster/blob/main/scripts/ClusterMSA.py
[speach_code] SPEACH_AF author notebook: SPEACH_AF_scan.ipynb
https://github.com/RSvan/SPEACH_AF/blob/main/SPEACH_AF_scan.ipynb

## 32. 행을 줄인다: MSA subsampling (87–90분)

아래 정렬은 원리를 설명하기 위한 가상 여덟 자리 예시이며 실제 단백질이 아니다. Query를 보존한 채 homolog 1과 3만 택한 경우를 손으로 표시하게 한다. Subsampling은 서열의 이름을 바꾸는 일이 아니라 실제 들어가는 행의 집합을 바꾸는 일이다. 같은 개수라도 중복된 서열 위주인지, 다양한 homolog를 포함하는지에 따라 정보가 달라진다. 깊이가 얕을수록 항상 더 좋은 것은 아니며 잘못 접힌 결과도 늘 수 있다.

[subsampling_paper] del Alamo et al. (2022), Sampling alternative conformational states of transporters and receptors with AlphaFold2
https://elifesciences.org/articles/75751

## 33. 논문 그림 읽기: 얕은 MSA의 효과와 한계 (90–92분)

del Alamo 등의 eLife 연구는 일부 수송체와 수용체를 시험했다. 확대한 A 패널에서 점의 색으로 MSA 깊이를 구분하고, 실험 구조와 예측을 겹친 보기를 확인한다. 구조를 더 많이 만들었다는 사실과 정확한 다른 구조를 찾았다는 사실을 분리한다. 원 논문에서는 깊이와 template 선택이 표적마다 달랐으며 모든 단백질에 통하는 최적 깊이를 정하지 못했다. 이 결과를 모든 단백질의 자유에너지 분포를 재현했다는 주장으로 바꾸지 않는다. 슬라이드에는 원본 Figure 1의 A 패널만 확대하여 표시한다. 점의 색상별 MSA depth와 해당 구조 비교를 읽는다.

[subsampling_paper] del Alamo et al. (2022), Sampling alternative conformational states of transporters and receptors with AlphaFold2
https://elifesciences.org/articles/75751

## 34. AF-Cluster: 서열을 먼저 나누어 예측 (92–95분)

그림에서 먼저 나누는 대상은 아직 구조가 없는 서열들임을 짚는다. AF-Cluster는 서열 유사성으로 만든 작은 MSA들을 예측에 사용한다. 그림 속 KaiB는 생체시계 단백질이며 알려진 두 접힘과 예측을 비교하는 교육 예시이다. 이 성공 사례가 모든 단백질의 숨은 상태를 찾아준다는 보장은 아니다. 논문은 온라인 2023년, Nature 권호는 2024년이므로 참고문헌 연도가 다른 이유를 짧게 설명한다. 실제 실행 단계는 examples/afcluster_guide.md를 사용한다. 공식 ClusterMSA.py의 positional 인자와 flags를 확인한 명령, query 보존 검사, cluster별 ColabFold 실행이 들어 있다. 이 자료 제작 중 실제 GPU 예측은 실행하지 않았다.

[afcluster_paper] Wayment-Steele et al. (2024), Predicting multiple conformations via sequence clustering and AlphaFold2
https://www.nature.com/articles/s41586-023-06832-9
[afcluster_code] AF-Cluster author repository and ClusterMSA.py
https://github.com/HWaymentSteele/AF_Cluster/blob/main/scripts/ClusterMSA.py

## 35. 각 cluster에도 같은 query가 들어간다 (95–98분)

AF-Cluster 저자 코드에서 query는 처음에 분리되고 각 cluster 파일을 쓸 때 다시 맨 앞에 붙는다. 가상 정렬에서 두 입력의 첫 줄이 완전히 같은지 학생이 확인하게 한다. 서열 cluster에 query와 먼 homolog가 포함될 수 있어도 예측 대상은 첫 query이다. 이것은 각 cluster의 대표 homolog 구조를 각각 예측하는 실험과 다른 질문이다. 실습에서는 query를 변경하거나 원본을 덮어쓰지 않는다.

[afcluster_code] AF-Cluster author repository and ClusterMSA.py
https://github.com/HWaymentSteele/AF_Cluster/blob/main/scripts/ClusterMSA.py

## 36. 서열 cluster는 열역학적 상태가 아니다 (98–100분)

앞 단원에서 배운 종분화와 유전자 중복을 연결한다. Ortholog와 paralog는 진화 사건에 대한 관계이고 open과 closed는 구조 상태에 대한 말이다. 서열 유사성만으로 만든 집합은 ortholog만을 보장하지 않으며 기능적 분화도 포함할 수 있다. 어떤 sequence cluster에서 구조가 잘 나왔다는 사실만으로 그 집합이 특정 열역학적 상태를 뜻한다고 부르지 않는다. 종별 서열 데이터 수가 많다는 사실도 분자의 상태 점유율과는 무관하다.

[afcluster_paper] Wayment-Steele et al. (2024), Predicting multiple conformations via sequence clustering and AlphaFold2
https://www.nature.com/articles/s41586-023-06832-9
[afcluster_response] Wayment-Steele et al. (2025), Does Sequence Clustering Confound AlphaFold2?
https://doi.org/10.1016/j.jmb.2025.169376

## 37. 2025년 논쟁: 비교 조건을 읽는다 (100–103분)

Schafer 등은 Nature Matters Arising에서 CF-random과 비교하고 evolutionary coupling 해석에 이의를 제기했다. Wayment-Steele 등의 2025년 JMB 응답은 비교 조건의 혼입을 지적하고 추가 분석으로 반박했다. 두 문헌을 함께 소개하며 한쪽의 제목을 확정된 결론처럼 읽지 않는다. 학생에게 비교에서 MSA 깊이, 모델 설정, seed 수가 달라지면 어느 요인의 효과인지 구분 가능한지 묻는다. 여기서 보편적 우승 방법을 정하지 않고 연구 질문에 맞는 대조 실험의 중요성을 가르친다.

[afcluster_critique] Schafer et al. (2025), Sequence clustering confounds AlphaFold2
https://www.nature.com/articles/s41586-024-08267-2
[afcluster_response] Wayment-Steele et al. (2025), Does Sequence Clustering Confound AlphaFold2?
https://doi.org/10.1016/j.jmb.2025.169376

## 38. 두 가지 clustering을 구별한다 (103–105분)

Clustering이라는 단어만 보지 말고 무엇을 어떤 거리로 묶었는지 확인하게 한다. 입력에서는 정렬된 서열의 차이를 이용한다. 출력에서는 적절히 정렬한 좌표나 도메인 간 거리, 접촉 양상처럼 질문에 맞는 구조 특징을 이용한다. 입력이 세 그룹이어도 출력이 두 구조 그룹일 수 있고 반대도 가능하다. 이 표는 일반 분석 설계이며 특정 논문의 cluster 수를 재현한 자료가 아니다.

[afcluster_code] AF-Cluster author repository and ClusterMSA.py
https://github.com/HWaymentSteele/AF_Cluster/blob/main/scripts/ClusterMSA.py
[afsample2_code] wallnerlab/AFsample2 author repository
https://github.com/wallnerlab/AFsample2

## 39. 열을 가린다: unknown X와 gap의 차이 (105–108분)

이 예시는 AFsample2의 아이디어를 가상 정렬로 설명한다. Homolog의 네 번째 정렬 위치만 X로 가렸고 query는 그대로임을 확인한다. X를 gap으로 대신 쓰면 같은 의미가 아니며, 열 자체를 지우면 길이와 좌표 대응도 바뀐다. A3M에서는 소문자 insertion이 정렬 열에 그대로 세어지는 것이 아니므로 실제 입력에서는 포맷을 이해해야 한다. 여기서는 모두 대문자와 gap만 있는 작은 정렬로 열의 의미에 집중한다.

[afsample2_paper] Kalakoti and Wallner (2025), AFsample2 predicts multiple conformations and ensembles with AlphaFold2
https://www.nature.com/articles/s42003-025-07791-9
[af3_input] Google DeepMind AlphaFold 3 input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 40. SPEACH_AF와 AFsample2는 같은 편집이 아니다 (108–111분)

Alanine은 실제 아미노산 A이고 unknown X와 다르다. 원 SPEACH_AF 논문과 저자 notebook은 선택한 위치를 정렬의 모든 서열에서 A로 편집하며 query도 포함하고 gap은 유지한다. 따라서 query를 고정한 마스킹 실습을 원 논문의 정확한 재현이라고 부르면 안 된다. AFsample2 논문은 query 첫 행을 제외하고 무작위로 선택한 열을 X로 바꾸고 dropout과 결합한다. 이 슬라이드는 방법 개념 비교이며 특정 단백질의 치환 설계를 다루지 않는다.

[speach_paper] Stein and Mchaourab (2022), SPEACH_AF: Sampling protein ensembles and conformational heterogeneity with Alphafold2
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010483
[speach_code] SPEACH_AF author notebook: SPEACH_AF_scan.ipynb
https://github.com/RSvan/SPEACH_AF/blob/main/SPEACH_AF_scan.ipynb
[afsample2_paper] Kalakoti and Wallner (2025), AFsample2 predicts multiple conformations and ensembles with AlphaFold2
https://www.nature.com/articles/s42003-025-07791-9

## 41. 논문 그림 읽기: AFsample2의 입력과 출력 (111–113분)

그림 a에서 MSA 가로와 세로 방향을 손으로 가리키며 앞 두 실습을 연결한다. 예측 뒤에는 구조 파일을 분석하여 후보의 품질과 다양성을 확인해야 한다. 논문의 일부 benchmark에서 대안 구조와 비슷한 후보를 더 잘 찾았지만 효과는 표적과 설정에 의존한다. 두 알려진 구조 사이에 보이는 모델은 가능한 중간 구조 가설이며 실제 전이 경로 위에 있다는 증명은 아니다. 슬라이드는 원본 Figure 1a만 확대해 표시한다. 저자의 제안 개념도이며 마스킹이 열림을 일으킨다는 직접 증거가 아니다. 실제 AFsample2에서 query 첫 행은 유지한다.

[afsample2_paper] Kalakoti and Wallner (2025), AFsample2 predicts multiple conformations and ensembles with AlphaFold2
https://www.nature.com/articles/s42003-025-07791-9

## 42. FASTA 제목에 open을 쓰면 열릴까? (113–115분)

학생에게 첫 두 레코드에서 바뀐 것이 실제 아미노산인지 이름인지 묻는다. Open이라고 이름을 붙였다는 이유로 열린 구조를 요구하는 프롬프트가 되는 것은 아니다. 다만 header는 언제나 무의미하다고 설명해서도 안 된다. 일부 multimer 파이프라인은 종 식별 정보를 읽어 MSA pairing에 사용하므로 임의로 바꾸면 입력 처리에 영향을 줄 수 있다. 단량체의 자유로운 별칭과 구조 예측용 생물학적 metadata를 구별한다.

[af3_input] Google DeepMind AlphaFold 3 input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 43. Seed·dropout·template도 별도 요인이다 (115–118분)

Seed를 바꾸면 같은 설정에서 다른 결과가 나올 가능성이 있지만 반드시 다른 구조가 생기지는 않는다. Dropout은 구현이 지원하는 경우에만 추론에서 활성화할 수 있으며, 다양성을 높여도 물리적 온도를 올리는 실험은 아니다. Template은 강한 사전 정보가 될 수 있어 독립적인 발견이라는 주장과 구분한다. 같은 MSA 두 조건을 비교한다면 나머지 설정과 반복 수를 맞추고 모두 기록해야 한다. 이 표는 요인 분리를 위한 설명이며 GPU 실행 지침이 아니다.

[ebi_inputs] EMBL-EBI / Google DeepMind training: AlphaFold2 inputs and outputs recap
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap/
[afsample2_code] wallnerlab/AFsample2 author repository
https://github.com/wallnerlab/AFsample2
[subsampling_paper] del Alamo et al. (2022), Sampling alternative conformational states of transporters and receptors with AlphaFold2
https://elifesciences.org/articles/75751

## 44. AF2 근거를 AF3에 그대로 옮길 수는 없다 (118–120분)

AF3는 단백질 외 분자를 함께 다루는 모델이며 구조 생성 방식도 AF2와 다르다. 로컬 공식 AF3 문서는 custom A3M을 지원하지만 첫 서열과 query의 일치를 요구한다. 공개 AlphaFold Server와 로컬 코드의 입력 제어 범위가 같다고 가정하지 않는다. AFsample3 연구 저장소가 존재함을 확인했으므로 AF3에서는 불가능하다고 단정하지 않는다. 동시에 이 강의의 AF2 benchmark 수치를 AF3의 성능 수치로 제시하지 않는다.

[af3_paper] Abramson et al. (2024), Accurate structure prediction of biomolecular interactions with AlphaFold 3
https://www.nature.com/articles/s41586-024-07487-w
[af3_input] Google DeepMind AlphaFold 3 input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md
[afsample3_code] wallnerlab/afsample3 research implementation
https://github.com/wallnerlab/afsample3

## 45. 3분 설계 실습: 공정한 비교를 고르기 (120–123분)

1분 개인 판단, 1분 짝 토론, 1분 공유로 운영한다. 기기가 없으면 종이에 A 또는 B와 이유를 적는다. 강사용 답: B가 행 선택 효과를 분리하기에 낫다. A는 query, template, 반복 수가 함께 바뀌어 차이의 원인을 구별하기 어렵다. B도 선택한 행 집합·MSA 유효 다양성·동일 seed 집합·코드 버전을 기록해야 재현과 해석이 가능하다. 이 답은 학생 화면에 먼저 보여주지 않는다.

[afcluster_critique] Schafer et al. (2025), Sequence clustering confounds AlphaFold2
https://www.nature.com/articles/s41586-024-08267-2
[afcluster_response] Wayment-Steele et al. (2025), Does Sequence Clustering Confound AlphaFold2?
https://doi.org/10.1016/j.jmb.2025.169376
[ebi_inputs] EMBL-EBI / Google DeepMind training: AlphaFold2 inputs and outputs recap
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap/

## 46. 대표 후보는 품질과 다양성을 함께 본다 (123–126분)

아래는 실제 AF2 출력이 아닌 교사의 가상 판단 연습이다. 먼저 평균 pLDDT만 읽지 말고 변한 부위와 domain 사이 PAE, 기하학적 이상을 보도록 한다. 강사용 토론 예: A와 B는 비교할 대표 후보로 보관하고 C는 잠정 보류, D는 A와 중복임을 표시한다. B의 더 큰 구조 차이가 정답을 뜻하지 않으며 후속 독립 증거가 필요하다. 전체 사슬을 무조건 맞추면 움직임이 희석될 수 있어 비교 core와 잔기 범위를 기록한다.

[ebi_plddt] EMBL-EBI / Google DeepMind training: pLDDT, Understanding local confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/
[ebi_pae] EMBL-EBI / Google DeepMind training: PAE, A measure of global confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/
[speach_paper] Stein and Mchaourab (2022), SPEACH_AF: Sampling protein ensembles and conformational heterogeneity with Alphafold2
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010483

## 47. pLDDT·PAE를 상태 확률로 읽지 않는다 (126–128분)

pLDDT는 AF2에서 잔기별 국소 정확도에 대한 예측 점수이고 PAE는 한 위치를 기준으로 맞췄을 때 다른 위치에 예상되는 오차이다. 둘 다 해당 조건에서 분자가 그 상태에 머무는 평형 확률을 출력한 값은 아니다. 같은 실험 조건을 표현하는 물리적 ensemble이 아니라 MSA·seed·template 설정에 민감한 생성 결과라는 점을 반복한다. 상태 점유율 또는 자유에너지를 주장하려면 그 목적에 맞는 독립적인 실험과 보정 근거가 추가되어야 한다.

[ebi_plddt] EMBL-EBI / Google DeepMind training: pLDDT, Understanding local confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/
[ebi_pae] EMBL-EBI / Google DeepMind training: PAE, A measure of global confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/
[afcluster_response] Wayment-Steele et al. (2025), Does Sequence Clustering Confound AlphaFold2?
https://doi.org/10.1016/j.jmb.2025.169376

## 48. 여러 구조를 얻은 뒤 남는 질문 (128–130분)

마지막으로 각자가 후보라는 단어를 포함해 결론 한 문장을 작성하게 한다. 강사용 예: MSA 입력을 바꾸자 같은 query에서 구조적으로 다른 후보가 나왔으며 실제 상태인지는 추가 검증이 필요하다. 그림을 열린 순서대로 나열하거나 보간한 영상은 설명용 시각화이며 분자 궤적이 아니다. 상태 간 전환 속도와 경로는 별도의 동역학 근거를 요구한다. 이어지는 실습에서는 어떤 입력을 바꿨는지, 결과에서 어디가 달랐는지, 무엇을 아직 모르는지를 한 묶음으로 기록한다.

[afsample2_paper] Kalakoti and Wallner (2025), AFsample2 predicts multiple conformations and ensembles with AlphaFold2
https://www.nature.com/articles/s42003-025-07791-9
[af3_paper] Abramson et al. (2024), Accurate structure prediction of biomolecular interactions with AlphaFold 3
https://www.nature.com/articles/s41586-024-07487-w

## 49. 휴식 (130–140분)

130–140분 휴식. 컴퓨터가 없는 학생에게 활동지를 배부한다. 컴퓨터 실습의 결과와 종이 실습에서 읽는 자료는 같은 원리를 다룬다.



## 50. 실습의 목표와 파일 (140–142분)

이번 실습의 필수 부분은 GPU가 없어도 수행한다. practice의 서열과 비교 수치는 교육용 가상 자료다. 이런 짧은 서열을 실제 생물학적 대상처럼 예측기에 넣어 얻은 결과를 해석하지 않는다. examples에는 UniProt에서 받은 인간 calmodulin-1 전체 서열 149개가 있다. 실제 모델 실행은 별도로 환경을 준비해야 하며, 자료를 만든 과정에서 구조 예측을 실행한 것으로 오해하지 않도록 구분한다. 학생은 각 결과의 출처를 먼저 확인한다.



## 51. 실습 1 · 중복 사건으로 관계 판단 (142–146분)

정답은 사람 A와 생쥐 A가 ortholog, 사람 A와 생쥐 B가 paralog다. 두 유전자의 가장 최근 공통조상에서 어떤 사건이 일어났는지 추적하게 한다. 사람 A와 사람 B도 paralog다. 서로 다른 종의 유전자라는 정보만으로 ortholog라고 할 수 없다. 학생의 설명이 이름이나 서열 유사도에만 의존하면 공통조상까지 다시 선을 따라가도록 유도한다. 종분화 후 사람 계통에서 A가 A1/A2로 중복된 경우도 구두로 추가해 co-ortholog를 확인한다.



## 52. 실습 2 · A3M을 열로 읽기 (146–150분)

실제 실습 파일 이름은 practice/README.md를 따른다. 소문자 insertion은 정렬 열로 세지 않는다. 다만 파서가 그 삽입 길이를 별도 특징으로 활용할 수 있으므로 소문자를 무의미한 문자라고 설명하지 않는다. Gap은 해당 정렬 위치의 잔기가 없는 대응, X는 잔기 종류를 알 수 없거나 가렸다는 표식이다. Subsampling은 진화적 다양성과 특정 위치의 coverage를 함께 바꿀 수 있다. 컴퓨터가 없는 학생은 활동지의 A3M 발췌를 사용한다.

[core_af3_input] AlphaFold 3 official input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 53. 실습 3 · 입력을 바꾸고 확인 (150–154분)

실습 스크립트는 표준 Python만으로 실행한다. Group A/B는 미리 정한 교육용 행 분할이며 AF-Cluster의 실제 clustering 알고리즘이 아니다. Query를 포함한 depth와 homolog 수를 구분하도록 한다. 마스킹한 열을 시각적으로 확인하고 lowercase insertion과 gap이 의도대로 유지되었는지 읽는다. 서열 변형 파일을 만들었다고 구조가 바뀌었다는 증거가 생긴 것은 아니다. 구조 차이는 실제 예측 후 별도로 평가한다.



## 54. ColabFold 노트북으로 실제 예측 (154–158분)

공식 ColabFold AlphaFold2 노트북을 사용한다. 계정 로그인과 GPU 사용 가능 여부는 수업 전에 교사가 확인한다. 첫 번째 단계에서는 FASTA header를 빼고 단백질 서열을 query_sequence에 넣는다. Custom MSA를 사용하는 단계에서는 A3M 첫 행이 동일한 전체 query인지 확인한다. 노트북 셀 실행 뒤 업로드 창이 나타나는 순서는 버전에 따라 달라질 수 있다. 본 실습의 가상 12열 정렬을 calmodulin MSA와 섞으면 안 된다. 저장한 결과에는 입력 MSA와 실행 설정을 함께 보관한다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb
[core_calm] UniProt P0DP23, human calmodulin-1
https://www.uniprot.org/uniprotkb/P0DP23/entry

## 55. ColabFold에서 depth 조건 비교 (158–162분)

아래는 실제 A3M을 준비한 뒤 실행할 명령이다. 두 조건의 query, 모델 수, seed, recycling을 맞춘다. 32:64는 총 depth가 32라는 뜻이 아니다. 입력 행 수가 한도보다 적으면 더 많은 행을 새로 만들어 주지 않는다. 각 seed에서 내부 subsampling에 따라 선택되는 행이 달라질 수 있다. 이 숫자는 교육용 비교 설정이며 최적값이나 대안 상태 회수를 보장하는 조합이 아니다. 전체 MSA 기준선과 비교할 때도 가능한 같은 생성 예산을 사용한다.

[core_cf_cli] ColabFold batch.py official CLI implementation
https://github.com/sokrypton/ColabFold/blob/main/colabfold/batch.py

## 56. Boltz-2에서 같은 A3M 사용 (162–165분)

Boltz 공식 문서는 YAML 입력을 권장한다. 이 수업의 입력 생성기는 동일한 FASTA와 A3M에서 단량체 YAML을 만든다. msa 파일을 지정하면 해당 정렬을 사용하며 자동 MSA 서버 옵션과 구분한다. 아래 명령은 설치와 모델 파일 다운로드, 적합한 계산 자원이 준비된 환경에서 실행한다. Boltz와 AF2의 기본값과 신뢰도 점수를 숫자만으로 동일시하지 않는다. 단백질이 calmodulin이라는 이유만으로 apo/holo 구조가 저절로 구분된다고 기대하지 않는다.

[core_boltz] Boltz official prediction documentation
https://github.com/jwohlwend/boltz/blob/main/docs/prediction.md
[core_calm] UniProt P0DP23, human calmodulin-1
https://www.uniprot.org/uniprotkb/P0DP23/entry

## 57. Chai-1과 ESMFold 비교 경로 (165–168분)

Chai-1은 header에 protein이라는 entity 유형을 지정하는 전용 FASTA를 사용한다. examples/prepare_inputs.py는 필요한 형식으로 복사한다. Chai-1의 custom MSA는 .aligned.pqt 형식이므로 A3M을 그대로 넘기는 AF2 사용법과 다르다. ESMFold는 단일 서열 비교 기준으로 소개한다. 언어 모델이 훈련 과정에서 진화적 서열 통계를 학습했으므로 입력 MSA가 없다는 사실이 진화 정보가 전혀 없다는 뜻은 아니다. 모델 간 결과 차이는 어느 모델이 정답인지 단독으로 결정하지 않는다.

[core_chai] Chai-1 official repository
https://github.com/chaidiscovery/chai-lab
[core_chai_msa] Chai-1 official MSA examples
https://github.com/chaidiscovery/chai-lab/tree/main/examples/msas
[core_esm] ESM / ESMFold official repository
https://github.com/facebookresearch/esm

## 58. 예측 구조 비교의 기준 (168–170분)

RMSD는 구조를 맞추는 원자 선택에 따라 달라진다. 전체를 정렬한 RMSD와 한 도메인에 정렬한 뒤 다른 도메인의 이동을 보는 것은 다른 질문이다. 잔기 번호가 다른 경우 서열 대응부터 확인한다. PAE는 실제 구조를 비교해 측정한 오차가 아니라 모델의 예측 오차다. 단량체 평균 pLDDT가 높아도 도메인 간 상대 배치는 불확실할 수 있다. 점수만 읽지 말고 같은 색과 표시 방식으로 구조를 관찰하도록 한다.

[core_af3_output] AlphaFold 3 official output documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/output.md

## 59. 실습 4 · 대안 구조 후보 선택 (170–175분)

practice/synthetic_comparison.json의 8개 중 4개 행을 발췌했다. 가상 180잔기 표적이며 12열 가상 A3M에서 계산한 값이 아니다. 선택 거리는 40번과 140번 Cα 사이 거리이며 PAE는 구간 20–70과 110–160 사이 두 방향 블록의 평균이다. F1/F2는 가까운 거리, S1은 더 먼 거리를 보여 서로 다른 후보를 검토할 수 있다. S2는 낮은 평균 pLDDT와 높은 PAE 때문에 먼저 품질을 확인한다. F2의 평균 pLDDT가 가장 높아도 이 하나만 남기면 다양성을 놓칠 수 있다. 두 상태의 실재 여부나 점유율은 이 가상 표에서 알 수 없다. 전체 8행 비교와 상세 답안은 practice/instructor_answers.md에 있다.



## 60. 최종 설명 활동 (175–178분)

첫 주장에는 유전자 계통과 종분화/중복 사건 정보가 빠졌다. 두 번째에는 서열 cluster와 구조 상태의 대응 검증이 빠졌다. 세 번째에는 샘플링 분포가 물리적 평형분포에 대응한다는 검증이 빠졌다. 학생에게 무조건 틀렸다고 외우게 하기보다 무엇을 추가로 알아야 하는지 묻는다. 평가 기준은 사건 기준으로 관계를 설명하는가, 입력 분할과 구조 분류를 구분하는가, 모델 점수와 물리적 확률을 구분하는가이다. 정답은 배포 활동지에 넣지 않는다.



## 61. 오늘 배운 내용 (178–179분)

학생이 자기 연구 대상에 적용할 때 첫 질문은 어떤 단백질이며 어떤 구조 차이를 확인하려는가이다. 모든 단백질에서 여러 상태를 얻는 것이 수업의 성공 기준은 아니다. 변화를 얻지 못해도 입력 품질과 대조 조건을 확인하면 의미 있는 기록이다. 후속 과제로 benign한 관심 단백질 하나의 accession, 서열 경계, MSA 기준선, 조작 조건, 판정 지표를 제안하도록 할 수 있다.



## 62. 논문과 실행 문서 (179–180분)

관련 문서는 계속 바뀌므로 실제 시연 전에 설치한 버전의 도움말과 공식 문서를 다시 확인한다. 이 강의는 MSA 조작을 손쉽게 상태를 제어하는 보장된 절차로 설명하지 않는다. 모든 수치 예제와 가상 서열은 실제 실험 자료와 명확히 구분한다. 주요 논문과 도구 문서 링크를 소개하고 질문을 받는다.

[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2
[core_af3] Abramson et al. (2024), Accurate structure prediction of biomolecular interactions with AlphaFold 3
https://www.nature.com/articles/s41586-024-07487-w
[core_cf] ColabFold official repository
https://github.com/sokrypton/ColabFold
[core_boltz] Boltz official prediction documentation
https://github.com/jwohlwend/boltz/blob/main/docs/prediction.md
[core_chai] Chai-1 official repository
https://github.com/chaidiscovery/chai-lab
