# ris-e26 — политика совместимости feature-record

## Отдельно принятое решение — 19.10.2026

Пользователь RIS в диалоге задачи `ris-e26` явно принял: поддерживается только
текущая структура; backward compatibility и миграционная capability не нужны;
прежние записи остаются неизменённой историей. AC-3 реализуется **точным отказом
без записи**, а не успешной миграцией. Следующее несовместимое изменение получает
отличимый идентификатор версии. Сейчас `/1` не перенумеровывается, двухсхемный API
не вводится. Эта запись атрибутирует переданное исполнителю решение пользователя,
не является самостоятельным одобрением реализации или новой приёмкой старых фич.

Для exact historical ID отказ возвращает `blocked`, `historical/unsupported`,
запрошенную зависимую операцию, наблюдаемые несовместимые поля, неизменённые данные
и `changes: []`; проверенные identity/source/decision факты отделяются от
непроверенных. Digests не превращаются в Git refs/принятия. Повтор перечитывает
actual record, а не повторяет замену. Read/status/retry/update не преобразуют
данные. Сохраняются original/history/foreign prose и прежние pins/acceptance.
Разрешение на conversion не создаёт отсутствующую capability.

Отдельно явно разрешённый административный status-only close сохраняется:
exact subject/authority/native children/blocker guards, без мутации description,
refs или verification и без независимой приёмки. Это не обход verified completion.
Production data migration, переприёмка и перепривязка исторических решений исключены.

## Наблюдаемые варианты, не определяемые одним `/1`

Read-only инвентаризация 19.10.2026 на Git
`064de3d0ff091e47c7668b7e1bf845924a79da1d`, Beads 1.3.1: полная all-status
выборка native tasks (98) и точные полные descriptions кандидатов.

| Форма | Различимые признаки и наблюдаемые ID | Результат текущего контракта |
|---|---|---|
| Прежняя `/1` | `scope`, `sha256`, top-level `history`, digest-based verification; `ris-p20.2`, `ris-p20.3` | historical/unsupported, данные неизменны, зависимые операции blocked |
| Текущая `/1` | Ровно `schema, slug, spec_path, requirements, design, verification`; refs `{path, revision, section, acceptance:{address,decision}}`; `ris-1wa.1`, `ris-qv1.1`, `ris-01r.1`, `ris-01r.2` | Структура поддерживается; это не новая проверка refs/evidence или приёмка |
| Duplicate/malformed/unknown | В шести blocks не обнаружены; 92 task descriptions без блока, включая три прозаических упоминания | Duplicate/malformed — conflict; unknown/отсутствующий у установленной feature блок — unsupported. Отсутствие блока не устанавливает ordinary kind |

Обе формы используют те же literal begin/end markers и schema `ris.feature-record/1`.
Исторический producer подтверждён в
`183f1fb57d69636a7832225645d3c4757290140a:skills/ris-beads-adapter/references/feature-record.md`;
переход на Git refs — в `e386a8559bd0bc95d22bec3edddd6f7d61b5ad1a` по тому же пути.
Это локально прочитанная история, не повторная проверка remote reachability.
Исходные принятия `ris-km5` и `ris-bf4`, включая прежний AC-004, остаются связаны
со своими ревизиями. Их спецификации не переписываются как сегодняшнее решение.

## Producer/consumer inventory

Пути ниже относительно `skills/`; все поставляемые ресурсы зеркалируются в
`.opencode/skills/`. Это инвентаризация инструкций, не исполняемый parser.

| Владелец и ресурсы | Операция / граница |
|---|---|
| `ris-proj-adapter-beads-tasks/SKILL.md`, `references/{feature-record,create,update,concurrency}.md` | Capability, единственный current encoding, classifier, initial create/reuse, update/verification/retry. Исторические коллизии не разрешают overwrite/recreate |
| Тот же адаптер: `references/{completion,standalone,plan-overview}.md` | Verified complete, kind boundaries, status diagnostics и отдельный status-only close без payload mutation |
| `ris-proj-op-specify-feature/SKILL.md` | Producer initial current block только с опубликованными принятыми refs; historical блокирует запись |
| `ris-proj-op-design-feature/SKILL.md`, `references/acceptance-and-save.md` | Producer design update; requirements pins/проза сохраняются; historical не мигрирует |
| `ris-proj-flow-prepare-feature/SKILL.md` | Orchestration опубликованных refs; существующий ID не разрешает create/rewrite |
| `ris-proj-op-decompose-feature/SKILL.md` | Current accepted refs до создания детей; historical blocked, guessed block запрещён |
| `ris-proj-op-plan-task/SKILL.md`, `ris-proj-op-implement-task-tdd/SKILL.md`, `ris-proj-flow-execute-task/SKILL.md`, его `references/{evidence,text-work}.md` | Feature-linked planning/execution потребляют adapter refs; unsupported не понижается до ordinary |
| `ris-proj-flow-execute-simple-task/references/tracker.md` | Fast admission не обходит настоящий kind/feature prerequisites |
| `ris-port-op-verify-feature/SKILL.md` | Потребляет immutable accepted refs, не Beads encoding; digest-only вход не становится current acceptance |
| `ris-proj-op-complete-container/SKILL.md`, `references/{epic,standalone}.md` | Строгая feature verification/complete и отдельный административный intent; не вводит второй encoding |
| `ris-proj-op-show-plan/SKILL.md`, `ris-proj-op-suggest-continuation/SKILL.md` | Read/status/next показывают диагностику, не мигрируют и не переопределяют kind |
| `ris-proj-op-update-documentation/SKILL.md` | Сохраняет feature/ordinary boundary |
| `ris-port-op-manage-installation/scripts/ris-install.sh` и `docs/installation.md` | Обновляет managed package, не Beads descriptions; успех установки не означает готовность старых данных |

Контракт — [адаптерный ресурс](../../skills/ris-proj-adapter-beads-tasks/references/feature-record.md),
нормативная область — [product §4](../product/04-contracts-and-adapters.md).
Инвентаризация ограничена данным repository/Beads snapshot и найденными consumers;
не обещает полноты внешних plugins/проектов или совместимости других клиентов.
Статическое чтение и parity не подтверждают фактическое поведение агента.
