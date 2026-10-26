# RIS · DAILY HELP

### 🧭 WHERE WE ARE

**`/risp-status [ID]`** — project plan (or ID subtree), blockers and one recommendation.

**`/risp-next <ID>`** — next step for selected work.

Both are read-only. Status first considers started work in its scope, even another
assignee's; a recommendation does not authorize takeover.

---

### 🧩 WORK OUT A FEATURE (PREPARE TASKS)

**`/risp-prepare-feature <ID, epic + chosen idea, or standalone idea> [auto|compact|full]`** — early-register the chosen feature,
use one safe copy and requirements/design dialogue, establish each scope's
direct/inherited/mixed or scoped policy basis,
review/publish inputs and verify decomposition plus tracker publication.
One author context, only new material questions (a related block is valid), short
sufficient spec/design. Draft review is optional; final independent review remains.
Resume finishes missing effects, not a new readiness checklist or repeated pushes.

No mandatory epic/Roadmap for a chosen idea. Auto depth defaults to sufficient
Compact work with reused mechanisms and one-task-first decomposition; concrete
design/risk/coordination needs justify Full. Explicit Full stays Full; material
Compact gaps need only the necessary agreed expansion. Children are independent
results, not package/config/API/test steps. Compact is not Fast; all gates remain.
Depth Auto is distinct from the acceptance setting below.

Prepare defaults to automatic requirements/design acceptance after substantive
answers (`workflows.prepare_feature.auto_accept: false` keeps manual acceptance).
Explicit approval requests make only named scopes manual; direct stages do not
inherit auto from config. Full automatic texts stay in documents, with a short linked result.

**Or use individual stages:**

- `/risp-status <epic ID>` — existing stage-ready and parallel candidates (read-only).
- `/risp-specify-feature` — agree requirements.
- `/risp-design-feature` — agree the design.

Empty epic? `/risp-roadmap` plans epics and preliminary features (default nearest
stage; also epic-only/all). One MVP epic is valid. All-blocked means diagnose
prerequisites, not generate more features. Preparation retains the preliminary ID.

**`/risp-decompose-feature <ID>`** — independently obtain/verify tasks from accepted
published inputs; already included in the whole preparation flow. No implementation.

---

### ⚙️ EXECUTE THE NEXT PREPARED TASK

**`/risp-run-task <ID>`** — implement, check, independently review, publish Git,
then separately complete the task and publish the tracker.

Without ID — confirmed unfinished work of the current actor first, then a ready
task: the choice may differ from status. Blocked selected own work stops the flow.
With ID the target stays fixed; a container is not replaced by a child, and a
multi-task container is not executed as a leaf task.

**`/risp-run-simple-task <request or ID>`** — Fast: one small, bounded, checkable
request/idea; a suitable natural request selects the same route. Code/config/docs/
tools/local files may qualify; no product-logic/architecture/material-contract
changes, coordinated outcomes or broad/unknown effects. Empty input asks for work.
One main agent, no subagents by default; self-check/TDD remain. Review only for an
explicit request, mandatory target policy or concrete material risk, not code/Git alone.
Versioned edits use an own branch/worktree; local-only uses actual targets without
dummy Git, mixed checks both. Separate tracker completion/publication when used
(short Beads accounting mandatory in RIS); eligible ancestors close inline, not via a mandatory subagent.

*Choose the whole workflow OR its individual stages — not both.*

---

### 📚 MORE DETAIL

**`/ris-help full`** — installation, initialization, roadmap, individual execution
stages, bugs, acceptance and retrospective.
