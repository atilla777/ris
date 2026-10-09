---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. By default, ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

When the caller explicitly requests **one-question-at-a-time mode** (as `/grillme` does), keep mapping the entire frontier but present exactly one decision question per message. Offer distinct answer options numbered `1`, `2`, etc. wherever discrete choices make sense; make `1` your recommended answer and explain why. Allow a reply containing just the number, but also accept a custom answer or a qualified choice. Wait for the user's answer, update the tree and frontier, and ask the next unblocked question in a new message. Do not combine dependent questions, and do not silently drop other frontier decisions. If an open-ended question has no honest discrete options, ask it directly rather than inventing a meaningless menu.

In the default mode, format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Word each question so "yes" accepts your recommended answer.

In one-question-at-a-time mode, use a single question with a numbered menu, for example:

```
❓ **<question title>**: <question body>

1. <recommended answer> — <brief reason> (recommended)
2. <alternative answer> — <meaningful tradeoff>
```

Treat `1` or "yes" as acceptance of the recommendation when applicable. Reset the option numbers for each new question; never number a question and its options with the same series.

Each answer reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier before asking further questions. A question whose answer depends on another unsettled question belongs to a _later_ turn or round, not the current one.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), dispatch a sub-agent to find it; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; ask the rest of the frontier now. The _decisions_ are the user's: put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.
