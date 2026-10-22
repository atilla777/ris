# Negative reading examples (not live tests or real evidence)

Read only when a /1 illustration of `report-format-v1.md` is needed, not for routine /2
production or consumption. Apply these independent mutations to its synthetic
serialization example; these oracles do not add format rules.

| Mutation / external fact | Expected result |
|---|---|
| Add root `passed: true`, omit a required key, use string `required: "true"`, duplicate/merge a key or add an alias | Invalid format, no gate; parsers may accept more than this profile |
| Change schema to `ris.review/99` | Unsupported, no gate |
| Keep approved but make F1 high/medium open, a required check unverified/failed, coverage unverified or a limitation blocking | Contradictory/invalid verdict, no gate |
| Set F1 high/open and verdict changes_required | Valid adverse result, no gate |
| Set independence unverified, invocation_evidence null, verdict blocked | Valid blocked result, no gate |
| Set independence self, reviewer_context author-session, invocation_evidence null, verdict blocked | Valid self-review analysis, no independent approval |
| Retain approved while invocation_evidence is unavailable to the caller, or reviewer was an unlisted actual author/repairer | External provenance fails, no gate regardless of asserted confirmed |
| Current tree/base/exclusions or required input version differs | Stale/inapplicable, no gate despite valid format |
| Pass evidence inaccessible or exercises a different tree | Missing/inapplicable mandatory evidence, no gate |
| Append r2 with previous r1, F1 high/open, verdict changes_required | Preserve r1; selecting r1 cannot bypass later refutation |
| Append r2 resolving F1 with reviewer disposition fixed and independently sufficient checks/provenance | New round may approve its exact subject; r1 is unchanged |
| Duplicate round ID, broken previous link, absent prior finding or resolved F1 without disposition | Invalid history, no gate |
| Append malformed/unsupported later round | Reconcile, never fallback to r1 |

These are synthetic reading/program-test oracles, not real review evidence or
claims of observed agent behavior. No author RED/GREEN chronology is needed to
review the final result; substantive test sufficiency and current checks remain.
