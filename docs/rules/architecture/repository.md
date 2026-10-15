---
type: Architecture
---

# Фактическая карта репозитория RIS

## Владельцы и размещение

| Область | Фактическое размещение и владелец |
|---|---|
| Инструкции пакета | `skills/<name>/SKILL.md` и ресурсы внутри каталога владельца. Переносимые базы получают явные входы; проектные скилы добавляют необходимую RIS-интеграцию. |
| OKF-операции | `ris-port-op-manage-okf-bundle` автономно владеет форматной методикой и единственным pinned snapshot/attribution; `ris-proj-op-manage-okf-bundle` применяет common/context/base, проверяет явные project/root/operation/scope и совокупный проектный результат. Авторы правил и обновление документации сохраняют содержательную ответственность. |
| Проектная установка OpenCode | `.opencode/skills/<name>/` содержит установленные копии исходников с ресурсами. Изменения синхронизируются с `skills/`; это не второй независимо редактируемый источник. Команды — `.opencode/command/`. |
| Управление комплектом RIS | `ris-port-op-manage-installation` владеет намерением/параметрами/проверенным отчётом; одноимённая тонкая команда только загружает скил. Единственный файловый движок — его `scripts/ris-install.sh` (W1); он владеет namespace, version/schema-1 journal, self-copy и rollback, без ris.yaml/Beads/инициализации. `tests/package_installation_integration/` проверяет полный фактический комплект; отдельный workflow — Linux/macOS. Опубликованный W2 `86d2f24f4dd831de3ef00e16973d7c285220340e` прошёл обе ОС в [run 38739083951](https://github.com/atilla777/ris/actions/runs/38739083951) и реальный public pinned bootstrap. В локальной интеграционной копии W2 объединён с U1, source/install синхронны; hosted CI и public bootstrap относятся к исходному W2 SHA, не к интегрированному снимку. Применимость unchanged engine/test свидетельств к изменённым instruction/resource bytes и полный итоговый снимок требуют отдельной независимой переоценки; main-публикация — отдельная операция. |
| Методика пакета | [Нормативный бандл](../../concepts/index.md). Он описывает требования и также целевые компоненты; фактический состав исходников/установки перечислен в [README](../../../README.md). |
| Правила разработки RIS | [development.md](../development.md); конфигурация путей и адаптера — корневой [ris.yaml](../../../ris.yaml). |
| Принятые поставки | [docs/specs/](../../specs/README.md), обычный Markdown, не дополнительный OKF-корень. Будущие решения остаются в спецификациях до реализации. |
| Очередь, статусы и связи | Beads/Dolt через выбранный `ris-proj-adapter-beads-tasks`; Git-публикация не синхронизирует эти записи. |
| Primary/context и handoff (U1) | `ris-proj-op-resolve-context` владеет bounded explicit→verified available saved primary resolution/provenance; потребители не копируют discovery. `ris-proj-lib-common/references/artifacts.md` задаёт recoverable locator/version/decision/channel/remainder без registry/mandatory next prompt. |
| Git-публикация (U1) | Existing `ris-proj-op-publish-task` принимает task/change и pre-ID document subject, включая requirements-only без будущих ID/design/implementation, через один whole-snapshot/review/authority/outgoing/preservation/reassessment/remote алгоритм. `ris-proj-flow-prepare-feature` вызывает этого owner и проверяет receipt; tracker writes/publication и closure не входят в publisher. |
| Подготовка рабочей копии | `ris-port-op-prepare-worktree` владеет переносимой проверкой copy/environment; `ris-proj-op-prepare-task-worktree` — task/actor/claim, project/shared roots, свежим context и совокупным handoff. Ограниченные `worktrees/1` list/read/create принадлежат `ris-port-adapter-git-worktrees` и явно выбранному `ris-port-adapter-worktrunk-worktrees`. |
| ID/standalone planning (U2) | Интегрированные specify/design/decompose восстанавливают own accepted inputs по ID; явно различают feature-record и ordinary standalone. Full finished owners вызывают existing Git/adapter publishers и проверяют receipts; limited contributions заданы явно. Beads `references/standalone.md` объявляет tool-specific create/source/child/link/evidence/exact-close, не расширяя tasks v1. |
| Container/leaf seams (U2) | `ris-proj-op-complete-container` добавляет ordinary standalone branch с собственными outcomes/mandatory composition, independent assessment и protected evidence/exact closure. Оба flow применяют owners/receipts; leaf plan/change/docs/review локальны до final Git. Structural parent не требует feature payload и не закрывается ребёнком. Интегрированные source/install синхронизированы; independent whole-snapshot review и публикация требуют отдельных свидетельств соответствующей ревизии. |
| Read-only навигация (U3) | `ris-proj-op-suggest-continuation` и одноимённая команда владеют только обоснованной рекомендацией, человеческим решением или exact blocker по выбранному ID/no-ID locator и текущим установленным контрактам. Common/context/selected adapter применяются по предметной необходимости; recovery/публикация/исполнение остаются у владельцев. Ноль persistent writes, claim, acceptance, push, closure или launch; рекомендация не authority/readiness. |
| Потребители копии | `ris-proj-op-plan-task` и `ris-proj-op-implement-task-tdd` проверяют пригодность переданной копии без создания worktree и без зависимости на preparation skills/адаптеры worktree. Планирование не требует claim; реализация проверяет/получает разрешённый claim перед изменениями. Конкретные команды и инструментальные особенности операций worktree принадлежат выбранному адаптеру. |
| Реализация и TDD | `ris-port-op-implement-change` владеет обычной реализацией и опциональным TDD; TDD-цикл и сложный publication snapshot — условные `references/` базы. `ris-proj-op-implement-task-tdd` требует TDD и владеет совокупным claim-aware code/tests/docs результатом; default отчёт `workspace.tasks/<ID>/implementation.md`. Протокол feature record остаётся у адаптера задач, применимость входов — у обёртки. |
| Ретроспектива предоставленной истории | Интегрированы source/install `ris-port-op-retrospect-session`: переносимые overview/эпизоды/причины, метрики по объявленной семантике и read-only отчёт; собственные `references/analysis.md`, условный `metrics.md`, `report.md`. Сбор OpenCode, RIS-интеграция и сохранение отчёта не входят в базу. |
| Локальная RIS-ретроспектива | На опубликованном T2 source/install кандидат T3 `ris-01r.2.3` локально интегрирован в task copy, ожидает итоговой независимой переоценки и публикации: `ris-retrospect-session` применяет common/context/базу и targeted evidence; owned OpenCode resource/stdlib reader сохраняют identity/tree/coverage/metrics. Условные wrapper-owned LF/delegation/save-report ресурсы сохраняют прежние границы; нового adapter/SDK/config/роли/state owner нет. Изолированный положительный v2 scoped CLI oracle прошёл только в initialized disposable T3 store OpenCode 1.18.33: protected content/schema сохранены, служебные эффекты классифицированы. Это не real/other-store fitness и не автоматическое распознавание invalid fitness; negatives проверяли withheld caller permission. S1 дал полезный local/no-save отчёт с обычной загрузкой. S2 частичен: supplied LF reasoning полезен, invalid part IDs оснастки и запрет identity inspection блокировали acquisition/save. Реальный ребёнок S3 завершился, parent timeout наступил до validated merge/report/save. New/append/conflict save, full leader validation, live LF, повторяемость и отдельные final-skill CLI cases непроверены. Превышение общего поведенческого бюджета (не менее15m24s при15min) сохранено; последний запрос пользователя исключает дальнейшие agent tests, поведенческие оценки, harness/code tests. Task copy объединяет текущие capability updates и remote rules; primary fast-forward отклонён из-за чужой dirty rules правки, push не выполнен. Итоговое полное дерево ожидает независимой переоценки; универсальная runtime safety и combined acceptance не установлены. |
| Локальные рабочие данные | `.sdlc/tasks/<confirmed-ID>/` основной копии; отдельные рабочие деревья — `.sdlc/worktrees/<confirmed-ID>/`. Старые `tasks/PLAN-*` — игнорируемый исторический архив. |

Namespace этой редакции поставляется согласованным комплектом source/install по
[карте перехода](../../skill-command-naming-migration.md) с добавлением W2 и U3: 43 скила/39 тонких
одноимённых op/flow команд из `commands/opencode/`, без команд lib/adapter.
В текущей task copy установка W2/U1/U2/U3 синхронизирована с исходниками.
Локальное объединение выполнено; независимая переоценка итогового снимка и main-публикация подтверждаются
отдельными свидетельствами соответствующей ревизии; локальная интеграция
не является подтверждением Git push. Строка «Локальная RIS-ретроспектива» выше
сохраняет исторический отчёт T3 и его имена/ограничения; текущий owner —
`ris-proj-op-retrospect-session`, не новое принятие T3.

Эта карта описывает размещение уже существующих элементов репозитория,
а не интегрирует будущие навыки из каталога. Нормативные границы компонентов
и композиции принадлежат [01](../../concepts/01-architecture.md) и
[03](../../concepts/03-composition.md); конкретные рабочие контракты —
их исходным `SKILL.md` и ресурсам. Перечень этапов SDLC не создаёт
автоматического исполнителя очереди или второго хранилища состояний.

Синхронизация имени и TDD-границ подготовлена вместе с исходниками редакции
`ris-cbs` по [согласованному объёму](../../specs/tdd-task-implementation/spec.md).
Она не является отдельным подтверждением Git-интеграции/удалённой публикации.

Default ветка задачи — `task/<ID>`, путь — `workspace.worktrees/<ID>` после
подтверждения ID и связи; явные/ранее подтверждённые значения имеют приоритет.
Опциональное свидетельство `workspace.tasks/<ID>/worktree.md` сохраняет историю
в основной копии по отдельному разрешению, не является реестром или удалённым
обязательным входом. Tracker/notes и вложенные worktree не копируются как
изолированное окружение. Claim и отдельная копия не обеспечивают CAS.
