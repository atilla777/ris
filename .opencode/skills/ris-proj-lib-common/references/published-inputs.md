# Discover and read saved project inputs

Read when a result depends on previously saved requirements, design, decisions
or other linked project evidence. The calling owner selects the material sources,
checks their substantive sufficiency/applicability and owns its result. This is
source discovery/reading, not copy preparation, publication or content acceptance.

## Sufficient requirements/design basis

For requirements and design, **accepted inputs/results** mean a sufficient
direct, inherited or mixed basis, not necessarily a new human decision for each
result. Keep the two complete content scopes and versions independently selectable.
For each material part distinguish:

- **Directly accepted:** read the actual attributable decision for its exact
  content scope/version under the owning acceptance protocol.
- **Inherited:** read the exact applicable accepted sources and their original
  decisions, then check that the material content actually follows from them.
  Explain that derivation and applicability in the substantive requirements/design
  scope using precise source/decision locators. Compatibility or absence of conflict
  is insufficient: materially different allowed choices require a human decision.
- **New/disputed:** obtain an authorized attributable decision only for those
  material choices, in the context of the complete identified candidate. A mixed
  result preserves inherited provenance alongside that bounded decision. One act
  can decide new parts of both independently identified requirements/design scopes.

A wholly inherited result needs no new approval, fictional acceptor or synthetic
`decision: accepted`. Sources must themselves have a checked accepted basis; follow
their derivation to actual original decisions as needed, without treating circular
references, publication or an author's assertion as authority. Check content,
source version, original acceptance and applicability to the intended target.
Missing, stale-inapplicable, conflicting or ambiguous evidence blocks only the
dependent scope; a stale checkout alone is not stale source authority (step 4).
Reviewer verifies derivation, never chooses new behavior for the human. Publisher,
execution, verification and navigation consume the same basis and retain their
own action/check/review gates.

Preserve existing direct decisions and original immutable addresses, including
`containing-commit`; unchanged applicable content is neither reaccepted nor
repinned. A changed result needs a fresh basis assessment, not automatically a
new approval if its changed material is demonstrably inherited. No new schema,
sidecar, registry or full assertion table is required; use substantive text and
existing links. Old sufficient inputs need no marker or migration. This does not
change Fast admission, versioned bug-history retrieval or review serialization.
Below, separate decisions are checked **where direct acceptance is used**; for
inherited parts check the original source decisions and derivation instead.

## Discover exact sources and assess applicability

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

Consumers reuse already read exact content in the same context; they do not
repeat source discovery merely for an internal boundary. After context loss,
recover only missing facts through these sources and their owners. A lost
acceptance decision is sought at its original address; if unavailable, return
only that missing material scope for a new human decision with actual provenance,
not a fabricated historical acceptance or reacceptance of unchanged known scopes.
For versioned bug inputs the adapter owns complete historical retrieval and
short-locator reconciliation; this reading method does not copy that algorithm.
For lost checks/review and confirmed publication/closure use artifacts' recovery
rules and the affected owner. Reading a source does not prove any of those effects.

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
an independently selectable section there or adjacent design.md. Each complete
requirements/design scope has its actual path/semantic section/version and the
sufficient basis above. Retain actual separate decisions for direct acceptance;
one act may explicitly decide new material in both scopes. No new acceptance
notation is imposed.
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
