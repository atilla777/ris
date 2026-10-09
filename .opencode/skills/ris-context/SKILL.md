---
name: ris-context
description: >-
  Prepare selected RIS project configuration, document and shared workspace
  paths, permissions, and input diagnostics for a specific project operation.
  Use before that operation or after a project, config, or worktree change;
  not for product planning, OKF validation, or task-tracker execution.
---

# Prepare RIS project context

Return checked settings for the **calling operation** in the selected project.
The caller owns document selection, domain readiness, task-tracker operations,
and its final result. Do not choose a lifecycle task, read every document,
validate OKF content, create directories or worktrees, or edit source files.

First ensure current `ris-common` instructions are available in this session
from its installed skill location. Apply its baseline rules now; read its
conditional resources before the actions they govern. If unavailable, state
the limitation and do not claim the dependent work complete. Do not assume
`ris-common` is installed beside this skill or in the RIS source repository.
Read `references/configuration.md` relative to **this skill's installed
directory** before preparing any settings. Stop dependent preparation if it
cannot be read. Do not treat the name of a dependency as its execution.

Obtain the calling operation, target project, needed configuration fields,
input vs prospective output roles, parameters, and permitted scope from the
request and applicable project instructions. If ambiguous, diagnose the
affected part rather than inventing a root, document, ID, or permission.
Prepare the paths and required inputs following the owned configuration
resource. Return applicable resolved settings, source/provenance, run scope,
status, and actionable diagnostics. Confirm that the result pertains to the
current project and operation; `ok` is only preparation, not downstream
completion. Never write a config, output, task, or persistent context, even
when the caller has write permission. Stop at the context result.
