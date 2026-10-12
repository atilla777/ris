---
name: ris-plan-task-base
description: >-
  Prepare and check a technical implementation plan for one selected task from
  its requirements, available code and constraints. Use when a task needs an
  actionable approach, steps and acceptance-check strategy; not for choosing or
  decomposing tasks, changing requirements, saving a project plan or implementing it.
---

# Plan one task's technical implementation

Own the **portable plan content and its readiness check**, not the project's
task selection, requirement approval, artifact storage, worktree or execution.
Work from the supplied task, applicable requirements, accessible code and
actual project rules. A direct call needs no RIS configuration, skills, tracker
or directory layout. A project caller supplies verified task identity and
requirements and owns any authorized persistence or subsequent preparation.

When the task implements an accepted feature design, require its applicable
scope/version and acceptance evidence, existing contracts and test seams as
inputs. Check their currency against inspected code and any relevant shared
contract integration; a tracker status or document's presence is not acceptance.
For a standalone task use its accepted technical constraints, without inventing
a parent feature, slug or separate design document.

## Establish inputs and evidence

Identify the selected task's outcome, boundary and acceptance criteria; the
sources, versions and decision status of its requirements; applicable technical
and project constraints; and the code or interfaces available for inspection.
Distinguish binding requirements from proposals, observed code facts from
assumptions, and technical choices from changes to agreed scope. Inspect the
affected implementation and existing conventions when access is available;
record what was inspected and when or at what revision. Do not infer the current
code from a specification or from an earlier conversation. A caller's claimed
state without inspectable evidence remains attributed input, not an observation.

If task scope, a material criterion or its governing source is absent or
contradictory, identify the exact missing decision and affected work. Ask a
focused question when it can be resolved now. If code is unavailable, stale or
insufficient for a concrete design, identify what needs fresh inspection and
which choices and steps depend on it. Give only supported, independently useful
planning as **partial**; do not claim a ready plan based on imagined files,
interfaces or commands. Do not silently settle conflicting requirements or
enlarge the task to accommodate a preferred implementation.

## Develop and check the approach

1. Map each accepted criterion and material constraint to the affected behavior
   and, where observable, existing code. Separate already implemented behavior
   from required change. Keep exclusions and negative or quantitative limits
   intact. Plan this task, not the whole feature or an unrelated refactor.
2. Identify a viable implementation approach in the actual code and explain why
   it fits. Compare reasonable alternatives only when their choice materially
   changes the result; state the tradeoff and consequence of the chosen option.
   For a straightforward local edit, skip a ceremonial alternatives section.
   Treat design proposals as proposals, never as newly approved requirements;
    do not impose a preferred language, stack or project structure.
    Implement the accepted responsibility/state ownership, public interfaces
    and dependency directions in the local plan; do not reopen feature-wide
    architecture for convenience. Local reversible algorithms remain local.
    A material contract/design departure yields a bounded revision request:
    affected criteria, contracts, tasks and checks, decision owner and independent
    work still possible. Do not plan dependent implementation under that proposal.
3. Lay out an executable sequence with checkable intermediate results and the
   dependencies between steps. Mention concrete files, interfaces and commands
   only if inspection establishes them and the next implementer needs them;
   otherwise state the investigation still required. Adjust detail to the
   difficulty rather than filling a fixed template.
4. For every acceptance criterion state a fitting check, its expected observable
   outcome, and whether it can actually run in the available environment. Add
   applicable project checks and relevant failure/edge cases. Name uncovered
   criteria, unrun checks and residual risks explicitly; a proposed check is
   not a passed test. Recheck the approach and steps against current evidence,
   accepted requirements and exclusions before marking the plan ready.

## Handoff and stop

Return a self-contained technical plan with task identity and scope, requirement
sources and status, inspected code and freshness limits, supported approach and
consequences, ordered steps and intermediate checks, and criterion-to-check
coverage. Explicitly distinguish facts, decisions, assumptions and open
questions; include enough source substance or reachable references for an
implementer without this chat. State **ready** only if the material scope and
checks are traceable and the technical steps rely on sufficiently current code.
Otherwise label the result **partial/blocked**, identify precisely what needs
confirmation or inspection, and which steps cannot yet be executed reliably.

Do not save or approve a project document, update tracker state, claim or
create a worktree, change code, run an implementation, or start another skill.
Stop after the checked plan content and its limitations are handed off.
