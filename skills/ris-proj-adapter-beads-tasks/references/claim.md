# Claim one record

Read only for claim/heartbeat, with `concurrency.md` and the main typed reads.
Require exact ID/type, actor and authorization. Bug execution adds its own
`bug-execution.md` capability; this method does not expand feature APIs.

`bd --sandbox --actor <actor> update <id> --claim --json` atomically guards
claim ownership. Require an open issue, exact actor and permitted claim; a claim
already owned by that actor may be verified unchanged. Purpose defaults to
`execution`: active or unresolved blockers prevent new claim admission and
dependent execution, including when an own claim already exists.

Only an explicitly requested `feature-preparation` claim for an explicitly confirmed feature
may use action-specific admission. Require the caller's exact authorized
preparation action and inspectable scope evidence for **every** active directed
blocker, matched to freshly read edge/endpoints/content. The caller owns the
substantive action/scope decision; verify its evidence against actual tracker
facts. Admit a fresh claim despite active edges only when each is proved
execution-only and does not prohibit that preparation action. Unknown applicability,
missing evidence or a real preparation blocker blocks admission. Do not infer
execution-only scope from a title, raw status, null refs or caller's purpose alone.
This exception does not authorize execution, remove edges or waive ownership.

`bd` allows `--claim` on a blocked issue: blocker admission is not atomic with
the claim. Independently verify `in_progress`, exact `assignee`, current directed
blockers and the purpose/action's evidence after claim (or own-claim reuse).
If blockers/content changed during the attempt, reconcile the fresh facts before
dependent progress: execution remains blocked by any active/unresolved blocker;
preparation proceeds only if every remaining active blocker is freshly proved
execution-only for that exact action. Otherwise report the persisted partial
claim and exact blocker/evidence gap and stop; claim success is not readiness.
Ownership loss or native refusal stops the dependent action regardless of purpose;
reconcile ambiguous effects before retry. A second actor receives conflict. Never
use `--force`, remove edges, silently release/reclaim or bypass native refusal.

For continuing work, `bd --sandbox --actor <actor> heartbeat <id>` refreshes the current
owner's lease. Baseline 1.3.1 `heartbeat --help` documents `lease_expires_at` and
`heartbeat_at` in an ephemeral node-local table, with no Dolt commit or history
from the lease update itself (unlike claim status/assignee writes). This does
not make the complete command publication-free. In pinned 1.3.1 source,
[`heartbeat.go`](https://github.com/steveyegge/beads/blob/v1.3.1/cmd/bd/heartbeat.go)
calls `commitPendingIfEmbedded`, which can commit pending embedded changes;
[`main.go`](https://github.com/steveyegge/beads/blob/v1.3.1/cmd/bd/main.go) also
allows heartbeat through post-run native auto-push. That route skips under
sandbox in [`dolt_autopush.go`](https://github.com/steveyegge/beads/blob/v1.3.1/cmd/bd/dolt_autopush.go).
Therefore sandbox is mandatory for heartbeat as well as issue writes, regardless
of consumer rules. It suppresses bd auto-push, not pending local commits, foreign
hooks or other publication routes. A lease is not a cross-machine content lock.
Recheck actual version/help and command-wide effects when the route differs;
do not infer a sandbox exception from ephemeral lease storage.
