---
name: ris-proj-op-design-feature
description: >-
  Create, accept and publish a RIS feature or explicit standalone work's design from accepted
  requirements and current architecture, obtain independent design acceptance,
  save its version and reconcile record links, or complete an explicitly
  requested document-only design without a tracker ID. Use for project feature
  design, focused redesign or bounded noninteractive save; not for choosing a
  feature, specifying its behavior, decomposing tasks, implementation, or portable
  unsaved design alone.
---

# Accept and save a feature design in a RIS project

By default own the **combined project result**: sufficient accepted design, checked saved
scope/version, Git publication and matching feature or ordinary standalone record
with tracker publication where applicable. `ris-port-op-design-feature`
owns the portable read-only method; the selected adapter owns bounded tracker
operations. The wrapper is necessary for project discovery, authority, versions,
persistence and impact coordination; it does not duplicate the base's design
method. Direct invocation works in the current agent without an execution role
or a surrounding scenario. Stop at this result, without starting another stage.

An explicitly requested **document-only** mode owns a complete accepted, saved
and checked/published design plus its separate decision evidence, before a task
exists. It is not an implicit fallback for failed combined work. Interview,
discussion and separate acceptance remain in the leading dialogue in a scenario.
Bounded formulation/accepted-content save may execute noninteractively in a
subagent; require
full exact candidate text with distinguishable version/scope, or a recipient-accessible
file at an exact address/version, accepted requirements inputs, destination
path/section, separate attributable design acceptance decision and permitted writes for save.
The caller owns that transfer. Read and validate complete content, version/scope
and decision/provenance without foreign-chat assumptions; return incomplete,
inaccessible, ambiguous or changed candidates before save. Do not reformulate
accepted content. Return missing decisions
to the caller without asking user questions, including through dependencies.
An explicitly limited optional draft-save contribution instead uses the resource's
pre-approval draft branch: full exact candidate/version/scope and agreed authorized
destination/write scope, without requiring or inventing design acceptance.
Direct invocation needs no configured execution role or new per-step skill.

## Establish inputs and permitted effects

Identify project, combined or explicitly requested document-only mode, selected
feature/slug, create or revise intent, linked requirements/design and authorized
file/evidence/record/optional ADR changes. Combined mode requires a confirmed
tracker ID (task or explicitly ordinary native bug); a feature's epic is optional
and checked when present. Document-only requires neither.
Full finished operation is default. An explicitly limited contribution names
proposal, optional pre-approval draft save, accepted local save or record-only
reconciliation from a checked Git receipt; nesting/Gas City does not select limited mode. Ensure
installed `ris-proj-lib-common` is available and apply its conditional
dialogue/artifact/quality resources before their actions. Apply installed
`ris-proj-op-resolve-context` with its configuration resource for `sources.rules`, related
`sources.product`, `sources.specs`, and only for tracker operations
`adapters.tasks.skill`; check root,
provenance, diagnostics and permission scope. Do not infer project from the
skill's location or use defaults on invalid selected configuration.

Before any document/evidence write intended for Git publication, including an
optional pre-approval draft, require the caller to supply an already prepared,
confirmed own branch and safe copy: work identity/association, repository/path/
branch/base, checked current state and adequate write/publication authority.
A suitable current copy is allowed; isolation or project rules may require a
worktree. Apply this to full combined/document-only calls and limited saves intended
for a caller's later publication. Validate the evidence and resolve destinations
in that copy. This wrapper does not create/switch branches or prepare copies;
neither does the publisher. Missing preparation blocks dependent publication before
writing. Independently authorized local/unpublished saving may proceed only within
project rules, stating the limitation and making no publisher call; do not silently
reduce a full request or promise later publication from a dirty primary copy.
Proposal-only and record-only calls need no new document working copy.

With an ID discover actual type/kind/key, own scope, source/decision links,
complete children and directed blockers through selected adapter reads. Retrieve
the actual accepted versions using common's conditional published-input reading
method; do not ask the user to repeat accessible facts or supply a prior receipt.
Missing/ambiguous/stale links block only the dependent result with an exact gap.
Explicit ordinary standalone work uses the adapter's advertised tool-specific
source update/reconciliation resource and guarantees, not feature-record/2 or
an invented epic/slug. Preserve structural parent and unrelated content. Simple
accepted constraints need no ceremonial design file; material design still needs
separate acceptance. A malformed/historical feature is never reclassified.

An explicitly selected native `bug` is ordinary work, not a feature task. Use
the adapter's advertised ordinary typed bug/children/blocker reads and authorized
source-link updates, not task-only feature APIs. Read its full current investigation
report (description section or exact published file), aligned criteria and accepted
behavior/constraints with actual authority. These sufficient inputs replace a
formal requirements file; research readiness alone does not accept behavior. Return
disputed expectations or stale/misaligned inputs before dependent design writes.
Resolve the material public-contract/data-model/responsibility/invariant choice
through this operation and **separate design acceptance**. Agree an ordinary design
document path without inventing an epic/feature slug. Execution-input snapshot is
not a prerequisite to design: it is fixed after necessary decisions. On resume
compare report/criteria/decisions and assess only affected design/evidence.
Pass this pre-execution design/document subject explicitly to review and Git
publication even when the bug ID exists. Its current report/criteria/accepted
constraints and exact accepted design/decision are sufficient input basis; future
execution snapshot, implementation or execution plan are not prerequisites to
that document result. The persistence resource carries this subject distinction
through both owners without waiving their independent whole-tree checks.

In the feature combined branch load the selected available adapter and check `tasks` v1 reads
for exact task, epic when present, children and directed blockers; use complete all-status task
selection only when related-design discovery or identity reconciliation needs it,
not merely because the feature ID is known. Additionally require
`tasks.feature-record/2` with `tasks.features.read` and, for a saved combined
result, `tasks.features.update`. Check each operation's guarantees before any
dependent write. Read exact ID/type/parent and its identity block: slug, spec
path, requirements `{path, revision, section, acceptance: {address, decision:
"accepted"}}` and its actual content/decision. Read prior design and current
verification on revision; Git owns displaced decisions, not tracker history.
Early null requirements are a precise missing accepted-input gate, not malformed
or ordinary kind. Before feature document writes require its pinned slug/spec
pair and same-ID checked own copy; a root feature needs no invented epic. A
non-null accepted design ref is required downstream even for inline design.
Historical unsupported records block dependent writes and remain intact; do not
guess a slug, overwrite malformed blocks or migrate in this operation. Title
edits preserve slug/spec. Document-only reads the supplied accepted requirements
and separate decision directly, including checked local pending-publication
inputs when authorized; it does not load the adapter solely to obtain an ID.

Select relevant product/rules/code/tests and related **active accepted** designs
from links, contracts and current tracker evidence, not a complete product scan.
Read the code's actual revision and contracts; distinguish existing architecture
from accepted future changes. Resolve only related source-version differences:
changed product behavior goes to its owner, missing baselines leave currency
unconfirmed. Do not rewrite product or publish future components as current
rules. Requirements acceptance is independent of design acceptance. Missing,
stale or disputed requirements block dependent design acceptance/writes; preserve
independent analysis and give the precise prerequisite rather than selecting
another feature. A closed feature needs separately authorized reopening or a
new approved work scope; do not mutate it as open work.

## Compose design and focused decisions

Read `references/acceptance-and-save.md` relative to this installed skill before
presenting a candidate, selecting accepted content, acceptance or any draft/accepted
save. If unavailable block that part.
For explicitly limited draft save, apply only its pre-approval draft branch to
the supplied full candidate; skip formulation, acceptance and accepted-content
persistence/publication. Return checked draft address/version/scope, actual effects
and limitations to the caller without asking the human in a subagent.
For bounded save of a verified accepted candidate, skip formulation/interview
and apply the persistence resource. For noninteractive formulation use supplied
decisions; return the full checked proposal with a distinguishable version/scope,
or an accessible file address/version when separately authorized, and unresolved
alternatives to the leading dialogue. That proposal is not an accepted saved
design; do not enter the interactive branches below in a subagent.

Ensure installed `ris-port-op-design-feature` is available and **apply** its method
to the checked requirements/AC, observed code, applicable architecture/contracts,
related designs and prior design/delta. Inspect its actual proposal and coverage,
not just its name. Keep one dialogue, using known decisions and evidence without
reinterviewing unchanged requirements. Resolve missing technical facts from code
first. For interdependent unresolved technical decisions apply installed
`ris-port-op-interview` in the same dialogue with a bounded architectural topic and
known answers; a single clarification does not need a full interview. Do not
turn that interview into a second functional requirements process.

Check the base's sufficient design, AC/test seams and compatibility against
the project evidence. For a conflict of common contracts coordinate a single
version and integration owner with affected owners, identify affected feature/
task IDs and necessary blocker direction, and obtain agreement before accepting
the dependent design. Independent portions stay available. Tracker edge changes
require specific permission and compatible adapter operations; propose them if
not permitted. For cross-feature edges check that the selected adapter actually
supports that scope; same-feature operations cannot be stretched to fit it.
No unresolved incompatible contract may be reported as accepted/ready.

On revision use the base's targeted impact analysis: affected AC, tasks, tests,
ADR and active designs, with exact references and versions. Local reversible
implementation choices leave accepted design intact. A substantive feature-design
delta needs focused acceptance; changed behavior needs its independent owner and
requirements decision; key architectural invariant/contract change needs separate
architectural authority. Propose ADR and independent architecture review by risk,
with appropriate permissions. Do not create ADR for every local choice, or treat
its accepted status as implementation. Preserve unchanged requirements evidence.

## Accept an independently versioned result

Default to an unambiguous separate design section in ordinary
`sources.specs/<slug>/spec.md` for a simple design, or `design.md` in that feature
directory when needed. Use verified existing links/project overrides instead of
moving files mechanically. Do not add OKF indexes/frontmatter to ordinary specs.
Read `references/acceptance-and-save.md` relative to this installed skill before
choosing the exact scope, obtaining acceptance or writing either document or
record. It owns the version/persistence protocol, including revisions and partial
effects; if unavailable, block that part. Prepare independent content selectors.
Before requesting separate acceptance of a new or materially changed design,
explain it in plain language: essence, main flow, reused/new technologies and why,
tradeoffs, material risks and irreversible/hard-to-reverse choices. Aim for roughly
one screen, not a measured limit; never hide material decisions to fit it. Identify
the exact COMPLETE candidate version/scope being accepted and keep its full text
accessible. A short full inline design may itself supply this explanation without
a duplicate summary. For a long design, the resource's optional authorized Markdown
draft branch may precede acceptance; no draft file/store is required. Show material
impact and obtain a recoverable decision approving exactly that complete design
scope/version, not merely its summary. For bounded supplied acceptance, validate
the actual candidate/decision instead of re-asking approval or opening dialogue.
Generic authorization, requirements approval, a commit or file presence does
not accept design. One act may accept both complete scopes only under the resource's
explicit two-selector/version protocol; a bounded save validates its design entry
without demanding another answer. An unchanged requirements scope is not reaccepted merely
because design changed. Apply the resource's save, adapter update and read-back
checks; do not claim the combined result from a document write alone.

## Hand off and stop

Return `ok|blocked|conflict|error`, project/config provenance, confirmed feature
ID/epic only when confirmed, mode/slug and spec/design paths, separate requirements
and design path/section/revision and acceptance addresses/status, verified
candidate text/version for an unsaved proposal or verified candidate address/version,
saved result addresses after saving and pending immutable refs, observed code/contracts versions,
AC/test seams, relevant source currency and impact decisions, ADR/review evidence
where needed, independent work and unresolved blockers. Report actual saved
effects and fresh file/adapter read evidence, preservation of prior decisions,
write guarantees and limitations. Provide sufficient input for a recipient
without this dialogue; do not rely on an ignored local note as remote evidence.
Full document-only `ok` requires accepted saved/read-back content and verified
Git publication; combined `ok` also requires matching record and tracker
publication. Explicit limited local/record contributions can be `ok` only for
their declared boundary, with exact remaining channels. Apply the resource's
review/Git/record/tracker sequence and inspect receipts; one channel alone is
insufficient for full mode: return the cause's `blocked|conflict|error`, completed
channels and exact remainder. No decomposition/implementation readiness follows from design success.
Do not close/claim work, create children or start implementation. Stop at the
requested result; the caller owns transitions after limited contributions.

For a noninteractive component return a short handoff: status, scope/mode,
full unsaved proposal with version/scope or verified saved result address and
candidate revision or confirmed ID, decision/evidence, limitations, actual effects
and decision needed. The caller forwards complete text/version or an accessible
file address/version with the separate decision to the next recipient; the
consumer reads and checks it without foreign chat. Never substitute an unverified
"done" for this result or require a file for a response-only proposal.
