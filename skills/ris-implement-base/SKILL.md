---
name: ris-implement-base
description: >-
  Implement one bounded accepted change or repair concrete review findings in
  current code, with applicable tests and versioned evidence. Use for portable
  task implementation; not requirement approval, feature redesign, independent
  review, project tracker/worktree management or publication.
---

# Implement a bounded change

Own code/test changes and their checked handoff. Work outside RIS with supplied
requirements, current code, accepted technical constraints/design, plan if
available, project rules and explicit file/command permissions. Do not require
RIS skills, configuration, directories or a tracker. The caller owns project
identity, claim, documentation integration, independent approval and publication.

1. Establish outcome, exclusions and criteria; inspect the actual implementation,
   conventions, current working tree and relevant tests. Record base revision,
   existing user changes and the exact permitted scope. Compare the plan's code
   assumptions and accepted contract versions to current facts; stale plans need
   bounded replanning, not blind execution. Missing essential inputs block only
   dependent changes. A feature implementation needs independent acceptance of
   the applicable requirements and design; a standalone change uses its accepted
   technical constraints without invented feature metadata.
2. Map criteria to behavior and test seams. Implement small checkable increments
   using existing interfaces, state owners and allowed dependency directions.
   Add meaningful tests for changed behavior and applicable static/contract/
   integration fitness checks; do not mirror implementation or add ceremonies
   for reversible low-impact edits. Keep quantitative and negative requirements.
3. Decide local reversible details within accepted design. A change of public
   contract, responsibility, state owner, invariant or desired behavior is a
   revision proposal, not an implementation choice. Report affected criteria,
   contracts, adjacent work/tests and required decision owner. Stop that dependent
   change while completing authorized independent work; do not rewrite product
   sources or global architecture to legitimize the departure.
4. Run applicable checks and inspect their actual exit/results. Record commands,
   environment, observed outcomes and limits against the exact final diff/tree
   (commit or reproducible content fingerprint including new files).
   Distinguish the proposed publication snapshot from local context: identify
   the base snapshot, authorized file overlays/additions/deletions and explicit
   exclusions before review. Bind every snapshot path/content (and Git modes
   where applicable); retain unchanged base files. Local reports, generated
   outputs and tracker state are evidence, not automatically publication payload.
   Excluded dirty tracked files use their specified base bytes in the proposed
   snapshot. Report contextual changes separately; do not hide code with exclusions.
   Failed or unavailable mandatory checks remain failures/unverified. After an edit assess
   which evidence is invalidated and rerun affected checks, not every expensive
   suite automatically. Inspect final diff for unintended changes.
5. For repair input, confirm findings apply to the current tree. Required repair
   covers high/medium: retain IDs and link them to fixes or reasoned disputes,
   preserving requirements and reporting unresolved blockers. Low recommendations
   are optional; do not repair them automatically or create tasks/another round
   for them alone. A collective disposition suffices. Recheck fixes and related
   regressions; changed inputs may expose new concrete blockers, not justify a
   fresh style audit. Repair is not approval: reassess affected bytes, independently
   when project/caller rules require it. No round limit approves unresolved blockers.

Return `checked|partial|blocked` with scope, input/design/contract versions, files
and final tree identity, criterion-to-check results, repair mapping if applicable,
unrun checks and revision needs. Do not call the change independently approved.
Do not commit/push, manage tracker/worktrees, close work, or start another skill.
