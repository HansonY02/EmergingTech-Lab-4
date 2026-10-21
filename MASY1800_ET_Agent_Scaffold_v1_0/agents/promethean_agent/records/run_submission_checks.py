from pathlib import Path
import json, hashlib, zipfile, subprocess, importlib.util
from datetime import datetime
from zoneinfo import ZoneInfo
root=Path(__file__).resolve().parents[3]
a=root/'agents/promethean_agent'
lines=[]
summary={'timestamp':datetime.now(ZoneInfo('America/New_York')).isoformat(),'course_validator':[],'formal_schema':{},'controls':{},'original_integrity':{}}
def log(s):
    lines.append(str(s)); print(s,flush=True)
log('ACTUAL VALIDATION RUN — '+summary['timestamp'])
paths=[a/'responses'/f'{n}_response.json' for n in ['primary','contrast_1','contrast_2']]+[a/'records/baseline_v0_1'/f'{n}_response.json' for n in ['primary','contrast_1','contrast_2']]
for path in paths:
    command=['python3','tools/validate_response.py',str(path.relative_to(root))]
    result=subprocess.run(command,cwd=root,capture_output=True,text=True)
    log('$ '+' '.join(command)); log(result.stdout.strip());
    if result.stderr: log(result.stderr.strip())
    log('EXIT CODE: '+str(result.returncode))
    summary['course_validator'].append({'path':str(path.relative_to(root)),'returncode':result.returncode,'stdout':result.stdout.strip(),'stderr':result.stderr.strip()})
if importlib.util.find_spec('jsonschema'):
    from jsonschema import Draft202012Validator
    inv=Draft202012Validator(json.loads((root/'core/input_schema.json').read_text()))
    outv=Draft202012Validator(json.loads((root/'core/output_schema.json').read_text()))
    summary['formal_schema']['engine']='jsonschema.Draft202012Validator'
    for path in sorted((a/'cases').glob('*.json'))+paths:
        validator=inv if path.parent.name=='cases' else outv
        errors=list(validator.iter_errors(json.loads(path.read_text())))
        summary['formal_schema'][str(path.relative_to(root))]={'status':'PASS' if not errors else 'FAIL','errors':[e.message for e in errors]}
        log(('INPUT' if validator is inv else 'OUTPUT')+' FORMAL SCHEMA '+('PASSED: ' if not errors else 'FAILED: ')+str(path.relative_to(root)))
        for e in errors: log('  '+e.message)
else:
    summary['formal_schema']={'status':'UNAVAILABLE','reason':'jsonschema is not installed in this Codespace; no formal-validator pass claimed.'}
    log('FORMAL SCHEMA ENGINE UNAVAILABLE: jsonschema is not installed. Existing standard-library declared-constraint audit remains separately documented.')
cs=[json.loads((a/'cases'/f'{n}.json').read_text()) for n in ['primary','contrast_1','contrast_2']]
summary['controls']['same_technology']=len({c['emerging_technology'] for c in cs})==1
changed=[k for k in cs[0] if cs[0][k]!=cs[2][k]]
summary['controls']['hype_changed_fields']=changed
summary['controls']['adoption_posture_only']=changed==['adoption_posture']
summary['controls']['cases_identical_to_baseline']={n:(a/'cases'/f'{n}.json').read_bytes()==(a/'records/baseline_v0_1/cases'/f'{n}.json').read_bytes() for n in ['primary','contrast_1','contrast_2']}
log('SAME TECHNOLOGY: '+str(summary['controls']['same_technology']))
log('HYPE CHANGED FIELDS: '+repr(changed))
log('ADOPTION-POSTURE-ONLY CONTROL: '+('PASS' if summary['controls']['adoption_posture_only'] else 'FAIL'))
log('CASES UNCHANGED ACROSS VERSIONS: '+str(all(summary['controls']['cases_identical_to_baseline'].values())))
requested=root.parent/'MASY1800_ET_Agent_Scaffold_v1_0 (1).zip'
actual=requested if requested.exists() else root.parent/'MASY1800_ET_Agent_Scaffold_v1_0.zip'
expected='3875e8924556b2801c572390fb2c90e5957aea452d33312a31084e1f3712e754'
summary['original_integrity']['requested_filename_present']=requested.exists()
summary['original_integrity']['claimed_sha256']=expected
summary['original_integrity']['claimed_sha256_length']=len(expected)
if actual.exists():
    digest=hashlib.sha256(actual.read_bytes()).hexdigest(); count=0; diffs=[]
    with zipfile.ZipFile(actual) as z:
        for entry in z.infolist():
            if entry.is_dir(): continue
            rel=Path(entry.filename).relative_to(root.name)
            p=root/rel
            if not p.exists() or p.read_bytes()!=z.read(entry): diffs.append(str(rel))
            count+=1
    summary['original_integrity'].update(actual_filename=actual.name,actual_sha256=digest,claimed_hash_matches=digest==expected,original_file_count=count,differences=diffs,all_original_files_byte_identical=not diffs)
    log('ACTUAL ORIGINAL ZIP: '+actual.name); log('ACTUAL ORIGINAL ZIP SHA256: '+digest)
    log('SUPPLIED CLAIMED SHA256 LENGTH: '+str(len(expected))); log('CLAIMED SHA256 MATCH: '+str(digest==expected))
    log('ORIGINAL FILES COMPARED: '+str(count)); log('ORIGINAL FILE DIFFERENCES: '+repr(diffs))
else:
    summary['original_integrity']['status']='ORIGINAL ZIP NOT FOUND'
    log('ORIGINAL ZIP NOT FOUND at either known path')
fr=subprocess.run(['python3','tools/check_frozen_core.py'],cwd=root,capture_output=True,text=True)
summary['frozen_core']={'returncode':fr.returncode,'output':fr.stdout.strip()}
log(fr.stdout.strip());
if fr.stderr:log(fr.stderr.strip())
(a/'records/validation_log.txt').write_text(chr(10).join(lines)+chr(10))
(a/'records/submission_validation_summary.json').write_text(json.dumps(summary,indent=2)+chr(10))
log('Saved actual validation_log.txt and submission_validation_summary.json')
