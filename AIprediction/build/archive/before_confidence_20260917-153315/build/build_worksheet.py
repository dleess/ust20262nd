"""Five printable A4 student activity pages. Answers are in instructor notes."""
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
    text(p,'MSA와 단백질 구조 예측 · 학생 활동지',38,28,520,35,20)
    text(p,title,38,73,520,25,14,col=TEAL)
    text(p,'이름: ____________________   조: __________   날짜: ______________',38,108,520,22,10)
    text(p,'교육용 가상 자료입니다. 답은 근거와 함께 적으세요.',38,788,520,19,9)
    text(p,str(number),548,812,20,15,9)
    return p

def answer(p,y,n=2):
    for i in range(n):
        p.draw_line((39,y+i*28),(555,y+i*28),color=(.75,.79,.79),width=.5)

p=page('1. 진화 설명 직후 · 종분화와 유전자 중복',1)
text(p,'상황 A: 유전자 중복(D)이 종분화(S)보다 먼저 일어났습니다.',38,150,520,30,12)
text(p,'          ancestor\n             D\n        /         \\\n       A           B\n       S           S\n     /   \\       /   \\\n   H_A   M_A   H_B   M_B',60,194,470,153,14,True)
text(p,'H = 사람 계통, M = 생쥐 계통. 가지 길이는 시간·유사도를 나타내지 않습니다.',38,356,520,30,10)
text(p,'1. H_A–M_A, H_A–H_B, H_A–M_B의 관계를 분류하고 판단한 사건을 쓰세요.',38,399,520,37,11)
answer(p,455,2)
text(p,'상황 B: 먼저 H와 M으로 종분화했고, H의 유전자만 H1·H2로 중복되었습니다.',38,518,520,40,11)
text(p,'2. H1–H2, H1–M, H2–M의 관계를 쓰세요. M에 대한 H1·H2의 관계도 설명하세요.',38,566,520,40,11)
answer(p,623,2)
text(p,'3. “서열이 가장 비슷한 두 유전자는 반드시 ortholog다.”에 빠진 정보는 무엇인가요?',38,693,520,40,11)
answer(p,756,1)

p=page('2. MSA 설명 직후 · A3M 읽기',2)
text(p,'아래는 12개 정렬 열을 가진 가상 자료입니다. 실제 예측용 단백질이 아닙니다.',38,150,520,35,11)
text(p,'>query\nACDEFGHIKLMN\n>example_A1 group=A\nACDEFGHIKLMN\n>example_A2 group=A\nACDeeEFGHIKLMN\n>example_A3 group=A\nACDE-GHIKLMN\n>example_B1 group=B\nACDEYGHIKLXN\n>example_B2 group=B\nACDttEYGHIKL-N\n>example_B3 group=B\nAC-EYGHIKLXN',50,192,490,257,12,True)
text(p,'1. Query 포함 행 수: ______  Homolog 행 수: ______  정렬 열 수: ______',38,465,520,29,11)
text(p,'2. A2의 ee는 몇 번째 정렬 열 직전에 있나요? 소문자를 대문자로 바꾸면 왜 안 되나요?',38,509,520,38,11)
answer(p,562,1)
text(p,'3. A3의 gap과 B1의 X가 있는 정렬 열 번호와 각각의 의미를 쓰세요.',38,594,520,33,11)
answer(p,645,1)
text(p,'4. 같은 행을 여러 번 복제해 depth를 키우면 독립적인 진화 정보가 늘어나나요?',38,680,520,35,11)
answer(p,743,1)

p=page('3. Coevolution 설명 직후 · 진화 관계와 두 열의 패턴',3)
text(p,'가상 자료: A/B 중복 후 H·M·R·F 네 종으로 분화했습니다. 각 종에 A와 B가\n하나씩 있습니다. i와 j는 같은 단백질 안의 두 정렬 위치입니다.',38,146,520,43,11)
text(p,'자료: 두 paralog 하위군을 합친 8행',38,201,283,24,11,col=TEAL)
left_rows=[['유전자','i','j']]+[[f'{family}_{species}',a,b] for family,a,b in [('A','D','K'),('B','K','D')] for species in ['H','M','R','F']]
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
text(p,'D = Asp, K = Lys\n한 행은 한 유전자의 두 위치입니다.\n두 표 모두 실제 관측값이 아닙니다.',327,367,225,47,9)
text(p,'1. 왼쪽 자료: P(D_i) = ____  P(K_j) = ____  실제 P(D_i, K_j) = ____\n   독립이라면 P(D_i) × P(K_j) = ____. 대조 자료와 무엇이 다른가요?',38,431,520,46,11)
answer(p,491,1)
text(p,'2. A_H–A_M, A_H–B_M의 진화 관계는? A/B를 따로 보면 변이가 남나요?',38,521,520,33,11)
answer(p,568,1)
text(p,'3. 왼쪽의 8행은 “독립적인 보상 변화 8번” 또는 “직접 접촉”의 증거인가요?\n   패턴이 공통 조상으로부터 함께 내려왔을 가능성을 설명하세요.',38,599,520,46,11)
answer(p,659,1)
text(p,'4. Ortholog만 모으면 계통 효과가 사라질까요? 더 필요한 근거를 써 보세요.',38,691,520,32,11)
answer(p,744,1)

p=page('4. Depth → clustering → masking · 설명마다 한 항목씩',4)
text(p,'컴퓨터: AIprediction/practice/에서 생성 후, 설명한 조건의 파일을 차례로 봅니다.',38,150,520,28,11)
text(p,'sh run_practice.sh\n# custom run\npython3 msa_lab.py --depth 4 --seed 7 \\\n  --out runs/student01',46,188,503,87,12,True)
text(p,'컴퓨터 없이: query와 A2, A3, B1을 선택했다고 가정합니다.\n여기 A/B는 임의 라벨이며, 3쪽의 진화 이력이 주어진 하위군과 별개입니다.',38,290,520,37,10)
text(p,'1. Depth 설명 직후: subsample.a3m의 첫 행은 무엇이며, 유지하는 이유는?',38,341,520,35,11)
answer(p,393,1)
text(p,'2. Clustering 설명 직후: group_A/B.a3m의 사전 라벨 분리와 AF-Cluster의 차이는?',38,429,520,35,11)
answer(p,480,1)
text(p,'3. Masking 설명 직후: homolog의 5·7·10열을 X로 가린 A2를 쓰고\n   masked.a3m과 비교하세요. Query·소문자 ee·기존 gap은 어떻게 하나요?',38,514,520,52,11)
answer(p,589,2)
text(p,'4. MSA 조건을 비교할 때 고정하거나 기록할 항목 세 가지 이상을 쓰세요.',38,655,520,35,11)
answer(p,707,2)

p=page('5. Confidence 설명 직후 · 가상 예측 결과 판독',5)
text(p,'가상 180잔기 표적의 독립 사고 실험입니다. 앞의 A3M에서 계산한 결과가 아닙니다.',38,147,520,37,10)
text(p,'거리 = 40–140번 Cα 거리. PAE = 20–70과 110–160 구간 사이 두 방향 평균.',38,184,520,35,10)
rows=json.loads((ROOT/'practice/synthetic_comparison.json').read_text())['rows']
headers=['ID','조건','pLDDT','거리 (Å)','PAE (Å)']
widths=[42,212,81,91,91]
xvals=[38]
for w in widths[:-1]:xvals.append(xvals[-1]+w)
labels={'full_MSA':'원본 MSA','shallow_MSA':'얕은 MSA','prelabelled_group_A':'사전 라벨 A','prelabelled_group_B':'사전 라벨 B','homolog_X_mask':'Homolog X 마스킹'}
for i,row in enumerate([headers]+[[r['id'],labels[r['condition']],f"{r['mean_plddt']:.0f}",f"{r['distance_A']:.1f}",f"{r['inter_region_pae_A']:.1f}"] for r in rows]):
    y=232+i*27
    for value,x,w in zip(row,xvals,widths):text(p,str(value),x+3,y,w-6,24,10,col=TEAL if i==0 else INK)
    p.draw_line((38,y+25),(555,y+25),color=(.78,.82,.82),width=.4)
text(p,'1. 서로 다른 후보 묶음을 골라 보세요. 큰 거리만 보고 S2/M2를 선택해도 될까요?',38,499,520,38,11)
answer(p,552,1)
text(p,'2. 평균 pLDDT가 가장 높은 구조 하나만 남길 때 무엇을 놓칠 수 있나요?',38,584,520,35,11)
answer(p,634,1)
text(p,'3. 8개 중 3개가 비슷한 거리라면 평형 점유율이 3/8인가요? 추가 근거를 쓰세요.',38,666,520,37,11)
answer(p,722,2)

doc.set_metadata({'title':'MSA와 단백질 구조 예측 · 학생 활동지','author':'Donghan Lee','subject':'진화 관계, A3M, coevolution, 입력 조작, 가상 결과 해석'})
out=ROOT/'build/msa_structure_prediction_worksheet_ko.pdf'
if out.exists():
    dest=ROOT/'build/archive'/datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    dest.mkdir(parents=True);shutil.copy2(out,dest/out.name)
doc.subset_fonts()
doc.save(out,deflate=True)
assert len(doc)==5
print(out)
