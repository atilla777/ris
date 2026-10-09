---
description: Stress-test a plan, decision, or idea one numbered question at a time.
---

Load the `grilling` skill with the skill tool and follow its instructions to interview the user about this plan, decision, or idea:

$ARGUMENTS

Use the skill's one-question-at-a-time mode for this command. Ask exactly one decision question per message; give numbered answer options with option 1 as your recommendation whenever discrete choices make sense, so the user can reply with just a number. Wait for the answer before asking the next question. Keep tracking the full decision frontier internally and preserve the skill's research, dependencies, and final shared-understanding confirmation.

If no topic was provided, ask the user what they want to grill.
