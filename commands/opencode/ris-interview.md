---
description: Interview about a bounded topic using ris-interview-base.
---

Load `ris-interview-base` with the skill tool and follow it to interview
about the user's bounded topic. Treat the following as the user's request,
including the topic, boundaries, intended result and any supplied context:

$ARGUMENTS

If no topic is identified, ask which topic the user wants to discuss.
Use the skill's full mode by default; limited mode requires an explicit request
and a sufficiency criterion. Return the skill's interview handoff in the response
and stop, without writing files, creating tasks or starting another stage by default.
