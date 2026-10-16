# Installing, updating and removing RIS

Use the [README quick start](../README.md#install-in-opencode) for first installation.
All package operations use one
[Bash engine](../skills/ris-port-op-manage-installation/scripts/ris-install.sh).
The [management skill](../skills/ris-port-op-manage-installation/SKILL.md) invokes
that same engine; it does not implement a separate copying algorithm.

## Requirements

Choose an **existing absolute project path**; spaces are supported. Runtime tools:

- **Bash 3.2+, Git 2.20+, flock**.
- Standard Unix `cp`, `mv`, `rm`, `mkdir`, `rmdir`, `mktemp`, `chmod`, `cmp`,
  `diff`, `id`, `ls`, `readlink`.
- On Linux use util-linux flock. On macOS install **discoteq/flock 0.4.0**,
  for example with `brew install flock`; `/bin/bash` is sufficient.
- `curl` is needed only for the README download step. Python 3 is development/test-only.

The installer reports missing tools and never installs dependencies. It does not
require `ris.yaml`, Beads, OpenCode or a Git repository in the target project.
Project-integrated skills have their own prerequisites after installation.

## Selecting a version

Leave `ref` empty in the quick start to follow upstream remote HEAD, regardless of
branch name. Set it to an **exact tag** or **full 40-hex commit SHA** to pin a version.
The downloaded raw script and `--ref` use the same pin.

Branch names and Git revision expressions are not `--ref` inputs. Lightweight and
annotated tags are supported; a 40-hex tag spelling is interpreted as a commit SHA.
For tags containing URL-special characters, URL-encode `raw_ref` in the bootstrap
while retaining the literal tag in `ref`. Incomplete package revisions are rejected.
Download errors stop before script execution; the bootstrap does not use `curl | sh`.

## Manage from an agent

After RIS is available to the agent, use an explicit operation and target:

```text
/risb-installation install RIS in /absolute/path/to/project
/risb-installation update RIS in /absolute/path/to/project to tag v-example
/risb-installation uninstall RIS from /absolute/path/to/project
```

The skill clarifies missing intent or target, runs its owner-relative script and
checks exit status, paths, counts and the version record. Update/removal is never
silently changed to install. `v-example` is a placeholder for your chosen tag.

## Manage from the shell

**First migration from long commands:** an old installed engine cannot acquire
the compact package. Use the README checked-download bootstrap from the chosen
new package revision, with that same tag/full SHA for both script and package.
Its `install` fully replaces the previous package; alternatively run that newly
downloaded engine's `update` against an existing installation. Do not run the old
installed engine for this first migration. Subsequent updates use the new installed
engine at the unchanged technical path below. There are no old-name aliases.
See the [complete 39-command map](skill-command-naming-migration.md#compact-command-migration--39).

```bash
bash '/absolute/project/.opencode/skills/ris-port-op-manage-installation/scripts/ris-install.sh' update --project '/absolute/project' # Optional --ref TAG_OR_SHA
bash '/absolute/project/.opencode/skills/ris-port-op-manage-installation/scripts/ris-install.sh' uninstall --project '/absolute/project'
```

`install` fully replaces an existing or manual installation. `update` requires
at least one managed element or version file. `uninstall` removes the managed
package and rejects `--ref`; repeating it is an offline successful no-op.
After the installed script is gone, an external copy of the engine can perform
that repeated request.

**Quit and restart OpenCode after package changes.** A running session retains
its loaded instructions.

## What changes and what is preserved

The reserved package paths are:

- `.opencode/skills/ris-*` — complete skill folders and their resources.
- `.opencode/command/ris-*.md` — retired/legacy slash-command templates.
- `.opencode/command/risp-*.md` and `risb-*.md` — compact command templates,
  only after package ownership has been established.
- `.opencode/ris-installation` — four-line format/source/full revision/harness record.

**Local edits to proven package paths and legacy reserved paths are overwritten**,
and retired elements are removed. Short-name ownership is recorded by the shipped
management-skill resource `references/command-ownership.txt`, whose list must
exactly cover the selected package's compact command files, without extra paths.
An old version marker or the new prefix alone is insufficient. Pre-existing
unproven short files/links cause a conflict before replacement/removal: preserve
them, inspect their ownership and explicitly resolve the collision (for example,
move your own command to a non-package name) before repeating. Ordinary proven
package updates require no extra per-file approvals. Keep this ownership resource
with complete manual package copies; do not extend it to claim foreign files.
Use names outside `ris-`, `risp-` and `risb-` for project additions. No timestamp or
backup history is kept in the unchanged four-line version record.

Other skills and commands, OpenCode settings, `ris.yaml`, `AGENTS.md`, docs/tasks,
alternate `skill/` and `commands/` locations, and global installations are preserved.
Check alternate/global locations for shadowing; the installer does not migrate them.
For old identifiers and consumer/config changes, see the
[namespace transition guide](skill-command-naming-migration.md).

Ordinary parent directories are required: symlink parents and unsafe managed
objects are refused. Old managed links are replaced as links without touching
their external targets.

Verify the full SHA and skill/command counts in the success report, inspect
`.opencode/ris-installation` and ordinary `git status`. Installed files and the
version record remain subject to the project's normal Git workflow. The installer
does not add ignores, initialize Git, commit or push, and does not override
existing project ignore rules.

## Interruption and recovery

The engine serializes cooperating processes for the same OS user and physical
project root. A busy lock exits without target writes. Before replacing its own
script, it continues from a private external copy.

A verified snapshot and schema-1 journal at `.opencode/.ris-install-transaction/`
support offline recovery **before any network operation**. A pre-commit failure
restores old bytes, types, modes and link targets. After SIGKILL, the next valid
request repeats the restore from immutable backup. Committed or rolled-back
terminal markers permit cleanup only, even after partial backup removal.

Exit **0** means verification and cleanup completed. Nonzero diagnostics distinguish
not changed, restored, recovery required, or applied/restored with cleanup incomplete.

- Repeat a valid request to finish recovery or cleanup.
- If the installed script was removed by interruption, use the README bootstrap
  again for the same project with a compatible schema-1 engine.
- If the journal is unknown or damaged, preserve its exact reported path for
  diagnosis; do not delete it or try another install over it.

Guarantees cover process interruption on a working filesystem, not power loss,
storage corruption, ACLs/xattrs or concurrent edits by other tools.

## Manual installation of a portable skill

Copy the **complete** skill folder, including resources, into a client-supported
discovery location. For example, the autonomous interview needs no RIS config or
other RIS skill. In OpenCode copy:

- `skills/ris-port-op-interview/` → `.opencode/skills/ris-port-op-interview/`.
- Optional: `commands/opencode/risb-interview.md` → `.opencode/command/risb-interview.md`.

Quit and restart OpenCode. Directly loading `ris-port-op-interview` needs no
command. A selective copy lacks the complete package's ownership evidence: before
a subsequent full install, explicitly reconcile that manually copied short
command if it causes a collision. Legacy reserved skill folders are replaced.
