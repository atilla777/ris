# Claim one record

Read only for claim/heartbeat, with `concurrency.md` and the main typed reads.
Require exact ID/type, actor and authorization. Bug execution adds its own
`bug-execution.md` capability; this method does not expand feature APIs.

For a **new assignment**, use the explicitly authorized actor first, then an
applicable existing project/tool identity after checking its provenance. If
neither exists, obtain the current session's exact ID from trusted host session
metadata/API and use `opencode:<verified-session-ID>` in OpenCode. Do not guess
from a neighboring session, OS user, model name, branch or issue owner. Missing
reliable host identity blocks only the dependent assignment with that exact gap;
no new config field or session registry is required. Pass actor and provenance
to participating owners; delegated work retains the caller's assigned actor.
An invalid explicit identity or conflicting configured facts is not fallback
permission. This selects a technical identity, not continuation rights: an
existing assignee/lease, even with the same string, requires verified execution/
copy association and current authority. Never use fallback to steal an old
claim, silently release/reclaim it or treat expired lease as transfer permission.

`bd --sandbox --actor <actor> update <id> --claim --json` atomically guards
claim ownership. Require an open issue, exact actor and permitted claim; a claim
already owned by that actor may be verified unchanged. Purpose defaults to
`execution`: active or unresolved blockers prevent new claim admission and
dependent execution, including when an own claim already exists.

Only an explicitly requested `feature-preparation` claim for a confirmed feature
activates `claim-preparation.md` beside this resource. Read/apply it before
admission or own-claim reuse; ordinary execution never uses that exception.

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
