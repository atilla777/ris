# Separately maintain the primary copy safely

Read for local maintenance, including no-change/recovery calls. The Git publisher
owns this separate effect; context owns primary identity/provenance. Integration,
commits and conflicts stay in the subject's own branch/copy, even when that copy
is the selected primary root. Never integrate on the local primary branch or
return to/update it before remote confirmation.
Explicit **remote-only** excludes this mutation. Otherwise attempt it only when
safety is verified, reporting skip/failure separately without narrowing or
invalidating confirmed Git publication. An explicit user request to update the
local copy remains an unfinished part of that request until checked successful.

## Local preflight (not a remote-push gate)

Use context's checked explicit → verified saved → verified ordinary Git source-copy
selection and association, not the first worktree or branch name. Require separate
authority for this copy/ref update; remote push authority and shared-path
resolution do not grant it. Unknown identity/authority or a project prohibition
blocks this local action only; do not ask for a remote-only exception to publish.

Inspect the selected physical copy, repository/worktree registration, symbolic
HEAD and exact local primary ref, index/worktree status, full untracked paths
(including ignored paths that the target would overwrite), unfinished Git
operations, applicable hooks and evidence of active users/writers. Establish a
safe update opportunity under the project's existing ownership/coordination
policy. A clean status alone does not prove the copy is idle; ambiguous or foreign
active use blocks the mutation. Do not install a coordinator or demand a global
publication queue. If concurrent writing cannot be excluded/protected for this
bounded copy update under that policy, return that specific gap, not a safety claim.

Select one of two bounded completion paths:

- **Already-primary:** the copy is already on the established local primary branch.
- **Own-current-primary return:** the selected primary root is also this subject's
  publication workspace, currently on its verified own task/change branch. Require
  attributable subject → repository/physical copy/branch association and authority
  to return this same exclusively owned copy to the existing established local
  primary branch. A branch name, assignee or clean status alone is insufficient.
  No other worktree may have that primary branch checked out; do not bypass native
  branch-occupancy guards. Preserve the own branch and its published commit. This
  is completion of the own-current-copy route, not permission to switch another
  copy, a foreign/detached branch or a busy shared primary.

Both paths require no staged/tracked changes, no unfinished operation and no
untracked/ignored file-directory or symlink collision with the exact target tree.
For the return path check both the existing local primary tree (the intermediate
checkout) and the intended remote tree, plus checkout hooks/side effects. Perform
the return only after remote confirmation and fresh local safety checks.
Unrelated untracked files may remain. Even byte-identical untracked files are
protected; do not adopt, stage, stash, move, delete or overwrite them automatically.
Check actual path/type collisions rather than treating an untracked directory
summary as one file. A different branch outside the verified own-return case blocks
local maintenance; do not switch it to primary. Report a skipped local update.
Check ancestry of the established local primary ref's tip, not the own subject
branch HEAD, to the intended remote target: ahead/divergent local primary history
is not an automatic merge/reset opportunity. Unknown/unsafe hooks or
custom checkout mechanisms block this automatic path; do not bypass them.
Failure of a local gate skips/stops only this mutation, never a **new** authorized
remote push. Preserve own-branch work and the busy/foreign copy unchanged. Report
the exact cause; if local updating was explicitly requested, retain it as the
unfinished requested part without holding up independent completion/Dolt gates.

## After independent remote read-back (or on recovery)

Retain exact published subject S and observed remote target R. Establish S is
reachable from the freshly read selected remote branch. Choose a full target R
from that confirmed branch; do not copy files or use an unpinned `pull`. If R
advanced beyond S, this step only mirrors published history: it does not accept
new content or expand S's check/review evidence. Respect any narrower authorized
sync scope; if it excludes R, report the scope decision rather than silently
syncing unapproved history or declaring currentness at the older S.

Re-read copy ownership/safety, HEAD/ref, index/files/untracked collisions and
target immediately before each mutation. If the copy changed since preflight,
reconcile it; never trust a saved clean marker. For the own-current-primary return,
require the own branch still at the exact checked/published subject commit S,
with a clean index/tracked tree and unchanged association/authority. Recheck the
existing primary ref, its ancestry to R, branch occupancy and collisions against
both checkout targets. Only within the established safe opportunity, after S's
remote reachability is confirmed, use native non-force
`git -C <primary> checkout --no-guess --no-overwrite-ignore <established-primary-branch> --`.
Do not create/reset the primary branch or override occupancy/overwrite refusals.
Immediately read back symbolic HEAD, primary ref/HEAD, index/files, protected paths
and operation state against the expected existing primary tip. Unexpected changes
or checkout failure stop dependent updates; reconcile actual effects before retry.

For either path, once the established primary branch is checked out and freshly
verified safe, use native
`git -C <primary> merge --ff-only --no-edit <full-R-SHA>`, letting native
overwrite/ref/index guards refuse conflicts. No force, reset, stash/autostash,
non-FF merge or manual tree copying; no branch switch except the narrowly guarded
post-confirmation own return above. Git guards and fresh reads are not an atomic
CAS over arbitrary filesystem writers; if the required protection cannot be
established, stop.

Read back symbolic HEAD, local ref/HEAD, index/tree, status and protected paths;
confirm the copy represents R with no unexpected changes and S is an ancestor.
Read the remote branch again: local synchronization success requires primary HEAD equals
that last observed remote tip. Report this observation's time/ref, not a guarantee
against future advancement. If it moved, reconsider only synchronization to the
new confirmed tip and protection/scope; after one bounded retry return conflict
with local/remote facts, not an unbounded chase or a repeated subject publication.
An already matching safe copy on primary needs no merge; still check and report
its state. An own branch at R is not completed primary synchronization until the
guarded return and read-back succeed.

If local maintenance is blocked/failed/unknown, report it separately with S/R,
actual local branch/tip/copy state and exact cause/remainder. Confirmed remote
publication remains successful; ordinary publication may return `ok` with local
maintenance skipped/failed. For an explicitly requested local update return the
cause's `blocked|conflict|error` for that part/combined request, not for verified
remote Git. Never undo remote history or replay a confirmed push. On an authorized
local retry check facts first and perform only the missing return, FF or read-back.
If return succeeded but FF/read-back did not, reuse the already-primary state
through its safety gates; do not switch back or recreate commits. No-change calls
preserve the same separation.
