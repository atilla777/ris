# Dialogue rules

Use before asking the user questions or discussing decisions. This resource
does not initiate an interview or define which subject the calling skill covers.

Read available sources and previous answers first. Investigate facts available
in the code, documents, or environment yourself instead of asking the user;
do not repeat answered questions without a material new reason. Distinguish
missing information from conflicting sources, and explain which decision or
part of the work they affect. Ask the user for decisions that materially affect
the goal, scope, permissions, or result. Continue independent work if a gap can
be stated as a nonblocking assumption; do not guess a critical decision.

Ask **one user decision question at a time** and wait for the answer before
choosing the next, even when questions are independent. Ask dependent questions
only after their premises are resolved. This default applies to all RIS work
using `ris-common`, not only to formal interviews. If the user explicitly asks
for multiple questions together, honor that request while preserving the
dependency order. When several methodologies need answers, coordinate one
conversation rather than repeating interviews.

Before each decision question, briefly explain its context and the consequences
of choosing, in plain language. Adapt the detail to the person's familiarity;
explain necessary specialist terms the first time you use them. When answers
genuinely differ and a recommendation can be justified, offer concise,
meaningful choices and leave room for an answer in the user's own words. In
every such set of choices, put **exactly one recommended choice first** and
briefly explain why it fits the known goal and constraints. Order the remaining
choices from more to less suitable when evidence supports that comparison;
otherwise their order is arbitrary. Do not invent a recommendation for a
factual or open-ended question, or force such a question into an artificial
menu: ask it openly instead. If the host provides a suitable choice form, put
the recommended choice first there too; otherwise number the choices so the
user can respond with one digit. Do not use a form when it would hide important
distinctions or prevent a needed free-form answer.

In a continuing dialogue, make the transition easy to scan: mark a confirmed
previous answer as **✅ Confirmed:** and the next question as **❓ Question:**.
Mark the first menu choice as recommended, with its short reason (for example,
**💡 Recommended:**); do not mark a proposal, assumption, disputed or deferred
answer as confirmed. Use labels in the conversation's language and keep the
format lightweight; do not restate the entire history before every question.

Separate recommendations from accepted decisions. Agreement with one proposal
does not approve other proposals. Record material decisions, open questions,
and assumptions in the calling skill's designated result when writing is
permitted; do not invent a separate dialogue log or write outside the allowed
area. Finish the discussion when the current task's criteria are met, rather
than exploring every possible future product decision.
