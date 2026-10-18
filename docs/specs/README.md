# Спецификации поставок RIS

Верхнеуровневые нормативные требования, целевой каталог SDLC MVP, общие шаблоны, примеры, источники и материалы проверки находятся в [product-бандле RIS](../product/index.md). `docs/product/` и `docs/rules/` — самостоятельные OKF-бандлы по [профилю корпуса](../product/knowledge-profile.md); этот каталог спецификаций остаётся обычным Markdown без обязательных OKF-метаданных и `index.md`. Здесь остаются планы конкретных поставок:

- [Основа и автор скилов](ris-foundation-and-skill-author.md).
- [Миграция контрактов OKF](okf-contract-migration/spec.md) и [дизайн](okf-contract-migration/design.md); [прежняя спецификация](ris-okf-skills.md) сохранена как история.
- [Первый срез roadmap RIS](ris-roadmap-first-slice.md).
- [Дерево решений для `ris-interview-base`](ris-interview-base.md).
- [Рефакторинг скилов ревью](review-skills-refactoring.md) — самостоятельное ревью, условные snapshot-инструкции и порог обязательных исправлений; реализация запускается отдельно.
- [Интервью о требованиях фичи для будущего `ris-interview-feature`](ris-interview-feature.md).
- [Соглашение об адаптерах и контракт роли `tasks`](ris-tasks-adapter-contract.md).
- [Выбор следующей фичи RIS](ris-select-next-feature.md).
- [Композиция RIS и первый сквозной сценарий фичи](ris-feature-work-first-slice.md).
- [Упрощение подготовки фичи RIS](feature-preparation-simplification.md) — принятый объём `ris-bf4`; [проверки реализации](feature-preparation-simplification-checks.md) фиксируют фактические результаты и пределы.
- [TDD-реализация задачи](tdd-task-implementation/spec.md) — согласованный объём `ris-cbs`: опциональный TDD в базе, обязательный в проектной обёртке и условные ресурсы; [локальные проверки](tdd-task-implementation/delivery-checks.md) и их пределы.
- [Комплексное выполнение одной задачи](task-execution/spec.md) — принятые требования `ris-execute-task`: выбор или продолжение готовой задачи, полный цикл с независимым ревью, публикацией и завершением; [дизайн](task-execution/design.md), [решение принятия](task-execution/acceptance.md) и [проверки поставок T1/T2](task-execution/delivery-checks.md). T2 добавляет условный safe-resume ресурс; controlled code/text resumes и completed combined AC-001–016 evidence matrix записаны с адресной применимостью T1 и ограничениями. Исходный кандидат прошёл независимое R1 ревью; локальная интеграция с текущим main требует независимой переоценки изменённого полного дерева до push. Это не приёмка или закрытие родительской фичи.
- [Ретроспектива одной агентской сессии](session-retrospective/spec.md) — принятая методика переносимой базы и RIS-обёртки: доказательные проблемы и улучшения, локальная история OpenCode, необязательный Langfuse; [решение принятия](session-retrospective/acceptance.md). Дизайн и реализация остаются отдельными этапами.
- [Целевая методика SDLC и план изменений](ris-sdlc-target-specification.md).
- [Проверки capability planning и scoped impact](ris-capability-impact-checks.md) — свидетельства ris-mnr, не отдельная спецификация или реестр.
- [Проверки интегрированной приёмки и завершения контейнера](ris-feature-verification-checks.md) — свидетельства ris-74c и пределы проверенных сценариев.
- [Создание и редактирование нормативных правил проекта](project-rules-authoring/spec.md) — четыре скила, базовый OKF-образец и профили Rails, DragonRuby и Odin; [план поставки](project-rules-authoring/delivery-plan.md).
- [Проектная установка, обновление и удаление RIS](package-installation/spec.md) — требования v1 для OpenCode, Linux/macOS; отдельно принятый [дизайн D1](package-installation/design.md), [решения](package-installation/acceptance.md), [декомпозиция](package-installation/delivery-plan.md) и [адресная поправка N1 к именам/порядку](package-installation/naming-amendment.md). Подготовка `ris-0pr`; реализация ещё не выполнена, продолжение после унификации имён RIS.
- [Инициализация целевого проекта после установки RIS](project-initialization/spec.md) — принятые требования v1 и [дизайн D1](project-initialization/design.md): отдельный сценарий подготовки инструкций, конфигурации, правил и инфраструктуры через профильных владельцев; отдельный переиспользуемый автор исходных знаний о продукте. [Решения принятия](project-initialization/acceptance.md). Пара автора интегрирована в `9d0399ea`; кандидат flow/команды `/risp-init` с ресурсами и справкой локально объединён с выбранным origin/main в task copy `ris-y2u.2`. Независимая переоценка и публикация нового полного snapshot требуют отдельных свидетельств; это не приёмка контейнера `ris-y2u` или live-поведения.
- [Единые имена скилов и команд RIS](skill-command-naming/spec.md) — принятые требования v1: `port/proj`, `op/flow/lib/adapter`, точное совпадение команды со скилом и переход без алиасов; отдельно принятый [дизайн D1 с полной картой](skill-command-naming/design.md), [решения](skill-command-naming/acceptance.md) и [декомпозиция P1 с фактическим оформлением](skill-command-naming/delivery-plan.md#9-последующее-оформление-и-публикация). Подготовка `ris-bsy`; самостоятельная реализация `ris-1fq` не начата. Отдельно принятая N1 установщика применяется после завершения `ris-1fq`.
- [Сквозная связность RIS](sdlc-continuity/spec.md) — требования v1 с исходным решением на `73b135b…`; историческая подготовка `ris-bxc` закрыта. [Дизайн D1](sdlc-continuity/design.md) отдельно принят с уточнениями после завершённой `ris-1fq`: текущие имена, общий `publish-task`, standalone, восстановление primary и read-only навигатор. [Решения](sdlc-continuity/acceptance.md), [исторический аудит](sdlc-continuity/audit.md) и отдельно принятый [план P1](sdlc-continuity/delivery-plan.md). Подготовка принятого дизайна/плана — `ris-vxw`; оформление контейнера и U1–U3 в Beads разрешено, начало реализации требует отдельного поручения.
- [Упрощение практического SDLC](sdlc-simplification/spec.md) — принятые требования и разбиение v1: отдельный эпик и девять задач, обычная параллельная работа без ручных окон, Dolt recovery, проверка состава, передача кандидатов, версии, достаточность, политика проверок, внедрение и статусы. Оформление разрешено; реализация запускается отдельно.
- [Компактные команды RIS](compact-commands/spec.md) — принятые требования v1: 18 коротких команд `risp-`/`risb-`, включая `/risb-skill`, с явной картой на неизменные скиллы; адресная замена прежнего правила одноимённых команд, обновление установки и переход без алиасов. [Решение принятия](compact-commands/acceptance.md#требования-v1). Реализация запускается отдельно.
- [Ускоренное выполнение простой задачи](fast-task-execution/spec.md) — принятые требования v1 для эпика `ris-1wa`: без обязательных подготовительных документов, Beads и файлов отчётности по умолчанию; соразмерные проверки, независимое ревью и подтверждённый direct push. [Решение требований](fast-task-execution/acceptance.md#требования-v1), отдельно принятый [дизайн D2](fast-task-execution/design.md) и [его решение](fast-task-execution/acceptance.md#дизайн-d2), заменяющее опубликованный D1 с сохранением истории. Фича `ris-1wa.1`; реализация запускается отдельно.
- [Компактный обзор плана Beads](plan-status/spec.md) — принятые требования v1 к `ris-proj-op-show-plan` и `/risp-status`: полное незакрытое дерево, атрибуты, блокировки, понятные этапы и одна проверенная рекомендация; [решение принятия](plan-status/acceptance.md). Реализация запускается отдельно.
- [Упрощение подготовки worktree задачи](worktree-preparation-simplification/spec.md) — принятые требования V2 к короткому обычному пути, соразмерным проверкам и отмене обязательных журналов `worktree.md`/`execution.md`; [решение требований](worktree-preparation-simplification/acceptance.md#требования-v2), [дизайн D1](worktree-preparation-simplification/design.md) и [его решение](worktree-preparation-simplification/acceptance.md#дизайн-d1). Текстовый кандидат ris-17f и [проверки поставки](worktree-preparation-simplification/delivery-checks.md) ожидают отдельного независимого ревью и интеграции; это не свидетельство публикации или поведения агента.
- [Путеводитель по командам и маршрутам RIS](workflow-help/spec.md) — требования v1 к `/ris-help`: схема SDLC 80×24 с атомарными операциями и границами комплексных сценариев, ветки простого изменения и бага, короткая справка и подбор маршрута без исполнения; [решение принятия](workflow-help/acceptance.md#требования-v1). Реализация запускается отдельно.

Для текущего меню исходные 18 команд compact-commands дополнены входом
`/risp-run-simple-task` по [адресной поправке fast D2](compact-commands/spec.md#8-поправка-fast-task-execution-d2--один-новый-вход):
`/risp-status` по [plan-status D1, §8](plan-status/design.md#8-поставка-и-совместимость)
`/risp-init` по [initialization D1](project-initialization/design.md)
и единственным исключением `/ris-help` по [workflow-help](workflow-help/spec.md):
22 = 17 project + 4 portable + одно help-исключение. Fast D2 сохраняет обязательные собственную ветку
и краткий Beads в самом RIS; worktree условен. В B `ris-1wa.1.2` подготовлен
локальный исходник flow/команды и синхронизация документации; это уточняет
«реализация запускается отдельно» в записи подготовки выше, но не означает
parity, прохождение delivery checks, независимое integrated review, публикацию
или приёмку фичи. Исходные требования, D2 и решения принятия не переписаны.

Согласованные планы не свидетельствуют о реализации перечисленных в них будущих возможностей.

Имена внутри принятых документов и отчётов сохранены как исторические snapshots;
актуальные вызовы и пути задаёт [инструкция перехода namespace](../skill-command-naming-migration.md).
Поставка `ris-1fq` представлена согласованным namespace-комплектом, локально
интегрированным в основную копию с синхронизированной установкой. Это уточняет
прежнее «не начата» в записи подготовки выше, не меняя принятые v1/D1/P1/N1
или их решения. Свидетельства независимой проверки и удалённой публикации
относятся к конкретным ревизиям и ведутся отдельно.
