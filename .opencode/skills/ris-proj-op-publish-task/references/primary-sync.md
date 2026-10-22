# Explicit-only safe source-copy fast-forward

Read only when the person explicitly requested source-copy updating, including
its no-change/recovery calls. Ordinary publication is remote-only and does not
activate this resource. The publisher owns this separate maintenance effect;
context owns the ordinary source folder's Git association. Integration, commits
and conflicts stay in the dedicated worktree. There is **no branch-return path**.

## Local preflight (never a remote-push/completion/Dolt gate)

Use context's Git-derived source folder, not saved-primary discovery. Require
explicit authority for this copy/ref update; remote push authority and shared-path
resolution do not grant it. Unknown identity/authority blocks only this action.

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
the explicit maintenance scope. R beyond S mirrors published history, not new
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

Report requested local updating separately as updated/skipped/failed/unknown,
with S/R, actual local branch/tip and exact cause/remainder. Confirmed remote Git
remains successful and consumable by completion/Dolt even if this requested part
is `blocked|conflict|error`. Never replay a confirmed push or recreate commits to
repair local maintenance. Retry only the missing authorized FF/read-back after
checking facts; no branch-return action exists.
