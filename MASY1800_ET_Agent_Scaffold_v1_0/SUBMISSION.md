# Assignment 4 — Promethean Technology Classification Agent

## Submission map
| Course requirement | File / location |
|---|---|
| 1. Working agent package and Agent Record | agents/promethean_agent/ and agents/promethean_agent/records/agent_record.md |
| 2. Agent output report | agents/promethean_agent/submission/01_primary_output_report.md; original JSON: responses/primary_response.json inside the agent folder |
| 3. Independent professional judgment, half a page or less | agents/promethean_agent/submission/02_independent_judgment.md |
| 4. AI / verification note | agents/promethean_agent/submission/03_ai_verification_note.md |
| 5. Craft Gained, at most 100 words | agents/promethean_agent/submission/04_craft_gained.md |

The short judgment is a student-review draft. Its local-action position follows the student's explicit confirmation. Craft Gained uses the student's stated surprise about judgment beyond valid output and confirmed future method of designing contrast tests earlier. No unreported personal experience or personal history is added. The student should read and adopt or amend the final wording before submission.

## Actual validation, not a reconstructed all-pass narrative
- Six course basic-validator runs: all pass.
- Formal jsonschema.Draft202012Validator: three inputs and three final outputs pass; three preserved baseline outputs fail because $schema and title are forbidden extra properties.
- Same-technology and unchanged-case-across-versions checks pass.
- Hype is a joint adoption-posture plus promotional-context contrast. The strict adoption-posture-only assertion fails; do not describe it as an isolated posture-only experiment.
- The supplied original ZIP hash matches; all 32 original files are byte-identical. Frozen core is intact.
- See records/validation_log.txt and submission_validation_summary.json inside the agent folder.

## Preserved evidence
Six actual independent ChatGPT webpage conversations, original JSON, prompts, v0.1 instructions and cases, v0.2 revision, source status and download-export discrepancy are retained. See records/testing_report.md, real_web_test_record.md and web_run_log.json.

## Version handoff
Repository: https://github.com/HansonY02/EmergingTech-Lab-4 . See records/version_record.json for the actual branch, current repository HEAD and working-tree digest. No final commit or remote push is claimed. Student name and final commit must be confirmed before handoff.
