---
name: ris-beads-tech
description: >-
  Execute and verify bounded Beads issue operations via an available bd CLI:
  read/list epics and tasks, create/update by confirmed ID, manage parent and
  blocking links, claim, and explicitly close. Use for authorized tracker
  operations, not for deciding roadmap content, planning a feature, configuring
  Dolt remotes, or automatically advancing work.
---

# Beads technical operations

Own only the requested tracker operation and its verified result. The caller
owns the choice of records, required content, completeness of mandatory work,
and authorization. This is one technical skill, not a portable planning method
or a project wrapper: `bd` operations have no independent RIS-free methodology
to split out. Ensure installed `ris-common` is available and apply it (and its
conditional resources before their respective actions). If project settings
must be resolved, use installed `ris-context` and its configuration resource
for that preparation; otherwise take the explicit project root from the caller.
Neither loading a dependency nor `adapters.tasks.skill` grants write access.

## Inputs and boundary

Require the chosen project/workspace, exact operation, record IDs for existing
records, desired fields or edge direction, actor for a claim, allowed write
scope, and expected outcome. For creation require the caller's approved type
(`epic` or `task`), title/content and a distinguishing stable reference or
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
  It includes `status`, `issue_type`, `parent` when present, dependencies and
  sometimes `revision`. A revision in output is **not** a supported CAS flag.
- `bd list --all --limit 0 --type epic --json` and likewise `--type task`
  provide untruncated sets including closed records. `bd list` defaults to
  50 and excludes closed; `--status all` is not its all-status flag. Apply
  caller filters only when they preserve required coverage; validate type,
  ID and scope on results. `bd list --parent <parent> --all --limit 0 --json`
  enumerates direct children without the default 50-row limit; repeat for
  descendants when completion requires them. `bd children <parent> --json`
  is useful for inspection but does not expose an explicit unlimited flag.
  `bd dep list <id> --json` and `bd show <id> --json` inspect typed edges;
  distinguish `parent-child` from `blocks`. A clean empty array is not an error.
  If a query fails or is truncated, do not claim completeness.

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
  stable identity and compare content/parent; an exact confirmed prior creation
  returns the existing ID, ambiguous matches are a `conflict`. An authorized
  creation defaults to best-effort without a separate concurrency-risk question:
  `bd` does not enforce unique external references, so concurrent creators can
  still make duplicates. Do not claim a no-duplicate guarantee from the search
  and read-back. If the caller explicitly requires that guarantee, require a
  separately established exclusive writer/quiescent window over
  search/create/verification; without it stop `conflict`. Run `bd create
  --type epic|task --title ... --description ... --acceptance ... --json`
  with only supplied fields (optional `--external-ref` or `--spec-id` for
  identity; neither is a uniqueness constraint). Prefer `--parent <id>` for
  a child only after checking the parent. Extract the returned ID, `show` it
  and verify content and parent. On uncertain creation, re-list all records
  and reconcile the stable identity before another attempt. With no reliable
  identity evidence, do not retry an ambiguous create: `conflict`.
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
  `--if-revision` in 1.3.1. For noncommutative content or reparenting requiring
  no lost update, require a separately established exclusive writer/quiescent
  window covering read/write/verify, otherwise return `conflict` before writing.
  Never claim this guarantee from read/write/read alone. If a limited best-effort
  update is expressly acceptable, label its concurrency limitation in the
  result. Avoid multi-ID updates: they can partially succeed.
- **Composition:** `bd create --parent <parent-id>` or `bd update <child-id>
  --parent <parent-id>`; inspect the existing parent and child, check proposed
  ancestry for a cycle; refuse a closed parent or a child whose state makes
  the requested composition invalid. `bd` can add an open child to a closed
  parent, so its success is not a readiness check. Then verify the child's
  `parent`, the typed
  `parent-child` dependency (child → parent), and unlimited parent selection.
  Reparenting/removing membership (`--parent ''`) changes mandatory scope;
  require explicit permission and exclusive writer as for content updates.
  Do not substitute a `blocks` edge for membership or add both.
- **Blocking:** `bd dep add <blocked-id> <blocker-id> --type blocks --json`;
  `bd dep remove <blocked-id> <blocker-id>` only for an explicitly authorized
  edge removal. Check both IDs and existing typed edges. Confirm the dependent
  is blocked by the blocker after add; before remove require the exact edge
  and a writer guarantee against deleting a concurrent replacement. Keep the
  default cycle check: never pass `--no-cycle-check`. `bd` rejects cycles and
  ancestor-blocking descendants; re-read on failure. A repeated add may say
  `added`: confirm actual edge rather than infer a new change.
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
  Closure has no general revision guard: if concurrent structural change is
  possible, require an exclusive writer/quiescent window or stop `conflict`.

## Result and stop

Return `status: ok|blocked|conflict|error`, operation, project, confirmed IDs
and values, `changes` (including any partial successes), evidence from actual
reads/command output, limitations, and a concrete next action. `ok` for a
limited best-effort write must explicitly state the missing concurrency
guarantee; if the caller requires that guarantee, it is a `conflict`, not `ok`.
On any partial/multi-step failure re-read every affected ID, report what was
persisted and stop before further writes. Never delete tracker entries as a
roadmap update, close parents automatically, choose the next work, or start
another lifecycle stage. `bd init` is a rare separate operation: read
`references/init.md` from this installed skill folder **only when explicitly
authorized to initialize the selected project**, before doing so. It is not
part of ordinary read/write requests.
