"""Context-aware corrections after replacing terminology; no scientific data changes."""
from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
fixes={
'공evolutionary signal':'coevolution signal','공evolutionary information':'coevolution information',
'gene phylogeny·species phylogeny수':'gene tree·species tree',
'most recent common ancestor (MRCA)':'MRCA',
'Conservation\n보존':'Conservation','Covariation\ncovariation':'Covariation','Coevolution\ncoevolution':'Coevolution',
'marginal frequency marginal frequency':'marginal frequency',
'기능 분화':'functional divergence','기능적 제약':'functional constraint','구조·기능 제약':'structural·functional constraint',
'구조를 겹':'structure를 겹','구조를':'structure를','구조가':'structure가','구조와':'structure와','구조의':'structure의','구조는':'structure는','구조도':'structure도','구조에':'structure에','구조 ' : 'structure ', '구조·':'structure·','구조/':'structure/',
'진화 순서':'evolution 순서','진화적':'evolutionary','진화':'evolution','기능':'function',
'결합 파트너':'binding partner','간접적인 결합':'indirect coupling','결합 분석':'coupling analysis','결합':'binding',
'구조':'structure','상동 ':'homologous ','중복':'redundancy','가중치':'weight','이웃':'neighbor','임계값':'threshold',
'상보적 조합':'compatible pair','비상보적 조합':'incompatible pair','관찰 분포':'observed distribution',
'작동 기전':'mechanism','표본':'sample','모형':'model','모델':'model','구간별':'per-region','도메인':'domain',
'표준 아미노산':'standard amino acid','동일성':'identity','유사도':'similarity','유사성':'similarity',
'훈련':'training','재가중':'reweighting','유효 다양성':'effective diversity','다양성':'diversity'
}
# Fix whole phrases before component nouns to avoid remnants such as phylogeny수.
fixes['네 speciation']='네 species로 분화'

def edit(t):
    for a,b in sorted(fixes.items(),key=lambda p:-len(p[0])):t=t.replace(a,b)
    vowel=['sequence','structure','residue','confidence','identity','similarity','homology','orthology','phylogeny','alignment','inference','coverage','MSA','PAE','pLDDT','lDDT','accuracy','lineage','diversity','probability','gene tree','species tree','charge']
    consonant=['coevolution','conservation','covariation','speciation','duplication','distribution','population','information','protein','gene','domain','training','contact','weight','target','alignment anchor','model','function','reference','signal','constraint','substitution','insertion','deletion','prediction','subfamily','complex','monomer','binding','motion','coupling','entropy']
    # subfamily, entropy, complex are vowel-ending in the Korean readings used here.
    for w in ['subfamily','entropy','complex','reference']:
        consonant.remove(w);vowel.append(w)
    for words,pairs in [(vowel,[('으로','로'),('이라는','라는'),('이라고','라고'),('을','를'),('은','는'),('과','와')]),(consonant,[('를','을'),('는','은'),('와','과')])]:
        for word in sorted(words,key=len,reverse=True):
            for a,b in pairs:t=re.sub(r'(?<![A-Za-z])('+re.escape(word)+')'+a,r'\1'+b,t,flags=re.I)
            a,b=('이','가') if words is vowel else ('가','이')
            t=re.sub(r'(?<![A-Za-z])('+re.escape(word)+')'+a+r'(?=[\s,.:;!?]|$)',r'\1'+b,t,flags=re.I)
    return t

def walk(v):
    if isinstance(v,str):return edit(v)
    if isinstance(v,list):return [walk(x) for x in v]
    if isinstance(v,dict):return {k:walk(x) for k,x in v.items()}
    return v
files=['evolution_msa.json','coevolution.json','confidence.json','alternative_methods.json','core_workflow.json']
for name in files:
    p=R/'content'/name;ss=walk(json.loads(p.read_text()))
    for s in ss:
        if s['id']==6:s['body'][0]='MRCA (most recent common ancestor): 두 gene이 처음 만나는 ancestor'
        if s['id']==12:s['title']='활동지 1 · Gene tree에서 ortholog·paralog 판정'
        if s['id']==57:s['title']='정답·해설 · Reference structure와 pLDDT 계산'
        if s['id']==27:
            s['body'][1]='Conserved 위치는 structural·functional constraint의 후보이며 원인은 추가 확인'
            s['notes']=s['notes'].replace('보존은','conservation은')
        if s['id'] in [51,53]:
            s['worksheet']['table']['headers']=['Pair','Ref.\nÅ','Pred.\nÅ','Abs.\nerror Å','Pass\n/ 4']
            s['worksheet']['caption']='Ref.=reference distance, Pred.=predicted distance. 가상 Cα pairs이며 reference distance는 모두 15 Å 미만입니다.'
        if s['id']==4:
            s['diagram']['inference']='Trained model:\n위치 관계 inference'
            s['diagram']['left_caption']='호환되는 residue 조합이\nhomologous sequences에 남을 수 있음'
            s['diagram']['right_title']='Structure · 근접 후보'
    p.write_text(json.dumps(ss,ensure_ascii=False,indent=2)+'\n')
for p in [R/'README.md',R/'content/worksheet_answers.md']+list((R/'examples').glob('*.md'))+list((R/'practice').glob('*.md')):
    p.write_text(edit(p.read_text()))
for name in ['build_deck.py','build_worksheet.py','verify_materials.py']:
    p=R/'build'/name;p.write_text(edit(p.read_text()))
p=R/'practice/synthetic_comparison.json';p.write_text(json.dumps(walk(json.loads(p.read_text())),ensure_ascii=False,indent=2)+'\n')
print('Context, grammar, and heading corrections applied')
