# RIS — инструкции агенту

Перед работой прочитай [README.md](README.md) и применяй [правила разработки](docs/rules/development.md) целиком: они определяют согласование задачи, локальную очередь, проверки, ревью и публикацию. Не считай планы уже реализованными функциями. Для проектных путей RIS используй корневой [ris.yaml](ris.yaml); расположение конфигурации относительно этого файла — корень проекта.

В этом проекте установлены `ris-author-skills-base`, `ris-author-skills`, `ris-common` и `ris-context` в `.opencode/skills/`; исходные скилы хранятся в `skills/`. Для автономного скила используй `ris-author-skills-base`, для RIS-интеграции — `ris-author-skills` (также доступна команда `/ris-author`). Нормативная спецификация — [docs/concepts/README.md](docs/concepts/README.md), планы поставок — [docs/specs/](docs/specs/README.md). Локальная `tasks/` остаётся вне Git и не является будущей `.sdlc/tasks/`.
