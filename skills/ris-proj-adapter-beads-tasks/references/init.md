# Explicit Beads initialization (bd 1.3.1)

Only load for an explicit request/consent to initialize the selected project.
Confirm the project root, write scope and absence of an active `.beads/`, local
history, and remote history before initialization. An existing or ambiguous
workspace is a stop, not permission to reinitialize or discard data. Inspect
Git hooks and project instructions before side effects. `bd init` may create
a Git repository, commit Beads files and install hooks; do not assume it only
creates `.beads/`. Confirm expected side effects and authorization before use.

This is infrastructure setup, not an ordinary issue mutation covered by the
main contract's ordinary-write and heartbeat sandbox rule. Its separate setup
authorization and side-effect checks still apply. The 1.3.1 init help exposes
`--skip-agents` and `--skip-hooks`; sandbox only disables bd Dolt auto-push,
not init's filesystem/Git/hook effects. Adding it cannot authorize setup or
replace these explicit side-effect checks. Do not change global/project
auto-push settings to satisfy the ordinary-write rule.

In the selected directory run `bd init --skip-agents --non-interactive` with
`--skip-hooks` if hooks are not separately approved; optional `--prefix` only
if agreed. Never use `--force`, `--reinit-local`, `--discard-remote`,
`--destroy-token`, or `--remote` without a separately scoped decision. Verify
exit status, `bd where`, `bd context`, initial `bd list --all --limit 0 --json`,
Git status, and `.beads/` effects. On ambiguity stop and report; do not retry
initialization destructively. Dolt remote setup, push/pull and project source
of truth migration are separate work, not effects of this operation.
