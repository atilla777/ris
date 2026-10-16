# Спецификации поставок RIS

Верхнеуровневые нормативные требования, целевой каталог SDLC MVP, общие шаблоны, примеры, источники и материалы проверки находятся в [нормативном комплекте](../concepts/index.md). `docs/concepts/` и `docs/rules/` — самостоятельные OKF-бандлы по [профилю корпуса](../concepts/knowledge-profile.md); этот каталог спецификаций остаётся обычным Markdown без обязательных OKF-метаданных и `index.md`. Здесь остаются планы конкретных поставок:

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
- [Единые имена скилов и команд RIS](skill-command-naming/spec.md) — принятые требования v1: `port/proj`, `op/flow/lib/adapter`, точное совпадение команды со скилом и переход без алиасов; отдельно принятый [дизайн D1 с полной картой](skill-command-naming/design.md), [решения](skill-command-naming/acceptance.md) и [декомпозиция P1 с фактическим оформлением](skill-command-naming/delivery-plan.md#9-последующее-оформление-и-публикация). Подготовка `ris-bsy`; самостоятельная реализация `ris-1fq` не начата. Отдельно принятая N1 установщика применяется после завершения `ris-1fq`.
- [Сквозная связность RIS](sdlc-continuity/spec.md) — требования v1 с исходным решением на `73b135b…`; историческая подготовка `ris-bxc` закрыта. [Дизайн D1](sdlc-continuity/design.md) отдельно принят с уточнениями после завершённой `ris-1fq`: текущие имена, общий `publish-task`, standalone, восстановление primary и read-only навигатор. [Решения](sdlc-continuity/acceptance.md), [исторический аудит](sdlc-continuity/audit.md) и отдельно принятый [план P1](sdlc-continuity/delivery-plan.md). Подготовка принятого дизайна/плана — `ris-vxw`; оформление контейнера и U1–U3 в Beads разрешено, начало реализации требует отдельного поручения.
- [Упрощение практического SDLC](sdlc-simplification/spec.md) — принятые требования и разбиение v1: отдельный эпик и девять задач, обычная параллельная работа без ручных окон, Dolt recovery, проверка состава, передача кандидатов, версии, достаточность, политика проверок, внедрение и статусы. Оформление разрешено; реализация запускается отдельно.

Согласованные планы не свидетельствуют о реализации перечисленных в них будущих возможностей.

Имена внутри принятых документов и отчётов сохранены как исторические snapshots;
актуальные вызовы и пути задаёт [инструкция перехода namespace](../skill-command-naming-migration.md).
Поставка `ris-1fq` представлена согласованным namespace-комплектом, локально
интегрированным в основную копию с синхронизированной установкой. Это уточняет
прежнее «не начата» в записи подготовки выше, не меняя принятые v1/D1/P1/N1
или их решения. Свидетельства независимой проверки и удалённой публикации
относятся к конкретным ревизиям и ведутся отдельно.
