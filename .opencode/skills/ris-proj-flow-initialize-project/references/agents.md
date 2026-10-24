# Executor availability and agreed project agents

Read on every initialization, including a repeated call with apparently complete
settings. Own only init's agent reconnaissance, agreement, bootstrap delta and
readiness checks; do not execute another RIS workflow or alter context's schema.

## Inspect project definitions and effective configuration

Inspect `standard` and `advanced` in the selected project's actual OpenCode files
AND host discovery for that project/location. Inspect applicable merged/global/
ancestor/managed settings read-only as necessary to explain effective overrides,
permissions and launch restrictions. An identifier in YAML or a visible agent
file is not a working executor; global-only definitions are not project setup.

Consult the installed host's current official documentation before writing syntax:
V2 https://opencode.ai/v2/docs/agents, https://opencode.ai/v2/docs/config and
https://opencode.ai/v2/docs/models. Reuse a suitable existing project definition
in place. New definitions may use `.opencode/agents/<name>.md` or the native V2
`agents` entries of an agreed project `opencode.json(c)` or
`.opencode/opencode.json(c)`; preserve the project's format/comments and unrelated
settings. Do not introduce duplicate competing definitions, deprecated syntax or
a template copied from the RIS author's machine.

For each tier require a project-owned explicit `provider/model` selector (and
optional catalog-verified `#variant`), a subagent-capable mode (`subagent` for new
definitions; preserve suitable `all`) and effective permissions suitable for its
agreed work. A subagent's omitted model inherits the parent's model in V2;
explicit inheritance is NOT sufficient for these two tiers. Other separately
agreed agent definitions may still use explicit inheritance. Do not change
visibility silently: `hidden` affects the subagent catalog, not authorization;
for hidden agents use exact-ID host inspection and verify the caller can address
them without a test launch. Unknown availability remains unverified.

## Recommend and agree models, without fixed package versions

Reuse applicable saved model choices and suitable project settings first, showing
their current check results in the one settings proposal. Do not ask again merely
because the provider has a newer model. Ask only for missing choices or a material
change/conflict, including moving an existing global-only setup into the project.

Read the host's current model catalog for the **target location**, enabled models,
available providers and advertised capabilities/variants. Do not guess IDs from
names/version numbers, assume a connected provider from another project, or treat
a public model list as proof of project access. A catalog entry does not prove a
successful authenticated request; report that limit without issuing a test call.
If discovery is unavailable, request the person's available catalog/selection or
defer the dependent check; never invent a recommendation as "current".

Offer a concise choice for each tier with exact IDs, catalog source/date, reasons
and known limits: Standard prioritizes adequate tool/coding capability and
cost/latency for selection, decomposition and orchestration; Advanced prioritizes
capability for requirements/design, implementation and independent review.
Use available metadata and applicable observations, not unsupported benchmark or
speed claims. Prefer current suitable supported models, not simply the highest
version number. Explain cost/capability tradeoffs when known; missing price data
stays unknown. No provider/family/version is a permanent RIS default. The person
may choose other available suitable models, including the same model for both
tiers; independence comes from a fresh review invocation, not model diversity.

Agree exact project paths/definitions, models, mode, visibility, permission policy
(including inherited effective rights) and role deltas as part of the single
settings/change set. Show the recommended choice, ask which models the person
wants only when not already decided, and carry the answer to bootstrap. No silent
model upgrade, model omission, fallback, broad rights escalation, credential
write, provider connection or global configuration edit.

## Bind roles and bootstrap only the agreed delta

Propose these six working-cycle bindings in `ris.yaml`:

| RIS role | Agent |
| --- | --- |
| `task-decomposition` | `standard` |
| `task-execution` | `standard` |
| `container-completion` | `standard` |
| `feature-preparation` | `advanced` |
| `task-implementation` | `advanced` |
| `task-review` | `advanced` |

Optional delegated preliminary feature-graph proposals reuse `task-decomposition`;
direct planning needs no role. Existing-work navigation does not need a selector role.
`container-completion` runs the execution flows' bounded ancestor-closure tail
in fresh context; it is not substantive feature verification or a third model tier.
Existing projects agree this added binding before using the delegated tail;
missing roles have no silent fallback. No `simple` agent or model change is implied.

Models live in the OpenCode definitions, never as invented model fields in
`execution.roles`. Preserve unrelated roles/options. For existing different
bindings, explain and agree the specific migration or retain the explicitly
agreed alternative with its rationale; do not silently normalize it. Agree
`project-initialization` separately using the main skill's contract (normally
propose `advanced` for document work). A tier name describes an executor profile,
not a new semantic role or isolation guarantee.

These bindings select executors for delegation, not a separate agent for every
internal step. The lead may apply authorized owners directly; only required
independent review must launch separately from all authors/repairers. A saved
role proves neither model, launch, independence nor Advanced implementation.
When delegating use the configured role and verify the actual invocation; an
unavailable role blocks that delegated route, without a silent model/agent switch.

The leading scenario can bootstrap definitions before an executor exists, using
the main skill's baseline/physical-path/freshness/read-back guards. Save only the
agreed delta. Record accepted model IDs/variants, definition paths, role bindings,
catalog provenance and material deferrals in the already agreed settings-decision
document; do not create another mandatory registry or ledger.

## Recheck and report the actual limits

Read back both project definitions, parse saved configuration, freshly apply RIS
context and compare every agreed role mapping. Refresh discovery if needed under
the host's supported procedure; seek appropriate authority for a disruptive
reload/restart rather than cancelling other sessions silently. Inspect effective
agent IDs, subagent mode, model/variant, provider/model availability and effective
child AND caller launch permissions for the selected project/location. Compare
against the agreed project definitions; higher-precedence overrides, disabled or
missing models, inheritance or launch restrictions block the dependent readiness
claim. Do not work around them by editing global settings or switching models.

If the person declines/defers a definition, pinned model, migration or refresh,
preserve useful work and name exactly what remains missing/unverified and which
operations are limited. A global-only definition can be available now but does
not satisfy project-owned tier setup. A deliberately retained alternative role
mapping is not the standard mapping; report its actual checked scope. Never call
the full working cycle ready from files alone or while tier gaps remain.

Each delegated operation must actually launch the configured executor and return a
checked result; direct work also needs its owner's checks. Independent review uses
a fresh invocation separate from every author/fixer, even when both use `advanced`.
Do not create an agent test session
or model request just to prove discovery, permissions or model reliability.
