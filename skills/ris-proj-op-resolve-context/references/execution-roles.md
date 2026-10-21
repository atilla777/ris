# Requested execution role

Read only when the calling operation requires an execution role. Whole-config
schema validation remains in `configuration.md`, even when no role is used.

`execution.roles` selects the executor when a caller delegates an operation;
it does not require delegating every internal step. A lead may apply an owner
directly within its authorized scope, except required independent review.
For a requested delegation, return the configured `agent` and its provenance.
An absent role blocks that dependent delegated route; name the missing role,
without silently substituting the current agent or another model. Choosing
authorized direct work is an explicit caller decision, not a disguised fallback.
A present record without a valid `agent` is an `error` for the selected config,
even when another operation is requested. Direct work needs no unused role;
absence of `execution` is valid for it, without claiming isolation or a model tier.

A role record alone proves neither a particular model, actual invocation,
independence nor use of Advanced for implementation. The caller checks host
availability/permissions and actual launch of the configured executor before
relying on delegated results. Required independent review must actually launch
separately from every author/repairer, even when they share an agent name/model.
Do not launch agents, select a fallback, switch models, rewrite bindings or run
a skill as part of context preparation. This field grants no write permission.
