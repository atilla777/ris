---
name: ris-project-okf
description: >-
  Read, create, edit, or check an explicitly rooted OKF specification in a RIS
  project's configured specifications directory. Use for project-scoped OKF
  specification work; not for ordinary Markdown, bundle discovery, or direct
  bundle work without project path resolution.
---

# Operate on a RIS project's OKF specification

Own the combined result for an explicitly specified OKF bundle root and
read/create/edit/check operation in the project's `sources.specs` directory.
For ordinary Markdown specifications use the calling specification workflow;
for direct bundle work without project path resolution use `ris-okf` alone.

Ensure current `ris-common`, `ris-context` and `ris-okf` instructions are
available via the host loader or their actual installed locations. Apply
`ris-common` and its conditional resources. For this operation, apply
`ris-context` with its installed `references/configuration.md`; check the
returned status, provenance and permission scope. Direct invocation must
perform the composition, not merely name or load dependencies. If a required
dependency is unavailable, report the blocked part without inventing paths
or an OKF validator.

Determine the project and requested operation from the request and project
instructions. Require the caller to supply the bundle root explicitly. If it
is missing or ambiguous, ask for it before bundle-dependent work; do not
discover bundles in the directory or infer the root from a document or link.
Have `ris-context` prepare only `sources.specs` as an input or prospective
output, as appropriate. Check that the supplied root lies within the resolved
specifications area and authorized scope, including its actual target when
symlinks are involved. Context preparation does not grant write permission.

For creation, require the requested content and authorization to write the
supplied root. Do not treat other Markdown files in `sources.specs` as OKF or
modify neighboring bundles.

Apply the installed `ris-okf` procedure and its pinned specification to the
supplied root for the requested operation; its format, version and
partial-result rules remain authoritative. Verify the outcome and report the
project/config provenance, bundle root, operation, actual result and limits
together. Stop after the requested project OKF specification work.
