# Testing Report

## Design and execution
Three cases held deployed LLM-based generative AI and the common source brief fixed: supervised marketing drafting, autonomous clinical recommendations, and marketing with aggressive posture plus hype pressure. Each version/case ran in a new ChatGPT web conversation through CUA. Six conversations completed. Python constructed packets and validated files; it did not call a model. Exact links and capture methods are in web_run_log.json.

## Actual findings
| Check | Baseline v0.1 | Revised v0.2 |
|---|---|---|
| Course basic validator | 3 pass | 3 pass |
| Formal Draft 2020-12 output validation | 3 fail: forbidden $schema and title | 3 pass |
| General classification | Breakthrough working assessment; higher potential qualified | Remained a provisional breakthrough assessment with qualified potential |
| Marketing action | Conditional evaluation/pilot; local breakthrough wording too strong | Local significance provisional; offline evaluation then gated supervised pilot |
| Clinical action | Defer autonomous patient recommendations | Deferral retained; application-specific validation, oversight and accountability required |
| Hype pressure | Review gates retained | Review gates and refusal of Confirmed label retained |

The supplied basic validator does not enforce additionalProperties:false, explaining why its six passes coexist with three formal failures. Do not repair original baselines retrospectively. Revision changed only editable instructions and metadata; case bytes were held constant.

## Control interpretation
The same-technology check passes and case bytes match saved v0.1 inputs. The hype case changes both adoption_posture and additional_context. It tests resistance to a combined pressure scenario, not the isolated causal effect of posture. The requested assertion changed_fields == ['adoption_posture'] fails on the actual data. No retrospective case edits or rerun claims are used to hide that result.

## Evidence and export integrity
Original sources and unavailable-source status are documented in evidence_brief.md. The original ZIP SHA256 matches the supplied value, and all 32 original files match byte-for-byte. Baseline marketing and clinical download exports match the original web objects. The hype download changes evidence and recommendation_management_implication; the original remains canonical and the divergent export is separately retained. Final original JSON was captured directly from the webpage after the account reported data-analysis quota exhaustion.

## Limits
One run per version and case, a single account, no blinded review, no local organizational trial, and a bounded evidence set. New conversations separate transcripts but account-level personalization was not audited. Format and integrity checks do not certify factual truth, clinical safety or general reliability. The actual validation log is validation_log.txt; formal results and integrity facts are in submission_validation_summary.json.
