---
name: ris-port-op-manage-installation
description: >-
  Install, update or uninstall the complete RIS package in one selected project's
  OpenCode directories through the bundled installer and report its checked
  outcome. Use for explicit RIS package management; not project initialization,
  individual skill authoring, automatic updates or global installation cleanup.
---

# Manage a project's RIS installation

Own intent, parameters, invocation and verified reporting for one operation.
The sole replacement/recovery engine is `scripts/ris-install.sh`, resolved
relative to **this loaded skill folder**, including after installation elsewhere.
Do not reproduce its copying, transaction or rollback algorithm. No RIS config,
Beads, other skill, initialized project or target Git repository is required.

## Establish the request

1. Determine `install`, `update` or `uninstall` from the explicit request. With
   empty or ambiguous input ask which operation and which project are intended;
   use already unambiguous supplied context without asking again. Never silently
   turn update/removal into installation or run an update during another task.
2. Establish the existing absolute target project directory independently of
   this skill's location. Inspect applicable target instructions and permission
   for the requested package write. Resolve ambiguous roots before execution;
   do not create a project. An explicit management request authorizes the full
   reserved-namespace replacement under applicable permissions, including local
   edits/collisions, without a second per-file approval.
3. For install/update accept an optional exact tag or full 40-hex **commit** SHA.
   Omission uses upstream remote HEAD, regardless of branch name. Do not pass
   branches or Git revision expressions; a 40-hex tag spelling is treated as a
   commit SHA. Uninstall accepts no ref. Preserve the requested operation/ref.
4. Explain the effect as needed: the whole `.opencode/skills/ris-*` and
   `.opencode/command/ris-*.md` namespace and `.opencode/ris-installation` are
   replaced/removed; retired entries and local edits are not merged. Other
   skills/commands, settings, `ris.yaml`, `AGENTS.md`, docs and tasks are preserved.
   Project additions need non-`ris-` names. Known duplicate installations in
   alternate `skill/`, `commands/`, global, parent or config-defined locations
   may shadow these files: report known paths, without expanding into cleanup.

## Invoke the one engine

Use Bash 3.2+, Git 2.20+, flock and the standard Unix tools listed by the
installer/README. On Linux flock is util-linux; on macOS the external dependency
is discoteq/flock 0.4.0 (`brew install flock`). Missing dependencies are a
diagnostic: do not install them as a side effect. curl is bootstrap-only.

Run the owner-relative script with separate safely quoted arguments, capturing
exit status, stdout and stderr. For example, with established values:

```bash
bash "$skill_dir/scripts/ris-install.sh" install --project "$project"
bash "$skill_dir/scripts/ris-install.sh" update --project "$project" --ref "$ref"
bash "$skill_dir/scripts/ris-install.sh" uninstall --project "$project"
```

Omit `--ref` entirely when absent. Never interpolate request text as shell code,
use eval, or source the version file. The fixed package source is
`https://github.com/atilla777/ris.git`; there is no alternate-source option.
Update requires an existing managed element or version file (manual installation
is enough); when absent report the engine's `use install` result and stop.

## Verify and report

Exit **0 plus applicable filesystem evidence** is required for success, not
stdout alone. The engine verifies the complete selected Git tree, bytes/modes,
foreign files and cleanup; do not implement a second installer to verify it.
Check the reported physical project root matches the selected target, the
expected managed directories/management skill, command and executable script
exist for install/update, and no transaction journal remains after success.
Count actual managed skill directories/commands and compare with the report.
Read `.opencode/ris-installation` strictly as four lines of data:

```text
format=1
source=https://github.com/atilla777/ris.git
revision=<full-40-hex-commit>
harness=opencode
```

Compare its full SHA with the report and explicit commit pin (or resolved tag
when independently available); do not claim a tag resolves correctly without
evidence. For uninstall verify the managed namespace and version file are absent,
including this skill/command/script, and no journal remains. Already absent is
an offline successful no-op. Inspect ordinary target `git status` when Git exists;
files/version stay available to its normal workflow. Do not initialize Git,
change ignores, force-add, commit or push. Existing ignores are not overridden.

On nonzero exit inspect diagnostics and actual state. Distinguish **not changed**,
**restored**, **recovery required**, and **applied/restored with cleanup incomplete**;
nonzero does not imply no write or a rollback. A busy lock permits no new writes.
For interruption, a repeat valid request first recovers offline using schema 1,
then processes the request; repeat only within the existing authorization.
If the installed script vanished, use the README checked-download bootstrap with
a compatible schema-1 engine and the same target. For unknown/damaged journal
preserve and report the exact `.opencode/.ris-install-transaction/` path and
diagnostics; stop for diagnosis, never delete evidence or install over it.
Report any separately named temporary-engine cleanup path too. Guarantees cover
process interruption on a working filesystem, not power/storage/OS crashes,
ACLs/xattrs or concurrent edits by noncooperating tools.

Return operation, physical target, source, full installed SHA (none for removal),
counts, actual exit/outcome, checks and any remaining evidence/recovery paths.
**Tell the user to quit and restart OpenCode**: the current session retains its
loaded instructions even after self-update/removal. Stop at the checked package
outcome; project initialization and normal Git publication are separate work.
