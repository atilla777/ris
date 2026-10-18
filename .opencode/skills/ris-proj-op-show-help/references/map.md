# Default view

Return only this fenced view on empty input, localizing descriptive labels under
SKILL.md without changing identifiers, routes or the 80x24 bound. This packaged
baseline is ASCII; headings and legend are inside the measured view. Cards and
routes are conditional. Translated renderings have not been pre-verified.

```text
RIS SDLC -- routes, not an obligatory checklist
p:name = /risp-name; b:name = /risb-name
* = direct skill call (exact names/examples: ask /ris-help <label>)
Choose a scenario OR its atomic operations; do not run both.
Idea/goal -> p:roadmap -> epic (p:refine-epic if unclear)
+-- p:prepare-feature ------------------------------------------+
| p:select-feature -> requirements: p:specify-feature             |
| -> explained, separately accepted design: p:design-feature     |
| -> reviewed/published inputs + published feature ID            |
+---------------------------------------------------------------+
  -> p:decompose-feature -> one task or children with blockers
+-- p:run-task -------------------------------------------------+
| prep-copy* -> p:plan-task -> implement/check* (+ docs*)          |
| -> independent p:review-task -> p:publish-task (Git)             |
| -> exact task completion* -> tracker publication*              |
+---------------------------------------------------------------+
Simple assigned change -> p:run-simple-task (own branch, checks,
  independent review, Git; separate tracked completion/publish)
Bug -> register-bug* -> investigate-bug* -> fix-bug*
  fix-bug* admits saved inputs, then REUSES p:run-task above
Container acceptance/close: separately p:complete-container
  verify is read-only; administrative close is NOT acceptance
Actual continuation: p:next <ID>; actual plan: p:status [ID]
Other init/product/install/rules/OKF/skills/retro: /ris-help <topic>
```
