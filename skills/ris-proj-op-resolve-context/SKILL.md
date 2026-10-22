---
name: ris-proj-op-resolve-context
description: >-
  Prepare selected RIS project configuration, document and shared workspace
  paths, optional execution roles, permissions, and input diagnostics for a
  specific project operation.
  Use before that operation or after a project, config, or worktree change;
  not for product planning, OKF validation, or task-tracker execution.
---

# Prepare RIS project context

Return checked v2 settings for the **calling operation** in the selected project.
The caller owns document selection, domain readiness, task-tracker operations,
and its final result. Do not choose a lifecycle task, read every document,
validate OKF content, create directories or worktrees, or edit source files.
Reject a selected v1 config, including `sources.concepts`, with an explicit
migration diagnostic; never reinterpret it as `sources.product` or use defaults.

First ensure current `ris-proj-lib-common` instructions are available in this session
from its installed skill location. Apply its baseline rules now; read its
conditional resources before the actions they govern. If unavailable, state
the limitation and do not claim the dependent work complete. Do not assume
`ris-proj-lib-common` is installed beside this skill or in the RIS source repository.
Read `references/configuration.md` relative to **this skill's installed
directory** before preparing any settings. Stop dependent preparation if it
cannot be read. Do not treat the name of a dependency as its execution.

Obtain the calling operation, target project, needed configuration fields,
input vs prospective output roles, parameters, and permitted scope from the
request and applicable project instructions. If ambiguous, diagnose the
affected part rather than inventing a root, document, ID, or permission.
Prepare only the requested settings under `references/configuration.md`; validate
the whole selected config even when some fields are unused. Missing unused fields
do not block independent preparation. From this installed folder read:

- `references/paths.md` before resolving/checking document or workspace paths;
- `references/shared-primary.md` only before using shared workspace paths or
  resolving the source folder for explicitly requested local maintenance;
- `references/execution-roles.md` only when the caller requires a role.

An explicit tracker workspace read need not invoke context at all. Never require
unused shared roots or execution settings. Return applicable resolved settings,
source/provenance, run scope, status, and actionable diagnostics. Confirm that
the result pertains to the current project and operation; `ok` is only
preparation, not downstream completion. A configured agent name is not proof
that the subagent exists, uses a particular model, was launched or is independent;
the caller checks actual delegated invocation and required review independence.
Roles select delegated executors, not mandatory delegation of each internal step.
Never select a fallback agent, switch models,
launch a subagent or skill, or write a config, output, task, or persistent
context, even when the caller has write permission. Stop at the context result.
