"""Two printable A4 activity pages, with embedded Korean text and coordinate images."""
from pathlib import Path
from io import BytesIO
import pymupdf as fitz
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
FONT = '/Library/Fonts/Arial Unicode.ttf'
DOC = fitz.open()
INK = (.09,.17,.21)
TEAL = (.12,.40,.44)

def new_page():
    p = DOC.new_page(width=595.276,height=841.89)
    p.insert_font(fontname='Korean',fontfile=FONT)
    return p

def txt(p, t, x, y, w, h, size=11, color=INK):
    room=p.insert_textbox(fitz.Rect(x,y,x+w,y+h),t,fontname='Korean',fontsize=size,color=color,lineheight=1.3)
    assert room>=0, (t,room)

def line(p,y,x=38,w=519):
    p.draw_line((x,y),(x+w,y),color=(.68,.73,.75),width=.5)

def img(p,name,x,y,w,h):
    im=Image.open(ROOT/'assets/figures'/name).convert('RGB')
    diff=ImageChops.difference(im,Image.new('RGB',im.size,'white')).convert('L')
    b=diff.point(lambda n:255 if n>20 else 0).getbbox()
    if b:
        b=(max(0,b[0]-25),max(0,b[1]-25),min(im.width,b[2]+25),min(im.height,b[3]+25))
        im=im.crop(b)
    data=BytesIO()
    im.save(data,format='PNG')
    p.insert_image(fitz.Rect(x,y,x+w,y+h),stream=data.getvalue(),keep_proportion=True)

p=new_page()
txt(p,'생체분자 구조 읽기 · 활동지',38,30,520,40,22)
txt(p,'이름: ____________________     날짜: ____________________',38,76,520,22,11)
txt(p,'활동 1. 기호와 설명 연결하기',38,117,520,25,14,TEAL)
items=[
    '① 물의 순전하가 0이면 물은 비극성이다.  O / X',
    '② O–H의 실선과 O–H···O의 점선은 같은 종류의 결합이다.  O / X',
    '③ 한 약물 안에 극성 부분과 비극성 부분이 함께 있을 수 있다.  O / X',
]
for i,t in enumerate(items):
    txt(p,t,38,150+i*34,520,26,11)
txt(p,'하나를 골라 판단한 이유를 적으세요.',38,257,520,22,11)
line(p,302)
txt(p,'활동 2. 질문에 맞는 구조 표현 고르기',38,325,520,25,14,TEAL)
for i,(name,label) in enumerate([('2ITY_whole.png','A'),('2ITY_allsticks.png','B'),('2ITY_surface.png','C')]):
    img(p,name,38+i*176,362,164,123)
    txt(p,label,105+i*176,489,30,22,12)
txt(p,'사슬의 접힘: ____     약물의 질소 원자: ____     포켓의 모양: ____',38,526,520,25,11)
txt(p,'선택한 표현 한 가지와 그 이유:',38,560,520,22,11)
line(p,602)
txt(p,'활동 3. 관찰, 가능한 해석, 근거 부족',38,628,520,25,14,TEAL)
for i,t in enumerate([
    '① Leu718의 곁사슬 탄소가 약물 가까이에 있다.  (________________)',
    '② Met793 주사슬이 수소결합에 기여할 수 있다.  (________________)',
    '③ 이 그림만으로 다른 약보다 효과가 크다고 알 수 있다.  (________________)',
]):
    txt(p,t,38,664+i*34,520,27,11)
txt(p,'구두 설명: 내 판단을 뒷받침하는 그림의 특징 하나를 짚어 보세요.',38,773,520,25,10)
txt(p,'그림: PDB 2ITY 원좌표 (rcsb.org/structure/2ITY). 원자 색은 표시 규칙입니다.',38,813,505,14,8)
txt(p,'1',557,813,20,14,8)

p=new_page()
txt(p,'최종 활동 · 새로운 구조 읽기',38,30,520,40,22)
txt(p,'EGFR–erlotinib, PDB 1M17. 가운데 큰 분자가 약물이며 두 작은 잔기에 이름이 붙어 있습니다.',38,78,520,35,10)
img(p,'1M17_whole.png',30,126,170,210)
img(p,'1M17_contacts.png',209,119,350,226)
txt(p,'전체 구조',80,343,110,24,11)
txt(p,'선택한 주변 잔기와 약물',282,343,260,24,11)
txt(p,'도움말',38,389,520,25,13,TEAL)
txt(p,'Leu764: 비극성 곁사슬을 가집니다.\nMet769: 주사슬 N–H는 수소결합 주개가 될 수 있습니다.\n약물의 고리 N은 받개 후보입니다. N은 파랑, O는 빨강이며 수소는 생략되어 있습니다.',38,420,520,68,11)
txt(p,'1. 위 전체 그림에 포켓을 표시하고, 확대 그림의 두 잔기를 각각 찾아 표시하세요.',38,512,520,35,11)
txt(p,'2. 각 잔기의 어느 부분이 어떻게 결합에 기여할 수 있는지 적으세요.',38,560,520,28,11)
txt(p,'Leu764:',38,596,78,23,11)
line(p,634,x=118,w=439)
txt(p,'Met769:',38,646,78,23,11)
line(p,684,x=118,w=439)
txt(p,'3. 이 그림만으로 알 수 없는 사항 하나와 그 이유를 적으세요.',38,709,520,26,11)
line(p,762)
txt(p,'번호는 1M17 파일의 표기입니다. 이름 암기보다 구조에서 찾은 근거를 평가합니다.',38,781,520,20,9)
txt(p,'그림: PDB 1M17 원좌표 (rcsb.org/structure/1M17). 관찰한 사실과 가능한 해석을 구분하세요.',38,813,510,14,8)
txt(p,'2',557,813,20,14,8)

DOC.set_metadata({'title':'생체분자 구조 읽기 · 학생 활동지','author':'Donghan Lee','subject':'종이 또는 구두 응답 활동'})
out=ROOT/'build/biomolecule_view_worksheet_ko.pdf'
DOC.subset_fonts()
DOC.save(out,deflate=True)
print(out)
