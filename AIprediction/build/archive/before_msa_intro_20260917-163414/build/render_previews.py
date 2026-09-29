"""Render each exported PDF page and contact sheets into a fresh QA folder."""
from datetime import datetime
from pathlib import Path
import pymupdf as fitz
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'build/previews'/datetime.now().strftime('%Y%m%d-%H%M%S')
out.mkdir(parents=True,exist_ok=False)
doc=fitz.open(ROOT/'build/msa_structure_prediction_3h_ko.pdf')
thumbs=[]
for i,page in enumerate(doc,1):
    pix=page.get_pixmap(matrix=fitz.Matrix(1.5,1.5))
    pix.save(out/f'slide-{i:02d}.png')
    im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
    im.thumbnail((640,360))
    tile=Image.new('RGB',(650,390),'white')
    tile.paste(im,(5,23));ImageDraw.Draw(tile).text((10,5),str(i),fill='black')
    thumbs.append(tile)
for n,start in enumerate(range(0,len(thumbs),6),1):
    sheet=Image.new('RGB',(1950,780),'#d5d9d9')
    for i,tile in enumerate(thumbs[start:start+6]):sheet.paste(tile,((i%3)*650,(i//3)*390))
    sheet.save(out/f'contact-{n:02d}.png')
(ROOT/'build/last_preview_dir.txt').write_text(str(out)+'\n')
print(out)
