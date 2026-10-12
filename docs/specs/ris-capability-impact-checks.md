# Проверки capability planning и scoped impact — ris-mnr

Дата: 12 октября 2026 г. Основание: [целевая спецификация](ris-sdlc-target-specification.md)
§§2, 4.1–4.2, 5–6, 8.1, P2 и сценарии 1, 7–10. Это свидетельства проверки
четырёх скилов, а не новая спецификация продукта или реестр delivery.

## Область и воспроизведение

Исходное дерево: `ab1094863f77b4c0a10582d6432a318745068468`.
Изменены `ris-plan-roadmap-base`, `ris-plan-roadmap`, `ris-plan-epic`,
`ris-select-next-feature`; установленные копии синхронизированы. Переносимая
база сохраняет независимый proposal, проектные скилы — собственные результаты
roadmap/refinement/selection. Новый общий impact-скил, реестр или оркестратор
не добавлены. После подтверждения публикации точный итоговый Git-коммит
фиксируется в записи Beads `ris-mnr` отдельной операцией завершения.

Среда: OpenCode, модель `openai/gpt-6.1-sol`, Linux; Beads 1.3.1 — для реальной
очереди RIS. Поведенческую проверку выполнил независимый агент `general`,
применяя установленные в двух disposable-проектах инструкции и реальные чтения
файлов/команды read-only JSON-адаптера. Это direct invocation в контексте
проверяющего, без внешнего workflow и без записи в тестовый трекер.

Для повторения подготовить два проекта, установить четыре папки целиком вместе
с `ris-common`, `ris-context` и выбранным доступным read-only tasks-адаптером:

- новый: `sources.product: docs/product/`, `rules: docs/rules/`,
  `specs: docs/specs/`; существующий: `knowledge/vision/`, `engineering/`,
  `increments/`. Конфигурация v2, пути относительно выбранного корня;
- принятая цель — playable gathering and warmth. Один свободный `biomes.md`
  содержит Gathering (2 wood/action в снежном лесу, 1 fiber в болотах), Cold
  (30 секунд тепла), Atmosphere и непринятый вопрос о бурях;
- минимальные правила: Python simulation, `WorldState/v1` владеет состоянием,
  persistence — adapter, governance owner — simulation maintainer. Headless
  проверка допустима, готового нового проекта нет;
- открытый epic E — gathering and warmth. В существующем проекте F/`warm-camp`
  начата; S/`camp-save` открыта. Их принятые design-scopes с проверяемыми SHA-256
  и адресами принятия несовместимо назначают HeatState исключительно
  `WorldState/v1` и `SaveStore/v2` соответственно;
- оба spec содержат AC-001 про 10 секунд и ссылку на Cold/v1. Прочитываемый
  baseline содержит 10 секунд. F.1 связан с `warm-camp#AC-001`, test_warmth и
  прежним evidence для 10 секунд. Код содержит только поле heat_seconds = 10;
  наличие теста не доказывает его запуск или полное camp-поведение;
- X/`gather-wood` открыта, Gathering не изменился, HeatState не используется.
  Есть закрытая историческая задача OLD. Все task/epic списки полные, включая
  closed, чтения конкретных ID и typed dependencies доступны; реальных blockers
  между F/S нет. Предлагаемые prerequisites не выдавать за записанные edges.

## Наблюдения

| Проверка | Полученный результат |
|---|---|
| Переносимая база вне RIS из явно переданных product/rules фактов | Предложены полезные gathering/warmth результаты и допустимый один эпик. Первый headless gathering-срез наблюдаем; нет разбиения по главам biomes или model/API/UI, нет требуемого полного будущего дизайна. |
| Новый проект, roadmap update E, proposal-only | Сохранена identity E, предложен один эпик с конкретными количествами. Недоступный baseline v1 оставил source currency неподтверждённой; отсутствующий specs не доказал отсутствие принятых дизайнов. `changes: []`. |
| Уточнение E | Понятный capability outcome не дробится формально; missing source baseline показан как отдельный пробел, без создания feature tasks. |
| Существующий проект, выбор в E | Проверены custom paths и реальные all-status/ID/dependency reads. F теряет приоритет из-за конкретного product delta и ownership conflict, X остаётся доступной рекомендацией. |
| Material product impact | Cold 10→30 прослежен к E, F, `warm-camp#AC-001`, F.1, test_warmth и прежнему evidence, а также AC-001 S. Старый тест/evidence не подтвердил новую длительность; нет самовольной правки product/AC/acceptance. |
| Активные контрактные scopes | Оба design digest совпали с acceptance JSON до признания принятия. Предложены simulation maintainer как coordinator, согласование общего ownership/version и affected work → coordination/integration prerequisites. Они остались предложениями; независимая X не остановлена. |
| Недоступный baseline — условный вариант | Реальное чтение отсутствующего файла завершилось ошибкой. При подстановке этого условия currency — unconfirmed, а не current/stale; независимо известный ownership conflict остаётся. |
| Editorial-only — scope comparison | Baseline Cold 30 секунд и текущий Cold 30 секунд содержательно совпали: нет behavioral delta в этой области. Это не отменило отдельный material delta относительно v1/10 секунд. |
| Условно согласованный WorldState/v1 | Contract resolution не приняло новое поведение 30 секунд. Требуется решение requirements owner; локальный implementation tweak не переоткрыл design. |
| Routing RU/EN | Goal/MVP → roadmap; vague epic → epic refinement; next feature → selection; child tasks → decomposition; detailed design → design owner; CSS spacing не выбрало эти четыре скила. |

Независимый baseline review до правки показал: capability planning уже работал,
но проверки source versions, AC/task/evidence impact и overlapping accepted
contracts были необязательными/неявными. После правки проверяющий исполнил эти
шаги по реальным данным. Установленные fixture/source файлы совпали по SHA-256;
54 fixture-файла после исполнения совпали с исходным snapshot: побочных записей нет.
Структура, метаданные, parity и `git diff --check` проверены отдельно.

## Ревью и пределы

Независимое implementation/execution review: **замечаний нет**. Проверены
разделение ответственности, переносимость базы, RIS-интеграция, отсутствие чужих
операций и ненужной обязательной загрузки. Итоговая документация проверяется
на том же публикуемом дереве перед коммитом.

Это репрезентативные read-only исполнения и single-agent routing observations,
не оценка статистической устойчивости выбора, не live acceptance владельцев
тестового продукта и не проверка интегрированной фичи. JSON-адаптер не обещает
Beads CAS. Новые операции записи не вводились: сохранение эпиков остаётся под
прежними agreement/concurrency/read-back gates; selection read-only. Git/Dolt
публикация самой ris-mnr проверяется отдельно и фиксируется в её записи.
