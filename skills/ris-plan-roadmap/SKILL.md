---
name: ris-plan-roadmap
description: >-
  Create or update a project's goal-level roadmap as verified tracker epics,
  or propose it without writing. Use for project MVP outcomes, epic boundaries
  and dependencies; not for a single feature's tasks, raw Beads operations,
  initializing a tracker, or implementing an epic.
---

# Project roadmap

Own the **combined project result**: selected accepted inputs, a checked
goal-level proposal, reconciliation with all existing tracker epics and a
verified saved roadmap when authorized. `ris-plan-roadmap-base` owns the
portable proposal method; this skill owns project selection, integration and
the adequacy of the persisted whole. Do not duplicate its planning algorithm.

## Prepare the operation

Establish the selected project/root (and explicit primary root if shared paths
are needed from a worktree), chosen goal and evidence of its acceptance,
`mode: create|update`, and precise write scope. An explicit proposal-only
request has `write: false`; without permission default to no write. Do not
infer goal acceptance from a file's presence or infer present capabilities
from a target vision. An absent accepted goal permits a labelled draft goal,
not a claim of a complete accepted roadmap. Ask for a missing mode before a
write; never turn an `update` into a `create` or vice versa.

Ensure the installed `ris-common` is available and apply its rules and
conditional resources before their governed actions. Use installed
`ris-context` and its configuration resource for **this project operation**:
resolve applicable `sources.concepts`, `sources.rules`, `sources.specs` when
needed, and `adapters.tasks.skill` for tracker operations. Check the returned
status, provenance, paths and scope; a configured adapter is not an available
adapter. Select the actual applicable accepted high-level documents from the
prepared directories, explicit inputs and their links; read project rules,
relevant specifications and evidence of the current state. Do not require
OKF, all documents in a directory, or a pre-existing output directory. If
accepted sources conflict, identify the affected content and stop its write.

Ensure installed `ris-plan-roadmap-base` is available; provide the selected
high-level specification, goal, observed starting state, constraints and,
for update, existing epics and confirmed accomplishments. Apply its method
to obtain a bounded proposal and gaps, not merely a loaded dependency. The
base does not receive project configuration as a required input. Coordinate
one dialogue across dependencies; resolve material decisions before writing.
If essential input or the base is missing, report the independent result and
block claims depending on it.

## Reconcile before any write

For tracker reads and writes, load the **selected and available** task adapter
and apply its actual contract. With `ris-beads-tech`, use its full all-status,
unlimited epic selection, confirmed-ID reads and typed-edge inspection in the
selected workspace. Its instructions govern `bd` calls, safe retries,
permissions and concurrency; never bypass it with direct storage edits or a
fallback roadmap file. If the adapter is missing, incompatible or the
workspace is unavailable, no tracker write is possible; an explicitly
requested proposal without writing can still be returned as **unsaved**, with
unknown tracker state identified. No implicit `bd init`.

Determine the full applicable set, **including closed epics**. Match by
confirmed IDs, a stable goal/roadmap membership reference in saved content
or tracker metadata, and meaning against the selected accepted goal; a title
or unverified uniqueness of a label alone is insufficient. Check related
records and links for scope and conflicting ownership. If existing records
cannot be enumerated completely or ownership/identity is ambiguous, stop
before writing; do not invent IDs, silently adopt another roadmap's epics,
or treat an ambiguous match as absence. Agree a stable per-goal and per-epic
identity for new records and include the goal, accepted input references,
outcome, boundary/exclusions, completion criterion and covered scenarios in
their saved content or confirmed metadata. Preserve that identity on update.
References must be resolvable by the recipient; a link to an inaccessible
document does not carry essential decisions. No second mutable roadmap file.

`create` requires a confirmed absence of that goal's roadmap across open and
closed records. A matching existing epic is a conflict, not permission to
create another. `update` requires an existing, unambiguous goal roadmap; an
empty or unidentifiable set is not a new create. Preserve existing IDs,
verified accomplishments, closed outcomes and closed-epic content. New
necessary epics may be proposed on update, but never retroactively rewrite a
closed epic, delete it, close it or change its status/assignee. Mark a
contradiction with an accepted closed result for resolution instead of
rewriting history. Differentiate a proposed new outcome from a confirmed
existing one and identify exactly which open epics and links need change.

## Save and verify only when authorized

Before writing, check the base proposal for unresolved blocking gaps and
check the **combined** result: goal scenarios and MVP boundary/constraints,
exclusions, first verifiable end-to-end result, each epic's useful outcome,
boundary and completion condition, scenario coverage, justified acyclic
blocking dependencies and order, and a reasoned next-epic recommendation.
Nearest epic should be actionable for refinement; farther ones may be coarser.
Do not silently drop a required scenario or weaken numerical/negative
requirements. Check that every proposed epic has a justified independent
outcome or bounded uncertainty: one epic may be sufficient; phases of one
delivery do not become separate epics just to reach a target count. If
coverage or identity cannot be demonstrated, stop dependent writes and return
the proposal with the specific gap.

Before any tracker mutation, show the proposed epic boundaries, outcomes,
exclusions, completion conditions, first end-to-end slice, and material
dependencies to the person and obtain agreement to the **specific breakdown**.
For `update`, show and agree material changes to existing outcomes, boundaries,
exclusions, completion conditions, dependencies or order, and any new epics;
do not demand renewed acceptance of unchanged content. A generic
"create/update the roadmap" request or write permission does not approve the
breakdown. An explicit instruction to plan the epics **without consulting the
person** waives this agreement step, even when the person did not supply the
breakdown; a specific breakdown already explicitly accepted by the person
does not need re-approval. Neither exception supplies write permission,
accepted inputs, a mode, or adapter guarantees. If agreement is needed but
not obtained, return the unsaved proposal with `changes: []` and stop. If a
material change to the agreed breakdown becomes necessary before writing,
present the changed part again unless the explicit waiver applies. Do not
hold a tracker lock while waiting for a decision.

Translate agreed (or explicitly consultation-waived) changes into bounded
adapter operations on confirmed IDs: create or update only roadmap epics in
scope, and add only required `blocks` edges in the correct direction (blocked
epic → prerequisite). Do not use a
parent-child edge as a blocking edge, create tasks or modify unrelated
records. Confirm the adapter's writer/quiescence guarantee for noncommutative
content and no-duplicate creation; if unavailable, stop with `conflict`
unless the caller **explicitly accepts** the adapter's limited best-effort
guarantee and its duplicate/lost-update risk. Do not present a mere
read/write/read sequence or `external-ref` as a lock. Re-read relevant
records and edges before each mutation, compare with expected state, execute
one bounded action, and verify the returned ID, content, status and links by
fresh reads before proceeding. An uncertain response requires full
reconciliation before any retry; never blindly repeat a create. On a failed
or partial operation re-read all affected records, report confirmed changes
and unsaved parts, then **stop before further writes**, including link edits.
No automatic rollback, close, assignment or launch of the recommended epic.

Finally re-enumerate the goal's complete open and closed set, re-read saved
records and typed dependencies, and compare the **persisted whole** with the
accepted goal and agreed or explicitly consultation-waived proposal: content,
coverage, first result, exclusions, unchanged closed accomplishments, IDs,
status, links, order and recommendation.
If the check is incomplete, do not claim a saved complete roadmap. Report
`ok|blocked|conflict|error`, mode, project, goal/input acceptance, actual
confirmed IDs and changes (including partial changes), breakdown agreement or
explicit waiver, evidence and its limits, unsaved proposal/gaps and the
recommended next epic with readiness.
Without write permission, return only a labelled unsaved proposal and
`changes: []`; even a complete proposal is not an accepted or persisted
roadmap. Stop at the roadmap: no feature decomposition, implementation,
tracker initialization, Dolt setup or transition of source of truth.
