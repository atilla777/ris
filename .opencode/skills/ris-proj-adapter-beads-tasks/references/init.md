# Explicit Beads initialization (bd 1.3.1)

Only load for an explicit request/consent to initialize the selected project.
Confirm the project root, write scope and absence of an active `.beads/`, local
history, and remote history before initialization. An existing or ambiguous
workspace is a stop, not permission to reinitialize or discard data. Inspect
Git hooks and project instructions before side effects. `bd init` may create
a Git repository, commit Beads files and install hooks; do not assume it only
creates `.beads/`. Confirm expected side effects and authorization before use.

In the selected directory run `bd init --skip-agents --non-interactive` with
`--skip-hooks` if hooks are not separately approved; optional `--prefix` only
if agreed. Never use `--force`, `--reinit-local`, `--discard-remote`,
`--destroy-token`, or `--remote` without a separately scoped decision. Verify
exit status, `bd where`, `bd context`, initial `bd list --all --limit 0 --json`,
Git status, and `.beads/` effects. On ambiguity stop and report; do not retry
initialization destructively. Dolt remote setup, push/pull and project source
of truth migration are separate work, not effects of this operation.
