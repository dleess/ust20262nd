# MSA와 protein structure 예측 · 강사용 노트

총 180분, 휴식 20분 포함. 각 실습 바로 다음 슬라이드에 정답·상세 해설을 제시합니다. 보충 답안은 content/worksheet_answers.md와 practice/instructor_answers.md에 있습니다.

## 1. MSA와 protein structure 예측 (0–1분)

시작부터 ‘왜 AlphaFold를 배우는데 alignment와 evolution를 먼저 보나요?’에 답합니다. 도입 2–4장은 query에서 MSA와 structure로 이어지는 흐름, 짧은 MSA의 conservation·covariation 예제, 정보의 질과 evolutionary relationship이 중요한 이유를 보여 줍니다. 이후 homology·ortholog·paralog를 배워 alignment에 들어온 sequence들이 어떤 관계인지 읽고, coevolution과 MSA 입력 조작으로 연결합니다. 활동지 1쪽은 evolutionary relationship, 2쪽은 A3M, 3쪽은 coevolution, 4쪽은 입력 조작, 5쪽은 lDDT 계산과 pLDDT training, 6쪽은 pLDDT·PAE, 7쪽은 결과 해석입니다. 교육용 가상 alignment와 실제 calmodulin 예측 입력을 구분합니다.

[intro_af2_overview] EMBL-EBI / Google DeepMind: AlphaFold2 high-level overview
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/a-high-level-overview/
[evo_ebi_msa] EMBL-EBI Training: Multiple sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/multiple-sequence-alignment/

## 2. AlphaFold에서 MSA는 어디에 쓰일까? (1–3분)

먼저 강의 전체의 목적부터 설명합니다. Query는 이번에 structure를 예측할 sequence 하나이며 MSA는 이 target과 관련된 여러 homologous sequence를 대응 위치별로 alignment한 입력입니다. 사용자가 ColabFold에 sequence만 넣어도 일반적인 검색 모드에서는 뒤에서 관련 sequence를 찾고 MSA를 만듭니다. MSA 파일에는 coordinates가 없지만 sequence들을 비교하면서 얻는 evolutionary constraint의 단서가 있습니다. 미리 training된 AlphaFold2는 MSA 표현과 residue쌍 표현을 함께 갱신해 coordinates를 inference하고 confidence를 출력합니다. MSA를 먼저 contact표로 완전히 바꾼 뒤 그 표만 model에 넣는다는 뜻은 아닙니다. Template은 이용할 경우 추가하는 기존 structural information입니다. 새 query마다 MSA를 만드는 것은 입력 준비이며 신경망 weight를 처음부터 다시 training하는 과정이 아닙니다. AF3도 MSA 정보를 사용하지만 Evoformer와 동일한 architecture가 아니라 MSA 처리·Pairformer·diffusion으로 역할이 달라집니다. 오늘 구체적 클릭 실습은 AF2 기반 ColabFold로 진행합니다. 다음 두 장에서 왜 여러 sequence를 비교해야 하는지 본 뒤 이 sequence들의 evolutionary relationship을 배웁니다.

[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2
[intro_af2_overview] EMBL-EBI / Google DeepMind: AlphaFold2 high-level overview
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/a-high-level-overview/
[intro_af2_runtime] Google DeepMind AlphaFold: loading trained parameters and running prediction
https://github.com/google-deepmind/alphafold/blob/main/run_alphafold.py
[intro_af3_overview] EMBL-EBI / Google DeepMind: How does AlphaFold 3 work?
https://www.ebi.ac.uk/training/online/courses/alphafold/alphafold-3-and-alphafold-server/introducing-alphafold-3/how-does-alphafold-3-work/

## 3. sequence 한 줄에서는 보이지 않던 단서가 생긴다 (3–5분)

이 예제는 손으로 만든 8열 alignment이며 실습의 149 residue calmodulin이나 뒤의 12열 A3M과 다른 교육용 자료입니다. Query 한 줄만 보면 C가 이 gene family에서 보존되는지, 3열과6열의 변화가 연결되는지 알 수 없습니다. 여러 행을 나란히 놓으면 2열과8열이 보존되고 3열과6열의 residue 조합이 함께 달라지는 패턴을 볼 수 있습니다. D·E는 negative charge 성질, K·R은 positive charge 성질의 예시여서 두 열에서 상보적인 조합을 떠올릴 수 있으나 실제 contact가 있다는 관측 자료는 아닙니다. 네 행만으로 statistical significance·인과 관계·compensatory evolution를 입증할 수 없습니다. structure 유지뿐 아니라 function 제약이나 common ancestor에서도 패턴이 생길 수 있음을 예고합니다. AlphaFold가 이 네 행에서 손으로 표시한 두 열만 사용하는 것은 아니며 많은 위치와 training한 structure 규칙을 함께 처리합니다. 여기서는 계산 공식을 배우기보다 한 sequence에 없는 비교 정보가 MSA에 생긴다는 점을 이해시킵니다. 마지막에 C가 모두 같다는 것을 학생이 직접 가리키도록 합니다. 다음 장은 다른 가상100 residue target의20·80열을 발췌한 도식입니다. covariation이 어떻게 structural information로 연결되는지 명시적으로 보여 줍니다.

[intro_af2_overview] EMBL-EBI / Google DeepMind: AlphaFold2 high-level overview
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/a-high-level-overview/
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957
[evo_ebi_msa] EMBL-EBI Training: Multiple sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/multiple-sequence-alignment/

## 4. coevolution이 3차원 structural information을 주는 이유 (5–7분)

그림을 왼쪽에서 오른쪽으로 읽으며 coevolution이 어떤 structural information을 주는지 설명합니다. 가상 100 residue 가족의 MSA에서 20번과 80번 열만 발췌했습니다. Query의 D/K와 homologous sequence의 E/R, K/D, R/E는 서로 맞는 charge 조합을 떠올리게 하는 예시입니다. sequence에서 60위치 떨어진 두 residue도 protein이 접히면 공간에서 가까워질 수 있습니다. contact하는 두 residue의 charge·크기·소수성 조합을 유지하려는 선택이 서로 허용되는 substitution을 제약하면, MSA에 두 열의 의존성으로 남을 수 있습니다. 이 evolutionary 흔적을 거꾸로 읽어 contact 후보와 거리·배치 관계를 inference하는 것이 핵심입니다. 중앙 화살표는 training된 model의 structure inference 방향이며 실제 evolution 순서나 물리적 fold 동영상을 뜻하지 않습니다. 오른쪽 사슬은 그린 개념도이며 atom coordinates나 실제 calmodulin 예측이 아닙니다. 한 쌍의 신호가 한 structure를 결정하는 것은 아니며, 여러 위치쌍과 sequence·training된 structure 규칙을 함께 이용합니다. AF2는 MSA 표현과 residue쌍 표현을 함께 갱신합니다. 먼저 MI/DCA로 contact표를 확정한 다음 그것만 structure 모듈에 넣는 파이프라인으로 읽지 않습니다. common ancestor·indirect correlation·function 제약도 같은 패턴을 만들 수 있어 모든 covariation이 direct contact라는 뜻은 아닙니다. 다음 evolutionary relationship 단원은 이 신호를 어떤 sequence들에서 읽는지 판단하기 위한 설명입니다.

[intro_af2_overview] EMBL-EBI / Google DeepMind: AlphaFold2 high-level overview
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/a-high-level-overview/
[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957
[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2

## 5. Homology: 얼마나 닮았나보다 어디에서 왔나 (7–9분)

도입의 질문 ‘MSA에 모인 sequence들은 어떤 관계인가?’를 이어받습니다. homology는 두 sequence의 evolutionary 기원에 대한 관계이고, identity는 alignment에서 측정하는 양입니다. 실제 분석에서는 homologous 여부의 근거가 강하거나 약할 수 있지만, homology를 백분율로 표시하지 않습니다. 높은 sequence identity는 homology inference의 근거가 될 수 있으나 짧은 구간의 우연한 일치만으로 전체 protein의 기원을 판단하지 않습니다. Similarity는 어떤 substitution을 비슷하다고 볼지 점수 체계에 의존한다는 점도 구분합니다.

[evo_ncbi_glossary] NCBI BLAST Glossary
https://www.ncbi.nlm.nih.gov/books/NBK62051/?report=reader
[evo_ebi_sequence] EMBL-EBI Training: Primary structure—Why sequence matters
https://www.ebi.ac.uk/training/online/courses/foundations-protein-structure/fundamentals-of-protein-composition/the-peptide-bond-and-primary-structure/ss/

## 6. Ortholog와 paralog: 갈라진 사건을 묻는다 (9–11분)

오늘은 gene duplication과 speciation을 중심으로 한 단순한 evolution model을 사용합니다. 두 gene을 거슬러 올라가 만나는 MRCA 노드가 speciation이면 ortholog, gene duplication이면 paralog입니다. 서로 다른 species에 존재하는 paralog도 있으므로 species가 다르다는 이유만으로 ortholog라고 부르면 안 됩니다. 이 관계는 function 실험 결과가 아니라 evolution 사건으로 정의됩니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_ensembl_tree] Ensembl: Protein trees
https://www.ensembl.org/info/docs/compara/homology_method.html

## 7. Species tree와 gene tree는 다른 질문 (11–13분)

species tree의 말단은 species이고 gene tree의 말단은 개별 gene입니다. 따라서 한 species에서 gene이 gene duplication되면 gene tree에는 같은 species 이름을 가진 말단이 여러 개 나타납니다. 실제 연구에서는 gene tree를 species tree와 대조하는 reconciliation을 통해 gene duplication과 speciation을 inference합니다. 여기서는 분기 길이와 시간 축은 생략하고 사건의 순서만 읽습니다.

[evo_ensembl_tree] Ensembl: Protein trees
https://www.ensembl.org/info/docs/compara/homology_method.html

## 8. 예제 1: speciation보다 먼저 gene duplication되었다면 (13–15분)

먼저 ancestor gene이 1번과 2번 lineage로 gene duplication되고, 이후 A와 B가 speciation한 가상 사례입니다. A_1과 B_1의 MRCA은 왼쪽 S이므로 ortholog입니다. A_1과 A_2 또는 A_1과 B_2를 거슬러 올라가면 MRCA은 맨 위 D이므로 두 쌍 모두 paralog입니다. 특히 A_1과 B_2는 다른 species에 있는 paralog라는 점을 손가락으로 경로를 짚어 설명합니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_ensembl_loss] Ensembl archived documentation: Gene Orthology/Paralogy prediction method
https://may2009.archive.ensembl.org/info/docs/compara/homology_method.html

## 9. 예제 2: speciation 뒤에 gene duplication되었다면 (15–17분)

이번에는 speciation이 먼저 발생하고 A lineage 안에서만 gene이 gene duplication되었습니다. A_1과 A_2를 비교하면 D에서 만나지만, 어느 쪽을 B_1과 비교하든 S에서 만나므로 각각 ortholog입니다. 따라서 orthology는 반드시 일대일 관계일 필요가 없으며 여기서는 일대다 관계입니다. Co-ortholog라는 표현은 무엇에 대한 관계인지 기준 상대인 B_1을 함께 말해야 정확합니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_ensembl_types] Ensembl: Homology types
https://mart.ensembl.org/info/genome/compara/homology_types.html

## 10. Paralog는 species 안에도, species 사이에도 있다 (17–18분)

이 표는 앞의 두 phylogenetic tree를 한 번 더 정리하는 장입니다. Within-species와 between-species는 현재 gene이 어느 species에 있는지를 말하고, inparalog와 outparalog는 기준 speciation보다 gene duplication이 나중인지 이전인지를 말합니다. 따라서 같은 species에 있는 paralog라는 사실만으로 gene duplication이 그 species에서 최근에 일어났다고 결론 내릴 수 없습니다. 초보 단계에서는 세부 명칭 암기보다 D와 S의 순서를 먼저 설명하게 합니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_ensembl_loss] Ensembl archived documentation: Gene Orthology/Paralogy prediction method
https://may2009.archive.ensembl.org/info/docs/compara/homology_method.html

## 11. gene loss: 남은 하나끼리 비교하면 생기는 착시 (18–20분)

고대 gene duplication 후 A에서는 2번 lineage, B에서는 1번 lineage가 사라진 가상 사례입니다. 현재 남은 A_1과 B_2만 보면 각 species에 하나씩 있는 대응처럼 보이지만, 이들의 MRCA은 D입니다. 그러므로 서로 paralog이며 단순한 일대일 검색 결과로 evolutionary history를 확정할 수 없습니다. 실제 자료에서는 loss뿐 아니라 불완전한 assembly나 annotation 누락도 gene이 없어 보이는 이유가 될 수 있음을 덧붙입니다.

[evo_ensembl_loss] Ensembl archived documentation: Gene Orthology/Paralogy prediction method
https://may2009.archive.ensembl.org/info/docs/compara/homology_method.html
[evo_ensembl_tree] Ensembl: Protein trees
https://www.ensembl.org/info/docs/compara/homology_method.html

## 12. 활동지 1 · Gene tree에서 ortholog·paralog 판정 (20–22분)

화면의 두 H/M gene tree를 비교합니다. 상황 A에서 H_A–M_A는 S에서 만나 ortholog, H_A–H_B와 H_A–M_B는 D에서 만나 paralog입니다. 상황 B에서 H1–H2는 paralog이고, H1/H2는 각각 M에 대해 ortholog이며 M 기준 co-orthologs입니다. 가장 비슷한 sequence라는 정보만으로 분기 사건을 확정할 수 없으며 gene tree·species tree와 duplication·speciation·loss 이력이 필요합니다. 바로 다음 두 정답 화면에서 근거를 확인합니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf

## 13. 정답·해설 · 상황 A: gene duplication 뒤 speciation (22–23분)

상황 A에서 gene duplication D로 A/B가 먼저 갈라지고, 각 lineage가 speciation S로 H/M이 되었습니다. H_A–M_A는 A lineage의 S에서 처음 만나므로 ortholog입니다. H_A–H_B와 H_A–M_B는 D에서 만나므로 paralog입니다. 가지 길이는 판단에 사용하지 않습니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf

## 14. 정답·해설 · 상황 B와 sequence similarity의 한계 (23–24분)

상황 B에서는 speciation 뒤 H lineage에서만 gene duplication이 일어납니다. 따라서 H1/H2는 서로 paralog이지만 각각 M에 대해 ortholog이며, M을 기준으로 co-orthologs라고 부릅니다. 관계는 비교하는 쌍과 분기 사건에 대해 정의합니다. 활동지1쪽3번의 답은 similarity만으로 사건을 알 수 없다는 것이며 phylogenetic tree와 gene duplication·loss 근거를 추가로 확인합니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_ensembl_tree] Ensembl: Protein trees
https://www.ensembl.org/info/docs/compara/homology_method.html

## 15. Ortholog여도 function이 완전히 같지는 않다 (24–25분)

Ortholog는 function을 inference할 때 유용하지만 모든 생물학적 function이 동일하다는 정의는 아닙니다. function은 catalysis, substrate, expression 조직, interaction partner 등 여러 층위로 나뉘므로 어느 층위의 similarity를 말하는지 명시해야 합니다. 실제 function 자료를 비교한 연구도 ortholog와 paralog의 차이를 통계적 경향으로 다루며 절대 규칙으로 다루지 않습니다. structure prediction용 MSA에는 목적에 따라 여러 homologous family이 포함될 수 있으므로 ortholog만 남겨야 한다는 규칙도 자동으로 적용하지 않습니다.

[evo_function] Altenhoff et al. (2012). Resolving the Ortholog Conjecture. PLOS Computational Biology.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002514
[evo_ensembl_tree] Ensembl: Protein trees
https://www.ensembl.org/info/docs/compara/homology_method.html

## 16. gene family에서 MSA로: 대응 위치를 제안한다 (25–27분)

phylogenetic tree를 통해 누가 누구와 관련되는지 생각했다면, 이제 각 sequence의 어느 위치끼리 비교할지 정해야 합니다. MSA는 insertion과 deletion을 고려해 대응한다고 보는 residue들을 같은 열에 배치합니다. 특히 짧은 반복, 매우 다른 길이, domain 구성이 다른 sequence에서는 alignment의 불확실성이 커질 수 있습니다. 이후 structure prediction에서 사용되는 정보는 이런 대응 관계에 영향을 받으므로 행 수를 세기 전에 alignment 자체를 읽는 습관을 들입니다.

[evo_ebi_msa] EMBL-EBI Training: Multiple sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/multiple-sequence-alignment/
[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki

## 17. MSA 읽기: 행·열·query·gap (27–30분)

가상 alignment에서 한 행을 가로로 읽으면 하나의 protein sequence를, 한 열을 세로로 읽으면 대응한다고 본 위치들의 상태를 읽습니다. Query의 세 번째 열에는 residue가 없으므로 이 열의 alignment 번호와 query의 residue number는 다릅니다. Gap은 이 위치에 alignment된 residue가 없다는 표시이지 미지의 amino acid이라는 기호가 아닙니다. 이 짧은 예시는 MSA 문법을 위한 것이며 실제 protein의 structure나 function을 예측할 수 있는 자료가 아닙니다.

[evo_ebi_msa] EMBL-EBI Training: Multiple sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/multiple-sequence-alignment/

## 18. Gap 하나가 residue number를 바꾼다 (30–32분)

같은 alignment를 다시 사용해 query의 D가 alignment에서는 4열이지만 원래 sequence에서는 3번 residue임을 확인합니다. structure 파일의 residue number나 실험에서 사용한 construct 번호는 여기서도 다시 달라질 수 있으므로 별도 대응이 필요합니다. 또한 seq_A의 Q를 query 대비 insertion으로 표현할 수 있어도 어느 ancestor에서 실제 insertion 또는 deletion이 일어났는지는 이 alignment만으로 결정하지 못합니다. 이후 masking 위치를 정할 때 번호 체계를 혼동하지 않도록 기록 단위를 명시합니다.

[evo_ebi_pairwise] EMBL-EBI Training: Pairwise sequence alignment
https://www.ebi.ac.uk/training/online/courses/guide-to-sequence-analysis-tools/sequence-alignment/pairwise-sequence-alignment/

## 19. FASTA: 이름 줄과 sequence 줄부터 읽기 (32–33분)

헤더와 sequence를 분리해 읽는 것만으로 많은 입력 실수를 줄일 수 있습니다. 첫 번째 줄의 synthetic이라는 말은 자료의 출처 설명이며 protein sequence에 포함되지 않습니다. sequence 길이가 서로 다를 수 있는 일반 FASTA와 gap을 넣어 대응 열을 맞춘 aligned FASTA를 구분합니다. 일반 FASTA에서 대소문자가 가지는 의미는 도구에 따라 다를 수 있으므로 다음 장의 A3M 규칙을 모든 FASTA 파일에 그대로 적용하지 않습니다.

[evo_ncbi_fasta] NCBI: BLAST QuickStart—Query and Database Sequence Formats
https://www.ncbi.nlm.nih.gov/books/NBK1734/?report=reader

## 20. A3M: 대문자와 소문자는 서로 다른 역할 (33–36분)

A3M에서는 insertion 열의 빈칸을 생략할 수 있어 텍스트 줄의 길이가 달라 보입니다. 예시의 소문자 q는 insertion residue이고 대문자 Y는 query의 F와 다른 residue지만 같은 match 열에 대응합니다. 소문자를 제외해 읽으면 각 행의 match와 deletion 위치는 여덟 개이며 query의 위치와 맞출 수 있습니다. insertion 정보의 처리 방식은 예측 파이프라인마다 다르므로 파일 원본을 무조건 대문자로 바꾸거나 모든 소문자를 임의 삭제해서 저장하지 않습니다.

[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki

## 21. 활동지 2 · 전체 A3M을 읽고 답하기 (36–38분)

활동지의 자료와 질문을 모두 화면에 제시합니다. 종이 없이 화면을 읽고 구두 또는 개인 노트로 답한 뒤 바로 다음 정답·해설을 봅니다. 먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. 실제 실습 파일 이름은 practice/README.md를 따른다. 소문자 insertion은 alignment 열로 세지 않는다. 다만 파서가 그 insertion 길이를 별도 특징으로 활용할 수 있으므로 소문자를 무의미한 문자라고 설명하지 않는다. Gap은 해당 alignment 위치의 residue가 없는 대응, X는 residue 종류를 알 수 없거나 가렸다는 표식이다. Subsampling은 evolutionary diversity와 특정 위치의 coverage를 함께 바꿀 수 있다. 컴퓨터가 없는 학생은 활동지의 A3M 발췌를 사용한다.  답: query 포함7행, homolog6행, alignment12열. A2의 ee는4열 직전 insertion이며 원문14글자와 alignment12열은 다릅니다. A3의 gap은5열, B1의 X는11열입니다. 활동지2쪽4번 Neff 질문은 해당 설명 직후 구두로 이어갑니다.

[core_af3_input] AlphaFold 3 official input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 22. 정답·해설 · 활동지 2쪽 · A3M의 행과 열 (38–39분)

실습 A3M은 헤더 일곱 개와 그에 대응하는 sequence 일곱 개로 구성됩니다. Query가 한 행이므로 homolog는 여섯 행이며, 헤더 줄과 sequence 줄을 합친 텍스트 줄 수를 MSA 행 수로 세면 안 됩니다. Query가 열두 residue이며 이 예제의 각 행에서 소문자를 제외하고 대문자와 gap을 세면 열두 alignment 열이 됩니다. Query와 동일한 A1도 원시 행 수에는 포함되지만 독립적인 evolutionary information이 하나 더 생긴다고 해석하지 않습니다. 행 수와 더불어 coverage, diversity, redundancy, 계산 정의를 기록한 Neff를 확인합니다. 이 A3M의 A/B header는 임의 라벨로, 활동지 1쪽의 gene lineage A/B와 연결해 orthology나 paralogy를 판정하지 않습니다.

[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki
[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108

## 23. 정답·해설 · 활동지 2쪽 · ee, gap, X의 차이 (39–40분)

A2 원문은 ACDeeEFGHIKLMN으로 열네 글자이지만, 소문자 ee는 D 뒤이자 query alignment 4열 E 직전의 insertion입니다. 소문자를 제외한 표시를 보조선으로 사용하면 열두 match/deletion 열이 유지됨을 확인할 수 있습니다. 이것은 읽기용 비교이며 원본에서 insertion 정보를 무조건 삭제하라는 지시가 아닙니다. A3의 다섯 번째 열은 gap이고 B1의 열한 번째 열은 X입니다. X는 한 alignment 위치를 차지하며 residue 종류를 모르거나 실습에서 의도적으로 가린 경우를 나타내므로 gap과 의미가 다릅니다.

[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki
[core_af3_input] AlphaFold 3 official input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 24. Coverage와 identity: 분모를 함께 적는다 (40–42분)

이 강의의 계산 예에서는 coverage를 query 전체 residue 중 상대 residue와 짝지어진 위치의 비율로 정의합니다. Identity는 두 sequence 모두 residue가 있는 비교 위치 중 같은 residue의 비율로 계산합니다. 실제 프로그램은 gap 포함 여부나 길이 기준이 달라질 수 있으므로 출력 문서를 확인하고 숫자만 비교하지 않습니다. 100% identity라도 query의 아주 짧은 부분만 덮는 hit는 전체 protein이 동일한 특징을 가진다는 근거가 되지 않습니다.

[evo_ncbi_glossary] NCBI BLAST Glossary
https://www.ncbi.nlm.nih.gov/books/NBK62051/?report=reader
[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki

## 25. 바로 실습 · Coverage와 identity 계산 (42–44분)

먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. 정답은 A가 비교 위치 4개 모두 같으므로 coverage 4/8=50%, identity 4/4=100%입니다. B는 비교 위치 8개 중 6개가 같으므로 coverage 8/8=100%, identity 6/8=75%입니다. 어느 하나가 무조건 더 좋은 MSA 입력이라고 정하기보다는 길이, homology 근거, alignment reliability와 분석 목적을 함께 확인한다는 답으로 마무리합니다.

[evo_ncbi_glossary] NCBI BLAST Glossary
https://www.ncbi.nlm.nih.gov/books/NBK62051/?report=reader

## 26. 정답·해설 · Coverage와 identity · 분모부터 쓰기 (44–45분)

Query는 ACDEFGHI로 여덟 residue입니다. A는 ACDE----이므로 query의 앞 네 위치만 덮고 비교한 네 위치는 모두 같습니다. 따라서 coverage는 4/8=50%, identity는 4/4=100%입니다. B는 ACNEYGHI로 query 전체를 덮으며 D/N과 F/Y 두 곳만 달라 coverage는 8/8=100%, identity는 6/8=75%입니다. 이는 앞 슬라이드에서 명시한 교육용 분모를 사용한 결과이며 실제 도구의 정의는 따로 확인합니다. A의 100% identity만 보고 전체 query가 동일하다고 말하거나 어느 하나가 무조건 더 좋은 입력이라고 결론 내리지 않습니다.

[evo_ncbi_glossary] NCBI BLAST Glossary
https://www.ncbi.nlm.nih.gov/books/NBK62051/?report=reader
[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki

## 27. Conservation: 한 열에서 무엇이 유지되는가? (45–47분)

각 열을 세로로 읽고 어떤 residue가 얼마나 자주 나타나는지 확인합니다. 예시에서 첫 번째 열은 모두 A이지만 두 번째 열은 C와 S로 달라집니다. conservation은 structural stability이나 functional constraint와 관련될 수 있지만 sampling된 sequence가 서로 너무 비슷해 conserved으로 보이는 경우도 있습니다. 네 개의 짧은 가상 sequence만으로 생물학적 중요도를 추정하지 않고 개념을 익히는 데만 사용합니다.

[evo_ebi_sequence] EMBL-EBI Training: Primary structure—Why sequence matters
https://www.ebi.ac.uk/training/online/courses/foundations-protein-structure/fundamentals-of-protein-composition/the-peptide-bond-and-primary-structure/ss/
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957

## 28. conservation·covariation·coevolution은 서로 다른 질문 (47–49분)

학생에게 MSA를 세로와 가로로 번갈아 보게 합니다. Ortholog와 paralog는 서로 다른 행인 gene들의 기원에 붙이는 이름이고, residue coevolution은 alignment에서 대응하는 위치들의 evolutionary 의존성을 묻습니다. 두 residue가 ortholog라는 표현은 이 문맥에 맞지 않습니다. 문헌에서는 covariation과 coevolution을 넓게 섞어 쓰기도 하지만, 오늘은 관찰된 statistical dependence과 그 원인에 관한 evolutionary 해석을 구별합니다. covariation을 보았다고 structural interaction 때문에 coevolution했다고 바로 결론 내리지 않습니다. 두 열이 완전히 보존되어 있으면 중요한 contact가 실제 존재하더라도 이 자료의 변화 패턴으로 의존성을 판별하기 어렵다는 점도 짚습니다. 여기서 함께 evolution한다는 것은 여러 세대에 걸친 sequence 제약의 의존성을 뜻합니다. protein의 두 residue가 시간에 따라 같은 방향으로 움직이는 dynamics적 상관과는 다른 개념입니다.

[coevo_miyazawa] Miyazawa (2013). Prediction of Contact Residue Pairs Based on Co-Substitution between Sites in Protein Structures. PLOS ONE.
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0054252
[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf

## 29. contact를 유지하는 선택이 coevolution을 만들 수 있다 (49–51분)

그림의 원은 atom 한 개가 아니라 residue side chain의 charge 성질을 단순화한 표식입니다. i 위치는 청록, j 위치는 주황으로 일관되게 표시하며 색 자체가 charge를 뜻하지 않습니다. D는 보통 negative charge, K는 positive charge를 띠지만 실제 charge·안정성은 pH·환경·거리·배향에 의존합니다. 여기서는 가까운 두 위치의 반대 charge 조합이 유리하다는 가정을 명시합니다. D−/K+와 K+/D− 두 조합을 나란히 보여주고, K+/K+는 이 가정에서 덜 유리하다고 표시합니다. 두 유리한 조합 사이에 화살표를 그리지 않았으므로 D/K에서 K/K를 거쳐 K/D로 evolution했다거나 두 substitution이 동시에 일어났다는 주장이 아닙니다. 한 위치의 substitution 효과가 다른 위치의 상태에 의존하는 것은 epistasis이며, 한 변화의 영향을 다른 변화가 완화할 수 있다는 것이 compensatory substitution의 직관입니다. 이런 structure 유지 제약이 여러 homologous sequence의 조합 패턴으로 남을 수 있기 때문에 coevolution 분석으로 sequence에서 멀리 떨어진 위치의 공간 contact를 추정할 수 있습니다. 다만 다음 빈도 실습의 통계만으로 이 물리적 원인을 확정하지 않습니다. 학생에게 ‘한 열만 보는 conservation과 두 열을 함께 읽는 structure 단서는 무엇이 다른가’를 구두로 물은 뒤 다음 계산 슬라이드로 진행합니다.

[coevo_miyazawa] Miyazawa (2013). Prediction of Contact Residue Pairs Based on Co-Substitution between Sites in Protein Structures. PLOS ONE.
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0054252
[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[intro_af2_overview] EMBL-EBI / Google DeepMind: AlphaFold2 high-level overview
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/a-high-level-overview/

## 30. 두 열의 빈도와 조합 빈도를 따로 센다 (51–54분)

표의 각 숫자는 그 residue 조합을 가진 sequence 행의 수입니다. 예를 들어 오른쪽 위의 4는 i에 D와 j에 K가 같은 sequence 안에서 함께 나타난 행이 네 개라는 뜻입니다. marginal frequency는 한 열만 보고 셉니다. i가 D인 행은 4/8, j가 K인 행도 4/8입니다. 두 열이 독립적이라면 이 비율들을 곱한 1/4, 즉 여덟 행 중 두 행 정도의 조합 빈도를 기대하지만 여기서는 네 행입니다. 이는 교육용 자료에서 관찰한 distribution과 독립 distribution을 비교한 것이며, 여덟 개 생물학적 독립 sample으로 significance test을 한 것이 아닙니다. 원하면 MI = sum P(a,b) log2[P(a,b)/(P(a)P(b))]라고 소개합니다. 이 가상 표의 경험적 MI는 1 bit이며 0 빈도 항의 기여는 0으로 처리합니다. 계산값 자체는 phylogenetic effects를 제거하지 않으며 contact 점수나 AlphaFold confidence도 아닙니다.

[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957

## 31. 활동지 3 · 두 열의 joint frequency 계산 (54–56분)

먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. 학생 실습지의 coevolution 페이지 첫 계산과 연결합니다.  두 자료 모두 P(D_i)=1/2, P(K_j)=1/2이므로 독립일 때 D–K의 빈도는 1/4입니다. 자료 P의 실제 D–K 빈도는 4/8=1/2, 자료 Q는 2/8=1/4입니다. Q에서는 네 조합이 모두 각각 1/4이므로 이 경험적 distribution은 독립입니다. 단일 열의 residue distribution과 conservation은 동일하므로 그것만으로 둘을 구분할 수 없습니다. 선택 심화 답은 경험적 MI가 P에서 1 bit, Q에서 0 bit라는 것입니다. Q에 covariation이 없다는 관찰도 실제 protein에서 contact가 없음을 입증하지 않습니다. P에 covariation이 있다는 관찰도 direct contact를 입증하지 않습니다. 작은 가상 표로 statistical significance이나 실제 coevolution을 판정하지 않는다고 마무리합니다.

[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957

## 32. 정답·해설 · 같은 conservation, 다른 joint distribution (56–57분)

학생의 계산을 marginal frequency, joint frequency, 독립 model의 expected value 순서로 확인합니다. 자료 P와 Q 모두 각 열의 D/K 빈도는 각각 1/2이므로 한 열씩 보거나 conservation만 계산하면 차이가 없습니다. 그러나 P의 D–K는 4/8이고 Q의 D–K는 2/8입니다. 독립일 때의 expected value 1/4과 비교하면 P에는 statistical dependence이 있습니다. Q는 D–K 하나만 맞는 것이 아니라 DD·DK·KD·KK 네 조합이 모두 1/4이므로 제시한 경험적 distribution이 독립입니다. 이 표는 손으로 만든 8행 자료이며 significance test이나 물리적 원인의 검증이 아닙니다. P의 패턴을 만든 원인이 contact인지, phylogenetic effects인지, indirect association인지 이 계산만으로 구분할 수 없습니다. 반대로 Q에 covariation이 없다는 관찰도 실제 protein에 contact가 없음을 입증하지 않습니다. 이 마지막 구분을 확인한 뒤 evolutionary relationship과 sampling의 문제로 연결합니다.

[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957

## 33. 휴식 (57–67분)

첫 번째 휴식. 방금 계산한 두 열의 상관이 무엇 때문에 생겼는지 생각해 두게 합니다. 다음 구간에서 ortholog의 common ancestor와 paralog 혼합을 같은 데이터에 연결합니다.



## 34. Ortholog를 모아도 common ancestor는 남아 있다 (67–70분)

Ortholog는 speciation로 갈라진 gene 관계이지 서로 독립적으로 실험한 시료라는 뜻이 아닙니다. 어느 ancestor 가지에서 D–K 조합이 생긴 뒤 많은 후손에게 전달되었다면, 말단 sequence의 반복 개수를 substitution 사건 수로 셀 수 없습니다. 여러 떨어진 가지에서 관련 변화가 반복되는지 묻는 것이 더 적절하지만, 이를 판단하려면 phylogenetic tree와 substitution model 등 추가 가정이 필요합니다. Ortholog를 선택하면 고대 gene duplication으로 분리된 다른 lineage를 섞는 일을 줄일 수 있으나 phylogenetic non-independence 자체를 없애지는 못합니다. sequence reweighting도 이 문제를 완벽히 제거하지 않습니다. 따라서 ortholog 선택, alignment 품질, phylogenetic structure, sequence diversity는 서로 다른 확인 항목입니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957
[evo_weighting] Hockenberry & Wilke (2019). Phylogenetic Weighting Does Little to Improve the Accuracy of Evolutionary Coupling Analyses.
https://www.mdpi.com/1099-4300/21/10/1000
[coevo_miyazawa] Miyazawa (2013). Prediction of Contact Residue Pairs Based on Co-Substitution between Sites in Protein Structures. PLOS ONE.
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0054252

## 35. Paralog 혼합은 lineage 차이를 함께 섞는다 (70–72분)

lineage A에서는 i가 D이고 j가 K, lineage B에서는 반대라고 가정하면 A와 B의 비중이 두 열의 조합 빈도를 함께 결정합니다. 이런 패턴에는 lineage 분기 역사가 들어 있으므로 전체 MSA의 상관만으로 반복적인 residue 보상을 inference할 수 없습니다. 곧바로 다음 장의 숫자를 직접 나눠 보게 합니다. structure prediction과 DCA는 일반적으로 homologous protein family의 정보를 활용하며 입력을 반드시 ortholog-only로 제한하는 정의가 아닙니다. Paralog도 공통 structure 제약을 알려 줄 수 있으므로 모두 제거하면 충분한 diversity까지 잃을 수 있습니다. 반대로 alignment되지 않는 domain이나 매우 다른 function lineage를 무조건 합치는 것도 바람직하지 않습니다. 가족별 비교는 원인을 점검하는 분석이며, 진짜 coevolution이 전혀 없다는 증명이 아닙니다.

[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957
[coevo_pairing] Gandarilla-Pérez et al. (2023). Combining phylogeny and coevolution improves the inference of interaction partners among paralogous proteins. PLOS Computational Biology.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011010

## 36. 활동지 3 · lineage를 나누고 evolutionary history 해석 (72–74분)

먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. 화면 표를 읽기 전에 다음 가정이 화면과 실습지에 제시되어 있음을 확인합니다: H/M/R/F는 네 가상 종이며, gene duplication으로 A/B가 나뉜 뒤 네 species이 분화했고 추가 gene duplication·loss은 없습니다. 실제 종의 약자가 아닙니다. 이 가정은 반드시 학생에게 읽어 줍니다.  정답: A_H–A_M은 ortholog, A_H–B_H와 A_H–B_M은 paralog입니다. 각 A 또는 B lineage 안에서는 이 두 위치에 variation가 없으므로 이 표만으로 lineage 내부의 coevolution을 검출할 근거가 없습니다. 전체에서는 앞 장의 자료 P와 같이 D–K와 K–D만 각각 네 번 나타납니다. 이 의존성은 lineage 구분과 겹치므로 반복적인 compensatory substitution이나 direct contact로 바로 해석하면 안 됩니다. 여덟 행은 여덟 번의 독립 substitution이 아니며 ancestor 상태와 실제 변화 횟수도 이 표로 결정하지 못합니다. 추가 근거로 더 넓은 lineage sampling, 신뢰할 만한 alignment·phylogenetic tree, lineage 내부 variation, 실제 structure 등을 제안하게 합니다. 여기 A/B는 주어진 가상 gene history에 따른 gene duplication lineage입니다. 별도 파일 practice/fictional_learning.a3m의 group A/B는 편의를 위한 교육용 라벨이며 ortholog/paralog 관계를 inference한 집단이 아닙니다. 두 자료를 같은 MSA로 연결하지 않습니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957

## 37. 정답·해설 · lineage 차이와 coevolution을 구분 (74–75분)

문제에서 A/B gene duplication이 H·M·R·F의 speciation보다 먼저 발생했고 추가 gene duplication·loss은 없다고 주었습니다. 그러므로 A_H와 A_M의 MRCA은 speciation 노드이며 ortholog입니다. A_H와 B_H, A_H와 B_M은 모두 먼저 일어난 gene duplication 노드에서 만나므로 paralog입니다. 현재 같은 species인지 다른 species인지만으로 분류하지 않습니다. A lineage에서는 i와 j가 D/K로 고정되고 B에서는 K/D로 고정되어, 각 lineage 내부에는 두 위치의 variation가 없습니다. 따라서 이 표가 lineage 내부의 coevolution을 검출할 정보를 주지는 않지만, coevolution이 생물학적으로 전혀 없다고 증명한 것도 아닙니다. 합친 표에서는 D–K와 K–D가 네 번씩 나타나지만 그 의존성은 lineage 이름과 완전히 겹칩니다. ancestor에게서 다른 조합을 물려받은 경우에도 이 표를 얻을 수 있으므로 여덟 후손을 여덟 번의 독립 compensatory substitution으로 세거나 substitution의 순서를 결정하지 않습니다. 실제 contact 여부는 alignment와 lineage 이력을 점검하고 structure·실험 근거로 확인합니다. Ortholog들끼리도 common ancestor에 따른 비독립성이 남으며, structure 분석에서 paralog를 항상 제거해야 한다는 뜻은 아닙니다. 이 A/B는 gene history가 주어진 가상 lineage입니다. 별도 A3M 실습 파일의 A/B 라벨과는 다른 자료입니다.

[evo_sonnhammer] Sonnhammer & Koonin (2002). Orthology, paralogy and proposed classification for paralog subtypes.
https://sonnhammer.org/download/papers/2002_TIG_18:619-620.pdf
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957
[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108

## 38. complex에서는 어떤 sequence끼리 짝지었는가? (75–77분)

앞의 A/B subfamily 예제와 혼동하지 않도록 이번에는 서로 interaction할 수 있는 두 protein family을 P와 Q라고 부릅니다. protein 내부의 coevolution은 한 가족의 MSA에서 열쌍을 비교합니다. protein 사이의 분석에서는 P와 Q의 MSA 행을 interaction partner에 맞춰 대응시키는 문제가 추가됩니다. 한 종에 P1/P2와 Q1/Q2가 모두 있으면 species 이름만으로 올바른 상대가 정해지지 않습니다. 다른 species의 ortholog 관계, genomic context, 알려진 interaction 및 sequence 신호가 pairing을 돕지만 보장은 아닙니다. 잘못 연결한 행은 protein 사이 신호를 약화시키거나 왜곡할 수 있습니다. AlphaFold 3의 입력 문서에서 말하는 MSA pairing 역시 행 대응을 구성하는 절차이며 실험적인 binding 확인을 뜻하지 않습니다. 단일 protein의 homologous MSA 선택과 complex의 파트너 pairing을 구분하게 합니다.

[coevo_pairing] Gandarilla-Pérez et al. (2023). Combining phylogeny and coevolution improves the inference of interaction partners among paralogous proteins. PLOS Computational Biology.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011010
[af3_input] Google DeepMind AlphaFold 3 input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 39. 함께 변한다고 모두 직접 연결된 것은 아니다 (77–79분)

칠판에 i—k—j를 그리고 i와 j 사이의 직접 선은 그리지 않습니다. 가운데 k를 통한 연결만으로 두 끝 위치의 관찰 distribution이 연관될 수 있다는 직관을 설명합니다. Direct Coupling Analysis는 모든 위치를 함께 고려하는 통계 model에서 쌍별 coupling을 추정해 단순한 두 열 상관의 간접 효과를 분리하려는 접근입니다. 여기서 direct는 해당 통계 model 안에서의 뜻이지 물리적 인과 관계가 검증되었다는 뜻이 아닙니다. sampling, phylogenetic effects, alignment 오류와 model 한계가 남을 수 있습니다. AlphaFold 2는 Evoformer에서 MSA 표현과 residue쌍 표현을 상호 갱신하며 structure training을 활용합니다. 따라서 MI를 계산해 높은 값끼리 붙이거나 고전적 DCA만 실행하는 절차로 설명하면 부정확합니다. AlphaFold 3 역시 이 장의 가상 MI 계산을 그대로 structure로 변환하는 도구가 아니며 세부 structure는 AF2와 다릅니다. 이 장에서는 입력 정보와 training된 inference를 구분하는 데 초점을 둡니다.

[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957
[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2
[core_af3] Abramson et al. (2024), Accurate structure prediction of biomolecular interactions with AlphaFold 3
https://www.nature.com/articles/s41586-024-07487-w

## 40. Raw depth와 Neff: 행 수와 diversity는 다르다 (79–82분)

weight 합으로 정의하는 한 방식에서는 각 sequence와 충분히 비슷한 neighbor 수를 자기 자신까지 포함해 센 뒤 그 역수를 weight로 사용합니다. 모두 같은 sequence 100개라면 각 weight는 1/100이므로 합은 1입니다. 이것은 교육용 reweighting 예시이며 HH-suite의 entropy 기반 Neff 등 다른 정의와 수치를 그대로 비교할 수 없습니다. Neff는 실제 독립 sample 수의 정답도 아니고 structure prediction accuracy를 보장하는 점수도 아닙니다. 마지막30초에 활동지2쪽4번을 구두로 확인합니다. 같은 행 복제는 raw depth를 높여도 새로운 독립적 evolution 사건을 만들지 않습니다.

[evo_morcos] Morcos et al. (2011). Direct-coupling analysis of residue coevolution captures native contacts across many protein families. PNAS.
https://doi.org/10.1073/pnas.1111471108
[evo_hhsuite] HH-suite official wiki: Multiple sequence alignment formats and model format
https://github.com/soedinglab/hh-suite/wiki
[evo_weighting] Hockenberry & Wilke (2019). Phylogenetic Weighting Does Little to Improve the Accuracy of Evolutionary Coupling Analyses.
https://www.mdpi.com/1099-4300/21/10/1000

## 41. AlphaFold2와 AlphaFold3 (82–83분)

AF2와 AF3를 단순한 accuracy 순위로 소개하지 않는다. AF2의 monomer model은 protein 중심이며 complex용 AlphaFold-Multimer가 별도로 있다. AF3는 protein 외 molecule들을 함께 다루고 diffusion 기반 coordinates 생성을 사용한다. protein MSA는 AF3에도 사용된다. AF2에서 관찰한 MSA 조작 효과가 AF3에서도 동일한 크기와 방식으로 나타난다고 가정하면 안 된다. model을 바꾸면 MSA 처리 방식과 점수의 의미도 함께 확인한다.

[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2
[core_af3] Abramson et al. (2024), Accurate structure prediction of biomolecular interactions with AlphaFold 3
https://www.nature.com/articles/s41586-024-07487-w

## 42. 웹 서버와 로컬 실행 (83–84분)

AlphaFold Server와 공개 AF3 로컬 코드는 지원하는 입력 항목과 실행 환경이 같지 않다. 웹 화면에서 로컬 JSON의 모든 항목을 조절할 수 있다고 설명하지 않는다. 초보자는 ColabFold 노트북에서 sequence 입력과 결과 파일을 먼저 경험한다. 교사는 강의 전에 접속 가능 여부와 GPU 할당을 확인하고 동일한 실습 파일을 준비한다. 수업은 오프라인 alignment 실습과 결과 판독만으로도 끝낼 수 있으며, 실제 예측 시연은 사전 준비한 환경에서 선택적으로 진행한다. 실행법은 examples/README.md에 제공한다.

[core_cf] ColabFold official repository
https://github.com/sokrypton/ColabFold
[core_af3_input] AlphaFold 3 official input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 43. Custom MSA의 기본 조건 (84–85분)

같은 protein의 대안 structure를 비교하는 실습이므로 query를 고정한다. 소문자를 대문자로 바꾸면 insertion이 alignment 열로 오해되어 열 대응이 깨질 수 있다. 줄마다 문자열 길이가 달라도 lowercase insertion을 제외한 alignment 길이는 같아야 한다. Gap과 unknown X의 의미는 다르다. 헤더는 sequence 식별과 일부 파이프라인의 species 정보 해석에 쓰일 수 있으므로 무작위로 바꾸는 것을 structure 제어 방법이라고 가르치지 않는다. complex pairing은 별도의 대응 문제다.

[core_cf] ColabFold official repository
https://github.com/sokrypton/ColabFold
[core_af3_input] AlphaFold 3 official input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 44. ColabFold 1 · 접속과 실습 준비 (85–87분)

공식 전체 URL은 슬라이드 하단과 examples/colabfold_walkthrough.md에 있습니다. ColabFold의 AlphaFold2 노트북이며 AlphaFold Server의 AF3 화면과 다릅니다. 브라우저 주소창에 표시된 URL을 붙여 넣고 실행 가능한 Google 계정으로 로그인합니다. 개인 사본 저장은 노트북 설정을 보존하는 선택 사항이며 Colab에서 임시 실행할 수도 있습니다. 먼저 교사가 공개 calmodulin sequence와 수업용 폴더를 학생에게 제공합니다. 12열짜리 fictional_learning.a3m은 실제 예측기에 넣지 않습니다. 수업 중에는 실행 준비와 결과 읽기를 함께 연습하고 실제 GPU 대기 시간은 보장하지 않습니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb
[core_calm] UniProt P0DP23, human calmodulin-1
https://www.uniprot.org/uniprotkb/P0DP23/entry

## 45. ColabFold 2 · GPU와 노트북 실행 방식 (87–89분)

Google Colab 공식 FAQ는 Runtime→Change runtime type에서 hardware accelerator를 고르도록 안내합니다. GPU 종류와 메뉴 표시는 계정·시점에 따라 달라질 수 있으므로 특정 T4가 항상 제공된다고 약속하지 않습니다. 선택 후 연결 상태를 확인합니다. 처음 쓰는 학생에게 셀은 코드와 결과가 붙어 있는 실행 단위라고 설명합니다. 입력 값을 먼저 정한 다음 Run all을 실행합니다. 학생 개인의 승인·로그인이 필요한 화면은 본인이 내용을 확인하고 처리합니다. GPU 사용량과 실행 수명은 제한되며 실제 대기 시간을 수업 시간에 보장하지 않습니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb
[core_colab_faq] Google Colab official FAQ
https://research.google.com/colaboratory/faq.html

## 46. ColabFold 3 · sequence와 기본 조건 입력 (89–91분)

공식 FASTA 직접 주소: https://rest.uniprot.org/uniprotkb/P0DP23.fasta . 브라우저 주소창에 붙여 넣습니다. 파일이 자동 다운로드되지 않고 텍스트가 보이면 페이지 저장(Ctrl+S / macOS Cmd+S)으로 calmodulin_P0DP23.fasta라는 이름으로 저장합니다. HTML이 아니라 >sp|P0DP23|CALM1_HUMAN으로 시작하는 일반 텍스트인지 확인하고, .txt가 자동으로 붙었다면 최종 확장자가 .fasta인지 확인합니다. 저장 없이 화면에서 제목을 제외한 sequence 줄만 복사해도 됩니다. examples/calmodulin_P0DP23.fasta를 텍스트로 열고 >sp로 시작하는 설명 줄은 제외합니다. 나머지 sequence 줄은 이어 붙이거나 줄바꿈 포함 복사해도 공백이 제거됩니다. 단일 사슬 실습이므로 콜론을 추가하지 않습니다. query_sequence에 기본 예제 sequence가 남아 있지 않은지 학생이 확인합니다. jobname은 영문·숫자·밑줄로 간단히 지정합니다. 이 calmodulin 예측에는 Ca2+를 입력하지 않으므로 결과를 실험적 apo 또는 holo 상태로 단정하지 않습니다. num_relax는 후처리 model 수이며 예측할 sequence 수가 아닙니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb
[core_calm] UniProt P0DP23, human calmodulin-1
https://www.uniprot.org/uniprotkb/P0DP23/entry
[core_calm_fasta] UniProt P0DP23 canonical FASTA: human calmodulin-1
https://rest.uniprot.org/uniprotkb/P0DP23.fasta

## 47. ColabFold 4 · Run all과 계산 진행 확인 (91–93분)

입력 폼을 먼저 모두 설정한 뒤 Runtime→Run all을 누릅니다. 공식 노트북은 설치, MSA 옵션, 고급 설정, 예측 셀을 순서대로 실행합니다. 초기 model 다운로드와 MSA 서버 대기 등이 포함되므로 완료 시간은 고정하지 않습니다. num_seeds=1이 structure 하나를 뜻하지 않습니다. 현재 노트북의 Run Prediction은 num_models=5로 실행합니다. 첫 기준 예측과 후속 조건에서 model 수와 seed 수를 맞춥니다. 중간에 실패하면 에러가 발생한 셀과 마지막 문구를 기록하고, 입력 변경 뒤에는 마지막 셀만 다시 누르지 않고 위쪽 입력부터 다시 실행합니다. 코드를 수정하지 않는 초급 경로를 가르칩니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

## 48. ColabFold 5 · 결과와 MSA 다운로드 (93–94분)

먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. 공식 노트북의 Package and download results 셀은 생성한 결과 ZIP을 다운로드합니다. 브라우저가 다운로드를 막았거나 자동 다운로드가 보이지 않으면 셀 결과와 왼쪽 Files 패널의 jobname.result.zip을 확인해 직접 다운로드합니다. 작업 폴더 이름에는 query 해시와 재실행 번호가 붙을 수 있습니다. 압축을 풀어 .a3m을 찾아 실제 calmodulin MSA로 보존하고, 다음 custom 조건에 이 파일을 재사용합니다. 3D 화면의 lDDT 색은 model pLDDT confidence 표시이며 experimental B-factor와 같은 뜻이 아닙니다. 순위1이 물리적으로 가장 많이 존재하는 상태라는 뜻도 아닙니다. 실제 ZIP 파일 이름은 jobname 출력값을 기준으로 확인합니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

## 49. 실습 확인·해설 · ColabFold 기본 실행 (94–95분)

이 페이지는 실행 성공 여부를 점검하는 기준입니다. 실제 GPU structure prediction 결과를 대신하는 모범 coordinates나 고정 점수는 제공하지 않습니다. 앞 실습의 설정과 실제 화면·파일을 대조하고 완료되지 않은 실행은 완료로 표시하지 않습니다. 실제 결과가 서로 다르더라도 입력·조건·출력 이력이 분명하면 비교할 수 있습니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

## 50. lDDT · reference structure의 주변 거리가 얼마나 보존되었나? (95–97분)

lDDT는 structure prediction 전부터 쓰던 accuracy 평가 지표이며 Mariani 등의 2013년 논문이 정의와 검증을 제시했습니다. 이름의 맨 앞 l은 local입니다. 중심 residue 주변의 3차원 neighbor를 평가하며 sequence에서 앞뒤 몇 residue만 고르는 뜻이 아닙니다. reference structure의 거리가 15 Å 미만인 쌍을 고른 뒤 같은 쌍의 predicted distance를 비교합니다. 15 Å는 inclusion radius이고 0.5·1·2·4 Å는 거리 오차의 네 tolerance입니다. 모든 coordinates를 같이 회전·이동해도 내부 거리는 유지되므로 전체 structure의 중첩이 필요 없습니다. 그러나 같은 residue·atom을 대응시켜야 합니다. 원 논문의 all-atom 평가와 아래 AF2의 Cα-only 계산을 구별합니다. AF2 구현은 자기 자신과 reference coordinates가 없는 위치를 제외하고 원 lDDT의 stereochemistry 보정은 생략합니다. 이 설명은 AF2/ColabFold 기준이며 AF3의 atom별 정의를 그대로 대체하지 않습니다.

[confidence_lddt_paper] Mariani et al. (2013), lDDT: a local superposition-free structure comparison score
https://pmc.ncbi.nlm.nih.gov/articles/PMC3799472/
[confidence_lddt_code] Google DeepMind AlphaFold2: lddt.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/lddt.py

## 51. 바로 실습 · 네 거리쌍의 lDDT 계산하기 (97–98분)

화면 왼쪽의 가상 거리 표를 보고 오른쪽 문항을 풉니다. reference structure에서15 Å 미만인 네 neighbor를 이미 골랐으며 coordinates가 모두 있다고 가정합니다. 각각의 absolute error와 네 threshold을 통과하는 횟수를 계산한 뒤, 통과 수 합을4쌍×4기준으로 나눕니다. inclusion radius과 오차 tolerance를 구별하게 합니다. d의 predicted distance가17 Å라도 reference distance14 Å로 선택했으므로 제외하지 않습니다. 1분 동안 구두 또는 개인 메모로 풀이하고 다음 정답 슬라이드에서0.625와62.5를 확인합니다. 별도 활동지 없이 현재 화면만으로 풀 수 있습니다. 실제 protein inference값이 아닌 교육용 거리입니다.

[confidence_lddt_paper] Mariani et al. (2013), lDDT: a local superposition-free structure comparison score
https://pmc.ncbi.nlm.nih.gov/articles/PMC3799472/
[confidence_lddt_code] Google DeepMind AlphaFold2: lddt.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/lddt.py

## 52. 정답·해설 · 네 neighbor의 거리 오차를 네 번 채점 (98–99분)

실제 protein coordinates에서 얻은 값이 아니라 중심 residue i와 네 neighbor 사이 거리를 가정한 계산 예입니다. reference distance 4·7·10·14 Å는 모두 15 Å 미만입니다. 예측에서 d가 17 Å로 멀어져도 기준에서 선택한 neighbor이므로 계산에서 빼지 않습니다. 오차 0.2는 네 기준, 0.8은 세 기준, 1.5는 두 기준, 3.0은 한 기준을 통과합니다. 총 16개 검사 중 10개를 통과하므로 0.625입니다. 각 tolerance별 보존 비율 1/4·2/4·3/4·4/4를 평균해도 같습니다. 62.5는 lDDT의 100점 표시이며 pLDDT가 아닙니다. 이 값은 중심 residue 하나의 점수입니다. 전체 structure의 lDDT를 모든 per-residue 점수의 단순평균이라고 일반화하지 않습니다. 각 residue에 속한 neighbor 수가 다를 수 있기 때문입니다. threshold에 정확히 걸리는 예를 피했으며 AF2 코드는 엄격한 미만(<) 비교를 사용합니다.

[confidence_lddt_paper] Mariani et al. (2013), lDDT: a local superposition-free structure comparison score
https://pmc.ncbi.nlm.nih.gov/articles/PMC3799472/
[confidence_lddt_code] Google DeepMind AlphaFold2: lddt.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/lddt.py

## 53. 바로 실습 · predicted distance가 더 멀어지면? (99–99.5분)

먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. d의 absolute distance error는 5 Å여서 네 검사 모두 실패합니다. 따라서 (4+3+2+0)/16=9/16=0.5625, 100점 척도 56.25입니다. neighbor 선택은 reference structure에서 하므로 reference distance 14 Å인 d는 계속 포함합니다. 계산에서 빼면 틀린 거리를 벌점 없이 제거하는 오류가 됩니다. 필요한 기본 거리와 a·b·c의 통과 수를 현재 화면에 함께 제공합니다. 별도 활동지나 이전 화면으로 돌아가지 않고 d의 변경 효과를 계산합니다. pLDDT 확률 계산과 reference structure 필요 여부는 뒤의 별도 질문·정답 슬라이드에서 다룹니다.

[confidence_lddt_code] Google DeepMind AlphaFold2: lddt.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/lddt.py

## 54. 정답·해설 · 오차가 커져도 neighbor는 그대로 (99.5–100.0분)

앞 실습의 두 질문을 순서대로 풉니다. 첫째, d의 predicted distance가17에서19 Å로 바뀌면 reference distance14 Å와의 차이는5 Å입니다. 5는0.5·1·2·4보다 모두 크므로 통과 수가1에서0으로 감소합니다. 나머지는4·3·2로 유지되어 총9회 통과합니다. 네 거리쌍에 네 기준을 각각 적용하므로 분모는16이며9/16=0.5625입니다. 100점 척도로56.25, 앞의62.5보다6.25점 낮습니다. 둘째, neighbor는 reference structure의 거리로 미리 정했으므로 d를 빼지 않습니다. 잘못 빼면 남은 세 쌍에서9/12=0.75가 되어 예측이 나빠졌는데 점수가 오르는 오류가 생깁니다. 15 Å는 neighbor 선택 기준이고0.5·1·2·4 Å는 오차 채점 기준이라는 차이를 다시 강조합니다. 이 값은 reference structure에 해당하는 가상 거리와 비교한 중심 residue의 lDDT입니다. model이 미리 예상한 pLDDT가 아니며, 실제 protein을 예측한 결과도 아닙니다.

[confidence_lddt_paper] Mariani et al. (2013), lDDT: a local superposition-free structure comparison score
https://pmc.ncbi.nlm.nih.gov/articles/PMC3799472/
[confidence_lddt_code] Google DeepMind AlphaFold2: lddt.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/lddt.py

## 55. pLDDT가 나온 과정 · 채점한 lDDT를 training target으로 (100.0–102.0분)

lDDT는 reference structure가 있을 때만 채점할 수 있습니다. 새 sequence는 그 reference structure를 모르는 경우가 많으므로, AlphaFold2는 per-residue lDDT-Cα 자체를 예상하는 보조 출력인 pLDDT를 training합니다. p는 predicted를 뜻합니다. structure 모듈의 per-residue internal representation을 작은 신경망에 넣어 50개 bin의 logits를 출력합니다. training 중 model이 만든 Cα coordinates와 training용 reference coordinates를 비교하여 정답 점수를 계산하고, 점수에 해당하는 bin을 cross-entropy로 지도합니다. 0.625라면 폭 0.02인 [0.62,0.64) bin입니다. reference coordinates를 confidence head 입력으로 주는 것이 아니라 손실의 정답을 만드는 데 사용합니다. 정답 점수는 현재 예측 coordinates에 따라 달라지며 pLDDT head만을 위한 수작업 confidence 라벨을 사람이 달지 않습니다. 코드에서는 정답 점수에 stop_gradient를 적용합니다. 여러 seed의 structure가 서로 얼마나 닮았는지를 계산하여 점수를 만드는 방식도 아닙니다. 여기서는 AF2의 training 과정를 설명하며 학생이 ColabFold에서 다시 training한다는 뜻이 아닙니다.

[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2
[confidence_af2_head] Google DeepMind AlphaFold2: PredictedLDDTHead
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/modules.py#L998-L1089
[confidence_af2_config] Google DeepMind AlphaFold2: predicted_lddt configuration
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/config.py
[confidence_lddt_code] Google DeepMind AlphaFold2: lddt.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/lddt.py

## 56. 바로 실습 · lDDT 계산과 pLDDT inference 구별하기 (102.0–103.0분)

training 과정 설명 직후 세 질문을 풉니다. 첫 질문은 직접 채점과 training된 model의 inference를 구분하는 확인입니다. 둘째 질문은 점수와 사건의 확률 또는 equilibrium population을 구분합니다. 셋째는 왼쪽 세 bin의 가중합과 가장 확률이 큰 bin 하나를 택하는 계산이 다름을 확인합니다. 실제 AF2는50개 bin center 전체의softmax probability를 사용합니다. 여기서는 그중0.49·0.69·0.89의세 중심에0.10·0.20·0.70만 놓고 나머지는0으로 이상화한 가상 예제입니다. 유한 logits에서 정확히0이 나온다는 주장은 아닙니다. 다음 슬라이드에서 필요한 reference structure의 구분, 90% 해석 불가, expected value81과최다bin중심89의 차이를 모두 공개합니다. 별도 활동지 없이 화면의 자료를 이용합니다.

[confidence_af2_code] Google DeepMind AlphaFold2: confidence.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/common/confidence.py
[confidence_af2_config] Google DeepMind AlphaFold2: predicted_lddt configuration
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/config.py
[confidence_afdb] AlphaFold Protein Structure Database: FAQ and confidence interpretation
https://alphafold.ebi.ac.uk/faq
[core_af3_output] AlphaFold 3 official output documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/output.md

## 57. 정답·해설 · Reference structure와 pLDDT 계산 (103.0–104.0분)

pLDDT는 predicted local Distance Difference Test입니다. inference 시 새 target의 정답 structure는 입력하지 않고, 이미 training된 model의 internal representation으로 confidence distribution을 출력합니다. softmax는 50개의 logits를 합이 1인 확률로 바꿉니다. 실제 AF2의 bin center은 0.01,0.03,…,0.99입니다. 각 중심에 예측 확률을 곱해 더한 expected value에 100을 곱합니다. 표는 실제 50개 중심 중 0.49·0.69·0.89만 고르고 나머지 확률은 0으로 이상화한 교육용 계산입니다. 유한 logits의 softmax에서 정확히 0이 나온다는 주장이 아닙니다. 합은 0.049+0.138+0.623=0.810으로 81점입니다. 가장 확률이 큰 0.89만 골라 89점으로 보고하지 않습니다. 확률distribution은 score bin에 대한 것이며 pLDDT를 곧바로 structure 정답의 확률로 읽지 않습니다. 실제 lDDT는 나중에 reference structure가 확보되면 따로 계산하고 pLDDT와 비교할 수 있습니다. AF2/ColabFold는 per-residue 점수이며 AF3의 atom별 출력은 정의와 범위를 따로 확인합니다. 예측 PDB의 B-factor 칸에 pLDDT가 저장되어도 실험 열운동 인자는 아닙니다.

[confidence_af2_code] Google DeepMind AlphaFold2: confidence.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/common/confidence.py
[confidence_af2_config] Google DeepMind AlphaFold2: predicted_lddt configuration
https://github.com/google-deepmind/alphafold/blob/main/alphafold/model/config.py
[confidence_afdb] AlphaFold Protein Structure Database: FAQ and confidence interpretation
https://alphafold.ebi.ac.uk/faq
[core_af3_output] AlphaFold 3 official output documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/output.md

## 58. pLDDT의 네 가지 색 · 숫자와 함께 읽기 (104.0–106.0분)

범위를 빈틈없이 표시하기 위해 공식 AF2 confidence.py의 50·70·90 경계 포함 방식을 사용했습니다. 웹 범례에는 >90 등 간략한 표기가 있을 수 있습니다. 진한 파랑은 local atom 배열을 정밀하게 검토할 출발점이지만, 모든 곁사슬·ligand contact가 맞다는 보증은 아닙니다. 하늘색은 골격이 대체로 타당해도 일부 곁사슬 방향은 다를 수 있습니다. 주황 영역은 flexibility이나 intrinsically disordered region일 가능성도 있고, model에 정보가 부족했을 가능성도 있습니다. 점수만으로 둘을 판별하지 않습니다. 69와70을 완전히 다른 생물학적 상태로 분리하지 말고 연속적인 confidence 변화로 읽게 합니다. 실제 ColabFold 3D 화면에서 색을 residue number·점수 그래프와 대응시키며, 체인별 색상으로 바뀌어 있지 않은지 범례를 확인하게 합니다.

[ebi_plddt] EMBL-EBI / Google DeepMind training: pLDDT, Understanding local confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/
[confidence_af2_code] Google DeepMind AlphaFold2: confidence.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/common/confidence.py

## 59. 평균 82.8점이 가리는 낮은 confidence 구간 (106.0–108.0분)

coordinates를 예측한 결과가 아니라 강사가 만든 점수입니다. domain을 실제 5 residue로 만든 protein이 있다는 뜻이 아니라, domain 내부와 linker의 차이를 12개 위치로 줄인 도식입니다. 기존 12열 fictional_learning.a3m과 calmodulin의 결과도 아닙니다. 학생과 왼쪽부터 점수를 따라 읽습니다: 94,93,91,90,88,43,39,86,92,94,93,91. 합계994를12로 나누면82.833…이며 소수점 한 자리로82.8입니다. A의 합계456/5와 B의 합계456/5는 각각91.2이고 linker82/2는41.0입니다. 평균 하나만 보고 모든 부분이 비슷하게 믿을 만하다고 판단하면 두 낮은 위치를 놓칩니다. 반대로 linker가 낮다고 양쪽의 local structure를 모두 버리지 않습니다. 그래프의 가로축은 residue 위치, 세로축은 pLDDT임을 짚고, 이 점수만으로 A와B의 relative placement는 결정할 수 없다고 다음 설명을 예고합니다.

[confidence_afdb] AlphaFold Protein Structure Database: FAQ and confidence interpretation
https://alphafold.ebi.ac.uk/faq

## 60. 바로 실습 · pLDDT 그래프에서 말할 수 있는 것 (108.0–109.0분)

먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. 답①6번43,7번39입니다. ②아닙니다. 평균은 낮은 구간을 가릴 수 있습니다. ③둘 다 확정할 수 없습니다. A·B는 각자 local structure에 대한 confidence가 높지만 서로의 배치에는 별도 정보가 필요합니다. 낮은 linker 점수는 disorder나 flexibility 가설의 출발점이 될 수 있어도 증명은 아닙니다. 낮은 값과 비정형 structure라는 생물학적 결론 사이에 정보 부족 등 다른 원인이 있음을 말하게 합니다. 91.2가A와B의 같은 모양을 뜻한다는 오답도 교정합니다. 점수는 structure 모양 자체가 아니라 그 예측에 대한 confidence입니다. 계산기나 컴퓨터 없이 그래프의 두 낮은 위치를 가리키는 방식으로도 진행합니다.

[ebi_plddt] EMBL-EBI / Google DeepMind training: pLDDT, Understanding local confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/
[confidence_afdb] AlphaFold Protein Structure Database: FAQ and confidence interpretation
https://alphafold.ebi.ac.uk/faq

## 61. 정답·해설 · 평균으로 낮은 confidence 구간을 가리지 않기 (109.0–110.0분)

6번과7번이 각각43과39로 가장 낮습니다. 이 두 값의 평균은41.0입니다. A1–5의 합456/5=91.2, B8–12도456/5=91.2이고 전체는994/12=82.833…입니다. 따라서 전체 평균이82.8이라는 사실과 특정 linker의 낮은 confidence는 동시에 성립합니다. 평균을 이유로 모든 residue를 똑같이 믿거나, linker가 낮다는 이유로 양쪽의 local 예측을 모두 버리지 않습니다. pLDDT는 각 위치 주변 모양의 prediction confidence이므로 상대 domain 방향의 판단에는 관련 PAE 블록을 추가로 확인합니다. 낮은 pLDDT는 flexibility 또는 disorder 가설과 양립하지만 그 증거를 확정하지 않으며 motion rate도 주지 않습니다. 마지막으로 A와B의 평균이같은91.2라는 것은 점수만 같다는 뜻이지 structure가 서로 동일하다는 뜻이 아닙니다. 실제5 residue짜리 domain을 주장하는 자료가 아니라12개 표시 위치로 축약한 교육용 예제입니다.

[ebi_plddt] EMBL-EBI / Google DeepMind training: pLDDT, Understanding local confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/
[confidence_afdb] AlphaFold Protein Structure Database: FAQ and confidence interpretation
https://alphafold.ebi.ac.uk/faq
[ebi_pae] EMBL-EBI / Google DeepMind training: PAE, A measure of global confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/

## 62. PAE · 기준을 고정하면 다른 위치는 얼마나 불확실할까? (110.0–113.0분)

피 에이 이라고 읽습니다. 두 손을 domain A와B로 삼아 A를 기준으로 붙잡고 B의 위치를 얼마나 확신하는지 묻는 비유를 사용합니다. 정확한 정의는 predicted structure와 참 structure를 residue j의 local coordinate frame에 alignment한다고 가정했을 때, residue i에서 예상되는 위치 오차입니다. AF2의 기준 residue에는 위치뿐 아니라 N–Cα–C로 정한 방향도 있으므로 atom 하나만 겹친다는 뜻으로 설명하지 않습니다. 정답 structure를 실제로 열어 계산한 측정 오차가 아니라 model이 예측한 오차이며, 각 residue 쌍에 값이 있어 길이N이면 N×N 표가 됩니다. 이 수업 표에서는 행이 평가 대상 i, 열이 기준 j라고 먼저 약속합니다. 실제 뷰어·원시 배열은 축과 인덱스 정의를 확인합니다. PAE3 Å를 ‘두 residue가3 Å만큼 떨어져 있다’로 읽지 않습니다. 실제 둘 사이가30 Å 떨어져 있어도 relative placement를 잘 확신하면 낮은 PAE일 수 있습니다. 낮은 값일수록 confidence가 높은 점은 pLDDT와 방향이 반대입니다.

[ebi_pae] EMBL-EBI / Google DeepMind training: PAE, A measure of global confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/
[confidence_af2_code] Google DeepMind AlphaFold2: confidence.py
https://github.com/google-deepmind/alphafold/blob/main/alphafold/common/confidence.py
[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2

## 63. PAE 표 읽기 · domain 내부와 domain 사이 (113.0–115.0분)

먼저 A3은 domain A의3번 표시 위치, B9는 domain B의9번 표시 위치임을 설명합니다. 앞 그래프의12×12 전체 PAE를 제시한 것이 아니라 네 위치만 뽑은4×4 교육용 표입니다. linker6·7에 대한 PAE는 여기 없습니다. 대각선0은 설명을 단순화한 값으로 실제 출력이 모두 정확히0이라는 주장이 아닙니다. 왼쪽 위A–A와 오른쪽 아래B–B의 대각선 밖 값1,2를 읽고 내부 배치를 비교적 확신한다고 말합니다. 이어 오른쪽 위A–B의18–21과 왼쪽 아래B–A의22–24는 relative placement에 큰 불확실성이 있음을 보여 줍니다. A3행/B9열18은B9를 기준으로A3을 평가한 값이고, B9행/A3열24는 기준과 대상을 바꾼 값입니다. 방향을 바꾸면 다른 reference coordinates계에서 다른 위치를 평가하므로 PAE는 대칭일 필요가 없습니다. 18과24를 protein 두 위치 사이의 상반된 거리 측정으로 해석하지 않습니다. 표를 평균으로 줄이기 전에 블록과 양방향을 읽습니다.

[ebi_pae] EMBL-EBI / Google DeepMind training: PAE, A measure of global confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/
[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2

## 64. 두 점수 함께 읽기 · 부분의 모양과 relative placement (115.0–117.0분)

조립 블록 두 개의 모양은 잘 만들었지만 두 블록을 연결하는 방향은 모를 수 있다는 비유로 local structure와 relative placement를 구분합니다. 앞 가상 예제에서 domain A·B의 local structure를 검토할 근거는 있지만, 두 domain 사이의 정확한 interface을 자신 있게 설명할 근거는 부족합니다. 높은 domain 사이 PAE는 그 배치의 불확실성이지 실제 동적 이동을 측정한 결과가 아닙니다. 유연한 hinge, 부족한 정보 등 가능한 설명을 구별하려면 다른 예측 조건과 실험 자료가 필요합니다. 반대로 낮은 PAE는 model이 배치를 확신한다는 뜻입니다. 물리적으로 두 protein이 binding하는지, binding affinity이 얼마인지, 어느 상태가 몇 퍼센트인지와는 다른 질문입니다. MSA subsampling·clustering으로 model을 여러 개 만들 때도 pLDDT와 관련 PAE 블록을 먼저 읽고 실제 coordinates의 차이와 비교합니다. pLDDT 최고 model 하나만으로 다른 후보를 모두 버리지 않도록 연결합니다.

[ebi_plddt] EMBL-EBI / Google DeepMind training: pLDDT, Understanding local confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/plddt-understanding-local-confidence/
[ebi_pae] EMBL-EBI / Google DeepMind training: PAE, A measure of global confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/
[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2

## 65. 바로 실습 · 같은 pLDDT, 다른 PAE (117.0–118.0분)

먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. ①B9의 local coordinate frame를 기준으로 alignment했을 때 A3의 expected positional error가18 Å이고, A3을 기준으로 했을 때B9는24 Å입니다. 둘은 다른 기준에서의 예측 오차이며 물리적인 residue 사이 거리가 아닙니다. ②높은 per-region pLDDT와 큰 구간 간 PAE는 모순이 아닙니다. 각 부분의 local 모양을 확신하면서도 relative placement를 확신하지 못할 수 있습니다. ③제시한 네 위치에 관해서는 Q가 A–B relative placement를 더 확신합니다. pLDDT가 같아도 PAE에서 이 차이가 나타납니다. Q의 낮은 값이 실험적으로 더 정확하다는 보증은 아니며, Q라는 상태가 더 많이 존재한다거나 P에서Q로 전이하는 속도를 말해주지 않습니다. linker6·7의 pLDDT는 Q에서도43·39로 그대로 낮습니다. 또한 선택한4×4만으로 생략한 모든 위치의 relative placement가 확실하다고 확대하지 않습니다. 마지막에 학생에게 한 문장 결론을 쓰게 합니다: ‘Q는 제시된 domain 간 위치에 대한 model confidence가 더 높지만, 실제 structure·population은 추가 검증이 필요하다.’ 앞 pLDDT 실습과 같은 가상 데이터이며 실제 GPU inference를 한 결과가 아닙니다.

[confidence_afdb] AlphaFold Protein Structure Database: FAQ and confidence interpretation
https://alphafold.ebi.ac.uk/faq
[ebi_pae] EMBL-EBI / Google DeepMind training: PAE, A measure of global confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/

## 66. 정답·해설 · PAE의 기준과 평가 대상을 나누기 (118.0–119.0분)

먼저 표의 축을 소리 내어 확인합니다. 이 수업의 약속은 행이 평가 대상i, 열이 alignment 기준j입니다. 그러므로 A3행·B9열18은 B9의 local coordinate frame를 맞췄다고 가정했을 때 A3의 위치에 대해 model이 예상하는 오차입니다. 반대쪽24는 A3를 기준으로 삼고 B9를 평가한 값입니다. 기준을 바꾸므로 두 값이같아야 할 이유가 없습니다. 하나의 물리적 거리 A3–B9를 양방향으로 측정해서 서로 다른 숫자가 나왔다는 뜻이 아닙니다. atom 하나의 위치만 맞추는 것이 아니라 기준 residue의 방향까지 포함한 local coordinate frame을 생각합니다. 두 값 모두 model의 예측 오차이며 실험적으로 확인한 오차가 아닙니다. 실제 소프트웨어에서는 축 정의가 이 표와 같은지 먼저 확인합니다. 앞 표는12개 위치 전체의144칸 중3·4·9·10번에 관한16칸만 제시한 교육용 자료입니다.

[ebi_pae] EMBL-EBI / Google DeepMind training: PAE, A measure of global confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/
[core_af2] Jumper et al. (2021), Highly accurate protein structure prediction with AlphaFold
https://www.nature.com/articles/s41586-021-03819-2

## 67. 정답·해설 · Q는 제시된 relative placement를 더 확신한다 (119.0–120.0분)

P와 Q는 동일한 pLDDT 그래프를 갖는다는 문제 조건을 먼저 유지합니다. 따라서 Q에서도 6·7번의 43·39는 그대로이고, 낮은 linker의 local confidence가 좋아졌다고 말할 수 없습니다. P의 선택된 domain 내부쌍은 1·2 Å, domain 사이쌍은 18–24 Å입니다. Q는 제시한 4×4의 대각선 밖 값이 모두 1–3 Å이므로 A–B 위치쌍의 배치에 대한 model confidence가 높아집니다. 낮은 PAE가 낮은 물리적 residue 간 거리라는 의미는 아닙니다. 이 판독은 한 사슬의 두 구간에 대한 것이며, 실제 binding·에너지·equilibrium population·transition rate를 증명하지 않습니다. Q가 현실에서 더 자주 존재한다고 결론 내리지 않습니다. PAE는 model이 예상한 오차이므로 어느 예측이 실험적으로 옳은지는 독립 근거로 검증합니다. 생략한 8개 위치의 PAE가 제공되지 않았으므로 전체 12×12 행렬도 모두 낮다고 일반화하지 않습니다. 학생에게 마지막으로 ‘Q는 제시된 domain 간 위치의 confidence가 더 높다’와 ‘Q가 실제로 우세한 상태다’를 구별하여 말하게 합니다.

[ebi_pae] EMBL-EBI / Google DeepMind training: PAE, A measure of global confidence
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/evaluating-alphafolds-predicted-structures-using-confidence-scores/pae-a-measure-of-global-confidence-in-alphafold-predictions/
[confidence_afdb] AlphaFold Protein Structure Database: FAQ and confidence interpretation
https://alphafold.ebi.ac.uk/faq

## 68. 휴식 (120.0–130.0분)

두 번째 휴식. pLDDT와 PAE의 차이를 한 문장씩 떠올리게 합니다. 이후 ColabFold custom MSA 경로와 입력 조작별 실습을 이어서 진행합니다.



## 69. ColabFold 6 · Custom MSA 업로드 (130.0–131.0분)

먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. MSA options 코드 셀이 실행될 때 파일 업로드 창이 나타납니다. 단순히 드롭다운만 바꾸어서는 업로드가 시작되지 않습니다. 현재 코드는 첫 번째 선택 파일을 사용하고 첫 sequence로 query_sequence를 갱신하므로, UI 입력만 같다고 안심하지 말고 업로드한 A3M의 query를 반드시 비교합니다. 기본 검색 결과 A3M을 그대로 올려 custom 입력 경로를 먼저 확인한 뒤 depth를 비교합니다. 실제 AF-Cluster의 각 cluster A3M도 같은 경로로 한 번에 한 파일씩 넣습니다. Masking 파일도 도구가 만든 정상 A3M과 동일 query일 때 같은 방식으로 입력합니다. 이 강의의 12열 가상 A3M이나 단순 라벨 분할 파일을 실제 CALM1 입력에 섞지 않습니다. 각 조건은 별도 jobname과 다운로드 파일로 보관합니다. 상세 클릭 경로는 examples/colabfold_walkthrough.md에 있습니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

## 70. 실습 확인·해설 · Custom MSA 입력 (131.0–132.0분)

이 페이지는 실행 성공 여부를 점검하는 기준입니다. 실제 GPU structure prediction 결과를 대신하는 모범 coordinates나 고정 점수는 제공하지 않습니다. 앞 실습의 설정과 실제 화면·파일을 대조하고 완료되지 않은 실행은 완료로 표시하지 않습니다. 실제 결과가 서로 다르더라도 입력·조건·출력 이력이 분명하면 비교할 수 있습니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

## 71. AF3에서 custom MSA 지정 (132.0–133.0분)

이 예시는 필드의 뜻을 읽는 용도다. sequence 자리에는 실제 query 전체가 필요하다. unpairedMsaPath는 JSON 파일 기준 상대 경로나 절대 경로다. pairedMsa의 빈 문자열은 paired MSA를 쓰지 않는다는 뜻이며 templates의 빈 목록은 template을 제공하지 않는다는 뜻이다. 필드를 생략하는 것과 명시적으로 빈 값으로 만드는 것은 처리 결과가 다를 수 있다. Path 필드는 입력 포맷 version 2부터 지원한다. examples/prepare_inputs.py가 실제 sequence와 MSA의 일치를 확인하고 실행용 JSON을 만든다.

[core_af3_input] AlphaFold 3 official input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 72. 한 번에 한 조건씩 비교 (133.0–135.0분)

sample 수가 다르면 더 많은 계산을 한 방법이 유리할 수 있다. 방법 간 생성 structure 수, seed 목록, template 유무, model 버전과 recycling 설정을 맞춘다. Depth는 query를 포함하는지 기록한다. 입력 MSA 행 수와 model 내부 max-msa의 두 한도는 구분한다. 어느 조건이 대안 structure를 더 잘 회수하는지는 동일한 평가 기준으로 비교한다. 이 실습에서는 결과를 예상해서 sequence를 골라 넣기보다 조작의 의미와 control을 설명하는 데 중점을 둔다. Depth·group·mask 세 조건은 모두 원본 MSA에서 각각 만들며 앞 조건의 출력에 다음 조작을 연속 적용한 자료가 아닙니다.

[core_cf] ColabFold official repository
https://github.com/sokrypton/ColabFold

## 73. 활동지 4 · 비교 조건을 설계하기 (135.0–137.0분)

먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. 기기가 없으면 종이에 A 또는 B와 이유를 적는다. 강사용 답: B가 행 선택 효과를 분리하기에 낫다. A는 query, template, 반복 수가 함께 바뀌어 차이의 원인을 구별하기 어렵다. B도 선택한 행 집합·MSA effective diversity·동일 seed 집합·코드 버전을 기록해야 재현과 해석이 가능하다.  한 조건씩 비교하는 원리를 설명한 직후 활동지4쪽4번을 풉니다. 실제 조작 파일은 뒤의 각 방법 설명 직후 만들어 확인합니다.

[afcluster_critique] Schafer et al. (2025), Sequence clustering confounds AlphaFold2
https://www.nature.com/articles/s41586-024-08267-2
[afcluster_response] Wayment-Steele et al. (2025), Does Sequence Clustering Confound AlphaFold2?
https://doi.org/10.1016/j.jmb.2025.169376
[ebi_inputs] EMBL-EBI / Google DeepMind training: AlphaFold2 inputs and outputs recap
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap/

## 74. 정답·해설 · 공정한 비교는 B (137.0–138.0분)

활동의 정답은 B입니다. A에서는 같은 protein의 배경 MSA만 바꾼 것이 아니라 query 경계, template 유무, 계산량까지 달라졌습니다. 따라서 structure 차이를 행 선택 탓으로 돌릴 수 없습니다. B는 전체 MSA를 baseline으로 두고 선택 MSA를 비교하므로 질문에 더 가깝습니다. 단, 10회라는 숫자가 같다는 조건만으로 충분하지 않습니다. 동일 model/weight와 동일 예측 seed 목록, template과 recycle 설정, 실제 생성 수를 맞춥니다. 행 추출 seed는 어느 homolog가 입력에 남는지를 정하고 예측 seed는 예측기의 stochastic 처리를 정하므로 둘을 구분해 기록합니다. 입력 MSA의 원시 행 수는 독립 evolutionary information의 수가 아닙니다. 선택 ID와 effective diversity도 함께 확인합니다. 비교한 모든 후보에 같은 structure 지표와 confidence 판정 기준을 적용하고 최고 점수 하나만 골라 방법의 우월성을 판단하지 않습니다. 전체 MSA의 예측 역시 실험적 정답은 아닙니다. content/worksheet_answers.md 4쪽 4번 및 기존 활동 58의 A/B 조건과 대조했습니다.

[afcluster_critique] Schafer et al. (2025), Sequence clustering confounds AlphaFold2
https://www.nature.com/articles/s41586-024-08267-2
[afcluster_response] Wayment-Steele et al. (2025), Does Sequence Clustering Confound AlphaFold2?
https://doi.org/10.1016/j.jmb.2025.169376
[ebi_inputs] EMBL-EBI / Google DeepMind training: AlphaFold2 inputs and outputs recap
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap/

## 75. 기준 예측부터 기록한다 (138.0–139.0분)

이 단원의 질문은 같은 protein에 대해 다른 structure 후보를 얻을 수 있는가이다. 첫 결과를 지우지 말고 baseline으로 보관한다. 학생에게 sequence 길이까지 달라지면 무엇을 비교한 것인지 물어본다. MSA 조작의 효과를 비교할 때 query와 model 버전, template 조건, 반복 수를 맞춘다. 뒤에서 소개할 원래 SPEACH_AF는 query도 편집하는 예외이므로, 오늘의 query 유지 실습과 구분한다.

[ebi_inputs] EMBL-EBI / Google DeepMind training: AlphaFold2 inputs and outputs recap
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap/
[afcluster_code] AF-Cluster author repository and ClusterMSA.py
https://github.com/HWaymentSteele/AF_Cluster/blob/main/scripts/ClusterMSA.py
[speach_code] SPEACH_AF author notebook: SPEACH_AF_scan.ipynb
https://github.com/RSvan/SPEACH_AF/blob/main/SPEACH_AF_scan.ipynb

## 76. 행을 줄인다: MSA subsampling (139.0–141.0분)

아래 alignment는 원리를 설명하기 위한 가상 여덟 자리 예시이며 실제 protein이 아니다. Query를 보존한 채 homolog 1과 3만 택한 경우를 손으로 표시하게 한다. Subsampling은 sequence의 이름을 바꾸는 일이 아니라 실제 들어가는 행의 집합을 바꾸는 일이다. 같은 개수라도 redundant sequence 위주인지, 다양한 homolog를 포함하는지에 따라 정보가 달라진다. 깊이가 얕을수록 항상 더 좋은 것은 아니며 잘못 접힌 결과도 늘 수 있다.

[subsampling_paper] del Alamo et al. (2022), Sampling alternative conformational states of transporters and receptors with AlphaFold2
https://elifesciences.org/articles/75751

## 77. 활동지 4 · Depth를 줄이고 query 확인 (141.0–143.0분)

활동지의 자료와 질문을 모두 화면에 제시합니다. 종이 없이 화면을 읽고 구두 또는 개인 노트로 답한 뒤 바로 다음 정답·해설을 봅니다. 먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. 기본 실행은 depth4/seed7이며 query,A2,A3,B1을 남깁니다. Query 포함4행, alignment12열이고 query는 예측 대상이므로 보존합니다. 원본7행 대비 남긴 lineage·열별 residue빈도·조합빈도가 달라질 수 있습니다. 프로그램은 세 조건 파일을 한 번에 만들지만 여기서는 subsample만 봅니다. 뒤의 group과 mask도 원본7행에서 각각 만들어진 독립 조건입니다. 컴퓨터가 없으면 활동지의 지정4행을 표시합니다. 작은 가상 MSA에 실제 coevolution significance test을 적용하지 않습니다.



## 78. 정답·해설 · Query 포함 4행, alignment 12열 (143.0–144.0분)

현재 practice/msa_lab.py의 subsample(rows, 4, 7)을 직접 실행한 결과와 practice/runs/verified_default/report.json을 대조했습니다. 출력 순서는 원본 순서이며 query, example_A2, example_A3, example_B1입니다. Query는 예측하려는 protein이므로 첫 행에 그대로 둡니다. 소문자 ee와 gap, X도 해당 행의 원문 그대로 남습니다. ee 두 글자를 alignment 열로 세면 14열로 오해하게 됩니다. 원래 A1은 query와 동일한 sequence이어서 이를 제거했다고 독립 정보 한 단위가 정확히 감소한다고 해석하지 않습니다. 행 선택에 따라 diversity, gap 위치와 coverage, 단일 열 빈도 및 여러 열 조합의 빈도가 함께 바뀔 수 있습니다. 이 작은 가상 MSA로 실제 coevolution signal의 유의성을 검정하지 않습니다. 같은 환경·입력·행 추출 seed를 사용하면 같은 부분집합이 나오지만 장기 재현을 위해 코드/Python 버전과 선택 ID도 기록합니다. depth, group, mask 출력은 원본 7행에서 각각 만든 독립 조건이며 순차 가공 결과가 아닙니다. content/worksheet_answers.md 4쪽 1번 및 practice/instructor_answers.md 4번과 일치합니다.



## 79. 논문 그림 읽기: 얕은 MSA의 효과와 한계 (144.0–146.0분)

del Alamo 등의 eLife 연구는 일부 수송체와 수용체를 시험했다. 확대한 A 패널에서 점의 색으로 MSA 깊이를 구분하고, 실험 structure와 예측을 겹친 보기를 확인한다. structure를 더 많이 만들었다는 사실과 정확한 다른 structure를 찾았다는 사실을 분리한다. 원 논문에서는 깊이와 template 선택이 target마다 달랐으며 모든 protein에 통하는 최적 깊이를 정하지 못했다. 이 결과를 모든 protein의 free energy distribution을 재현했다는 주장으로 바꾸지 않는다. 슬라이드에는 원본 Figure 1의 A 패널만 확대하여 표시한다. 점의 색상별 MSA depth와 해당 structure 비교를 읽는다.

[subsampling_paper] del Alamo et al. (2022), Sampling alternative conformational states of transporters and receptors with AlphaFold2
https://elifesciences.org/articles/75751

## 80. ColabFold 7 · 화면에서 MSA depth 비교 (146.0–148.0분)

먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. Advanced settings 아래 Sample settings를 펼칩니다. 현재 공식 노트북의 max_msa 선택지는 auto,512:1024,256:512,64:128,32:64,16:32입니다. 두 비교 조건에는 동일한 실제 calmodulin A3M을 업로드하고 model_type=alphafold2_ptm, num_recycles=3, num_seeds=1, use_dropout=False, template_mode=none을 함께 유지합니다. 웹 노트북은 기본적으로 다섯 model을 사용하므로 두 조건을 모두 같은 방식으로 실행합니다. Runtime→Run all로 입력 셀부터 다시 실행하며 jobname은 조건별로 다르게 적습니다. 입력 MSA 행 수가 한도보다 작으면 그만큼만 사용됩니다. 이 설정은 교육용 비교이며 대안 상태 생성이나 accuracy 향상을 보장하지 않습니다. CLI 예시는 examples/README.md에 따로 있습니다. 웹 UI에는 128:256 선택지가 없으므로 CLI 예시와 혼동하지 않습니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

## 81. 실습 확인·해설 · max_msa 두 조건 비교 (148.0–149.0분)

이 페이지는 실행 성공 여부를 점검하는 기준입니다. 실제 GPU structure prediction 결과를 대신하는 모범 coordinates나 고정 점수는 제공하지 않습니다. 앞 실습의 설정과 실제 화면·파일을 대조하고 완료되지 않은 실행은 완료로 표시하지 않습니다. 실제 결과가 서로 다르더라도 입력·조건·출력 이력이 분명하면 비교할 수 있습니다.

[core_cf_nb] ColabFold AlphaFold2 official notebook
https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb

## 82. AF-Cluster: sequence를 먼저 나누어 예측 (149.0–152.0분)

그림에서 먼저 나누는 대상은 아직 structure가 없는 sequence들임을 짚는다. AF-Cluster는 sequence similarity로 만든 작은 MSA들을 예측에 사용한다. 그림 속 KaiB는 circadian clock protein이며 알려진 두 fold와 예측을 비교하는 교육 예시이다. 이 성공 사례가 모든 protein의 숨은 상태를 찾아준다는 보장은 아니다. 논문은 온라인 2023년, Nature 권호는 2024년이므로 참고문헌 연도가 다른 이유를 짧게 설명한다. 실제 실행 단계는 examples/afcluster_guide.md를 사용한다. 공식 ClusterMSA.py의 positional 인자와 flags를 확인한 명령, query 보존 검사, cluster별 ColabFold 실행이 들어 있다. 이 자료 제작 중 실제 GPU 예측은 실행하지 않았다.

[afcluster_paper] Wayment-Steele et al. (2024), Predicting multiple conformations via sequence clustering and AlphaFold2
https://www.nature.com/articles/s41586-023-06832-9
[afcluster_code] AF-Cluster author repository and ClusterMSA.py
https://github.com/HWaymentSteele/AF_Cluster/blob/main/scripts/ClusterMSA.py

## 83. 각 cluster에도 같은 query가 들어간다 (152.0–153.0분)

AF-Cluster 저자 코드에서 query는 처음에 분리되고 각 cluster 파일을 쓸 때 다시 맨 앞에 붙는다. 가상 alignment에서 두 입력의 첫 줄이 완전히 같은지 학생이 확인하게 한다. sequence cluster에 query와 먼 homolog가 포함될 수 있어도 예측 대상은 첫 query이다. 이것은 각 cluster의 대표 homolog structure를 각각 예측하는 실험과 다른 질문이다. 실습에서는 query를 변경하거나 원본을 덮어쓰지 않는다.

[afcluster_code] AF-Cluster author repository and ClusterMSA.py
https://github.com/HWaymentSteele/AF_Cluster/blob/main/scripts/ClusterMSA.py

## 84. 활동지 4 · 두 그룹의 MSA를 직접 비교 (153.0–155.0분)

활동지의 자료와 질문을 모두 화면에 제시합니다. 종이 없이 화면을 읽고 구두 또는 개인 노트로 답한 뒤 바로 다음 정답·해설을 봅니다. 먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. 각 그룹은 query 1행과 해당 homolog 3행으로 총 4행입니다. 교육용 header의 group=A/B에 따라 미리 분리했으며 거리 기반 AF-Cluster를 구현한 것이 아닙니다. A homolog의 5열은 F,F,gap이고 B의 5열은 Y,Y,Y입니다. A의 11열은 M,M,M이고 B는 X,gap,X입니다. 두 열을 비교해 선택한 sequence 집합이 residue distribution과 coverage까지 바꿈을 확인합니다. Coevolution 활동지 3쪽에서는 가상 gene history를 주었지만 이 파일에는 ortholog/paralog 판정 근거가 없습니다. Cluster마다 같은 query를 넣어도 conformational state 분류나 coevolution 증명이 되지는 않습니다. 실제 clustering 명령은 examples/afcluster_guide.md로 시연합니다.



## 85. 정답·해설 · 그룹마다 residue distribution이 달라진다 (155.0–156.0분)

현재 practice/msa_lab.py의 prelabelled_groups 결과를 직접 계산하여 확인했습니다. 두 파일의 첫 query는 모두 ACDEFGHIKLMN입니다. Query를 제외하고 A1/A2/A3 순서로 5열을 읽으면 F,F,-이고 11열은 M,M,M입니다. B1/B2/B3는 각각 Y,Y,Y와 X,-,X입니다. X는 alignment 열 하나를 차지하지만 residue 정체를 알 수 없고, gap은 해당 alignment 위치에 대응하는 residue가 없다는 표식입니다. 따라서 B의 11열을 세 종류의 알려진 amino acid distribution로 세면 안 됩니다. Query를 포함해 빈도를 계산하면 각 그룹에 query의 5열 F와 11열 M이 하나씩 더해지므로, 분모와 query 포함 여부를 반드시 명시합니다. 이 활동의 A/B는 3쪽 coevolution 문제에서 evolutionary history가 주어진 gene A/B와 별개입니다. 이 파일에는 speciation·gene duplication 관계를 판정할 근거가 없습니다. sequence similarity로 실제 clustering을 수행하더라도 sequence 그룹이 conformational state·상태 수·population과 곧바로 같아지는 것은 아닙니다. content/worksheet_answers.md 4쪽 2번과 기존 활동 66의 5열/11열 distribution에 일치합니다.



## 86. sequence cluster는 thermodynamic 상태가 아니다 (156.0–157.0분)

앞 단원에서 배운 speciation과 gene duplication을 연결한다. Ortholog와 paralog는 evolution 사건에 대한 관계이고 open과 closed는 conformational state에 대한 말이다. sequence similarity만으로 만든 집합은 ortholog만을 보장하지 않으며 functional 분화도 포함할 수 있다. 어떤 sequence cluster에서 structure가 잘 나왔다는 사실만으로 그 집합이 특정 thermodynamic 상태를 뜻한다고 부르지 않는다. species별 sequence 데이터 수가 많다는 사실도 molecule의 state population과는 무관하다.

[afcluster_paper] Wayment-Steele et al. (2024), Predicting multiple conformations via sequence clustering and AlphaFold2
https://www.nature.com/articles/s41586-023-06832-9
[afcluster_response] Wayment-Steele et al. (2025), Does Sequence Clustering Confound AlphaFold2?
https://doi.org/10.1016/j.jmb.2025.169376

## 87. 2025년 논쟁: 비교 조건을 읽는다 (157.0–158.0분)

Schafer 등은 Nature Matters Arising에서 CF-random과 비교하고 evolutionary coupling 해석에 이의를 제기했다. Wayment-Steele 등의 2025년 JMB 응답은 비교 조건의 혼입을 지적하고 추가 분석으로 반박했다. 두 문헌을 함께 소개하며 한쪽의 제목을 확정된 결론처럼 읽지 않는다. 학생에게 비교에서 MSA 깊이, model 설정, seed 수가 달라지면 어느 요인의 효과인지 구분 가능한지 묻는다. 여기서 보편적 우승 방법을 정하지 않고 연구 질문에 맞는 대조 실험의 중요성을 가르친다.

[afcluster_critique] Schafer et al. (2025), Sequence clustering confounds AlphaFold2
https://www.nature.com/articles/s41586-024-08267-2
[afcluster_response] Wayment-Steele et al. (2025), Does Sequence Clustering Confound AlphaFold2?
https://doi.org/10.1016/j.jmb.2025.169376

## 88. 두 가지 clustering을 구별한다 (158.0–159.0분)

Clustering이라는 단어만 보지 말고 무엇을 어떤 거리로 묶었는지 확인하게 한다. 입력에서는 alignment된 sequence의 차이를 이용한다. 출력에서는 적절히 alignment한 coordinates나 domain 간 거리, contact 양상처럼 질문에 맞는 structure 특징을 이용한다. 입력이 세 그룹이어도 출력이 두 structure 그룹일 수 있고 반대도 가능하다. 이 표는 일반 분석 설계이며 특정 논문의 cluster 수를 재현한 자료가 아니다.

[afcluster_code] AF-Cluster author repository and ClusterMSA.py
https://github.com/HWaymentSteele/AF_Cluster/blob/main/scripts/ClusterMSA.py
[afsample2_code] wallnerlab/AFsample2 author repository
https://github.com/wallnerlab/AFsample2

## 89. 열을 가린다: unknown X와 gap의 차이 (159.0–161.0분)

이 예시는 AFsample2의 아이디어를 가상 alignment로 설명한다. Homolog의 네 번째 alignment 위치만 X로 가렸고 query는 그대로임을 확인한다. X를 gap으로 대신 쓰면 같은 의미가 아니며, 열 자체를 지우면 길이와 coordinates 대응도 바뀐다. A3M에서는 소문자 insertion이 alignment 열에 그대로 세어지는 것이 아니므로 실제 입력에서는 포맷을 이해해야 한다. 여기서는 모두 대문자와 gap만 있는 작은 alignment로 열의 의미에 집중한다.

[afsample2_paper] Kalakoti and Wallner (2025), AFsample2 predicts multiple conformations and ensembles with AlphaFold2
https://www.nature.com/articles/s42003-025-07791-9
[af3_input] Google DeepMind AlphaFold 3 input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 90. 활동지 4 · A2의 5·7·10열을 X로 가리기 (161.0–162.0분)

활동지의 자료와 질문을 모두 화면에 제시합니다. 종이 없이 화면을 읽고 구두 또는 개인 노트로 답한 뒤 바로 다음 정답·해설을 봅니다. 먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. A2의 결과는 ACDeeEXGXIKXMN입니다. Query, 소문자 ee, 기존 gap은 보존하고 homolog의 5·7·10열 residue 정체를 가립니다. 먼저 파일 전체를 대문자로 바꾸면 insertion이 alignment 열이 되어 잘못된 위치를 가리게 됩니다. 선택 열의 기존 gap은 그대로 두며 X는 gap과 다릅니다. Mask는 해당 열의 conservation과 다른 열과의 조합 정보를 함께 약화시킬 수 있습니다. 실제 model의 X 처리와 다른 입력에 따라 예측 반응이 다르므로 특정 contact만 선택적으로 꺼졌다고 해석하지 않습니다.



## 91. 정답·해설 · A2의 완성 문자열과 열 번호 (162.0–163.0분)

현재 practice/msa_lab.py의 mask_homologs(rows, {5,7,10})을 직접 실행하고 저장된 masked.a3m 및 두 교사용 해설과 대조했습니다. A2의 query alignment 문자열은 ACDEFGHIKLMN입니다. 이 문자열의 5열 F, 7열 H, 10열 L을 가리므로 aligned 결과는 ACDEXGXIKXMN이고 원문에 ee를 그대로 남기면 ACDeeEXGXIKXMN이 됩니다. A2 원문의 4·5번째 글자인 ee는 insertion이므로 alignment 번호가 없습니다. 원문 6–14번째 글자가 alignment 4–12열에 대응합니다. 1-based 원문 위치 7·9·12는 Python의 0-based 문자열 index 6·8·11입니다. A3는 원래 5열에 gap이 있어서 그 열을 X로 바꾸지 않으며 7열과 10열의 residue만 바뀝니다. A3 결과는 ACDE-GXIKXMN입니다. 파일의 모든 homolog에 같은 alignment 열 규칙을 적용하되 query는 건너뜁니다. 이 화면은 허구 12열 alignment의 손계산 답이며 실제 protein의 variation 설계가 아닙니다. content/worksheet_answers.md 4쪽 3번 및 practice/instructor_answers.md 6–7번에 일치합니다.



## 92. 정답·해설 · X로 가린 정보와 남긴 정보 (163.0–164.0분)

masking 결과를 쓸 수 있다는 것과 원래 예측 방법을 재현했다는 것을 분리합니다. 여기서는 지정한 5·7·10열에서 homolog의 알려진 대문자 residue를 X로 바꿉니다. 기존 X는 X로 남고 gap은 그대로이므로 residue 정체를 가리더라도 gap과 coverage 패턴은 남습니다. 이 조작은 한 열의 conservation도와 빈도, 다른 열과의 residue 조합 정보를 동시에 바꿀 수 있습니다. 특정 contact의 정보만 선택적으로 제거한 것으로 해석할 수 없습니다. 예측기의 X 인코딩과 나머지 입력에 따라 효과가 달라질 수 있어 예측 반응을 이 문자열만 보고 단정하지 않습니다. AFsample2의 실제 파이프라인은 무작위 열 선택, dropout을 포함한 예측과 여러 후보 생성 등을 수행하므로 고정 열 X substitution만 한 오늘의 실습과 같지 않습니다. 동일 query·model·seed 집합으로 원본 control과 비교해야 변화의 원인을 판단할 수 있습니다. Query를 바꾸면 target 자체가 달라지고, depth/group 결과에 추가 masking을 하면 행과 열 조작이 함께 달라지므로 오늘의 독립 조건 비교와 다른 실험이 됩니다. 현재 프로그램은 원본 7행에서 depth/group/mask 파일을 각각 만듭니다.

[afsample2_paper] Kalakoti and Wallner (2025), AFsample2 predicts multiple conformations and ensembles with AlphaFold2
https://www.nature.com/articles/s42003-025-07791-9
[afsample2_code] wallnerlab/AFsample2 author repository
https://github.com/wallnerlab/AFsample2
[af3_input] Google DeepMind AlphaFold 3 input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 93. SPEACH_AF와 AFsample2는 같은 편집이 아니다 (164.0–166.0분)

Alanine은 실제 amino acid A이고 unknown X와 다르다. 원 SPEACH_AF 논문과 저자 notebook은 선택한 위치를 alignment의 모든 sequence에서 A로 편집하며 query도 포함하고 gap은 유지한다. 따라서 query를 고정한 masking 실습을 원 논문의 정확한 재현이라고 부르면 안 된다. AFsample2 논문은 query 첫 행을 제외하고 무작위로 선택한 열을 X로 바꾸고 dropout과 함께 사용한다. 이 슬라이드는 방법 개념 비교이며 특정 protein의 substitution 설계를 다루지 않는다.

[speach_paper] Stein and Mchaourab (2022), SPEACH_AF: Sampling protein ensembles and conformational heterogeneity with Alphafold2
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010483
[speach_code] SPEACH_AF author notebook: SPEACH_AF_scan.ipynb
https://github.com/RSvan/SPEACH_AF/blob/main/SPEACH_AF_scan.ipynb
[afsample2_paper] Kalakoti and Wallner (2025), AFsample2 predicts multiple conformations and ensembles with AlphaFold2
https://www.nature.com/articles/s42003-025-07791-9

## 94. 논문 그림 읽기: AFsample2의 입력과 출력 (166.0–168.0분)

그림 a에서 MSA 가로와 세로 방향을 손으로 가리키며 앞 두 실습을 연결한다. 예측 뒤에는 structure 파일을 분석하여 후보의 품질과 diversity를 확인해야 한다. 논문의 일부 benchmark에서 대안 structure와 비슷한 후보를 더 잘 찾았지만 효과는 target과 설정에 의존한다. 두 알려진 structure 사이에 보이는 model은 가능한 중간 structure 가설이며 실제 전이 경로 위에 있다는 증명은 아니다. 슬라이드는 원본 Figure 1a만 확대해 표시한다. 저자의 제안 개념도이며 masking이 열림을 일으킨다는 직접 증거가 아니다. 실제 AFsample2에서 query 첫 행은 유지한다.

[afsample2_paper] Kalakoti and Wallner (2025), AFsample2 predicts multiple conformations and ensembles with AlphaFold2
https://www.nature.com/articles/s42003-025-07791-9

## 95. FASTA 제목에 open을 쓰면 열릴까? (168.0–169.0분)

학생에게 첫 두 레코드에서 바뀐 것이 실제 amino acid인지 이름인지 묻는다. Open이라고 이름을 붙였다는 이유로 열린 structure를 요구하는 프롬프트가 되는 것은 아니다. 다만 header는 언제나 무의미하다고 설명해서도 안 된다. 일부 multimer 파이프라인은 종 식별 정보를 읽어 MSA pairing에 사용하므로 임의로 바꾸면 입력 처리에 영향을 줄 수 있다. monomer의 자유로운 별칭과 structure prediction용 생물학적 metadata를 구별한다.

[af3_input] Google DeepMind AlphaFold 3 input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md

## 96. Seed·dropout·template도 별도 요인이다 (169.0–170.0분)

Seed를 바꾸면 같은 설정에서 다른 결과가 나올 가능성이 있지만 반드시 다른 structure가 생기지는 않는다. Dropout은 구현이 지원하는 경우에만 inference에서 활성화할 수 있으며, diversity를 높여도 물리적 온도를 올리는 실험은 아니다. Template은 강한 사전 정보가 될 수 있어 독립적인 발견이라는 주장과 구분한다. 같은 MSA 두 조건을 비교한다면 나머지 설정과 반복 수를 맞추고 모두 기록해야 한다. 이 표는 요인 분리를 위한 설명이며 GPU 실행 지침이 아니다.

[ebi_inputs] EMBL-EBI / Google DeepMind training: AlphaFold2 inputs and outputs recap
https://www.ebi.ac.uk/training/online/courses/alphafold/inputs-and-outputs/alphafold-inputs-and-outputs-recap/
[afsample2_code] wallnerlab/AFsample2 author repository
https://github.com/wallnerlab/AFsample2
[subsampling_paper] del Alamo et al. (2022), Sampling alternative conformational states of transporters and receptors with AlphaFold2
https://elifesciences.org/articles/75751

## 97. AF2 근거를 AF3에 그대로 옮길 수는 없다 (170.0–171.0분)

AF3는 protein 외 molecule를 함께 다루는 model이며 structure 생성 방식도 AF2와 다르다. 로컬 공식 AF3 문서는 custom A3M을 지원하지만 첫 sequence와 query의 일치를 요구한다. 공개 AlphaFold Server와 로컬 코드의 입력 제어 범위가 같다고 가정하지 않는다. AFsample3 연구 저장소가 존재함을 확인했으므로 AF3에서는 불가능하다고 단정하지 않는다. 동시에 이 강의의 AF2 benchmark 수치를 AF3의 성능 수치로 제시하지 않는다.

[af3_paper] Abramson et al. (2024), Accurate structure prediction of biomolecular interactions with AlphaFold 3
https://www.nature.com/articles/s41586-024-07487-w
[af3_input] Google DeepMind AlphaFold 3 input documentation
https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md
[afsample3_code] wallnerlab/afsample3 research implementation
https://github.com/wallnerlab/afsample3

## 98. 활동지 7 · 후보 8개를 confidence와 함께 판독 (171.0–173.0분)

활동지의 자료와 질문을 모두 화면에 제시합니다. 종이 없이 화면을 읽고 구두 또는 개인 노트로 답한 뒤 바로 다음 정답·해설을 봅니다. 먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. practice/synthetic_comparison.json의 8개 후보 전체를 제시했다. 가상 180 residue target이며 12열 가상 A3M에서 계산한 값이 아니다. 선택 거리는 40번과 140번 Cα 사이 거리이며 PAE는 구간 20–70과 110–160 사이 두 방향 블록의 평균이다. F1/F2는 가까운 거리, S1은 더 먼 거리를 보여 서로 다른 후보를 검토할 수 있다. S2는 낮은 평균 pLDDT와 높은 PAE 때문에 먼저 품질을 확인한다. F2의 평균 pLDDT가 가장 높아도 이 하나만 남기면 diversity를 놓칠 수 있다. 두 상태의 실재 여부나 population은 이 가상 표에서 알 수 없다. 전체 8행 비교와 상세 답안은 practice/instructor_answers.md에 있다. MSA 조작 결과를 앞서 배운 pLDDT·PAE로 다시 평가하며 활동지7쪽을 풉니다. 핵심은1번과3번이며 시간이 남으면2번을 토의합니다. 같은 sequence 구간과 atom을 alignment해 비교하며 RMSD는 alignment 기준에 따라 달라짐을 설명합니다. local pLDDT와 구간 간 PAE, atom 충돌, structure diversity를 함께 보고 대표 후보를 남깁니다.



## 99. 정답·해설 · 거리와 confidence를 함께 비교 (173.0–175.0분)

활동지7쪽1–2번의 예시 답안입니다. 전체8행은 practice/synthetic_comparison.json에 있는 가상 숫자로 실제 model을 실행한 결과가 아닙니다. 화면 문제에 나온 F1/F2/S1/S2를 먼저 읽고, 활동지의 A1/B1/M1/M2를 같은 기준으로 추가합니다. S2/M2의 낮은 평균 pLDDT와 높은 구간 간 PAE는 먼저 불확실성을 점검할 이유이며 새로운 상태가 없음을 증명하는 기준도 아닙니다. 약8/16Å라는 묶음은 한 관측량을 기준으로 한 임시 분류입니다. 전체 PAE와 local pLDDT, atom 충돌, 동일 seed 집합의 반복 결과를 확인합니다.



## 100. 정답·해설 · 3/8은 equilibrium population이 아니다 (175.0–176.0분)

활동지7쪽3번 정답은3/8=37.5%는 이 가상 생성물 집합의 비율이라는 것입니다. 16Å 후보3개를 open state로 이름 붙이는 것부터 추가 structure 확인이 필요합니다. confidence 낮은 S2/M2를 제외하면 분모가 달라지는 사실도 sample과 선별 방식이 비율에 영향을 준다는 설명에 사용할 수 있습니다. 어떤 분모를 골라도 현재 자료에는 equilibrium distribution을 대표한다는 근거가 없습니다. 높은 confidence 후보는 후속 검증의 출발점으로 남기되 population이나 transition rate로 해석하지 않습니다.

[afcluster_critique] Schafer et al. (2025), Sequence clustering confounds AlphaFold2
https://www.nature.com/articles/s41586-024-08267-2
[afcluster_response] Wayment-Steele et al. (2025), Does Sequence Clustering Confound AlphaFold2?
https://doi.org/10.1016/j.jmb.2025.169376

## 101. 최종 설명 활동 (176.0–177.0분)

먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. 첫 주장에는 ortholog 사이에도 남는 common ancestor 효과와 간접 관계, contact 검증이 빠졌다. 두 번째에는 sequence cluster와 conformational state의 대응 검증이 빠졌다. 세 번째에는 샘플링 distribution이 물리적 equilibrium distribution에 대응한다는 검증이 빠졌다. 학생에게 무조건 틀렸다고 외우게 하기보다 무엇을 추가로 알아야 하는지 묻는다. 평가 기준은 사건 기준으로 관계를 설명하는가, 입력 분할과 structure 분류를 구분하는가, model 점수와 물리적 확률을 구분하는가이다. 정답은 배포 활동지에 넣지 않는다.



## 102. 정답·해설 · 세 주장을 근거에 맞게 고치기 (177.0–178.0분)

세 문장을 한 문장씩 바꾸게 한 뒤 표의 예시와 비교합니다. 첫째는 gene의 분기 관계와 두 위치의 evolutionary 의존성, 직접 공간 contact를 구분하는지 봅니다. 둘째는 입력 sequence 집합의 cluster와 출력 coordinates의 structure 분류를 구분하는지 봅니다. 셋째는 알고리즘의 생성 빈도와 실제 물리적 population을 구분하는지 봅니다. Ortholog 선택이나 coevolution 분석을 무용하다고 결론짓지 말고 structural information을 주는 단서를 적절한 가정 아래 활용한다고 설명합니다.

[evo_covariation] Rodriguez Horta & Weigt (2021). On the effect of phylogenetic correlations in coevolution-based contact prediction in proteins.
https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008957
[afcluster_critique] Schafer et al. (2025), Sequence clustering confounds AlphaFold2
https://www.nature.com/articles/s41586-024-08267-2
[afcluster_response] Wayment-Steele et al. (2025), Does Sequence Clustering Confound AlphaFold2?
https://doi.org/10.1016/j.jmb.2025.169376

## 103. 오늘 배운 내용 (178.0–179.0분)

학생이 자기 연구 대상에 적용할 때 첫 질문은 어떤 protein이며 어떤 structure 차이를 확인하려는가이다. 모든 protein에서 여러 상태를 얻는 것이 수업의 성공 기준은 아니다. 변화를 얻지 못해도 입력 품질과 대조 조건을 확인하면 의미 있는 기록이다. 후속 과제로 benign한 관심 protein 하나의 accession, sequence 경계, MSA 기준선, 조작 조건, 판정 지표를 제안하도록 할 수 있다.



## 104. 논문과 실행 문서 (179.0–180.0분)

관련 문서는 계속 바뀌므로 실제 시연 전에 설치한 버전의 도움말과 공식 문서를 다시 확인한다. 이 강의는 MSA 조작을 손쉽게 상태를 제어하는 보장된 절차로 설명하지 않는다. 모든 수치 예제와 가상 sequence는 실제 실험 자료와 명확히 구분한다. 주요 논문과 도구 문서 링크를 소개하고 질문을 받는다.

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
