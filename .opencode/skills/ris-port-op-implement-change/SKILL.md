---
name: ris-port-op-implement-change
description: >-
  Implement one bounded accepted change or repair concrete review findings in
  current code, with meaningful tests, affected checks and optional required TDD.
  Use for portable implementation or test-first work; not requirement approval,
  feature redesign, independent review, tracker/worktree management or publication.
---

# Implement a bounded change

Own code/test changes and their checked handoff. Work outside RIS with supplied
requirements, current code, accepted technical constraints/design, plan if
available, project rules and explicit file/command permissions. Do not require
RIS skills, configuration, directories or a tracker. The caller owns project
identity, claim, documentation integration, independent approval and publication.

Establish `implementation_mode: standard|tdd` from the caller, request and project
rules; default to `standard` only when none requires TDD. This is a semantic input,
not a host-loader argument or RIS config field. Conflicting requirements block the
affected work. Both modes require meaningful tests for changed behavior and actual
applicable checks.

## Conditional resources

Read from **this installed folder**, only on the stated condition:

- `references/tdd.md` in `tdd` mode before changing behavior. Observe expected
  RED before implementation and GREEN after; never silently fall back to test-last.
- `references/publication-snapshot.md` before checks/handoff when unrelated dirty
  files, context exclusions or ambiguity complicate the publication snapshot.

Unavailable required resources block dependent work, not independent inspection.

## Implement and check

1. Establish outcome, exclusions and criteria; inspect the actual implementation,
   conventions, current working tree and relevant tests. Record base revision,
   existing user changes and the exact permitted scope. Compare the plan's code
   assumptions and accepted contract versions to current facts; stale plans need
   bounded replanning, not blind execution. Missing essential inputs block only
   dependent changes. A feature implementation needs independent acceptance of
   the applicable requirements and design; a standalone change uses its accepted
   technical constraints without invented feature metadata.
   If feasibility rests on an uncertain platform behavior or external boundary,
   use current evidence or the smallest permitted decisive probe before dependent
   changes. Return a confirmed contract conflict promptly to the caller/user;
   do not prolong attempts to satisfy incompatible obligations. Independent
   authorized work may continue, but cannot resolve or conceal that decision.
2. Map criteria to observable behavior and stable test boundaries from accepted
   inputs and existing conventions; ask only for missing material decisions.
   Implement small increments using existing interfaces, state owners and allowed
   dependency directions; in `tdd` apply the owned loop. Add/update tests for
   changed behavior, including applicable failures, boundaries and quantitative
   requirements. Derive expectations independently from requirements or worked
   examples, not by repeating the implementation. Prefer real internal components;
   isolate external boundaries or nondeterminism where needed, and justify any
   implementation-coupled substitute. Do not add ceremonial tests for text-only
   or reversible low-impact changes; behavior-preserving refactors keep tests green.
3. Decide local reversible details within accepted design. A change beyond or
   contrary to accepted requirements/design/contracts in public contract,
   responsibility, state owner, invariant or desired behavior is a revision
   proposal, not an implementation choice. Report affected criteria,
   contracts, adjacent work/tests and required decision owner. Stop that dependent
   change while completing authorized independent work; do not rewrite product
   sources or global architecture to legitimize the departure.
4. Select and **run** the smallest sufficient affected check set: new/changed tests,
   existing regression tests and consumers of changed contracts, plus applicable
   static/contract/integration checks. Use project commands and inspect actual
   exits/results. Run a full suite only when project rules require it or impact
   cannot be covered reliably by a narrower set; state the reason. After edits
   rerun invalidated checks, retaining suitable current evidence for other parts.
   Prefer deterministic tests for parsing, arithmetic and error handling; live
   agent runs are for behavior those tests cannot establish, such as instruction
   following and tool choice. Before extra live runs or new verification setup,
   name the remaining evidence gap, why cheaper/current evidence is insufficient
   and the decision the result will inform. If effort materially grows beyond the
   planned check, return the limitation and options to the caller/user before
   expanding dependent verification. Do not silently waive a mandatory check;
   any accepted reduction retains explicit unverified claims and limits.
   Failed/unavailable mandatory checks remain failed/unverified, not inapplicable.
   Record commands, environment, selection rationale, outcomes and limits against
   the exact final snapshot: base revision plus authorized additions/changes/
   deletions bound to content and modes, retaining unchanged base files. Include
   new files; identify the snapshot reproducibly by commit or content fingerprint.
   Local reports/tracker/tooling are context, not automatically publication payload.
   Checks must exercise that snapshot; runtime-affecting contextual differences
   require reassessment. Inspect the final diff for unintended changes.
5. For repair input, confirm findings apply to the current tree. Required repair
   covers high/medium: retain IDs and link them to fixes or reasoned disputes,
   preserving requirements and reporting unresolved blockers. Low recommendations
   are optional; do not repair them automatically or create tasks/another round
   for them alone. A collective disposition suffices. Recheck fixes and related
   regressions; changed inputs may expose new concrete blockers, not justify a
   fresh style audit. Repair is not approval: reassess affected bytes, independently
   when project/caller rules require it. No round limit approves unresolved blockers.

Return `checked|partial|blocked` with mode, scope, input/design/contract versions,
files and final snapshot identity, criterion-to-check results, TDD evidence when
required, repair mapping, unrun checks and revision needs. Do not call the change
independently approved.
Do not commit/push, manage tracker/worktrees, close work, or start another skill.
