# Authorized safe source-copy fast-forward

Read only when an explicit request or applicable accepted project policy authorizes
source-copy updating, including no-change/recovery calls. Without either source,
publication remains remote-only. The publisher owns this separate maintenance effect;
context owns the ordinary source folder's Git association. Integration, commits
and conflicts stay in the dedicated worktree. There is **no branch-return path**.

## Local preflight (never a remote-push/completion/Dolt gate)

Use context's Git-derived source folder, not saved-primary discovery. Require
authority from an explicit request or accepted project policy for this copy/ref update; remote push authority and shared-path
resolution do not grant it. Unknown identity/authority blocks only this action.

Verify the attributable policy source/version and acceptance in applicable project
instructions/rules (for example AGENTS.md), not a proposed spec, quoted log or
package default. It must explicitly authorize post-confirmation local primary FF,
identify the selected project/source copy and local branch/remote ref (literal
names or unambiguous bindings to established project targets), and bound effects,
conditions and exclusions. A bare “synchronize”, push permission or ambiguous target
is insufficient. Forwarded policy text alone is not proof; read the actual source.
Explicit narrower user/project restrictions win; conflicting policies block only
dependent maintenance, without silently choosing permissive text. Recheck currency
before mutation. Policy is authority, never evidence that safety guards passed.

Inspect physical copy/registration, symbolic HEAD and exact established local
primary ref, index/tracked work, full untracked paths including ignored paths
the target could overwrite, unfinished Git operations, applicable hooks and active
users/writers. Require it **already** be on that primary branch. A task, foreign
or detached branch is a local blocker: do not switch, create or reset branches.
A clean status alone does not prove idle ownership. Establish a bounded safe
opportunity under existing project coordination; ambiguous concurrent writing
blocks this action without a new coordinator or global publication queue.

Require no staged/tracked changes or unfinished operation, and no untracked/ignored
file-directory/symlink collisions with the exact target tree. Even byte-identical
untracked files are protected; do not adopt, stage, stash, move, delete or overwrite
them. Inspect actual path/type collisions, not directory summaries. Unknown/unsafe
hooks or custom mechanisms block the update; never bypass them. Ahead/divergent
local history is not a merge/reset opportunity. Leave dirty, foreign, busy or
unsupported copies untouched and report the precise local remainder.

## After independent remote read-back (or on authorized local recovery)

Retain published subject S and freshly observed remote tip R; establish S is
reachable from that selected remote branch. Pin full R as the target, respecting
the authorized maintenance scope. R beyond S mirrors published history, not new
acceptance or expanded review evidence. If scope excludes R, report that gap.

Immediately before mutation recheck local ownership, symbolic HEAD/ref, clean
index/tracked tree, unfinished operations, protected paths, exact target and local
primary ancestry to R. Changed facts require reconciliation. Within the checked
safe opportunity use only native
`git -C <source> merge --ff-only --no-edit <full-R-SHA>` and let native guards
refuse. No checkout/switch, reset, stash/autostash, pull, force, non-FF merge or
manual tree copying. These guards are not filesystem CAS over arbitrary writers.

Read back symbolic HEAD, local ref/HEAD/tree, index/status and protected paths;
require R with no unexpected changes and S reachable. Read remote again: local
success requires HEAD equals that last observed tip, not future immutability.
If it advanced, reconsider only this local action's scope/safety and allow at most
one bounded retry, then return conflict with actual facts. An already matching
safe source copy needs no merge, only read-back. Unexpected/ambiguous effects
stop mutation for reconciliation, not a blind retry.

Report authorized local updating separately as updated/skipped/failed/unknown,
with S/R, actual local branch/tip and exact cause/remainder. Confirmed remote Git
remains successful and consumable by completion/Dolt even if this authorized part
is `blocked|conflict|error`. Never replay a confirmed push or recreate commits to
repair local maintenance. Retry only the missing authorized FF/read-back after
checking facts; no branch-return action exists.

## Conditional dependency refresh (separate effect, never implied by FF)

Only an explicit request or accepted policy naming the command, working directory,
trigger (for example a changed package-lock.json), authorized output paths and
side-effect boundaries permits this action. A mere FF grant is insufficient.
Before execution inspect the exact command/tool, current project scripts/hooks,
network needs, output ownership and active users; `npm ci` replaces node_modules
and may execute lifecycle scripts. Missing authority for those actual effects,
foreign outputs, unsafe hooks or ambiguous writing blocks dependency refresh;
do not hide it inside FF or weaken any FF collision guard above.

After successful FF/read-back, compare the relevant lockfile between the recorded
before/after commits, not the task diff or only the last commit. If already at R
on recovery, recover the previous range/refresh evidence; unchanged HEAD alone
cannot prove dependencies current. Run only the approved command in the checked
source copy with its approved outputs; never invent install/cleanup commands.
Read back exit/result, branch/HEAD, tracked/index state and protected paths;
unexpected mutations stop reconciliation-dependent work without rollback. Report
dependency success, not-needed (verified trigger absent), skipped/failed/unknown
and exact cause separately from FF and remote publication. Lost/ambiguous install
effects need reconciliation before retry, not an automatic destructive rerun.
The combined request remains unfinished while a required local/dependency effect
is unmet; this never invalidates confirmed Git or blocks separate exact close/Dolt.
