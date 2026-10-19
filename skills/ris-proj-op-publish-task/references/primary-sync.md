# Preflight and complete primary-copy synchronization

Read for full publication, including no-change/recovery calls. The Git publisher
owns this local completion; context owns primary identity/provenance. Integration,
commits and conflicts stay in the subject's own branch/copy. Do not use the shared
primary copy as an integration workspace or update it before remote confirmation.
Explicit **remote-only** skips this mutation, reports local synchronization as
excluded and never represents full publication. Do not select it silently.

## Before a new push

Use context's checked explicit/available-saved primary selection and association,
not the first Git worktree, branch name or common-dir alone. Require authority
for this copy/ref update as well as remote push; unknown identity/authority blocks
full publication before push. An existing project prohibition on moving local main
is a blocker, not something this package overrides.

Inspect the selected physical copy, repository/worktree registration, symbolic
HEAD and exact local primary ref, index/worktree status, full untracked paths
(including ignored paths that the target would overwrite), unfinished Git
operations, applicable hooks and evidence of active users/writers. Establish a
safe update opportunity under the project's existing ownership/coordination
policy. A clean status alone does not prove the copy is idle; ambiguous or foreign
active use blocks the mutation. Do not install a coordinator or demand a global
publication queue. If concurrent writing cannot be excluded/protected for this
bounded copy update under that policy, return that specific gap, not a safety claim.

For the conservative automatic path require the copy already on the established
local primary branch, no staged/tracked changes, no unfinished operation and no
untracked/ignored file-directory or symlink collision with the exact target tree.
Unrelated untracked files may remain. Even byte-identical untracked files are
protected; do not adopt, stage, stash, move, delete or overwrite them automatically.
Check actual path/type collisions rather than treating an untracked directory
summary as one file. Never switch a busy/different/detached branch to primary.
Check local tip ancestry to the intended remote target: ahead/divergent local
history is not an automatic merge/reset opportunity. Unknown/unsafe hooks or
custom checkout mechanisms block this automatic path; do not bypass them.
Known failure of any full-result gate stops a **new** push. Independently permitted
local own-branch work is preserved. The person may separately authorize a bounded
remote-only operation, but a caller must accept that limited result explicitly.

## After independent remote read-back (or on recovery)

Retain exact published subject S and observed remote target R. Establish S is
reachable from the freshly read selected remote branch. Choose a full target R
from that confirmed branch; do not copy files or use an unpinned `pull`. If R
advanced beyond S, this step only mirrors published history: it does not accept
new content or expand S's check/review evidence. Respect any narrower authorized
sync scope; if it excludes R, report the scope decision rather than silently
syncing unapproved history or declaring currentness at the older S.

Re-read copy ownership/safety, HEAD/ref, index/files/untracked collisions and
target immediately before updating. If the copy changed since preflight, reconcile
it; never trust a saved clean marker. Within the established safe opportunity use
native `git -C <primary> merge --ff-only --no-edit <full-R-SHA>` only for the
already-checked-out primary branch, letting native overwrite/ref/index guards
refuse conflicts. No force, reset, branch switch, non-FF merge, autostash or manual
tree copying. Git guards and fresh reads are not an atomic CAS over arbitrary
filesystem writers; if the required protection cannot be established, stop.

Read back symbolic HEAD, local ref/HEAD, index/tree, status and protected paths;
confirm the copy represents R with no unexpected changes and S is an ancestor.
Read the remote branch again: full success requires local primary HEAD equals
that last observed remote tip. Report this observation's time/ref, not a guarantee
against future advancement. If it moved, reconsider only synchronization to the
new confirmed tip and protection/scope; after one bounded retry return conflict
with local/remote facts, not an unbounded chase or a repeated subject publication.
An already matching safe copy needs no merge; still check and report its state.

If remote publication is confirmed but local completion is blocked/failed/unknown,
return the cause's `blocked|conflict|error`, **remote published, local sync pending**,
S/R, actual local tip/copy state and exact remaining gate/action. Never undo remote
history or replay a confirmed push. Retry only the missing local verification/sync
after fresh reads. No-change calls also owe this local completion in full mode.
