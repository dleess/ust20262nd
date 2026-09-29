"""One-off editorial revision; source keys, IDs, sequences, and URLs are unchanged."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
TERMS={
'가장 최근 공통 조상':'most recent common ancestor (MRCA)','가장 최근 공통조상':'most recent common ancestor (MRCA)',
'공통 조상':'common ancestor','공통조상':'common ancestor',
'유전자·종 계통수':'gene tree·species tree','유전자 계통수':'gene tree','종 계통수':'species tree',
'유전자 가족':'gene family','유전자 이력':'gene history','유전자 역사':'gene history','유전자 소실':'gene loss','유전자 중복':'gene duplication',
'종 분화':'speciation','종분화':'speciation','계통적 비독립성':'phylogenetic non-independence','계통 효과':'phylogenetic effects','계통 영향':'phylogenetic effects','계통수':'phylogenetic tree',
'진화적 관련성':'evolutionary relatedness','진화적 관계':'evolutionary relationship','진화 관계':'evolutionary relationship','진화 이력':'evolutionary history','진화 역사':'evolutionary history','진화 정보':'evolutionary information','진화적 제약':'evolutionary constraint','진화 신호':'evolutionary signal',
'서열 동일성':'sequence identity','서열 유사도':'sequence similarity','서열 유사성':'sequence similarity','상동 서열':'homologous sequence','상동서열':'homologous sequence','상동성':'homology','상동 계열':'homologous family',
'다중서열정렬':'multiple sequence alignment','다중 서열 정렬':'multiple sequence alignment','서열 정렬':'sequence alignment',
'계통 다양성':'phylogenetic diversity','서열 재가중':'sequence reweighting','유효 서열 수':'effective sequence number','서열 다양성':'sequence diversity','유전자 계열':'gene lineage','하위 계열':'subfamily','하위군':'subfamily',
'보상적 치환':'compensatory substitution','보상 치환':'compensatory substitution','보상 변화':'compensatory change','보상적 변화':'compensatory change','보상 돌연변이':'compensatory mutation','보상적 제약':'compensatory constraint',
'공진화':'coevolution','공변화':'covariation','공변이':'covariation','보존도':'conservation',
'주변 빈도':'marginal frequency','공동 빈도':'joint frequency','공동 분포':'joint distribution','통계적 의존성':'statistical dependence','통계적 연관':'statistical association','간접 상관':'indirect correlation','간접 연관':'indirect association','직접 결합':'direct coupling',
'국소 구조 정확도':'local structural accuracy','국소 정확도':'local accuracy','국소 구조 신뢰도':'local structural confidence','국소 신뢰도':'local confidence','구조 신뢰도':'structural confidence','예측 신뢰도':'prediction confidence','예측 정확도':'prediction accuracy','정렬 신뢰도':'alignment reliability',
'학습 정답':'training target','학습용 기준 구조':'training reference structure','신뢰도 head':'confidence head','내부 표현':'internal representation',
'기준 구조':'reference structure','기준 좌표':'reference coordinates','예측 구조':'predicted structure','구조 예측':'structure prediction','구조예측':'structure prediction','단백질 구조':'protein structure','구조 정보':'structural information','구조정보':'structural information','구조 상태':'conformational state','구조 안정성':'structural stability','전체 구조 중첩':'global superposition','회전·병진':'rotation·translation',
'절대 거리 오차':'absolute distance error','절대 오차':'absolute error','예상 위치 오차':'expected positional error','예측 거리':'predicted distance','기준 거리':'reference distance','이웃 선택 반경':'inclusion radius','허용 오차':'error tolerance','허용치':'tolerance','임계값':'threshold',
'정렬 기준 위치':'alignment anchor','정렬 기준 j':'alignment anchor j','국소 좌표틀':'local coordinate frame','국소 좌표계':'local coordinate frame','상대 배치':'relative placement','상대 방향':'relative orientation',
'점수 구간':'score bin','구간 중심':'bin center','확률가중 평균':'probability-weighted mean','확률 가중 평균':'probability-weighted mean','가중평균':'weighted mean','가중 평균':'weighted mean','기대값':'expected value','확률 분포':'probability distribution','평형분포':'equilibrium distribution','평형 분포':'equilibrium distribution','분포':'distribution',
'평형 점유율':'equilibrium population','평형점유율':'equilibrium population','상태 점유율':'state population','점유율':'population','전환 속도':'transition rate','전이 속도':'transition rate','운동 시간척도':'dynamic timescale','운동 시간 척도':'dynamic timescale','운동 속도':'motion rate','빠른 운동':'fast motion',
'결합 친화도':'binding affinity','자유에너지':'free energy','열역학적':'thermodynamic','열역학':'thermodynamics','동역학':'dynamics','분광학':'spectroscopy','무질서':'disorder','유연성':'flexibility','연결부':'linker','중간 상태':'intermediate state',
'상호작용 상대':'interaction partner','결합 상대':'binding partner','상호작용':'interaction','측쇄':'side chain','전하':'charge','직접 접촉':'direct contact','접촉':'contact','복합체':'complex','단량체':'monomer','리간드':'ligand','칼슘':'calcium',
'아미노산':'amino acid','잔기별':'per-residue','잔기 번호':'residue number','잔기번호':'residue number','잔기':'residue','원자':'atom','도메인':'domain','단백질':'protein','유전자':'gene','서열':'sequence','좌표':'coordinates',
'종 이름':'species 이름','같은 종':'같은 species','다른 종':'다른 species','종들의':'species들의','각 종':'각 species','네 종':'네 species','종·균주':'species·strain','종 정보':'species 정보','종 간':'between-species','종 사이':'species 사이','종 안':'species 안','종 안의':'within-species',
'줄기':'lineage','계통':'lineage','조상':'ancestor','하위군':'subfamily','계열':'lineage','기질':'substrate','발현':'expression','촉매 작용':'catalysis','활성':'activity',
'표본 추출':'sampling','무작위 표본':'random sample','표집':'sampling','표본':'sample','대조군':'control','재현성':'reproducibility','중복도':'redundancy','엔트로피':'entropy','재가중':'reweighting','가중치':'weight','표적':'target','마스킹':'masking','클러스터링':'clustering','클러스터':'cluster',
'보존된':'conserved','보존적':'conserved','삽입':'insertion','결실':'deletion','치환':'substitution','변이':'variation','소실':'loss','정렬':'alignment','신뢰도':'confidence','정확도':'accuracy','추론':'inference','학습':'training'
}
# Phrases whose Korean word has different meanings in sequence editing and evolution.
PRE={
'보존(conservation)':'conservation','보존은 구조':'conservation은 구조','보존은 protein':'conservation은 protein',
'보존·공변화':'conservation·covariation','보존·공변이':'conservation·covariation','보존·공진화':'conservation·coevolution',
'보존·빈도':'conservation·frequency','보존된':'conserved',
'단일 열의 보존':'한 열의 conservation','위치의 보존':'위치의 conservation',
'삽입과 결실':'insertion과 deletion',
'종·유전자 계통수':'species tree·gene tree','유전자·종 계통':'gene phylogeny·species phylogeny',
'열림/닫힘 상태':'open/closed state','열린 상태':'open state','닫힌 상태':'closed state',
'유전자 중복(Duplication, D)':'gene duplication (D)','종 분화(Speciation, S)':'speciation (S)',
'공변화(covariation)':'covariation','공변이(covariation)':'covariation','상동성(homology)':'homology','보존도(conservation)':'conservation',
'학습용':'training용','교육용 학습':'교육용','허구 학습 자료':'허구 실습 자료',
'이산화':'discretization','softmax 확률':'softmax probability'
}

def edit_text(text, gene_context=False):
    for old,new in sorted(PRE.items(),key=lambda item:-len(item[0])):text=text.replace(old,new)
    text=text.replace('중복', 'gene duplication' if gene_context else 'redundancy')
    for old,new in sorted(TERMS.items(),key=lambda item:-len(item[0])):text=text.replace(old,new)
    # Avoid duplicated bilingual labels after replacing their Korean half.
    text=re.sub(r'\b([A-Za-z][A-Za-z -]*)\(\1\)',r'\1',text,flags=re.I)
    text=text.replace('유전자','gene').replace('gene gene duplication','gene duplication')
    # Keep Korean particles natural for the terms most frequently used in prose.
    vowel=['sequence','structure','residue','confidence','identity','similarity','homology','orthology','phylogeny','alignment','inference','coverage','MSA','PAE','pLDDT','lDDT','accuracy','lineage','gene tree','species tree']
    for word in sorted(vowel,key=len,reverse=True):
        for before,after in [('으로','로'),('이라는','라는'),('이라고','라고'),('을','를'),('은','는'),('과','와')]:
            text=re.sub(r'(?<![A-Za-z])('+re.escape(word)+')'+before,r'\1'+after,text,flags=re.I)
    text=re.sub(r'(\d)(residue|protein|sequence)',r'\1 \2',text)
    return text

def walk(value,gene_context=False):
    if isinstance(value,str):return edit_text(value,gene_context)
    if isinstance(value,list):return [walk(v,gene_context) for v in value]
    if isinstance(value,dict):return {k:walk(v,gene_context) for k,v in value.items()}
    return value

files=['evolution_msa.json','coevolution.json','confidence.json','alternative_methods.json','core_workflow.json']
for name in files:
    p=R/'content'/name;ss=json.loads(p.read_text())
    for i,s in enumerate(ss):
        if s['id']==12:
            s['notes']='화면의 두 H/M gene tree를 비교합니다. 상황 A에서 H_A–M_A는 S에서 만나 ortholog, H_A–H_B와 H_A–M_B는 D에서 만나 paralog입니다. 상황 B에서 H1–H2는 paralog이고, H1/H2는 각각 M에 대해 ortholog이며 M 기준 co-orthologs입니다. 가장 비슷한 sequence라는 정보만으로 분기 사건을 확정할 수 없으며 gene tree·species tree와 duplication·speciation·loss 이력이 필요합니다. 바로 다음 두 정답 화면에서 근거를 확인합니다.'
        if s['id']==98:s['notes']=s['notes'].replace('8개 중 4개 행을 발췌했다.','8개 후보 전체를 제시했다.')
        ss[i]=walk(s,5<=s['id']<=16 or 34<=s['id']<=37)
    p.write_text(json.dumps(ss,ensure_ascii=False,indent=2)+'\n')
# Teaching prose and printable worksheet text; identifiers and sequence data remain intact.
paths=[R/'README.md',R/'content/worksheet_answers.md']+list((R/'examples').glob('*.md'))+list((R/'practice').glob('*.md'))
for p in paths:
    paragraphs=p.read_text().split('\n')
    p.write_text('\n'.join(edit_text(line,any(w in line for w in ['종분화','종 분화','중복(D)','중복·소실','유전자 중복'])) for line in paragraphs))
for name in ['build_deck.py','build_worksheet.py','verify_materials.py']:
    p=R/'build'/name
    p.write_text('\n'.join(edit_text(line,any(w in line for w in ['종분화','종 분화','중복(D)'])) for line in p.read_text().split('\n')))
# The descriptions are teaching prose; all numeric fixtures and technical keys stay unchanged.
p=R/'practice/synthetic_comparison.json';p.write_text(json.dumps(walk(json.loads(p.read_text())),ensure_ascii=False,indent=2)+'\n')
print('English terminology applied to lecture sources, worksheet builder, and teaching guides')
