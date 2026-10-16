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
Bounded formulation/save may execute noninteractively in a subagent; require
full exact candidate text with distinguishable version/scope, or a recipient-accessible
file at an exact address/version, accepted requirements inputs, destination
path/section, separate attributable design acceptance decision and permitted writes for save.
The caller owns that transfer. Read and validate complete content, version/scope
and decision/provenance without foreign-chat assumptions; return incomplete,
inaccessible, ambiguous or changed candidates before save. Do not reformulate
accepted content. Return missing decisions
to the caller without asking user questions, including through dependencies.
Direct invocation needs no configured execution role or new per-step skill.

## Establish inputs and permitted effects

Identify project, combined or explicitly requested document-only mode, selected
feature/slug, create or revise intent, linked requirements/design and authorized
file/evidence/record/optional ADR changes. Combined mode requires confirmed task
ID; only the feature branch requires an epic. Document-only requires neither.
Full finished operation is default. An explicitly limited contribution names
proposal, accepted local save or record-only reconciliation from a checked Git
receipt; nesting/Gas City does not select limited mode. Ensure
installed `ris-proj-lib-common` is available and apply its conditional
dialogue/artifact/quality resources before their actions. Apply installed
`ris-proj-op-resolve-context` with its configuration resource for `sources.rules`, related
`sources.product`, `sources.specs`, and only for tracker operations
`adapters.tasks.skill`; check root,
provenance, diagnostics and permission scope. Do not infer project from the
skill's location or use defaults on invalid selected configuration.

With an ID discover actual type/kind/key, own scope, source/decision links,
complete children and directed blockers through selected adapter reads. Retrieve
the actual accepted versions; do not ask the user to repeat accessible facts.
Missing/ambiguous/stale links block only the dependent result with an exact gap.
Explicit ordinary standalone work uses the adapter's advertised tool-specific
source update/reconciliation resource and guarantees, not feature-record/1 or
an invented epic/slug. Preserve structural parent and unrelated content. Simple
accepted constraints need no ceremonial design file; material design still needs
separate acceptance. A malformed/historical feature is never reclassified.

In the feature combined branch load the selected available adapter and check `tasks` v1 reads
for exact task, epic, all-status tasks, children and directed blockers; additionally require
`tasks.feature-record/1` with `tasks.features.read` and, for a saved combined
result, `tasks.features.update`. Check each operation's guarantees before any
dependent write. Read exact ID/type/parent and its identity block: slug, spec
path, requirements `{path, revision, section, acceptance: {address, decision:
"accepted"}}` and its actual content/decision. Read prior design and current
verification on revision; Git owns displaced decisions, not tracker history.
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
selecting accepted content, acceptance or save. If unavailable block that part.
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
effects; if unavailable, block that part. Prepare independent content selectors,
show the specific proposed design and impact to the project's acceptance authority,
and obtain a recoverable decision approving exactly this design scope/version.
Generic authorization, requirements approval, a commit or file presence does
not accept design. An unchanged requirements scope is not reaccepted merely
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
