# Native mutations and concurrency protection

Read before a mutation whose correctness depends on ownership, an earlier
record value, mandatory composition or blockers. Select the smallest adequate
guarantee; a human-confirmed pause is a fallback, not a routine prerequisite.
Authorization and protection are separate: neither grants the other.

## Establish actual capabilities

Check installed `bd version`, engine and the selected command's help. Baseline
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
| Update conditioned only on status/assignee | `--if-status`/`--if-assignee` with only approved fields. A stale guard writes nothing; exit 13 requires reconciliation, not removal of the guard. |
| Append notes or change independent metadata keys | Native `--append-notes` or `--set-metadata`/`--unset-metadata`; merge against the current row inside the transaction. Do not emulate by reading and replacing the whole field. Same-key conflicting decisions still require reconciliation. Reconcile an ambiguous append before retry so it is not duplicated. |
| Close one ID using native child/blocker policy | Native `bd --sandbox close <id> --reason ... --json`, without force/auto-next. The checked close enforces open direct-child and live direct-blocker policy in the transaction, including dependency coordination. No separate manual pause for these native predicates. It does not verify accepted requirements, exact expected membership, descendant completeness or the freshness of external evidence. |
| Replace description, acceptance or a feature-record from an earlier snapshot | Full applicable revision CAS if the installed command actually supports it; otherwise automatic coordination over the affected record and relevant structure/evidence. Status/assignee guards are insufficient for this read-modify-write. |
| Remove/reparent a specific edge, strict creation uniqueness or preserve exact mandatory graph/evidence | A proven transaction/conditional operation covering those predicates, or automatic coordination covering all relevant writers. Row-only CAS does not automatically protect edges or other records. |

Use revision CAS only after inspecting the installed command/backend contract:
which edits advance its token, which fields/edges are guarded, mismatch output
and rollback behavior. If `--if-revision` is supported, pass the exact fresh
token for that one ID, without numeric rounding. Never invent it from a hash,
timestamp or CLI `revision` field. Baseline 1.3.1 help exposes no such flag;
do not advertise full CAS merely because current upstream has added it.

## Automatic coordination and fallback

For predicates not protected by the chosen native operation, use an existing
project coordinator/lock automatically within authorized scope. Identify its
provider, exact record/graph keys, participating writers and lifetime through
read/mutate/read-back; release on success or failure, and never hold it during
human acceptance or long implementation. A local advisory lock protects only
writers that actually use that same lock. It is adequate for that declared
local scope, not for independent replicas, uncooperative routes or a live SQL
server's other clients. Independently maintained replicas are reconciled at
publication; a local transaction is not a distributed lock.

Do not install a coordinator, configure a server, upgrade Beads, invent lock
paths or run raw SQL writes as a hidden tracker operation. Reuse a documented
mechanism only when available. A claim, lease, sandbox, worktree, output token
or repeated read is not a general content/graph guarantee.

On a stale guard or transaction conflict, reread actual effects first. Rebuild
only the authorized operation if its inputs and decision remain applicable;
allow one bounded retry, then return `conflict` with the observed state.
Changed acceptance, membership, ownership or incompatible content is returned
to its owner rather than overwritten. No blind retry, force or weakening of
preconditions. An already-settled effect is reused.

Ask the user for a narrowly scoped pause only when a required predicate lacks
both native protection and available automatic coordination. State that exact
gap once; use one agreed window for the bounded dependent operations, not a
fresh question per internal command. Generic write permission is not a pause.
For ordinary epic content only, the main contract's explicitly accepted limited
lost-update risk remains available; it does not authorize loss of feature
acceptance evidence or bypass required composition checks.
