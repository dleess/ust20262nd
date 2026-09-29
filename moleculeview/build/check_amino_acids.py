"""Verify that the lesson explains every basic amino acid once with correct codes."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
slides = json.loads((ROOT / 'content/foundations.json').read_text())
expected = {
    'Gly': ('G', 'Glycine'), 'Ala': ('A', 'Alanine'), 'Val': ('V', 'Valine'),
    'Leu': ('L', 'Leucine'), 'Ile': ('I', 'Isoleucine'), 'Pro': ('P', 'Proline'),
    'Met': ('M', 'Methionine'), 'Phe': ('F', 'Phenylalanine'), 'Tyr': ('Y', 'Tyrosine'),
    'Trp': ('W', 'Tryptophan'), 'Ser': ('S', 'Serine'), 'Thr': ('T', 'Threonine'),
    'Cys': ('C', 'Cysteine'), 'Asn': ('N', 'Asparagine'), 'Gln': ('Q', 'Glutamine'),
    'Asp': ('D', 'Aspartic acid'), 'Glu': ('E', 'Glutamic acid'),
    'Lys': ('K', 'Lysine'), 'Arg': ('R', 'Arginine'), 'His': ('H', 'Histidine'),
}
seen = {}
for slide in slides:
    if slide['kind'] != 'amino_acids':
        continue
    assert slide['notes'] and slide['sources']
    for name, code, side_chain, feature in slide['table']['rows']:
        three, one = code.split(' / ')
        assert three not in seen, f'Duplicate amino acid: {three}'
        assert side_chain.strip() and feature.strip(), f'Missing explanation: {three}'
        seen[three] = (one, name.split('\n')[1])
assert seen == expected, (seen.keys() ^ expected.keys(), seen)
print('PASS: all 20 basic amino acids have names, correct codes, side chains and explanations')
