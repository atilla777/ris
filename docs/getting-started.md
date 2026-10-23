# Getting started with RIS

## 1. Install, then try one portable operation

Follow the [README installation instructions](../README.md#install-in-opencode):
use its bootstrap for the complete package, or the installation guide's
[manual selective installation](installation.md#manual-installation-of-a-portable-skill)
of the autonomous interview folder **with all resources** and `risb-interview` command.
Quit and restart OpenCode after installation so the new files are discovered.

In OpenCode, for example:

```text
/risb-interview Decide how a small CLI should report invalid arguments: users, error messages and exit codes; implementation is outside this discussion.
```

The [portable interview](../skills/ris-port-op-interview/SKILL.md) uses full mode
by default: it investigates material decisions within that bounded topic, reuses
known answers and asks one decision question at a time. Limited mode needs an
explicit request and a sufficiency criterion. It returns a read-only handoff in
the response: decisions, sources, open questions and their impact. It does not
save a specification, accept requirements, create tasks or start implementation.
Pass that handoff explicitly to a later conversation if needed.

This operation needs no `ris.yaml`, project common/context, Beads/Dolt or
subagent. Portable operations follow their own declared dependencies and the
actual target project's rules; selective use does not require the whole package.
The command is a convenience; the skill can also be invoked directly.

## 2. Add project context only when the operation needs it

Choose a project operation by the result you want in the
[skill catalog](skills.md), then check its
inputs and permissions. Project operations use common/context as their contracts
require. There is no mandatory onboarding interview or automatic configuration.

The optional root `ris.yaml` uses schema v2. For a direct
[documentation synchronization](../skills/ris-proj-op-update-documentation/SKILL.md)
that needs only the project's rules directory, this is a minimal example:

```yaml
version: 2
sources:
  rules: docs/rules/
```

The directory must contain the actual applicable project rules; the operation
still needs an inspected implementation, bounded document scope and write
authorization. Add other fields only for the selected operation's needs. If the
optional root file is absent, package defaults apply. If a config is present,
**only its values apply**: missing fields are not merged from defaults. An
explicitly selected missing/invalid config is an error, not a default fallback.
See the [configuration owner](../skills/ris-proj-op-resolve-context/references/configuration.md)
for the schema, defaults and path checks.

| When needed | What to prepare |
| --- | --- |
| Project documents | The operation's required `sources.*` fields and actual rules/specs/product inputs. Product knowledge is author-owned; a configured directory does not authorize edits. |
| Shared task notes or worktrees | Required `workspace.*` and context-checked primary: explicit → verified saved association → verified ordinary Git source copy. Never the first worktree or a fallback around bad explicit/conflicting facts. Resolving shared addresses grants no permission to change that copy. |
| Tracked task work | Select an available tasks adapter, e.g. `adapters.tasks.skill: ris-proj-adapter-beads-tasks`, and an existing accessible Beads/Dolt project for that route. Installation does not initialize it. |
| Delegated operations/flows | Configure the roles that the chosen owner requires under `execution.roles.<role>.agent` and verify actual agent availability/launch. A configured name alone is insufficient; direct calls do not universally require roles. |
| Publication | Configured relevant remotes, access, explicit publication authority and inspection of the entire outgoing scope, plus the owner's required checks/review and independent remote read-back. |

For tracked work, the [Beads adapter](../skills/ris-proj-adapter-beads-tasks/SKILL.md)
owns exact record, ownership, composition and typed-blocker checks and bounded
native writes. A claim or lease is not a general content/graph lock. For a full
single-task cycle, the [execution flow](../skills/ris-proj-flow-execute-task/SKILL.md)
owns transitions and its required roles; call it only with that cycle authorized.
Neither operation requires a new setup skill. Optionally add the
[consumer AGENTS fragment](product/templates/agents-fragment.md) to an existing
project `AGENTS.md`; it supplements the project's instructions without replacing them.

For a read-only overview in an existing tracked project, use `/risp-status` for
the complete unclosed plan, or `/risp-status <ID>` for one subtree with necessary
ancestors/blockers. It works in the current agent without execution roles and
returns one checked next action or an exact gap; it does not save, claim or launch
work. `/risp-next <ID>` instead inspects an already selected subject. Commands must
be present in the installed package and discovered after restart; see the
[current menu](skills.md#current-compact-command-menu).

For bug work, directly load `ris-proj-op-register-bug` to record a message and
stop at its ID, or `ris-proj-op-investigate-bug` to investigate an existing exact
native bug ID. The latter applies `ris-port-op-investigate-bug`, saves report and
agreed criteria under actual content-protection gates, and stops before fixing.
If those gates are unavailable, research can still return useful findings but
the current report is not claimed saved. Insufficient evidence keeps the message
open; proved correct/duplicate messages have a separate checked disposition.
No additional slash command or execution role is required for these direct calls.

Fixing is a separate direct load of
[`ris-proj-flow-fix-bug`](../skills/ris-proj-flow-fix-bug/SKILL.md) with the exact
native bug ID, project, actor and authorized fix/publication scope. Its sufficient
saved report establishes expected behavior/authority, confirmed divergence,
bounded scope, criteria and technical constraints. It returns precise gaps without
silently investigating. Material choices use the existing design owner and separate
acceptance; a local contract-preserving solution needs no formal spec/design pair.
The adapter verifies the full used report/criteria/decisions at an exact tracker-history
version plus immutable Git sources and acceptance decisions. A short ordinary basis
locator in notes enables discovery from project+ID without old chat; no new full
snapshot or file is required. Missing/incomplete history blocks dependent execution.
The flow reuses execute-task in full with its existing roles; consumers name the basis
and reassess affected change/review/evidence on material drift. Preserve old snapshots
and append a new locator only for a newly admitted basis, never rewrite history.
No saved plan or implementation report is required. Copy/claim, TDD for code,
independent review and separate Git/result/exact close/Dolt obligations remain.
Locator append/retry belongs to the adapter and is not concurrent append-once or
content CAS; investigation's current report replacement conditions remain unchanged.

### A clear assigned simple request

```text
/risp-run-simple-task In <project>, replace the specified heading with <text>; keep the rest unchanged. Use existing task <ID> if supplied.
```

The [simple-task flow](../skills/ris-proj-flow-execute-simple-task/SKILL.md) can
also be chosen by a natural request or the agent for work already assigned.
It checks clarity, bounded consequences and checkability; empty input asks for
work, never selects the queue. No mandatory interview/spec/design/decomposition,
plan or log/review files by default. Supply applicable project rules and the
configured, actually launchable independent `task-review`; the main agent applies
the existing implementation/docs/publisher owners itself. Checks are proportionate,
and mandatory project checks/TDD apply. Use a verified own branch in a suitable
current copy; isolation or rules activate the existing worktree owners.

Tracking is conditional on a supplied ID or project accounting rules, not merely
an installed adapter. **RIS itself requires short Beads accounting**; without ID
the flow reconciles/creates a sufficient ordinary task before changes. Existing
type, accepted inputs, ownership, children and blockers remain binding. Full
task/bug/feature preparation and direct plan-task/TDD contracts are preserved.
High/medium findings need repair/checks/fresh independent review. PR-only, forbidden
direct push or missing mandatory review/checks block publication; tracker result,
exact close and publication remain separate from Git. Material decisions trigger
targeted clarification/preparation; resume checks actual effects and available evidence.

## 3. Authorize work and publish from the task's own copy

Installing RIS grants **no write, push or task-close rights**. Establish the
accepted outcome, allowed paths/effects and current authority for each operation.
Project [review](../skills/ris-proj-op-review-task/SKILL.md) and Git publication
can take an agreed bounded change with or without a task ID. Supply the attributable
request, criteria, accepted constraints/decisions, exact copy/branch/base and complete
candidate (including additions/deletions/modes), checks and review purpose. Separate
spec/design/plan files are not inherently required. Response-only review is sufficient
where project rules allow; required tracking or report saving remains a gate.
An ordinary Beads task can preserve that self-contained accepted request and authority
without invented specification links; existing feature/bug contracts still apply.

For publication, supply an already prepared own branch and dedicated worktree,
preserving foreign changes. Reuse a suitable associated worktree; the ordinary
source folder is never a development/publication workspace. Preparation belongs to the
caller and existing preparation owners; shared local `main` is not a publication workspace.

The [Git publication owner](../skills/ris-proj-op-publish-task/SKILL.md) integrates
the fresh established remote primary branch (often `main`) into that own branch,
resolves conflicts there, and requires affected rechecks and independent
reassessment of the complete new snapshot before a normal non-force push. Remote
advancement triggers only the affected reconciliation/check/reassessment work;
compatible evidence and unchanged acceptance remain applicable. No global
publisher queue or manual writer pause is required for ordinary own-branch work.
After remote confirmation an explicit request or applicable accepted project policy
can activate separate safe local primary FF, never branch switching/return.
Callers check and forward actual policy source/version/acceptance and bounded
targets/effects; without either authority source keep remote-only. Dependency
refresh needs its own bounded authorization. An unsafe/busy
copy remains untouched. Skipped/failed local updating does not invalidate remote
Git or block exact completion/Dolt; report it separately, never push again for it.
A policy-required or explicitly requested local update remains unfinished in the
combined result; do not call that whole result complete while it is pending.
Full requests include ordinary constituent actions across existing owners, without
repeated technical permissions; narrower authority and substantive gates remain.
For a new assignment actor may fall back to a verified current host-session ID,
never to steal an existing claim/copy. Missing reliable identity is an exact gap.

Git publication, exact task completion and Dolt publication are **separate
effects**. A successful Git push does not close a task or synchronize its tracker;
closing a child does not accept or close its parent. Use the adapter's
[Dolt publication contract](../skills/ris-proj-adapter-beads-tasks/references/dolt-publication.md)
for full outgoing-history authority and independent read-back, rather than
assuming Git and tracker publication are interchangeable.

For ordinary instruction changes, completion uses reading, affected static checks
and independent review; names/resources/dependencies and source/install parity
are checked statically. Executable programs need their applicable ordinary tests.
This repository prohibits new agent behavioral tests: absence of a live run is
not a blocker or a reason for another run question for ordinary instruction work.
Static readiness does not establish agent reliability, cost or repeatability;
existing observations retain their original versions and limits, and unmet
historical obligations remain unverified. Portable use follows the actual target
project's rules. See the [development guide](development.md) and its links to the
normative evidence boundaries.
