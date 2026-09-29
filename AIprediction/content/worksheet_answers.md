# 학생 활동지 해설 · 교사용

작성: Donghan Lee

진행: 모든 문항과 필요한 자료가 강의 화면에 내장되어 있으므로 슬라이드만 보며 수업할 수 있습니다. 문제 바로 다음 화면에 정답·해설을 제시하고 이 문서는 보충 설명에 사용합니다. 정답을 채우지 않은 7쪽 PDF는 선택 인쇄용입니다. 4쪽의 비교 설계·depth·clustering·masking 문항은 각 설명 직후 나누어 풉니다. 5쪽의 계산표와 training·inference 문항도 모두 화면에 포함되며, 거리 변경(53–54)은 풀이·해설을 합해 1분입니다.

| 선택 인쇄본 | 문제 슬라이드 → 정답·해설 슬라이드 |
|---|---|
| 1쪽 · 상황 A/B evolutionary relationship | 12 → 13–14 |
| 2쪽 · 전체 A3M | 21 → 22–23 |
| 3쪽 · 빈도 / lineage 해석 | 31 → 32 / 36 → 37 |
| 4쪽 · 비교 / depth / clustering / masking | 73 → 74 / 77 → 78 / 84 → 85 / 90 → 91–92 |
| 5쪽 · 계산표 / 거리 변경 / training·inference | 51 → 52 / 53 → 54 / 56 → 57 |
| 6쪽 · pLDDT / PAE | 60 → 61 / 65 → 66–67 |
| 7쪽 · 후보 비교 | 98 → 99–100 |

## 1쪽 · speciation과 gene duplication

1. H_A–M_A는 ortholog입니다. 두 gene의 MRCA에서 speciation이 일어났습니다. H_A–H_B와 H_A–M_B는 paralog입니다. 두 경우의 gene 분기는 gene duplication 사건에서 시작합니다. 서로 다른 species의 gene도 paralog일 수 있습니다.
2. H1–H2는 paralog, H1–M과 H2–M은 각각 ortholog입니다. M을 기준으로 H1·H2는 co-ortholog 관계입니다. speciation 후 gene duplication이 생겼기 때문입니다. 관계는 비교하는 gene 쌍에 대해 정의합니다.
3. gene tree와 species tree, gene duplication·speciation·loss 사건에 대한 근거가 필요합니다. 높은 identity나 서로 다른 species이라는 정보만으로 orthology를 확정하지 않습니다.

## 2쪽 · A3M 읽기

1. Query 포함 7행, homolog 6행, alignment 열 12개입니다. query와 동일한 homolog가 있어도 원시 행 수에는 포함되지만 독립 정보가 늘었다고 볼 수는 없습니다.
2. `ee`는 query alignment 4열 직전의 insertion입니다. `ACDeeEFGHIKLMN`의 원문 길이는 14지만 alignment 열은 12개입니다. 대문자화하면 insertion을 match column으로 오해합니다.
3. A3의 5열은 gap이고 B1의 11열은 X입니다. Gap은 해당 alignment 위치에 residue가 없는 대응, X는 residue의 정체를 모르는 표식입니다. 실습에서는 알고 있는 homolog residue를 X로 가리는 경우도 있습니다.
4. 단순 복제는 독립 evolutionary information을 늘리지 않습니다. Coverage·diversity·redundancy와, 정의를 기록한 Neff를 함께 봅니다.

## 3쪽 · Coevolution과 ortholog/paralog

이 표는 계산을 위한 가상 자료입니다. A/B gene duplication이 H·M·R·F의 speciation보다 앞섰다는 gene history를 문제에서 주었습니다. 실제 sequence를 보고 이 이력을 추정한 결과가 아닙니다.

1. 합친 8행에서 `P(D_i) = 4/8 = 1/2`, `P(K_j) = 4/8 = 1/2`, `P(D_i, K_j) = 4/8 = 1/2`입니다. 독립이라면 joint frequency는 `(1/2) × (1/2) = 1/4`여야 합니다. 두 열에 statistical association이 있습니다. 대조 자료는 `DD`, `DK`, `KD`, `KK`가 각각 2행이므로 각 열의 D/K 빈도는 같은 1/2이지만, `P(D_i, K_j) = 2/8 = 1/4`입니다. 다른 세 조합도 모두 1/4입니다. 한 열씩 보는 conservation·빈도가 같아도 두 열의 joint distribution은 달라질 수 있습니다. 이 빈도 계산만으로 evolution 과정에서 두 위치가 서로 영향을 주었다고 입증한 것은 아닙니다.
2. A_H–A_M은 ortholog, A_H–B_M은 paralog입니다. A 내부에는 `DK`만 있고 B 내부에는 `KD`만 있습니다. 따라서 각 subfamily 안에는 두 위치 모두 variation가 없어 그 안의 covariation을 평가할 정보가 없습니다. 합친 표의 패턴은 subfamily 구분과 완전히 겹칩니다. A/B에서 서로 다른 조합을 ancestor로부터 물려받은 경우에도 같은 표를 얻을 수 있습니다.
3. 8개 sequence 행은 8회의 독립적인 evolution 사건이 아닙니다. 여러 후손이 ancestor에게서 같은 residue 조합을 물려받았을 수 있습니다. ancestor 상태와 변화가 일어난 가지를 재구성하지 않고 변화 횟수·방향·보상 순서를 정할 수 없습니다. residue들이 direct contact한다는 결론도 내릴 수 없습니다. indirect coupling, 다른 functional constraint, lineage·subfamily 효과가 statistical association을 만들 수 있습니다. D/K의 charge가 반대라는 사실만으로 salt bridge를 단정하지 않습니다.
4. Ortholog들 역시 common ancestor를 공유하므로 phylogenetic non-independence이 남습니다. 가까운 종을 많이 모은 것과 여러 독립 가지에서 variation가 반복된 것은 다릅니다. 필요한 근거의 예: species tree와 gene duplication·loss을 고려한 gene history, 정확한 alignment와 충분한 variation·phylogenetic diversity, subfamily별 분석, 독립 가지의 변화 여부, indirect association을 고려하는 coupling analysis, contact를 확인할 structure·실험 자료. 행 수나 Neff만 늘리는 것으로 모든 교란이 사라지지는 않습니다. coevolution 분석에 paralog를 무조건 제외하는 규칙을 적용하기보다 분석 목표와 domain·function·lineage 구성을 확인합니다.

교사용 핵심 문장: **Ortholog/paralog는 gene들이 어떤 사건으로 갈라졌는지를 설명하고, coevolution은 위치·molecule 사이 evolutionary constraint의 연결을 묻습니다. MSA에서 보이는 covariation은 그 연결을 탐색하는 관측 신호이며, evolutionary history를 함께 보아야 합니다.**

## 4쪽 · 입력 조작과 대조 조건

1. 첫 행은 원래 query입니다. Query를 바꾸면 예측하려는 protein 자체가 달라집니다. 같은 protein에서 MSA 배경만 바꾸려는 비교에서 query를 고정합니다.
2. Group A/B는 가상 header의 사전 라벨로 나눈 것입니다. 3쪽의 A/B에는 evolutionary history가 문제 조건으로 주어졌지만, 2·4쪽 A3M의 A/B는 이와 별개인 임의 라벨입니다. 이 라벨만으로 orthology·paralogy를 판단할 수 없습니다. AF-Cluster는 실제 sequence의 similarity를 바탕으로 clustering합니다. 라벨 A/B가 open state/closed state를 뜻하지 않습니다.
3. A2의 결과는 `ACDeeEXGXIKXMN`입니다. 소문자 `ee`는 보존하고, query 전체와 기존 gap도 보존합니다. 5·7·10은 원문 문자열의 문자 위치가 아닌 query alignment 열입니다.
4. 예: model·weight 버전, query 경계, template 유무, ligand/complex 조성, 예측 seed, sampling seed, recycle 조건, 생성 model 수, MSA 검색 DB·날짜. 모든 설정을 동시에 바꾸면 결과 변화의 원인을 분리하기 어렵습니다.

## 5쪽 · lDDT 계산과 pLDDT의 차이

**표 계산:** Cα 거리 네 쌍만 사용한 가상 예제입니다. reference distance로 neighbor를 고르고, reference distance와 predicted distance의 차이를 평가합니다. 전체 structure를 겹치는 rotation·translation alignment 없이 내부 거리끼리 비교합니다. 실제 lDDT-Cα 계산에는 대상 residue의 유효한 모든 해당 neighbor 쌍을 사용하며, 이 표가 실제 protein의 neighbor 네 개라는 뜻은 아닙니다.

| neighbor | reference distance | predicted distance | absolute error | 오차가 미만인 기준 | 통과 횟수 |
|---|---:|---:|---:|---|---:|
| a | 4 Å | 4.2 Å | 0.2 Å | 0.5, 1, 2, 4 Å | 4 |
| b | 7 Å | 7.8 Å | 0.8 Å | 1, 2, 4 Å | 3 |
| c | 10 Å | 11.5 Å | 1.5 Å | 2, 4 Å | 2 |
| d | 14 Å | 17 Å | 3 Å | 4 Å | 1 |

통과 합은 10, 평가 횟수는 `4쌍 × 4기준 = 16`이므로 `lDDT_i = 10/16 = 0.625`입니다. 100을 곱해 표시하면 **62.5**입니다. 이는 주어진 reference structure와 비교해 계산한 이 residue의 점수이며 pLDDT 예측값이 아닙니다. 반대로 기준별 통과 쌍의 비율 `1, 3/4, 2/4, 1/4`를 평균해도 0.625입니다. 이 자료에서는 판정 기준을 엄밀히 **미만(`<`)**으로 사용하며 경계와 같은 오차는 통과시키지 않습니다.

1. **포함, 9/16, 56.25점**입니다. d의 predicted distance가 19 Å로 바뀌면 오차는 5 Å이며 네 기준을 모두 통과하지 못합니다. 통과 횟수 합만 `4+3+2+0 = 9`로 줄어듭니다. neighbor 선택은 **reference structure의 거리 14 Å**로 결정했으므로 d는 여전히 포함되며 분모는 16입니다. 예측이 멀어졌다는 이유로 d를 빼면 큰 오차를 평가에서 제거하여 점수가 부당하게 좋아집니다. 이 사례의 핵심은 낮아진 점수 계산과 neighbor 선택 기준을 분리하는 것입니다.
2. **직접 lDDT 계산에는 비교할 reference structure가 필요하지만, pLDDT inference에는 그 target의 reference structure를 입력하지 않습니다.** AlphaFold2 training에서는 예측 coordinates와 training용 reference coordinates로 per-residue lDDT-Cα target을 계산하고 어느 score bin에 해당하는지 confidence head를 training시킵니다. 실제 inference에서는 model internal representation을 받아 이 score bin의 distribution을 예측합니다. 따라서 pLDDT는 reference structure 없이 출력할 수 있지만 실제 오차를 측정한 검증 결과는 아닙니다. `p`는 predicted이며 per-residue lDDT-Cα의 예측이라는 연결을 강조합니다. 여기서 설명한 50개 bin·confidence head는 AF2 구현에 관한 설명입니다.
3. **두 해석 모두 맞지 않습니다.** pLDDT 90은 model이 residue의 local lDDT-Cα를 높게 예상한다는 뜻입니다. discretization한 score bin에 대한 확률은 계산에 사용되지만, 최종 0–100 값 자체가 “이 coordinates가 참일 확률”은 아닙니다. conformational state의 population·binding 확률·free energy·motion rate도 아닙니다. 높은 값만으로 domain 사이 배치까지 확정하지 않으며 PAE와 독립 근거를 함께 봅니다.
4. `100 × (0.10 × 0.49 + 0.20 × 0.69 + 0.70 × 0.89) = 100 × (0.049 + 0.138 + 0.623) =` **81**입니다. 가장 확률이 큰 구간의 중심만 쓰면 89가 되므로 다른 값입니다. 실제 AF2는 0–1 범위의 **50개 bin center 전체**에 softmax probability를 가중해 합하고 100을 곱합니다. 0.49·0.69·0.89는 그 50개 중 세 중심이며 구간을 세 개로 다시 정의한 것이 아닙니다. 표는 나머지 매우 작은 확률을 무시하고 제시한 확률을 합 1로 둔 교육용 근사입니다. 실제 계산에서는 생략하지 않습니다.

교사용 한 문장: **lDDT는 reference structure와 비교해서 계산한 점수이고, pLDDT는 그 per-residue local accuracy 점수를 model이 미리 추정한 값입니다.**

## 6쪽 · pLDDT와 PAE를 나누어 읽기

domain 개념을 12개 위치로 축약한 가상 예제입니다. 5 residue짜리 실제 domain이 있다는 뜻이 아닙니다. 숫자는 실제 model에서 얻지 않았으며, 2·4쪽의 12열 A3M과도 별개입니다. A는 1–5번, linker는 6–7번, B는 8–12번입니다.

1. **Linker의 6·7번을 특히 조심해서 해석합니다.** pLDDT는 각각 43·39로 다른 구간보다 낮습니다. A/B는 각각 평균 91.2이고 linker 평균은 41.0입니다. 전체 평균 82.8만 읽으면 이 local적인 약점을 놓칠 수 있습니다. pLDDT는 model이 예측한 local structural accuracy의 척도이며, 90이 곧 “정확할 확률 90%”이거나 atom 오차가 10%라는 뜻은 아닙니다. 실제 structure와 대조해 측정한 값도 아닙니다. 낮은 pLDDT는 disorder나 여러 배치 가능성과 관련될 수 있지만, 불충분한 정보·어려운 structure prediction에서도 생깁니다. 이 수치 하나로 disorder 상태·fast motion·dynamic timescale를 확정하지 않습니다. 그런 주장은 별도의 structure·spectroscopy·dynamics 근거로 확인해야 합니다.
2. **PAE(A3, B9)=18 Å, PAE(B9, A3)=24 Å**입니다. 이 활동지의 행은 평가 대상 i, 열은 alignment anchor j입니다. 첫 값은 B9의 local coordinate frame을 기준으로 alignment했을 때 A3 위치에 대해 model이 예상하는 오차이고, 두 번째는 A3의 local coordinate frame을 기준으로 했을 때 B9의 예상 오차입니다. 한 점만 맞추어 회전 방향까지 정한다는 뜻이 아니라 해당 위치의 local coordinate frame을 기준으로 생각합니다. 기준이 달라지므로 두 방향의 PAE는 같을 필요가 없습니다. 18 Å는 A3–B9의 물리적 거리·contact 거리도, 실험으로 확인한 실제 오차도 아닙니다. 파일을 시각화한 도구가 축을 바꾸거나 전치했을 수 있으므로 실제 그림에서는 축과 범례를 먼저 확인합니다.
3. **모순이 아닙니다.** 표에 제시한 A 내부 위치쌍의 PAE는 1 Å, B 내부는 2 Å로 작습니다. 두 구간 사이에는 18–24 Å의 큰 값이 있습니다. 구간 내부의 local structure에는 자신이 있으면서도 두 구간의 relative placement에는 자신이 없을 수 있습니다. 높은 per-region pLDDT는 domain 간 자세까지 보증하지 않습니다. 표의 숫자는 전체 12×12 행렬 중 네 위치의 부분표이므로, 나머지 위치에 대해서까지 동일한 패턴이라고 단정하지 않습니다. 실제 분석에서는 전체 PAE 행렬에서 내부 블록과 구간 간 블록을 함께 봅니다.
4. **조건 Q에서는 제시한 A–B 위치쌍의 relative placement에 대한 model confidence가 더 높습니다.** pLDDT가 같으므로 제공된 local confidence는 바뀌지 않았고, PAE의 추가 정보로 구간 간 배치를 구별할 수 있습니다. 낮은 PAE는 그 배치가 실제라는 실험적 증명이나 두 molecule의 binding 검증이 아닙니다. 이 예제는 한 사슬 안의 구간 비교이기도 합니다. binding affinity·에너지·특정 conformational state의 존재 확률·equilibrium population·transition rate를 수치에서 읽어서는 안 됩니다. 올바른 target·complex 조성·model 조건, structure의 물리적 타당성과 독립 실험 근거를 함께 확인합니다. Q의 PAE 범위도 표에 제공한 네 위치에 대한 조건입니다.

교사용 한 문장: **pLDDT는 “이 위치 주변의 모양에 얼마나 자신이 있는가”, PAE는 “다른 위치를 기준으로 보아도 이 위치의 배치에 자신이 있는가”를 묻습니다. 둘 다 예측 confidence이며, 상태의 물리적 존재나 population을 직접 측정한 값은 아닙니다.**

## 7쪽 · 가상 결과 해석

1. F1/F2/A1은 거리가 약 8 Å인 후보, S1/B1/M1은 약 16 Å인 후보 묶음으로 우선 정리할 수 있습니다. 하나의 거리만으로 conformational state를 확정할 수는 없습니다. S2/M2는 낮은 평균 pLDDT와 높은 구간 간 PAE 때문에 불확실한 model일 가능성을 먼저 확인합니다. PAE는 실제 측정 오차가 아닌 model의 예측값입니다.
2. 최고 평균 pLDDT 하나만 선택하면 다른 structure 후보를 버릴 수 있습니다. local confidence, 전체 PAE, domain 배치, contact, 물리적 충돌, 다른 seed의 reproducibility과 독립 실험 근거를 확인합니다.
3. 3/8은 이 가상 생성물 집합에서의 비율입니다. equilibrium population이라고 해석할 근거가 없습니다. 입력 선택과 model 샘플링 distribution이 물리적 equilibrium distribution에 대응하는지 별도 검증해야 합니다. 실험 structure, NMR/FRET/SAXS 등의 제약 또는 검증된 물리적 model과 비교할 수 있습니다.

숫자·짧은 sequence는 모두 가상 training 자료입니다. 실제 inference 또는 실험 결과로 인용하지 않습니다.
