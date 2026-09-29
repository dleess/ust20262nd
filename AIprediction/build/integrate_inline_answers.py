"""One-off migration: insert reviewed answers into the existing source JSON files."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
FILES = ['evolution_msa.json', 'coevolution.json', 'confidence.json', 'alternative_methods.json', 'core_workflow.json']
blocks = {}
for path in sorted((ROOT / 'build/answer_drafts').glob('*.json')):
    for block in json.loads(path.read_text()):
        assert block['after_id'] not in blocks, block['after_id']
        blocks[block['after_id']] = block['slides']
assert set(blocks) == {12,19,21,26,30,41,44,49,53,55,58,61,63,66,71,77,78}

by_file = {name: json.loads((ROOT / 'content' / name).read_text()) for name in FILES}
original = sorted((s for slides in by_file.values() for s in slides), key=lambda s:s['id'])
assert len(original) == 80, 'Migration already applied or source changed'
assert sum(s['minutes'] for s in original) == 180
result, mapping, answers = [], {}, {}
for source in original:
    old_id = source['id']
    inserted = blocks.get(old_id, [])
    if inserted:
        for s in inserted:
            s['minutes'] = .5 if old_id == 44 else (2 if old_id == 77 and s is inserted[0] else 1)
        source['minutes'] -= sum(s['minutes'] for s in inserted)
        assert source['minutes'] > 0, (old_id, source['minutes'])
        # Existing activity time already included the explanation: split, never add it twice.
        note = source['notes']
        timing = [
            '개인 풀이 1분, 짝 토론 1분, 전체 해설 2분으로 운영합니다.',
            '4분 안에는 화면 예제와 활동지 1번을 우선 풀고 나머지는 해설·확장 문항으로 둡니다.',
            '진행 2분 풀이+2분 해설.',
            '개인 계산 1분 후 짝과 분모를 확인하고 1분 동안 해설합니다.',
            '1분 개인 계산, 1분 짝 비교, 1분 강사 해설로 운영합니다.',
            '1분 관계 판정, 1분 전체·계열별 비교, 1분 해설로 운영합니다.',
            '30초 구두 또는 손계산, 30초 해설로 진행합니다.',
            '1분 개인 풀이 뒤1분 해설합니다.',
            '2분 짝 토의와1분 해설로 진행합니다.',
            '1분 개인 판단, 1분 짝 토론, 1분 공유로 운영한다.',
            '개인1분·확인1분·해설1분.',
            '1분 파일 읽기, 1분 비교, 1분 해설로 진행합니다.',
            '1분 손계산, 1분 출력 대조, 1분 해설로 진행합니다.',
            '학생 활동지에는 정답을 적지 않았으며 이 노트만 교사용 해설입니다.',
            '이 답은 학생 화면에 먼저 보여주지 않는다.',
        ]
        for t in timing:
            note = note.replace(t, '')
        source['notes'] = '먼저 문제를 풀고, 바로 다음 정답·해설 화면에서 풀이와 흔한 오류를 확인합니다. ' + note.strip()
    source['id'] = len(result) + 1
    mapping[old_id] = source['id']
    result.append(source)
    for s in inserted:
        s['id'] = len(result) + 1
        s['answer_for'] = source['id']
        result.append(s)
        answers.setdefault(source['id'], []).append(s['id'])

assert sum(s['minutes'] for s in result) == 180
assert sum(s['minutes'] for s in result if s['kind']=='break') == 20
for name, original_slides in by_file.items():
    owned_ids = {s['id'] for s in original_slides}
    owned = [s for s in result if s['id'] in owned_ids or s.get('answer_for') in owned_ids]
    (ROOT / 'content' / name).write_text(json.dumps(owned, ensure_ascii=False, indent=2) + '\n')

# References within source prose, distinct from all structural ID fields above.
p = ROOT / 'content/core_workflow.json'
ss = json.loads(p.read_text())
for s in ss:
    s['body'] = [t.replace('다운로드는 39번', f'다운로드는 {mapping[39]}번') for t in s['body']]
p.write_text(json.dumps(ss, ensure_ascii=False, indent=2)+'\n')
(ROOT/'build/inline_answers_slide_map.json').write_text(json.dumps({'old_to_new':mapping,'answer_slides':answers,'slides':len(result)},ensure_ascii=False,indent=2)+'\n')
print(f'{len(original)} -> {len(result)} slides; {sum(map(len,blocks.values()))} answer/check slides; 180 minutes')
