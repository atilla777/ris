---
name: ris-proj-op-publish-task
description: >-
  Integrate an independently reviewed RIS task/change or pre-ID document result into the project's
  established primary Git branch and verify authorized direct push. Use for
  authorized Git publication, including requirements-only documents; not content acceptance, PR creation, deploy, tracker/Dolt publication,
  feature acceptance or task/container completion.
---

# Integrate and verify Git publication

Own one bounded Git integration/publication result. One skill suffices: this is
an operational Git result, not a distinct portable content method. Load/apply
`ris-proj-lib-common` and applicable resources, and `ris-proj-op-resolve-context` for project rules and
evidence paths only when needed. Load the selected task adapter only for necessary identity/
blocker/ownership reads; this operation never writes or publishes tracker state.
Direct invocation requires no execution role.

## Select the subject, then gate the common result

Require one explicit bounded subject and authorized effects; do not fabricate a
task or acceptance to fit this operation. Select the applicable input branch:

- **Task/change:** confirmed ID and agreed change scope, applicable accepted
  requirements/design/contracts or sufficient accepted technical constraints,
  implementation/docs/check evidence and independent review. Through the selected
  adapter freshly check identity, blockers and ownership where execution requires
  claim; an old receipt/lease is neither permission nor general content/graph CAS.
  Active blockers or lost required ownership stop dependent publication. Recheck
  mutable task gates before the action; the receipt does not supply write authority.
- **Pre-ID documents:** exact project-relative paths and subject/scope, separate
  acceptance decisions for applicable accepted results, substantive checks and
  independent review of the full intended snapshot. Requirements-only publication
  requires no task ID, implementation evidence or not-yet-existing design. An
  explicitly authorized proposed document stays proposed after publication.
  Use `ris-port-op-review-change` for independent assessment of this concrete
  document subject; use `ris-proj-op-review-task` when a task-bound review applies.
  Review is required evidence, not content acceptance or a next-stage assignment.

Both branches converge here into the **one** Git algorithm below. Require exact
checked/reviewed base and complete final publication snapshot: base plus overlays,
additions, deletions and modes, including unchanged base files and exclusions
declared before review. Bind independent reviewer/context provenance to that
whole subject, not only changed paths or a dirty-tree fingerprint. Require
no unresolved high/medium findings, recorded low
dispositions (one collective decision suffices; low alone requires no repair,
task creation or new review round), integration and direct push authority.
Read current project rules,
Git status, diff, recent history, worktree mapping, remotes and tracking. Establish
the primary branch and selected remote from project evidence; do not assume the
literal name `main`, configure remotes or grant direct-write permission yourself.
Missing target/permission/checks/reviewer blocks publication with useful local
state reported. A task's in-progress status is not a publication gate.
Publication does not accept content, create tracker records or enlarge the
caller's authority. Check all outgoing history, not just the chosen subject's diff.

## Integrate, reassess, publish

1. Fetch the selected remote and inspect divergence and the full outgoing commit
   and file set. Preserve dirty/untracked user work; stage only authorized files,
   inspect staged diff and exclude secrets/local workspace/tracker storage. Do not
   send unrelated local commits just because this task's tip is approved. Use
   project-established integration policy; no force push, destructive reset,
   hook bypass or silent conflict resolution. If target has advanced, inspect the
   new code/contracts before integrating; conflicting dependent work stops.
2. If there are no intended changes, verify the existing result's applicable
   checks/review, decisions and required remote visibility; return its actual
   receipt without an empty commit or redundant push. Existing unsent commits
   still require the full outgoing gate. Otherwise commit intended changes using
   project history style. Integrate into the
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

Return `ok|partial|blocked|conflict|error`, subject kind/identity and exact paths
(confirmed ID only when applicable), source/target branches and remote,
commits/tree/ref, input/result versions and separate decision locators,
checks/review addresses, provenance and applicability, docs state, actual push
and remote-read evidence, preserved local effects and recovery needs. Persist
authorized evidence with an exact filename and read it back. With an ID use the
checked task evidence area only when authorized; without an ID use an explicitly
authorized address or the response and state any discovery gap. Never invent an
ID folder. For partial/unknown push reconcile actual local and remote effects
before retrying; preserve confirmed commits and unchanged decisions and give the
exact remainder. The caller checks the semantic whole and receipt; local notes
are not remote inputs. Stop at
Git publication: never declare the feature accepted, close tasks/parents, push
Dolt, deploy, create a PR or choose a subsequent operation.
