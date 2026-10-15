---
name: ris-proj-op-update-documentation
description: >-
  Synchronize explicitly authorized RIS project documentation with an inspected
  implementation and integration state. Use for affected API/examples/rules and
  architecture documentation updates; not authoring product requirements, feature
  redesign, whole-project audit or Git publication.
---

# Synchronize affected documentation

Own bounded, verified documentation changes or a justified no-change result.
This is a reusable project operation; it has no separate portable base because
its result is authorized project synchronization, while format knowledge belongs
to the selected format specialist. Load/apply `ris-proj-lib-common` and applicable resources,
and `ris-proj-op-resolve-context` for the requested document sources and, if saving task evidence,
shared workspace paths. Require selected project, affected implementation/task
scope, actual code/tree evidence, integration state and permitted document paths.
No adapter or execution role is required unless task reads are actually needed.

1. Inspect relevant existing API instructions, examples, user/technical docs and
   rules alongside current code. Identify concrete stale statements and needed
   changes; do not scan every project document or create empty files for ceremony.
   Sources designate knowledge owners, not automatic write authority. Product
   is author-owned: propose needed behavior/source corrections, but do not edit
   it without separate explicit permission for the precise scope.
2. Update only permitted statements. Current architecture maps must describe
   actually integrated, checked components/contracts/state owners. Before
   integration, proposed synchronized text may be prepared in the change branch,
   explicitly as pending integration; do not publish it independently as current.
   Future components stay future in accepted design/ADR. Keep normative principles
   distinct from factual implementation. Record the implementation/tree on which
   each material factual change depends so integration can revalidate it.
3. For an explicitly selected OKF bundle, load/apply installed project `ris-proj-op-manage-okf-bundle`
   before edits/checks, passing the established project/config provenance,
   explicit root, operation, bounded scope, rules and permissions. It applies
   `ris-port-op-manage-okf-bundle` with the base-owned format resource; substantive synchronization
   remains here. Identify the real bundle root and
   approved RIS profile: type-frontmatter, indexes in real knowledge directories,
   bundle-root links and nested architecture/ADR all remain coherent. Product and
   rules are separate bundles. Ordinary `spec.md`/`design.md` remain ordinary
   Markdown: do not add an index/frontmatter for uniformity or silently migrate
   a legacy tree. A malformed/legacy bundle needing migration is a bounded gap,
   not permission to restructure it.
4. Read back changed documents, resolve links/navigation and inspect final diff.
   Verify claims against the specified code tree and integration state; preserve
   source decisions and unrelated work. If publication/integration changes code,
   these checks must be assessed again before claiming documents current.

Return status, authorized scope, changed files or justified no-change, code/tree
and integration state, claim-to-code/format/link checks, pending integration and
unresolved permission/knowledge gaps. No autonomous product rewrite, design
acceptance, tracker writes/closure, publication or following-operation launch.
