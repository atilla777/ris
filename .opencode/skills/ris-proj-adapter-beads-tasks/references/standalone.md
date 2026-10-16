# Beads-specific ordinary work operations

Load for explicitly identified ordinary standalone tasks, task-containers and
their children. This resource composes the main adapter's Create, Update,
Composition, Blocking, Complete and read/reconcile operations; it does not extend
the common tasks v1 feature-parent rules or introduce a new record schema.
Apply `concurrency.md` before dependent writes and `dolt-publication.md` only for
authorized publication/preflight. The caller owns kind, content and acceptance.

## Inputs and advertised capabilities

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
