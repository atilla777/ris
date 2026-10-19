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

Turn product knowledge, a chosen goal and the observed starting state into epic
outcomes. A proposal-only request makes no tracker changes. Not feature tasks.

---

### 🔍 REFINE AN EPIC

**`/risp-refine-epic <ID>`**

Clarify an existing epic's outcome, boundaries and prerequisites when they prevent
feature selection. Does not specify every future feature.

---

### 🧩 PREPARE A FEATURE END TO END

**`/risp-prepare-feature <epic or context>`**

Choose a feature, separately accept requirements and design, review/publish the
inputs and obtain a published feature ID. Decomposition and implementation are
outside this scenario.

---

### 🎯 SELECT A FEATURE

**`/risp-select-feature <epic ID>`**

Recommend a small verifiable result within an epic. Does not create tasks or
launch development.

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
in plain language and separately accept the complete candidate before accepted
save/publication. Does not decompose or implement tasks.

---

### 📋 PREPARE TASKS

**`/risp-decompose-feature <ID>`**

Check whether one task suffices or create necessary tasks and dependencies from
accepted requirements/design. Does not plan one task's implementation.

---

## PAGE 3 · EXECUTE THE NEXT PREPARED TASK

### ⚙️ EXECUTE THE WHOLE TASK CYCLE

**`/risp-run-task [ID]`**

Execute or resume one prepared task: copy/claim, plan as required, implementation,
checks, independent review, Git publication, separate task completion and tracker
publication. An explicit ID selects only that work; without one, reconcile own
unfinished work before ready-task choice. Not a whole multi-task container.

---

### 🌿 PREPARE A WORKING COPY

**Direct skill: `ris-proj-op-prepare-task-worktree`**

Prepare or safely reuse a copy for a confirmed task, checking claim, blockers,
association and authorized setup. Does not plan or implement the task.

---

### 📝 PLAN THE TASK

**`/risp-plan-task <ID>`**

Save a technical plan and check strategy in a supplied suitable copy. Does not
create a worktree or implement the change.

---

### 🧪 IMPLEMENT AND CHECK WITH TDD

**Direct skill: `ris-proj-op-implement-task-tdd`**

Implement code/tests or repair review findings with mandatory TDD and affected
checks. Stops at checked changes, not independent approval, publication or close.

---

### 📖 UPDATE AFFECTED DOCUMENTATION

**Direct skill: `ris-proj-op-update-documentation`**

Synchronize explicitly authorized documentation with inspected implementation.
Does not redefine product requirements or redesign the feature.

---

### 🔎 INDEPENDENT REVIEW

**`/risp-review-task [ID]`**

Assess a concrete complete change and return findings. Does not repair or publish.
Self-review does not provide independent publication approval.

---

### 🚀 PUBLISH GIT

**`/risp-publish-task [ID]`**

Integrate an independently reviewed whole change into the established primary
branch and verify the authorized direct push. Does not complete the task,
publish tracker history, deploy or create a PR.

---

### 🏁 COMPLETE THE TASK AND PUBLISH THE TRACKER

**Separate effects within `/risp-run-task`; no separate slash command.**

After verified Git publication, persist the result, verify exact task completion,
then separately publish tracker history through the selected adapter under its
gates. Git push alone proves none of these effects. Never close parents implicitly.

---

### ⚡ EXECUTE A SIMPLE ASSIGNED CHANGE

**`/risp-run-simple-task <request>`**

Execute clear bounded assigned work: own branch, proportionate checks, independent
review and Git; separate tracker result/completion/publication when used. No
mandatory plan/log/review files by default; mandatory project rules and TDD remain.
Not queue selection or a bypass for an unprepared feature/bug.

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

For a feature, standalone task-container or epic, choose read-only verification,
explicit administrative close, or verify-and-close with successful verification
and authorized writes. Administrative close is NOT acceptance. Not ordinary
leaf-task completion; children/ancestors are never closed automatically.

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
