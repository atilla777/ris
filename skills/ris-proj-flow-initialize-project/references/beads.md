# Selected Beads preparation

Read only when Beads is the agreed task adapter. Load/apply installed
`ris-proj-adapter-beads-tasks` for bounded workspace reads, checking its actual
version/capabilities and target identity. Inspect existing tracker/config/local
and remote history before considering initialization; an unavailable workspace
read is not proof of absence. Existing or ambiguous storage must not be
reinitialized, replaced or accessed through another ambient/global database.

If absent and initialization is requested, load that adapter's installed
`references/init.md` **before** approving or performing it. Present its actual
Git repository/commit/hooks/storage side effects and obtain explicit authority
for them, independently of document writes. Use its native selected-directory
init operation and postchecks, including project identity, complete initial
inventory and Git effects; do not copy its algorithm or write `.beads/` directly.
No force/destructive reinit or hidden tracker upgrade. A separately approved
init commit is not permission to publish project source or outgoing Dolt history.

Return actual workspace/version/read results and preserved data, not merely a
configured adapter name. A non-Beads adapter needs its own available supported
preparation contract, not this Beads recipe. Missing tools activate tools.md.
Remote/service setup, migration and Dolt push/pull require separate authority and
their actual owner; they are not defaults. Ambiguous effects activate recovery.md
before retry. Do not create roadmap/tasks to prove the tracker works.
