"""One-off update: put the existing worksheet data and questions on lesson slides."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
files=['evolution_msa.json','coevolution.json','core_workflow.json','alternative_methods.json']
by_file={f:json.loads((R/'content'/f).read_text()) for f in files}
slides={s['id']:s for v in by_file.values() for s in v}

def worksheet(sid, title, data_title, questions, caption, items, data_text=None, table=None):
    s=slides[sid]
    s.update(title=title, kind='activity', body=[], worksheet_items=items)
    for k in ['sequence','table','profile']:
        s.pop(k,None)
    w={'data_title':data_title,'questions':questions,'caption':caption}
    if data_text is not None:w['data_text']=data_text
    if table is not None:w['table']=table
    s['worksheet']=w
    s['notes']='활동지의 자료와 질문을 모두 화면에 제시합니다. 종이 없이 화면을 읽고 구두 또는 개인 노트로 답한 뒤 바로 다음 정답·해설을 봅니다. '+s['notes']

worksheet(12,'활동지 1 · 두 계통수에서 진화 관계 판정','상황 A: D → S / 상황 B: S → D',[
'① 상황 A: H_A–M_A, H_A–H_B, H_A–M_B의 관계와 분기 사건은?',
'② 상황 B: H1–H2, H1–M, H2–M의 관계는? M에 대한 H1·H2의 관계는?',
'③ 가장 비슷한 두 서열은 반드시 ortholog일까요? 빠진 정보는?'],
'H=사람 계통, M=생쥐 계통. 가상 이력이며 가지 길이는 시간·유사도를 뜻하지 않습니다.', ['1.1','1.2','1.3'],
'A: duplication -> speciation\n           D\n       /       \\\n      A         B\n      S         S\n    /   \\     /   \\\n  H_A   M_A  H_B  M_B\n\nB: speciation -> duplication\n           S\n        /     \\\n       D       M\n     /   \\\n    H1   H2')
s=slides[13];s.pop('sequence',None)
s.update(kind='table',title='정답·해설 · 상황 A: 중복 뒤 종분화',table={'headers':['비교할 유전자 쌍','처음 만나는 사건','관계'],'widths':[4,4,4],'rows':[['H_A–M_A','종분화 S','Ortholog'],['H_A–H_B','중복 D','Paralog'],['H_A–M_B','중복 D','Paralog']]},body=['두 유전자에서 조상 쪽으로 거슬러 올라가 처음 만나는 노드를 찾습니다. 그 사건이 S인지 D인지로 판정합니다.','H_A–M_B는 서로 다른 종에 있어도 paralog입니다. 종 이름이나 서열 유사도만으로 관계를 정하지 않습니다.'])
s['notes']='상황 A에서 중복 D로 A/B가 먼저 갈라지고, 각 계열이 종분화 S로 H/M이 되었습니다. H_A–M_A는 A 계열의 S에서 처음 만나므로 ortholog입니다. H_A–H_B와 H_A–M_B는 D에서 만나므로 paralog입니다. 가지 길이는 판단에 사용하지 않습니다.'
s=slides[14];s['title']='정답·해설 · 상황 B와 서열 유사도의 한계'
s['table']={'headers':['상황 B의 비교','처음 만나는 사건','관계'],'widths':[4,4,4],'rows':[['H1–H2','중복 D','Paralog'],['H1–M / H2–M','종분화 S','두 쌍 모두 ortholog']]}
s['body']=['H1·H2는 M에 대한 co-orthologs입니다. H1과 H2 서로의 관계는 paralog입니다.','③ 높은 identity만으로 orthology를 확정할 수 없습니다. 유전자·종 계통수와 중복·종분화·소실 이력에 대한 근거가 필요합니다.']
s['notes']='상황 B에서는 종분화 뒤 H 계통에서만 중복이 일어납니다. 따라서 H1/H2는 서로 paralog이지만 각각 M에 대해 ortholog이며, M을 기준으로 co-orthologs라고 부릅니다. 관계는 비교하는 쌍과 분기 사건에 대해 정의합니다. 활동지1쪽3번의 답은 유사도만으로 사건을 알 수 없다는 것이며 계통수와 중복·소실 근거를 추가로 확인합니다.'

a3m='>query\nACDEFGHIKLMN\n>example_A1 group=A\nACDEFGHIKLMN\n>example_A2 group=A\nACDeeEFGHIKLMN\n>example_A3 group=A\nACDE-GHIKLMN\n>example_B1 group=B\nACDEYGHIKLXN\n>example_B2 group=B\nACDttEYGHIKL-N\n>example_B3 group=B\nAC-EYGHIKLXN'
worksheet(21,'활동지 2 · 전체 A3M을 읽고 답하기','전체 입력 · 7개 서열의 A3M',[
'① Query 포함/제외 행 수와 정렬 열 수는?',
'② ee의 위치는? 대문자화하면 생기는 오류는?',
'③ A3의 gap·B1의 X: 열 번호와 뜻은?',
'④ 행을 복제하면 독립 진화 정보도 늘어나나요?'],
'허구 자료이며 실제 예측 표적이 아닙니다. A/B는 임의 라벨입니다. 헤더 설명은 축약했고 서열은 그대로입니다.', ['2.1','2.2','2.3','2.4'],a3m)
slides[21]['worksheet']['data_size']=17

slides[31]['worksheet_items']=['3.1']
slides[31]['title']='활동지 3 · 두 열의 공동 빈도 계산'
slides[31]['body']=[
'D=Asp, K=Lys; i·j는 같은 단백질의 두 정렬 위치입니다. 두 자료는 가상입니다.',
'① 각 자료의 P(D_i), P(K_j), P(D_i, K_j)를 계산하고 독립일 때의 곱과 비교하세요.',
'단일 열의 빈도·보존도만으로 두 자료를 구별할 수 있나요?']
slides[36]['worksheet_items']=['3.2','3.3','3.4']
slides[36]['title']='활동지 3 · 계열을 나누고 진화 이력 해석'
slides[36]['body']=[
'가정: A/B 중복 → H/M/R/F 네 종 분화. 추가 중복·소실 없음. D=Asp, K=Lys.',
'② A_H–A_M, A_H–B_M의 관계는? 각 계열 내부에 변이가 남나요?',
'③ 8행은 독립 보상 변화 8회 또는 직접 접촉의 증거인가요? 공통 조상 효과는?',
'④ Ortholog만 모으면 계통 효과가 사라지나요? 더 필요한 근거를 쓰세요.']
slides[37]['body']=[
'8행은 독립 보상 변화 8회가 아닙니다. 조상의 조합을 물려받았을 수 있어 직접 접촉도 확정할 수 없습니다.',
'④ Ortholog 사이에도 공통 조상 효과가 남습니다. 정렬·계통수·계열 내부 변이·독립 가지의 변화와 구조·실험 근거를 함께 확인합니다.']

s=slides[71];s['worksheet_items']=['4.4'];s['title']='활동지 4 · 비교 조건을 설계하기'
s['body']=['④ MSA 행 선택의 효과를 보려면 A/B 중 어느 설계가 더 공정한가요?', '고정하거나 기록할 항목을 세 가지 이상 쓰고 이유를 설명하세요.']
compact='ID / group   A3M sequence\nquery        ACDEFGHIKLMN\nA1 / A       ACDEFGHIKLMN\nA2 / A       ACDeeEFGHIKLMN\nA3 / A       ACDE-GHIKLMN\nB1 / B       ACDEYGHIKLXN\nB2 / B       ACDttEYGHIKL-N\nB3 / B       AC-EYGHIKLXN'
worksheet(75,'활동지 4 · Depth를 줄이고 query 확인','원본 MSA와 선택 조건',[
'① Query와 A2·A3·B1만 남깁니다. 첫 행은 무엇이고 왜 유지하나요?',
'결과의 전체 행 수·homolog 행 수·정렬 열 수는?',
'원본과 비교해 잃거나 달라질 수 있는 정보는?'],
'실행 위치: AIprediction/practice/ · 컴퓨터 없이도 왼쪽 입력에서 선택 행을 표시해 풀 수 있습니다.', ['4.1'],
compact+'\n\n# depth=4, seed=7\npython3 msa_lab.py --depth 4 --seed 7 \\\n  --out runs/student01')
slides[75]['worksheet']['data_size']=17
worksheet(82,'활동지 4 · 두 그룹의 MSA를 직접 비교','그룹 라벨과 전체 입력',[
'② 동일 query와 A 행만, 동일 query와 B 행만 각각 묶으세요. 각 파일은 몇 행인가요?',
'각 그룹의 homolog 5열·11열 분포를 비교하세요.',
'이 라벨 분리와 AF-Cluster의 차이는? Ortholog 집합·구조 상태라 부를 수 있나요?'],
'A/B는 편의를 위한 사전 라벨입니다. 활동지 3쪽의 진화 이력을 주어진 조건으로 사용하지 않습니다.', ['4.2'],compact)
worksheet(88,'활동지 4 · A2의 5·7·10열을 X로 가리기','수정 전 입력 · 정렬 열은 1부터',[
'③ A2의 정렬 5·7·10열을 X로 바꾼 원문 문자열을 쓰세요.',
'Query·소문자 ee·A3의 기존 gap은 어떻게 하나요?',
'어느 열의 빈도와 다른 열과의 조합 정보가 가려지나요?'],
'5·7·10은 원문 문자 위치가 아닌 query 정렬 열입니다. 컴퓨터에서는 masked.a3m과 대조합니다.', ['4.3'],
'query      ACDEFGHIKLMN\nA2         ACDeeEFGHIKLMN\nA3         ACDE-GHIKLMN\n\nquery col  123456789012\n\nmask cols: 5, 7, 10\n\nA2 output: ______________')
rows=json.loads((R/'practice/synthetic_comparison.json').read_text())['rows']
labels={'full_MSA':'원본','shallow_MSA':'얕음','prelabelled_group_A':'라벨 A','prelabelled_group_B':'라벨 B','homolog_X_mask':'X mask'}
t={'headers':['ID','MSA','pLDDT','거리 Å','PAE Å'],'widths':[.60,1.60,1.35,1.55,1.55],'rows':[[r['id'],labels[r['condition']],str(int(r['mean_plddt'])),str(r['distance_A']),str(r['inter_region_pae_A'])]for r in rows]}
worksheet(96,'활동지 7 · 후보 8개를 신뢰도와 함께 판독','가상 180잔기 표적 · 전체 8개 후보',[
'① 서로 다른 거리의 후보 묶음을 찾으세요. 큰 거리만 보고 S2/M2를 선택해도 될까요?',
'② 평균 pLDDT가 가장 높은 모델 하나만 남기면 무엇을 놓칠 수 있나요?',
'③ 8개 중 3개가 비슷하면 평형 점유율은 3/8인가요? 더 필요한 근거는?'],
'거리: 40–140번 Cα / PAE: 20–70과 110–160 사이 양방향 평균. 실제 예측이나 앞의 A3M에서 계산한 값이 아닙니다.', ['7.1','7.2','7.3'],table=t)

for f,ss in by_file.items():
 (R/'content'/f).write_text(json.dumps(ss,ensure_ascii=False,indent=2)+'\n')
print('Worksheet pages 1–4 and 7 embedded in existing exercise slides')
