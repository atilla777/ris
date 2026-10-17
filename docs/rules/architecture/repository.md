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
| Управление комплектом RIS | `ris-port-op-manage-installation` владеет намерением/параметрами/проверенным отчётом; тонкая команда `/risb-installation` только загружает скил. Единственный файловый движок — его `scripts/ris-install.sh` (W1); он владеет namespace, version/schema-1 journal, self-copy и rollback, без ris.yaml/Beads/инициализации. Компактные команды требуют пакетного свидетельства принадлежности `references/command-ownership.txt`; старый version marker или префикс не разрешают удалять чужие файлы. Первая миграция требует нового checked-download/bootstrap, старый движок не приобретает компактный пакет. `tests/package_installation_integration/` проверяет полный фактический комплект; отдельный workflow — Linux/macOS. Опубликованный W2 `86d2f24f4dd831de3ef00e16973d7c285220340e` прошёл обе ОС в [run 38739083951](https://github.com/atilla777/ris/actions/runs/38739083951) и реальный public pinned bootstrap. В локальной интеграционной копии W2 объединён с U1, source/install синхронны; hosted CI и public bootstrap относятся к исходному W2 SHA, не к интегрированному снимку. Новый движок compact-commands требует собственных обычных CLI-проверок и независимой переоценки полного снимка; main-публикация — отдельная операция. |
| Методика пакета | [Нормативный бандл](../../concepts/index.md). Он описывает требования и также целевые компоненты; фактический состав исходников/установки перечислен в [README](../../../README.md). |
| Правила разработки RIS | [development.md](../development.md); конфигурация путей и адаптера — корневой [ris.yaml](../../../ris.yaml). |
| Принятые поставки | [docs/specs/](../../specs/README.md), обычный Markdown, не дополнительный OKF-корень. Будущие решения остаются в спецификациях до реализации. |
| Очередь, статусы и связи | Beads/Dolt через выбранный `ris-proj-adapter-beads-tasks`; Git-публикация не синхронизирует эти записи. |
| Primary/context и handoff (U1) | `ris-proj-op-resolve-context` владеет bounded explicit→verified available saved primary resolution/provenance; потребители не копируют discovery. `ris-proj-lib-common/references/artifacts.md` задаёт recoverable locator/version/decision/channel/remainder без registry/mandatory next prompt. |
| Git-публикация (U1) | Existing `ris-proj-op-publish-task` принимает task/change и pre-ID document subject, включая requirements-only без будущих ID/design/implementation, через один whole-snapshot/review/authority/outgoing/preservation/reassessment/remote алгоритм. `ris-proj-flow-prepare-feature` вызывает этого owner и проверяет receipt; tracker writes/publication и closure не входят в publisher. |
| Подготовка рабочей копии | `ris-port-op-prepare-worktree` владеет переносимой проверкой copy/environment; `ris-proj-op-prepare-task-worktree` — task/actor/claim, project/shared roots, свежим context и совокупным handoff. Ограниченные `worktrees/1` list/read/create принадлежат `ris-port-adapter-git-worktrees` и явно выбранному `ris-port-adapter-worktrunk-worktrees`. |
| ID/standalone planning (U2) | Интегрированные specify/design/decompose восстанавливают own accepted inputs по ID; явно различают feature-record и ordinary standalone. Full finished owners вызывают existing Git/adapter publishers и проверяют receipts; limited contributions заданы явно. Beads `references/standalone.md` объявляет tool-specific create/source/child/link/evidence/exact-close, не расширяя tasks v1. |
| Container/leaf seams (U2, поправка ris-6jf) | В task copy ris-6jf подготовлен source/install кандидат: `ris-proj-op-complete-container` различает administrative exact-ID close, read-only verify и verify-and-close. Административный статус не приёмка и не меняет feature verification; assessment использует собственные outcomes/mandatory composition, verified completion сохраняет evidence/exact-close gates. Beads отдельно объявляет status-only ветку без ослабления `tasks.features.complete`. Execution flow явно требует verify-and-close для one-task feature; leaf plan/change/docs/review локальны до final Git. Structural parent не требует feature payload и не закрывается ребёнком. Main-интеграция, независимое whole-snapshot review и публикация кандидата требуют отдельных свидетельств соответствующей ревизии. |
| Read-only навигация (U3) | `ris-proj-op-suggest-continuation` и команда `/risp-next` владеют только обоснованной рекомендацией, человеческим решением или exact blocker по выбранному ID/no-ID locator и текущим установленным контрактам. Slash-рекомендация проверяет фактическую установленную команду и её явный target, не строит имя из имени скила. Common/context/selected adapter применяются по предметной необходимости; recovery/публикация/исполнение остаются у владельцев. Ноль persistent writes, claim, acceptance, push, closure или launch; рекомендация не authority/readiness. |
| Потребители копии | `ris-proj-op-plan-task` и `ris-proj-op-implement-task-tdd` проверяют пригодность переданной копии без создания worktree и без зависимости на preparation skills/адаптеры worktree. Планирование не требует claim; реализация проверяет/получает разрешённый claim перед изменениями. Конкретные команды и инструментальные особенности операций worktree принадлежат выбранному адаптеру. |
| Реализация и TDD | `ris-port-op-implement-change` владеет обычной реализацией и опциональным TDD; TDD-цикл и сложный publication snapshot — условные `references/` базы. `ris-proj-op-implement-task-tdd` требует TDD и владеет совокупным claim-aware code/tests/docs результатом; default отчёт `workspace.tasks/<ID>/implementation.md`. Протокол feature record остаётся у адаптера задач, применимость входов — у обёртки. |
| Ретроспектива предоставленной истории | Интегрированы source/install `ris-port-op-retrospect-session`: переносимые overview/эпизоды/причины, метрики по объявленной семантике и read-only отчёт; собственные `references/analysis.md`, условный `metrics.md`, `report.md`. Сбор OpenCode, RIS-интеграция и сохранение отчёта не входят в базу. |
| Локальная RIS-ретроспектива | На опубликованном T2 source/install кандидат T3 `ris-01r.2.3` локально интегрирован в task copy, ожидает итоговой независимой переоценки и публикации: `ris-retrospect-session` применяет common/context/базу и targeted evidence; owned OpenCode resource/stdlib reader сохраняют identity/tree/coverage/metrics. Условные wrapper-owned LF/delegation/save-report ресурсы сохраняют прежние границы; нового adapter/SDK/config/роли/state owner нет. Изолированный положительный v2 scoped CLI oracle прошёл только в initialized disposable T3 store OpenCode 1.18.33: protected content/schema сохранены, служебные эффекты классифицированы. Это не real/other-store fitness и не автоматическое распознавание invalid fitness; negatives проверяли withheld caller permission. S1 дал полезный local/no-save отчёт с обычной загрузкой. S2 частичен: supplied LF reasoning полезен, invalid part IDs оснастки и запрет identity inspection блокировали acquisition/save. Реальный ребёнок S3 завершился, parent timeout наступил до validated merge/report/save. New/append/conflict save, full leader validation, live LF, повторяемость и отдельные final-skill CLI cases непроверены. Превышение общего поведенческого бюджета (не менее15m24s при15min) сохранено; последний запрос пользователя исключает дальнейшие agent tests, поведенческие оценки, harness/code tests. Task copy объединяет текущие capability updates и remote rules; primary fast-forward отклонён из-за чужой dirty rules правки, push не выполнен. Итоговое полное дерево ожидает независимой переоценки; универсальная runtime safety и combined acceptance не установлены. |
| Локальные рабочие данные | `.sdlc/tasks/<confirmed-ID>/` основной копии; отдельные рабочие деревья — `.sdlc/worktrees/<confirmed-ID>/`. Старые `tasks/PLAN-*` — игнорируемый исторический архив. |

Namespace этой редакции поставляется согласованным комплектом source/install по
[карте перехода](../../skill-command-naming-migration.md) с добавлением W2 и U3;
текущий инвентарь — в [каталоге скилов](../../skills.md).
Компактные 18 команд `risp-`/`risb-` находятся в `commands/opencode/` с явной картой
к сохранённым скилам; остальные операции доступны прямой загрузкой, lib/adapter
без команд. Основание — [compact-commands v1](../../specs/compact-commands/spec.md),
адресно заменяющая командные правила v1/D1/N1; прежние snapshots и URL не переписываются.
Source/install синхронизированы в task copy ris-2j6; локальная интеграция выполнена.
Полный комплект проверяется по путям, байтам, типам и режимам; публикация подтверждается отдельными свидетельствами соответствующей ревизии.
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
В кандидате ris-17f подготовка и full flow передают компактный проверенный результат
без обязательных `worktree.md`/`execution.md` или заменяющего журнала переходов.
Старые заметки сохраняются как подсказки; план, ход/итог, review и Beads-итог
остаются по правилам. Обычный create проверяет регистрации/target/ref/base/новую
копию; расширенная сохранность условна для reuse и hooks/setup. Обёртка проверяет
весь выбранный config, но сравнивает значимость различий для операции/получателя:
допустимое неиспользуемое `sources.product` не блокирует, смена tracker/используемого
shared path блокирует зависимую передачу. Подробности и пределы — в
[проверках поставки](../../specs/worktree-preparation-simplification/delivery-checks.md).
Это синхронизация кандидата в task copy, ожидающего независимого ревью и интеграции,
не подтверждение main-публикации или runtime. Tracker/notes и вложенные worktree не копируются как
изолированное окружение. Claim и отдельная копия не обеспечивают CAS.

Обычные разрешённые tracker writes используют fresh reads, точечные native
operations и read-back без ручного окна или обязательного global lock. Git owner
собирает/интегрирует latest primary remote в собственной ветке/копии subject и
публикует её commit в разрешённый primary remote ref без force; общую local main
не использует как workspace. Продвижение remote требует только затронутых
проверок и независимой переоценки нового snapshot, с сохранением применимых
свидетельств и неизменённых принятий. Это текущий контракт, не runtime evidence.
