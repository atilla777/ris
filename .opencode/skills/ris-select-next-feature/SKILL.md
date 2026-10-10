---
name: ris-select-next-feature
description: >-
  Recommend the next small verifiable feature within a current project roadmap
  epic, or explain why selection is blocked. Use when choosing what feature to
  pursue next or whether to continue one already started; not for planning
  epics, refining an unclear epic, specifying a feature, creating tasks, or
  implementing work.
---

# Select the next feature

Own a **read-only recommendation and handoff**, not a feature record or an
accepted specification. This is one RIS project skill: its evidence and result
depend on the selected project's roadmap, actual tracker, work in progress and
rules; no independently useful RIS-free base result is required. Do not start
another lifecycle operation as a side effect.

## Prepare and establish the epic

Establish the target project/root, accepted goal, any explicitly confirmed epic
ID and the user's requested scope. Ensure installed `ris-common` is available;
apply its rules and read its conditional resources before governed actions.
Use installed `ris-context` **with its configuration resource** to resolve the
selected project's `sources.rules`, `sources.concepts`, `sources.specs` and
`adapters.tasks.skill` as needed. Inspect its status, provenance, paths,
diagnostics and permissions. Select applicable documents by relevance and
acceptance, not by directory membership; read the project's instructions and
rules. In RIS itself, use the root `ris.yaml` rather than a historical roadmap
pointer or the local development queue as the configured task workspace. In a
different project, use that project's own selected configuration and rules.
Do not confuse a planned skill or target behavior with an implemented one.

Load and **apply the selected available task adapter** for read operations;
confirm it supports the needed epic, child/task and typed dependency reads in
the selected workspace. `tasks` v1 standardizes only roadmap epic and blocking
reads: child/task reads remain adapter-specific and this feature selector is
not yet interchangeable with an arbitrary tasks v1 adapter. With
`ris-beads-adapter`, have the adapter verify its supported CLI version,
workspace and responses. Require the `tasks` v1 all-status complete epic list,
confirmed-ID epic reads and typed `blocks` reads. Read related tasks including
closed records using the selected adapter's own task-read contract and complete
selection where applicable; this operation is not part of `tasks` v1. A
configured name alone is not availability. If a required source,
resource, adapter or tracker is inaccessible, report which inference is blocked;
do not guess from a file, a default list, or direct tracker storage.

An explicitly confirmed epic ID takes precedence: verify its type, goal
membership, status, `blocks` edges and applicability; never infer an ID from a
title. Without an ID, inspect the full current set (including closed) and
typed blocking links for the accepted goal. Choose the sole unfinished,
unblocked epic if there is one. If several are ready, follow an explicitly
recorded **still applicable** next-epic recommendation only if unambiguous;
otherwise show the ready choices and ask the person which epic to use. Neither
list order nor numeric priority establishes sequence. A blocked, completed,
unconfirmed or ambiguous epic cannot support a next-feature recommendation:
give the specific reason and the next resolution action. Suggest epic
refinement only when its outcome or boundary is too unclear to choose a
feature; epic size alone is not a reason. Do not redo goal-to-epic planning.

## Compare bounded feature candidates

Read the chosen epic's outcome, boundary and completion conditions, relevant
accepted concepts/specifications and rules, related open and completed records,
dependencies and started work. Inspect only the relevant parts of the code or
other current-state evidence needed to avoid recommending completed, redundant
or blocked work; do not design each candidate's implementation. Identify any
existing feature specification and its known status without deciding whether
it is sufficient or whether another interview is necessary.

First test whether an already-started feature remains relevant, available and
contributes to the nearest verifiable epic outcome. Prefer finishing it over
starting something new when these conditions hold; otherwise explain why not.
If no prior feature list exists, derive a small set of candidates (usually
1–3 when evidence permits) from the epic and observed state, without inventing
tracker entries. Compare useful outcome, small verifiable scope, dependencies,
continuity and significant risks. Recommend the nearest justified slice,
give reasons and meaningful alternatives, and mark boundaries that feature
specification may refine. If the person chooses an alternative, assess it by
the same criteria, state the tradeoff and hand off **their** choice without
rerunning the selection. If none is defensible, identify concrete missing
evidence or blockers and a next action instead of fabricating a feature.

## Return a usable handoff and stop

Distinguish proposal from the person's acceptance. For an evidenced choice,
give the confirmed epic ID and outcome; recommended or person-chosen feature
and its verifiable result; reasons and material alternatives; source references,
related work and known statuses; open questions and the next required result.
Link a found specification with its **known** status, leaving its suitability
and any interview to the specification owner. Make the handoff sufficient for
a new conversation without this chat. For a blocked choice, include only
confirmed facts, the concrete reason and the next action; do not invent an ID
or a feature. Verify references and distinguish observed evidence from
proposals. No tracker or file mutations, claims, assignments or status changes
are permitted even after agreement with a feature.

Once the person accepts a feature, **offer** to work out its specification as
a separate, explicitly authorized step; name that next result in plain terms.
`ris-specify-feature` may be mentioned as an optional pointer if available,
but it is not a runtime dependency and need not be installed. Do not start
its interview, save a specification, create a task or launch implementation
here. Stop after the checked recommendation or an honest blocked handoff.
