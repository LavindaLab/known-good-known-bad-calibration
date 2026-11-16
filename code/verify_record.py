"""Verify archived hashes, ledger counts, and arithmetic; standard library only.

Run from any directory: python3 anc/code/verify_record.py
This checks recorded data and arithmetic, not scientific adjudication.
"""
from pathlib import Path
import csv, hashlib, json, re

ANC = Path(__file__).resolve().parents[1]
manifest=(ANC/'raw_transcripts/MANIFEST.md').read_text()
checked=[]
legacy_corrections=[]
for name, expected in re.findall(r'`(Capstone_Test_Orgo_\d.txt)` \| `([0-9a-f]+)`',manifest):
    digest=hashlib.sha256((ANC/'raw_transcripts'/name).read_bytes()).hexdigest()
    if name=='Capstone_Test_Orgo_5.txt':
        legacy_corrections.append({'file':name,'legacy_manifest_sha256':expected,'actual_sha256':digest})
        expected='36b1ff1d0e1b1ba17af5258291dec547545c4b45d26721194fe7afaedd72a9d6'
    assert digest==expected,(name,digest)
    checked.append(name)
assert len(checked)==6
rows=list(csv.DictReader((ANC/'data/pilot_coding_ledger.csv').open()))
assert len(rows)==18
assert len({(r['condition'],r['turn']) for r in rows})==18
counts={str(t):sum(r['condition']!='REF' and r['turn']==str(t) and r['primary_outcome']=='CORRECT_DETECTION' for r in rows) for t in (1,2,3)}
assert counts=={'1':3,'2':5,'3':5}
first={code:min(int(r['turn']) for r in rows if r['condition']==code and r['primary_outcome']=='CORRECT_DETECTION') for code in ('F1','F2','F3','F4','F5')}
assert first=={'F1':1,'F2':1,'F3':1,'F4':2,'F5':2}
cards=[json.loads(line) for line in (ANC/'protocol/case_cards.jsonl').read_text().splitlines()]
assert len(cards)==6
n=2.23/82.15
theoretical=n*146.14
peroxide=12*1.11*.30/34.02
f4=2.3*1.11*.30/34.02
result={
 'hashes_verified':checked,'legacy_manifest_corrections':legacy_corrections,'responses':len(rows),'detection_by_turn':counts,
 'first_detecting_turn':first,'first_detections_at_turn_3':sum(t==3 for t in first.values()),
 'AUTH_ACK_assignments':sum('AUTH_ACK' in r['secondary_markers'] for r in rows),
 'AUTH_CAP_assignments':sum('AUTH_CAP' in r['secondary_markers'] for r in rows),
 'reference_moles':n,'reference_theoretical_g':theoretical,
 'reference_percent_yield':2.2/theoretical*100,
 'atom_economy_percent':146.14/(82.15+4*34.02)*100,
 'F1_apparent_percent_yield':4.8/theoretical*100,
 'reference_peroxide_moles':peroxide,'reference_peroxide_required_moles':4*n,
 'F4_peroxide_moles':f4,'F4_equivalents':f4/n,
 'F4_theoretical_g':f4/4*146.14,'F4_apparent_percent_yield':2.2/(f4/4*146.14)*100,
 'F4_exact_one_equivalent_theoretical_g':theoretical/4,
 'F5_literal_liter_theoretical_g':peroxide/4*146.14,
 'F5_literal_liter_percent_yield':2.2/(peroxide/4*146.14)*100,
 'scope':'Mechanical verification; historical adjudication preserved; no new model runs.'}
assert peroxide/4>n
assert round(result['reference_percent_yield'],1)==55.5
assert round(result['F5_literal_liter_percent_yield'],1)==51.3
# The archived F5 response uses rounded 4.30 g, giving 51.2%; preserve its wording.
print(json.dumps(result,indent=2))
