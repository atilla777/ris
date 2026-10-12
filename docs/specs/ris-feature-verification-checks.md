# Проверки feature verification и container completion (ris-74c)

12 октября 2026 г. Область: `ris:sdlc-target:feature-verification` по
[целевой спецификации](ris-sdlc-target-specification.md) §§4.9, 5, 8, 9 P3,
10 (11, 12, 14). Это проверочный отчёт, не новая спецификация или реестр фич.

## Владельцы результата

- `ris-verify-feature-base` — переносимая read-only приёмка полной фичи на одной
  идентифицированной интегрированной версии: AC, cross-component checks,
  architecture fitness, docs/source currency и применимость прежнего evidence.
  Не сохраняет отчёты, не пишет трекер, не ремонтирует и не закрывает работу.
- `ris-complete-container` — проектный владелец полного состава/блокеров, actual
  применения метода, безопасного сохранения приёмки/read-back и отдельного
  закрытия ровно выбранного ID. Для фичи нужен `tasks.feature-record/1`; для эпика
  условно загружается отдельная ветка его критериев, без feature-record/методики.
- Формат и гарантии записи принадлежат выбранному адаптеру; Git integration —
  вход, tracker publication — отдельно разрешённая и проверяемая операция.
  Нет обязательного `verification.md`, child на каждый шаг, нового статуса или
  workflow engine. Задачи исправления и авторские product-правки не входят в скил.

## Среда и метод

OpenCode 1.18.33, Linux, Python 3.14.7 и Git; модель ведущего — openai/gpt-6.1-sol.
Fixtures используют модель по умолчанию своего OpenCode вызова. Отдельные реальные
контексты OpenCode с установленными папками скилов/ресурсами, наблюдаемые tool logs
и прямое чтение файлов/трекерных эффектов. Два проекта: `docs/rules`, `docs/specs`,
`main`; `knowledge/policy`, `delivery/specifications`, `trunk`. У каждого local
bare Git remote. Третий проект копирует repaired tree для отказа tracker transport.

Test-only JSON adapter предоставляет полный all-status read/membership/blockers,
защищённые sequential записи под test-owner window, separate record/close и
независимое чтение remote snapshot. Это симуляция хранения/транспорта, **не Beads,
Dolt, сетевой отказ хостинга или распределённый CAS**. Реальный adapter contract
Beads сохранён: без отдельно установленного окна его записи запрещены.
Принятия требований/дизайна и разрешение repair в fixtures синтетические.

## Наблюдения

| Сценарий | Фактический результат |
|---|---|
| Четыре closed ребёнка + green pre-integration unit/review | F-1/E-1 остаются open: три order-level AC и delegation contract провалились на опубликованной общей версии; reserve unit test проходит |
| Сохранение failed приёмки | Разрешённый actual record-verification с AC/checks/SHA/hashes/inline observations; полный read-back; только F-1 evidence изменён; snapshot publication и независимый remote-read подтверждены; close не вызван |
| Repair и новая интегрированная версия | Test owner исправил quantity forwarding и добавил завершённый C-5; F-1 остаётся open до новой приёмки. Новые 4 tests PASS, полный состав C-1..C-5 и контракт/документы проверены |
| Successful completion | Сохранена новая приёмка, прежний fail verbatim в history; отдельно close F-1, exact read-back и remote-read; E-1 остаётся open |
| Другое расположение документов / отсутствующая гарантия | Контекст разрешил другие paths; прочитан inactive window; полезный actual fail verdict, ни record, ни close не вызваны |
| Portable direct use | Только base из явно заданного источника, без RIS loads/config/adapter calls/persistence; реальные тесты выявили три интеграционных провала; no file effects |
| Subjective AC / missing baseline | В portable variant feel без плейтеста/решения unverified, baseline absent → currency unconfirmed; build не подменяет доказательства |
| Epic direct invocation | Собственные criterion/composition и persisted feature acceptance; отдельный readable epic-record/close, без feature-record или загрузки feature base |
| Повтор завершённой фичи | Natural Russian request проверил сохранённые evidence/status/remote и не переписал history ради повторного вызова |
| Tracker transport failure | После разрешённого local record/close транспорт отказал; remote остаётся open. Отчёт различил local closed / remote open и partial, без blind retry/force/rollback |
| Несогласованный состав | Первоначальные epic/retry inputs ошибочно сохраняли прежний exact набор C-1..C-4 после появления C-5; оба прогона вернули conflict без записи. После исправления fixture inputs проверены успешные epic и repeat |
| Структура/формат | Metadata, installed-relative epic resource, source/installed parity новых папок; 34 source skills; весь concepts bundle: 24 Markdown, применимые OKF 0.2 frontmatter/index/log и 217 local link targets; ordinary specs и diff whitespace PASS |

Fixture Git versions:

- Failed `main`: `8bcc13e235635f30c04f38f0d8d017af01f53a2b`.
- Repaired `main`: `5c8f88cac672a36c575f25016efea442b83f620e`.
- Alternate-path failed `trunk`: `414b5ec62e7483ea64cc49f94a5e7564d2ef7709`.

Requirements/design/product hashes неизменны между failed/repaired версиями;
единственный application diff — передача `q` вместо hard-coded `1`. Affecting
integration tests выполнены заново; green unit/review не переиспользованы как
доказательство полного результата. Tracker evidence содержит проверки и версии,
так что последующий контекст не зависит от ignored локальных логов.

## Выбор и пределы

Прямые вызовы wrapper/base и natural Russian повтор реально исполнялись.
Смежные запросы классифицированы без выполнения: diff review, leaf-task closure,
commit message не принадлежат completion; portable verification отделена от
проектной записи. Это не статистика маршрутизации всех формулировок.

Начальный failure-прогон и его продолжение завершились по лимиту времени до
записи. Actual state перечитан; новый отдельный контекст завершил тот же сценарий.
Эти прерванные вызовы не считаются успешными прогонами и не доказывают стабильность.
Единичные наблюдения одной версии/модели не подтверждают все клиенты, distributed
writers и каждый recovery branch. Полноценный продуктовый плейтест не выполнялся;
проверен отказ при его отсутствии. Публикация самой ris-74c в Git/Beads/Dolt
фиксируется отдельно в её подтверждённой трекерной записи.
