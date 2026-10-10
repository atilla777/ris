---
description: Create or improve an Agent Skill source folder using the appropriate author.
---

For an autonomous skill (even in a RIS project), load `ris-author-skills-base`
with the skill tool and follow it directly, without loading RIS-only rules or
context. For a RIS package skill or a project skill whose operation integrates
with RIS, load `ris-author-skills` and follow it. Classify by the requested
skill's actual responsibility; if unclear, clarify before choosing. Pass the
request through unchanged:

$ARGUMENTS

If the request is empty, ask what skill the user wants to create or improve.
