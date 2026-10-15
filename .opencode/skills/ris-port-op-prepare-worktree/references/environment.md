# Authorized environment preparation

Read when setup or creation hooks are requested/required, before dependent writes.
The base owns the combined environment verdict; the selected adapter inspects and
reports tool-specific hooks/effects. Do not invent a config format or setup runner.

1. Obtain each exact command/hook/copy action, working directory, prerequisites,
   allowed writes/resources, expected result, success/readiness check and retry
   policy. Inspect available project scripts and effective hooks, including Git
   `post-checkout`, before running them. Tool availability or ignored files do not
   grant permission. Required but unobservable/uncontrolled actions block readiness.
2. Resolve real source/destination paths and symlink ancestry. Copy only an explicit
   allowlist of files whose contents/types are inspectable and destination is absent;
   no overwrite, broad recursive copy, implicit glob expansion or “all ignored”.
   Reject shared mutable tracker databases, primary-copy shared notes, nested
   worktrees, Git metadata and other shared resources as independent environment
   copies. Their names/layout are project inputs, not a requirement to use RIS.
   Stop on escaped targets, existing destination or uncertain selected contents.
3. Record pre-state of protected existing data and the authorized output set.
   Execute only permitted actions in the verified copy, checking actual outputs,
   return codes and preservation of files/resources outside scope. Commands must
   have understood side effects; an allowlist is not a sandbox. Do not authorize
   an opaque install script by observing its exit code after it has run.
4. Foreground completion needs observed exit and output checks. For background
   jobs require observable completion/exit or an approved service readiness signal
   bound to the started instance (not an old PID/log/port). Merely returning a PID,
   launching a shell job or successful worktree creation is unverified. Do not
   start a job with no authorized lifecycle/observation method. Do not silently
   kill it as rollback. Report any remaining process and how to observe/resume it.
5. On failure retain created copy and completed actions. Before retry, inspect
   current copy/ownership evidence and every previous action's outputs/processes.
   A previously copied file may be accepted as a completed effect only if current
   bytes/type match the approved source/evidence; a conflicting destination is
   not overwritten. Skip proved complete actions, rerun only authorized safe
   actions, and ask for the bounded retry decision for non-idempotent/unknown ones.

Report per-action effects and evidence, failures/pending processes and independent
copy/environment verdicts. Worktrees share repository refs/objects/config and
may share tracker, services and notes; they do not isolate those resources.
