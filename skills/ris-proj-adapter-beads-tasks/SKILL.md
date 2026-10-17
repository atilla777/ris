---
name: ris-proj-adapter-beads-tasks
description: >-
  Serve the tasks v1 and optional feature-record/1 adapter roles and verify
  bounded Beads operations via bd: read/list epics and tasks, ordinary native bug
  read/list/create/update and protected investigation/disposition, create/update by
  confirmed ID, manage links, claim, conditionally update feature evidence,
  ordinary bug execution claim/snapshot/fix-completion, administratively close
  exact containers or complete verified work, and
  separately publish authorized Dolt history; also provide read-only all-work-type
  plan inventories and exact unknown-type reads. Use for
  bounded tracker operations, not for planning a feature or configuring remotes.
---

# Beads tasks adapter

Own only the requested tracker operation and its verified result. The caller
owns record choice, content, mandatory scope and authorization. This is one
technical skill: bounded `bd` operations need no separate portable method.
Ensure installed `ris-proj-lib-common` is available and apply its baseline and
resources under their actual triggers. If project settings must be resolved,
apply installed `ris-proj-op-resolve-context`; otherwise use the caller's explicit
project/workspace without context, shared roots or execution roles. Neither a
dependency nor `adapters.tasks.skill` grants write access.

## Capabilities and conditional resources

Support `tasks` v1 roadmap `tasks.epics.list|read|create|update` and
`tasks.blocks.list|add|remove`; optional task operations are
`tasks.items.list|read|create`, `tasks.children.list` and
`tasks.dependencies.list|add`. These are semantic names, not CLI commands.
Feature and child records use native `task`, feature parent `epic`; native
`feature` is not a substitute. Read routes below cover these reads and ordinary
native bug reads/lists with the caller's expected type. No feature payload is
required for ordinary reads. Report requested supported operations/guarantees
and contract version before dependent writes, not every unrelated capability on
each read. An unsupported requested version, operation or full-selection guarantee
blocks its dependent write, even if some other `bd` command exists.

Read the following **from this installed skill folder before the named action**;
do not load other branches merely to list or exact-read a record:

| Action | Required owned resource |
| --- | --- |
| Read-only plan overview: all working types, exact unknown type, complete children, parent and blocks | `references/plan-overview.md` |
| Authorized bounded field update | `references/update.md` and `references/concurrency.md` |
| Create/reconcile epic or task; `tasks.items.create` | `references/create.md` and `references/concurrency.md` |
| Membership or blocking-edge mutation | `references/structure.md` and `references/concurrency.md` |
| Claim/heartbeat | `references/claim.md` and `references/concurrency.md` |
| Administrative exact-container status close or verified completion | `references/completion.md` and `references/concurrency.md` |
| Ordinary standalone create/source-content/child-link/result/close specifics | `references/standalone.md` plus only the action resource it selects; no standalone resource for a simple non-source field edit |
| Native bug registration create/update (not ordinary read/list) | `references/standalone.md` and its selected resources |
| Bug report/acceptance persistence, duplicate relation or disposition-close | `references/investigation.md` |
| Bug execution claim/snapshot/design-link/result/fix-completion | `references/bug-execution.md` |
| Feature-record read, update, record-verification, complete; or initial block on create | `references/feature-record.md` |
| Separately authorized `dolt.publish` or remote-gated write preflight | `references/dolt-publication.md` |
| Explicitly authorized selected-project initialization only | `references/init.md` |

The feature-record capability is optional `tasks.feature-record/1`, not implicit
in tasks v1; its resource owns its guarantees. Malformed/absent feature data never
selects ordinary kind. Administrative status close is Beads-specific, not
`tasks.features.complete`; it preserves the payload and is not acceptance.
List/read/list-blocks give complete inspected results or an explicit failure.
Create is best-effort, update uses fresh expected fields/native guards, and edge
writes verify exact typed direction. Read/write/read and row guards are not
universal content/graph CAS. An explicitly required unsupported guarantee blocks
its dependent write; ordinary operations need no manual/global writer lock.

## Inputs and selected workspace

Require chosen project/workspace, exact operation, expected native type and IDs
for existing records (plan overview may explicitly request discovery of actual type),
needed fields/edge direction and expected outcome. Writes
add explicit authority/allowed fields; claims add actor. Never guess an ID from
a title. Check `bd version` (supported baseline 1.3.1), `bd where`/`bd context`
in the selected project. An uninitialized, wrong, unavailable or read-only
workspace blocks dependent writes. Use `bd -C <project-root>` only for an existing
Beads project; initialization needs the working directory and its separate owner
resource. Do not use `--global`, `--db` or ambient fallback to bypass a missing
project. Commands below refer to this workspace. Request `--json`, check exit
code AND body. Pass IDs, titles and body as separate safely quoted arguments,
not interpolated shell code; use `--body-file` when text must not be exposed as
an argument. Never edit `.beads/` directly. Read-only requests may use
`--readonly`; CLI acceptance alone is no write authority.

## Read and reconcile

Start with identity, then retrieve the content needed for the caller's decision.
Completeness of the record set does not require every record's full text.
When full own content is already required, use exact `show` directly rather than
adding a redundant brief identity read.
Checked native forms for `bd` 1.3.1 (all in the selected workspace):

| Read | Native command | Required interpretation |
| --- | --- | --- |
| Complete epic/task inventory | `bd list --all --limit 0 --type epic --brief --json` (or `--type task`, ordinary `--type bug`) | All statuses including closed; validate each ID/type/scope. |
| Exact identity | `bd list --id <id> --all --limit 0 --brief --json` | Require exactly one exact matching ID and actual expected type; do not hide wrong type with a type filter. |
| Complete direct children | `bd list --parent <id> --all --limit 0 --brief --json` | Validate each actual parent/type; recurse when mandatory scope requires descendants. |
| Directed blockers | `bd dep list <id> --type blocks --direction=down --json` | Down means queried blocked ID → blocker; up means queried blocker → blocked ID. Normalize blocked → blocker. |
| Necessary record content | `bd show <id> --brief-deps --json` | Full own record, compact dependency bodies; read a related ID separately when its content is needed. |

Brief JSON supplies `id`, `issue_type`, `status`, `title` and available identity/
ordering fields such as assignee, priority, external_ref and timestamps. It omits
free-form description/design/acceptance/notes/payload/waiters: omitted is **not
empty**. Validate actual fields, not an assumed universal schema. Counts do not
prove membership or directed edges. If parent/spec/edge fields needed by a
predicate are missing, use bounded exact `show`/typed `dep list` reads; unknown
shapes remain unverified, never empty. Full native JSON is a valid fallback.
Native `dep list` can include full related bodies and has no checked compact-body
flag; retain this bounded edge-read fallback instead of inventing a projection.
Only request additional related content when the caller needs it.

An exact known ID needs no global list unless the caller actually needs absence/
duplicate evidence. For absence/dedup retain all-status/unlimited relevant sets
across parents. Disclose every field needed by **each** identity predicate: key/
spec fields can select candidates only for the predicates they establish; a slug,
historical feature block or similar bug content may require description reads
for every relevant record. An unproven filter cannot exclude those candidates.
Read full accepted inputs, report/criteria, notes snapshots, preserved prose and
decisions whenever readiness, replacement, reconciliation or evidence needs them.
Do not replace required content with a title, count, hash or brief row.

`--brief` is incompatible with `--format`; direct `.ID`/`.id` templates produced
`no value` and are not this route. `show --short` lacks the typed structured
contract; `show --brief-deps` is not single-field projection of the own record.
Check exit status and full output: nonzero, malformed JSON, `no value`, truncation
or an unknown shape cannot establish absence. Recover complete output through
the host's saved-output facility or bounded reads; do not silently drop records.

- `bd show <id> --brief-deps --json` returns an array; require exactly one matching ID
  and expected `issue_type` (native bug reads expect `bug`, not a feature task).
  It includes status, type, parent when present, dependencies and sometimes
  revision; use a revision as CAS only when the installed command/backend
  explicitly supports that token and its scope.
- `show`/`dep list` edges may use related-record `id` plus `dependency_type`;
  all-state `list` edges may use `issue_id`, `depends_on_id`, `type`. Normalize
  using the queried endpoint and explicit direction, not native Dolt columns.
  Unknown edge shapes are not empty sets. Membership `parent-child` is not `blocks`.
- Inventories include closed records with `--all --limit 0`; defaults are 50
  and exclude closed, and `--status all` is not the all-status flag. Filters must
  preserve required coverage. `bd children <parent> --json` has no explicit
  unlimited flag. Query descendants only when required. A clean empty array is
  not an error; failed/truncated queries cannot prove completeness. One-parent
  lists cannot exclude duplicates elsewhere. `bd show <id> --json` and
  `bd dep list <id> --json` remain full typed-edge inspection fallbacks.

## Mutation verification and result

Before a mutation fresh-read the affected IDs/expected target fields and only
the children/edges, ownership or external evidence on which that operation's
predicates depend. Compare with confirmed expected state; unexpected differences
return `conflict` without writing. No delivery reconstruction for a simple field
edit. Follow the selected action resource: close cannot masquerade as update.
Afterward independently read requested and preserved fields and relevant
structure. Zero exit/returned ID is not proof of the full intended effect.
For nonzero/malformed/ambiguous output reconcile actual effects before any retry;
if identity/effect is unknown, stop. Never blindly recreate, reparent or close.

For ordinary reads return the requested facts and material limits briefly; no
formal envelope, unrelated acceptance/channel history or mandatory next action.
When a caller needs structured status, use `ok|blocked|conflict|error` (tracker
status is different). Writes report actual IDs/values, checked changes and native
guarantee limits; a required unsupported stronger guarantee is `conflict`, not
best-effort `ok`. Partial/multi-step failure re-reads every affected ID and returns
persisted effects, stopping cause and exact remainder with causal status. Apply
common artifacts rules for partial/uncertain effects or execution transfer.
Reuse confirmed IDs/closure and reconcile uncertain effects before repetition.
Never delete entries as a roadmap update, close parents automatically, choose
next work or start another lifecycle stage. Publication is separate, never an
implicit consequence of create/update/close.
