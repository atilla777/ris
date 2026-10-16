# Local bugfix — integrated delivery checks

## Subject, versions and evidence boundary

This is delivery evidence for the combined A+B+C instruction/package candidate,
not new requirements/design acceptance, feature verification or tracker closure.
Requirements and design v2 are the **entire** [spec.md](spec.md) and
[design.md](design.md), independently accepted in
[acceptance.md](acceptance.md#требования-v2) and
[the separate design decision](acceptance.md#дизайн-v2). Both original v2 decisions
resolve `containing-commit` to `aa27a20e049273fce55d660934af98bd65f34a79`;
later unchanged copies do not renew or repin them. All three files are unchanged
from that accepted revision in this candidate.

- A, registration (`ris-qv1.1.1`): integrated published source
  `4de804c8d7de22320f71348c244e8a1c9a05ed54`.
- B, investigation (`ris-qv1.1.2`): integrated published source/base
  `a284af3bb503228dfc0135e54f04c92e20babd89`.
- C, fixing (`ris-qv1.1.3`): complete candidate based on B, including source,
  synchronized installed resources, README/catalog/getting-started and this file.
  Exact complete-tree/check/author witness is retained in the authorized local
  implementation handoff for review; this self-referential document describes
  the **reviewed complete tree** without inventing its own future commit SHA.
  A publisher can provide the actual exact integrated published commit and
  independent review/publication evidence through tracker/implementation evidence.
  At initial author handoff those effects remain pending, not a claimed pass.

The A/B source contracts are inspected together with C on this candidate; prior
delivery observations apply only to their original unchanged mechanisms and
limits. Reading/static checks establish instruction consistency, and the existing
deterministic package lifecycle check covers the actual payload. Neither proves
live agent behavior, report-write CAS, reliability, speed, cost or cross-client
compatibility. No agent tests/live runs are part of this delivery.

## Inspected owners and seams

Paths below are relative to repository root. Corresponding installed skill paths
are exact synchronized copies under `.opencode/skills/`.

| Short locator | Inspected source / contribution |
|---|---|
| Register | `skills/ris-proj-op-register-bug/SKILL.md`: registration/duplicate identity, no investigation; adapter `references/standalone.md` native bug branch |
| Investigate | `skills/ris-port-op-investigate-bug/SKILL.md`, `skills/ris-proj-op-investigate-bug/SKILL.md`: sourced report, five outcomes, current report/file alternative; adapter `references/investigation.md` |
| Fix | `skills/ris-proj-flow-fix-bug/SKILL.md`: exact ID admission, conditional separately accepted design, snapshot and whole execute-task transfer |
| Adapter | `skills/ris-proj-adapter-beads-tasks/SKILL.md`, `references/{standalone,bug-execution,concurrency}.md`: typed ordinary bug reads/claim, accepted-design link append, recoverable full notes snapshot and real fix-completion separate from disposition |
| Design | `skills/ris-proj-op-design-feature/SKILL.md`, `references/acceptance-and-save.md`: accepted report/criteria basis, ordinary bug, separate decision and explicitly pre-execution design/document review → Documents publication; no future execution snapshot or implementation plan prerequisite |
| Execute | `skills/ris-proj-flow-execute-task/SKILL.md`, `references/{evidence,recovery,text-work}.md`: same full route/roles/recovery, conditional saved plan and snapshot applicability |
| Consumers | `skills/ris-proj-op-{prepare-task-worktree,plan-task,implement-task-tdd,review-task,publish-task}/SKILL.md`: explicit ordinary bug basis and bounded existing methods |
| Navigate/docs | `skills/ris-proj-op-suggest-continuation/SKILL.md`, `README.md`, `docs/{skills,getting-started}.md`: separate operations, read-only recommendation, direct loading, 47 skills / 18 commands / three flows |

## All 18 criteria on one integrated candidate

Each row records substantive **instruction inspection**, not an executed agent
scenario. Independent review of the complete candidate and later exact published
revision assessment remain separate owner gates; this author cannot approve itself.

| Criterion | A+B+C evidence and inspected positive/negative boundary |
|---|---|
| AC-001 | Investigate reuses supplied facts; Fix admission reads full saved report and sources without a mandatory questionnaire or repeated preparation. |
| AC-002 | Investigate report distinguishes expectation/basis, actual divergence, conditions, evidence/code/environment; Fix and Adapter preserve that text and criteria, Consumers identify the basis. A readiness/status label cannot replace authority or confirmation. |
| AC-003 | Fix accepts a sufficient report without formal spec/design or artificial children. Execute step 2 and recovery row 2 allow a justified no-saved-plan decision only when rules and execution/handoff sufficiency permit. Direct plan-task still persists; RIS's mandatory local plan remains. |
| AC-004 | Investigate performs proportionate local diagnosis and names facts/hypotheses/gaps; Fix stops on a precise research gap rather than inventing a cause, investigating silently or launching full feature preparation. Unknown final cause alone does not prevent a sufficient fix. |
| AC-005 | Investigate/Fix/Design return disputed expectation or conflicting sources to authority before dependent edits; a material contract/data-model/responsibility/invariant decision gets separately accepted design. Only affected results are reassessed. |
| AC-006 | Fix/Execute implementation and review transfer original divergence, success and affected-regression criteria with snapshot identity and exact candidate/check revision. TDD and review reject tuned expectations; unrun checks and applicability limits are explicit. |
| AC-007 | Execute retains three configured roles/actual launches, claim/copy guards, mandatory code TDD and fresh independent review. Text uses its bounded content owner without artificial RED. Consumers preserve project rules and missing-check limitations. |
| AC-008 | Fix transfers the same exact native bug to execute-task **in full**; existing prepare/plan/implementation/review/Git/adapter owners retain methods. No second recovery/publication engine or repeated sufficient-report preparation is introduced. |
| AC-009 | Fix/Execute/Adapter report fix/check/review, Git receipt, separate exact real fix-completion and tracker snapshot/read-back individually. Full success needs every promised effect; disposition or one channel alone is insufficient. |
| AC-010 | Register reconciles stable create/supplement identity; Investigate reconciles report/acceptance/original/relation/close separately. Adapter snapshot checks marker AND full text/occurrences; Execute recovery reuses actual applicable effects, verifies unknown remote effects and never blindly repeats append/push/close. |
| AC-011 | Conditional preparation is tied to concrete sufficiency or project obligations, with mandatory RIS local plan/TDD/review/copy/roles retained. No rules or future `ris-1wa` decisions/dependencies are introduced. |
| AC-012 | Source/install/docs/catalog are synchronized; metadata/resources/local links/dependencies/full diff and entire managed inventory are checked statically (47 skills, 18 unchanged command targets, three flows). One existing deterministic payload lifecycle check is selected; independent complete-tree review is handed to its owner. No new executable behavior or agent tests. |
| AC-013 | Register preserves an unconfirmed message/context, all-status duplicate/creation-key search, safe original supplement, verified exact ID and stop. Fix neither registers nor silently changes ID/type; task-only feature operations remain separate. |
| AC-014 | Portable Investigate has no RIS/tracker dependencies; project Investigate applies it and saves current report/aligned criteria or reports exact unsaved/partial remainder. Confirmation and readiness are independently reasoned, not new mandatory statuses. |
| AC-015 | Investigate leaves insufficient confirmation/unknown cause/failed reproduction open; only proved correct/duplicate enters separate disposition after stored proof, useful-original transfer/no-delta and nonblocking relation as applicable. Adapter execution completion instead requires a real verified fix and required Git publication. |
| AC-016 | Investigate current report is a delimited description section or a sole exact published `investigation.md`, preserving original/foreign content. Fix/Consumers retrieve full text; full execution-input notes snapshot is recoverable via project/tracker + exact ID + marker, independent of ignored local notes/chat. |
| AC-017 | Fix/Design/Consumers accept sufficient report/criteria/accepted constraints without formal spec/design pair. Material choices invoke the existing design owner and actual separate acceptance. Its exact-ID pre-execution review/publication use current report/criteria/accepted constraints and accepted design/decision, without a future execution snapshot or implementation plan. Fix implementation/mixed publication still require the full snapshot and applicable plan policy. Design source links can be appended without premature snapshot or report replacement. |
| AC-018 | Adapter snapshot contains full report, exact criteria, accepted decisions/constraints, identity/source/code revision and design evidence when needed. Plan/change/review identify it; each relevant consumer compares current basis and routes material drift for targeted applicability reassessment. Historical snapshots and published/closed facts are preserved; hashes/claims do not substitute for full text or freshness. |

## Checks and retained limitations

Independent review v1 of tree `8401051ea6a086d37226fc099406108fd7adc59a`
found R1 (medium): exact-ID pre-execution design review inherited an unconditional
execution-snapshot requirement. The R1 repair distinguishes document/design and
fix-implementation subjects in review and publication and carries the explicit
subject/basis through the design caller. It preserves independent complete-tree
review, separate acceptance, drift assessment and every implementation/publication
guard. This records an authored correction, not a passed fresh independent review;
the new complete tree requires that separate reassessment, especially AC-005/008/017.

Author checks cover the full source change plus all corresponding installed
bytes/types/modes and documentation. Source names/frontmatter/descriptions, owned
resources, dependency activation and local navigation are inspected; command count
and target map remain unchanged. The README bootstrap block is preserved.
The factual architecture map's existing general owner/placement statements still
apply: no normative rules or OKF bundle amendment is necessary for these seams.

The one applicable existing package check is:

```sh
PYTHONDONTWRITEBYTECODE=1 RIS_TEST_BASH=/bin/bash python3 -m unittest discover -s tests/package_installation_integration -p test_package.py -k test_complete_candidate_default_tag_sha_and_self_lifecycle -v
```

Its exact observed result, captured tree/fingerprint and applicability to the final
candidate are recorded with implementation/check evidence. This is a disposable
filesystem/CLI lifecycle oracle, not an agent run; no full installer matrix is
triggered by text payload additions. Independent review/publication/closure are
not implied by this file or by a passed package check.

Baseline Beads has no general content CAS. Investigation's stronger protected
report/acceptance replacement contract remains fail-closed if no provider exists;
C does not claim to repair that platform limit. Snapshot/source-link native append
preserves foreign notes but promises neither concurrent append-once nor atomic
report+snapshot capture. Fresh comparison/read-back and targeted drift assessment
are explicit, without pretending claim/sandbox is content/graph CAS. Live successful
report replacement, snapshot execution and bug completion were not exercised here.

The review handoff must bind the **complete** candidate tree (unchanged base,
overlays/additions/deletions/modes, no hidden exclusions), all 18 rows and actual
check evidence. High/medium findings require owner repair and fresh independent
review. Publication/integration changes require affected reassessment on the exact
new tree and separate independent remote receipts. Feature/epic closure remains
an explicitly authorized separate operation; this C delivery cannot close them.
