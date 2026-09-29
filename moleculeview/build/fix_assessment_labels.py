from pathlib import Path
import json
import pymol
from pymol import cmd
R=Path(__file__).resolve().parents[1]
pymol.finish_launching(['pymol','-cq'])
cmd.load(str(R/'build/1M17_teaching.pse'))
cmd.hide('everything')
cmd.label('all','')
cmd.show('sticks','test and (resn AQ4 or resi 764+769)')
cmd.set_view(json.loads((R/'build/views.json').read_text())['1M17_pocket'])
cmd.set('label_size',32)
cmd.label('test and resi 764 and name CA','"Leu764"')
cmd.label('test and resi 769 and name CA','"Met769"')
cmd.set('label_position',[1.7,1.7,0],'test and resi 764 and name CA')
cmd.set('label_position',[-14,-3,0],'test and resi 769 and name CA')
cmd.set('label_size',26,'test and resi 769 and name CA')
cmd.png(str(R/'assets/figures/1M17_contacts.png'),width=1800,height=1250,ray=1,quiet=1)
cmd.distance('polar_contact','test and resi 769 and name N','test and resn AQ4 and name N2')
cmd.set('dash_color','contact_c')
cmd.set('dash_width',5)
cmd.set('dash_gap',.25)
cmd.hide('labels','polar_contact')
cmd.png(str(R/'assets/figures/1M17_hbond.png'),width=1800,height=1250,ray=1,quiet=1)
cmd.quit()
