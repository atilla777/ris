---
name: ris-plan-roadmap-base
description: >-
  Draft and check a bounded, portable project roadmap proposal from an explicitly
  supplied high-level specification, chosen goal, and observed starting state.
  Use for goal-to-epic planning or revising proposed epics without a tracker;
  not for decomposing one feature into implementation tasks or persisting epics.
---

# Plan a project roadmap proposal

Own the content and completeness of a proposed roadmap, not its storage or
project integration. Work directly from the supplied material and applicable
rules of the actual project. This skill requires no other RIS skill, `ris.yaml`,
tracker, or RIS directory. A caller that needs project document discovery,
existing tracker records, or saved epics must provide the relevant inputs and
own that integration and the final persisted result.

## Inputs and readiness

Identify the high-level specification and its acceptance status, the selected
goal and its acceptance status, the supported starting state (what already
works or is done, with evidence), applicable constraints, and the scope of the
requested proposal. For a revision, take any existing proposed epics and
confirmed accomplishments as inputs; retain their identity and completed
results rather than rewriting history. Do not infer acceptance from a document's
existence, or infer the present state from a future vision. Separate observed
facts, accepted requirements, proposals, assumptions, and unknowns.

If the accepted goal is missing, offer a **draft goal** when the supplied
material permits, labelled unaccepted; do not present a goal-dependent roadmap
as agreed. If a needed specification, material decision, or reliable starting
state is missing or contradictory, identify the affected scenarios or epics,
ask for the decision or evidence when necessary, and hold the dependent claim
of completeness. Independent parts may still be proposed with explicit gaps.
Do not invent requirements to fill missing inputs.

## Method

1. Extract the goal's main end-to-end scenarios and the minimum capabilities
   and constraints needed for a coherent MVP. Separate accepted scope from
   proposed scope; state exclusions, including postponed capabilities. Preserve
   quantitative limits and negative requirements exactly.
2. Identify a small **first verifiable end-to-end result** from a user action
   to an observable outcome, or a bounded improvement of an existing path.
   Explain what it proves and what it does not. Avoid a horizontal sequence of
   infrastructure layers unless a specific dependency justifies it.
3. Propose a small number of finishable epics to reach the chosen goal. For
   each give the useful outcome, boundary and significant exclusions, observable
   completion condition, and the scenarios it covers. Describe the nearest
   epic enough to refine next; keep farther epics coarser. An investigation
   epic must resolve a named uncertainty with a verifiable conclusion. Do not
   pre-split the entire future into implementation tasks or decide every design.
4. Explain only necessary prerequisite relationships: which prior outcome
   enables which later outcome. Distinguish dependency from priority, check
   for cycles and for reliance on unconfirmed work, and propose an order that
   tests important assumptions early. Existing verified results need not be
   re-planned. Recommend the next epic with a reason and note whether it is
   ready for refinement or blocked by an input; recommendation is not a start.
5. Cross-check every required scenario, MVP constraint, and the first end-to-end
   result against the epic outcomes. Explicitly identify uncovered requirements,
   unsupported epics, hidden exclusions, vague completion tests, unjustified
   dependencies, or cycles; revise the proposal or mark the specific gap. A
   list of titles or technical layers alone is not a complete roadmap.

## Result and stop

Return a proposal containing the goal and input/acceptance status, evidenced
starting state, scenarios and MVP boundary, exclusions, first end-to-end
result, bounded epics with their outcomes and completion conditions, coverage
and gaps, justified dependencies and order, open decisions, and recommended
next epic. Clearly label what is proposed rather than accepted, and say whether
the content is complete against available accepted inputs or which claims are
blocked. If acceptance or evidence is insufficient, return the useful partial
proposal with its limits instead of claiming full coverage.

This skill does not create or update files, tracker records, links, statuses,
assignments, or tasks; it neither approves the proposal nor starts another
stage. The caller may use the checked content for a separately authorized
project operation. Stop after reporting the checked proposal and its gaps.
