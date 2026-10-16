# Beads-specific ordinary work operations

Load for explicitly identified ordinary standalone tasks, task-containers and
their children, or bounded native bug read/list/create/update below.
This resource composes the main adapter's Create, Update,
Composition, Blocking, Complete and read/reconcile operations; it does not extend
the common tasks v1 feature-parent rules or introduce a new record schema.
Apply `concurrency.md` before dependent writes and `dolt-publication.md` only for
authorized publication/preflight. The caller owns kind, content and acceptance.

## Inputs and advertised capabilities

### Native bug registration capability

Advertise ordinary **bug read, list, create/reconcile and update** as
Beads-specific operations, not `tasks.items.*` or feature-record/1. The task
operations below remain task-only; this branch does not extend claim, close,
children, composition or blocking to bugs. The caller decides substantive
duplicate identity, not this adapter.

Require the selected project, bounded authority, operation, expected native
type, message/title and available context, stable project-scoped creation key
and expected absence, or exact existing ID and approved supplement. Accepted
fix requirements/design, reproduction, diagnosis and readiness are not creation
prerequisites. Persist the message as unconfirmed in readable description, with
available context and possible related IDs distinguished from proven duplicates.
Do not invent a parent, feature payload, stage children or confirmation status.

- **Read/list:** `bd show <id> --json` must contain exactly one exact ID and the
  expected `issue_type: bug`. For deduplication and identity reconciliation use
  `bd list --all --limit 0 --type bug --json` across the entire relevant project,
  including closed records and other parents. Validate returned IDs/types and
  completeness. When legacy task originals are relevant, additionally inspect
  the complete `--type task` set and exact typed reads; do not convert their
  type or treat them as feature operations. Failed/incomplete reads cannot
  establish absence and stop dependent writes.
- **Create/reconcile:** apply main Create's identity, best-effort concurrency,
  response-shape and ambiguous-effect rules, using `bd --sandbox create --type
  bug --title <approved-title> --description <message-and-context> --external-ref
  <stable-project-scoped-key> --json`, with only approved fields. Keep the same
  key across retries; distinguish it from a similarity/title search. Before
  create, on uncertain response and after create, search the full all-status
  relevant sets by that key and compare type, message, context, parent absence
  and intended identity. Independently exact-read any returned or recovered ID.
  Reuse only the exact prior result; multiple matches, changed identity or an
  unreconciled effect returns conflict with all known persisted IDs. Never
  generate a new key or repeat create to evade uncertainty. External references
  are not unique: report best-effort limits and any detected collision; a required
  strict guarantee unavailable here blocks its write under main Create.
- **Update/supplement:** on the caller's confirmed original ID, fresh-read its
  type, message, notes and expected content. Use native `bd --sandbox update
  <id> --append-notes <approved-supplement> --json` under `concurrency.md`.
  Include a stable scoped supplement identity and the message/context being
  added so a repeat can inspect the exact marker AND content. An already present
  exact supplement is verified unchanged; same marker with different content or
  uncertain effect is conflict, not permission to append again. On ambiguous
  append independently read notes before any retry. Native append preserves
  foreign notes; no whole-description/notes replay is needed. This is not
  atomic append-once under concurrent retries: reconcile/report repeated markers
  rather than promise uniqueness. Legacy ordinary task originals use this same
  bounded append through advertised ordinary task update, with expected type
  `task`; other types return an exact unsupported-type diagnostic. Never change
  type, status, assignee, original message, investigation sections or acceptance
  as a registration supplement. Closed originals may receive an authorized
  supplement, but are not reopened or closed by registration.

After either write independently exact-read ID/type, message/context, key or
supplement identity/content, preserved foreign description/notes/fields and
unchanged status where applicable. Repeat complete creation-key reconciliation
after create or recovery; inspect supplement occurrences after append. Unexpected
changes return conflict with actual effects. Main concurrency rules govern any
separately authorized necessary field replacement; without required protection
stop that write, never advertise status/assignee guards as content CAS.
Return created/supplemented/unchanged and local persistence separately from
publication. No implicit Dolt push, claim, investigation or completion follows.

### Ordinary task/container capabilities

Require selected project, exact operation/ID (or approved creation identity),
explicit kind and authority, own outcome/scope/criteria, stable key, exact source
selectors/versions and separate acceptance addresses, constraints/contracts,
expected current state and permitted fields/links. A standalone root has no
artificial epic. A structural parent is permitted when explicitly confirmed;
children carry their own sufficient contract. Neither missing feature JSON nor
a feature parser failure proves ordinary kind. Preserve malformed/historical
feature blocks and return their diagnostic; no reclassification or migration.

Advertise only actual supported Beads operations:

- **ordinary create/reconcile:** `bd create --type task` with supplied title,
  description, acceptance, `--external-ref` and optional approved `--spec-id`;
  `--parent` only for a confirmed open structural parent. Search the complete
  all-state task set across parents by stable key and source association before
  and after creation, following main Create. Reuse only exact kind/type/key,
  parent, content, sources and decisions. Existing ID means read/reconcile that
  ID, never implicit create. Multiple matches or changed identity is conflict.
  Best-effort creation is not uniqueness; strict uniqueness needs protection
  covering every relevant creator. Ambiguous creation is reconciled before retry.
- **ordinary source/content update:** main Update with only authorized fields;
  retain separate pinned requirements/design/decision links in readable content
  or agreed independent metadata keys. No mandatory feature JSON, digest or
  history store. A simple accepted task can use sufficient accepted constraints
  without a design file; material design requires a separate verifiable decision.
  Description/acceptance replacement uses fresh expected content and targeted
  fields under `concurrency.md`, followed by independent read-back. Native
  independent metadata-key edits merge other keys, but do not protect same-key
  decisions, related graph or external evidence. Changed inputs invalidate
  dependent evidence; preserve unrelated content and unchanged acceptance pins.
- **ordinary children/links:** main Composition and Blocking, with confirmed
  ordinary scope/endpoints, all-state child reconciliation, ancestry/cycle checks
  and exact read-back. Use `bd create --parent` and `bd dep add <blocked>
  <blocker> --type blocks --json`, not common feature-only create/add semantics.
  Native cycle checks do not protect expected membership. Partial creation or
  edge failure stops further writes and returns every persisted ID/edge.
- **ordinary result persistence:** main Update using native `--append-notes` or
  authorized `--set-metadata key=value` where suitable, never stale whole-field
  replacement. Include exact ID/kind, own criteria/outcomes and disposition,
  integrated revision(s), accepted refs/decisions, check/review provenance,
  mandatory composition/blockers, evidence addresses and limits. Reports must
  be accessible without local ignored notes. Reconcile uncertain append before
  retry. Append/key merge protects only its native row operation; snapshot-bound
  evidence needs fresh applicability/composition checks, not an atomic freeze
  over all relevant content/graph/external evidence.
- **ordinary exact close:** main Complete, separately from persistence, on one
  explicit ID with full mandatory scope/cancellation disposition and current
  evidence supplied by the caller. Native transactional direct-child/blocker
  checks cover those predicates only; expected membership, descendants and
  external-evidence freshness are checked immediately before close and after it,
  without a manual window or global lock. Report native limits and any unsupported
  explicitly required stronger guarantee before its dependent write. Never force, close
  ancestors/children, reopen a closed record or use status update as a shortcut.

Read back exact fields, type/kind/identity, source decisions, complete children,
typed edges and status after the bounded operation. An already-settled effect
returns verified unchanged; closed-pending publication gets only that remainder.
Return the main result envelope with actual provider/covered predicates/limits,
known IDs and separate local/persisted/closed/published facts. Reuse the single
adapter publication algorithm; no automatic Dolt push follows these writes.
