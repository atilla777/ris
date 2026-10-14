# Conditional Langfuse evidence

Read only for a named episode or metric gap with an authorized source. The
wrapper owns the join, applicability and combined report; the portable base
interprets the supplied evidence. Do not start a recurring multi-session audit.

## Bound access before reading

1. Name the missing assertion, selected repository/service, exact session ID,
   relevant message/call IDs, stopped snapshot/cutoff, and permitted data scope.
   Supplied observations can be analyzed without network access. Distinguish
   their stated provenance from independently checked live correspondence.
2. Load installed `langfuse` and its applicable CLI reference before source
   interpretation/access. Consult current official documentation and, for a
   self-hosted service, its deployment-matching API schema. Record the actually
   available CLI/API versions and schema provenance; never invent a version or
   transplant another deployment's flags. An unavailable skill/auth/API/source
   leaves this branch partial; continue the independently useful local report.
3. For live access use only an already available authorized CLI, not an implicit
   `npx` download, install, credential setup or new SDK/plugin/server. Use its
   supported version/help/schema discovery to establish observation list and
   selected-detail operations, filters, field groups and pagination. Credentials
   stay in the existing private environment, never in arguments, excerpts or
   reports. Do not read auth files just to diagnose an unavailable capability.
4. Set a small explicit call/row/time ceiling fitting the episode before data
   reads. Request only identity, relevant metadata/usage/timing and necessary
   selected content; avoid full input/output unless the specific gap needs it.
   Scope observation queries to the exact session/known trace, service identity
   and episode time range. Use the discovered filter semantics: a general
   filter can override fixed parameters, so preserve all bounds in the effective
   query. Follow only the returned continuation within the same scope/budget;
   reaching a ceiling or missing cursor/field group is a coverage gap, not zero.
5. Use the version-supported observations read interface, not a guessed trace
   download. Current v2 uses cursor pagination and selective field groups; it
   has no separate get-by-ID route (a selected ID is a filtered observation read).
   A deployed older API may differ: discover it, do not silently migrate or widen
   the query. On identity conflict, missing permissions or unsupported scope stop
   this branch; do not scan all projects/days looking for similar content.

No ingestion, score, feedback, experiment, prompt/config update or telemetry
creation is permitted. Network availability and a syntactically correct query
do not establish correspondence or complete coverage.

## Establish two different relations

Maintain addressed observations with deployment/project, repository/service
binding, exact session, trace/observation ID, observed version/time, event link,
granularity, metric semantics, and gaps. A matching session ID without the
repository/service binding is insufficient. Generation `messageID` and tool
`callID` are usable only where the source schema/integration actually supplies
them. Never join by title, text similarity, ordering or timestamp proximity.
Unmatched/foreign/ambiguous records remain separate evidence with that limit.

**Observation-to-message is not observation-to-request.** A messageID alone
cannot bind an observation to an OpenCode step-finish. Before supplementing an
unknown local request, require an explicit step/request identifier or a verified
integration contract proving exactly one request, plus compatible field units,
cache semantics, version and cutoff. Record that proof. With two steps, partial
local usage and several observations on one message, leave local usage unknown
at those steps: do not distribute, add, infer a peak or silently fill cache zeros.
An independently proven Langfuse request can have its own source-specific peak
and limited coverage without pretending it is joined to a local step.

Deduplicate repeated delivery by deployment/project + trace/observation ID.
Identical deliveries count once. Different values/versions of one ID remain
addressed conflicts, never a sum, average or silently chosen winner. Different
observation IDs on the same message are not automatically duplicates; establish
their granularity before any arithmetic. Count a compatible one-to-one request
once across sources, retaining both provenance readings. Conflicting readings
do not become a certain peak/sum; preserve conflicting threshold signals for
investigation, separately from an established exceedance.

For the inspected OpenCode plugin 0.4.0, cache values repeat local OpenCode usage,
not independent measurements; its fallback total excludes cache and is not an
input-context peak. This is an integration-specific fact, not every plugin's
contract. Apply the base's metrics method to known semantics only; aggregates,
output/reasoning and multistep message usage do not become request context.
Generation elapsed is not thinking time. Do not add parent waits and parallel
child intervals twice or bring late telemetry into an exact historical cutoff.

## Return to composition

Return only safe source addresses, matched/unmatched/conflicting identities,
request-mapping proof where available, bounded coverage, known readings and
limitations. Re-read key selected observations before relying on a finding.
Absent records may reflect delayed ingestion, permissions, missing fields or
partial pagination, not absence of the underlying action. Keep local findings
useful and separate from telemetry-dependent hypotheses. Explicitly mark live
identity correspondence unverified when only supplied fixtures were available.

Authoring references (consult current/deployment docs at execution):
[CLI](https://langfuse.com/docs/api-and-data-platform/features/cli),
[Public API and observations v2](https://langfuse.com/docs/api-and-data-platform/features/public-api#v2).
The CLI package is now documented as `@langfuse/cli`, with legacy
`langfuse-cli` maintained alongside it until a new major; both use `langfuse`.
This resource neither pins an unobserved binary version nor authorizes migration.
