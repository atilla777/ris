# `worktrees/1` — portable adapter contract

Owned by `ris-prepare-worktree-base`. This is a semantic interface, not CLI
commands, a universal JSON format or a registry. Direct adapters need the explicit
inputs below, not installation of this base or RIS. Each adapter ships sufficient
tool mapping for direct invocation; the base checks compatibility on composition.

## Inputs and capability report

Before dependent calls report tool/version, supported `worktrees.list`,
`worktrees.read`, `worktrees.create`, completeness/diagnostic limits and mutation
guarantees. Require repository and invocation root, exact operation, canonical
absolute target path for read/create, branch and full commit for create, explicit
read/write and side-effect scope, expected state and applicable project rules.
The caller supplies association/ownership decisions and required concurrency
guarantees. No selected capability means blocked, never an unannounced fallback.

Base selection requires the selected adapter to map explicit commit resolution
and exact remote/branch refresh to its tool. Report full commit and ref effects;
fetch failure is not freshness. These are supporting tool observations, not a
fourth worktree operation or permission to update an existing copy.

## Operations

### `worktrees.list`

Return **all** registered copies of the selected repository, including its main
copy: canonical paths, full HEAD, full branch ref or detached state, lock/prunable
and reasons, plus available diagnostics. Distinguish complete empty selection
from failure/truncation/unknown. Check repository common-directory identity, not
only a matching branch name. Listing registrations does not establish that their
directories are accessible or healthy; use exact read for the chosen copy.

### `worktrees.read`

Read exactly one selected registered copy. Verify physical path, top-level root,
per-copy Git directory and common-directory relationship; return branch/detached,
HEAD, staged/index, unstaged and untracked state, operation markers and
registration diagnostics. Unknown/unreadable state is not clean. For preservation
checks bind index bytes, HEAD/refs and bytes/types/modes of relevant pre-existing
files, including ignored/untracked files (status alone omits ignored bytes).
Inspection must not refresh/write the index or run repair. Record observation
limits, races or inaccessible content instead of claiming a stable snapshot.

### `worktrees.create`

Require authorized absolute absent path, validated branch and accessible pinned
full commit, expected branch absence, and preflight of effective tool/Git hooks
and other side effects. Re-read complete registrations, target and ref state
immediately before writing. No nested-copy collision or foreign data may be
overwritten. Default is a **new** branch at that commit. Explicitly authorized
use of an existing unoccupied branch is a separate input mode: require expected
current branch commit equal to pinned input, confirmed caller association and
permission; never reset it to a new base. Refuse an attached branch elsewhere.

Use non-force creation. Verify actual path/branch/HEAD/repository with independent
Git reads, not only tool output. A nonzero or ambiguous exit requires reconciliation
of branch, registration, files and possible hook effects; report every observed
partial effect, never blind retry. Do not remove/prune/repair rollback artifacts.

## Guarantees and result

Return `status: ok|blocked|conflict|error`, selected operation/tool/version,
requested and actual values, complete evidence/checks, effects, uncertainty and
specific recovery. Read/write/read and a task claim are not CAS, a transaction
or strict cross-process uniqueness. If such a guarantee is required, establish
an independent external writer window for the exact short operation or block.
Detectable concurrent changes yield conflict with actual persisted effects.

Creation success proves only the copy operation, not caller ownership, tracker
state, hooks/background completion or environment readiness. The caller owns
combined acceptance and setup. No task claims, belonging decisions, plans,
publication, closures, deletion, fallback tools, force, reset, rebase, stash,
commit, clobber or automatic repair/prune are part of this contract.
