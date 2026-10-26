# RIS · FULL HELP

### 🧭 PROJECT PLAN

**`/risp-status [ID]`**

Show the complete unclosed project plan or the selected subtree, dependencies
and blockers. Read-only; does not start work.

---

### ➡️ NEXT STEP

**`/risp-next <ID>`**

Recommend the next prompt, necessary decision or blocker for selected work.
Does not execute the recommendation or certify readiness.

---

### ❓ FOCUSED HELP

**`/ris-help <topic>`**

Explain one command, comparison or route. Use `/ris-help` for daily help.
Recommendations are explanations, never permission to execute them.

---

## PAGE 1 · PROJECT PREPARATION

### 📦 PACKAGE INSTALLATION

**`/risb-installation`**

Install, update or uninstall the complete RIS package in an existing selected
project directory. Does not initialize the project. Restart OpenCode after
package changes.

---

### 🛠 PROJECT INITIALIZATION

**`/risp-init <project and scope>`**

After installation, prepare or safely resume agreed settings, agent instructions,
RIS infrastructure and separately accepted product/architecture/engineering
documents, reusing suitable existing material. Check combined local readiness
and report deferrals. Publication is separate. Stop before roadmap, development
or product build/test/format/CI setup.

---

### 🌱 PRODUCT FOUNDATION

**Direct skill: `ris-proj-op-author-product-foundation`**

Create or make a bounded update to purpose, users, tasks, capabilities, boundaries
and constraints. Separately accept the complete content, then save/check within
configured `sources.product`. This is input for a roadmap, not every future
feature's specification. Does not initialize or publish the project.

---

### 🏛 ARCHITECTURE RULES

**Direct skill: `ris-proj-op-author-architecture-rules`**

Formulate, separately accept and save project architecture norms or a bounded
amendment. Not a code audit or a feature design.

---

### 🔧 DEVELOPMENT RULES

**Direct skill: `ris-proj-op-author-development-rules`**

Formulate, separately accept and save engineering norms: versions, builds, style,
testing, review and CI practices. Does not install tools or configure CI.

---

## PAGE 2 · WORK OUT A FEATURE (PREPARE TASKS)

### 🗺 ROADMAP

**`/risp-roadmap`**

Turn freely structured product knowledge, a chosen goal and observed state into
epics and agreed preliminary feature graphs in one session. One MVP epic is valid.
Depth: epic-only, nearest stage (default), or all. Proposal-only makes no changes.
No detailed specs/design or implementation tasks; planning is not acceptance.

---

### 🔍 REFINE AN EPIC

**`/risp-refine-epic <ID>`**

Clarify an existing epic's unclear goal/outcome/boundary. Does not build a second
feature graph or specify every future feature.

---

### 🧩 PREPARE A FEATURE END TO END

**`/risp-prepare-feature <epic or context>`**

Early-register the chosen feature, prepare one safe ID-associated copy and work
out requirements/design in one dialogue. Each distinct scope/version has sufficient
direct/inherited/mixed basis: check original accepted sources and actual derivation,
not mere compatibility. Wholly inherited content needs no new approval/acceptor;
mixed content decides only new material in the full candidate context. One act
may decide new parts of both scopes; preserve original provenance.
Only this flow uses strict boolean `workflows.prepare_feature.auto_accept`:
`true` or omission (also absent optional root config) defaults to policy acceptance;
`false` keeps the ordinary manual protocol. Invalid config/types, including `"true"`
and null, stop automatic continuation. Explicit requests to approve requirements,
design or both make only named scopes manual. Substantive questions remain, but
sufficient answers need no separate formal reply or full-text chat dump: documents
hold complete texts, the result is short with links. Policy provenance is recoverable,
not human approval or inheritance; repairs/resume follow the same scope modes.
Direct specify/design calls never enable auto from config. No closure follows.
Independently review/publish inputs, update the same ID and apply existing
decomposition through verified one-task or child-task/edge coverage and separate
tracker publication. Sufficient inline design needs no design.md. No implementation.
The full request includes ordinary Git/tracker publication within its authority;
no approval per internal step. Local saving is intermediate. Missing authority
requires one concrete question; explicit restrictions remain. Unrelated Git commits
and uncovered shared Dolt history are not authorized by one feature request.

---

### 🎯 PLAN AN EXISTING EPIC'S FEATURES

**Direct skill: `ris-proj-op-plan-epic-features` with exact epic ID**

Propose/revise its preliminary graph, agree concrete changes, reconcile all states
and preserve existing IDs/accepted/foreign/completed work before controlled writes
and separate publication. No spec/design/AC/children required at registration.
Portable proposal: `ris-port-op-plan-epic-features` with supplied inputs, no RIS required.
Status/next/prepare select existing records for the needed stage and show parallel
candidates; empty epics need planning, all-blocked needs diagnosis, not new features.
Requirements prerequisites wait for exact accepted decisions, not whole-feature
closure; implementation-only blocks do not automatically bar requirements work.
Preparation keeps the same preliminary ID and actual acceptance/readiness gates.

---

### 💬 INTERVIEW FOR REQUIREMENTS

**Direct skill: `ris-proj-op-interview-feature`**

Clarify behavior and material quality requirements through dialogue. Does not
accept or save a complete specification.

---

### 📝 AGREE REQUIREMENTS

**`/risp-specify-feature <ID>`**

Formulate, accept, save and publish requirements within the authorized scope.
Does not replace technical design.

---

### 📐 AGREE THE DESIGN

**`/risp-design-feature <ID>`**

Prepare a sufficient technical solution from accepted requirements, explain it
in plain language and check its independently sufficient direct/inherited/mixed
basis before save/publication, obtaining approval only for new material in the
complete candidate context. Does not decompose or implement tasks.

---

### 📋 PREPARE TASKS

**`/risp-decompose-feature <ID>`**

Check whether one task suffices or create necessary tasks and dependencies from
accepted requirements/design. Also available independently or to resume this result;
already included in prepare-feature. Does not plan one task's implementation.

---

## PAGE 3 · EXECUTE THE NEXT PREPARED TASK

### ⚙️ EXECUTE THE WHOLE TASK CYCLE

**`/risp-run-task [ID]`**

Execute or resume one prepared task: copy/claim, implementation from sufficient accepted inputs,
checks, independent review, Git publication, separate task completion and tracker
publication. An explicit ID selects only that work; without one, reconcile own
unfinished work before ready-task choice. Not a whole multi-task container.
An explicit human request to continue/execute that task already authorizes session
reassignment without another takeover question. Preserve its verified worktree,
branch and changes; old actor/lease alone is not a blocker. Real conflicts and
task blockers remain binding.

---

### 🌿 PREPARE A WORKING COPY

**Direct skill: `ris-proj-op-prepare-task-worktree`**

Prepare or safely reuse a copy for a confirmed task, checking claim, blockers,
association and authorized setup. All versioned Git-project edits, including
simple tasks and documents, reuse a dedicated worktree, never the source folder.
Installation and agreed pre-Git bootstrap retain their direct-target exceptions.
Does not plan or implement the task.

---

### 🧪 IMPLEMENT AND CHECK WITH TDD

**Direct skill: `ris-proj-op-implement-task-tdd`**

Implement code/tests or repair review findings with mandatory TDD and affected
checks. Stops at checked changes, not independent approval, publication or close.
No saved plan, implementation report or author test-history report is required.

---

### 📖 UPDATE AFFECTED DOCUMENTATION

**Direct skill: `ris-proj-op-update-documentation`**

Synchronize explicitly authorized documentation with inspected implementation.
Does not redefine product requirements or redesign the feature.

---

### 🔎 INDEPENDENT REVIEW

**`/risp-review-task [ID]`**

Assess a concrete complete change and return findings. Does not repair or publish.
Ordinary project review saves one local `review.yaml`: new files use ris.review/2;
existing /1 files continue unchanged under the format owner's conditional contract,
without migration. No-ID saving needs an explicit path. Beads stores address/round
only, not verdict/findings. Fast review is conditional as below; active review permits
session-only independent evidence, and optional
save follows the same new/existing-file schema rule. The single format owner is
`ris-proj-op-review-task/references/report-format.md`.
Valid YAML alone is not approval of the current snapshot and provenance.
Self-review does not provide independent publication approval.

---

### 🚀 PUBLISH GIT

**`/risp-publish-task [ID]`**

Integrate an independently reviewed whole change into the established primary
branch from the work's dedicated worktree and verify the authorized direct push.
Default is remote-only. An explicit request or applicable accepted project policy
permits separate safe FF only on an already
suitable source copy, never branch switching. It is separate:
an unsafe/busy copy stays untouched and skipped/failed updating does not block
task completion or tracker publication. Caller checks/forwards the policy's actual
source/version/acceptance and boundaries; dependencies need their own bounded
authorization. Policy-required or explicitly requested local updating remains an
unfinished combined-result part, never complete while pending. Does not complete the task,
publish tracker history, deploy or create a PR.

---

### 🏁 COMPLETE THE TASK AND PUBLISH THE TRACKER

**Separate effects within `/risp-run-task`; no separate slash command.**

After verified Git publication, persist the result, verify exact task completion,
then separately publish tracker history through the selected adapter under its
gates. Git push alone proves none of these effects. After confirmed close and
publication, one fresh `container-completion` subagent ascends actual parent links:
child-based closure with separate publication, stopping at the first unfinished/
blocked parent. Explicit limits win; report task completion separately from any
cascade failure or unfinished effects.
Full requests include ordinary actions across skill boundaries; narrower limits
and substantive gates remain. Tracker publication uses the selected project's
standing shared-history policy or explicit authority, without automatic policy changes.

---

### ⚡ EXECUTE A SIMPLE ASSIGNED CHANGE

**`/risp-run-simple-task <request>`**

Execute/resume one small, locally bounded, understood and checkable request or idea;
a suitable natural request selects this same Fast without the command. Judge
consequences/boundaries/checks, not file type/diff size or an operation allowlist:
code/config/docs/tools/versioned/ignored/external can qualify. No product-logic,
architecture/material-contract changes, coordinated independent outcomes, broad/unknown
effects or insufficient checks. Resolve minor ambiguity here; agree only necessary
expansion, not automatic full SDLC restart. Empty input asks for work, not queue choice.
Existing feature/bug/container obligations remain, never downgraded to fit Fast.

One main agent, default zero subagents; no mandatory preparation/plan/handoff/log/review
files. Mandatory self-check/checks/TDD remain. Independent review only for explicit
request, mandatory applicable target-project policy or concretely explained material
risk; code, external location and Git push alone are not triggers. General RIS review
wording does not cancel this exception. Inactive review loads no role/format or skip
report; active review is really independent, high/medium need repair/checks/reassessment,
unavailable required review blocks dependent gates. No fictional approval.

Versioned edits use one own branch/dedicated worktree with reuse, never source-folder
development. Local-only changes authorized actual targets without empty copy/dummy SHA/
push; mixed preserves/checks both channels and shared-resource conflicts separately.
Git retains outgoing/integration/non-force/remote gates; no-change checks needed existing
state without empty commit/push. Local-only needs useful checked effects and honest
availability limits, not Git SHA; partial mixed is unfinished. Separate tracker result,
exact close/read-back and publication when used (short Beads mandatory in RIS); Dolt
does not publish local files. Eligible ancestors close inline through the existing
owner, without mandatory `container-completion` role/subagent; no parent is no-op.
Full/bug retains fresh delegation and independent review; direct review is unchanged.
Resume reuses ID/copy/foreign work, reconciles uncertain effects and never replays
confirmed push/close or owes absent inapplicable review. Changed subjects get affected
self-check/risk reassessment and independent reassessment when required.

*Choose the whole workflow OR individual operations — not both. Listed stages
are not extra mandatory calls on top of the workflow.*

---

## PAGE 4 · BUGS, ACCEPTANCE AND OTHER OPERATIONS

### 🐞 REGISTER A BUG MESSAGE

**Direct skill: `ris-proj-op-register-bug`**

Check duplicates, record an unconfirmed message and return a verified ID. Does
not investigate, claim or fix it.

---

### 🔬 INVESTIGATE A REGISTERED BUG

**Direct skill: `ris-proj-op-investigate-bug`**

Investigate an exact native bug ID. Ordinary saving uses one assigned investigator,
authorized native writes, fresh comparison and read-back, preserving original/foreign
content; not CAS or exclusion of all parallel writers. Missing authority/capability
or observed conflict can block saving, not useful research. Confirmation and saving
are not fix readiness. No automatic fixing.

---

### 🩹 FIX A REGISTERED BUG

**Direct skill: `ris-proj-flow-fix-bug`**

Fix an exact bug from sufficient saved inputs, obtaining separate acceptance for
material design if needed. Reuses the whole `/risp-run-task` execution route;
does not silently register or investigate a fresh report.

---

### ✅ VERIFY OR CLOSE A CONTAINER

**`/risp-complete-container <intent> <ID>`**

Ordinary parent close checks a nonempty complete direct-child list (all closed)
and no active parent blockers; no recursive acceptance/Git/review audit. Asking
whether it can be closed uses those reads only. Zero-child features retain
own-result verification. Explicit read-only fulfillment verification,
verify-and-close and administrative close remain available. Child-based or
administrative closure is NOT fresh whole-result acceptance. Not ordinary leaf
completion; this direct call neither closes children/ancestors nor starts execution's cascade.

---

### 🔄 SESSION RETROSPECTIVE

**`/risp-retro <session ID>`**

Analyze one session's evidence, causes, costs and minimal improvements. Does not
repair the problems or perform multi-session analytics. Saving needs permission.

---

### 📚 PROJECT OKF BUNDLE

**Direct skill: `ris-proj-op-manage-okf-bundle`**

Read, create, edit or check an explicitly selected OKF bundle in project context,
with project/root/operation/scope. Ordinary Markdown is not automatically OKF.

---

### 🧰 AUTHOR AN AUTONOMOUS SKILL

**`/risb-skill`**

Create or improve standalone skill source, even inside a RIS project. Does not
install or execute the resulting skill.

---

### 🔗 AUTHOR A RIS-INTEGRATED SKILL

**Direct skill: `ris-proj-op-author-skill`**

Create or improve skill source that actually integrates with RIS, checking the
combined result. Does not install or execute it.

---

### 💬 INTERVIEW ON A BOUNDED TOPIC

**`/risb-interview <topic>`**

Explore interdependent decisions from supplied context without project setup.
Returns an interview handoff, not a saved accepted specification.

---

### 🔎 REVIEW A SUPPLIED CHANGE

**`/risb-review-change <change and scope>`**

Review a concrete change read-only without RIS configuration or a tracker.
Returns findings, not fixes or publication.

For other portable methods and exact inputs, ask `/ris-help <topic>` or request
the exhaustive inventory. Full help is an orientation guide, not a readiness
verdict or authority to run any of these operations.
