---
name: ris-decompose-spec-base
description: >-
  Propose and check verifiable work units from a supplied feature specification,
  tracing criteria, accepted design, test seams and necessary dependencies. Use
  when feature requirements and sufficient design are ready to break into work;
  not for eliciting or approving requirements, planning one task's technical
  implementation, or creating tracker records.
---

# Decompose feature requirements into verifiable work

Own the **portable task proposal and its coverage check**, not the source
specification, its acceptance, project paths, tracker records or task ownership.
Work from explicitly supplied content and applicable rules of the actual
project. This skill requires no `ris-common`, `ris-context`, `ris.yaml`, Beads,
RIS layout or other installed skill. A project caller selects and checks the
current specification, acceptance evidence, existing task state and technical
context; it owns any authorized persistence and verification of real IDs and
links. Do not turn a proposed task into a saved or accepted one.

## Establish the inputs

Identify the feature goal, boundary, specification/version and its known
acceptance status, observable criteria, constraints and exclusions, existing
verified work if supplied, and the requested level of decomposition. Retain
source references and decision status so that a recipient can trace each
material requirement. A file's presence or another agent's claim of acceptance
does not prove it; if the supplied version is only proposed, label every
derived task proposal as conditional on its acceptance. Do not assume a
particular task type, tracker key, branch, file format, or ID.

Require the supplied sufficient design and its independently known acceptance
scope/version, applicable contracts and versions, component/state owners,
allowed dependency direction, error/data flows and test seams. A short design
confirming existing contracts can suffice; no separate design file or new
abstraction is mandatory. Check relevant observed code and whether contracts
are current, accepted future prerequisites, or unavailable. Missing or disputed
design/test boundaries prevent a ready task set: return supported analysis as
partial, without inventing architecture or treating requirements approval as
design approval. An explicitly requested provisional proposal stays conditional.
On changed design, identify affected units/criteria/checks and retain unchanged
requirements decisions; return substantive contract conflicts to their owner.

Check that the specification actually states the behavior and observable
results needed to bound the work. If the feature identity, scope or material
criterion is missing or contradictory, identify precisely which tasks and
coverage claims it blocks. Ask a focused clarification if the user can resolve
it now; otherwise return independently supported parts as **partial**, not a
complete task set. Do not choose among disputed requirements or turn an open
decision into a default. A nonblocking open question may remain open when its
effect and boundary are explicit; do not pre-plan it as accepted scope.

## Derive the smallest useful work set

1. Map the specification's required outcomes, scenarios, failures, numerical
   and negative constraints, interfaces and material quality properties to
   work that can be verified. Separate accepted scope from unaccepted proposals
   and exclusions. Account for confirmed existing work without recreating it;
   identify what is already covered and what still needs doing. Never convert
   an exclusion or an optional future idea into a required task.
2. If the feature itself is one bounded, verifiable work unit, propose **one
   feature task** with its outcome and check; no artificial child or duplicate
   parent task. Otherwise partition along coherent deliverable outcomes or
   genuinely necessary investigation, not one task per document section,
   technology layer, test type, or lifecycle phase. Keep units small enough to
   finish and check independently where feasible, yet retain end-to-end
   behavior; explain why the split is needed. Do not plan the technical steps
    inside every unit or prescribe a stack without supporting input. Prefer
    tracer-bullet units that verify complete behavior through the necessary
    components using the accepted design, not autonomous stacks per feature.
    A headless outcome need not add UI. Justify a preparatory migration or
    infrastructure unit by the contract/result it enables; do not relabel it
    as a user capability or introduce a mandatory model → API → UI chain.
3. For each proposed unit give its useful result and boundary, significant
   exclusions, the observable completion check, and the specific source
    requirements it covers, the needed design/contracts and versions, and test
    seams/check ownership. Preserve supplied stable AC IDs; when a permanent
    feature slug is supplied, qualify them as `slug#AC-nnn` without inventing
    global product IDs or a second registry. Retain conditions of numerical limits and negative
   requirements in the checks. A task may cover several requirements and one
   requirement may span tasks; name where the **combined behavior** will be
    checked on a common integrated revision instead of assuming that isolated
    successes prove the feature. A shared integration check need not be a
    separate task or acceptance phase.
4. Add only prerequisite relationships justified by an outcome that must be
   available first. State direction unambiguously (blocked unit → prerequisite)
   with a reason; distinguish necessity from preferred order or shared scope.
   Verify that endpoints exist in the proposed or confirmed-existing set and
   there are no cycles. Independent units need no invented chain. A dependency
   on a disputed, unfinished or inaccessible external result is a readiness
   gap, not a silently completed prerequisite.
5. Cross-check every accepted requirement and observable criterion against
   the proposal **and** any confirmed existing work; check exclusions, key
   alternative/error scenarios, overlap, unsupported additions, missing
   combined checks, vague completion conditions, unjustified edges and cycles.
   Revise the split or report each uncovered or unverified area and why. No
   claimed full coverage from task titles alone.

## Return and stop

Return the feature/spec and independent design identities, scopes, versions and
acceptance status, applicable contracts/test seams, observed existing work (if any),
one task or a bounded set of task proposals with outcomes, checks, boundaries
and traceable source coverage; for multiple units return a clear mapping of
requirements to proposed/existing units and combined checks. List necessary
directed dependencies and their reasons, or explicitly say none are needed.
State whether all **available accepted** requirements are covered, and whether
missing evidence or unaccepted decisions block declaring a complete, ready
task set. Give the exact open questions and their effects. Labels are local
proposal references, not tracker IDs; include enough source substance or
accessible references and statuses for continuation without this chat.

Do not write a project file, create or update tracker entries, assign work,
approve the specification, produce technical plans, or start implementation.
The caller checks acceptance, permissions and persisted coverage separately.
Stop after reporting the checked proposal and its limitations.
