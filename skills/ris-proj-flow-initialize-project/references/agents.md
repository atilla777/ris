# Executor availability and agreed project agents

Read only for unresolved role suitability/availability or proposed project
definitions. Inspect the host's actual discoverable agents, launch permissions,
capabilities and current project definitions/settings; reuse suitable available
agents first. An identifier in YAML or an agent file is not a working executor.
Do not silently choose a fallback or make the leader perform a blocked child step.

If definitions are needed, consult the installed host's current official OpenCode
agent/config documentation before writing syntax. For V2 the official agent guide
is https://opencode.ai/v2/docs/agents; project Markdown definitions live in
`.opencode/agents/<name>.md`. Do not infer schema from deprecated fields or copy
a model/rights template from the RIS author's machine.

Agree the exact minimal project definition/content, name/mode, model **or explicit
inheritance**, permission policy (including inherited effective rights), target
and intended operation. Preserve existing definitions and unrelated settings;
no global edits, broad rights escalation or provider credentials. Only write the
agreed delta using bootstrap's baseline/path/read-back guards. Model omission in
V2 subagents inherits the parent model: that must be an explicit choice, not an
accident. A reusable role describes work, not a model tier or isolation guarantee.

Refresh host discovery/restart if necessary, then inspect actual availability and
permissions. Do not claim readiness from file presence; missing refresh/access
blocks the dependent operation. Each required standalone operation must still
actually launch and return a checked receipt. Independent review uses a fresh
invocation separate from every author/fixer, even when all use the same agent ID.
Do not create an agent test session just to prove discovery.
