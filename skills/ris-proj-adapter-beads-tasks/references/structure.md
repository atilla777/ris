# Membership and blocking edges

Read before structural mutations, with `concurrency.md` and main typed reads.
The caller supplies endpoints, scope, expected structure and authorization.

For optional `tasks.feature-dependencies.add|remove`, require a concrete approved
graph delta, both exact endpoint IDs/native task types, confirmed feature kinds
from scope/content/source associations (not membership alone), and exact epic
memberships. Both endpoints must belong to the approved same epic, or both epics
must be explicitly in approved cross-epic scope. No inferred neighbor authority.
Fresh-read both endpoints, content/reason, membership/status/ownership and typed
edges before each write; preserve started/accepted/foreign commitments. Require
explicit implementation result/reason supplied by the caller; requirements-only
and informational relationships cannot be converted to blocks. Check proposed
directed graph for cycles, including relevant external paths, retaining native
cycle checks below. Use the same bounded native blocks add/remove forms below,
but this optional contract is distinct from intra-feature `dependencies.add`.
For removal require exact current `blocks` type/direction and deletion authority;
the baseline remove command has no type-scoped CAS, so refuse ambiguity with a
different/replaced endpoint relation and disclose concurrent replacement limits.
Independently reread both endpoints, membership and exact typed edge after add/
remove. Scope drift is conflict with persisted effects, not success. A failure
stops further graph writes; reconcile before retry, never remove unrelated edges.

- **Composition:** `bd --sandbox create --parent <parent-id>` or `bd --sandbox update <child-id>
  --parent <parent-id>`; inspect the existing parent and child, check proposed
  ancestry for a cycle; refuse a closed parent or a child whose state makes
  the requested composition invalid. `bd` can add an open child to a closed
  parent, so its success is not a readiness check. Then verify the child's
  `parent`, the typed
  `parent-child` dependency (child → parent), and unlimited parent selection.
  Reparenting/removing membership (`--parent ''`) changes mandatory scope;
  require explicit permission, fresh expected structure and result checks.
  Do not substitute a `blocks` edge for membership or add both. A /2 root feature
  may receive a confirmed epic later only as a separately authorized composition
  operation; keep payload/refs/pins unchanged. Requirements update does not add it.
- **Blocking:** `bd --sandbox dep add <blocked-id> <blocker-id> --type blocks --json`;
  `bd --sandbox dep remove <blocked-id> <blocker-id>` only for an explicitly authorized
  edge removal. Check both IDs and existing typed edges. Confirm the dependent
  is blocked by the blocker after add; before remove freshly verify the exact
  expected edge and afterward its absence. This does not exclude an undetected
  concurrent replacement; report an unsupported stronger request. Keep the
  default cycle check: never pass `--no-cycle-check`. `bd` rejects cycles and
  ancestor-blocking descendants; re-read on failure. A repeated add may say
  `added`: confirm actual edge rather than infer a new change. For common
  `tasks.dependencies.add`, both endpoints must reread as `task` in the
  confirmed feature scope; refuse wrong type, unknown ID, cross-scope edge,
  cycle or an unexpected prior edge. An existing exact edge may be returned as
  unchanged after verification. Check membership and blockers again after add;
  concurrent membership change is `conflict` with the actual persisted edge,
  not `ok` for the requested scope. `bd` cycle checking does not provide a
  transaction over all concurrent graph changes; report this limit.
