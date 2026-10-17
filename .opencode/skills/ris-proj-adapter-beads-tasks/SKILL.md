---
name: ris-proj-adapter-beads-tasks
description: >-
  Serve the tasks v1 and optional feature-record/1 adapter roles and verify
  bounded Beads operations via bd: read/list epics and tasks, ordinary native bug
  read/list/create/update and protected investigation/disposition, create/update by
  confirmed ID, manage links, claim, conditionally update feature evidence,
  ordinary bug execution claim/snapshot/fix-completion, explicitly close, and
  separately publish authorized Dolt history. Use for
  bounded tracker operations, not for planning a feature or configuring remotes.
---

# Beads tasks adapter

Own only the requested tracker operation and its verified result. The caller
owns the choice of records, required content, completeness of mandatory work,
and authorization. This is one technical skill, not a portable planning method
or a project wrapper: `bd` operations have no independent RIS-free methodology
to split out. Ensure installed `ris-proj-lib-common` is available and apply it (and its
conditional resources before their respective actions). If project settings
must be resolved, use installed `ris-proj-op-resolve-context` and its configuration resource
for that preparation; otherwise take the explicit project root from the caller.
Neither loading a dependency nor `adapters.tasks.skill` grants write access.

## Role contract: tasks v1

Implement the roadmap portion of the shared `tasks` version 1 contract:
`tasks.epics.list`, `tasks.epics.read`, `tasks.epics.create`,
`tasks.epics.update`, `tasks.blocks.list`, `tasks.blocks.add`,
`tasks.blocks.remove`. These names describe semantic operations, **not** CLI
commands. Report this version, supported operations and guarantees to the
caller before dependent writes. For all-status, unlimited epic selection use
`bd list --all --limit 0 --type epic --json`; for an exact ID use `bd show
<id> --json`; for typed directed edges use `bd dep list <id> --json`.
The caller owns the goal and membership identity, acceptable content, scope,
and required guarantees. Return actual ID, issue type, status, content and
applicable `blocks` edges with fresh-read evidence; an incomplete list cannot
establish absence. `bd`'s status values are tracker data, not RIS result codes.

Guarantees by operation: list/read/list-blocks provide complete inspected
results or an explicit failure; create is best-effort and cannot promise unique
external references under concurrency without a proven uniqueness mechanism;
update uses fresh expected values, targeted fields and applicable native guards;
blocks.add
checks endpoints, direction and cycles and verifies the resulting edge;
blocks.remove requires the exact selected edge, authorized scope, and a
fresh check of that exact edge and result read-back. Neither read/write/read nor
row guards promise protection against every concurrent replacement. Apply
`references/concurrency.md` before dependent mutations. Ordinary operations need
no manual pause, mandatory global lock or graph-wide transaction. An explicitly
required stronger guarantee unsupported by the tool blocks only its dependent write.

Also implement the optional feature-task operations of `tasks` v1:
`tasks.items.list`, `tasks.items.read`, `tasks.items.create`,
`tasks.children.list`, `tasks.dependencies.list`, `tasks.dependencies.add`.
This is an additive capability set, not a change to roadmap operations or a
claim that any v1 adapter automatically supports feature tasks. Report the
specific supported operations and guarantees; a caller requiring feature-task
work must check each before a dependent write. The common record type is
`task` for the feature and its children; the feature's parent is an `epic`.
Neither task status nor `bd`'s `feature` issue type substitutes for this type.

For `items.list`, use `bd list --all --limit 0 --type task --json`, covering
closed tasks and inspecting ID, type, parent, stable key, spec link and content;
do not rely on a default-limited or open-only search for absence. For
`items.read`, require exactly one matching ID and `issue_type: task` from
`bd show <id> --json`. For `children.list`, use `bd list --parent <feature-id>
--all --limit 0 --json`, check every child's `parent` and type; explicitly
  distinguish an empty complete set from an error. For `dependencies.list`,
  read `bd dep list <task-id> --type blocks --direction=down --json` for
  blockers, or `--direction=up` for tasks blocked by that ID; normalize each
  returned edge to blocked → blocker and distinguish empty from an error;
for `dependencies.add`, use `bd dep add <blocked-task-id>
<blocker-task-id> --type blocks --json` with cycle checks enabled. Verify
typed direction after the call. `parent-child` is membership, not a `blocks`
edge. An unsupported version, operation, full-selection guarantee or required
concurrency guarantee blocks the dependent write, regardless of the existence
of another `bd` command. Claim, complete, reparent, content update and edge
removal remain tool-specific unless covered by the original roadmap operations.

## Tool-specific ordinary standalone work

Also support bounded ordinary standalone task/container create/reconcile,
source-link update, child/link operations, result persistence and exact close.
Read `references/standalone.md` before these operations. These are **Beads-specific
capabilities**, not expanded `tasks` v1 create semantics or feature-record/1.
Report each requested capability and its actual predicate-specific guarantees;
missing required support blocks that write. Ordinary reads and claim retain the
main contract. An absent or invalid feature payload never selects standalone.

Also advertise **ordinary native bug read/list/create/update**, independently of
`tasks.items.*` and feature-record/1. Read `references/standalone.md` for this
bounded capability before use. Exact reads require the caller's expected type;
bug lists cover every status without a limit. Creation preserves an unconfirmed
message with stable retry identity; supplementation uses native append preserving
foreign content. Execution capabilities are advertised separately below, never
through feature operations.
Legacy ordinary task originals retain their type and use
only explicitly authorized ordinary task updates.

For bug investigation additionally advertise report/acceptance persistence,
nonblocking duplicate relation, read-only children/blocker inspection for
disposition, and separate exact not-bug/duplicate close **only under**
`references/investigation.md`; read it before those operations. This resource
requires real report-content protection, not ordinary fresh compare/write/read;
unsupported protection blocks its dependent replacements while research remains
useful. Disposition closure resolves the message, not fix acceptance. It does not
extend bug claim, composition or execution completion; ordinary task and feature
completion retain their existing acceptance/publication gates.

For ordinary native bug execution advertise exact typed reads, complete children/
directed-blocker reads, native claim, full recoverable execution-input notes
snapshot append/read/reconcile, accepted-design source-link append, fix-result persistence and separate exact
fix-completion under `references/bug-execution.md`. Read it before those operations.
It composes main Claim/Complete and concurrency/publication owners, not a second
algorithm. Fix-completion requires real criteria/check/review and required Git
publication, separately from investigation disposition. Feature APIs stay task-only;
this does not add bug composition or automatic bug selection.

## Optional feature-record capability

Separately advertise `tasks.feature-record/1` with `tasks.features.read`,
`tasks.features.update`, `tasks.features.record-verification`, and
`tasks.features.complete` **only under the guarantees in**
`references/feature-record.md`. Read that resource before any of these four
operations **or** `tasks.items.create` when the caller supplies an initial
feature-record block; it is not needed for ordinary roadmap, feature creation
without that block, claim, or tool-specific task completion. These are not
implicit `tasks` v1 operations.
Baseline `bd` 1.3.1 has no CLI-wide revision CAS; select protection for the
actual operation through `references/concurrency.md` and the feature-record
resource, rather than requiring a manual window for every write. A row-only
guard does not protect all acceptance evidence or structure. The caller owns acceptance and completeness decisions; this
adapter checks and persists only the specifically authorized result.

## Inputs and boundary

Require the chosen project/workspace, exact operation, record IDs for existing
records, desired fields or edge direction, actor for a claim, allowed write
scope, and expected outcome. For creation require the caller's approved type
(`epic` or `task`, or `bug` for the advertised ordinary capability), title/content and a distinguishing stable reference or
other agreed identity evidence for safe retry; for completion require the
caller's explicit confirmation of full mandatory scope and reason. Never guess
an ID from a title. Check `bd version` for the supported 1.3.1 behavior and
`bd where`/`bd context` in the selected project; an uninitialized, wrong,
unavailable, or read-only workspace blocks dependent writes. Use `bd -C
<project-root>` only for an existing Beads project (initialization needs the
working directory). Do not use `--global`, `--db`, or ambient workspace fallback
to work around a missing project. All commands below refer to that selected
workspace. Request `--json` for structured results, check exit code AND body.
Pass IDs, titles, and body as separate safely quoted arguments, not interpolated
shell code; use `--body-file` when text must not be exposed as a command argument.
Never edit `.beads/` directly. Read-only requests may use `--readonly`; writing
needs explicit authorization even if the CLI accepts it.

## Read and reconcile

- `bd show <id> --json` returns an array; require exactly one matching ID.
  For ordinary typed reads also require the caller's expected `issue_type`;
  registration creation/read-back expects `bug`, never a feature-task substitute.
  It includes `status`, `issue_type`, `parent` when present, dependencies and
  sometimes `revision`. An output revision is usable as CAS only when the
  installed command/backend explicitly supports that token and its scope.
- `bd create --json` returns an object with `id` in the checked version;
  `bd update --json` returns an array. Validate the actual response rather than
  applying one assumed shape to every command. `show`/`dep list` edges may use
  related-record `id` plus `dependency_type`; all-state `list` edges may use
  `issue_id`, `depends_on_id`, `type`. Normalize using the queried endpoint and
  explicit direction. Do not confuse these with native Dolt table columns
  or silently treat an unknown edge shape as an empty set.
- `bd list --all --limit 0 --type epic --json` and likewise `--type task`
  or ordinary `--type bug`
  provide untruncated sets including closed records. `bd list` defaults to
  50 and excludes closed; `--status all` is not its all-status flag. Apply
  caller filters only when they preserve required coverage; validate type,
  ID and scope on results. `bd list --parent <parent> --all --limit 0 --json`
  enumerates direct children without the default 50-row limit; repeat for
  descendants when completion requires them. `bd children <parent> --json`
  is useful for inspection but does not expose an explicit unlimited flag.
  `bd dep list <id> --json` and `bd show <id> --json` inspect typed edges;
  distinguish `parent-child` from `blocks`. A clean empty array is not an error.
  If a query fails or is truncated, do not claim completeness. A list filtered
  to one parent cannot exclude duplicate feature tasks under a different
  parent; search the entire relevant task scope before feature creation.

Before every mutation, re-read affected IDs and relevant children/edges;
compare with the caller's confirmed expected state. On unexpected differences
return `conflict` without writing. After a command, independently read the
record(s), children/edges or full selection as applicable and compare requested
fields, status, type and direction. A zero exit or a JSON ID alone is not proof
of the full intended outcome. Report actual IDs and state, including unrelated
changes seen. For a nonzero, malformed, or ambiguous response, inspect actual
state before any retry. If identity or effect cannot be established, stop;
never blindly recreate, reparent, remove an edge, or close.

## Mutations (one bounded action at a time)

- **Create:** search all relevant records (including closed) for the caller's
  stable identity and compare content/parent; for a feature also search slug
  and spec association across all project tasks, using the feature-record
  resource when supplied. An exact confirmed prior creation
  returns the existing ID, ambiguous matches are a `conflict`. An authorized
  creation defaults to best-effort without a separate concurrency-risk question:
  `bd` does not enforce unique external references, so concurrent creators can
  still make duplicates. Do not claim a no-duplicate guarantee from the search
  and read-back. If the caller explicitly requires that guarantee, require a
  proven native uniqueness mechanism covering all relevant creators;
  without it report the exact limitation and stop `conflict`, without a pause request. Run `bd create
  --type epic|task --title ... --description ... --acceptance ... --json`
  with only supplied fields (optional `--external-ref` or `--spec-id` for
  identity; neither is a uniqueness constraint). Prefer `--parent <id>` for
  a child only after checking the parent. Extract the returned ID, `show` it
  and verify content and parent, then repeat the full all-state identity search
  (including feature key/slug/spec) to detect concurrent collisions. Return
  `conflict` with persisted IDs for a duplicate; never silently pick one.
  On uncertain creation, re-list all records
  and reconcile the stable identity before another attempt. With no reliable
  identity evidence, do not retry an ambiguous create: `conflict`. For common
  `tasks.items.create`, require a confirmed open epic as parent of a feature
  task, or a confirmed open feature task as parent of a direct child. Require
  caller-approved task content, a stable retry key and expected absence; for
  the feature also require the exact accepted-spec link and a verifiable
  address of the acceptance decision (do not infer acceptance from a file or
  `--spec-id`). Persist that address in the approved description, or verify it
  is accessible in the linked specification, and reread it on return/retry.
  If the evidence cannot be retrieved or does not match the accepted version,
  report `blocked` rather than declaring acceptance. Use
  `--type task --parent <id>` with supplied content and `--external-ref` for
  the stable key; use `--spec-id` only when the caller supplied it and retain
  the exact link in the approved description or other readable field. Scope
  child keys to their feature parent and feature keys to their epic/goal; a
  globally reused raw key is insufficient. On retry, compare key, type,
  parent, content, spec link and acceptance evidence address for a feature,
  including all-status records. Reuse only an
  exact match; changed content, moved parent, closed parent or multiple matches
  are `conflict`, not permission to update. Verify the new child's `parent`,
  typed `parent-child` edge (child → parent), parent direct-child selection,
  and the reread content. For a feature verify the epic and the same membership.
  A feature with no children needs no artificial child. If strict no-duplicate
  creation is requested, require proven native support or report the unsupported
  guarantee before creation: `--external-ref` is not
  unique in Beads. If a multi-child request partially succeeds, reread every
  affected ID, return the persisted IDs and stop further writes on the first
  failure; on retry reconcile all existing children before creating missing ones.
- **Update:** use `bd update <id> --title/--description/--acceptance/... --json`
  only for explicitly supplied fields, never send a whole stale snapshot.
  A request to set `status: closed` (or any configured done status) is always
  **Complete**, regardless of whether the CLI offers `bd update --status`;
  apply its full checks. A request to enter `in_progress` as a claim uses
  **Claim**, not an unguarded status/assignee update. Never use `--force`.
  `--if-status <expected>` and `--if-assignee <expected>` are atomic guards
  ONLY on those fields (guard mismatch exits 13 when all failures are stale).
  They cannot protect title, description, labels, parent or arbitrary content
  against concurrent changes while status/assignee remain equal. There is no
  `--if-revision` in baseline 1.3.1 help. Apply `references/concurrency.md`:
  native merge operations for appends/key edits and applicable native conditions.
  Freshly compare expected content before preparing a bounded field replacement;
  verify it and preserved fields afterward. This is not universal lost-update
  protection; unsupported explicitly requested stronger guarantees return a precise
  limitation, not a request to pause writers. Preserve
  unrelated prose and fields. Avoid multi-ID updates: they can partially succeed.
- **Composition:** `bd create --parent <parent-id>` or `bd update <child-id>
  --parent <parent-id>`; inspect the existing parent and child, check proposed
  ancestry for a cycle; refuse a closed parent or a child whose state makes
  the requested composition invalid. `bd` can add an open child to a closed
  parent, so its success is not a readiness check. Then verify the child's
  `parent`, the typed
  `parent-child` dependency (child → parent), and unlimited parent selection.
  Reparenting/removing membership (`--parent ''`) changes mandatory scope;
  require explicit permission, fresh expected structure and result checks.
  Do not substitute a `blocks` edge for membership or add both.
- **Blocking:** `bd dep add <blocked-id> <blocker-id> --type blocks --json`;
  `bd dep remove <blocked-id> <blocker-id>` only for an explicitly authorized
  edge removal. Check both IDs and existing typed edges. Confirm the dependent
  is blocked by the blocker after add; before remove freshly verify the exact
  expected edge and afterward its absence. This does not exclude an undetected
  concurrent replacement; report an unsupported stronger request. Keep the
  default cycle check: never pass `--no-cycle-check`. `bd` rejects cycles and
  ancestor-blocking descendants; re-read on failure. A repeated add may say
  `added`: confirm actual edge rather than infer a new change. For common
  `tasks.dependencies.add`, both endpoints must reread as `task` in the
  confirmed feature scope; refuse wrong type, unknown ID, cross-scope edge,
  cycle or an unexpected prior edge. An existing exact edge may be returned as
  unchanged after verification. Check membership and blockers again after add;
  concurrent membership change is `conflict` with the actual persisted edge,
  not `ok` for the requested scope. `bd` cycle checking does not provide an
  transaction over all concurrent graph changes; report this limit.
- **Claim:** `bd --actor <actor> update <id> --claim --json` atomically guards
  claim ownership; require an open, unblocked issue (or a claim already owned
  by the same actor), and verify `in_progress`, `assignee` and current blockers
  after. `bd` allows `--claim` on a blocked issue: this check is not atomic
  with the claim. If blocker changes during the attempt, report partial claim
  and stop; do not proceed as ready. A second actor must
  receive a conflict; never overwrite a live claim with `--force`. Lease
  heartbeats are node-local (`bd --actor <actor> heartbeat <id>` if continuing
  work); do not treat a lease as a cross-machine content lock.
- **Complete:** require a specific ID, explicit permission and verified caller
  completion criteria (including mandatory members, cancelled vs completed,
  and any required publication evidence). Read status, blockers and **all**
  direct/descendant mandatory children; refuse open children or active blockers.
  Use `bd close <id> --reason <reason> --json` with no `--force`, `--continue`,
  `--claim-next` or automatic epic closing. Re-read `status: closed`, reason,
  children and edges. If already closed, report that state; do not close again.
  `bd`'s refusal is a backstop, not proof that all required children exist.
  Apply `references/concurrency.md`: native transactional child/blocker guards
  suffice for their own predicates. Freshly verify exact expected mandatory
  composition, descendants and applicable evidence before close and read them
  back afterward; no graph/external-evidence freeze is required. Native closure
  is not full feature verification or a distributed transaction. An unsupported
  explicitly required stronger guarantee returns its exact limitation.

## Separately requested Dolt publication (outside tasks v1)

Read `references/dolt-publication.md` before `dolt.publish` or preflight of a
remote-gated write. Pass exact requested/recovered revision S and separate local
result evidence when confirming prior publication. After project/destination/
safe-read checks, freshly fetch the selected remote and check S reachability
before incoming-only/divergence or new-write gates. Confirmed S returns verified
no-op despite newer local/remote history, without push, result write or close;
unknown identity, ancestry or failed reads remain unverified. Proven unsent work
needs current authority for shared project `main` history of explicitly agreed
tasks, including other agents' authorized records, and fresh destination/direction
checks. Use ordinary non-force `main:main` push and fresh remote revision assurance,
not mandatory per-commit/parent audit, private ref, new clone or full-row comparison.
The moving branch does not promise exact sent-snapshot identity, independent proof
of each historic action's authority or field-by-field equivalence. Known unknown/
foreign scope and divergence block publication; no hidden merge or force.
It is not `tasks` v1 and is never implicit in create/update. Remote-gated
mutations use `bd --sandbox` after checking auto-publication routes; this
suppresses auto-push, not concurrent writers or selective publication.
Do not adopt/configure remotes, force divergence away, commit/publish Git, close
tasks or dump database internals to the caller. Return a compact verified
revision/IDs/evidence/limitations result; Git and Dolt effects remain separate.

## Result and stop

Return `status: ok|blocked|conflict|error`, operation, project, confirmed IDs
and values, `changes` (including any partial successes), evidence from actual
reads/command output, limitations, and a concrete next action. `ok` for a
limited best-effort write must explicitly state the missing concurrency
guarantee; if the caller requires that guarantee, it is a `conflict`, not `ok`.
On any partial/multi-step failure re-read every affected ID, report what was
persisted, the actual stopping cause and exact remaining operation, using that
cause's `blocked|conflict|error`. Reuse confirmed IDs/closure; reconcile ambiguous
effects before repetition and stop before further writes. Never delete tracker entries as a
roadmap update, close parents automatically, choose the next work, or start
another lifecycle stage. `bd init` is a rare separate operation: read
`references/init.md` from this installed skill folder **only when explicitly
authorized to initialize the selected project**, before doing so. It is not
part of ordinary read/write requests.
