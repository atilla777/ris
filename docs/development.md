# Developing RIS

Read [AGENTS.md](../AGENTS.md), the complete
[development rules](rules/development.md) and root [ris.yaml](../ris.yaml) before
changing the repository. Source skills live in [`skills/`](../skills/), command
templates in [`commands/opencode/`](../commands/opencode/); installation is
synchronized from these sources.

Development state and dependencies belong to Beads (Dolt). New local task notes
live in the primary copy's `.sdlc/tasks/<confirmed-ID>/`; `tasks/PLAN-*` is a
historical archive. Git push does not synchronize Beads. Follow the rules for
review and separate Git/tracker publication and completion.

Publish from the task's own branch/copy, integrating the latest primary remote
branch there; shared local `main` is not a publication workspace. Ordinary tracker
work uses fresh checks, targeted native writes and read-back, without manual
writer windows or mandatory global locks. See the rules for exact guarantees.

For routine Beads inventories use the adapter's native compact forms, for example
`bd list --all --limit 0 --type task --brief --json` (or `--type epic`). For a
known ID use `bd list --id <id> --all --limit 0 --brief --json`, checking exact
cardinality and actual type; no global queue reread is needed just for that ID.
Children use `list --parent <id> --all --limit 0 --brief --json`; directed blockers
use `dep list <id> --type blocks --direction=down --json`. Counts do not replace
edges. Missing parent/spec fields need bounded exact/edge reads. Disclose necessary
content with `bd show <id> --brief-deps --json`: this keeps the full own record,
not a single-field projection. Omitted brief fields are not empty. Absence/dedup
still needs complete all-status/unlimited coverage and every field needed for
key/slug/spec/content predicates, including historical descriptions when relevant.
Errors, `no value`, malformed or truncated output cannot prove absence. Full
native JSON remains a fallback; do not use the failing Go-template projections.

Git publication uses native fetch/push `--quiet`; Dolt publication uses
fetch/push `--silent` for progress. Preserve stderr, exit status and verified
results without a mandatory new log. Git whole-outgoing-history checks, exact
reviewed-tree publication and independent remote read-back remain required. Dolt
uses authorized shared-main scope, ordinary non-force publication and fresh remote
revision/reachability assurance, with local exact-content checks kept separate.
See the [Beads adapter](../skills/ris-proj-adapter-beads-tasks/SKILL.md) and
[Git publication owner](../skills/ris-proj-op-publish-task/SKILL.md).

Ordinary instruction edits use reading, affected static checks and independent
review. This repository prohibits new agent behavioral tests; absence of a live
run does not block ordinary text work or require another run question. Static
readiness does not prove agent reliability, cost or repeatability. Existing
observations retain their versions and limits; unmet historical obligations remain
unverified. Portable skills follow the actual target project's rules. See the
[validation levels](concepts/05-adoption-and-validation.md#4-три-уровня-проверки)
and [evidence criteria](concepts/07-quality-and-verification.md#2-критерий-и-подтверждение).

## Package-installation checks

These are deterministic filesystem/CLI tests, not agent sessions:

```sh
python3 -m unittest discover -s tests/package_installation -p 'test_*.py' -v
PYTHONDONTWRITEBYTECODE=1 RIS_TEST_BASH=/bin/bash python3 -m unittest discover -s tests/package_installation_integration -p 'test_*.py' -v
bash -n skills/ris-port-op-manage-installation/scripts/ris-install.sh
```

The [CLI workflow](../.github/workflows/package-installation.yml) checks lock/copy
feasibility and the mechanism suite against minimal Git fixtures. The
[production integration workflow](../.github/workflows/package-installation-integration.yml)
captures the actual source package into a disposable upstream and checks lifecycle,
recovery and the README bootstrap. Both run on Linux and macOS with explicit
`/bin/bash` (3.2 on macOS) and externally installed flock.

The integration oracle derives expected files, bytes, types, executable modes,
directories and numeric skill/command counts from each selected source revision,
independently of the installer report and installed payload. Regression controls
cover source additions/removals, incorrect counts and missing/extra/changed entries.

The bootstrap integration test extracts the first `bash` block in README and
substitutes its project/ref inputs. Preserve that entry point when editing docs.
Workflow definitions are not evidence of a successful remote run; check actual
results and their applicability to the revision being assessed.

## Architecture, plans and delivery records

- [Normative concepts](concepts/index.md) and the
  [target SDLC methodology](concepts/08-sdlc-methodology.md) describe architecture
  and future components; they are not an installed inventory.
- [Repository rules](rules/index.md) include the current owner map. Concepts and
  rules are separate OKF 0.2 bundles under the [knowledge profile](concepts/knowledge-profile.md).
  `docs/concepts/` does not replace author-owned `docs/product/`.
- [Delivery specifications](specs/README.md) are ordinary Markdown. Historical
  names and immutable decision references are interpreted through the
  [namespace transition guide](skill-command-naming-migration.md).
- Installation: [specification](specs/package-installation/spec.md),
  [design](specs/package-installation/design.md),
  [delivery plan](specs/package-installation/delivery-plan.md).
- Continuity: [delivery records](specs/sdlc-continuity/).
- Retrospectives: [design](specs/session-retrospective/design.md) and
  [CLI policy amendment](specs/session-retrospective/cli-read-policy.md).
- Task execution: [delivery checks](specs/task-execution/delivery-checks.md).

Delivery evidence is bound to its original inputs and revision. Reusing it requires
checking applicability; a documentation edit does not establish new runtime,
review, integration or publication outcomes.
