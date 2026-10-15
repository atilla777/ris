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
| Методика пакета | [Нормативный бандл](../../concepts/index.md). Он описывает требования и также целевые компоненты; фактический состав исходников/установки перечислен в [README](../../../README.md). |
| Правила разработки RIS | [development.md](../development.md); конфигурация путей и адаптера — корневой [ris.yaml](../../../ris.yaml). |
| Принятые поставки | [docs/specs/](../../specs/README.md), обычный Markdown, не дополнительный OKF-корень. Будущие решения остаются в спецификациях до реализации. |
| Очередь, статусы и связи | Beads/Dolt через выбранный `ris-proj-adapter-beads-tasks`; Git-публикация не синхронизирует эти записи. |
| Подготовка рабочей копии | `ris-port-op-prepare-worktree` владеет переносимой проверкой copy/environment; `ris-proj-op-prepare-task-worktree` — task/actor/claim, project/shared roots, свежим context и совокупным handoff. Ограниченные `worktrees/1` list/read/create принадлежат `ris-port-adapter-git-worktrees` и явно выбранному `ris-port-adapter-worktrunk-worktrees`. |
| Потребители копии | `ris-proj-op-plan-task` и `ris-proj-op-implement-task-tdd` проверяют пригодность переданной копии без создания worktree и без зависимости на preparation skills/адаптеры worktree. Планирование не требует claim; реализация проверяет/получает разрешённый claim перед изменениями. Конкретные команды и инструментальные особенности операций worktree принадлежат выбранному адаптеру. |
| Реализация и TDD | `ris-port-op-implement-change` владеет обычной реализацией и опциональным TDD; TDD-цикл и сложный publication snapshot — условные `references/` базы. `ris-proj-op-implement-task-tdd` требует TDD и владеет совокупным claim-aware code/tests/docs результатом; default отчёт `workspace.tasks/<ID>/implementation.md`. Протокол feature record остаётся у адаптера задач, применимость входов — у обёртки. |
| Ретроспектива предоставленной истории | Интегрированы source/install `ris-port-op-retrospect-session`: переносимые overview/эпизоды/причины, метрики по объявленной семантике и read-only отчёт; собственные `references/analysis.md`, условный `metrics.md`, `report.md`. Сбор OpenCode, RIS-интеграция и сохранение отчёта не входят в базу. |
| Локальная RIS-ретроспектива | На опубликованном T2 source/install кандидат T3 `ris-01r.2.3` локально интегрирован в task copy, ожидает итоговой независимой переоценки и публикации: `ris-retrospect-session` применяет common/context/базу и targeted evidence; owned OpenCode resource/stdlib reader сохраняют identity/tree/coverage/metrics. Условные wrapper-owned LF/delegation/save-report ресурсы сохраняют прежние границы; нового adapter/SDK/config/роли/state owner нет. Изолированный положительный v2 scoped CLI oracle прошёл только в initialized disposable T3 store OpenCode 1.18.33: protected content/schema сохранены, служебные эффекты классифицированы. Это не real/other-store fitness и не автоматическое распознавание invalid fitness; negatives проверяли withheld caller permission. S1 дал полезный local/no-save отчёт с обычной загрузкой. S2 частичен: supplied LF reasoning полезен, invalid part IDs оснастки и запрет identity inspection блокировали acquisition/save. Реальный ребёнок S3 завершился, parent timeout наступил до validated merge/report/save. New/append/conflict save, full leader validation, live LF, повторяемость и отдельные final-skill CLI cases непроверены. Превышение общего поведенческого бюджета (не менее15m24s при15min) сохранено; последний запрос пользователя исключает дальнейшие agent tests, поведенческие оценки, harness/code tests. Task copy объединяет текущие capability updates и remote rules; primary fast-forward отклонён из-за чужой dirty rules правки, push не выполнен. Итоговое полное дерево ожидает независимой переоценки; универсальная runtime safety и combined acceptance не установлены. |
| Локальные рабочие данные | `.sdlc/tasks/<confirmed-ID>/` основной копии; отдельные рабочие деревья — `.sdlc/worktrees/<confirmed-ID>/`. Старые `tasks/PLAN-*` — игнорируемый исторический архив. |

Namespace в этой task-редакции подготовлен вместе с source/install по
[карте перехода](../../skill-command-naming-migration.md): 41 скил/37 тонких
одноимённых op/flow команд из `commands/opencode/`, без команд lib/adapter.
Основная копия обновляется при отдельной проверенной интеграции; эта редакция
не является свидетельством публикации. Строка «Локальная RIS-ретроспектива» выше
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
