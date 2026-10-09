---
name: ris-project-okf
description: >-
  Resolve and operate on a specific OKF bundle in a RIS project's configured
  rules, concepts, or specifications. Use for explicit project OKF work; not
  for ordinary Markdown in those directories, direct named bundles elsewhere,
  or generic project context preparation.
---

# Operate on a RIS project's OKF bundle

Own the combined project-facing result: prepare paths, select **one** bundle,
apply `ris-okf` to it and verify/report the operation. Do not infer OKF merely
because a document is under a configured directory. For a directly selected
bundle without project path resolution, use `ris-okf` alone.

Ensure current `ris-common`, `ris-context` and `ris-okf` instructions are
available via the host loader or their actual installed locations. Apply
`ris-common` and its conditional resources, then apply `ris-context` including
its installed `references/configuration.md` to the selected project's current
operation; loading a skill name is not executing it. If a required dependency
is unavailable, stop the dependent part without substituting hard-coded paths
or a homemade validator. Direct invocation of this wrapper must perform the
whole composition, not wait for an external orchestrator.

Determine the project root and operation from the request and project
instructions. Ask `ris-context` to prepare only the needed `sources.rules`,
`sources.concepts`, or `sources.specs` paths (input or prospective output as
appropriate), configuration provenance, diagnostics and permission scope. If
the optional config is absent use its package defaults; if a selected config
is invalid or lacks a required field, do not fill it from defaults. Check the
returned status and path authorization before inspecting or writing. A path
preparation result never selects a document or grants write permission.

Inspect the relevant configured directory and the request for a uniquely
identifiable OKF bundle. A root `index.md` with `okf_version`, a named OKF
concept or links can help locate a candidate, but a missing index does not
disqualify a bundle. Directories may contain ordinary Markdown, multiple
bundles, or nothing. Select only when the request and available documents
identify exactly one intended bundle/root. If no unique target is established,
ask which bundle is intended before bundle-dependent work; do not coerce the
entire directory into OKF or edit a plausible neighbor. For creation, obtain
an unambiguous target root and requested content; context may prepare a
prospective output directory, but it cannot choose its name or contents.

Once selected, actually follow the installed `ris-okf` procedure and its
pinned local specification for the requested read/create/edit/check operation.
Respect the base skill's version, permission and partial-result rules. Check
the resulting files and report project/config provenance, selected area and
bundle root, selection evidence, the base operation's result, format findings,
verification and limits together. Stop after the requested project OKF work.
