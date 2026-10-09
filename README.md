# RIS — Ready-to-use Infrastructure Skills

RIS is a growing collection of source skills for AI agents working across the
software development lifecycle. The first application skill,
`ris-author-skills`, creates and improves skill source folders for the RIS
package, RIS-integrating projects, and standalone projects. It does not install
the skills it creates.

## Available source skills

- `skills/ris-author-skills/` — author or revise an agent skill and check its
  source, selection, and behavior.
- `skills/ris-common/` — shared rules applied by RIS skills.
- `skills/ris-context/` — read-only preparation of project settings when an
  operation needs them; an optional `ris.yaml` can override package defaults.

Each folder contains an Agent Skills `SKILL.md`. Install the folder **with its
resources** into a skill discovery location supported by your client before
using it. For OpenCode 1.18.33, one project-local location is
`.opencode/skills/<name>/`; `ris-author-skills` also needs `ris-common` and,
for authoring operations requiring RIS project settings, `ris-context`.
Installing a source folder does not install skills created by the author.
This repository installs all three source skills in `.opencode/skills/` for its
own OpenCode project; the copies there must be kept in sync with `skills/`.
The optional project command `.opencode/command/ris-author.md` exposes
`/ris-author <request>` in OpenCode once the author skill is discoverable;
direct requests use the same skill contract. Restart OpenCode after changing
skill or command files so a running session picks them up.

The [specification](docs/specs/README.md) describes RIS architecture
and future components; it is not a list of installed skills. A staged
[implementation specification](docs/specs/ris-foundation-and-skill-author.md)
records the agreed scope of the initial source skills.
This repository's [development rules](docs/rules/development.md) and root
[`ris.yaml`](ris.yaml) identify its actual document and local task directories.

## License

MIT — see [LICENSE](LICENSE).
