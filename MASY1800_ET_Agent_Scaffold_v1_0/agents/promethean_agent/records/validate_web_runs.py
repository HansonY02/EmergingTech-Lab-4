"""Validate the actual schema constraints and preserve failures; no model invocation."""
from pathlib import Path
import json
import subprocess
root = Path(__file__).resolve().parents[3]
agent = root / 'agents/promethean_agent'

def errors(value, schema, where='$'):
    out=[]
    kinds={'object':dict,'array':list,'string':str}
    kind=schema.get('type')
    if kind in kinds and not isinstance(value,kinds[kind]):
        return [where+': wrong type, expected '+kind]
    if kind=='object':
        for key in schema.get('required',[]):
            if key not in value: out.append(where+': missing '+key)
        props=schema.get('properties',{})
        if schema.get('additionalProperties') is False:
            for key in value:
                if key not in props: out.append(where+': forbidden property '+key)
        for key,item in value.items():
            if key in props: out.extend(errors(item,props[key],where+'.'+key))
    elif kind=='array':
        for i,item in enumerate(value): out.extend(errors(item,schema.get('items',{}),where+'['+str(i)+']'))
    return out

schema=json.loads((root/'core/output_schema.json').read_text())
intake=json.loads((root/'core/input_schema.json').read_text())
report={'checker_scope':'All constraint keywords actually used in these schemas: type, required, properties, additionalProperties, items. Not a general-purpose JSON Schema implementation.','inputs':{},'baseline_v0_1':{},'revised_v0_2':{}}
for name in ['primary','contrast_1','contrast_2']:
    case=agent/'cases'/f'{name}.json'
    report['inputs'][name]=errors(json.loads(case.read_text()),intake)
    assert case.read_bytes()==(agent/'records/baseline_v0_1/cases'/f'{name}.json').read_bytes(),'case changed'
    for group,folder in [('baseline_v0_1',agent/'records/baseline_v0_1'),('revised_v0_2',agent/'responses')]:
        response=folder/f'{name}_response.json'
        if not response.exists():
            report[group][name]={'status':'not_saved'}
            continue
        try:
            value=json.loads(response.read_text())
            full_errors=errors(value,schema)
            basic=subprocess.run(['python3',str(root/'tools/validate_response.py'),str(response)],capture_output=True,text=True)
            report[group][name]={'status':'pass' if not full_errors else 'fail','schema_errors':full_errors,'supplied_basic_validator_returncode':basic.returncode,'supplied_basic_validator_output':basic.stdout.strip() or basic.stderr.strip()}
        except Exception as exc:
            report[group][name]={'status':'invalid_json','error':str(exc)}
subprocess.run(['python3',str(root/'tools/check_frozen_core.py')],check=True)
(agent/'records/web_validation_results.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
