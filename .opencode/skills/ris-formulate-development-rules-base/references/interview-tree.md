# Engineering decision map

Read only when material decisions are unresolved. This is subject input to
`ris-interview-base`, not a second interview procedure. Reuse sourced answers.

| Branch | Prerequisites | Necessary decisions/evidence |
|---|---|---|
| Scope | Request | Create/update, nearest goal, bounded norm delta, existing task/permission/publication process |
| Environment | Scope and stack | Actual versions, license/SDK availability, shipped OS/architecture/web targets, dependency/build records |
| Existing checks | Environment | Commands/settings already in use, accepted style/tests, constraints of local/CI runners |
| Style/static | Existing checks | Preserve/choose one authority, supported diagnostics, generated/vendor exclusions, scoped old-code exception |
| Test strategy | Goal, environment and related architecture | Changed risks, pure/runtime/UI seams, fixtures/seeds/time, integration boundaries, test evidence |
| Security/dependencies | Inputs and distribution model | Relevant attack surface/advisories/provenance, freshness/skip handling, native libraries/assets |
| CI/DoD | Selected checks and process | Required/conditional gates, runner limitations, result/revision reporting, review/docs expectations |
| Exceptions/transition | Norm candidates and current project | Scope/authority/revisit trigger, how new/touched old code is governed without claiming compliance |

Ask the runtime/target question before proposing a command that depends on it.
Independent style, docs and known process branches can proceed while a platform
choice is deferred. Do not ask the person for facts available in supplied config.
Examples of focused questions: Which targets must this release support? Is the
existing test/style framework accepted? What licensed runner can CI actually use?
Who may accept a temporary exception? Where known, state options and their
tradeoffs; no forced tool selection just to finish the interview.
