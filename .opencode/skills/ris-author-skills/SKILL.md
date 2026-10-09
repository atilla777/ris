---
name: ris-author-skills
description: >-
  Create or improve ready-to-use source folders for RIS package skills,
  RIS-integrating project skills, and standalone project skills. Use for a
  request to write or revise an agent skill's instructions and resources;
  not for installing skills, configuring OpenCode alone, or executing the
  lifecycle task described by a skill.
---

# Author an agent skill

Own the source skill folder (`SKILL.md` and only resources it actually needs).
Work on the requested skill, not the lifecycle stage the skill will eventually
perform. A source folder is not an installation, a discovered skill, or a
publication. Follow the person's language for the conversation and the
target project's/user's language for a project skill. Use English for
RIS-distributed operational instructions and metadata.

## Dependencies and preparation

Ensure the current `ris-common` instructions are available in this session via
the host skill loader or its actual installed location; apply its baseline
rules now and read its owned conditional resources before dialogue, artifact
work, and checking respectively. Do not assume it lives beside this skill or
that merely naming it loads or applies it. If unavailable, report what part
cannot be completed. Investigate the request, project instructions, existing
skills, nearby owners, and affected consumers before asking for facts available
locally. Check the destination and write permission before editing; do not
overwrite an existing folder as though it were a new skill.

Determine whether **this authoring operation** needs RIS project settings
(for example, resolving a configured project document directory for an input
or output). If so, ensure `ris-context` and its owned configuration resource
are available, prepare context for this specific operation, and check its
status, provenance, relevant paths, diagnostics and permission scope before
using them. An absent optional `ris.yaml` uses package defaults; an explicitly
chosen inaccessible/invalid config is an error, not a fallback. A project
skill that will later need context may declare that dependency even if the
author does not need project settings to write it today. Do not call
`ris-context` just because this author is a RIS skill, or force RIS
dependencies onto a standalone target. Neither dependency automatically
installs the result or authorizes writing.

## Establish the contract

Identify the target type, owner and destination, goal and observable defect
(for improvement), use triggers and nearest non-use cases, inputs and their
readiness, expected output, allowed changes, acceptance checks and stop/error
conditions. Resolve missing user decisions in dependency order under
`ris-common` dialogue rules; a suggestion is not an accepted requirement.
Choose among these targets explicitly:

- **RIS package skill:** name the folder and skill `ris-*`; apply the relevant
  RIS result/operation contract, ownership and dependency rules. An applied
  skill owns its result and stop condition, even when it composes other skills.
  Shared rules belong to `ris-common`; project settings preparation belongs
  to `ris-context` only when needed. Do not assert that an illustrative or
  future RIS skill or adapter has been implemented.
- **RIS-integrating project skill:** follow the project's conventions and
  Agent Skills format; apply RIS rules only for its actual RIS responsibilities.
  Declare and execute relevant dependencies at the right time, including for
  direct invocation, without imposing package naming on the project skill.
- **Standalone project skill:** follow the project's and user's rules and
  Agent Skills format; do not introduce RIS naming, configuration, or runtime
  dependencies just because this author is part of RIS.

For an improvement, inspect the existing contract, the reported problem and
affected consumers/neighbor skills. Preserve accepted behavior outside the
agreed change and identify comparable before/after scenarios, including
selection failures, before modifying it. If the desired change contradicts
accepted behavior, resolve the decision rather than silently changing it.

For each proposed step, identify whether it is necessary to the promised
result, already owned by a dependency (for example, project path preparation
by `ris-context`), or a distinct operation with its own inputs and checks.
Keep target selection with the owner of the result when it is needed to perform
that result; split independently useful discovery or a different substantive
operation into its own skill only when its contract warrants it. Put coordination
of multiple results in the calling composite skill. Do not split by line count
or add a wrapper solely for symmetry. For RIS package skills record the reason
for a portable base/project wrapper or a single skill. A separated portable
base must work without required `ris-common`, `ris-context`, `ris.yaml` or RIS
project directories; the project wrapper depends on the base and owns its RIS
integration. For other targets apply the same ownership test without imposing
RIS dependencies.

## Build the source

Write `SKILL.md` in the selected source folder with Agent Skills frontmatter:
`name` (matching the folder; lowercase alphanumeric words separated by single
hyphens, at most 64 characters) and a nonempty `description` (at most 1024
characters). Describe the result, positive triggers and nearest exclusion in
the description; make the body the actual usable contract. In plain, actionable
language cover purpose and owner, when to use or defer, inputs and readiness,
dependencies and their activation, permissions, method, outputs, verification,
failure/partial result and stopping point. For a composite skill state who
combines the results and how, rather than claiming loading alone performs work.
Avoid invented frontmatter imports, parameters, automatic dependency loading,
unavailable tools or hard-coded RIS-repository paths.

Keep reusable shared rules with their existing owner; include only necessary
local references/assets/scripts inside the target folder. Resolve owned
resources relative to that folder's **installed location**, not the source
repository. Do not make a separately editable copy of another contract.
Keep the main `SKILL.md` sufficient to select the skill, activate dependencies,
and own and check its result. Put lengthy detail for a conditional branch in
an owned reference with an explicit trigger, read before that branch; do not
load it for unrelated requests. Moving text to a reference does not make a
second responsibility belong to this skill. Keep mandatory instructions
available when their conditions apply; context savings never justify skipping
required behavior or evidence.
Distinguish workflow method, common rules, project configuration, restricted
operations and host-specific commands. Put a thin command in host integration
only when manual invocation is useful; it must not replace the skill contract.
Respect the selected destination and scope; never install the generated skill
unless separately requested and permitted. If writing is not permitted, give
an explicitly unsaved draft instead of claiming a file exists.

## Check and finish

Inspect actual saved files/diff and resource links. Check metadata, name vs
folder, declared dependencies' actual availability and absence of dependency
cycles, scope and permissions, and preservation of accepted behavior. Test
selection with natural relevant, neighboring and irrelevant requests, and
exercise execution in the target environment on small representative inputs;
for an improvement compare the affected before/after cases. Check the resulting
files/actions, not just the agent's assertion. Separate structural, routing and
behavioral evidence and label any unrun check; structure alone does not prove
production readiness. Do not claim compatibility with an untested client.

Review for unrelated operations, duplicated dependency methods and unnecessary
loading on a typical request. If the skill has a conditional branch, check that
its instructions and evidence are available when triggered, not loaded for an
unrelated request. For an improvement, compare before/after loading where
observable; shorter text or more skills alone are not evidence of improvement.

Report the source location or unsaved draft, actual changes, checks and
observations, remaining limitations and any unresolved decisions. If a
required input, dependency or verification is missing, report the independent
part and what is blocked rather than calling the whole result complete. Stop
after authoring and checking the requested source; do not initiate another
lifecycle stage or imply it is installed.
