---
name: ris-author-skills-base
description: >-
  Create or improve an autonomous Agent Skills source folder from worked-out
  requirements. Use for a standalone skill, including one in a project that
  happens to use RIS. Its method may be composed by a result-owning RIS author;
  do not use it alone to own RIS integration, install a skill, or perform the
  operation described by the skill.
---

# Author an autonomous Agent Skill

For autonomous requests own the source folder (`SKILL.md` and only resources
it needs); when composed by a RIS author, provide the general method while
that author owns the combined result. Do not take over its RIS integration.
Do not perform the operation the resulting skill will later perform. Follow the user's language
in conversation and the target project's language for its skill. Apply the
project's instructions and permissions. Work directly without requiring any
particular project layout, configuration file, or other skill installation.

## Establish the result

Use already worked-out requirements supplied in the request or a document;
there is no mandatory document format. Inspect the project's instructions,
existing skill and consumers (for an improvement), neighboring skills and
available facts before asking for missing facts. Identify destination and
write scope, purpose, owner of the result, positive triggers and nearest
non-use cases, inputs and readiness, expected output, acceptance evidence,
dependencies, failure and stopping conditions. An improvement needs an
observable defect, preserved accepted behavior and comparable before/after
selection and execution cases. Resolve a contradiction with accepted behavior
instead of silently changing it.

If a substantive user choice or essential subject-matter contract is missing,
state the specific gap and request clarification; do not invent behavior or
conduct a new full requirements interview. An incomplete draft may be labeled
as such, never as a verified result. Check whether a proposed extra step is
necessary for the promised result, belongs to a dependency, or has a separate
result and owner. Do not create extra skills for line count or symmetry.

## Build the source

Check the destination and permission before editing; preserve existing work.
Write Agent Skills frontmatter with `name` matching the folder (lowercase
alphanumeric words separated by single hyphens, at most 64 characters) and a
nonempty `description` (at most 1024 characters) stating result, positive use
and nearest exclusion. In actionable language describe inputs, readiness,
dependencies and how to activate them for direct invocation, permissions,
method, output, verification, error/partial-result behavior and stop point.
For a composed result name who combines and checks the contributions: listing
dependencies alone does not execute them. Respect the project's conventions.

Keep only necessary local references/assets/scripts inside the skill folder;
resolve resources relative to that folder after installation. Keep the main
file sufficient to select the skill and invoke dependencies. Put lengthy rare
branches in owned references with explicit read conditions; do not hide
mandatory instructions or duplicate another owner's method. Avoid invented
frontmatter imports, automatic loading, unavailable tools and hard-coded paths
to the author's workspace. For critical risks, give subject-specific shortcuts
to avoid and observable failure signals with corrective reactions, rather than
empty boilerplate headings. Compare accepted constraints and exclusions with
the written result.

Deliver the ready-to-use **source**, not an installed or published skill.
Never install it or start its subject-matter operation without separate
authorization. If writing is not permitted, provide an explicitly unsaved
draft instead of claiming a file was created.

## Check and hand off

Inspect saved files and diff, metadata, links, resource availability,
dependency cycles, permissions and preserved behavior. Test selection on
natural positive, neighboring and irrelevant requests, and actual execution
on small representative inputs in the target environment; inspect resulting
files and effects rather than trusting the agent's report. For an improvement
compare affected before/after cases and loading where observable. Temporary
installation of test fixtures for behavioral checks does not install the
requested skill in the user's project. Separate structural, routing and
behavioral evidence; mark unrun checks as unverified and do not claim
compatibility with untested clients.

Report source location (or unsaved draft), changes, checks and observations,
limitations and unresolved decisions. If a required input, dependency or
check is missing, report independent progress and the blocked part. Stop
after the requested source and its checks; do not begin another stage.
