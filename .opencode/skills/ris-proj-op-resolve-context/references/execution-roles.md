# Requested execution role

Read only when the calling operation requires an execution role. Whole-config
schema validation remains in `configuration.md`, even when no role is used.

For a caller requiring an isolated role, return the configured `agent` with
its provenance if present. If the role is absent, report `blocked` for that
dependent step and name the missing role; do not silently run it in the
current agent. A present record without a valid `agent` is an `error` for the
selected config, even when another operation is requested. For a direct
operation that does not require a role, absence of `execution` is valid:
prepare its other settings without claiming isolation or a model tier.
Merely reading `agent` cannot establish that the project-provided subagent
exists, can run in this environment, has a particular model, or has been
invoked. The caller checks availability and actual launch before relying on
isolation. Do not launch agents, select a fallback, switch models, or run a
skill as part of context preparation. This field grants no write permission.
