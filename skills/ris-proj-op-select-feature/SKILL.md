---
name: ris-proj-op-select-feature
description: >-
  Recommend the next small verifiable feature within a current project roadmap
  epic, or explain why selection is blocked. Use when choosing what feature to
  pursue next or whether to continue one already started, with light linked-source
  currency and shared-contract checks; not for planning
  epics, refining an unclear epic, specifying a feature, creating tasks, or
  implementing work.
---

# Select the next feature

Own a **read-only recommendation**, not a feature record or an
accepted specification. This is one RIS project skill: its evidence and result
depend on the selected project's roadmap, actual tracker, work in progress and
rules; no independently useful RIS-free base result is required. Do not start
another lifecycle operation as a side effect.
Recommend a direction from minimum sufficient facts; do not certify execution
readiness. The executing owner checks current inputs, acceptance, ownership,
permissions and write guarantees. Unknown facts remain explicit, not evidence
that work is available; they block only the conclusion that needs them.
The semantic execution role is `feature-selection` when a caller assigns this
work to a subagent. The caller verifies the configured agent's availability
and actual launch and supplies bounded inputs; a role name alone does not
provide isolation or a model. **Direct invocation** runs in the current agent
without requiring `execution` or claiming isolation.

## Prepare and establish the epic

Establish the target project/root, accepted goal, any explicitly confirmed epic
ID and the user's requested scope. Ensure installed `ris-proj-lib-common` is available;
apply its rules and read its conditional resources before governed actions.
Use installed `ris-proj-op-resolve-context` **with its configuration resource** to resolve the
selected project's `sources.rules`, `sources.product`, `sources.specs` and
`adapters.tasks.skill` as needed. Inspect its status, provenance, paths,
diagnostics and permissions. Select applicable documents by relevance and
acceptance, not by directory membership; read the project's instructions and
rules. In RIS itself, use the root `ris.yaml` rather than a historical roadmap
pointer or the local development queue as the configured task workspace. In a
different project, use that project's own selected configuration and rules.
Do not confuse a planned skill or target behavior with an implemented one.

Load and **apply the selected available task adapter** for read operations;
confirm it supports the needed epic, child/task and typed dependency reads in
the selected workspace. `tasks` v1 includes optional feature-task and direct-child
reads alongside roadmap epic and blocking reads; verify the selected adapter's
actual operations and guarantees rather than inferring support from v1. With
`ris-proj-adapter-beads-tasks`, have the adapter verify its supported CLI version,
workspace and responses. Use confirmed-ID epic reads, relevant task/child reads
and typed `blocks` reads; require epic listing only for discovery or a concrete
cross-epic question. Read related tasks including closed records where needed to
identify started, completed or redundant work. A
configured name alone is not availability. If a required source,
resource, adapter or tracker is inaccessible, report which inference is blocked;
do not guess from a file, a default list, or direct tracker storage.

An explicitly confirmed epic ID takes precedence: verify its type, goal
membership, status, `blocks` edges and applicability; never infer an ID from a
title. Read that epic directly, its relevant candidates/started work and blockers;
do not dump all epics/tasks unless an explicit absence, redundancy or cross-epic
conflict question needs that coverage. Without an ID, discover compact suitable
epic identities for the accepted goal, then read candidate content and relevant
typed blockers as needed. Use the adapter's native compact forms: for Beads,
`list --all --limit 0 --type epic --brief --json` for discovery and exact
`show <id> --brief-deps --json` for necessary own content. Omitted brief fields
are unknown, not empty; absence claims still need complete relevant coverage.
Choose the sole unfinished epic with no known material blocker if there is one.
If several are suitable, follow an explicitly
recorded **still applicable** next-epic recommendation only if unambiguous;
otherwise show the suitable choices and ask the person which epic to use. Neither
list order nor numeric priority establishes sequence. A blocked, completed,
unconfirmed or ambiguous epic cannot support a next-feature recommendation:
give the specific reason and the next resolution action. Suggest epic
refinement only when its outcome or boundary is too unclear to choose a
feature; epic size alone is not a reason. Do not redo goal-to-epic planning.
When invoked as a subagent, return the evidenced choices and the needed
human decision to the caller instead of opening a separate user dialogue;
on direct invocation, ask the person in the current dialogue.

## Compare bounded feature candidates

Read the chosen epic's outcome, boundary and completion conditions, relevant
accepted concepts/specifications and rules, related open and completed records,
dependencies and started work. Inspect only the relevant parts of the code or
other current-state evidence needed to avoid recommending completed, redundant
or blocked work; do not design each candidate's implementation. Identify any
existing feature specification and its known status without deciding whether
it is sufficient or whether another interview is necessary.

Keep a **light boundary/currency check** against relevant current source/code and
known related work: obvious responsibility/state overlaps, undefined/incompatible
shared interfaces and boundary-affecting risks. Use freely structured author
material as desired-product evidence, not a feature list derived from headings;
do not impose global IDs or design every candidate. Shared files alone are not a
conflict, and a proposed design is not accepted.

Expand historical baselines, design acceptance and linked evidence only for a
named material question that can change the recommendation, such as changed
behavior or competing shared contracts. Follow actual source/AC/task/test/design
links within that scope; never guess a slug or infer coverage from test presence.
Distinguish editorial from behavioral deltas. Missing baselines leave currency
unconfirmed, not automatically current or stale, and need not prevent an
independently justified direction. For a new project use minimal architecture
evidence, not full future design. On a known material conflict
identify affected features/tasks/contracts, propose coordination/integration owner,
common version to agree and necessary blocked → prerequisite relationships. Do
not call dependent work available until those decisions are evidenced; independent
candidates remain selectable. Distinguish a material product change (requirements
owner), substantive design change (focused design revision) and changed global
invariant (architecture authority) from a local implementation choice. Preserve
unaffected accepted scopes. Do not revise/accept any document or add tracker links.

First assess whether an already-started feature remains relevant, has no known
material blocker and
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
When a subagent needs the person's feature choice, return the bounded options
to the caller and stop until it supplies the confirmed choice; do not silently
accept the recommendation on the person's behalf.

## Return a usable recommendation and stop

Distinguish proposal from the person's acceptance. For an evidenced choice,
give the confirmed epic ID and outcome; recommended or person-chosen feature
and its verifiable result; reasons and material alternatives; source references,
related work and known statuses; open questions and the next required result.
Link a found specification with its **known** status, leaving its suitability
and any interview to the specification owner. Give a usable subject/locator and
enough evidence for this choice, without a universal execution handoff. If execution
is actually transferred to another actor/session, apply common's detailed handoff
rules. For a blocked choice, include only
confirmed facts, the concrete reason and the next action; do not invent an ID
or a feature. Verify references and distinguish observed evidence from
proposals. No tracker or file mutations, claims, assignments or status changes
are permitted even after agreement with a feature.
Include the material input versions, decisions, addresses and unknowns required
by common's applicable result rules, without reconstructing history merely to
fill the response. Report the light boundary check and any recommendation-changing
source/contract issue, affected scopes, proposed coordinator/prerequisite and
independent work. Versions and AC/task/test/design links belong when the actual
comparison or conflict depends on them; do not populate unrelated fields or hide
material gaps. Mark uninvestigated acceptance/channel facts unknown rather than
treating them as passed. Explain if started work loses preference; absence of a
version is uncertainty, not proof it is obsolete. If unavoidable material ambiguity
prevents a justified choice, ask one focused question (or return it to the caller).
The recommendation grants no readiness or authority.

Once the person accepts a feature, identify working out its specification as
a possible separate, explicitly authorized next result in plain terms. Do not
start an interview, save a specification, create a task or launch implementation
here. Stop after the checked recommendation or an honest blocked handoff.
