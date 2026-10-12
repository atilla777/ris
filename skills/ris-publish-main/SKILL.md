---
name: ris-publish-main
description: >-
  Integrate an independently reviewed RIS task change into the project's
  established primary Git branch and verify authorized direct push. Use for
  task Git publication; not PR creation, deploy, tracker/Dolt publication,
  feature acceptance or task/container completion.
---

# Integrate and verify Git publication

Own one bounded Git integration/publication result. One skill suffices: this is
an operational Git result, not a distinct portable content method. Load/apply
`ris-common` and applicable resources, and `ris-context` for project rules and
shared task evidence. Load the selected task adapter only for necessary identity/
blocker/ownership reads; this operation never writes or publishes tracker state.
Direct invocation requires no execution role.

## Gate and establish target

Require confirmed task/change scope, current accepted design/contracts,
implementation/docs evidence, exact checked/reviewed base and final tree,
independent reviewer provenance, no unresolved high/medium findings, recorded low
dispositions, integration and direct push authority. Read current project rules,
Git status, diff, recent history, worktree mapping, remotes and tracking. Establish
the primary branch and selected remote from project evidence; do not assume the
literal name `main`, configure remotes or grant direct-write permission yourself.
Confirm no active task blockers or lost ownership where execution requires claim.
Missing target/permission/checks/reviewer blocks publication with useful local
state reported. A task's in-progress status is not a publication gate.

## Integrate, reassess, publish

1. Fetch the selected remote and inspect divergence and the full outgoing commit
   and file set. Preserve dirty/untracked user work; stage only authorized files,
   inspect staged diff and exclude secrets/local workspace/tracker storage. Do not
   send unrelated local commits just because this task's tip is approved. Use
   project-established integration policy; no force push, destructive reset,
   hook bypass or silent conflict resolution. If target has advanced, inspect the
   new code/contracts before integrating; conflicting dependent work stops.
2. Commit intended changes using project history style. Integrate into the
   established primary branch only as authorized. Record resulting commit and
   exact integrated tree and current input versions. Compare it to the report's
   complete approved publication snapshot,
   not a dirty working-tree fingerprint. Verify staged/committed path/content/
   modes against its manifest, including unchanged base files and predeclared
   exclusions. Local evidence is checked separately. Do not invent exclusions
   after review or justify differing committed bytes by calling them contextual;
   obtain independent assessment of the new subject before push.
   If identical, document why evidence remains applicable. If changed
   (including compatible upstream edits, merge resolutions or doc adjustments),
   assess affected criteria, test seams, architecture fitness and doc claims;
   obtain applicable checks and independent review of the integrated version
   before push. A clean merge or an unchanged task diff does not prove the old
   review covers the new whole tree. Do not reuse failed/unavailable checks.
3. Confirm architecture documentation's factual claims on that actual integrated
   tree; pending-integration statements must now match facts. Any required doc
   correction changes the tree and is subject to the same check/review gate.
4. Reinspect target/remote and complete outgoing scope immediately before direct
   push; push only the authorized primary branch without force. On rejection or
   ambiguous response inspect local/remote refs before retry; do not recommit or
   overwrite divergence blindly. Local commits are not publication.
5. Read the selected remote branch independently (remote ref query and fetch or
   separate clone as project requires). Verify the sent commit is visible/reachable
   and expected files/tree match its snapshot. Later allowed remote commits do
   not negate a verified earlier snapshot. Record exact sent SHA/tree and remote
   evidence, not merely command exit. Stop with partial state if verification fails.

Return `ok|partial|blocked|conflict|error`, task, source/target branches and remote,
commits/tree, checks/review provenance and applicability, docs state, actual push
and remote-read evidence, preserved local effects and recovery needs. Persist
authorized local task evidence with an exact filename and read it back. Stop at
Git publication: never declare the feature accepted, close tasks/parents, push
Dolt, deploy, create a PR or choose a subsequent operation.
