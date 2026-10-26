# Developing RIS

Read [AGENTS.md](../AGENTS.md), the complete
[development rules](rules/development.md) and root [ris.yaml](../ris.yaml) before
changing the repository. Source skills live in [`skills/`](../skills/), command
templates in [`commands/opencode/`](../commands/opencode/); installation is
synchronized from these sources.

The client-only `/ris-help` entry lives in `plugins/opencode/ris-help/`, installed
at `.opencode/plugins/ris-help/` with paired server/TUI entrypoints. Its `pages/`
is the sole bilingual fixed-help source, shared with direct help-skill calls.
Do not recreate `commands/opencode/ris-help.md` or duplicate pages inside a skill.
The installer owns the exact plugin directory only with shipped ownership evidence;
all other plugins/global configuration remain foreign. Update isolated installed
mirrors alongside source; preserve historical accepted specifications.

Deterministic client checks (no agent sessions):

```sh
node --test tests/client_help/help.test.mjs
RIS_OPENCODE_RUNTIME="$(command -v opencode)" python3 -B -m unittest discover -s tests/client_help -p test_runtime.py -v
```

The opt-in runtime check pins installed OpenCode 2.0.32, uses a disposable project
and isolated XDG directories, renders the production TUI module and validates the
actual skill-attachment prompt schema with `resume:false` (no agent/model call).
Unit doubles establish routing only, not runtime compatibility. Current V2 docs:
[discovery](https://opencode.ai/v2/docs/cli/plugins),
[TUI API](https://opencode.ai/v2/docs/build/plugins/cli),
[client](https://opencode.ai/v2/docs/build/client). The installed client uses
`session.prompt({sessionID,text,skills,delivery})`; do not copy outdated
`session.command({command,arguments})` examples into forwarding code.

Development state and dependencies belong to Beads (Dolt). New local task notes
live in the primary copy's `.sdlc/tasks/<confirmed-ID>/`; `tasks/PLAN-*` is a
historical archive. Git push does not synchronize Beads. Follow the rules for
review and separate Git/tracker publication and completion.

Ordinary project review uses one local `review.yaml` under the
[ris.review/2 owner](../skills/ris-proj-op-review-task/references/report-format.md).
Existing /1 files continue conditionally without migration. New compact rounds
use assessment, new findings and dispositions; no six fixed coverage mappings or
repeated per-check tree. Machine approved/changes_required/blocked distinguishes
proceed/repair/stop; invalid/unsupported/missing evidence is never a repair loop.
Beads stores only address/round, not verdict/findings. Fast review is conditional
as below; active review permits session-only evidence, optional save uses the same format. YAML parsing checks syntax,
not schema/approval: assess final subject, inputs, checks and actual independence
separately. The owner documents the bundled read-only Python validator, its
explicit venv dependency installation, CLI and distinct format/setup outcomes.
It checks mechanics, not external approval; self-review remains analysis only.
No historical report migration or author TDD-history audit is added.

Validator program tests (after explicitly authorized installation from the
skill's `requirements.txt` into the selected venv):

```sh
/path/to/venv/bin/python -B -m unittest discover -s tests/review_validation -p 'test_*.py' -v
```

These exercise both /1 and /2 synthetic reports and the same CLI, including an isolated skill copy
without Git/Beads executables, not live agents or actual evidence/approval.

For current readiness and limitations use the [README entrypoint](../README.md#current-readiness-and-limits),
not this guide or historical delivery reports as a second readiness register.

Handoff/recovery uses the [common artifact contract](../skills/ris-proj-lib-common/references/artifacts.md)
for fact producers/consumers, mutable sources and lost evidence. In-session owners
reuse available inputs; delegates get only missing exact sources, permissions and
a bounded expected result, without inherited-chat assumptions. New sessions start
from project+ID and Git/config/tracker sources. Flows select the first missing or
inapplicable result; context/copy/Git/history/guards/sandbox/Dolt algorithms and
uncertain-effect reconciliation stay with their infrastructure owners. There is
no receipt envelope, registry or transition journal. Missing review/check/acceptance
never creates historical pass: restore required exact evidence or obtain honest current
review/affected checks/only the lost human scope. Confirmed pushes and closed
statuses are reused, not replayed. These are instruction contracts; static
inspection does not establish live recovery behavior. Eligible Fast owes no absent
inapplicable review, but known adverse findings and changed risks remain material.

Feature preparation follows the current [SDLC methodology](product/08-sdlc-methodology.md):
early same-ID registration/copy, one requirements/design dialogue and
sufficient direct/inherited/mixed basis of both scopes (new decisions only on new
material; one act allowed), independent review/Git, same-ID
ordinary record and existing full decomposition with separate tracker publication. Internal
executors are optional; independent review is actually separate. Sufficient inline
design needs no design.md. Direct component operations remain available. This does
not start implementation after prepare.

Preparation depth `auto` (default), `compact` or `full` belongs to the request,
not config or tracker metadata, and is independent of boolean `auto_accept`.
The existing flow accepts Feature ID, Epic ID + chosen idea or standalone idea
without mandatory roadmap/epic. It applies sufficient reuse-first inline design
and one-task-first independent-result decomposition in either depth; explicit
Compact expansion requires only the necessary agreed scope, Full is not downgraded.
Source owners define the method; see the [flow](../skills/ris-proj-flow-prepare-feature/SKILL.md).

One author context reuses stable context/preflight until material drift/copy change/
loss; internal contributions validate supplied results instead of restarting
standalone ceremonies. Live write guards remain fresh. Native same-record
`feature-preparation` assignment is not a second execution claim. Dialogue asks
only new material choices (a related ordered block or early blocking fork is
valid); draft review is optional, final independent publication review and changed-
snapshot reassessment remain. Short sufficient spec/design includes AC/how-to-check,
no quotas/backlog/status/checklist or architecture recap. Obvious splits need no
new approval; changed scope/delivery/obligations do. Verify the full one-task or
child/edge composition and assigned combined check, then separately publish final
Dolt. Partial Git/record/children success is not complete; resume inspects existing
sources and finishes only missing effects without new markers/matrices/reports.

Full preparation carries ordinary Git/tracker publication authority across owners,
subject to explicit project/user limits and the actual outgoing-history scope.
Limited child saves return to the lead for continued review/publication/decomposition;
they never silently reduce the request. A missing permission needs one concrete
question, a technical failure an exact blocker. Shared Dolt policy is agreed once
per project, not inferred from one feature's authorization or installed settings.

There is no feature JSON, duplicate accepted refs/readiness or mandatory saved
verification. New feature
documents use configured `sources.specs/<full feature ID>/spec.md`, readable H1
then column-zero Feature-ID/Summary/optional Keywords; design is inline or adjacent.
Independent scope/version basis and original containing-commit provenance remain.
The common published-inputs owner checks original accepted sources, applicability
and actual derivation, not mere compatibility; wholly inherited results need no
new approval/acceptor. Mixed results retain source provenance and decide only new
material in the full candidate context. No schema/sidecar/assertion registry is added.
Legacy links/payload hints locate real documents, without schema gates, migration
or title-derived paths. Missing/old/malformed JSON alone is not a blocker. Ordinary,
document-only and bug subjects keep their paths/contracts. Bugfix uses the
[versioned-basis contract](product/06-artifacts-and-handoff.md#41-воспроизводимое-основание-bugfix)
and the adapter's complete historical read/short locator reconciliation, without a
mandatory duplicate full snapshot or new file. Legacy snapshots and review YAML
are not migrated. Historical specifications/evidence are not rewritten.

Execution uses sufficient accepted inputs/current code without a standalone planner, saved
plan/omission-decision or implementation report. Do not replace/distribute the
removed journal in other artifacts. TDD stays with the executor; final-result
review/recovery do not require saved author RED/GREEN chronology. Current checks,
independent review, safe publication and separate tracker gates remain.
This contract description is not evidence of publication, independent approval
or complete lifecycle acceptance; each requires its own applicable observations.

No default `worktree.md`/`execution.md` or equivalent transition ledger is required.
Keep the independent review report and sufficient
Beads result required by the rules, not a substitute implementation log.
Use live Git/Beads and accessible exact owner results at transitions; missing
association, reviewed-snapshot identity or independence blocks only the dependent
step. Ordinary creation without hooks/setup checks registrations, target/ref,
pinned base and the new copy, without hashing all primary/sibling contents.
Reuse and hooks/setup activate scoped preservation. Context validates the entire
config on selection/change, reuses unchanged validity and refreshes local paths/
association after a copy change. It compares only settings used by the recipient;
a valid unused product-source difference is not a handoff blocker.
See [the read/action comparison and check limits](specs/worktree-preparation-simplification/delivery-checks.md).
Those historical checks remain tied to `d8c5bac6164eeb559d07e987f42c12467141477a`;
this guide does not establish new live behavior or regrade the historical report.

Explicitly or naturally selected [Fast](../skills/ris-proj-flow-execute-simple-task/SKILL.md)
uses the [accepted ris-ci3.1 S1/D1](specs/ris-ci3.1/spec.md) boundary: one small,
locally bounded, understood and checkable request/idea, without product-logic,
architecture or material shared/public-contract changes. Code/config/docs/tools/
ignored/external can qualify by consequences/checks, not extension/diff size.
Coordinated independent outcomes, broad/unknown consequences or insufficient checks
need targeted scope agreement, not automatic SDLC restart. Empty input asks for work.
One main agent, default zero subagents; no mandatory preparation/plan/handoff/log/
review files. **Short Beads accounting remains mandatory in RIS**, with same-ID/native
kind, claim/composition/blocker guards and no feature/bug/container downgrade.
Self-check and mandatory checks/TDD remain. Independent review is required by explicit
request, mandatory applicable target-project policy or concretely explained material
risk, not code/external location/Git push alone. General RIS review wording does not
cancel this exception. Inactive review loads no role/format and needs no skip report;
active `task-review` must actually be independent, with high/medium repair and applicable
new consideration. Unavailable mandatory review blocks dependent gates. Changed snapshots
get affected self-check and renewed admission/risk assessment, plus independent review when required.
Versioned edits need one own branch/dedicated worktree through the existing preparer,
reused across stages/sessions; the source folder is never a development or branch-return
target. Local-only instead changes authorized actual targets without empty copy/dummy
SHA/push. Mixed preserves both boundaries, foreign data and shared-resource conflict checks.
Git-only retains outgoing/integration/non-force/remote gates; no-change verifies the
necessary existing state without empty commit/push. Local-only completion needs useful
actual-target evidence/availability limits, not Git SHA; mixed requires both parts.
Result, exact close/read-back and Dolt publication stay separate; Dolt does not publish
local files. Full/feature/bug/direct-review and non-Fast publisher gates remain unchanged.
Installation/update and agreed pre-Git bootstrap keep their explicit-target exceptions;
later versioned edits require worktree-first without dirty-file transfer. Historical
[D2](specs/fast-task-execution/design.md) and [ris-ppw](specs/ris-ppw/spec.md) decisions
retain their original versions, not alternate current algorithms.

Ordinary container closure trusts a nonempty complete direct-child set (all
`closed`) and checks parent blockers, without recursive delivery/acceptance audits.
Closure-feasibility questions use the same reads without writing. Explicit
verify/verify-and-close remains substantive; zero-child features retain own-result
verification. See the [current container rules](rules/development.md#отдельные-намерения-для-контейнера).

After verified task close and tracker publication, full execution (including bugfix) delegates
the eligible ancestor chain to one fresh `container-completion` subagent (RIS:
`standard`); Fast runs the same ascent inline in the main agent, with no mandatory
closure role/subagent. The shared [flow tail](../skills/ris-proj-flow-execute-task/references/ancestor-completion.md)
uses the existing exact-container owner at each level, confirms tracker publication,
and stops at the first unfinished/blocked parent. Explicit restrictions win;
no-parent is a no-op. Leaf completion survives cascade failure, whose remaining
effects stay explicit in the combined result. Direct status/verify/container close
does not cascade; recovery never replays confirmed close/push. No new model tier.

For routine Beads inventories use the adapter's native compact forms, for example
`bd list --all --limit 0 --type task --brief --json` (or `--type epic`). For a
known ID use `bd list --id <id> --all --limit 0 --brief --json`, checking exact
cardinality and actual type; no global queue reread is needed just for that ID.
Children use `list --parent <id> --all --limit 0 --brief --json`; directed blockers
use `dep list <id> --type blocks --direction=down --json`. Counts do not replace
edges. Missing parent/spec fields need bounded exact/edge reads. Disclose necessary
content with `bd show <id> --brief-deps --json`: this keeps the full own record,
not a single-field projection. Omitted brief fields are not empty. Absence/dedup
still needs complete all-status/unlimited coverage and every field needed for
key/slug/spec/content predicates, including historical descriptions when relevant.
Errors, `no value`, malformed or truncated output cannot prove absence. Full
native JSON remains a fallback; do not use the failing Go-template projections.

Git publication uses native fetch/push `--quiet`; Dolt publication uses
fetch/push `--silent` for progress. Preserve stderr, exit status and verified
results without a mandatory new log. Git whole-outgoing-history checks, exact
whole-candidate publication and independent remote read-back remain required;
review follows the narrow Fast exception above, otherwise remains independent. Dolt
uses authorized shared-main scope, ordinary non-force publication and fresh remote
revision/reachability assurance, with local exact-content checks kept separate.
See the [Beads adapter](../skills/ris-proj-adapter-beads-tasks/SKILL.md) and
[Git publication owner](../skills/ris-proj-op-publish-task/SKILL.md).

The current source contract separates confirmed remote Git from optional safe
source-copy maintenance, activated by an explicit request or applicable accepted
project policy and limited to
safe FF on an already suitable branch, never switching. Skipped/failed updating does not block exact
close or Dolt; policy-required or explicitly requested updating retains its own
unfinished combined-result part. Caller checks/forwards actual policy provenance
and boundaries; publisher verifies them, never infers dependency-refresh rights
from FF permission. RIS's bounded `main`/`origin/main` policy is in the development
rules; projects without a policy retain remote-only. See the
[amendment](specs/policy-primary-sync/amendment.md).
Context derives the source folder from the actual shared `.git` directory in the
supported one-repository/one-project layout, without saved-primary discovery or
mutation rights. Workspace leaf defaults apply even with a valid selected config;
explicit overrides win, absent output folders never select another path. Sources
remain current-copy paths; sources/adapters/roles get no missing-field defaults
from a selected file. Claim owners resolve a new actor
from explicit/configured identity or verified host-session ID, not as takeover
authority by itself. An explicit human continuation/execution request for that
task supplies guarded reassignment authority without a second takeover question,
lease wait or proof the old session ended. The associated copy/branch and changes
are preserved; concrete conflicts and native guards remain binding. Full requests
carry ordinary constituent actions across owner seams;
technical failures are exact blockers, not repeat permission questions. RIS's
standing shared Dolt policy is repository-local; other projects keep theirs.
This describes the source contract, not evidence of remote publication or
observed agent behavior; static checks establish instruction consistency only.

Ordinary Beads record writes and heartbeat use `bd --sandbox ...` under the
adapter's own contract, independent of consumer project rules. Heartbeat's lease
update is node-local, but its command can commit pending changes and invoke native
auto-push. Initialization keeps its separate authorization and side-effect checks;
sandbox is neither content CAS nor suppression of foreign hooks. Tracker
publication still uses the separate native Dolt route and its remote gates.

Feature preparation uses strict boolean `workflows.prepare_feature.auto_accept`
(default `true` even in existing configs with an omitted leaf or absent optional
root). Context owns validation/provenance; prepare alone applies separate scope
modes and explicit approval overrides. Direct specify/design never enable auto
from config. Read/check policy basis under common published-inputs, including
historical setting/default, exact scopes/versions and prepare request/limits;
do not relabel it human approval or inheritance. Interview for material gaps,
independent review and separate publications remain. Auto saves complete documents
without formal confirmation/full-text chat duplication; repairs/resume preserve
actual decisions. Invalid config never falls back. This is an instruction contract,
not observed agent behavior; inspect routes/config clauses, links and source/install
parity, not live/scenario agent tests. No executable config parser is introduced.

## Package-installation checks

These are deterministic filesystem/CLI tests, not agent sessions:

```sh
python3 -m unittest discover -s tests/package_installation -p 'test_*.py' -v
PYTHONDONTWRITEBYTECODE=1 RIS_TEST_BASH=/bin/bash python3 -m unittest discover -s tests/package_installation_integration -p 'test_*.py' -v
bash -n skills/ris-port-op-manage-installation/scripts/ris-install.sh
```

The [CLI workflow](../.github/workflows/package-installation.yml) checks lock/copy
feasibility and the mechanism suite against minimal Git fixtures. The
[production integration workflow](../.github/workflows/package-installation-integration.yml)
captures the actual source package into a disposable upstream and checks lifecycle,
recovery and the README bootstrap. Both run on Linux and macOS with explicit
`/bin/bash` (3.2 on macOS) and externally installed flock.

The bootstrap integration test extracts the first `bash` block in README and
substitutes its project/ref inputs. Preserve that entry point when editing docs.
Workflow definitions are not evidence of a successful remote run; check actual
results and their applicability to the revision being assessed.

## Architecture, plans and delivery records

- [RIS product knowledge](product/index.md) and the
  [target SDLC methodology](product/08-sdlc-methodology.md) describe architecture
  and future components; they are not an installed inventory.
- [Repository rules](rules/index.md) include the current owner map. Product and
  rules are separate OKF 0.2 bundles under the [knowledge profile](product/knowledge-profile.md).
  RIS uses `docs/product/` as its product source, including normative methodology
  and design; acceptance and readiness still depend on the selected operation.
- [Delivery specifications](specs/README.md) are ordinary Markdown. Historical
  names and immutable decision references are interpreted through the
  [namespace transition guide](skill-command-naming-migration.md).
- Installation: [specification](specs/package-installation/spec.md),
  [design](specs/package-installation/design.md),
  [delivery plan](specs/package-installation/delivery-plan.md).
- Continuity: [delivery records](specs/sdlc-continuity/).
- Retrospectives: [design](specs/session-retrospective/design.md) and
  [CLI policy amendment](specs/session-retrospective/cli-read-policy.md).
  The current [reader contract](../skills/ris-proj-op-retrospect-session/references/opencode.md)
  adds OpenCode V2 (2.0.32 baseline) without rewriting the historical decisions.
  Its deterministic parser/transport/metric regressions run with
  `python3 -B -m unittest discover -s tests/session_retrospective -p 'test_opencode*.py'`.
  They test the Python reader, not live agent behavior; the old `real_checks.py`
  agent scenarios are historical evidence, not a command to rerun.
- Task execution: [delivery checks](specs/task-execution/delivery-checks.md).

Delivery evidence is bound to its original inputs and revision. Reusing it requires
checking applicability; a documentation edit does not establish new runtime,
review, integration or publication outcomes.
