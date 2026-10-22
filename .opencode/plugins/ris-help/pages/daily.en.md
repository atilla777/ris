# RIS · DAILY HELP

### 🧭 WHERE WE ARE

**`/risp-status [ID]`** — project plan (or ID subtree), blockers and one recommendation.

**`/risp-next <ID>`** — next step for selected work.

Both are read-only. Status first considers started work in its scope, even another
assignee's; a recommendation does not authorize takeover.

---

### 🧩 WORK OUT A FEATURE (PREPARE TASKS)

**`/risp-prepare-feature <ID or context>`** — early-register the chosen feature,
use one safe copy and requirements/design dialogue, precisely accept both scopes,
review/publish inputs and verify decomposition plus tracker publication.

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

**`/risp-run-simple-task <request>`** — execute a clear, bounded assigned change.

*Choose the whole workflow OR its individual stages — not both.*

---

### 📚 MORE DETAIL

**`/ris-help full`** — installation, initialization, roadmap, individual execution
stages, bugs, acceptance and retrospective.
