"""Seven printable A4 student activity pages. Answers are in instructor notes."""
from pathlib import Path
from datetime import datetime
import json
import shutil
import pymupdf as fitz

ROOT=Path(__file__).resolve().parents[1]
FONT='/Library/Fonts/Arial Unicode.ttf'
MONO='/System/Library/Fonts/Supplemental/Courier New.ttf'
INK=(.09,.17,.21)
TEAL=(.12,.40,.44)
doc=fitz.open()

def text(p,value,x,y,w,h,size=11,mono=False,col=INK):
    room=p.insert_textbox(fitz.Rect(x,y,x+w,y+h),value,fontname='Mono' if mono else 'Korean',fontsize=size,lineheight=1.22,color=col)
    assert room>=0,(p.number,value[:80],room)

def page(title,number):
    p=doc.new_page(width=595.28,height=841.89)
    p.insert_font(fontname='Korean',fontfile=FONT)
    p.insert_font(fontname='Mono',fontfile=MONO)
    text(p,'MSA와 protein structure 예측 · 학생 활동지',38,28,520,35,20)
    text(p,title,38,73,520,25,14,col=TEAL)
    text(p,'이름: ____________________   조: __________   날짜: ______________',38,108,520,22,10)
    text(p,'교육용 가상 자료입니다. 답은 근거와 함께 적으세요.',38,788,520,19,9)
    text(p,str(number),548,812,20,15,9)
    return p

def answer(p,y,n=2):
    for i in range(n):
        p.draw_line((39,y+i*28),(555,y+i*28),color=(.75,.79,.79),width=.5)

p=page('1. evolution 설명 직후 · speciation과 gene duplication',1)
text(p,'상황 A: gene duplication(D)이 speciation(S)보다 먼저 일어났습니다.',38,150,520,30,12)
text(p,'          ancestor\n             D\n        /         \\\n       A           B\n       S           S\n     /   \\       /   \\\n   H_A   M_A   H_B   M_B',60,194,470,153,14,True)
text(p,'H = 사람 lineage, M = 생쥐 lineage. 가지 길이는 시간·similarity를 나타내지 않습니다.',38,356,520,30,10)
text(p,'1. H_A–M_A, H_A–H_B, H_A–M_B의 관계를 분류하고 판단한 사건을 쓰세요.',38,399,520,37,11)
answer(p,455,2)
text(p,'상황 B: 먼저 H와 M으로 speciation했고, H의 gene만 H1·H2로 gene duplication되었습니다.',38,518,520,40,11)
text(p,'2. H1–H2, H1–M, H2–M의 관계를 쓰세요. M에 대한 H1·H2의 관계도 설명하세요.',38,566,520,40,11)
answer(p,623,2)
text(p,'3. “sequence가 가장 비슷한 두 gene은 반드시 ortholog다.”에 빠진 정보는 무엇인가요?',38,693,520,40,11)
answer(p,756,1)

p=page('2. MSA 설명 직후 · A3M 읽기',2)
text(p,'아래는 12개 alignment 열을 가진 가상 자료입니다. 실제 예측용 protein이 아닙니다.',38,150,520,35,11)
text(p,'>query\nACDEFGHIKLMN\n>example_A1 group=A\nACDEFGHIKLMN\n>example_A2 group=A\nACDeeEFGHIKLMN\n>example_A3 group=A\nACDE-GHIKLMN\n>example_B1 group=B\nACDEYGHIKLXN\n>example_B2 group=B\nACDttEYGHIKL-N\n>example_B3 group=B\nAC-EYGHIKLXN',50,192,490,257,12,True)
text(p,'1. Query 포함 행 수: ______  Homolog 행 수: ______  alignment 열 수: ______',38,465,520,29,11)
text(p,'2. A2의 ee는 몇 번째 alignment 열 직전에 있나요? 소문자를 대문자로 바꾸면 왜 안 되나요?',38,509,520,38,11)
answer(p,562,1)
text(p,'3. A3의 gap과 B1의 X가 있는 alignment 열 번호와 각각의 의미를 쓰세요.',38,594,520,33,11)
answer(p,645,1)
text(p,'4. 같은 행을 여러 번 복제해 depth를 키우면 독립적인 evolutionary information이 늘어나나요?',38,680,520,35,11)
answer(p,743,1)

p=page('3. Coevolution 설명 직후 · evolutionary relationship와 두 열의 패턴',3)
text(p,'가상 자료: A/B gene duplication 후 H·M·R·F 네 species로 분화했습니다. 각 species에 A와 B가\n하나씩 있습니다. i와 j는 같은 protein 안의 두 alignment 위치입니다.',38,146,520,43,11)
text(p,'자료: 두 paralog subfamily를 합친 8행',38,201,283,24,11,col=TEAL)
left_rows=[['gene','i','j']]+[[f'{family}_{species}',a,b] for family,a,b in [('A','D','K'),('B','K','D')] for species in ['H','M','R','F']]
for row_index,row in enumerate(left_rows):
    y=234+row_index*18
    for value,x,w in zip(row,[38,167,226],[129,59,59]):
        text(p,value,x+4,y,w-8,18,10,col=TEAL if row_index==0 else INK)
    p.draw_line((38,y+17),(285,y+17),color=(.78,.82,.82),width=.4)
text(p,'대조 자료: 다른 가상 8행',327,201,225,24,11,col=TEAL)
for row_index,row in enumerate([['i, j','행 수'],['D, D','2'],['D, K','2'],['K, D','2'],['K, K','2']]):
    y=234+row_index*25
    for value,x,w in zip(row,[327,463],[136,89]):
        text(p,value,x+4,y,w-8,23,10,col=TEAL if row_index==0 else INK)
    p.draw_line((327,y+23),(552,y+23),color=(.78,.82,.82),width=.4)
text(p,'D = Asp, K = Lys\n한 행은 한 gene의 두 위치입니다.\n두 표 모두 실제 관측값이 아닙니다.',327,367,225,47,9)
text(p,'1. 왼쪽 자료: P(D_i) = ____  P(K_j) = ____  실제 P(D_i, K_j) = ____\n   독립이라면 P(D_i) × P(K_j) = ____. 대조 자료와 무엇이 다른가요?',38,431,520,46,11)
answer(p,491,1)
text(p,'2. A_H–A_M, A_H–B_M의 evolutionary relationship는? A/B를 따로 보면 variation가 남나요?',38,521,520,33,11)
answer(p,568,1)
text(p,'3. 왼쪽의 8행은 “독립적인 compensatory change 8번” 또는 “direct contact”의 증거인가요?\n   패턴이 common ancestor로부터 함께 내려왔을 가능성을 설명하세요.',38,599,520,46,11)
answer(p,659,1)
text(p,'4. Ortholog만 모으면 phylogenetic effects가 사라질까요? 더 필요한 근거를 써 보세요.',38,691,520,32,11)
answer(p,744,1)

p=page('4. Depth → clustering → masking · 설명마다 한 항목씩',4)
text(p,'컴퓨터: AIprediction/practice/에서 생성 후, 설명한 조건의 파일을 차례로 봅니다.',38,150,520,28,11)
text(p,'sh run_practice.sh\n# custom run\npython3 msa_lab.py --depth 4 --seed 7 \\\n  --out runs/student01',46,188,503,87,12,True)
text(p,'컴퓨터 없이: query와 A2, A3, B1을 선택했다고 가정합니다.\n여기 A/B는 임의 라벨이며, 3쪽의 evolutionary history가 주어진 subfamily와 별개입니다.',38,290,520,37,10)
text(p,'1. Depth 설명 직후: subsample.a3m의 첫 행은 무엇이며, 유지하는 이유는?',38,341,520,35,11)
answer(p,393,1)
text(p,'2. Clustering 설명 직후: group_A/B.a3m의 사전 라벨 분리와 AF-Cluster의 차이는?',38,429,520,35,11)
answer(p,480,1)
text(p,'3. Masking 설명 직후: homolog의 5·7·10열을 X로 가린 A2를 쓰고\n   masked.a3m과 비교하세요. Query·소문자 ee·기존 gap은 어떻게 하나요?',38,514,520,52,11)
answer(p,589,2)
text(p,'4. MSA 조건을 비교할 때 고정하거나 기록할 항목 세 가지 이상을 쓰세요.',38,655,520,35,11)
answer(p,707,2)

p=page('5. lDDT 계산 → pLDDT 예측',5)
text(p,'가상 lDDT-Cα 예제: 중심 residue i의 neighbor a·b·c·d 네 쌍만 평가합니다.\nreference structure에서 15 Å 미만인 쌍을 선택하며, coordinates가 모두 있다고 가정합니다.',38,145,520,43,10.5)
text(p,'각 쌍의 absolute distance error를 구하고 0.5·1·2·4 Å보다 작은지 각각 셉니다.\n이 예제의 lDDT_i = 네 쌍의 통과 횟수 합 / (4쌍 × 4기준).\n표는 설명과 함께 채우고, 1번만 1분 핵심 실습으로 풉니다. 2–4번은 확장용입니다.',38,194,520,57,10)
lddt_rows=[['neighbor','reference distance (Å)','predicted distance (Å)','absolute error (Å)','통과 횟수 / 4'],['a','4','4.2','______','______'],['b','7','7.8','______','______'],['c','10','11.5','______','______'],['d','14','17','______','______']]
for row_index,row in enumerate(lddt_rows):
    y=262+row_index*24
    for value,x,w in zip(row,[38,100,213,327,441],[62,113,114,114,114]):
        text(p,value,x+4,y,w-8,23,9.7,col=TEAL if row_index==0 else INK)
    p.draw_line((38,y+23),(555,y+23),color=(.78,.82,.82),width=.4)
text(p,'표의 lDDT_i = ____ / 16 = ______ (0–1). 100점 척도로 표시하면 ______.',38,395,520,28,10.5)
text(p,'1. [1분] d의 predicted distance만 17 → 19 Å로 바꿉니다. d는 neighbor 계산에 [포함 / 제외].\n   새 lDDT_i는 [9/16 또는 9/12]이며, 100점 척도에서는 ______입니다.',38,439,520,43,10.5)
answer(p,497,1)
text(p,'2. [확장] lDDT를 직접 계산할 때와 pLDDT를 inference할 때,\n   비교할 reference structure가 필요한 쪽은 무엇인가요?',38,518,520,39,10.5)
answer(p,573,1)
text(p,'3. [확장] pLDDT 90을 “coordinates가 정확할 확률 90%” 또는\n   “이 conformational state의 population 90%”로 해석해도 될까요?',38,594,520,40,10.5)
answer(p,647,1)
text(p,'4. [확장] AF2의 50개 구간 중 3개 중심만 보인 교육용 근사입니다.\n   중심 c: 0.49, 0.69, 0.89 / 확률 p: 0.10, 0.20, 0.70\n   나머지 매우 작은 확률은 생략했습니다. 100 × Σ(p × c) = ______.\n   가장 확률이 큰 한 구간의 중심만 사용한 값과 같은가요?',38,667,520,74,10.5)
answer(p,757,1)

p=page('6. pLDDT → PAE · 설명 직후 나누어 읽기',6)
text(p,'domain 개념을 12개 위치로 축약한 가상 예제입니다. 실제 protein·inference 결과가\n아니며 앞의 12열 A3M과 별개입니다. A: 1–5, linker: 6–7, B: 8–12.',38,146,520,43,10)
plddt_rows=[['구간','residue 위치','각 residue의 pLDDT (0–100)'],['A','1–5','94, 93, 91, 90, 88'],['linker','6–7','43, 39'],['B','8–12','86, 92, 94, 93, 91']]
for row_index,row in enumerate(plddt_rows):
    y=197+row_index*19
    for value,x,w in zip(row,[38,127,239],[89,112,316]):
        text(p,value,x+4,y,w-8,18,10,col=TEAL if row_index==0 else INK)
    p.draw_line((38,y+18),(555,y+18),color=(.78,.82,.82),width=.4)
text(p,'1. pLDDT 설명 직후: 어느 구간의 coordinates를 특히 조심해서 해석해야 하나요?\n   이 값만으로 그 구간이 disorder하거나 빠르게 움직인다고 확정할 수 있나요?',38,282,520,39,10.5)
answer(p,336,1)
text(p,'조건 P의 PAE (Å): 전체 12×12 중 3·4·9·10번 위치만 뽑은 4×4 표입니다.\n행 i = 오차를 평가할 위치, 열 j = alignment anchor. 다음은 PAE 설명 뒤 풉니다.',38,355,520,42,10)
pae_rows=[['i / j','A3','A4','B9','B10'],['A3','0','1','18','20'],['A4','1','0','19','21'],['B9','24','23','0','2'],['B10','22','24','2','0']]
for row_index,row in enumerate(pae_rows):
    y=410+row_index*23
    for value,x in zip(row,[38,99,160,221,282]):
        text(p,value,x+4,y,53,22,10,col=TEAL if row_index==0 else INK)
    p.draw_line((38,y+22),(343,y+22),color=(.78,.82,.82),width=.4)
text(p,'A3 = A 구간의 3번 위치\nB9 = B 구간의 9번 위치\n\n수치는 모두 가상입니다.\n표의 방향부터 확인하세요.',365,415,190,99,10)
text(p,'2. PAE(A3, B9) = ____ Å, PAE(B9, A3) = ____ Å.\n   각각 어느 위치를 기준으로 한 예상 오차인가요? residue 사이 거리인가요?',38,542,520,40,10.5)
answer(p,597,1)
text(p,'3. A/B 내부와 A–B 사이 PAE를 비교하세요. 높은 per-region pLDDT와\n   큰 구간 간 PAE가 동시에 나오는 것은 모순인가요?',38,615,520,40,10.5)
answer(p,669,1)
text(p,'4. 조건 Q는 pLDDT가 같고, 위 표의 대각선 밖 PAE가 모두 1–3 Å입니다.\n   무엇에 더 자신이 있나요? binding·특정 상태의 존재나 population도 확정되나요?',38,689,520,43,10.5)
answer(p,754,1)

p=page('7. Confidence를 함께 보기 · 가상 예측 결과 판독',7)
text(p,'가상 180 residue target의 독립 사고 실험입니다. 앞의 A3M에서 계산한 결과가 아닙니다.',38,147,520,37,10)
text(p,'거리 = 40–140번 Cα 거리. PAE = 20–70과 110–160 구간 사이 두 방향 평균.',38,184,520,35,10)
rows=json.loads((ROOT/'practice/synthetic_comparison.json').read_text())['rows']
headers=['ID','조건','pLDDT','거리 (Å)','PAE (Å)']
widths=[42,212,81,91,91]
xvals=[38]
for w in widths[:-1]:xvals.append(xvals[-1]+w)
labels={'full_MSA':'원본 MSA','shallow_MSA':'얕은 MSA','prelabelled_group_A':'사전 라벨 A','prelabelled_group_B':'사전 라벨 B','homolog_X_mask':'Homolog X masking'}
for i,row in enumerate([headers]+[[r['id'],labels[r['condition']],f"{r['mean_plddt']:.0f}",f"{r['distance_A']:.1f}",f"{r['inter_region_pae_A']:.1f}"] for r in rows]):
    y=232+i*27
    for value,x,w in zip(row,xvals,widths):text(p,str(value),x+3,y,w-6,24,10,col=TEAL if i==0 else INK)
    p.draw_line((38,y+25),(555,y+25),color=(.78,.82,.82),width=.4)
text(p,'1. 서로 다른 후보 묶음을 골라 보세요. 큰 거리만 보고 S2/M2를 선택해도 될까요?',38,499,520,38,11)
answer(p,552,1)
text(p,'2. 평균 pLDDT가 가장 높은 structure 하나만 남길 때 무엇을 놓칠 수 있나요?',38,584,520,35,11)
answer(p,634,1)
text(p,'3. 8개 중 3개가 비슷한 거리라면 equilibrium population이 3/8인가요? 추가 근거를 쓰세요.',38,666,520,37,11)
answer(p,722,2)

doc.set_metadata({'title':'MSA와 protein structure 예측 · 학생 활동지','author':'Donghan Lee','subject':'evolutionary relationship, A3M, coevolution, 입력 조작, lDDT와 pLDDT 및 PAE, 가상 결과 해석'})
out=ROOT/'build/msa_structure_prediction_worksheet_ko.pdf'
if out.exists():
    dest=ROOT/'build/archive'/datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    dest.mkdir(parents=True);shutil.copy2(out,dest/out.name)
doc.subset_fonts()
doc.save(out,deflate=True)
assert len(doc)==7
print(out)
