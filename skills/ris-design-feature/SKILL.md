---
name: ris-design-feature
description: >-
  Create or revise one RIS project's feature technical design from accepted
  requirements and current architecture, obtain independent design acceptance,
  save the scoped version and verify its feature-record links. Use for project
  feature design or focused redesign; not for choosing a feature, specifying its
  behavior, decomposing tasks, implementation, or portable unsaved design alone.
---

# Accept and save a feature design in a RIS project

Own the **combined project result**: sufficient accepted design, checked saved
scope/version and matching feature-record evidence. `ris-design-feature-base`
owns the portable read-only method; the selected adapter owns bounded tracker
operations. The wrapper is necessary for project discovery, authority, versions,
persistence and impact coordination; it does not duplicate the base's design
method. Direct invocation works in the current agent without an execution role
or a surrounding scenario. Stop at this result, without starting another stage.

## Establish inputs and permitted effects

Identify project, confirmed feature task ID and epic, permanent slug, create or
revise intent, linked spec/design, and the authorized file/record/optional ADR
changes. Ensure installed `ris-common` is available and apply its conditional
dialogue/artifact/quality resources before their actions. Apply installed
`ris-context` with its configuration resource for `sources.rules`, related
`sources.product`, `sources.specs`, and `adapters.tasks.skill`; check root,
provenance, diagnostics and permission scope. Do not infer project from the
skill's location or use defaults on invalid selected configuration.

Load the selected available adapter and check `tasks` v1 reads for exact task,
epic, all-status tasks, children and directed blockers; additionally require
`tasks.feature-record/1` with `tasks.features.read` and, for a saved combined
result, `tasks.features.update`. Check each operation's guarantees before any
dependent write. Read exact ID/type/parent and its identity block: slug, spec
path, requirements scope/digest and accessible acceptance address approving
that scope/version. Check actual document bytes, not the presence of a file.
Read prior design/history on revision and any existing verification; do not
guess a legacy slug, overwrite malformed blocks or silently migrate old tasks.
Legacy migration needs separate explicit authority, verified old links and the
adapter's initial-update guarantees. Title edits preserve slug and spec path.

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

Ensure installed `ris-design-feature-base` is available and **apply** its method
to the checked requirements/AC, observed code, applicable architecture/contracts,
related designs and prior design/delta. Inspect its actual proposal and coverage,
not just its name. Keep one dialogue, using known decisions and evidence without
reinterviewing unchanged requirements. Resolve missing technical facts from code
first. For interdependent unresolved technical decisions apply installed
`ris-interview-base` in the same dialogue with a bounded architectural topic and
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
effects; if unavailable, block that part. Prepare independent scopes/digests,
show the specific proposed design and impact to the project's acceptance authority,
and obtain a recoverable decision approving exactly this design scope/version.
Generic authorization, requirements approval, a commit or file presence does
not accept design. An unchanged requirements scope is not reaccepted merely
because design changed. Apply the resource's save, adapter update and read-back
checks; do not claim the combined result from a document write alone.

## Hand off and stop

Return `ok|blocked|conflict|error`, project/config provenance, confirmed feature
ID/epic/slug and spec/design paths, separate requirements and design scopes,
SHA-256 digests and acceptance addresses/status, observed code/contracts versions,
AC/test seams, relevant source currency and impact decisions, ADR/review evidence
where needed, independent work and unresolved blockers. Report actual saved
effects and fresh file/adapter read evidence, preservation of prior decisions,
write guarantees and limitations. Provide sufficient input for a recipient
without this dialogue; do not rely on an ignored local note as remote evidence.
Direct success concerns the checked **local** design/record result, not Git/Dolt
publication, decomposition or implementation readiness. If remote availability
is required by the caller, report each channel separately and require actual
independent remote checks under the caller's publication authority; one channel
alone is partial. This skill does not commit/push, close/claim work, create child
tasks or start implementation. Stop after the design result or precise partial
handoff; the caller owns transitions and any separate publication.
