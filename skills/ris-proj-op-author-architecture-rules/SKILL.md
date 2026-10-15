---
name: ris-proj-op-author-architecture-rules
description: >-
  Create or revise a RIS project's normative architecture rules from project
  evidence and a focused interview, obtain explicit acceptance and save the
  accepted scope as OKF in sources.rules. Use for project architecture-rules
  authoring or a bounded amendment; not for code audit, feature design, delivery
  impact, engineering rules, tooling setup, library extraction or format migration.
---

# Author project architecture rules

Own the **accepted, saved and document-checked architecture scope** in one
selected project's rules bundle. Apply the portable content method; own project
inputs, acceptance, persistence and the combined result. This is a project
wrapper, not a two-author scenario. Do not call the engineering author, choose
a next skill, audit implementation compliance, enumerate delivery impact,
extract a library or change product, code, tools, config or tracker. Preserve
the project's task, permission and publication process. Saving here does not
publish Git or tracker history.

## Prepare the selected scope

1. Establish the target project/current working-copy root, create/update,
   requested architecture subject, authorized writer/acceptance authority and
   whether the request permits saving after acceptance or only a proposal.
   A request to author rules permits preparing them, not accepting them for
   the person. Create needs purpose, nearest goal, constraints and known or
   discussed stack; no product bundle, roadmap, tracker or complete design is
   mandatory. Update additionally needs existing rules and an explicit boundary;
   missing input blocks update, never silently becomes create.
2. Load and apply installed `ris-proj-lib-common`, including its dialogue, artifacts and
   quality resources before their respective actions. Load and actually apply
   `ris-proj-op-resolve-context` and its configuration resource for this operation: require
   `sources.rules`, input in update/prospective output in create. Check status,
   provenance, resolved paths, diagnostics and permitted scope. Source paths
   belong to the selected **current worktree**, not the installation or primary
   copy; no workspace paths or execution roles are needed for this operation.
   Do not load a configured task adapter just because it exists.
3. Inspect the selected rules root, its root index/version, relevant architecture
   documents and applicable neighboring development/process rules. Determine
   the actual storage protocol and preserve the usable layout and identities.
   Record baseline bytes/absence for all prospective writes, including indexes,
   existing affected logs and decision evidence; identify relevant read-only
   dependencies to recheck. Do not interpret ordinary Markdown, OKF 0.1 or an
   unknown/versionless format silently as OKF 0.2. A declared 0.2 root does not
   prove every concept was converted. If a required conversion reaches beyond
   this scope or changes the storage protocol, return a proposal and block the
   dependent save until separately authorized. Never migrate neighboring rules.
4. Load and apply installed project `ris-proj-op-manage-okf-bundle`, passing the already established
   project/config provenance, explicit `sources.rules` bundle root, operation,
   bounded concepts/indexes, applicable rules and permissions. It applies
   `ris-port-op-manage-okf-bundle` and the base-owned pinned specification; this author retains
   content/acceptance ownership. Check dependency/resource
   availability before promising format-dependent results. Missing resources
   block the dependent action, not permission to imitate them.

## Apply the content method

Load and actually apply installed `ris-port-op-formulate-architecture-rules` with
create/update, the subject/boundary, purpose/nearest goal, constraints, factual
and proposed stack, sourced current evidence, existing decisions/exceptions,
neighboring rules and already confirmed interview answers. Its resources
resolve from its own installed folder. It chooses applicable profiles and
conditionally applies `ris-port-op-interview` for interdependent unknowns; keep
one dialogue and do not repeat confirmed answers. Do not reproduce that method
or treat loading its name as a content result.

Inspect its substantive proposal, sources/statuses, exact update delta,
deferred questions/triggers, exceptions, adjacent conflicts and checks. Check
that it is sufficient for this scope, not merely generic headings, and matches
project evidence. Missing material decisions remain open or block their
dependent norm; no automatic ECS, Service Layer or full future design. Rules
describe normative obligations, not components falsely claimed implemented.
For an existing project, include an applicable scoped transition policy when
needed without claiming old code complies or creating a migration backlog.
Architecture owns what must hold; engineering owns versions/tooling/practices.
Show a necessary neighboring amendment without changing it. An explicitly
accepted limited result may retain that visible dependency; do not claim
overall consistency while a related conflict remains unresolved.

## Present, accept, save and check

For a first bundle, **only if a layout illustration is useful**, read
`assets/rules-example/index.md`, `assets/rules-example/architecture/index.md`
and `assets/rules-example/architecture/principles.md` from installed `ris-proj-lib-common`.
This non-binding example does not replace the base/profile or require reading
the engineering example/author. Do not copy its whole bundle or example status
into project rules. Existing bounded updates need no example.

1. Assemble a concrete candidate in the project's language using `ris-proj-op-manage-okf-bundle` for
   format. Show the actual normative content (update: old → new norms), exact
   file/section scope, necessary navigation changes, candidate version and
   source-material version/provenance. Explain exceptions, deferred decisions,
   conflicts and unconfirmed applicability **before** acceptance. Do not publish
   unused profile alternatives, placeholders or drafts at normative paths.
2. Obtain explicit acceptance of **this content, version and scope** from the
   authorized person/channel. Interview answers, permission to create, an
   existing file, format validation or a base proposal are not final acceptance.
   If refused, absent or proposal-only, make zero normative writes and return
   the unsaved proposal. A substantive change after acceptance needs renewed
   acceptance of the affected part.
3. Use the project's accessible decision/version convention, without requiring
   a new manifest or tracker. If none exists, propose a concise decision and
   provenance section in a scoped architecture concept: candidate revision,
   precisely identified normative sections/files, real acceptance decision and
   known actor/date/source version. Include this placement in the presented
   scope. Do not invent an identity or template version. A revision label must
   identify the exact shown content; include a content digest or accessible
   revision when needed for unambiguous recovery. If evidence records a digest,
   keep the evidence outside the hashed content to avoid self-reference.
   Persist the actually used source-material provenance/version with the
   accepted result, including the base/profile package revision or resource
   digest from available evidence. If it is unavailable, obtain it through
   permitted tools or the supplied package identity; never manufacture it or
   silently omit the limitation from the combined-result assessment.
   Do not use OKF `verified` to imply implementation compliance or substitute
   for the scoped decision. If acceptance cannot be made accessible, report
   that gap rather than call the combined result complete.
4. Immediately before saving, reread baseline files/absence and relevant
   dependencies, compare actual bytes and confirm paths still resolve inside
   authorized scope. Stop dependent writes on an unexpected change; show the
   conflict and reconcile the candidate/acceptance instead of overwriting it.
   Follow the project's concurrency/write protocol; a baseline comparison is
   conflict detection, not atomic CAS or protection against every race. If a
   required guarantee cannot be established, block that write. Keep any short
   write window separate from the interview/acceptance conversation.
5. Save only accepted architecture content, decision evidence and necessary
   navigation/affected existing log entries via `ris-proj-op-manage-okf-bundle`. One rules bundle:
   architecture and ADR directories are nested knowledge, not separate roots.
   On first create, use only a minimal root `index.md` declaring
   `okf_version: "0.2"`, an architecture index and sufficient concepts; every
   real knowledge directory is indexed under the RIS profile. Nested indexes
   have no frontmatter; concepts have a nonempty string `type`. Preserve an
   existing usable layout; do not require particular filenames or split a
   small scope into empty files. Common-index edits are navigation only:
   retain neighboring entries/text/extension fields, do not copy norms into
   indexes or create the absent engineering area. No new log is mandatory.
6. Reread actual saved files. Compare normative content/decision/version with
   acceptance and unaffected bytes with the baseline. Apply `ris-proj-op-manage-okf-bundle` checks
   and resolve changed links (leading `/` from the rules root, relative links
   from their file; cross-bundle targets explicitly). For create of a new
   minimal bundle, check that entire created bundle and RIS directory indexes.
   Adding an architecture area to existing rules, or updating it, checks only
   changed concepts/indexes and affected links. Report OKF mandatory violations
   separately from recommendations and stricter RIS profile requirements.
   An unrelated unchecked/invalid concept does not authorize its repair or
   imply whole-bundle conformance; a fault directly preventing a correct scoped
   save blocks that write. Subject sufficiency remains this wrapper's check.

On any failed, partial or ambiguous write, stop further writes and reread
actual state before considering a retry. Return exact saved/unsaved parts,
current versions and missing navigation/evidence/checks. Do not blindly retry,
roll back foreign edits or claim a partially indexed result complete. A later
attempt reconciles persisted content and prior acceptance before writing.

## Return and stop

Report `ok|blocked|conflict|error`, project/current root and context provenance,
operation/scope, real document addresses and version, accessible acceptance
address/decision, source provenance, actual changes, subject and scoped OKF/RIS
checks, neighboring conflicts, deferred questions and limitations. Distinguish
proposed, accepted and saved; `ok` for the promised saved result requires all
three plus read-back checks. An unchanged retry may return existing accepted
content only after checking its version, decision and files; no fresh approval
or duplicate history is inferred. Report proposal-only completion as such,
not as accepted/saved rules. State that implementation compliance, delivery
readiness and remote publication were not established by document checks.
Stop at this result; installed template changes never update project norms.
