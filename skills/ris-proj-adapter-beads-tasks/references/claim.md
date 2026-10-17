# Claim one record

Read only for claim/heartbeat, with `concurrency.md` and the main typed reads.
Require exact ID/type, actor and authorization. Bug execution adds its own
`bug-execution.md` capability; this method does not expand feature APIs.

`bd --actor <actor> update <id> --claim --json` atomically guards
claim ownership; require an open, unblocked issue (or a claim already owned
by the same actor), and verify `in_progress`, `assignee` and current blockers
after. `bd` allows `--claim` on a blocked issue: this check is not atomic
with the claim. If blocker changes during the attempt, report partial claim
and stop; do not proceed as ready. A second actor must
receive a conflict; never overwrite a live claim with `--force`. Lease
heartbeats are node-local (`bd --actor <actor> heartbeat <id>` if continuing
work); do not treat a lease as a cross-machine content lock.
