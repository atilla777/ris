# Native mutations and concurrency protection

Read before a mutation whose correctness depends on ownership, an earlier
record value, mandatory composition or blockers. Ordinary work uses fresh reads,
native atomic/conditional operations, targeted fields and independent read-back;
it requires no manual pause, global lock or graph-wide transaction.
Authorization and protection are separate: neither grants the other.

## Establish actual capabilities

Establish installed `bd version`, engine and selected command support once per
unchanged tool/workspace context; check only missing/new capabilities, not the
same help on every mutation. Baseline
CLI is 1.3.1; do not assume newer upstream flags exist locally. Source evidence
for its transaction semantics is the pinned upstream
[update implementation](https://github.com/steveyegge/beads/blob/v1.3.1/internal/storage/issueops/update.go),
[checked close](https://github.com/steveyegge/beads/blob/v1.3.1/internal/storage/issueops/close.go)
and [batch close](https://github.com/steveyegge/beads/blob/v1.3.1/internal/storage/issueops/close_batch.go).
This is source inspection, not a claim of a live concurrency test or of
equivalence across engines, remote replicas or future versions.

| Requested effect | Preferred protection and limit |
|---|---|
| Claim one ID | Native `--claim`; ownership CAS, not readiness/composition CAS. |
| Reassign a session on explicit human continuation | `claim.md` guarded assignee/status update, preserving the associated copy; no second takeover confirmation, release/reclaim or force. Changed holder/status stops reconciliation-dependent writes. |
| Update conditioned only on status/assignee | `--if-status`/`--if-assignee` with only approved fields. A stale guard writes nothing; exit 13 requires reconciliation, not removal of the guard. |
| Append notes or change independent metadata keys | Native `--append-notes` or `--set-metadata`/`--unset-metadata`; merge against the current row inside the transaction. Do not emulate by reading and replacing the whole field. Same-key conflicting decisions still require reconciliation. Reconcile an ambiguous append before retry so it is not duplicated. |
| Close one ID using native child/blocker policy | Native `bd --sandbox close <id> --reason ... --json`, without force/auto-next. The checked close enforces open direct-child and live direct-blocker policy in the transaction, including dependency coordination. No separate manual pause for these native predicates. It does not verify accepted requirements, exact expected membership, descendant completeness or the freshness of external evidence. |
| Set approved description/acceptance fields | Freshly read the exact record, compare expected values, preserve unrelated prose, historical payloads and source links, prepare only the approved field, use applicable native conditions and read back. No full-record replay or feature JSON mutation. This does not promise protection from every same-field concurrent edit. |
| Remove/reparent a specific edge | Freshly check exact endpoints, type, expected membership and permission; use the bounded native operation and verify the resulting graph. This does not guarantee against an undetected concurrent remove/re-add. |
| Explicitly demanded strict uniqueness or atomic multi-record/evidence predicate | Require an actually supported operation covering that predicate; otherwise return the exact unsupported guarantee before the dependent write. Do not turn ordinary work into that stronger request. |

Use revision CAS only after inspecting the installed command/backend contract:
which edits advance its token, which fields/edges are guarded, mismatch output
and rollback behavior. If `--if-revision` is supported, pass the exact fresh
token for that one ID, without numeric rounding. Never invent it from a hash,
timestamp or CLI `revision` field. Baseline 1.3.1 help exposes no such flag;
do not advertise full CAS merely because current upstream has added it.

## Freshness, limits and conflicts

Bug investigation report/acceptance persistence applies `investigation.md`: one
assigned investigator is sufficient organizational control for ordinary bounded
fresh-compare/targeted-write/read-back, not a technical exclusion of other writers.
No CAS provider is mandatory for that ordinary request. Preserve original/foreign
content, stop observed conflicts and reconcile report/acceptance separately. An
explicitly required stronger unsupported content predicate still blocks its write;
status/assignee guards cannot satisfy it. Independent research remains possible.

Before each mutation reread identity and expected target values; reread ownership
and complete children/typed blockers only when its actual
predicates depend on them. A simple title/priority/independent-key edit does not
require delivery, acceptance or graph reconstruction. Changed accepted content,
claim, membership/edge mutation and completion retain their specific checks.
Ordinary child-based container close checks the nonempty complete direct-child
set (all closed) and parent blockers; administrative container
status-only close checks direct native predicates. Neither requires recursive
delivery/acceptance reconstruction or external Git/verification evidence.
For operations depending on external evidence, consume its checked pinned-version
and applicability result; restore missing evidence or reassess relevant changes,
not immutable source history on every write. These are substantive checks, not a
requirement to freeze the graph or external documents through write/read-back.
Afterward independently verify requested fields, preserved content and relevant
structure. Unexpected changes stop dependent work and are reconciled with their
owner. Immutable accepted Git refs remain pinned; do not repin to hide drift.
Independent replicas are reconciled at publication, not by a local lock.

Do not install a coordinator, require a global lock/queue, configure a server,
upgrade Beads, invent lock paths or run raw SQL writes as a hidden operation.
A claim, lease, sandbox, worktree, output token or repeated read is not a general
content/graph guarantee. Ordinary own-task and explicitly assigned shared-record
writes proceed with the bounded native guarantees and freshness checks above;
report their limits without a separate risk-acceptance question.

On a stale guard or transaction conflict, reread actual effects first. Rebuild
only the authorized operation if its inputs and decision remain applicable;
allow one bounded retry, then return `conflict` with the observed state.
Changed acceptance, membership, ownership or incompatible content is returned
to its owner rather than overwritten. No blind retry, force or weakening of
preconditions. An already-settled effect is reused.

If a complex requested action cannot be performed correctly by the available
bounded operations, return its exact limitation and preserved effects. Do not
ask to stop writers or silently weaken an explicitly required atomic guarantee.
Return only a substantive scope/acceptance conflict to the human; technical
reconciliation stays with the operation owner when supported.
