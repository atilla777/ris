---
description: Execute or safely resume one ready RIS task through implementation, independent review, Git publication and separate tracker completion/publication.
---

Load `ris-execute-task` with the skill tool and follow it for one task in the
current RIS project. Treat the following as the user's request, including any
exact task ID, actor, scope or other context:

$ARGUMENTS

With an explicit task ID, work only on that target. Without an ID, let the skill
reconcile confirmed own unfinished work first, otherwise select one ready task
using its ordering and readiness rules. For prior or partial effects, follow
the skill's recovery route rather than restarting completed operations.

Treat invocation as a request for the full single-task cycle under the skill's
permission contract; establish actual permissions and applicable project limits
before effects. Keep human decisions in the leading dialogue and launch the
configured executors as required by the skill.

Stop after the selected task's verified result or a concrete blocker. Report the
next recommendation without claiming or starting another task.
