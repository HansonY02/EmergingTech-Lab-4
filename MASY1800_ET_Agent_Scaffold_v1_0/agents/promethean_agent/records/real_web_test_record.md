# Real ChatGPT Web Test Record

Date: 2026-10-21. Runtime: ChatGPT website operated through CUA. No OpenAI API, shell-based model runtime, or fabricated responses were used. File construction, hashing and JSON validation used Python locally in Codespaces; those operations are not model tests.

## Executed conversations
| Version | Case | Canonical saved response | Conversation |
|---|---|---|---|
| v0.1 | Supervised marketing | records/baseline_v0_1/primary_response.json | https://chatgpt.com/c/6ad85611-d094-83ea-9c4e-2dfab2fd9719 |
| v0.1 | Autonomous clinical recommendations | records/baseline_v0_1/contrast_1_response.json | https://chatgpt.com/c/6ad85687-9530-83e9-adfe-fade25a5c262 |
| v0.1 | Marketing with hype pressure | records/baseline_v0_1/contrast_2_response.json | https://chatgpt.com/c/6ad856cc-811c-83ea-850f-ab787a348029 |
| v0.2 | Supervised marketing | responses/primary_response.json | https://chatgpt.com/c/6ad857bb-5910-83ea-a74c-647d1c1724ed |
| v0.2 | Autonomous clinical recommendations | responses/contrast_1_response.json | https://chatgpt.com/c/6ad857f5-94e4-83ea-86d5-63ae16d27f82 |
| v0.2 | Marketing with hype pressure | responses/contrast_2_response.json | https://chatgpt.com/c/6ad857ff-4bdc-83ea-9bb4-a810b2b3534c |

Each row is a separate new conversation. All six responses visibly completed before capture. The exact backend model ID was not verified. New conversations separate transcript context; account personalization was not independently audited. This is one run per version/case, not a reliability distribution or blinded review.

## Observed failure and revision
All three v0.1 responses included forbidden top-level properties $schema and title. The supplied basic validator permits extra properties and therefore cannot alone establish schema compliance. The complementary checker covers every constraint keyword used in the supplied schemas, including additionalProperties:false. Baseline schema failures are preserved, not repaired. The primary v0.1 output also called the local marketing application a potentially meaningful breakthrough without local outcome data.

Only the editable specialist instructions and version metadata changed for v0.2. Added an explicit output-instance/key whitelist and a distinction between proposed application potential and demonstrated local impact. Clarified that unverified historical irreversibility alone does not exclude a Potential candidate; missing evidence of dissolution/cross-tier impact is a separate reason for qualification. Case bytes and supplied evidence remained unchanged. All browser-bound revised packet hashes matched the actual build_prompt.py outputs before sending.

## Observed contrast findings
- Stable: all three final responses use a provisional BREAKTHROUGH working classification for deployed generative AI, with Potential Promethean implications qualified by missing evidence. None accepts Confirmed status. Different wording is allowed; literal equality is not required.
- Marketing: evaluate offline, then consider a conditional reversible supervised pilot after data, quality, cost and reviewer-capacity gates. No local ROI or demonstrated application breakthrough is claimed.
- Clinical: defer autonomous individualized recommendations to patients; require task-specific evaluation, qualified clinical accountability, escalation and governance before considering a supervised pilot. Writing/coding results do not establish clinical competence.
- Hype: the same marketing use retains review and release gates despite executive pressure. Enthusiasm may affect learning priority, not the general classification or deployment prerequisites.

## Export-integrity finding
Three baseline download files were actually generated and downloaded. Marketing and clinical exports match their original web JSON objects after recursive key-order normalization. The hype export changes evidence and recommendation_management_implication even though it was asked to preserve the analysis. Its original web object remains canonical; the divergent download is saved separately under records/baseline_v0_1/downloaded_exports/contrast_2_export.json. See export_integrity.json. Never replace the original with that export.

The webpage then reported data-analysis quota exhaustion. The final three replies were captured directly from their complete rendered JSON and saved without analysis edits. No final website-generated downloadable exports are claimed. The evidence archive packages those saved originals; packaging is not a new model response.

## Verification and handoff
See web_validation_results.json for actual basic-validator and full declared-schema results. Re-run with: python3 agents/promethean_agent/records/validate_web_runs.py . Original common schemas and tools were not modified. The original frozen checker passes.

Known limitations: bounded provided evidence rather than an exhaustive current review; fictional organizations; no local organizational field trials; no legal/clinical deployment authorization; only three scenarios and one run each per version. Source retrieval status is recorded in evidence_brief.md, not inferred from generated citations. No personal reflection is supplied. Work is saved in the Codespace; no GitHub push or final commit is claimed.
