# RIS — Ready-to-use Infrastructure Skills

RIS is a growing collection of source skills for AI agents working across the
software development lifecycle. The application skill
`ris-author-skills` creates and improves skill source folders for the RIS
package, RIS-integrating projects, and standalone projects. It does not install
the skills it creates. Two OKF skills operate on Open Knowledge Format bundles.

## Available source skills

- `skills/ris-author-skills/` — author or revise an agent skill and check its
  source, selection, and behavior.
- `skills/ris-common/` — shared rules applied by RIS skills.
- `skills/ris-context/` — read-only preparation of project settings when an
  operation needs them; an optional `ris.yaml` can override package defaults.
- `skills/ris-okf/` — read, create, edit and check a selected OKF bundle using
  a pinned local copy of the official OKF 0.2 specification; direct use does
  not require RIS project configuration.
- `skills/ris-project-okf/` — resolve a RIS project's configured specifications
  directory and operate on an explicitly rooted OKF specification via `ris-okf`.
- `skills/ris-plan-roadmap-base/` — prepare and check a bounded roadmap proposal
  from explicitly supplied inputs, marking unaccepted goals and gaps, without
  RIS project dependencies or tracker writes.

Each folder contains an Agent Skills `SKILL.md`. Install the folder **with its
resources** into a skill discovery location supported by your client before
using it. For OpenCode 1.18.33, one project-local location is
`.opencode/skills/<name>/`; `ris-author-skills` also needs `ris-common` and,
for authoring operations requiring RIS project settings, `ris-context`.
`ris-okf` needs `ris-common`; `ris-project-okf` needs `ris-common`,
`ris-context` and `ris-okf` installed with their resources.
Installing a source folder does not install skills created by the author.
This repository installs all six source skills in `.opencode/skills/` for its
own OpenCode project; the copies there must be kept in sync with `skills/`.
The optional project command `.opencode/command/ris-author.md` exposes
`/ris-author <request>` in OpenCode once the author skill is discoverable;
direct requests use the same skill contract. Restart OpenCode after changing
skill or command files so a running session picks them up.

The [normative specification](docs/concepts/README.md) describes RIS architecture
and future components; it is not a list of installed skills. A staged
[implementation specification](docs/specs/ris-foundation-and-skill-author.md)
records the agreed scope of the initial source skills.
This repository's [development rules](docs/rules/development.md) and root
[`ris.yaml`](ris.yaml) identify its document and future SDLC workspace directories.
The development queue remains in Git-ignored `tasks/`; it is separate from
the configured `.sdlc/tasks/` for future tracker task artifacts.

## License

MIT — see [LICENSE](LICENSE). The pinned third-party OKF specification in
`skills/ris-okf/references/spec-v02.md` is Apache-2.0; see its
[source attribution](skills/ris-okf/references/source.md).
