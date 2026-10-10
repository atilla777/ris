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

1. Trace the goal to the people or systems whose behavior matters and the
   observable change sought; map its main end-to-end scenarios in the order
   their users experience them. Relate candidate deliverables to those changes
   rather than treating workflow phases as outcomes. Extract the minimum
   capabilities and constraints for a coherent MVP. Separate accepted scope
   from proposed scope; state exclusions, including postponed capabilities.
   Preserve quantitative limits and negative requirements exactly. Do not
   invent an actor, behavior, or feature when the inputs do not establish it.
2. Select a small **first verifiable end-to-end slice** across the scenario,
   from a user action to an observable outcome, or a bounded improvement of an
   existing path. Explain what it proves and what it does not. Avoid a
   horizontal sequence of infrastructure layers unless a specific dependency
   justifies it.
3. Propose only as many finishable epics as distinct outcomes or bounded
   uncertainties justify; **one epic is valid** when it covers a coherent
   goal. For each give the useful outcome, boundary and significant exclusions,
   observable completion condition, and the scenarios it covers. Test each
   boundary: if a proposed epic only prepares, publishes, or verifies the same
   delivery as another, consider one end-to-end epic with these as internal
   work instead; separate them only for a justified independent result. An
   investigation epic must resolve a named uncertainty with a verifiable
   conclusion. Describe the nearest epic enough to refine next; keep farther
   epics coarser. Name a concrete nearest outcome when supported by the inputs;
   if choosing the feature is a material open decision, identify it rather
   than inventing one. Do not pre-split future work into implementation tasks.
4. Explain only necessary prerequisite relationships: which prior outcome
   enables which later outcome. Distinguish dependency from priority, check
   for cycles and for reliance on unconfirmed work, and propose an order that
   tests important assumptions early. Existing verified results need not be
   re-planned. Recommend the next epic with a reason and note whether it is
   ready for refinement or blocked by an input; recommendation is not a start.
5. Cross-check every required scenario, MVP constraint, and the first end-to-end
   result against the epic outcomes. Explicitly identify uncovered requirements,
   unsupported epic boundaries, hidden exclusions, vague completion tests,
   unjustified dependencies, or cycles; revise the proposal or mark the
   specific gap. Ask whether the same single delivery has been split merely
   to increase the epic count. A list of titles or technical layers alone is
   not a complete roadmap.

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
