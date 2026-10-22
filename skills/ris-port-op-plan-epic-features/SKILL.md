---
name: ris-port-op-plan-epic-features
description: >-
  Propose or revise a bounded preliminary product-feature graph for one supplied
  epic outcome, checking coverage, identities, stage prerequisites and neighboring
  impacts. Use with direct product and current-work inputs; not for choosing next
  work, detailed requirements/design, implementation-task splitting or persistence.
---

# Plan preliminary features of one epic

Own a read-only, product-level graph proposal and its checks. Work from supplied
inputs in the current context or an isolated context chosen by the caller. Require
no RIS configuration, directory layout, tracker, CLI, harness or other skill.
The caller discovers sources, obtains human agreement and owns any persistence.
Do not launch agents, claim work, save files or mutate a tracker.

## Bound the inputs

Obtain the epic's goal/outcome, boundary, completion intent, accepted product
materials and constraints, observed capabilities, existing open/started/closed
features and dependencies, neighboring epic boundaries and roadmap context. A
proposed epic without a tracker ID is valid input; use an explicitly local draft
label, never a fabricated ID. State missing input and its dependent conclusions.
For revision include prior source scopes/versions, accepted commitments and actual
effects. Distinguish accepted behavior, observed results, assumptions and proposals.
Unknown tracker coverage cannot prove absence or authorize a new identity.

## Construct and check the proposal

1. Read relevant freely structured product material for desired behavior, not as
   a feature/module list. Extract substantial outcomes for this bounded goal/stage;
   retain numerical and negative constraints. Explain many-to-many source/outcome
   coverage with readable references, not a new global ID or trace registry.
   List covered, deferred (with reason), uncovered and unknown requirements.
   Return contradictions/material ambiguity for decision; do not promote new ideas.
2. Reconcile existing identities and accomplished capabilities before proposing
   additions. Prefer retaining the same identity for the same outcome; compare
   meaning, sources, boundaries and effects, not titles alone. Include all relevant
   states. Accepted/started/completed/foreign work constrains the plan. Diagnose
   stale candidates without deleting/closing them or rewriting accepted specs.
3. Propose the minimal sufficient coherent features, each with title, capability,
   observable expected result, epic membership, exclusions, source rationale and
   known prerequisites. One feature can suffice. Features may be preliminary:
   detailed spec/design, AC and implementation children are not entry conditions.
   Do not split into technical tasks or prescribe every future implementation.
4. Classify each proposed relationship explicitly:
   - implementation prerequisite: the dependent needs a delivered/integrated result
     for implementation or functioning; state that result and concrete reason;
   - requirements prerequisite: the dependent needs a specified accepted decision
     or contract before its dependent requirements work; identify the decision,
     required scope and evidence, not completion of the prerequisite feature;
   - informational reference: useful context only, never a blocker.
   Express direction as dependent → prerequisite. Do not serialize requirements
   merely because implementation will need another feature. Existing relationships
   of unknown scope remain unknown, not automatically implementation-only.
5. Check whole bounded outcome coverage, duplicates/overlaps, cycles (including
   existing and external paths), wrong directions, excessive/transitive blocking
   and independent parallel sets. Explain which work can be prepared concurrently
   and which concrete decisions/results it waits for; no universal strict sequence.
   A record/file/no blockers/raw closed alone never proves acceptance or readiness.
   This is a stage-aware plan, not a detailed lifecycle transition algorithm.
6. Lightly inspect supplied architecture/current-contract facts for ownership,
   shared-interface conflicts and research risks. Shared files alone do not imply
   conflict. Identify required common contract/version/decision and its owner;
   preserve independent work. Missing facts remain explicit, not invented design.
7. Compare neighboring epics and plans before settling membership. Propose a
   roadmap/boundary decision for cross-epic overlap; never silently move scope or
   invent a neighbor feature. Mark cross-epic endpoints outside supplied scope.

## Revision and result

On product changes, partial registration, changed dependencies or stale candidates,
repeat reconciliation against actual effects, retaining exact existing identities.
Distinguish unchanged, proposed additions, bounded content edits, explicitly proposed
edge removals and unresolved material changes. Accepted work requires an explicit
scope decision; create is not update. An unknown create effect needs reconciliation,
not another draft identity. Do not treat plans as implemented functionality.

Return the bounded graph with exact existing IDs versus local draft labels,
per-feature fields and source rationale, classified directed relationships and
needed decisions/results, coverage/gaps, parallel sets, neighbor impacts and a
concrete proposed delta with unresolved decisions. Verify references and graph
checks against supplied inputs; disclose incomplete inventory/baseline/acceptance
evidence. The result is an unsaved proposal, not human agreement, readiness,
persistence or authority for the next lifecycle operation. Stop here.
