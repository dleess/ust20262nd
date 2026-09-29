"""Check the teaching excerpts against the original 2ITY coordinate files."""
from pathlib import Path
import json
import shlex

ROOT = Path(__file__).resolve().parents[1]
slides = json.loads((ROOT / 'content/foundations.json').read_text())
slides += json.loads((ROOT / 'content/structure_reading.json').read_text())
assert [s['id'] for s in slides] == list(range(1, 62))
assert sum(s['minutes'] for s in slides) == 180
assert sum(s['minutes'] for s in slides if s['kind'] == 'break') == 20
pdb_index = next(i for i, s in enumerate(slides) if s['kind'] == 'pdb_text')
assert slides[pdb_index - 1]['title'] == '잔기 라벨 읽기'
pdb_slide, cif_slide, fields_slide = slides[pdb_index:pdb_index + 3]

pdb_atoms = [line.rstrip() for line in (ROOT / 'assets/structures/2ITY.pdb').read_text().splitlines()
             if line.startswith('ATOM  ')][:2]
assert pdb_slide['code'].splitlines() == pdb_atoms
cif_lines = (ROOT / 'assets/structures/2ITY.cif').read_text().splitlines()
tags = [line.strip() for line in cif_lines if line.startswith('_atom_site.')]
# ponytail: only the two simple ATOM rows used here; use a CIF library for general parsing.
original = [dict(zip(tags, shlex.split(line), strict=True)) for line in cif_lines
            if line.startswith('ATOM ')][:2]
example = cif_slide['code'].splitlines()
assert example[:2] == ['data_2ITY', 'loop_']
for line, atom, pdb_atom in zip(cif_slide['data_rows'].splitlines(), original, pdb_atoms, strict=True):
    assert shlex.split(line) == [atom[tag] for tag in example[2:]]
    assert [float(pdb_atom[start:start + 8]) for start in (30, 38, 46)] == [
        float(atom['_atom_site.Cartn_' + axis]) for axis in ('x', 'y', 'z')]
    assert pdb_atom[22:26].strip() == atom['_atom_site.auth_seq_id']
    assert pdb_atom[21] == atom['_atom_site.auth_asym_id']

first = original[0]
expected = [first['_atom_site.occupancy'], first['_atom_site.B_iso_or_equiv'] + ' Å²',
            first['_atom_site.label_seq_id'] + ' / ' + first['_atom_site.auth_seq_id'],
            first['_atom_site.label_alt_id'] + ' / ' + first['_atom_site.pdbx_PDB_ins_code']]
assert [row[1] for row in fields_slide['table']['rows']] == expected
print('PASS: PDB/mmCIF excerpts, field values, slide sequence and 180-minute schedule')
