# Read-only plan overview on Beads 1.3.1

Read before serving the Beads-specific plan-overview capability. This is separate
from task-only `tasks` v1 and `tasks.feature-record/1`; it changes no mutation
contract. The caller owns working-set interpretation, tree, candidate selection
and recommendation. Return checked data, coverage and field-level unknowns.
Apply the main skill's selected-workspace, exit/body and bounded-read rules.
Use `bd --readonly` for every route. No initialization, claim, heartbeat, repair,
configuration, report saving, pull/push or installation is part of this capability.

## Routes and completeness

Advertise these requested operations before dependent overview reads:

| Operation | Native route in the selected project | Guarantee after validation |
| --- | --- | --- |
| Project inventory, all types and statuses | `bd --readonly list --all --limit 0 --max-rows 0 --include-gates --include-ephemeral --include-infra --include-templates --brief --json` | Complete unfiltered candidate set, including normally hidden categories and closed context, or explicit incompleteness |
| Exact actual-type/content read | `bd --readonly show <ID> --brief-deps --json` | Exactly one exact ID; report actual native type, own content and available row fields, without an expected-type filter |
| Complete direct children, any native type | `bd --readonly list --parent <ID> --all --limit 0 --max-rows 0 --include-gates --include-ephemeral --include-infra --include-templates --brief --json` | All direct children including closed/hidden categories, or explicit incompleteness; validate actual membership |
| Parent membership when needed | `bd --readonly dep list <ID> --type parent-child --direction=down --json` | Queried child → parent, separately from blocks |
| Direct blocking prerequisites | `bd --readonly dep list <ID> --type blocks --direction=down --json` | Queried blocked ID → prerequisite; use exact endpoint reads when status/content is needed |

No `--type` filter, `--ready`, `--no-parent`, open-only filter, default 50 limit
or CLI tree rendering substitutes for these inventory routes. `--max-rows 0`
disables an ambient `BEADS_MAX_ROWS` ceiling; it does not cure host truncation.
Use only flags supported by the actual installed version/help. If an inclusion
category or required structure is unsupported, report which coverage is unknown;
do not quietly fall back to task/epic/bug-only or call a partial set complete.
An exact-ID overview recursively uses the child route, not a mandatory project
inventory. Ancestors and external blockers use exact reads, not their independent
subtrees. Bound traversal by visited IDs and diagnose cycles.

Check exit code, parse the entire JSON body as an array, validate unique nonempty
IDs and actual type/status/parent fields and requested scope. Duplicate IDs with
conflicting rows, missing endpoints or unknown edge shapes are diagnostics, not
an invitation to discard rows. A successful empty array means empty only for
that checked selection. Recover host-truncated output through the host's saved
output reader or supported bounded reads; until fully inspected, mark incomplete.

## Working categories and row disclosure

The inclusion flags deliberately expose both work and potentially non-work rows.
Keep epic, task, bug, feature, chore, decision, gate, convoy, molecule and any other
encountered working types, including ephemeral work. Exclude a row from the work
tree only on inspected evidence that it is infrastructure (e.g. agent/role/message)
or a template rather than an instance of work. A name, unfamiliar type, ephemeral
storage or parent position alone is not exclusion evidence. If the brief row
does not disclose the needed category/template marker, exact-read that ID and
the necessary native fields (use supported `show --long` if needed). Unresolved
rows remain visible with a classification diagnostic and a coverage limitation;
report proven exclusions compactly without dumping infrastructure prose.

Brief rows omit free-form content and may omit parent/spec or other fields. Omitted
means unknown, not empty. Fetch only fields necessary for membership, required
row attributes, feature interpretation or the caller's one recommendation question:
use exact own-content reads and typed edges above. Counts alone prove neither
membership nor absence of blocks. Reconcile `parent` with typed membership if
missing or conflicting; never infer it from dotted IDs. For blocks normalize main
skill's supported edge shapes using the queried endpoint and direction. Retain
cross-branch edges. Only a checked closed prerequisite is inactive; unknown
status remains an unknown blocker, not ready.

Preserve raw status/priority, assignee, start time and due date when available.
Distinguish a checked absent optional value from an undisclosed value. Validate
the direct child set before returning a precise closed/all counter; do not use
descendant totals or cached counts as its denominator. Include closed rows in
the data even when the caller suppresses them in presentation.

## Feature interpretation without an acceptance audit

Native `feature`, native `task` under an epic, title or a spec link alone does not
establish RIS feature kind. When feature interpretation is needed, read the own
description/identity and apply this adapter's installed `references/feature-record.md`
for current markers/schema and historical/malformed diagnostics. Its reading and
classification rules apply; do not activate its writes or require every linked
acceptance document merely to draw the tree. Potential feature records must have
their relevant content disclosed; missing brief description cannot prove ordinary
kind. A current structural payload is still only a reference, not confirmed
content acceptance. Historical/malformed feature data stays visible as such and
never silently selects ordinary kind or migration. Return references as unverified
unless the specific version and independent decision were actually checked for
the caller's bounded question.

## Result limits

Return project/scope, actual rows and separately normalized membership/blocks,
proven exclusions, complete versus incomplete selections and unknown fields.
Failure of one read retains independently checked rows with the exact gap. These
are non-transactional observations, not a graph freeze or acceptance/readiness
certificate. Fresh rereads of a chosen candidate and material edges are supported;
the caller owns revising its conclusion after changes. Never choose next work or
write anything as part of this capability.
