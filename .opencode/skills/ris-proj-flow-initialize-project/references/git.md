# Local Git preparation

Read only for missing Git or agreed Git/ignore adjustments. Inspect the selected
physical project boundary, enclosing/nested repositories, instructions, status,
existing ignores, hooks, branch policy and remotes. Do not initialize a nested
repository accidentally or change someone else's worktree/branch.

For no repository, propose the exact local root, primary branch and exclusions
(including the agreed local RIS workspace directories); get agreement before
`git init` or ignore writes. Use supported Git commands for the installed version,
not assumed flags. Preserve existing ignores; add only agreed exclusions and check
their actual effect with Git's ignore inspection, without untracking existing
files. Context does not initialize Git or create workspace directories.

Read back repository root/branch, status, ignore effects and unexpected files.
Once a usable repository exists, obtain/reuse the dedicated worktree through
common's preparation rule before further versioned edits, including ignore,
`AGENTS.md` and `ris.yaml` changes. Pre-Git bootstrap writes remain local; never
move dirty/foreign files automatically to make a later publication possible.
Do not commit, create/configure a remote, install hooks, switch a busy branch or
edit global Git settings as an implicit setup effect. Any required local Git
setting needs explicit scoped agreement. Publication remains a separate offer
through the publisher. Missing remote limits publication, not checked local
configuration; inability/refusal to create Git limits operations that require it.
On error/ambiguous effects read actual state before retry via recovery.
