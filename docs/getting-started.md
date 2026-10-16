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
| Shared task notes or worktrees | Required `workspace.*` fields and a checked primary root. `sources.*` resolve in the current project copy; shared paths resolve in the primary. In a separate worktree, supply the primary explicitly or reuse a verified applicable association receipt. |
| Tracked task work | Select an available tasks adapter, e.g. `adapters.tasks.skill: ris-proj-adapter-beads-tasks`, and an existing accessible Beads/Dolt project for that route. Installation does not initialize it. |
| Delegated operations/flows | Configure the roles that the chosen owner requires under `execution.roles.<role>.agent` and verify actual agent availability/launch. A configured name alone is insufficient; direct calls do not universally require roles. |
| Publication | Configured relevant remotes, access, explicit publication authority and inspection of the entire outgoing scope, plus the owner's required checks/review and independent remote read-back. |

For tracked work, the [Beads adapter](../skills/ris-proj-adapter-beads-tasks/SKILL.md)
owns exact record, ownership, composition and typed-blocker checks and bounded
native writes. A claim or lease is not a general content/graph lock. For a full
single-task cycle, the [execution flow](../skills/ris-proj-flow-execute-task/SKILL.md)
owns transitions and its required roles; call it only with that cycle authorized.
Neither operation requires a new setup skill. Optionally add the
[consumer AGENTS fragment](concepts/templates/agents-fragment.md) to an existing
project `AGENTS.md`; it supplements the project's instructions without replacing them.

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
The flow verifies a full historical report/criteria/decision snapshot in bug notes,
then reuses execute-task in full with its existing three roles. Consumers name that
snapshot and reassess affected plan/change/review/evidence on material input drift.
A saved plan is needed for execution/handoff sufficiency or project rules; RIS
retains its mandatory local plan, and direct plan-task still saves a plan. Copy/
claim, TDD for code, independent review and publication obligations are retained.
Snapshot append is recoverable native merge, not concurrent append-once or content
CAS; investigation's stronger report replacement gate remains unchanged.

## 3. Authorize work and publish from the task's own copy

Installing RIS grants **no write, push or task-close rights**. Establish the
accepted outcome, allowed paths/effects and current authority for each operation.
For ordinary task execution, work in your own task branch and working copy,
preserving foreign changes; shared local `main` is not a publication workspace.

The [Git publication owner](../skills/ris-proj-op-publish-task/SKILL.md) integrates
the fresh established remote primary branch (often `main`) into that own branch,
resolves conflicts there, and requires affected rechecks and independent
reassessment of the complete new snapshot before a normal non-force push. Remote
advancement triggers only the affected reconciliation/check/reassessment work;
compatible evidence and unchanged acceptance remain applicable. No global
publisher queue or manual writer pause is required for ordinary work.

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
