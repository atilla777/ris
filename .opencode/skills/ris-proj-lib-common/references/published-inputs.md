# Discover and read saved project inputs

Read when a result depends on previously saved requirements, design, decisions
or other linked project evidence. The calling owner selects the material sources,
checks their substantive sufficiency/applicability and owns its result. This is
source discovery/reading, not copy preparation, publication or content acceptance.

1. Start from the selected project and exact tracker ID through its selected
   adapter, or an explicit document-only locator. Follow saved source/decision
   links and the checked document convention below. A mutable title is not an
   identity key. Legacy explicit source links and readable payload paths/refs are
   nonauthoritative discovery hints only: read actual documents and decisions.
   Missing, old or malformed JSON alone never blocks this route. Preserve old
   payloads/prose unchanged; do not validate a legacy schema, migrate on read or
   introduce a compatibility parser. Ambiguous identity, missing actual sources
   or unproved acceptance blocks only the dependent action with its exact gap.
2. Read each required published content version at its full Git commit and
   project-relative path/semantic section, then its separate decision at the
   pinned decision address. When objects are already available in the verified
   project repository, use read-only `git show <full-SHA>:<path>` (and tree/diff
   reads); this does not need a matching checkout. An explicitly known other
   copy is usable only after checking repository identity and exact version, not
   because its file exists. Use an exact immutable remote source if necessary;
   fetching missing objects or creating a copy requires the applicable permission.
   Do not silently fetch in a zero-persistent-change navigation operation. Report
   the missing object/access permission precisely if no permitted read route works.
3. Check the actual decision's content selector/version, acceptor and scope using
   the owner's acceptance protocol. Resolve decision-only `containing-commit`
    from its original immutable address, never from a later copy. Requirements and
    design may share a decision address only when that act explicitly accepts both
    independently identifiable content selectors/versions; check each entry rather
    than infer one acceptance from the other. A record flag,
   proposed design, publication or file presence is not acceptance. Read the
   complete selected substantive content, not only the link or summary, when the
   conclusion depends on it. Verify publication separately where the owner needs it;
   local object availability alone does not establish remote reachability.
4. Diagnose the current copy independently: exact HEAD, source presence and any
   difference from the pinned version and intended target revision. Missing files
   in an older checkout do not mean missing accepted inputs or revoked acceptance.
   Name **readable published input, stale checkout** when supported. Compare
   applicability against the intended integration target and related code/contracts;
   absence in the stale checkout alone is not a substantive design change. If target
   or material changes are unresolved, block only dependent applicability/writes,
   not reading or an independently supported direction. Do not repin accepted refs
   merely to match HEAD.
5. Keep reading, applicability and preparing/updating the working copy separate.
   A read-only owner never pulls, checks out, copies files into the tree or repairs
   the copy. An authorized writing owner obtains a suitable target copy through
   the existing preparation/publication owner before dependent writes. Return exact
   source/decision versions, checked target/checkout facts and only material gaps.

A completed saved/published stage must be consumable in a new session from project
and exact ID (or its document-only locator) using these saved associations, without
previous chat, local notes or a publication receipt. Producers check those links
and decisions at completion. Explicit candidate text/decision transfers remain
necessary between components for unsaved or not-yet-discoverable intermediate
results; that rule must not become a manual handoff requirement after completion.

## Feature documents, not a tracker registry

For a confirmed feature, new documents live at
`sources.specs/<full feature ID>/spec.md` (default specs root `docs/specs/`).
Use the checked configured root, never the skill installation or a fixed repository
path. The directory has no title/slug suffix and does not move on title changes.
Before writing check the exact ID, destination and existing associations/content;
conflicting identity is a conflict, not permission to overwrite or relocate.
Start new spec.md with a Markdown H1 readable feature name, followed by these
column-zero English labels (values/content use the project language):

```markdown
# Readable feature name
Feature-ID: <full feature ID>
Summary: <one-line summary>
Keywords: <optional comma-separated terms>
```

Omit Keywords when unnecessary. Requirements are in spec.md; sufficient design is
an independently selectable section there or adjacent design.md. Retain the
existing attributable acceptance convention: each complete requirements/design
scope has its actual content path/semantic section/version and separate decision;
one act may explicitly accept both. No new acceptance notation is imposed.
Resolve `containing-commit` from the original decision commit, using its immutable
link or bounded Git history inspection if needed; copied text never renews it.
Preserve original provenance and unchanged acceptance, not a latest-HEAD rebind.

For existing work follow explicit checked source links and legacy hints without
moving files or requiring the new header retrospectively. Missing old JSON or a
different old layout alone is not a readiness gap. A new session must reach actual
documents/decisions from project+ID via this convention or existing explicit links.
Beads holds ordinary goal/scope/criteria/status/dependencies, not duplicate accepted
refs, readiness or verification. No mandatory JSON/YAML/metadata/sidecar registry,
pin operation, bulk migration or product/functionality index is introduced.

Establish feature kind from explicit selected scope and actual record content/
source association, checking native type/relationships where relevant. JSON shape,
title, directory existence or child-parent membership alone cannot establish kind;
unknown kind remains a bounded gap, not an ordinary-task fallback. Document-only,
ordinary standalone and native bug subjects keep their own paths/contracts: never
invent a feature ID or force this directory/header on them. New feature AC links
use the full feature ID as qualifier (`<ID>#AC-nnn`); retain existing legacy links.
