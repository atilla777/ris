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
- [Целевая методика SDLC и план изменений](ris-sdlc-target-specification.md).
- [Проверки capability planning и scoped impact](ris-capability-impact-checks.md) — свидетельства ris-mnr, не отдельная спецификация или реестр.
- [Проверки интегрированной приёмки и завершения контейнера](ris-feature-verification-checks.md) — свидетельства ris-74c и пределы проверенных сценариев.
- [Создание и редактирование нормативных правил проекта](project-rules-authoring/spec.md) — четыре скила, базовый OKF-образец и профили Rails, DragonRuby и Odin; [план поставки](project-rules-authoring/delivery-plan.md).

Согласованные планы не свидетельствуют о реализации перечисленных в них будущих возможностей.
