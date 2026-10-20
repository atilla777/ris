# Discover and read saved project inputs

Read when a result depends on previously saved requirements, design, decisions
or other linked project evidence. The calling owner selects the material sources,
checks their substantive sufficiency/applicability and owns its result. This is
source discovery/reading, not copy preparation, publication or content acceptance.

1. Start from the selected project and exact tracker ID through its selected
   adapter, or an explicit document-only locator. Follow saved source/decision
   links and the project's checked path conventions. For a current feature use
   its permanent slug/spec association and reference objects under the adapter's
   record contract; a mutable title is not an identity key. Preserve unsupported,
   historical or malformed payload diagnostics, never infer acceptance or migrate
   them. Missing source links need bounded discovery through actual associations,
   not a second registry, arbitrary receipts or guessed title-derived paths.
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
