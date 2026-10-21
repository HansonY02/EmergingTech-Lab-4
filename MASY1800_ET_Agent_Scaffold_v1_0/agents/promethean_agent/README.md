# Promethean Technology Classification Agent

Assignment 4, version 0.2-student. Start with ../../SUBMISSION.md, records/agent_record.md and records/testing_report.md.

Final original webpage JSON: responses/primary_response.json, contrast_1_response.json, contrast_2_response.json. Baseline originals, instructions, inputs and prompts: records/baseline_v0_1/. Source status: records/evidence_brief.md. Six actual conversation links: records/web_run_log.json.

## Reproduce verification from the scaffold root

    python3 agents/promethean_agent/records/run_submission_checks.py
    python3 agents/promethean_agent/records/validate_web_runs.py
    python3 tools/check_frozen_core.py

The formal validator requires jsonschema. All six course basic checks pass, but all three preserved baseline outputs fail the full schema because of forbidden extra properties. All three final outputs pass. The hype case varies both posture and promotional context; it is not a posture-only control. See the actual log rather than assuming all checks pass.

The submission folder contains the primary report, short professional-judgment draft, AI note and Craft Gained draft based on student-confirmed input. Student review and final Git versioning remain handoff steps. No OpenAI API key is required.
