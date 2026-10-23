---
name: ris-proj-op-publish-task
description: >-
  Integrate an independently reviewed RIS project change with optional task ID, or a pre-ID document result, into the project's
  established primary Git branch and verify authorized direct push; source-copy maintenance needs an explicit request or accepted project policy. Use for
  authorized Git publication, including requirements-only documents; not content acceptance, PR creation, deploy, tracker/Dolt publication,
  feature acceptance or task/container completion.
---

# Integrate and verify Git publication

Own one bounded Git integration/publication result: confirmed remote publication,
with no local source-checkout maintenance by default. An explicit request or
accepted project policy can authorize a separate local maintenance effect; never switch its branch.
An unavailable/unsafe local update never blocks remote publication, exact task
completion or separate tracker publication. If local updating is authorized by
the request or applicable policy, retain that unfulfilled part separately; do not silently
drop it or call the whole combined request complete. One skill suffices: this is
an operational Git result, not a distinct portable content method. Load/apply
`ris-proj-lib-common` and applicable resources, and `ris-proj-op-resolve-context` for project rules and
evidence paths when needed and source-folder identity only for authorized
local maintenance. Load the selected task adapter only for necessary identity/
blocker/ownership reads; this operation never writes or publishes tracker state.
Direct invocation requires no execution role.
Reuse already available current owner instructions. For a supplied native bug,
read `references/bug-subject.md` from this installed folder before selecting the
publication basis; ordinary tasks and documents do not load it.

## Select the subject, then gate the common result

Require one explicit bounded subject and authorized effects; do not fabricate a
task or acceptance to fit this operation. Select the applicable input branch:
Choose by the actual publication subject: an existing native bug ID does not turn
pre-execution design/documents into fix implementation. Mixed fix/document changes
use Task/change and retain all implementation/snapshot guards below.

- **Task/change:** selected project, attributable agreed request, outcome,
  boundaries/criteria, accepted technical constraints/material decisions and
  exact copy/branch/base/candidate, implementation/docs/check evidence and
  independent review. A sufficient accepted request needs no separate spec/design/
  plan files. The task ID is optional; no-ID implementation belongs here, not in
  Documents. Its absence does not waive project-required tracking or other gates.
  With an ID, load/apply the selected adapter, discover its applicable accepted
  requirements/design/contracts and freshly check typed identity, membership,
  blockers and ownership where execution requires
  claim; an old receipt/lease is neither permission nor general content/graph CAS.
  Active blockers or lost required ownership stop dependent publication. Recheck
  mutable task gates before the action; the receipt does not supply write authority.
  Without an ID do not require an adapter or fabricate a record/task directory.
  Supplied feature/ordinary/bug identities retain their real contracts; absent or
  malformed feature data cannot select ordinary admission.
- **Documents (including pre-ID):** exact project-relative paths and subject/scope, separate
  acceptance decisions for applicable accepted results, substantive checks and
  independent review of the full intended snapshot. Requirements-only publication
  requires no task ID, implementation evidence or not-yet-existing design. An
  explicitly authorized proposed document stays proposed after publication.
  Use `ris-port-op-review-change` for independent assessment of this concrete
  document subject, or `ris-proj-op-review-task` when project-integrated review
  applies, with or without an ID.
   Review is required evidence, not content acceptance or a next-stage assignment.
   An existing ID may accompany a document-only planning subject for identity
   discovery; it does not require future implementation evidence or design for
   requirements-only publication. Check its applicable identity/authority/blocker
   gates, but do not treat document publication as task execution or claim it.

When consuming saved project review evidence, read/apply the installed
`ris-proj-op-review-task/references/report-format.md` before the gate. Ordinary
project review requires one
accessible local supported YAML (/2 for new files; conditional /1 compatibility)
and explicit round selector, including no-ID
document subjects at their authorized path. Portable assessment contributes content
but does not bypass the ordinary project save contract. Explicit fast execution
may instead supply its sufficient independent session result; no mandatory file
is introduced there, and an optional save uses the same format. Keep format
validity separate from approval applicability: apply that owner's two consumer
results with expected work/scope, publication purpose, full tree/base/exclusions,
input versions, sufficient assessment/checks and actual invocation/all-author evidence.
Require its external approval gate before push. For fast session-only evidence
check these substantive predicates and repair/history applicability without YAML;
do not load serialization resources unless a saved review file is used.

Valid applicable independent `approved` proceeds without another repair/review
loop. `changes_required` needs correction and new independent assessment;
`blocked`, missing/invalid/unsupported/inapplicable evidence or setup failure
stops the dependent gate, not an automatic implementation loop. Do not fall back
to an old approval past later adverse or unknown evidence.

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
PR-only policy, forbidden direct push or missing target/permission/checks/reviewer
blocks publication with useful local state reported. A task's in-progress status
is not a publication gate.
Publication does not accept content, create tracker records or enlarge the
caller's authority. Check all outgoing history, not just the chosen subject's diff.
Direct-push authority may be supplied by the full parent operation or accepted
project policy, not only a new publication-specific human message. Verify its
source, subject, destination and exclusions; do not re-ask when already covered.
An explicit project requirement for further approval remains binding. Return the
exact missing authority to the lead (or ask the specific question on direct
invocation), never reinterpret the parent's scope as local-only. This does not
authorize unrelated outgoing commits, a new remote/ref, force or bypassed review.

## Integrate, reassess, publish

Check applicable project instructions/rules for accepted local-maintenance policy
on every invocation, including direct, no-change and recovery calls; verify any
policy forwarded by the caller against its actual source and acceptance. Do not
infer it from push rights, installed settings or an example. Without an explicit
request or applicable accepted policy, keep the remote-only default: no local
maintenance identity resolution or writes. With either authority source,
read/apply `references/primary-sync.md` before that action, including
no-change/recovery calls. It owns safe FF and evidence; context owns source-folder
identity. A local identity/safety gap blocks only that local action, never remote.

Use native `git fetch --quiet` and `git push --quiet` for routine network
progress, with the explicit selected remote/refspec required below. Keep stderr,
command exit status and the verified result/receipt available; do not redirect
errors away, mask failure with a pipeline or infer publication from silence.
No new log file is required. Quiet output does not replace outgoing-history
inspection, independent review or remote read-back.

1. Require an already prepared, confirmed own branch and safe working copy as the
   publication workspace, with or without an ID (for pre-ID documents, its own
   authorized document branch/worktree). Require a registered dedicated worktree
   distinct from the ordinary source folder, also for simple or no-ID work. Ambiguous
   ownership, overlapping foreign changes or a busy shared copy block dependent
   publication until the caller supplies safe preparation through existing owners.
   This operation does not prepare worktrees or create work branches. All branch
   switching is forbidden, including a post-confirmation return to primary.
   Never reset primary/main or use the local primary branch for integration.
   One publisher owns this subject, not every project's publication. Fetch the
   latest established primary branch from the selected remote and inspect its
   new code/contracts, divergence and the full outgoing commit/file set.
   Preserve dirty/untracked user work; stage only authorized files,
   inspect staged diff and exclude secrets/local workspace/tracker storage. Do not
   send unrelated local commits just because this task's tip is approved. Use
   project-established integration policy; no force push, destructive reset,
   hook bypass or silent conflict resolution. Conflicting accepted scope or
   authority returns to its owner; ordinary merge conflicts are resolved in this
   own copy within the accepted scope and checked below.
2. If there are no intended changes, verify the existing result's applicable
   checks/review, decisions and required remote visibility; return its actual
   remote evidence without an empty commit or redundant push; local maintenance
   runs only under an explicit request or applicable accepted project policy. Existing unsent commits
   still require the full outgoing gate. Otherwise commit intended changes using
   project history style in this own branch/copy. Merge the fetched latest
   established primary remote branch into it, resolving conflicts there; do not
   use shared local main as an integration workspace. Record resulting commit and
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
   rerun affected checks and obtain independent reassessment of the integrated version
   before push. A clean merge or an unchanged task diff does not prove the old
   review covers the new whole tree. The reassessment identifies the full new
   snapshot and may reuse still-applicable review/check evidence for unaffected
   parts. Remote advancement alone does not restart planning/implementation,
   repeat all checks or renew acceptance of unchanged documents. Reaccept only
   substantively changed results through their owner. Do not reuse failed/unavailable checks.
3. Confirm architecture documentation's factual claims on that actual integrated
   tree; pending-integration statements must now match facts. Any required doc
   correction changes the tree and is subject to the same check/review gate.
4. Reinspect target/remote and complete outgoing scope immediately before direct
   push; send the checked resulting own-branch commit to the authorized primary
   remote ref with an explicit source:destination refspec and normal non-force
   push after all remote publication gates. Local primary safety is not a push
   gate. Do not move
   shared local main before remote confirmation. On remote advancement/rejection,
   freshly fetch and reconcile refs, merge the new target in this own copy,
   resolve conflicts and repeat only affected integration/check/reassessment
   steps before the next push. On ambiguous response independently inspect the
   remote for the sent SHA before retry; reuse confirmed effects, do not recommit
   or overwrite divergence blindly. Local commits are not publication.
5. Read the selected remote branch independently (remote ref query and fetch or
   separate clone as project requires). Verify the sent commit is visible/reachable
   and expected files/tree match its snapshot. Later allowed remote commits do
   not negate a verified earlier snapshot. Record exact sent SHA/tree and remote
   evidence, not merely command exit. On failed verification return the stopping
   cause's `blocked|conflict|error`, confirmed local/remote effects and the exact
   remaining check; reconcile an uncertain push before repeating it.
6. After confirmed remote publication, perform no source-copy writes by default.
   An explicit request or applicable accepted project policy activates the separate
   safe-FF resource; verify its authority and boundaries, never weaken its guards.
   Dependency refresh is not implied by FF authority: apply only its separately
   authorized conditional branch. Report local FF and dependency effects separately
   as updated/skipped/failed/unknown, with exact causes and remaining work.
   Ordinary Git publication is `ok` once its remote gates succeed.
   If local updating is required by the request or applicable policy, the combined result retains its
   causal non-`ok` status and exact local remainder; its confirmed Git result is
   still successful and consumable by completion/Dolt owners. Retry checks facts
   first and never republishes S just to repair local maintenance.

Return `ok|blocked|conflict|error`, subject kind/identity and exact paths
(confirmed ID only when applicable), source/target branches and remote,
commits/tree/ref, input/result versions and separate decision locators,
checks/review addresses, provenance and applicability, docs state, actual push
and remote-read evidence, publication scope and remote-only default when no local
authority applies. State the checked authority source (request or policy locator/
version/acceptance), exact copy/remote/ref/effects and exclusions, or its absence/
conflict. For authorized maintenance include source-folder association, before/after
local ref/HEAD/tree, dependency outcome when applicable, and safety/read-back evidence
or its pending cause. Never claim the combined result complete with an unmet
policy-required or explicitly requested effect. Include preserved
local effects and recovery needs. Persist
authorized evidence with an exact filename and read it back. With an ID use the
checked task evidence area only when authorized; without an ID use an explicitly
authorized address or the response and state any discovery gap. Never invent an
ID folder. For partial/unknown push reconcile actual local and remote effects
before retrying; preserve confirmed commits and unchanged decisions and give the
exact remainder. The caller checks the semantic whole and receipt; local notes
are not remote inputs. Stop at
Git publication: never declare the feature accepted, close tasks/parents, push
Dolt, deploy, create a PR or choose a subsequent operation.
