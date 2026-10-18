# Claim one record

Read only for claim/heartbeat, with `concurrency.md` and the main typed reads.
Require exact ID/type, actor and authorization. Bug execution adds its own
`bug-execution.md` capability; this method does not expand feature APIs.

`bd --sandbox --actor <actor> update <id> --claim --json` atomically guards
claim ownership; require an open, unblocked issue (or a claim already owned
by the same actor), and verify `in_progress`, `assignee` and current blockers
after. `bd` allows `--claim` on a blocked issue: this check is not atomic
with the claim. If blocker changes during the attempt, report partial claim
and stop; do not proceed as ready. A second actor must
receive a conflict; never overwrite a live claim with `--force`.

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
