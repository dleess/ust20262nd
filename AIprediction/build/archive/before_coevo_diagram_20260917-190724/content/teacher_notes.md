# MSA와 단백질 구조 예측 · 강사용 노트

총 180분, 휴식 20분 포함. 활동 답안은 이 강사용 노트와 practice/instructor_answers.md에 수록합니다.

## 1. MSA와 단백질 구조 예측 (0–1분)

시작부터 ‘왜 AlphaFold를 배우는데 정렬과 진화를 먼저 보나요?’에 답합니다. 도입 2–4장은 query에서 MSA와 구조로 이어지는 흐름, 짧은 MSA의 보존·공변화 예제, 정보의 질과 진화 관계가 중요한 이유를 보여 줍니다. 이후 homology·ortholog·paralog를 배워 정렬에 들어온 서열들이 어떤 관계인지 읽고, coevolution과 MSA 입력 조작으로 연결합니다. 활동지 1쪽은 진화 관계, 2쪽은 A3M, 3쪽은 coevolution, 4쪽은 입력 조작, 5쪽은 lDDT 계산과 pLDDT 학습, 6쪽은 pLDDT·PAE, 7쪽은 결과 해석입니다. 교육용 가상 정렬과 실제 calmodulin 예측 입력을 구분합니다.

[intro_af2_overview] EMBL-EBI / Google DeepMind: AlphaFold2 high-level overview
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/a-high-level-overview/
[evo_ebi_msa] EMBL-EBI Training: Multiple sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/multiple-sequence-alignment/

## 2. AlphaFold에서 MSA는 어디에 쓰일까? (1–3분)

먼저 강의 전체의 목적부터 설명합니다. Query는 이번에 구조를 예측할 서열 하나이며 MSA는 이 표적과 관련된 여러 상동 서열을 대응 위치별로 정렬한 입력입니다. 사용자가 ColabFold에 서열만 넣어도 일반적인 검색 모드에서는 뒤에서 관련 서열을 찾고 MSA를 만듭니다. MSA 파일에는 좌표가 없지만 서열들을 비교하면서 얻는 진화적 제약의 단서가 있습니다. 미리 학습된 AlphaFold2는 MSA 표현과 잔기쌍 표현을 함께 갱신해 좌표를 추론하고 신뢰도를 출력합니다. MSA를 먼저 접촉표로 완전히 바꾼 뒤 그 표만 모델에 넣는다는 뜻은 아닙니다. Template은 이용할 경우 추가하는 기존 구조 정보입니다. 새 query마다 MSA를 만드는 것은 입력 준비이며 신경망 가중치를 처음부터 다시 학습하는 과정이 아닙니다. AF3도 MSA 정보를 사용하지만 Evoformer와 동일한 구조가 아니라 MSA 처리·Pairformer·diffusion으로 역할이 달라집니다. 오늘 구체적 클릭 실습은 AF2 기반 ColabFold로 진행합니다. 다음 두 장에서 왜 여러 서열을 비교해야 하는지 본 뒤 이 서열들의 진화 관계를 배웁니다.

[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2
[intro_af2_overview] EMBL-EBI / Google DeepMind: AlphaFold2 high-level overview
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/a-high-level-overview/
[intro_af2_runtime] Google DeepMind AlphaFold: loading trained parameters and running prediction
https://github.com/google-deepmind/alphafold/blob/main/run_alphafold.py
[intro_af3_overview] EMBL-EBI / Google DeepMind: How does AlphaFold 3 work?
https://www.ebi.ac.uk/training/online/courses/alphafold/alphafold-3-and-alphafold-server/introducing-alphafold-3/how-does-alphafold-3-work/

## 3. 서열 한 줄에서는 보이지 않던 단서가 생긴다 (3–5분)

이 예제는 손으로 만든 8열 정렬이며 실습의 149잔기 calmodulin이나 뒤의 12열 A3M과 다른 교육용 자료입니다. Query 한 줄만 보면 C가 이 유전자 가족에서 보존되는지, 3열과6열의 변화가 연결되는지 알 수 없습니다. 여러 행을 나란히 놓으면 2열과8열이 보존되고 3열과6열의 잔기 조합이 함께 달라지는 패턴을 볼 수 있습니다. D·E는 음전하 성질, K·R은 양전하 성질의 예시여서 두 열에서 상보적인 조합을 떠올릴 수 있으나 실제 접촉이 있다는 관측 자료는 아닙니다. 네 행만으로 통계적 유의성·인과 관계·보상 진화를 입증할 수 없습니다. 구조 유지뿐 아니라 기능 제약이나 공통 조상에서도 패턴이 생길 수 있음을 예고합니다. AlphaFold가 이 네 행에서 손으로 표시한 두 열만 사용하는 것은 아니며 많은 위치와 학습한 구조 규칙을 함께 처리합니다. 여기서는 계산 공식을 배우기보다 한 서열에 없는 비교 정보가 MSA에 생긴다는 점을 이해시킵니다. 마지막에 C가 모두 같다는 것을 학생이 직접 가리키도록 합니다.

[intro_af2_overview] EMBL-EBI / Google DeepMind: AlphaFold2 high-level overview
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/a-high-level-overview/
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957
[evo_ebi_msa] EMBL-EBI Training: Multiple sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/multiple-sequence-alignment/

## 4. MSA가 중요한 이유 · 구조를 추론할 단서를 보강 (5–7분)

왜 이 강의에서 AlphaFold 버튼 사용에 앞서 진화를 배우는지 연결합니다. MSA는 표적 한 줄에서 직접 측정할 수 없는 보존과 위치 간 조합 패턴을 제공하므로 구조 추론에 도움이 됩니다. 깊고 다양한 정렬은 이런 단서를 보강할 수 있지만 낮은 coverage·잘못된 정렬·중복된 계열은 행이 많아도 유용한 정보를 보장하지 않습니다. 학습된 모델의 사전 지식도 작용하므로 결과를 MSA 정보만의 산물로 설명하지 않습니다. 이 설명은 MSA가 없으면 어떤 경우에도 구조를 만들 수 없다는 주장도 아닙니다. 마지막 30초에는 ‘같은 query에서 MSA만 바꾸면 무엇이 달라지나’를 구두로 묻습니다. 답은 모델 가중치나 표적 서열 자체가 아니라 예측 때 제공하는 진화적 단서입니다. Depth를 줄이면 행 수와 표집 다양성이, clustering은 선택하는 서열 계열과 조합 분포가, masking은 특정 열의 잔기와 조합 정보가 달라집니다. 이 때문에 같은 query라도 다른 구조 후보가 나올 수 있으나 항상 달라지거나 더 정확해지는 것은 아닙니다. 원하는 상태·평형 점유율을 지정하는 명령이 아니며 후보는 신뢰도와 실험으로 검증합니다. 다음 장의 homology·ortholog·paralog는 바로 ‘MSA 행들은 어떤 관계인가’를 답하기 위한 개념입니다.

[intro_af2_overview] EMBL-EBI / Google DeepMind: AlphaFold2 high-level overview
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/a-high-level-overview/
[intro_msa_quality] EMBL-EBI / Google DeepMind: Customising AlphaFold structure predictions
https://www.ebi.ac.uk/training/online/courses/alphafold/advanced-modeling-and-applications-of-predicted-protein-structures/customising-alphafold-structure-predictions/
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957
[subsampling_paper] del Alamo et al. (2022), Sampling alternative conformational states of transporters and receptors with AlphaFold2
https://elifesciences.org/articles/75751
[afcluster_paper] Wayment-Steele et al. (2024), Predicting multiple conformations via sequence clustering and AlphaFold2
https://www.nature.com/articles/s41586-023-06832-9
[afsample2_paper] Kalakoti and Wallner (2025), AFsample2 predicts multiple conformations and ensembles with AlphaFold2
https://www.nature.com/articles/s42003-025-07791-9

## 5. Homology: 얼마나 닮았나보다 어디에서 왔나 (7–9분)

도입의 질문 ‘MSA에 모인 서열들은 어떤 관계인가?’를 이어받습니다. 상동성은 두 서열의 진화적 기원에 대한 관계이고, 동일성은 정렬에서 측정하는 양입니다. 실제 분석에서는 상동 여부의 근거가 강하거나 약할 수 있지만, 상동성을 백분율로 표시하지 않습니다. 높은 서열 동일성은 상동성 추론의 근거가 될 수 있으나 짧은 구간의 우연한 일치만으로 전체 단백질의 기원을 판단하지 않습니다. Similarity는 어떤 치환을 비슷하다고 볼지 점수 체계에 의존한다는 점도 구분합니다.

[evo_ncbi_glossary] NCBI BLAST Glossary
https://www.ncbi.nlm.nih.gov/books/NBK62051/?report=reader
[evo_ebi_sequence] EMBL-EBI Training: Primary structure—Why sequence matters
https://www.ebi.ac.uk/training/online/courses/foundations-protein-structure/fundamentals-of-protein-composition/the-peptide-bond-and-primary-structure/ss/

## 6. Ortholog와 paralog: 갈라진 사건을 묻는다 (9–11분)

오늘은 유전자 중복과 종 분화를 중심으로 한 단순한 진화 모형을 사용합니다. 두 유전자를 거슬러 올라가 만나는 가장 최근 공통 조상 노드가 종 분화이면 ortholog, 유전자 중복이면 paralog입니다. 서로 다른 종에 존재하는 paralog도 있으므로 종이 다르다는 이유만으로 ortholog라고 부르면 안 됩니다. 이 관계는 기능 실험 결과가 아니라 진화 사건으로 정의됩니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_ensembl_tree] Ensembl: Protein trees
https://www.ensembl.org/info/docs/compara/homology_method.html

## 7. Species tree와 gene tree는 다른 질문 (11–13분)

종 계통수의 말단은 종이고 유전자 계통수의 말단은 개별 유전자입니다. 따라서 한 종에서 유전자가 중복되면 gene tree에는 같은 종 이름을 가진 말단이 여러 개 나타납니다. 실제 연구에서는 유전자 계통수를 종 계통수와 대조하는 reconciliation을 통해 중복과 종 분화를 추론합니다. 여기서는 분기 길이와 시간 축은 생략하고 사건의 순서만 읽습니다.

[evo_ensembl_tree] Ensembl: Protein trees
https://www.ensembl.org/info/docs/compara/homology_method.html

## 8. 예제 1: 종 분화보다 먼저 중복되었다면 (13–15분)

먼저 조상 유전자가 1번과 2번 계열로 중복되고, 이후 A와 B가 종 분화한 가상 사례입니다. A_1과 B_1의 가장 최근 공통 조상은 왼쪽 S이므로 ortholog입니다. A_1과 A_2 또는 A_1과 B_2를 거슬러 올라가면 가장 최근 공통 조상은 맨 위 D이므로 두 쌍 모두 paralog입니다. 특히 A_1과 B_2는 다른 종에 있는 paralog라는 점을 손가락으로 경로를 짚어 설명합니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_ensembl_loss] Ensembl archived documentation: Gene Orthology/Paralogy prediction method
https://may2009.archive.ensembl.org/info/docs/compara/homology_method.html

## 9. 예제 2: 종 분화 뒤에 중복되었다면 (15–17분)

이번에는 종 분화가 먼저 발생하고 A 계통 안에서만 유전자가 중복되었습니다. A_1과 A_2를 비교하면 D에서 만나지만, 어느 쪽을 B_1과 비교하든 S에서 만나므로 각각 ortholog입니다. 따라서 orthology는 반드시 일대일 관계일 필요가 없으며 여기서는 일대다 관계입니다. Co-ortholog라는 표현은 무엇에 대한 관계인지 기준 상대인 B_1을 함께 말해야 정확합니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_ensembl_types] Ensembl: Homology types
https://mart.ensembl.org/info/genome/compara/homology_types.html

## 10. Paralog는 종 안에도, 종 사이에도 있다 (17–18분)

이 표는 앞의 두 계통수를 한 번 더 정리하는 장입니다. Within-species와 between-species는 현재 유전자가 어느 종에 있는지를 말하고, inparalog와 outparalog는 기준 종 분화보다 중복이 나중인지 이전인지를 말합니다. 따라서 같은 종에 있는 paralog라는 사실만으로 중복이 그 종에서 최근에 일어났다고 결론 내릴 수 없습니다. 초보 단계에서는 세부 명칭 암기보다 D와 S의 순서를 먼저 설명하게 합니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_ensembl_loss] Ensembl archived documentation: Gene Orthology/Paralogy prediction method
https://may2009.archive.ensembl.org/info/docs/compara/homology_method.html

## 11. 유전자 소실: 남은 하나끼리 비교하면 생기는 착시 (18–20분)

고대 중복 후 A에서는 2번 계열, B에서는 1번 계열이 사라진 가상 사례입니다. 현재 남은 A_1과 B_2만 보면 각 종에 하나씩 있는 대응처럼 보이지만, 이들의 가장 최근 공통 조상은 D입니다. 그러므로 서로 paralog이며 단순한 일대일 검색 결과로 진화 역사를 확정할 수 없습니다. 실제 자료에서는 소실뿐 아니라 불완전한 조립이나 주석 누락도 유전자가 없어 보이는 이유가 될 수 있음을 덧붙입니다.

[evo_ensembl_loss] Ensembl archived documentation: Gene Orthology/Paralogy prediction method
https://may2009.archive.ensembl.org/info/docs/compara/homology_method.html
[evo_ensembl_tree] Ensembl: Protein trees
https://www.ensembl.org/info/docs/compara/homology_method.html

## 12. 바로 실습 · Ortholog와 paralog 판정 (20–24분)

개인 풀이 1분, 짝 토론 1분, 전체 해설 2분으로 운영합니다. 정답은 A_x–A_y가 D에서 만나는 paralog, A_x–B_z와 A_y–B_z가 각각 S에서 만나는 ortholog입니다. A_x와 A_y는 B_z에 대한 co-orthologs이며, 서로가 ortholog라는 뜻은 아닙니다. 종이 다르다는 이유만 쓴 답에는 가장 최근 공통 조상 노드를 표시하도록 다시 요청하고, 화면을 읽기 어려운 학생에게는 동일 내용을 구두로 설명합니다. 활동지 1쪽을 이어서 사용합니다. 상황 A의 H_A–M_A는 S에 의한 ortholog, H_A–H_B와 H_A–M_B는 D에 의한 paralog입니다. 상황 B에서 H1–H2는 paralog, H1/H2는 각각 M의 ortholog이며 M에 대한 co-orthologs입니다. 4분 안에는 화면 예제와 활동지 1번을 우선 풀고 나머지는 해설·확장 문항으로 둡니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf

## 13. Ortholog여도 기능이 완전히 같지는 않다 (24–25분)

Ortholog는 기능을 추론할 때 유용하지만 모든 생물학적 기능이 동일하다는 정의는 아닙니다. 기능은 촉매 작용, 기질, 발현 조직, 상호작용 상대 등 여러 층위로 나뉘므로 어느 층위의 유사성을 말하는지 명시해야 합니다. 실제 기능 자료를 비교한 연구도 ortholog와 paralog의 차이를 통계적 경향으로 다루며 절대 규칙으로 다루지 않습니다. 구조 예측용 MSA에는 목적에 따라 여러 상동 계열이 포함될 수 있으므로 ortholog만 남겨야 한다는 규칙도 자동으로 적용하지 않습니다.

[evo_function] Altenhoff et al. (2012). Resolving the Ortholog Conjecture. PLOS Computational Biology.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002514
[evo_ensembl_tree] Ensembl: Protein trees
https://www.ensembl.org/info/docs/compara/homology_method.html

## 14. 유전자 가족에서 MSA로: 대응 위치를 제안한다 (25–27분)

계통수를 통해 누가 누구와 관련되는지 생각했다면, 이제 각 서열의 어느 위치끼리 비교할지 정해야 합니다. MSA는 삽입과 결실을 고려해 대응한다고 보는 잔기들을 같은 열에 배치합니다. 특히 짧은 반복, 매우 다른 길이, 도메인 구성이 다른 서열에서는 정렬의 불확실성이 커질 수 있습니다. 이후 구조 예측에서 사용되는 정보는 이런 대응 관계에 영향을 받으므로 행 수를 세기 전에 정렬 자체를 읽는 습관을 들입니다.

[evo_ebi_msa] EMBL-EBI Training: Multiple sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/multiple-sequence-alignment/
[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki

## 15. MSA 읽기: 행·열·query·gap (27–30분)

가상 정렬에서 한 행을 가로로 읽으면 하나의 단백질 서열을, 한 열을 세로로 읽으면 대응한다고 본 위치들의 상태를 읽습니다. Query의 세 번째 열에는 잔기가 없으므로 이 열의 정렬 번호와 query의 잔기 번호는 다릅니다. Gap은 이 위치에 정렬된 잔기가 없다는 표시이지 미지의 아미노산이라는 기호가 아닙니다. 이 짧은 예시는 MSA 문법을 위한 것이며 실제 단백질의 구조나 기능을 예측할 수 있는 자료가 아닙니다.

[evo_ebi_msa] EMBL-EBI Training: Multiple sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/multiple-sequence-alignment/

## 16. Gap 하나가 잔기 번호를 바꾼다 (30–32분)

같은 정렬을 다시 사용해 query의 D가 정렬에서는 4열이지만 원래 서열에서는 3번 잔기임을 확인합니다. 구조 파일의 잔기 번호나 실험에서 사용한 construct 번호는 여기서도 다시 달라질 수 있으므로 별도 대응이 필요합니다. 또한 seq_A의 Q를 query 대비 삽입으로 표현할 수 있어도 어느 조상에서 실제 삽입 또는 결실이 일어났는지는 이 정렬만으로 결정하지 못합니다. 이후 마스킹 위치를 정할 때 번호 체계를 혼동하지 않도록 기록 단위를 명시합니다.

[evo_ebi_pairwise] EMBL-EBI Training: Pairwise sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/pairwise-sequence-alignment/

## 17. FASTA: 이름 줄과 서열 줄부터 읽기 (32–33분)

헤더와 서열을 분리해 읽는 것만으로 많은 입력 실수를 줄일 수 있습니다. 첫 번째 줄의 synthetic이라는 말은 자료의 출처 설명이며 단백질 서열에 포함되지 않습니다. 서열 길이가 서로 다를 수 있는 일반 FASTA와 gap을 넣어 대응 열을 맞춘 aligned FASTA를 구분합니다. 일반 FASTA에서 대소문자가 가지는 의미는 도구에 따라 다를 수 있으므로 다음 장의 A3M 규칙을 모든 FASTA 파일에 그대로 적용하지 않습니다.

[evo_ncbi_fasta] NCBI: BLAST QuickStart—Query and Database Sequence Formats
https://www.ncbi.nlm.nih.gov/books/NBK1734/?report=reader

## 18. A3M: 대문자와 소문자는 서로 다른 역할 (33–36분)

A3M에서는 삽입 열의 빈칸을 생략할 수 있어 텍스트 줄의 길이가 달라 보입니다. 예시의 소문자 q는 삽입 잔기이고 대문자 Y는 query의 F와 다른 잔기지만 같은 match 열에 대응합니다. 소문자를 제외해 읽으면 각 행의 match와 deletion 위치는 여덟 개이며 query의 위치와 맞출 수 있습니다. 삽입 정보의 처리 방식은 예측 파이프라인마다 다르므로 파일 원본을 무조건 대문자로 바꾸거나 모든 소문자를 임의 삭제해서 저장하지 않습니다.

[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki

## 19. 바로 실습 · A3M의 열과 삽입 읽기 (36–40분)

실제 실습 파일 이름은 practice/README.md를 따른다. 소문자 insertion은 정렬 열로 세지 않는다. 다만 파서가 그 삽입 길이를 별도 특징으로 활용할 수 있으므로 소문자를 무의미한 문자라고 설명하지 않는다. Gap은 해당 정렬 위치의 잔기가 없는 대응, X는 잔기 종류를 알 수 없거나 가렸다는 표식이다. Subsampling은 진화적 다양성과 특정 위치의 coverage를 함께 바꿀 수 있다. 컴퓨터가 없는 학생은 활동지의 A3M 발췌를 사용한다. 진행 2분 풀이+2분 해설. 답: query 포함7행, homolog6행, 정렬12열. A2의 ee는4열 직전 insertion이며 원문14글자와 정렬12열은 다릅니다. A3의 gap은5열, B1의 X는11열입니다. 활동지2쪽4번 Neff 질문은 해당 설명 직후 구두로 이어갑니다.

[core_af3_input] AlphaFold 3 official input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 20. Coverage와 identity: 분모를 함께 적는다 (40–42분)

이 강의의 계산 예에서는 coverage를 query 전체 잔기 중 상대 잔기와 짝지어진 위치의 비율로 정의합니다. Identity는 두 서열 모두 잔기가 있는 비교 위치 중 같은 잔기의 비율로 계산합니다. 실제 프로그램은 gap 포함 여부나 길이 기준이 달라질 수 있으므로 출력 문서를 확인하고 숫자만 비교하지 않습니다. 100% identity라도 query의 아주 짧은 부분만 덮는 hit는 전체 단백질이 동일한 특징을 가진다는 근거가 되지 않습니다.

[evo_ncbi_glossary] NCBI BLAST Glossary
https://www.ncbi.nlm.nih.gov/books/NBK62051/?report=reader
[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki

## 21. 바로 실습 · Coverage와 identity 계산 (42–45분)

개인 계산 1분 후 짝과 분모를 확인하고 1분 동안 해설합니다. 정답은 A가 비교 위치 4개 모두 같으므로 coverage 4/8=50%, identity 4/4=100%입니다. B는 비교 위치 8개 중 6개가 같으므로 coverage 8/8=100%, identity 6/8=75%입니다. 어느 하나가 무조건 더 좋은 MSA 입력이라고 정하기보다는 길이, 상동성 근거, 정렬 신뢰도와 분석 목적을 함께 확인한다는 답으로 마무리합니다.

[evo_ncbi_glossary] NCBI BLAST Glossary
https://www.ncbi.nlm.nih.gov/books/NBK62051/?report=reader

## 22. Conservation: 한 열에서 무엇이 유지되는가? (45–47분)

각 열을 세로로 읽고 어떤 잔기가 얼마나 자주 나타나는지 확인합니다. 예시에서 첫 번째 열은 모두 A이지만 두 번째 열은 C와 S로 달라집니다. 보존은 구조 안정성이나 기능적 제약과 관련될 수 있지만 표집된 서열이 서로 너무 비슷해 보존적으로 보이는 경우도 있습니다. 네 개의 짧은 가상 서열만으로 생물학적 중요도를 추정하지 않고 개념을 익히는 데만 사용합니다.

[evo_ebi_sequence] EMBL-EBI Training: Primary structure—Why sequence matters
https://www.ebi.ac.uk/training/online/courses/foundations-protein-structure/fundamentals-of-protein-composition/the-peptide-bond-and-primary-structure/ss/
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957

## 23. 보존·공변이·공진화는 서로 다른 질문 (47–49분)

학생에게 MSA를 세로와 가로로 번갈아 보게 합니다. Ortholog와 paralog는 서로 다른 행인 유전자들의 기원에 붙이는 이름이고, residue coevolution은 정렬에서 대응하는 위치들의 진화적 의존성을 묻습니다. 두 잔기가 ortholog라는 표현은 이 문맥에 맞지 않습니다. 문헌에서는 covariation과 coevolution을 넓게 섞어 쓰기도 하지만, 오늘은 관찰된 통계적 의존성과 그 원인에 관한 진화적 해석을 구별합니다. 공변이를 보았다고 구조적 상호작용 때문에 공진화했다고 바로 결론 내리지 않습니다. 두 열이 완전히 보존되어 있으면 중요한 접촉이 실제 존재하더라도 이 자료의 변화 패턴으로 의존성을 판별하기 어렵다는 점도 짚습니다. 여기서 함께 진화한다는 것은 여러 세대에 걸친 서열 제약의 의존성을 뜻합니다. 단백질의 두 잔기가 시간에 따라 같은 방향으로 움직이는 동역학적 상관과는 다른 개념입니다.

[coevo_miyazawa] Miyazawa (2013). Prediction of Contact Residue Pairs Based on Co-Substitution between Sites in Protein Structures. PLOS ONE.
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0054252
[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf

## 24. 한 위치의 선택은 다른 위치에 달릴 수 있다 (49–51분)

D는 aspartate, K는 lysine이며 보통의 생리적 pH에서 측쇄가 각각 음전하와 양전하를 띤다는 단순화를 사용합니다. 실제 전하와 안정성은 환경, 거리, 배향, 용매, 다른 잔기 등에 의존하므로 이 표를 모든 단백질의 규칙으로 설명하지 않습니다. 한 위치의 치환 효과가 다른 위치의 상태에 달라지는 생각이 epistasis입니다. 보상적 치환은 한 변화의 영향을 다른 변화가 완화하는 가능한 설명입니다. 그러나 D–K와 K–D 두 조합을 나란히 보았다고 D–K에서 K–K를 거쳐 K–D로 진화했다고 읽을 수 없습니다. 화살표나 시간 순서를 그리지 않은 이유를 말해 줍니다. 이 장은 물리적 직관을 위한 가상 모형이며 다음 MSA 빈도 예제에 실제 접촉이나 보상 치환을 부여하지 않습니다. 접촉하는 잔기들이 서로 맞는 크기나 전하 조합을 유지하면 단백질의 접힘과 기능을 보존하는 데 기여할 수 있습니다. 따라서 서로 먼 서열 위치 사이의 조합 정보가 3차원 공간의 근접성을 추정하는 단서가 됩니다. 공진화가 두 돌연변이의 동시 발생을 뜻하지는 않습니다.

[coevo_miyazawa] Miyazawa (2013). Prediction of Contact Residue Pairs Based on Co-Substitution between Sites in Protein Structures. PLOS ONE.
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0054252

## 25. 두 열의 빈도와 조합 빈도를 따로 센다 (51–54분)

표의 각 숫자는 그 잔기 조합을 가진 서열 행의 수입니다. 예를 들어 오른쪽 위의 4는 i에 D와 j에 K가 같은 서열 안에서 함께 나타난 행이 네 개라는 뜻입니다. 주변 빈도 marginal frequency는 한 열만 보고 셉니다. i가 D인 행은 4/8, j가 K인 행도 4/8입니다. 두 열이 독립적이라면 이 비율들을 곱한 1/4, 즉 여덟 행 중 두 행 정도의 조합 빈도를 기대하지만 여기서는 네 행입니다. 이는 교육용 자료에서 관찰한 분포와 독립 분포를 비교한 것이며, 여덟 개 생물학적 독립 표본으로 유의성 검정을 한 것이 아닙니다. 원하면 MI = sum P(a,b) log2[P(a,b)/(P(a)P(b))]라고 소개합니다. 이 가상 표의 경험적 MI는 1 bit이며 0 빈도 항의 기여는 0으로 처리합니다. 계산값 자체는 계통 효과를 제거하지 않으며 접촉 점수나 AlphaFold 신뢰도도 아닙니다.

[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957

## 26. 즉시 실습: 같은 열 빈도, 다른 조합 (54–57분)

학생 실습지의 coevolution 페이지 첫 계산과 연결합니다. 1분 개인 계산, 1분 짝 비교, 1분 강사 해설로 운영합니다. 두 자료 모두 P(D_i)=1/2, P(K_j)=1/2이므로 독립일 때 D–K의 빈도는 1/4입니다. 자료 P의 실제 D–K 빈도는 4/8=1/2, 자료 Q는 2/8=1/4입니다. Q에서는 네 조합이 모두 각각 1/4이므로 이 경험적 분포는 독립입니다. 단일 열의 잔기 분포와 보존도는 동일하므로 그것만으로 둘을 구분할 수 없습니다. 선택 심화 답은 경험적 MI가 P에서 1 bit, Q에서 0 bit라는 것입니다. Q에 공변이가 없다는 관찰도 실제 단백질에서 접촉이 없음을 입증하지 않습니다. P에 공변이가 있다는 관찰도 직접 접촉을 입증하지 않습니다. 작은 가상 표로 통계적 유의성이나 실제 공진화를 판정하지 않는다고 마무리합니다.

[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957

## 27. 휴식 (57–67분)

첫 번째 휴식. 방금 계산한 두 열의 상관이 무엇 때문에 생겼는지 생각해 두게 합니다. 다음 구간에서 ortholog의 공통 조상과 paralog 혼합을 같은 데이터에 연결합니다.



## 28. Ortholog를 모아도 공통 조상은 남아 있다 (67–70분)

Ortholog는 종 분화로 갈라진 유전자 관계이지 서로 독립적으로 실험한 시료라는 뜻이 아닙니다. 어느 조상 가지에서 D–K 조합이 생긴 뒤 많은 후손에게 전달되었다면, 말단 서열의 반복 개수를 치환 사건 수로 셀 수 없습니다. 여러 떨어진 가지에서 관련 변화가 반복되는지 묻는 것이 더 적절하지만, 이를 판단하려면 계통수와 치환 모형 등 추가 가정이 필요합니다. Ortholog를 선택하면 고대 중복으로 분리된 다른 계열을 섞는 일을 줄일 수 있으나 phylogenetic non-independence 자체를 없애지는 못합니다. 서열 재가중도 이 문제를 완벽히 제거하지 않습니다. 따라서 ortholog 선택, 정렬 품질, 계통 구조, 서열 다양성은 서로 다른 확인 항목입니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957
[evo_weighting] Hockenberry & Wilke (2019). Phylogenetic Weighting Does Little to Improve the Accuracy of Evolutionary Coupling Analyses.
https://www.mdpi.com/1099-4300/21/10/1000
[coevo_miyazawa] Miyazawa (2013). Prediction of Contact Residue Pairs Based on Co-Substitution between Sites in Protein Structures. PLOS ONE.
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0054252

## 29. Paralog 혼합은 계열 차이를 함께 섞는다 (70–72분)

계열 A에서는 i가 D이고 j가 K, 계열 B에서는 반대라고 가정하면 A와 B의 비중이 두 열의 조합 빈도를 함께 결정합니다. 이런 패턴에는 계열 분기 역사가 들어 있으므로 전체 MSA의 상관만으로 반복적인 잔기 보상을 추론할 수 없습니다. 곧바로 다음 장의 숫자를 직접 나눠 보게 합니다. 구조 예측과 DCA는 일반적으로 상동 단백질 가족의 정보를 활용하며 입력을 반드시 ortholog-only로 제한하는 정의가 아닙니다. Paralog도 공통 구조 제약을 알려 줄 수 있으므로 모두 제거하면 충분한 다양성까지 잃을 수 있습니다. 반대로 정렬되지 않는 도메인이나 매우 다른 기능 계열을 무조건 합치는 것도 바람직하지 않습니다. 가족별 비교는 원인을 점검하는 분석이며, 진짜 공진화가 전혀 없다는 증명이 아닙니다.

[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957
[coevo_pairing] Gandarilla-Pérez et al. (2023). Combining phylogeny and coevolution improves the inference of interaction partners among paralogous proteins. PLOS Computational Biology.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011010

## 30. 즉시 실습: 계열을 나누면 무엇이 보이나? (72–75분)

화면 표를 읽기 전에 다음 가정이 화면과 실습지에 제시되어 있음을 확인합니다: H/M/R/F는 네 가상 종이며, 유전자 중복으로 A/B가 나뉜 뒤 네 종이 분화했고 추가 중복·소실은 없습니다. 실제 종의 약자가 아닙니다. 이 가정은 반드시 학생에게 읽어 줍니다. 1분 관계 판정, 1분 전체·계열별 비교, 1분 해설로 운영합니다. 정답: A_H–A_M은 ortholog, A_H–B_H와 A_H–B_M은 paralog입니다. 각 A 또는 B 계열 안에서는 이 두 위치에 변이가 없으므로 이 표만으로 계열 내부의 coevolution을 검출할 근거가 없습니다. 전체에서는 앞 장의 자료 P와 같이 D–K와 K–D만 각각 네 번 나타납니다. 이 의존성은 계열 구분과 겹치므로 반복적인 보상 치환이나 직접 접촉으로 바로 해석하면 안 됩니다. 여덟 행은 여덟 번의 독립 치환이 아니며 조상 상태와 실제 변화 횟수도 이 표로 결정하지 못합니다. 추가 근거로 더 넓은 계통 표집, 신뢰할 만한 정렬·계통수, 계열 내부 변이, 실제 구조 등을 제안하게 합니다. 여기 A/B는 주어진 가상 유전자 역사에 따른 중복 계열입니다. 별도 파일 practice/fictional_learning.a3m의 group A/B는 편의를 위한 교육용 라벨이며 ortholog/paralog 관계를 추론한 집단이 아닙니다. 두 자료를 같은 MSA로 연결하지 않습니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957

## 31. 복합체에서는 어떤 서열끼리 짝지었는가? (75–77분)

앞의 A/B 하위 계열 예제와 혼동하지 않도록 이번에는 서로 상호작용할 수 있는 두 단백질 가족을 P와 Q라고 부릅니다. 단백질 내부의 coevolution은 한 가족의 MSA에서 열쌍을 비교합니다. 단백질 사이의 분석에서는 P와 Q의 MSA 행을 상호작용 상대에 맞춰 대응시키는 문제가 추가됩니다. 한 종에 P1/P2와 Q1/Q2가 모두 있으면 종 이름만으로 올바른 상대가 정해지지 않습니다. 다른 종의 ortholog 관계, 유전체 맥락, 알려진 상호작용 및 서열 신호가 pairing을 돕지만 보장은 아닙니다. 잘못 연결한 행은 단백질 사이 신호를 약화시키거나 왜곡할 수 있습니다. AlphaFold 3의 입력 문서에서 말하는 MSA pairing 역시 행 대응을 구성하는 절차이며 실험적인 결합 확인을 뜻하지 않습니다. 단일 단백질의 상동 MSA 선택과 복합체의 파트너 pairing을 구분하게 합니다.

[coevo_pairing] Gandarilla-Pérez et al. (2023). Combining phylogeny and coevolution improves the inference of interaction partners among paralogous proteins. PLOS Computational Biology.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011010
[af3_input] Google DeepMind AlphaFold 3 input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 32. 함께 변한다고 모두 직접 연결된 것은 아니다 (77–79분)

칠판에 i—k—j를 그리고 i와 j 사이의 직접 선은 그리지 않습니다. 가운데 k를 통한 연결만으로 두 끝 위치의 관찰 분포가 연관될 수 있다는 직관을 설명합니다. Direct Coupling Analysis는 모든 위치를 함께 고려하는 통계 모형에서 쌍별 coupling을 추정해 단순한 두 열 상관의 간접 효과를 분리하려는 접근입니다. 여기서 direct는 해당 통계 모형 안에서의 뜻이지 물리적 인과 관계가 검증되었다는 뜻이 아닙니다. 표집, 계통 효과, 정렬 오류와 모형 한계가 남을 수 있습니다. AlphaFold 2는 Evoformer에서 MSA 표현과 잔기쌍 표현을 상호 갱신하며 구조 학습을 활용합니다. 따라서 MI를 계산해 높은 값끼리 붙이거나 고전적 DCA만 실행하는 절차로 설명하면 부정확합니다. AlphaFold 3 역시 이 장의 가상 MI 계산을 그대로 구조로 변환하는 도구가 아니며 세부 구조는 AF2와 다릅니다. 이 장에서는 입력 정보와 학습된 추론을 구분하는 데 초점을 둡니다.

[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957
[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2
[core_af3] Abramson et al. (2024), Accurate structure prediction of biomolecular interactions with AlphaFold 3
https://www.nature.com/articles/s41586-024-07487-w

## 33. Raw depth와 Neff: 행 수와 다양성은 다르다 (79–82분)

가중치 합으로 정의하는 한 방식에서는 각 서열과 충분히 비슷한 이웃 수를 자기 자신까지 포함해 센 뒤 그 역수를 가중치로 사용합니다. 모두 같은 서열 100개라면 각 가중치는 1/100이므로 합은 1입니다. 이것은 교육용 재가중 예시이며 HH-suite의 엔트로피 기반 Neff 등 다른 정의와 수치를 그대로 비교할 수 없습니다. Neff는 실제 독립 표본 수의 정답도 아니고 구조 예측 정확도를 보장하는 점수도 아닙니다. 마지막30초에 활동지2쪽4번을 구두로 확인합니다. 같은 행 복제는 raw depth를 높여도 새로운 독립적 진화 사건을 만들지 않습니다.

[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki
[evo_weighting] Hockenberry & Wilke (2019). Phylogenetic Weighting Does Little to Improve the Accuracy of Evolutionary Coupling Analyses.
https://www.mdpi.com/1099-4300/21/10/1000

## 34. AlphaFold2와 AlphaFold3 (82–83분)

AF2와 AF3를 단순한 정확도 순위로 소개하지 않는다. AF2의 monomer 모델은 단백질 중심이며 복합체용 AlphaFold-Multimer가 별도로 있다. AF3는 단백질 외 분자들을 함께 다루고 diffusion 기반 좌표 생성을 사용한다. 단백질 MSA는 AF3에도 사용된다. AF2에서 관찰한 MSA 조작 효과가 AF3에서도 동일한 크기와 방식으로 나타난다고 가정하면 안 된다. 모델을 바꾸면 MSA 처리 방식과 점수의 의미도 함께 확인한다.

[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2
[core_af3] Abramson et al. (2024), Accurate structure prediction of biomolecular interactions with AlphaFold 3
https://www.nature.com/articles/s41586-024-07487-w

## 35. 웹 서버와 로컬 실행 (83–84분)

AlphaFold Server와 공개 AF3 로컬 코드는 입력 기능과 실행 환경이 같지 않다. 웹 화면에서 로컬 JSON의 모든 항목을 조절할 수 있다고 설명하지 않는다. 초보자는 ColabFold 노트북에서 서열 입력과 결과 파일을 먼저 경험한다. 교사는 강의 전에 접속 가능 여부와 GPU 할당을 확인하고 동일한 실습 파일을 준비한다. 수업은 오프라인 정렬 실습과 결과 판독만으로도 끝낼 수 있으며, 실제 예측 시연은 사전 준비한 환경에서 선택적으로 진행한다. 실행법은 examples/README.md에 제공한다.

[core_cf] ColabFold official repository
https://github.com/sokrypton/ColabFold
[core_af3_input] AlphaFold 3 official input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 36. Custom MSA의 기본 조건 (84–85분)

같은 단백질의 대안 구조를 비교하는 실습이므로 query를 고정한다. 소문자를 대문자로 바꾸면 삽입이 정렬 열로 오해되어 열 대응이 깨질 수 있다. 줄마다 문자열 길이가 달라도 lowercase insertion을 제외한 정렬 길이는 같아야 한다. Gap과 unknown X의 의미는 다르다. 헤더는 서열 식별과 일부 파이프라인의 종 정보 해석에 쓰일 수 있으므로 무작위로 바꾸는 것을 구조 제어 방법이라고 가르치지 않는다. 복합체 pairing은 별도의 대응 문제다.

[core_cf] ColabFold official repository
https://github.com/sokrypton/ColabFold
[core_af3_input] AlphaFold 3 official input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 37. ColabFold 1 · 접속과 실습 준비 (85–87분)

공식 전체 URL은 슬라이드 하단과 examples/colabfold_walkthrough.md에 있습니다. ColabFold의 AlphaFold2 노트북이며 AlphaFold Server의 AF3 화면과 다릅니다. 브라우저 주소창에 표시된 URL을 붙여 넣고 실행 가능한 Google 계정으로 로그인합니다. 개인 사본 저장은 노트북 설정을 보존하는 선택 사항이며 Colab에서 임시 실행할 수도 있습니다. 먼저 교사가 공개 calmodulin 서열과 수업용 폴더를 학생에게 제공합니다. 12열짜리 fictional_learning.a3m은 실제 예측기에 넣지 않습니다. 수업 중에는 실행 준비와 결과 읽기를 함께 연습하고 실제 GPU 대기 시간은 보장하지 않습니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb
[core_calm] UniProt P0DP23, human calmodulin-1
https://www.uniprot.org/uniprotkb/P0DP23/entry

## 38. ColabFold 2 · GPU와 노트북 실행 방식 (87–89분)

Google Colab 공식 FAQ는 Runtime→Change runtime type에서 hardware accelerator를 고르도록 안내합니다. GPU 종류와 메뉴 표시는 계정·시점에 따라 달라질 수 있으므로 특정 T4가 항상 제공된다고 약속하지 않습니다. 선택 후 연결 상태를 확인합니다. 처음 쓰는 학생에게 셀은 코드와 결과가 붙어 있는 실행 단위라고 설명합니다. 입력 값을 먼저 정한 다음 Run all을 실행합니다. 학생 개인의 승인·로그인이 필요한 화면은 본인이 내용을 확인하고 처리합니다. GPU 사용량과 실행 수명은 제한되며 실제 대기 시간을 수업 시간에 보장하지 않습니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb
[core_colab_faq] Google Colab official FAQ
https://research.google.com/colaboratory/faq.html

## 39. ColabFold 3 · 서열과 기본 조건 입력 (89–91분)

공식 FASTA 직접 주소: https://rest.uniprot.org/uniprotkb/P0DP23.fasta . 브라우저 주소창에 붙여 넣습니다. 파일이 자동 다운로드되지 않고 텍스트가 보이면 페이지 저장(Ctrl+S / macOS Cmd+S)으로 calmodulin_P0DP23.fasta라는 이름으로 저장합니다. HTML이 아니라 >sp|P0DP23|CALM1_HUMAN으로 시작하는 일반 텍스트인지 확인하고, .txt가 자동으로 붙었다면 최종 확장자가 .fasta인지 확인합니다. 저장 없이 화면에서 제목을 제외한 서열 줄만 복사해도 됩니다. examples/calmodulin_P0DP23.fasta를 텍스트로 열고 >sp로 시작하는 설명 줄은 제외합니다. 나머지 서열 줄은 이어 붙이거나 줄바꿈 포함 복사해도 공백이 제거됩니다. 단일 사슬 실습이므로 콜론을 추가하지 않습니다. query_sequence에 기본 예제 서열이 남아 있지 않은지 학생이 확인합니다. jobname은 영문·숫자·밑줄로 간단히 지정합니다. 이 calmodulin 예측에는 Ca2+를 입력하지 않으므로 결과를 실험적 apo 또는 holo 상태로 단정하지 않습니다. num_relax는 후처리 모델 수이며 예측할 서열 수가 아닙니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb
[core_calm] UniProt P0DP23, human calmodulin-1
https://www.uniprot.org/uniprotkb/P0DP23/entry
[core_calm_fasta] UniProt P0DP23 canonical FASTA: human calmodulin-1
https://rest.uniprot.org/uniprotkb/P0DP23.fasta

## 40. ColabFold 4 · Run all과 계산 진행 확인 (91–93분)

입력 폼을 먼저 모두 설정한 뒤 Runtime→Run all을 누릅니다. 공식 노트북은 설치, MSA 옵션, 고급 설정, 예측 셀을 순서대로 실행합니다. 초기 모델 다운로드와 MSA 서버 대기 등이 포함되므로 완료 시간은 고정하지 않습니다. num_seeds=1이 구조 하나를 뜻하지 않습니다. 현재 노트북의 Run Prediction은 num_models=5로 실행합니다. 첫 기준 예측과 후속 조건에서 모델 수와 seed 수를 맞춥니다. 중간에 실패하면 에러가 발생한 셀과 마지막 문구를 기록하고, 입력 변경 뒤에는 마지막 셀만 다시 누르지 않고 위쪽 입력부터 다시 실행합니다. 코드를 수정하지 않는 초급 경로를 가르칩니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

## 41. ColabFold 5 · 결과와 MSA 다운로드 (93–95분)

공식 노트북의 Package and download results 셀은 생성한 결과 ZIP을 다운로드합니다. 브라우저가 다운로드를 막았거나 자동 다운로드가 보이지 않으면 셀 결과와 왼쪽 Files 패널의 jobname.result.zip을 확인해 직접 다운로드합니다. 작업 폴더 이름에는 query 해시와 재실행 번호가 붙을 수 있습니다. 압축을 풀어 .a3m을 찾아 실제 calmodulin MSA로 보존하고, 다음 custom 조건에 이 파일을 재사용합니다. 3D 화면의 lDDT 색은 모델 pLDDT 신뢰도 표시이며 experimental B-factor와 같은 뜻이 아닙니다. 순위1이 물리적으로 가장 많이 존재하는 상태라는 뜻도 아닙니다. 실제 ZIP 파일 이름은 jobname 출력값을 기준으로 확인합니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

## 42. lDDT · 기준 구조의 주변 거리가 얼마나 보존되었나? (95–97분)

lDDT는 구조 예측 전부터 쓰던 정확도 평가 지표이며 Mariani 등의 2013년 논문이 정의와 검증을 제시했습니다. 이름의 맨 앞 l은 local입니다. 중심 잔기 주변의 3차원 이웃을 평가하며 서열에서 앞뒤 몇 잔기만 고르는 뜻이 아닙니다. 기준 구조의 거리가 15 Å 미만인 쌍을 고른 뒤 같은 쌍의 예측 거리를 비교합니다. 15 Å는 이웃 선택 반경이고 0.5·1·2·4 Å는 거리 오차의 네 허용치입니다. 모든 좌표를 같이 회전·이동해도 내부 거리는 유지되므로 전체 구조의 중첩이 필요 없습니다. 그러나 같은 잔기·원자를 대응시켜야 합니다. 원 논문의 all-atom 평가와 아래 AF2의 Cα-only 계산을 구별합니다. AF2 구현은 자기 자신과 기준 좌표가 없는 위치를 제외하고 원 lDDT의 stereochemistry 보정은 생략합니다. 이 설명은 AF2/ColabFold 기준이며 AF3의 원자별 정의를 그대로 대체하지 않습니다.

[confidence_lddt_paper] Mariani et al. (2013), lDDT: a local superposition-free structure comparison score
https://pmc.ncbi.nlm.nih.gov/articles/PMC3799472/
[confidence_lddt_code] Google DeepMind AlphaFold2: lddt.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/lddt.py

## 43. 직접 계산 · 네 이웃의 거리 오차를 네 번 채점 (97–99분)

실제 단백질 좌표에서 얻은 값이 아니라 중심 잔기 i와 네 이웃 사이 거리를 가정한 계산 예입니다. 기준 거리 4·7·10·14 Å는 모두 15 Å 미만입니다. 예측에서 d가 17 Å로 멀어져도 기준에서 선택한 이웃이므로 계산에서 빼지 않습니다. 오차 0.2는 네 기준, 0.8은 세 기준, 1.5는 두 기준, 3.0은 한 기준을 통과합니다. 총 16개 검사 중 10개를 통과하므로 0.625입니다. 각 허용치별 보존 비율 1/4·2/4·3/4·4/4를 평균해도 같습니다. 62.5는 lDDT의 100점 표시이며 pLDDT가 아닙니다. 이 값은 중심 잔기 하나의 점수입니다. 전체 구조의 lDDT를 모든 잔기별 점수의 단순평균이라고 일반화하지 않습니다. 각 잔기에 속한 이웃 수가 다를 수 있기 때문입니다. 임계값에 정확히 걸리는 예를 피했으며 AF2 코드는 엄격한 미만(<) 비교를 사용합니다.

[confidence_lddt_paper] Mariani et al. (2013), lDDT: a local superposition-free structure comparison score
https://pmc.ncbi.nlm.nih.gov/articles/PMC3799472/
[confidence_lddt_code] Google DeepMind AlphaFold2: lddt.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/lddt.py

## 44. 바로 실습 · 예측 거리가 더 멀어지면? (99–100분)

30초 구두 또는 손계산, 30초 해설로 진행합니다. d의 절대 거리 오차는 5 Å여서 네 검사 모두 실패합니다. 따라서 (4+3+2+0)/16=9/16=0.5625, 100점 척도 56.25입니다. 이웃 선택은 기준 구조에서 하므로 기준 거리 14 Å인 d는 계속 포함합니다. 계산에서 빼면 틀린 거리를 벌점 없이 제거하는 오류가 됩니다. 활동지 5쪽의 기본 표는 앞 슬라이드를 보며 채우고 이 시간에는 변경 문항만 풉니다. pLDDT 확률 계산과 정답 구조 필요 여부 문항은 다음 학습·추론 설명 뒤 구두 확인 또는 수업 후 확장에 사용합니다.

[confidence_lddt_code] Google DeepMind AlphaFold2: lddt.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/lddt.py

## 45. pLDDT가 나온 과정 · 채점한 lDDT를 학습 정답으로 (100–102분)

lDDT는 기준 구조가 있을 때만 채점할 수 있습니다. 새 서열은 그 기준 구조를 모르는 경우가 많으므로, AlphaFold2는 잔기별 lDDT-Cα 자체를 예상하는 보조 출력인 pLDDT를 학습합니다. p는 predicted를 뜻합니다. 구조 모듈의 잔기별 내부 표현을 작은 신경망에 넣어 50개 구간의 logits를 출력합니다. 학습 중 모델이 만든 Cα 좌표와 학습용 기준 좌표를 비교하여 정답 점수를 계산하고, 점수에 해당하는 구간을 cross-entropy로 지도합니다. 0.625라면 폭 0.02인 [0.62,0.64) 구간입니다. 기준 좌표를 신뢰도 head 입력으로 주는 것이 아니라 손실의 정답을 만드는 데 사용합니다. 정답 점수는 현재 예측 좌표에 따라 달라지며 pLDDT head만을 위한 수작업 confidence 라벨을 사람이 달지 않습니다. 코드에서는 정답 점수에 stop_gradient를 적용합니다. 여러 seed의 구조가 서로 얼마나 닮았는지를 계산하여 점수를 만드는 방식도 아닙니다. 여기서는 AF2의 학습 구조를 설명하며 학생이 ColabFold에서 재학습한다는 뜻이 아닙니다.

[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2
[confidence_af2_head] Google DeepMind AlphaFold2: PredictedLDDTHead
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/modules.py#L998-L1089
[confidence_af2_config] Google DeepMind AlphaFold2: predicted_lddt configuration
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/config.py
[confidence_lddt_code] Google DeepMind AlphaFold2: lddt.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/lddt.py

## 46. 새 서열에서는 정답 없이 pLDDT를 출력한다 (102–104분)

pLDDT는 predicted local Distance Difference Test입니다. 추론 시 새 표적의 정답 구조는 입력하지 않고, 이미 학습된 모델의 내부 표현으로 신뢰도 분포를 출력합니다. softmax는 50개의 logits를 합이 1인 확률로 바꿉니다. 실제 AF2의 구간 중심은 0.01,0.03,…,0.99입니다. 각 중심에 예측 확률을 곱해 더한 기대값에 100을 곱합니다. 표는 실제 50개 중심 중 0.49·0.69·0.89만 고르고 나머지 확률은 0으로 이상화한 교육용 계산입니다. 유한 logits의 softmax에서 정확히 0이 나온다는 주장이 아닙니다. 합은 0.049+0.138+0.623=0.810으로 81점입니다. 가장 확률이 큰 0.89만 골라 89점으로 보고하지 않습니다. 확률분포는 점수 구간에 대한 것이며 pLDDT를 곧바로 구조 정답의 확률로 읽지 않습니다. 실제 lDDT는 나중에 기준 구조가 확보되면 따로 계산하고 pLDDT와 비교할 수 있습니다. AF2/ColabFold는 잔기별 점수이며 AF3의 원자별 출력은 정의와 범위를 따로 확인합니다. 예측 PDB의 B-factor 칸에 pLDDT가 저장되어도 실험 열운동 인자는 아닙니다.

[confidence_af2_code] Google DeepMind AlphaFold2: confidence.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/common/confidence.py
[confidence_af2_config] Google DeepMind AlphaFold2: predicted_lddt configuration
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/config.py
[confidence_afdb] AlphaFold Protein Structure Database: FAQ and confidence interpretation
https://alphafold.ebi.ac.uk/faq
[core_af3_output] AlphaFold 3 official output documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/output.md

## 47. pLDDT의 네 가지 색 · 숫자와 함께 읽기 (104–106분)

범위를 빈틈없이 표시하기 위해 공식 AF2 confidence.py의 50·70·90 경계 포함 방식을 사용했습니다. 웹 범례에는 >90 등 간략한 표기가 있을 수 있습니다. 진한 파랑은 국소 원자 배열을 정밀하게 검토할 출발점이지만, 모든 곁사슬·리간드 접촉이 맞다는 보증은 아닙니다. 하늘색은 골격이 대체로 타당해도 일부 곁사슬 방향은 다를 수 있습니다. 주황 영역은 유연성이나 intrinsically disordered region일 가능성도 있고, 모델에 정보가 부족했을 가능성도 있습니다. 점수만으로 둘을 판별하지 않습니다. 69와70을 완전히 다른 생물학적 상태로 분리하지 말고 연속적인 신뢰도 변화로 읽게 합니다. 실제 ColabFold 3D 화면에서 색을 잔기 번호·점수 그래프와 대응시키며, 체인별 색상으로 바뀌어 있지 않은지 범례를 확인하게 합니다.

[ebi_plddt] EMBL-EBI / Google DeepMind training: pLDDT, Understanding local confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/
[confidence_af2_code] Google DeepMind AlphaFold2: confidence.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/common/confidence.py

## 48. 평균 82.8점이 가리는 낮은 신뢰도 구간 (106–108분)

좌표를 예측한 결과가 아니라 강사가 만든 점수입니다. 도메인을 실제 5잔기로 만든 단백질이 있다는 뜻이 아니라, 도메인 내부와 연결부의 차이를 12개 위치로 줄인 도식입니다. 기존 12열 fictional_learning.a3m과 calmodulin의 결과도 아닙니다. 학생과 왼쪽부터 점수를 따라 읽습니다: 94,93,91,90,88,43,39,86,92,94,93,91. 합계994를12로 나누면82.833…이며 소수점 한 자리로82.8입니다. A의 합계456/5와 B의 합계456/5는 각각91.2이고 연결부82/2는41.0입니다. 평균 하나만 보고 모든 부분이 비슷하게 믿을 만하다고 판단하면 두 낮은 위치를 놓칩니다. 반대로 연결부가 낮다고 양쪽의 국소 구조를 모두 버리지 않습니다. 그래프의 가로축은 잔기 위치, 세로축은 pLDDT임을 짚고, 이 점수만으로 A와B의 상대 배치는 결정할 수 없다고 다음 설명을 예고합니다.

[confidence_afdb] AlphaFold Protein Structure Database: FAQ and confidence interpretation
https://alphafold.ebi.ac.uk/faq

## 49. 바로 실습 · pLDDT 그래프에서 말할 수 있는 것 (108–110분)

1분 개인 풀이 뒤1분 해설합니다. 답①6번43,7번39입니다. ②아닙니다. 평균은 낮은 구간을 가릴 수 있습니다. ③둘 다 확정할 수 없습니다. A·B는 각자 국소 구조에 대한 신뢰도가 높지만 서로의 배치에는 별도 정보가 필요합니다. 낮은 연결부 점수는 disorder나 유연성 가설의 출발점이 될 수 있어도 증명은 아닙니다. 낮은 값과 비정형 구조라는 생물학적 결론 사이에 정보 부족 등 다른 원인이 있음을 말하게 합니다. 91.2가A와B의 같은 모양을 뜻한다는 오답도 교정합니다. 점수는 구조 모양 자체가 아니라 그 예측에 대한 신뢰도입니다. 계산기나 컴퓨터 없이 그래프의 두 낮은 위치를 가리키는 방식으로도 진행합니다. 학생 활동지에는 정답을 적지 않았으며 이 노트만 교사용 해설입니다.

[ebi_plddt] EMBL-EBI / Google DeepMind training: pLDDT, Understanding local confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/
[confidence_afdb] AlphaFold Protein Structure Database: FAQ and confidence interpretation
https://alphafold.ebi.ac.uk/faq

## 50. PAE · 기준을 고정하면 다른 위치는 얼마나 불확실할까? (110–113분)

피 에이 이라고 읽습니다. 두 손을 도메인 A와B로 삼아 A를 기준으로 붙잡고 B의 위치를 얼마나 확신하는지 묻는 비유를 사용합니다. 정확한 정의는 예측 구조와 참 구조를 잔기 j의 국소 좌표계에 정렬한다고 가정했을 때, 잔기 i에서 예상되는 위치 오차입니다. AF2의 기준 잔기에는 위치뿐 아니라 N–Cα–C로 정한 방향도 있으므로 원자 하나만 겹친다는 뜻으로 설명하지 않습니다. 정답 구조를 실제로 열어 계산한 측정 오차가 아니라 모델이 예측한 오차이며, 각 잔기 쌍에 값이 있어 길이N이면 N×N 표가 됩니다. 이 수업 표에서는 행이 평가 대상 i, 열이 기준 j라고 먼저 약속합니다. 실제 뷰어·원시 배열은 축과 인덱스 정의를 확인합니다. PAE3 Å를 ‘두 잔기가3 Å만큼 떨어져 있다’로 읽지 않습니다. 실제 둘 사이가30 Å 떨어져 있어도 상대 배치를 잘 확신하면 낮은 PAE일 수 있습니다. 낮은 값일수록 신뢰도가 높은 점은 pLDDT와 방향이 반대입니다.

[ebi_pae] EMBL-EBI / Google DeepMind training: PAE, A measure of global confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/
[confidence_af2_code] Google DeepMind AlphaFold2: confidence.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/common/confidence.py
[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2

## 51. PAE 표 읽기 · 도메인 내부와 도메인 사이 (113–115분)

먼저 A3은 domain A의3번 표시 위치, B9는 domain B의9번 표시 위치임을 설명합니다. 앞 그래프의12×12 전체 PAE를 제시한 것이 아니라 네 위치만 뽑은4×4 교육용 표입니다. 연결부6·7에 대한 PAE는 여기 없습니다. 대각선0은 설명을 단순화한 값으로 실제 출력이 모두 정확히0이라는 주장이 아닙니다. 왼쪽 위A–A와 오른쪽 아래B–B의 대각선 밖 값1,2를 읽고 내부 배치를 비교적 확신한다고 말합니다. 이어 오른쪽 위A–B의18–21과 왼쪽 아래B–A의22–24는 상대 배치에 큰 불확실성이 있음을 보여 줍니다. A3행/B9열18은B9를 기준으로A3을 평가한 값이고, B9행/A3열24는 기준과 대상을 바꾼 값입니다. 방향을 바꾸면 다른 기준 좌표계에서 다른 위치를 평가하므로 PAE는 대칭일 필요가 없습니다. 18과24를 단백질 두 위치 사이의 상반된 거리 측정으로 해석하지 않습니다. 표를 평균으로 줄이기 전에 블록과 양방향을 읽습니다.

[ebi_pae] EMBL-EBI / Google DeepMind training: PAE, A measure of global confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/
[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2

## 52. 두 점수 함께 읽기 · 부분의 모양과 상대 배치 (115–117분)

조립 블록 두 개의 모양은 잘 만들었지만 두 블록을 연결하는 방향은 모를 수 있다는 비유로 국소 구조와 상대 배치를 구분합니다. 앞 가상 예제에서 도메인 A·B의 국소 구조를 검토할 근거는 있지만, 두 도메인 사이의 정확한 접촉면을 자신 있게 설명할 근거는 부족합니다. 높은 도메인 사이 PAE는 그 배치의 불확실성이지 실제 동적 이동을 측정한 결과가 아닙니다. 유연한 hinge, 부족한 정보 등 가능한 설명을 구별하려면 다른 예측 조건과 실험 자료가 필요합니다. 반대로 낮은 PAE는 모델이 배치를 확신한다는 뜻입니다. 물리적으로 두 단백질이 결합하는지, 결합력이 얼마인지, 어느 상태가 몇 퍼센트인지와는 다른 질문입니다. MSA subsampling·clustering으로 모델을 여러 개 만들 때도 pLDDT와 관련 PAE 블록을 먼저 읽고 실제 좌표의 차이와 비교합니다. pLDDT 최고 모델 하나만으로 다른 후보를 모두 버리지 않도록 연결합니다.

[ebi_plddt] EMBL-EBI / Google DeepMind training: pLDDT, Understanding local confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/
[ebi_pae] EMBL-EBI / Google DeepMind training: PAE, A measure of global confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/
[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2

## 53. 바로 실습 · 같은 pLDDT, 다른 PAE (117–120분)

2분 짝 토의와1분 해설로 진행합니다. ①B9의 국소 좌표계를 기준으로 정렬했을 때 A3의 예상 위치 오차가18 Å이고, A3을 기준으로 했을 때B9는24 Å입니다. 둘은 다른 기준에서의 예측 오차이며 물리적인 잔기 사이 거리가 아닙니다. ②제시한 네 위치에 관해서는 Q가 A–B 상대 배치를 더 확신합니다. pLDDT가 같아도 PAE에서 이 차이가 나타납니다. Q의 낮은 값이 실험적으로 더 정확하다는 보증은 아니며, Q라는 상태가 더 많이 존재한다거나 P에서Q로 전이하는 속도를 말해주지 않습니다. 연결부6·7의 pLDDT는 Q에서도43·39로 그대로 낮습니다. 또한 선택한4×4만으로 생략한 모든 위치의 상대 배치가 확실하다고 확대하지 않습니다. 마지막에 학생에게 한 문장 결론을 쓰게 합니다: ‘Q는 제시된 도메인 간 위치에 대한 모델 신뢰도가 더 높지만, 실제 구조·점유율은 추가 검증이 필요하다.’ 앞 pLDDT 실습과 같은 가상 데이터이며 실제 GPU 추론을 한 결과가 아닙니다.

[confidence_afdb] AlphaFold Protein Structure Database: FAQ and confidence interpretation
https://alphafold.ebi.ac.uk/faq
[ebi_pae] EMBL-EBI / Google DeepMind training: PAE, A measure of global confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/

## 54. 휴식 (120–130분)

두 번째 휴식. pLDDT와 PAE의 차이를 한 문장씩 떠올리게 합니다. 이후 ColabFold custom MSA 경로와 입력 조작별 실습을 이어서 진행합니다.



## 55. ColabFold 6 · Custom MSA 업로드 (130–132분)

MSA options 코드 셀이 실행될 때 파일 업로드 창이 나타납니다. 단순히 드롭다운만 바꾸어서는 업로드가 시작되지 않습니다. 현재 코드는 첫 번째 선택 파일을 사용하고 첫 서열로 query_sequence를 갱신하므로, UI 입력만 같다고 안심하지 말고 업로드한 A3M의 query를 반드시 비교합니다. 기본 검색 결과 A3M을 그대로 올려 custom 입력 경로를 먼저 확인한 뒤 depth를 비교합니다. 실제 AF-Cluster의 각 cluster A3M도 같은 경로로 한 번에 한 파일씩 넣습니다. Masking 파일도 도구가 만든 정상 A3M과 동일 query일 때 같은 방식으로 입력합니다. 이 강의의 12열 가상 A3M이나 단순 라벨 분할 파일을 실제 CALM1 입력에 섞지 않습니다. 각 조건은 별도 jobname과 다운로드 파일로 보관합니다. 상세 클릭 경로는 examples/colabfold_walkthrough.md에 있습니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

## 56. AF3에서 custom MSA 지정 (132–133분)

이 예시는 필드의 뜻을 읽는 용도다. sequence 자리에는 실제 query 전체가 필요하다. unpairedMsaPath는 JSON 파일 기준 상대 경로나 절대 경로다. pairedMsa의 빈 문자열은 paired MSA를 쓰지 않는다는 뜻이며 templates의 빈 목록은 template을 제공하지 않는다는 뜻이다. 필드를 생략하는 것과 명시적으로 빈 값으로 만드는 것은 처리 결과가 다를 수 있다. Path 필드는 입력 포맷 version 2부터 지원한다. examples/prepare_inputs.py가 실제 서열과 MSA의 일치를 확인하고 실행용 JSON을 만든다.

[core_af3_input] AlphaFold 3 official input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 57. 한 번에 한 조건씩 비교 (133–135분)

표본 수가 다르면 더 많은 계산을 한 방법이 유리할 수 있다. 방법 간 생성 구조 수, seed 목록, template 유무, 모델 버전과 recycling 설정을 맞춘다. Depth는 query를 포함하는지 기록한다. 입력 MSA 행 수와 모델 내부 max-msa의 두 한도는 구분한다. 어느 조건이 대안 구조를 더 잘 회수하는지는 동일한 평가 기준으로 비교한다. 이 실습에서는 결과를 예상해서 서열을 골라 넣기보다 조작의 의미와 대조군을 설명하는 데 중점을 둔다. Depth·group·mask 세 조건은 모두 원본 MSA에서 각각 만들며 앞 조건의 출력에 다음 조작을 연속 적용한 자료가 아닙니다.

[core_cf] ColabFold official repository
https://github.com/sokrypton/ColabFold

## 58. 바로 실습 · 공정한 비교 설계 (135–138분)

1분 개인 판단, 1분 짝 토론, 1분 공유로 운영한다. 기기가 없으면 종이에 A 또는 B와 이유를 적는다. 강사용 답: B가 행 선택 효과를 분리하기에 낫다. A는 query, template, 반복 수가 함께 바뀌어 차이의 원인을 구별하기 어렵다. B도 선택한 행 집합·MSA 유효 다양성·동일 seed 집합·코드 버전을 기록해야 재현과 해석이 가능하다. 이 답은 학생 화면에 먼저 보여주지 않는다. 한 조건씩 비교하는 원리를 설명한 직후 활동지4쪽4번을 풉니다. 실제 조작 파일은 뒤의 각 방법 설명 직후 만들어 확인합니다.

[afcluster_critique] Schafer et al. (2025), Sequence clustering confounds AlphaFold2
https://www.nature.com/articles/s41586-024-08267-2
[afcluster_response] Wayment-Steele et al. (2025), Does Sequence Clustering Confound AlphaFold2?
https://doi.org/10.1016/j.jmb.2025.169376
[ebi_inputs] EMBL-EBI / Google DeepMind training: AlphaFold2 inputs and outputs recap
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap/

## 59. 기준 예측부터 기록한다 (138–139분)

이 단원의 질문은 같은 단백질에 대해 다른 구조 후보를 얻을 수 있는가이다. 첫 결과를 지우지 말고 baseline으로 보관한다. 학생에게 서열 길이까지 달라지면 무엇을 비교한 것인지 물어본다. MSA 조작의 효과를 비교할 때 query와 모델 버전, template 조건, 반복 수를 맞춘다. 뒤에서 소개할 원래 SPEACH_AF는 query도 편집하는 예외이므로, 오늘의 query 유지 실습과 구분한다.

[ebi_inputs] EMBL-EBI / Google DeepMind training: AlphaFold2 inputs and outputs recap
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap/
[afcluster_code] AF-Cluster author repository and ClusterMSA.py
https://github.com/HWaymentSteele/AF_Cluster/blob/main/scripts/ClusterMSA.py
[speach_code] SPEACH_AF author notebook: SPEACH_AF_scan.ipynb
https://github.com/RSvan/SPEACH_AF/blob/main/SPEACH_AF_scan.ipynb

## 60. 행을 줄인다: MSA subsampling (139–141분)

아래 정렬은 원리를 설명하기 위한 가상 여덟 자리 예시이며 실제 단백질이 아니다. Query를 보존한 채 homolog 1과 3만 택한 경우를 손으로 표시하게 한다. Subsampling은 서열의 이름을 바꾸는 일이 아니라 실제 들어가는 행의 집합을 바꾸는 일이다. 같은 개수라도 중복된 서열 위주인지, 다양한 homolog를 포함하는지에 따라 정보가 달라진다. 깊이가 얕을수록 항상 더 좋은 것은 아니며 잘못 접힌 결과도 늘 수 있다.

[subsampling_paper] del Alamo et al. (2022), Sampling alternative conformational states of transporters and receptors with AlphaFold2
https://elifesciences.org/articles/75751

## 61. 바로 실습 · Depth를 줄인 MSA (141–144분)

개인1분·확인1분·해설1분. 기본 실행은 depth4/seed7이며 query,A2,A3,B1을 남깁니다. Query 포함4행, 정렬12열이고 query는 예측 대상이므로 보존합니다. 원본7행 대비 남긴 계통·열별 잔기빈도·조합빈도가 달라질 수 있습니다. 프로그램은 세 조건 파일을 한 번에 만들지만 여기서는 subsample만 봅니다. 뒤의 group과 mask도 원본7행에서 각각 만들어진 독립 조건입니다. 컴퓨터가 없으면 활동지의 지정4행을 표시합니다. 작은 가상 MSA에 실제 coevolution 유의성 검정을 적용하지 않습니다.



## 62. 논문 그림 읽기: 얕은 MSA의 효과와 한계 (144–146분)

del Alamo 등의 eLife 연구는 일부 수송체와 수용체를 시험했다. 확대한 A 패널에서 점의 색으로 MSA 깊이를 구분하고, 실험 구조와 예측을 겹친 보기를 확인한다. 구조를 더 많이 만들었다는 사실과 정확한 다른 구조를 찾았다는 사실을 분리한다. 원 논문에서는 깊이와 template 선택이 표적마다 달랐으며 모든 단백질에 통하는 최적 깊이를 정하지 못했다. 이 결과를 모든 단백질의 자유에너지 분포를 재현했다는 주장으로 바꾸지 않는다. 슬라이드에는 원본 Figure 1의 A 패널만 확대하여 표시한다. 점의 색상별 MSA depth와 해당 구조 비교를 읽는다.

[subsampling_paper] del Alamo et al. (2022), Sampling alternative conformational states of transporters and receptors with AlphaFold2
https://elifesciences.org/articles/75751

## 63. ColabFold 7 · 화면에서 MSA depth 비교 (146–149분)

Advanced settings 아래 Sample settings를 펼칩니다. 현재 공식 노트북의 max_msa 선택지는 auto,512:1024,256:512,64:128,32:64,16:32입니다. 두 비교 조건에는 동일한 실제 calmodulin A3M을 업로드하고 model_type=alphafold2_ptm, num_recycles=3, num_seeds=1, use_dropout=False, template_mode=none을 함께 유지합니다. 웹 노트북은 기본적으로 다섯 모델을 사용하므로 두 조건을 모두 같은 방식으로 실행합니다. Runtime→Run all로 입력 셀부터 다시 실행하며 jobname은 조건별로 다르게 적습니다. 입력 MSA 행 수가 한도보다 작으면 그만큼만 사용됩니다. 이 설정은 교육용 비교이며 대안 상태 생성이나 정확도 향상을 보장하지 않습니다. CLI 예시는 examples/README.md에 따로 있습니다. 웹 UI에는 128:256 선택지가 없으므로 CLI 예시와 혼동하지 않습니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

## 64. AF-Cluster: 서열을 먼저 나누어 예측 (149–152분)

그림에서 먼저 나누는 대상은 아직 구조가 없는 서열들임을 짚는다. AF-Cluster는 서열 유사성으로 만든 작은 MSA들을 예측에 사용한다. 그림 속 KaiB는 생체시계 단백질이며 알려진 두 접힘과 예측을 비교하는 교육 예시이다. 이 성공 사례가 모든 단백질의 숨은 상태를 찾아준다는 보장은 아니다. 논문은 온라인 2023년, Nature 권호는 2024년이므로 참고문헌 연도가 다른 이유를 짧게 설명한다. 실제 실행 단계는 examples/afcluster_guide.md를 사용한다. 공식 ClusterMSA.py의 positional 인자와 flags를 확인한 명령, query 보존 검사, cluster별 ColabFold 실행이 들어 있다. 이 자료 제작 중 실제 GPU 예측은 실행하지 않았다.

[afcluster_paper] Wayment-Steele et al. (2024), Predicting multiple conformations via sequence clustering and AlphaFold2
https://www.nature.com/articles/s41586-023-06832-9
[afcluster_code] AF-Cluster author repository and ClusterMSA.py
https://github.com/HWaymentSteele/AF_Cluster/blob/main/scripts/ClusterMSA.py

## 65. 각 cluster에도 같은 query가 들어간다 (152–153분)

AF-Cluster 저자 코드에서 query는 처음에 분리되고 각 cluster 파일을 쓸 때 다시 맨 앞에 붙는다. 가상 정렬에서 두 입력의 첫 줄이 완전히 같은지 학생이 확인하게 한다. 서열 cluster에 query와 먼 homolog가 포함될 수 있어도 예측 대상은 첫 query이다. 이것은 각 cluster의 대표 homolog 구조를 각각 예측하는 실험과 다른 질문이다. 실습에서는 query를 변경하거나 원본을 덮어쓰지 않는다.

[afcluster_code] AF-Cluster author repository and ClusterMSA.py
https://github.com/HWaymentSteele/AF_Cluster/blob/main/scripts/ClusterMSA.py

## 66. 바로 실습 · 서열 그룹별 입력 비교 (153–156분)

1분 파일 읽기, 1분 비교, 1분 해설로 진행합니다. 각 그룹은 query 1행과 해당 homolog 3행으로 총 4행입니다. 교육용 header의 group=A/B에 따라 미리 분리했으며 거리 기반 AF-Cluster를 구현한 것이 아닙니다. A homolog의 5열은 F,F,gap이고 B의 5열은 Y,Y,Y입니다. A의 11열은 M,M,M이고 B는 X,gap,X입니다. 두 열을 비교해 선택한 서열 집합이 잔기 분포와 coverage까지 바꿈을 확인합니다. Coevolution 활동지 3쪽에서는 가상 gene history를 주었지만 이 파일에는 ortholog/paralog 판정 근거가 없습니다. Cluster마다 같은 query를 넣어도 구조 상태 분류나 공진화 증명이 되지는 않습니다. 실제 clustering 명령은 examples/afcluster_guide.md로 시연합니다.



## 67. 서열 cluster는 열역학적 상태가 아니다 (156–157분)

앞 단원에서 배운 종분화와 유전자 중복을 연결한다. Ortholog와 paralog는 진화 사건에 대한 관계이고 open과 closed는 구조 상태에 대한 말이다. 서열 유사성만으로 만든 집합은 ortholog만을 보장하지 않으며 기능적 분화도 포함할 수 있다. 어떤 sequence cluster에서 구조가 잘 나왔다는 사실만으로 그 집합이 특정 열역학적 상태를 뜻한다고 부르지 않는다. 종별 서열 데이터 수가 많다는 사실도 분자의 상태 점유율과는 무관하다.

[afcluster_paper] Wayment-Steele et al. (2024), Predicting multiple conformations via sequence clustering and AlphaFold2
https://www.nature.com/articles/s41586-023-06832-9
[afcluster_response] Wayment-Steele et al. (2025), Does Sequence Clustering Confound AlphaFold2?
https://doi.org/10.1016/j.jmb.2025.169376

## 68. 2025년 논쟁: 비교 조건을 읽는다 (157–158분)

Schafer 등은 Nature Matters Arising에서 CF-random과 비교하고 evolutionary coupling 해석에 이의를 제기했다. Wayment-Steele 등의 2025년 JMB 응답은 비교 조건의 혼입을 지적하고 추가 분석으로 반박했다. 두 문헌을 함께 소개하며 한쪽의 제목을 확정된 결론처럼 읽지 않는다. 학생에게 비교에서 MSA 깊이, 모델 설정, seed 수가 달라지면 어느 요인의 효과인지 구분 가능한지 묻는다. 여기서 보편적 우승 방법을 정하지 않고 연구 질문에 맞는 대조 실험의 중요성을 가르친다.

[afcluster_critique] Schafer et al. (2025), Sequence clustering confounds AlphaFold2
https://www.nature.com/articles/s41586-024-08267-2
[afcluster_response] Wayment-Steele et al. (2025), Does Sequence Clustering Confound AlphaFold2?
https://doi.org/10.1016/j.jmb.2025.169376

## 69. 두 가지 clustering을 구별한다 (158–159분)

Clustering이라는 단어만 보지 말고 무엇을 어떤 거리로 묶었는지 확인하게 한다. 입력에서는 정렬된 서열의 차이를 이용한다. 출력에서는 적절히 정렬한 좌표나 도메인 간 거리, 접촉 양상처럼 질문에 맞는 구조 특징을 이용한다. 입력이 세 그룹이어도 출력이 두 구조 그룹일 수 있고 반대도 가능하다. 이 표는 일반 분석 설계이며 특정 논문의 cluster 수를 재현한 자료가 아니다.

[afcluster_code] AF-Cluster author repository and ClusterMSA.py
https://github.com/HWaymentSteele/AF_Cluster/blob/main/scripts/ClusterMSA.py
[afsample2_code] wallnerlab/AFsample2 author repository
https://github.com/wallnerlab/AFsample2

## 70. 열을 가린다: unknown X와 gap의 차이 (159–161분)

이 예시는 AFsample2의 아이디어를 가상 정렬로 설명한다. Homolog의 네 번째 정렬 위치만 X로 가렸고 query는 그대로임을 확인한다. X를 gap으로 대신 쓰면 같은 의미가 아니며, 열 자체를 지우면 길이와 좌표 대응도 바뀐다. A3M에서는 소문자 insertion이 정렬 열에 그대로 세어지는 것이 아니므로 실제 입력에서는 포맷을 이해해야 한다. 여기서는 모두 대문자와 gap만 있는 작은 정렬로 열의 의미에 집중한다.

[afsample2_paper] Kalakoti and Wallner (2025), AFsample2 predicts multiple conformations and ensembles with AlphaFold2
https://www.nature.com/articles/s42003-025-07791-9
[af3_input] Google DeepMind AlphaFold 3 input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 71. 바로 실습 · 정렬 열을 X로 가리기 (161–164분)

1분 손계산, 1분 출력 대조, 1분 해설로 진행합니다. A2의 결과는 ACDeeEXGXIKXMN입니다. Query, 소문자 ee, 기존 gap은 보존하고 homolog의 5·7·10열 잔기 정체를 가립니다. 먼저 파일 전체를 대문자로 바꾸면 삽입이 정렬 열이 되어 잘못된 위치를 가리게 됩니다. 선택 열의 기존 gap은 그대로 두며 X는 gap과 다릅니다. Mask는 해당 열의 보존도와 다른 열과의 조합 정보를 함께 약화시킬 수 있습니다. 실제 모델의 X 처리와 다른 입력에 따라 예측 반응이 다르므로 특정 접촉만 선택적으로 꺼졌다고 해석하지 않습니다.



## 72. SPEACH_AF와 AFsample2는 같은 편집이 아니다 (164–166분)

Alanine은 실제 아미노산 A이고 unknown X와 다르다. 원 SPEACH_AF 논문과 저자 notebook은 선택한 위치를 정렬의 모든 서열에서 A로 편집하며 query도 포함하고 gap은 유지한다. 따라서 query를 고정한 마스킹 실습을 원 논문의 정확한 재현이라고 부르면 안 된다. AFsample2 논문은 query 첫 행을 제외하고 무작위로 선택한 열을 X로 바꾸고 dropout과 결합한다. 이 슬라이드는 방법 개념 비교이며 특정 단백질의 치환 설계를 다루지 않는다.

[speach_paper] Stein and Mchaourab (2022), SPEACH_AF: Sampling protein ensembles and conformational heterogeneity with Alphafold2
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010483
[speach_code] SPEACH_AF author notebook: SPEACH_AF_scan.ipynb
https://github.com/RSvan/SPEACH_AF/blob/main/SPEACH_AF_scan.ipynb
[afsample2_paper] Kalakoti and Wallner (2025), AFsample2 predicts multiple conformations and ensembles with AlphaFold2
https://www.nature.com/articles/s42003-025-07791-9

## 73. 논문 그림 읽기: AFsample2의 입력과 출력 (166–168분)

그림 a에서 MSA 가로와 세로 방향을 손으로 가리키며 앞 두 실습을 연결한다. 예측 뒤에는 구조 파일을 분석하여 후보의 품질과 다양성을 확인해야 한다. 논문의 일부 benchmark에서 대안 구조와 비슷한 후보를 더 잘 찾았지만 효과는 표적과 설정에 의존한다. 두 알려진 구조 사이에 보이는 모델은 가능한 중간 구조 가설이며 실제 전이 경로 위에 있다는 증명은 아니다. 슬라이드는 원본 Figure 1a만 확대해 표시한다. 저자의 제안 개념도이며 마스킹이 열림을 일으킨다는 직접 증거가 아니다. 실제 AFsample2에서 query 첫 행은 유지한다.

[afsample2_paper] Kalakoti and Wallner (2025), AFsample2 predicts multiple conformations and ensembles with AlphaFold2
https://www.nature.com/articles/s42003-025-07791-9

## 74. FASTA 제목에 open을 쓰면 열릴까? (168–169분)

학생에게 첫 두 레코드에서 바뀐 것이 실제 아미노산인지 이름인지 묻는다. Open이라고 이름을 붙였다는 이유로 열린 구조를 요구하는 프롬프트가 되는 것은 아니다. 다만 header는 언제나 무의미하다고 설명해서도 안 된다. 일부 multimer 파이프라인은 종 식별 정보를 읽어 MSA pairing에 사용하므로 임의로 바꾸면 입력 처리에 영향을 줄 수 있다. 단량체의 자유로운 별칭과 구조 예측용 생물학적 metadata를 구별한다.

[af3_input] Google DeepMind AlphaFold 3 input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 75. Seed·dropout·template도 별도 요인이다 (169–170분)

Seed를 바꾸면 같은 설정에서 다른 결과가 나올 가능성이 있지만 반드시 다른 구조가 생기지는 않는다. Dropout은 구현이 지원하는 경우에만 추론에서 활성화할 수 있으며, 다양성을 높여도 물리적 온도를 올리는 실험은 아니다. Template은 강한 사전 정보가 될 수 있어 독립적인 발견이라는 주장과 구분한다. 같은 MSA 두 조건을 비교한다면 나머지 설정과 반복 수를 맞추고 모두 기록해야 한다. 이 표는 요인 분리를 위한 설명이며 GPU 실행 지침이 아니다.

[ebi_inputs] EMBL-EBI / Google DeepMind training: AlphaFold2 inputs and outputs recap
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap/
[afsample2_code] wallnerlab/AFsample2 author repository
https://github.com/wallnerlab/AFsample2
[subsampling_paper] del Alamo et al. (2022), Sampling alternative conformational states of transporters and receptors with AlphaFold2
https://elifesciences.org/articles/75751

## 76. AF2 근거를 AF3에 그대로 옮길 수는 없다 (170–171분)

AF3는 단백질 외 분자를 함께 다루는 모델이며 구조 생성 방식도 AF2와 다르다. 로컬 공식 AF3 문서는 custom A3M을 지원하지만 첫 서열과 query의 일치를 요구한다. 공개 AlphaFold Server와 로컬 코드의 입력 제어 범위가 같다고 가정하지 않는다. AFsample3 연구 저장소가 존재함을 확인했으므로 AF3에서는 불가능하다고 단정하지 않는다. 동시에 이 강의의 AF2 benchmark 수치를 AF3의 성능 수치로 제시하지 않는다.

[af3_paper] Abramson et al. (2024), Accurate structure prediction of biomolecular interactions with AlphaFold 3
https://www.nature.com/articles/s41586-024-07487-w
[af3_input] Google DeepMind AlphaFold 3 input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md
[afsample3_code] wallnerlab/afsample3 research implementation
https://github.com/wallnerlab/afsample3

## 77. 바로 실습 · 대안 구조 후보 선택 (171–176분)

practice/synthetic_comparison.json의 8개 중 4개 행을 발췌했다. 가상 180잔기 표적이며 12열 가상 A3M에서 계산한 값이 아니다. 선택 거리는 40번과 140번 Cα 사이 거리이며 PAE는 구간 20–70과 110–160 사이 두 방향 블록의 평균이다. F1/F2는 가까운 거리, S1은 더 먼 거리를 보여 서로 다른 후보를 검토할 수 있다. S2는 낮은 평균 pLDDT와 높은 PAE 때문에 먼저 품질을 확인한다. F2의 평균 pLDDT가 가장 높아도 이 하나만 남기면 다양성을 놓칠 수 있다. 두 상태의 실재 여부나 점유율은 이 가상 표에서 알 수 없다. 전체 8행 비교와 상세 답안은 practice/instructor_answers.md에 있다. MSA 조작 결과를 앞서 배운 pLDDT·PAE로 다시 평가하며 활동지7쪽을 풉니다. 핵심은1번과3번이며 시간이 남으면2번을 토의합니다. 같은 서열 구간과 원자를 정렬해 비교하며 RMSD는 정렬 기준에 따라 달라짐을 설명합니다. 국소 pLDDT와 구간 간 PAE, 원자 충돌, 구조 다양성을 함께 보고 대표 후보를 남깁니다.



## 78. 최종 설명 활동 (176–178분)

첫 주장에는 ortholog 사이에도 남는 공통 조상 효과와 간접 관계, 접촉 검증이 빠졌다. 두 번째에는 서열 cluster와 구조 상태의 대응 검증이 빠졌다. 세 번째에는 샘플링 분포가 물리적 평형분포에 대응한다는 검증이 빠졌다. 학생에게 무조건 틀렸다고 외우게 하기보다 무엇을 추가로 알아야 하는지 묻는다. 평가 기준은 사건 기준으로 관계를 설명하는가, 입력 분할과 구조 분류를 구분하는가, 모델 점수와 물리적 확률을 구분하는가이다. 정답은 배포 활동지에 넣지 않는다.



## 79. 오늘 배운 내용 (178–179분)

학생이 자기 연구 대상에 적용할 때 첫 질문은 어떤 단백질이며 어떤 구조 차이를 확인하려는가이다. 모든 단백질에서 여러 상태를 얻는 것이 수업의 성공 기준은 아니다. 변화를 얻지 못해도 입력 품질과 대조 조건을 확인하면 의미 있는 기록이다. 후속 과제로 benign한 관심 단백질 하나의 accession, 서열 경계, MSA 기준선, 조작 조건, 판정 지표를 제안하도록 할 수 있다.



## 80. 논문과 실행 문서 (179–180분)

관련 문서는 계속 바뀌므로 실제 시연 전에 설치한 버전의 도움말과 공식 문서를 다시 확인한다. 이 강의는 MSA 조작을 손쉽게 상태를 제어하는 보장된 절차로 설명하지 않는다. 모든 수치 예제와 가상 서열은 실제 실험 자료와 명확히 구분한다. 주요 논문과 도구 문서 링크를 소개하고 질문을 받는다.

[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2
[confidence_lddt_paper] Mariani et al. (2013), lDDT: a local superposition-free structure comparison score
https://pmc.ncbi.nlm.nih.gov/articles/PMC3799472/
[core_cf] ColabFold official repository
https://github.com/sokrypton/ColabFold
[ebi_plddt] EMBL-EBI / Google DeepMind training: pLDDT, Understanding local confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/
[ebi_pae] EMBL-EBI / Google DeepMind training: PAE, A measure of global confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/
