---
type: Architecture
---

# Фактическая карта репозитория RIS

## Владельцы и размещение

В этой редакции исходников и синхронизированной установки реализована клиентская
`/ris-help`: paired OpenCode
TUI-плагин локально показывает фиксированные daily/full Markdown без модели;
семантические вопросы передаёт read-only владельцу `ris-proj-op-show-help`
с условными cards/routes.
Это единственное исключение из `risp-`/`risb-`, без aliases и искусственной
portable-пары: предмет — сам RIS. Обычная справка не требует config/Beads/repo,
применяет только нужные общие правила, ничего не пишет/запускает и не подменяет
`next`/`status`. Исходники и установленная копия синхронизируются вместе.
Help и init интегрированы в `929ffe395ada51ed3bb6f331e796be838fbe011d`;
это статус исходников, не подтверждение runtime или обнаружения конкретным клиентом.
Единая актуальная точка входа в готовность и ограничения — [README](../../../README.md#current-readiness-and-limits).
Текущий состав исходников: 52 скила, пять flow, 20 пользовательских входов
(15 project + 4 portable + одно help-исключение). Контракт lean execution задан
исходниками изменения ris-b1a.4; описание контракта не доказывает его Git-публикацию,
independent approval, runtime evidence или whole-S1 acceptance.
Исторические числа ниже
относятся к указанным там ревизиям. Старый `ris-help.md` удаляется из reserved
legacy `ris-*.md`, чтобы не конфликтовать с клиентом. Новый установщик управляет
точным `.opencode/plugins/ris-help/` только по installed `plugin-ownership.txt`;
чужие плагины и глобальные настройки сохраняет. Журнал schema 2 включает плагин;
schema 1 восстанавливается с прежней foreign-классификацией. Первая миграция
требует нового plugin-aware bootstrap; старый движок плагины не поставляет.

| Область | Фактическое размещение и владелец |
|---|---|
| Инструкции пакета | `skills/<name>/SKILL.md` и ресурсы внутри каталога владельца. Переносимые базы получают явные входы; проектные скилы добавляют необходимую RIS-интеграцию. |
| OKF-операции | `ris-port-op-manage-okf-bundle` автономно владеет форматной методикой и единственным pinned snapshot/attribution; `ris-proj-op-manage-okf-bundle` применяет common/context/base, проверяет явные project/root/operation/scope и совокупный проектный результат. Авторы правил и обновление документации сохраняют содержательную ответственность. |
| Исходная основа продукта | Source/install пара интегрирована в [9d0399ea](https://github.com/atilla777/ris/commit/9d0399ea048145bba1d2b66d0da45fa8c87e8454) по принятому [D1, §4](../../specs/project-initialization/design.md#4-документы-и-порядок-работы): `ris-port-op-formulate-product-foundation` владеет переносимым read-only содержательным предложением и условно применяет существующее интервью; `ris-proj-op-author-product-foundation` — common/context, отдельным принятием конкретного содержания, сохранением в `sources.product` через проектного OKF-owner и совокупным read-back. Формат остаётся у OKF, содержание — у автора; create/bounded update не запускают init/roadmap/разработку. Прямая загрузка без новых команд; свидетельства той поставки не означают приёмку инициализации или live-поведения. |
| Инициализация проекта | Интегрированы `ris-proj-flow-initialize-project` и тонкая `/risp-init` в `929ffe395ada51ed3bb6f331e796be838fbe011d` по [D1](../../specs/project-initialization/design.md). Flow владеет единым диалогом, обоснованным набором настроек, согласованными bootstrap-записями и совокупной локальной готовностью; после записи повторно применяет read-only context v2. По принятому [T7](../../specs/sdlc-audit-remediation/spec.md#t7-уточнить-смысл-executionroles) ведущий применяет владельцев сам либо делегирует неинтерактивные операции согласованному доступному исполнителю `project-initialization`, проверяя фактический запуск. Независимый reviewer реально запускается отдельно от всех авторов/исправителей; роль сама не доказывает модель, запуск или независимость. Продукт → архитектура → инженерные правила остаются у существующих авторов с отдельными принятиями и scoped OKF-save. Условные Git/Beads/tools/agents/recovery-ресурсы не расширяют установщик и сохраняют раздельные разрешения. Commit/push — отдельное предложение через existing publisher; отсутствие remote не отменяет локальные проверки. Не создаёт roadmap/фичи и не настраивает build/test/format/CI. Интеграция исходников не означает готовность произвольного проекта или новую оценку поведения агента; конкретные проверки и независимое review относятся к своему snapshot. |
| Проектная установка OpenCode | `.opencode/skills/<name>/` содержит установленные копии исходников с ресурсами. Изменения синхронизируются с `skills/`; это не второй независимо редактируемый источник. Команды — `.opencode/command/`; paired client-плагин — `.opencode/plugins/ris-help/` из `plugins/opencode/ris-help/`, без глобальных config writes. |
| Клиентская справка (ris-1te) | Плагин владеет одной `/ris-help`, exact whole-argument выбором daily/full на русском/английском и scrollable Markdown dialog без модели. Единственный источник четырёх страниц — `plugins/opencode/ris-help/pages/`; прямой скил читает те же installed assets. Вопрос разрешает фактический ID/name `ris-proj-op-show-help` и передаёт один `session.prompt` с attachment и `delivery: queue`; из Home создаёт location-scoped help session. Отсутствующий/неоднозначный скил и ошибка запроса видимы, без fake alias/fallback. Реальный bounded ABI-тест OpenCode 2.0.32 проверяет production TUI и prompt schema с `resume:false`, без запуска агента; это не агентское поведенческое свидетельство. |
| Управление комплектом RIS | `ris-port-op-manage-installation` владеет намерением/параметрами/проверенным отчётом; тонкая команда `/risb-installation` только загружает скил. Единственный файловый движок — его `scripts/ris-install.sh`; он владеет namespace, version/schema-2 journal с чтением legacy schema 1, self-copy и rollback, без ris.yaml/Beads/инициализации. Компактные команды и точный help-плагин требуют пакетных `references/command-ownership.txt` и `plugin-ownership.txt`; старый version marker или префикс не разрешают удалять чужие файлы. Первая миграция требует нового checked-download/bootstrap, старый движок не поставляет плагин. `tests/package_installation_integration/` проверяет полный фактический комплект; отдельный workflow — Linux/macOS. Исторический опубликованный W2 `86d2f24f4dd831de3ef00e16973d7c285220340e` прошёл обе ОС в [run 38739083951](https://github.com/atilla777/ris/actions/runs/38739083951) и реальный public pinned bootstrap. Hosted CI и public bootstrap относятся к исходному W2 SHA, не к новому снимку. Текущий движок требует своих обычных CLI-проверок и независимой переоценки полного снимка; main-публикация — отдельная операция. |
| Продукт и методика пакета | [Product-бандл RIS](../../product/index.md), выбранный в `sources.product` корневого `ris.yaml`. Содержит нормативную методику, дизайн, требования и целевые компоненты; перенос не переобъявляет их принятие или готовность для каждой продуктовой операции. Фактический состав исходников/установки перечислен в [README](../../../README.md). |
| Правила разработки RIS | [development.md](../development.md); конфигурация путей и адаптера — корневой [ris.yaml](../../../ris.yaml). |
| Принятые поставки | [docs/specs/](../../specs/README.md), обычный Markdown, не дополнительный OKF-корень. Будущие решения остаются в спецификациях до реализации. |
| Очередь, статусы и связи | Beads/Dolt через выбранный `ris-proj-adapter-beads-tasks`; Git-публикация не синхронизирует эти записи. |
| Roadmap и граф фич (ris-a17) | Интегрировано в `6db21d8ace9d4c0c66aa4d49dc396e48f0bbd7a4`: `ris-proj-op-plan-roadmap` владеет единым эпик/предварительные фичи результатом с epic-only/nearest (default)/all глубиной. `ris-port-op-plan-epic-features` — автономное read-only предложение, `ris-proj-op-plan-epic-features` — проектные входы, согласование графа, bounded writes и отдельная публикация. Один эпик MVP допустим. Show-plan владеет existing-stage candidates, specify — stage prerequisites; parent-feature gates сохраняются при исполнении ребёнка. Selector/его команда удалены без alias; accepted/foreign/completed work и история сохраняются. Проверки исходников не доказывают live-поведение. |
| Документы фичи | Common `published-inputs.md` владеет full-ID convention/legacy discovery, project owners — actual independent acceptance/applicability, Beads — ordinary native task/edges/close, без JSON/реестра/миграции. New `sources.specs/<full feature ID>/spec.md`: H1 и Feature-ID/Summary/optional Keywords, дизайн inline либо adjacent. Старые payload — hints к реальным sources/decisions, не schema gate. Explicit substantive verify-and-close не требует saved verification; ordinary parent close — отдельный intent ниже. |
| Primary/context и handoff | `ris-proj-op-resolve-context` вычисляет обычную source folder из actual common `.git` в one-repository/one-project layout, без saved-primary cascade. Workspace leaf defaults дополняют только отсутствующие workspace leaves выбранного валидного config; sources — из текущей копии. Потребители не копируют discovery. Common artifacts сохраняет свой recoverable-result контракт без registry/mandatory next prompt. |
| Git-публикация (U1) | Existing `ris-proj-op-publish-task` принимает task/change и pre-ID document subject, включая requirements-only без будущих ID/design/implementation, через один whole-snapshot/review/authority/outgoing/preservation/reassessment/remote алгоритм. `ris-proj-flow-prepare-feature` вызывает этого owner и проверяет receipt; tracker writes/publication и closure не входят в publisher. |
| Подготовка рабочей копии | `ris-port-op-prepare-worktree` владеет переносимой проверкой copy/environment; `ris-proj-op-prepare-task-worktree` — task/actor/claim, project/shared roots, свежим context и совокупным handoff. Ограниченные `worktrees/1` list/read/create принадлежат `ris-port-adapter-git-worktrees` и явно выбранному `ris-port-adapter-worktrunk-worktrees`. |
| Единая подготовка фичи (ris-b1a.3) | Source/install `ris-proj-flow-prepare-feature` интегрирован и Git-опубликован в [c5de3e112c9e35813a5af91b290acccbe1758ec1](https://github.com/atilla777/ris/commit/c5de3e112c9e35813a5af91b290acccbe1758ec1) по [S1 §3 / D1 §§2–4](../../specs/sdlc-feature-lifecycle/acceptance.md). Текущий путь: early same-ID и один выделенный worktree → один requirements/design dialogue и две точные accepted scopes (один акт допустим) → independent review/remote Git → ordinary record → полная existing decomposition → separate tracker publication. Inline sufficient design допустим; внутренние executors условны, независимый reviewer обязателен отдельно. Direct specify/design/decompose сохраняются. Факт Git-публикации не удостоверяет независимость/применимость review или live behavior; свидетельства имеют собственные версии и границы. Lean execution — отдельный ris-b1a.4 ниже. |
| ID/standalone planning | Specify/design/decompose восстанавливают own accepted inputs по project+ID через common document discovery; различают feature и ordinary standalone по действительной области/связи источников, не JSON. Finished owners вызывают existing Git/adapter publishers и проверяют результат; limited contributions заданы явно. Beads `references/standalone.md` объявляет tool-specific create/source/child/link/result/exact-close, не расширяя tasks v1. |
| Container/leaf seams | `ris-proj-op-complete-container` различает ordinary child-based close/feasibility, administrative exact-ID close, read-only verify и explicit verify-and-close. Substantive assessment использует own outcomes/mandatory composition и актуальное integrated evidence, без mandatory saved verification. Administrative status не приёмка и не меняет payload. One-task feature сохраняет own-result execution/review/Git gates; leaf change/docs/review локальны до final Git. Structural parent не требует feature payload и не закрывается ребёнком. |
| Обычное закрытие родителя (ris-oub) | Контракт исходников дополняет ris-6jf коротким default close: `ris-proj-op-complete-container` проверяет непустой полный список прямых детей (все `closed`) и блокеры родителя, Beads выполняет native exact close/read-back без force; Dolt отдельно. Без обхода потомков, аудита декомпозиции, повторных specs/Git/review/acceptance gates. Feasibility — те же чтения без записи. Явная содержательная verify/verify-and-close и own-result gates фичи без детей сохранены; статус родителя не новая независимая приёмка. Исторические evidence не переоцениваются, live-ускорение этим описанием не доказано. |
| Каскад предков execution (ris-qq2) | Общий ресурс `ris-proj-flow-execute-task/references/ancestor-completion.md` применяется full/fast после task close/publication; bugfix наследует full. Один свежий `container-completion` субагент (`standard` в RIS) вызывает existing exact-container owner по реальной parent-цепочке, с child-based gates/read-back/отдельной publication. Нет родителя — no-op; остановка на первом незавершённом/заблокированном, явные границы сохраняются. Direct status/verify/close не запускают каскад; ошибки не отменяют leaf и отражаются отдельно, recovery не повторяет confirmed effects. Третьего модельного уровня и повторной приёмки нет. |
| Read-only навигация (U3) | `ris-proj-op-suggest-continuation` и команда `/risp-next` владеют только обоснованной рекомендацией, человеческим решением или exact blocker по выбранному ID/no-ID locator и текущим установленным контрактам. Slash-рекомендация проверяет фактическую установленную команду и её явный target, не строит имя из имени скила. Common/context/selected adapter применяются по предметной необходимости; recovery/публикация/исполнение остаются у владельцев. Ноль persistent writes, claim, acceptance, push, closure или launch; рекомендация не authority/readiness. |
| Компактный обзор плана (plan-status D1) | `ris-proj-op-show-plan` и тонкая `/risp-status` добавлены в `b69789f21b229aa08740ccc16ed67b46bd77fecc`, интегрированная редакция ris-oqv — `fbd0b56dc1d433bcaa05a7a7f4a8173f84b17a0f`: полный project/ID-subtree обзор всех рабочих типов, реальные parent/blocks, прямой closed/all счётчик и выбор одного кандидата. Common/context/selected adapter обеспечивают общие правила, настройки и чтения; Beads `references/plan-overview.md` — условный read-only ресурс всех типов/скрытых категорий, отдельно от task-only tasks v1. Для точного кандидата применяется существующий `ris-proj-op-suggest-continuation` и проверяется установленная команда. Ноль writes/claim/launch; рекомендация не authority/readiness. Интеграция исходников и справки не доказывает обнаружение команды конкретным клиентом или runtime readiness; evidence сохраняет свою версию. |
| Потребитель копии | `ris-proj-op-implement-task-tdd` проверяет пригодность переданной копии без создания worktree и зависимости на preparation skills/адаптеры worktree; проверяет/получает разрешённый claim перед изменениями. Конкретные команды и инструментальные особенности worktree принадлежат выбранному адаптеру. |
| Реализация и TDD | `ris-port-op-implement-change` владеет реализацией и опциональным TDD; TDD-цикл и сложный publication snapshot — условные ресурсы базы. `ris-proj-op-implement-task-tdd` требует TDD и владеет claim-aware code/tests/docs результатом. Достаточные принятые входы/current code и подход проверяются исполнителем без planner/плана/implementation-report или заменяющего журнала. История RED/GREEN не гейт review/recovery; известное нарушение не скрывается. Full flow гибко применяет owners, reviewer отдельно независим. Claim/blockers/copy, whole-tree review, подтверждённый remote Git и отдельные result/close/Dolt сохраняются; local maintenance — по отдельному authority-контракту ниже. |
| Versioned bug basis | Admission выбирает достаточные report/criteria/decisions/code/environment; Beads `references/bug-execution.md` владеет полным historical read и коротким basis locator/append/reconcile/drift. Fix-bug использует полный existing execute-task flow, не второй engine. Полная дополнительная копия snapshot/новый файл не нужны; incomplete/unavailable history блокирует зависимое исполнение. Старые snapshots сохраняются. Контракт интегрирован в `d1336c27b3d171aa3d2de86f8894197cd58e4128`; реальный positive native-bug history check той поставки явно пропущен пользователем и остаётся unverified, не pass. |
| Проектное ревью | Portable review владеет содержательной оценкой; `ris-proj-op-review-task/references/report-format.md` — единственными YAML types/history/gates, wrapper — save/read-back. Новый файл `/2`; existing `/1` продолжается условно без миграции. Компактные assessment/checks, новые findings/dispositions без six mappings/per-check tree/previous/повтора находок. Один read-only Python CLI проверяет оба формата с exits 0/1/2/3; consumers отдельно проверяют whole-tree/inputs/checks/actual independence. Valid applicable independent approved завершает цикл, changes_required требует repair/re-review, blocked/missing/invalid/unsupported останавливает dependent progression. Beads — адрес/раунд; fast no-file сохранён. Контракт интегрирован в `c2f366c0141b0bb3059905a42d6cfca3aede798c`; старые evidence не переоцениваются. |
| Handoff/recovery | Common artifacts определяет producer/consumer/source/mutability/recovery обязательных фактов, без envelope/журнала. Flows выбирают первый missing/inapplicable результат; context/copy/Git publisher/adapter владеют инфраструктурой и reconcile uncertain effects. Lost evidence восстанавливается точно либо честно заново, не выдумывает historical pass или replay confirmed push/close. Unknown ownership/setup/process блокирует dependent mutation. Контракт интегрирован в `250f650f027166c47b88c83790b9efc91c151b44`; static evidence не доказывает live recovery. |
| Простая порученная задача (B) | Интегрированы source/install `ris-proj-flow-execute-simple-task` и тонкая `/risp-run-simple-task`; поставка A+B опубликована в [8ca6c4a](https://github.com/atilla777/ris/commit/8ca6c4ad252cadb32f0718f826c73609a51e74e5). Flow владеет достаточностью/переходами; основной агент применяет существующих владельцев реализации/docs/публикатора/трекера, отдельный `task-review` фактически ревьюит независимо. Fast-only review без обязательного файла — в development; краткий Beads в RIS, собственная ветка и выделенный worktree обязательны. Copy resource применяет того же preparer, что full/feature/bug; tracker/recovery загружаются по условиям. Полный flow и TDD сохраняют substantive gates без плана/implementation-журнала по ris-b1a.4. Проверки поставки и независимое ревью относятся к указанной версии; это не свидетельство live-поведения или измеренного ускорения. Общая приёмка фичи и её закрытие — отдельные операции Beads. |
| Ретроспектива предоставленной истории | Интегрированы source/install `ris-port-op-retrospect-session`: переносимые overview/эпизоды/причины, метрики по объявленной семантике и read-only отчёт; собственные `references/analysis.md`, условный `metrics.md`, `report.md`. Сбор OpenCode, RIS-интеграция и сохранение отчёта не входят в базу. |
| Локальная RIS-ретроспектива | На опубликованном T2 source/install кандидат T3 `ris-01r.2.3` локально интегрирован в task copy, ожидает итоговой независимой переоценки и публикации: `ris-retrospect-session` применяет common/context/базу и targeted evidence; owned OpenCode resource/stdlib reader сохраняют identity/tree/coverage/metrics. Условные wrapper-owned LF/delegation/save-report ресурсы сохраняют прежние границы; нового adapter/SDK/config/роли/state owner нет. Изолированный положительный v2 scoped CLI oracle прошёл только в initialized disposable T3 store OpenCode 1.18.33: protected content/schema сохранены, служебные эффекты классифицированы. Это не real/other-store fitness и не автоматическое распознавание invalid fitness; negatives проверяли withheld caller permission. S1 дал полезный local/no-save отчёт с обычной загрузкой. S2 частичен: supplied LF reasoning полезен, invalid part IDs оснастки и запрет identity inspection блокировали acquisition/save. Реальный ребёнок S3 завершился, parent timeout наступил до validated merge/report/save. New/append/conflict save, full leader validation, live LF, повторяемость и отдельные final-skill CLI cases непроверены. Превышение общего поведенческого бюджета (не менее15m24s при15min) сохранено; последний запрос пользователя исключает дальнейшие agent tests, поведенческие оценки, harness/code tests. Task copy объединяет текущие capability updates и remote rules; primary fast-forward отклонён из-за чужой dirty rules правки, push не выполнен. Итоговое полное дерево ожидает независимой переоценки; универсальная runtime safety и combined acceptance не установлены. |
| Локальные рабочие данные | `.sdlc/tasks/<confirmed-ID>/` основной копии; отдельные рабочие деревья — `.sdlc/worktrees/<confirmed-ID>/`. Старые `tasks/PLAN-*` — игнорируемый исторический архив. |

## Исторические сведения о поставках

Следующие версионные наблюдения сохраняют исходные границы, не являются текущей
очередью или альтернативными предписаниями. Текущие контракты — в карте выше.

Namespace этой редакции поставляется согласованным комплектом source/install по
[карте перехода](../../skill-command-naming-migration.md) с добавлением W2 и U3;
текущий инвентарь — в [каталоге скилов](../../skills.md).
С парой автора основы продукта, справкой и сценарием инициализации текущий комплект содержит
52 скила, пять flow и 20 входов (15 project + 4 portable + клиентское исключение help); это состав текущих исходников, не новая
оценка runtime или перепринятие исторических поставок.
Компактные команды `risp-`/`risb-` находятся в `commands/opencode/` с явной картой
к сохранённым скилам; остальные операции доступны прямой загрузкой, lib/adapter
без команд. Исторические 18 входов — [compact-commands v1](../../specs/compact-commands/spec.md),
адресно заменяющая командные правила v1/D1/N1; source-меню ris-oqv расширено
`/risp-status` по [plan-status D1, §8](../../specs/plan-status/design.md#8-поставка-и-совместимость),
актуальная карта — в [каталоге](../../skills.md#current-compact-command-menu).
В опубликованной поставке A+B добавлена `/risp-run-simple-task` по [поправке fast D2](../../specs/compact-commands/spec.md#8-поправка-fast-task-execution-d2--один-новый-вход).
Совместный комплект [8ca6c4a](https://github.com/atilla777/ris/commit/8ca6c4ad252cadb32f0718f826c73609a51e74e5)
содержит 49 скилов, четыре flow, 20 команд (16 project + 4 portable).
Для полного дерева `98b76b4b68231990cd9b58648dfbdc18ea6d64a8` проверены
source/install по путям, байтам, типам и режимам, затронутые статические и обычные
CLI-проверки доставки; независимое review-2 `ses_eb6cfe843ffefoLX1H9GnMaUwl`
завершено без замечаний. Версионный итог доступен в Beads `ris-1wa.1.2`,
заметка `ris-1wa.1.2-completion-20261017-v1`. Это проверка инструкций и пакета,
не live-поведения, macOS/hosted CI этой версии или ускорения; общая приёмка
`ris-1wa.1` не следует автоматически из завершения B. Позднейшие изменения
требуют проверки применимости этих свидетельств.

Прежние локальные snapshots B `3e3d21d`/upstream `fbd0b56` и ris-2j6
сохраняются как история подготовки, а не текущий статус ожидания публикации A+B.
Их URL и отдельные решения не переписываются. Локальная интеграция сама по себе
не подтверждает Git push. Строка «Локальная RIS-ретроспектива» выше
сохраняет исторический отчёт T3 и его имена/ограничения; текущий owner —
`ris-proj-op-retrospect-session`, не новое принятие T3.

Эта карта описывает размещение уже существующих элементов репозитория,
а не интегрирует будущие навыки из каталога. Нормативные границы компонентов
и композиции принадлежат [01](../../product/01-architecture.md) и
[03](../../product/03-composition.md); конкретные рабочие контракты —
их исходным `SKILL.md` и ресурсам. Перечень этапов SDLC не создаёт
автоматического исполнителя очереди или второго хранилища состояний.

Синхронизация имени и TDD-границ редакции `ris-cbs` интегрирована в
`fc43451768f08d503afdf8783afff23bd434f37e` по [согласованному объёму](../../specs/tdd-task-implementation/spec.md).
Это статус исходников, не новая оценка runtime или перепринятие исторических проверок.

## Рабочая копия и границы публикации

Default ветка задачи — `task/<ID>`, путь — `workspace.worktrees/<ID>` после
подтверждения ID и связи; явные/ранее подтверждённые значения имеют приоритет.
В интегрированной редакции ris-17f подготовка и full flow передают компактный проверенный результат
без обязательных `worktree.md`/`execution.md` или заменяющего журнала переходов.
Старые планы/заметки сохраняются как необязательные подсказки; review и Beads-итог
остаются по правилам без implementation-журнала. Обычный create проверяет регистрации/target/ref/base/новую
копию; расширенная сохранность условна для reuse и hooks/setup. Обёртка проверяет
весь выбранный config, но сравнивает значимость различий для операции/получателя:
допустимое неиспользуемое `sources.product` не блокирует, смена tracker/используемого
shared path блокирует зависимую передачу. Подробности и пределы — в
[проверках поставки](../../specs/worktree-preparation-simplification/delivery-checks.md).
Редакция исходников интегрирована в `d8c5bac6164eeb559d07e987f42c12467141477a`;
исторические проверки сохраняют свою версию и пределы, не устанавливают новое runtime evidence. Tracker/notes и вложенные worktree не копируются как
изолированное окружение. Claim и отдельная копия не обеспечивают CAS.

Обычные разрешённые tracker writes используют fresh reads, точечные native
operations и read-back без ручного окна или обязательного global lock. Git owner
собирает/интегрирует latest primary remote в собственной ветке/копии subject и
публикует её commit в разрешённый primary remote ref без force; общую local main
не использует как workspace. Продвижение remote требует только затронутых
проверок и независимой переоценки нового snapshot, с сохранением применимых
свидетельств и неизменённых принятий. Это текущий контракт, не runtime evidence.
Публикатор отделяет подтверждённый
remote Git от optional safe local update. Пропуск/ошибка локальной синхронизации
не блокируют close/Dolt; обязательное по политике/поручению обновление остаётся
отдельным незавершённым combined-result долгом. Без authority результат remote-only:
local update не вызывается. Explicit request или applicable accepted project policy
разрешает safe FF уже подходящей source copy, без branch switching/return; найденный
primary не разрешает его мутацию. Common владеет полномочиями полного поручения/вопросами,
Beads claim owner — actor нового назначения (explicit/configured/verified session),
не правом забрать прежнее исполнение. Standing shared Dolt policy — в правилах RIS,
не автоматическая настройка соседних проектов. Это описание текущего контракта,
не новое review/publication/runtime evidence;
исторические строки поставок выше сохраняют исходные версии.
В этой редакции ris-3a4 caller проверяет/передаёт реальные source/version/acceptance
политики и её target/effect boundaries; publisher независимо проверяет источник и
сохраняет прежние guards в `references/primary-sync.md`. Dependency refresh — лишь
отдельно авторизованная условная maintenance-ветка с отдельной проверкой, не следствие
FF. Новых owner/config/registry нет. Ограниченная standing policy самого RIS —
`main` из `origin/main`, без dependency setup — находится в development rules;
[новое решение](../../specs/policy-primary-sync/amendment.md) не переписывает старые specs.
Общий условный `published-inputs.md` владеет чтением сохранённых версий/решений
по project+ID/устойчивым ссылкам независимо от старого checkout; context только
диагностирует пути. Обзор различает собственный следующий результат контейнера
и представленную потомками работу, навигация сначала проверяет необходимость
результата, затем совместимость команды. Свидетельства поправки относятся к
исходникам; установка и публикация подтверждаются отдельно. Статические проверки
не доказывают live-поведение.
