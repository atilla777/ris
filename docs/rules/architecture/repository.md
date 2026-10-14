---
type: Architecture
---

# Фактическая карта репозитория RIS

## Владельцы и размещение

| Область | Фактическое размещение и владелец |
|---|---|
| Инструкции пакета | `skills/<name>/SKILL.md` и ресурсы внутри каталога владельца. Переносимые базы получают явные входы; проектные скилы добавляют необходимую RIS-интеграцию. |
| OKF-операции | `ris-okf-base` автономно владеет форматной методикой и единственным pinned snapshot/attribution; `ris-okf` применяет common/context/base, проверяет явные project/root/operation/scope и совокупный проектный результат. Авторы правил и обновление документации сохраняют содержательную ответственность. |
| Проектная установка OpenCode | `.opencode/skills/<name>/` содержит установленные копии исходников с ресурсами. Изменения синхронизируются с `skills/`; это не второй независимо редактируемый источник. Команды — `.opencode/command/`. |
| Методика пакета | [Нормативный бандл](../../concepts/index.md). Он описывает требования и также целевые компоненты; фактический состав исходников/установки перечислен в [README](../../../README.md). |
| Правила разработки RIS | [development.md](../development.md); конфигурация путей и адаптера — корневой [ris.yaml](../../../ris.yaml). |
| Принятые поставки | [docs/specs/](../../specs/README.md), обычный Markdown, не дополнительный OKF-корень. Будущие решения остаются в спецификациях до реализации. |
| Очередь, статусы и связи | Beads/Dolt через выбранный `ris-beads-adapter`; Git-публикация не синхронизирует эти записи. |
| Подготовка рабочей копии | `ris-prepare-worktree-base` владеет переносимой проверкой copy/environment; `ris-prepare-task-worktree` — task/actor/claim, project/shared roots, свежим context и совокупным handoff. Ограниченные `worktrees/1` list/read/create принадлежат `ris-git-worktree-adapter` и явно выбранному `ris-worktrunk-adapter`. |
| Потребители копии | `ris-plan-task` и `ris-tdd-implement-task` проверяют пригодность переданной копии без создания worktree и без зависимости на preparation skills/адаптеры worktree. Планирование не требует claim; реализация проверяет/получает разрешённый claim перед изменениями. Конкретные команды и инструментальные особенности операций worktree принадлежат выбранному адаптеру. |
| Реализация и TDD | `ris-implement-base` владеет обычной реализацией и опциональным TDD; TDD-цикл и сложный publication snapshot — условные `references/` базы. `ris-tdd-implement-task` требует TDD и владеет совокупным claim-aware code/tests/docs результатом; default отчёт `workspace.tasks/<ID>/implementation.md`. Протокол feature record остаётся у адаптера задач, применимость входов — у обёртки. |
| Ретроспектива предоставленной истории | Интегрированы source/install `ris-retrospect-session-base`: переносимые overview/эпизоды/причины, метрики по объявленной семантике и read-only отчёт; собственные `references/analysis.md`, условный `metrics.md`, `report.md`. Сбор OpenCode, RIS-интеграция и сохранение отчёта не входят в базу. |
| Локальная RIS-ретроспектива | Локально в main интегрирован source/install кандидат T2 `ris-01r.2.2`, `ris-retrospect-session`: common/context + применение базы, targeted historic/current evidence и response-only отчёт. Owned `references/opencode.md`/`scripts/opencode_read.py` владеют CLI/GET/export, identity/tree/coverage/metrics, без диагноза и нового state owner. Принятый v2 допускает только CLI metadata/housekeeping/log вне проекта; история/файлы/Git/задачи/телеметрия защищены. `--allow-cli` остаётся явным caller-established scoped fitness/initialized-storage assertion. Новые live проверки не выполнены по сокращённому пользователем объёму, не объявлены pass; старый failed-v1 evidence сохранён. Исходный кандидат прошёл независимое ревью сокращённого объёма; изменённый интегрированный snapshot требует независимой переоценки до публикации. Langfuse/delegation/save/combined acceptance — T3. |
| Локальные рабочие данные | `.sdlc/tasks/<confirmed-ID>/` основной копии; отдельные рабочие деревья — `.sdlc/worktrees/<confirmed-ID>/`. Старые `tasks/PLAN-*` — игнорируемый исторический архив. |

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
