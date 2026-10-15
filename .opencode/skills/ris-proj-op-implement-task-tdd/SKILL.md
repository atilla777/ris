---
name: ris-proj-op-implement-task-tdd
description: >-
  Implement or fix review findings for one claimed RIS task with mandatory TDD,
  accepted design/contracts and authorized documentation updates. Use for project
  test-first task execution; not text-only work, task selection, feature redesign,
  independent approval, worktree preparation, publication or tracker completion.
---

# Implement one claimed project task through TDD

Own the project's checked change and handoff. Load/apply `ris-proj-lib-common` and its
applicable resources, `ris-proj-op-resolve-context` for rules/specs/adapter and shared task paths,
and `ris-port-op-implement-change` with required `implementation_mode: tdd` for code/test
work. Before documentation synchronization,
load/apply `ris-proj-op-update-documentation`. Check actual dependency availability and
results, not just their names. Direct execution needs no configured agent role.

Establish exact task ID/project, actor, authorized code/test/docs scope, current
working copy, applicable plan or enough accepted technical inputs, and optional
review findings from the request, project and available evidence; ask only for
missing material decisions. Through the selected available adapter freshly read
task identity/content, membership, blockers and claim. Check its explicitly
supported claim operation: `tasks` v1 alone does not promise it. Confirm own
claim or atomically claim an authorized open/unblocked task before file changes;
verify ownership/state/blockers after. Do not overwrite another actor's live claim.
Recheck ownership on resumption and before new mutation batches; stop on loss or
new blockers, preserving partial work. Verify the supplied current copy's project/
repository, actual revision/state and suitability without altering existing work.
Read `references/current-copy.md` from **this installed folder** for a task-specific
or separate copy, or after a copy change, before dependent mutations/shared-path
access. Missing/conflicting inputs block that part. Use the provided suitable copy;
do not create/repair/switch/reset it or load preparation skills/worktree adapters.

For a feature-linked task use the selected adapter's supported feature-record read
and **its owned contract**; require verified published requirements/design and
their separate acceptance decisions. Missing design, unsupported/historical or
unverified inputs block dependent implementation; preserve the adapter diagnostic,
not a guessed migration. Standalone work needs accepted technical constraints,
not an invented feature record. Compare actual accepted content and contract
versions with current code and relevant integration; labels alone do not prove
applicability. Preserve accepted refs; material departures return to their owner.
Discover own accepted inputs by ID and links, and the plan at context-checked
primary `workspace.tasks/<ID>/plan.md` or its inspected override. Confirm actual
feature linkage: structural parent alone does not imply a feature. Standalone
children need their own scope/criteria/refs/seams, not copied global AC. Simple
accepted constraints need no ceremonial design file; material design does.
For an actual feature child read the confirmed feature parent's accepted record
through supported adapter reads, then restrict implementation to the child's
own criteria/refs/contracts. Do not expect a feature payload in every child or
replace its contract with the parent's complete acceptance scope.
Pass verified inputs, constraints and required TDD mode to `ris-port-op-implement-change`;
actually apply its method and check its criterion/test and RED/GREEN evidence.
Do not duplicate the loop here or waive it for convenience. Text-only work belongs
to its document operation; associated docs and behavior-preserving refactors use
the base's applicable checks without artificial RED.

Apply `ris-proj-op-update-documentation` to the affected **authorized** documents (or
record a justified no-change result). Supply actual implementation evidence and
whether the tree is pre-integration; future architecture must not be presented as
current before integration. Product writes need separate explicit permission.
Check the combined code/tests/docs diff against task criteria and accepted
contracts. With authorized evidence writes save scope, mode, checks/TDD evidence,
repair mapping and exact final snapshot identity under the primary copy's
`workspace.tasks/<confirmed-ID>/implementation.md` by default; explicit address,
then project-prescribed convention take priority. Read existing content, preserve
history/unrelated notes, append or identify the new result and verify read-back.
If shared-path access or saving is blocked, return the checked evidence unsaved
and the project result partial; do not lose independent code/test results.
Do not write tracker content/evidence unless separately authorized through the
adapter's supported concurrency guarantees.

Return status, ID/claim/copy, scope and input versions, final snapshot identity,
criteria/checks/TDD/docs results, saved/unsaved report paths and remaining needs. Local
choices do not reopen global design; material departures return bounded impact
and decision needs, with dependent changes stopped. Stop at the checked change;
no independent approval, commit/push, task/container closure or next-skill launch.
