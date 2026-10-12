# Проверки поставки task delivery (ris-npn)

Дата: 12 октября 2026 г. Область: критерии задачи
`ris:sdlc-target:task-delivery` по
[целевой спецификации](ris-sdlc-target-specification.md) §§4.7–4.9,
6.2–6.3, 8, 10 (9–13). Это отчёт о проверках, не новая спецификация требований
и не свидетельство готовности ещё не поставленного feature verification.

## Реализованное разделение

- `ris-plan-task-base` удерживает принятые design/contracts и достаточные test
  seams; проектный `ris-plan-task` проверяет ID и сохраняет локальный план.
- `ris-implement-base` реализует/исправляет ограниченное изменение без RIS;
  `ris-implement-task` владеет подтверждённым claim, проектным контекстом,
  совокупным code/tests/docs результатом и локальными свидетельствами.
- `ris-review-base` даёт read-only предметный verdict; `ris-review` проверяет
  проектные входы, независимость и сохраняет отчёт. Отдельный запуск даёт
  независимое ревью; саморевью не проходит gate публикации.
- `ris-update-documentation` — самостоятельная проектная операция, со
  специалистом OKF только для выбранного реального бандла. Отдельная база
  не требуется для синхронизации разрешённых документов проекта.
- `ris-publish-main` — единая Git-операция интеграции и подтверждённого direct
  push. Она не пишет tracker, не публикует Dolt и не закрывает контейнеры.

Нет второго workflow engine или обязательной задачи на каждый этап.
Base-методики получают содержательные входы без RIS конфигурации/адаптера;
wrappers проверяют свой проектный результат, а не копируют их алгоритмы.

## Среда и метод наблюдения

OpenCode 1.18.33, openai/gpt-6.1-sol, Linux, Python 3.14.7, Git и PyYAML.
Два disposable проекта: обычные `docs/rules`, `docs/specs`, `.sdlc/tasks`,
основная ветка `main`; другие `knowledge/policy`, `delivery/specifications`,
`scratch/jobs`, основная ветка `trunk`. У обоих отдельный local bare Git remote.
Временная установка содержит source skills с ресурсами; прогоны — реальные
отдельные OpenCode контексты с журналами инструментов и inspectable эффектами.

Test-only JSON adapter явно поддерживает exact read и guarded claim, работает
последовательно под одним владельцем. Это **не Beads CAS, не Dolt и не
доказательство распределённой concurrency**. В реальной задаче RIS применяется
выбранный Beads adapter, sandbox claim/read-back и отдельная публикация.
Решения принятия requirements/design в fixtures даны синтетическим владельцем
и проверяются по фактическим whole-file SHA-256; это не живое принятие продукта.

## Наблюдаемые результаты

| Проверка | Фактическое наблюдение | Результат |
|---|---|---|
| Структура/установка | Метаданные восьми изменённых скилов, source/installed byte parity, 28 source folders, diff whitespace | PASS |
| План в двух проектах | Adapter read, actual code/spec/design/decision hashes, AC coverage; сохранённый plan прочитан по configured ID path; планирование без claim | PASS |
| Реализация/claim | Claim и read-back раньше code/test edits; существующая чистая функция и signature сохранены; invalid/zero/boundary tests сначала выявили отсутствие guards, затем прошли | PASS |
| Checks/design fitness | По 4 и 5 test methods; чистое владение без нового storage/global state; actual errors/negative/zero/insufficient сценарии | PASS |
| Независимое review | Новые review contexts применили base, проверили actual diff/new files и exact snapshot; сохранены reports | PASS после исправления F-01 |
| Snapshot approval | Полный prospective Git manifest (15 paths, modes/blobs), base tracker bytes и predeclared context exclusions; сохранение local report не меняет approval subject | PASS |
| Git integration/publication | Fast-forward task branch → установленная primary branch; commit/push и remote ref/fetch/bare snapshot совпали с reviewed tree; повторная публикация existing snapshot — no-op | PASS |
| Upstream drift | Поздний compatible upstream файл изменил полное дерево; старое review не разрешило новую интеграцию/push; после отдельной интеграции и свежего independent assessment новая ревизия проверена | PASS |
| Stale design | Добавление mutable cache не совпало с accepted digest и нарушало pure contract; partial unsaved plan, dependent implementation blocked, bounded impact, никаких исправлений accepted sources/claim/code | PASS |
| Self-review и изменённый код | Self-approval отвергнуто; другой dirty source вернул 999 и провалил tests — push/commit не выполнялись | PASS |
| Actual docs update | Исправлены ложные implemented-service/negative/overdraft claims, добавлен нужный API concept и nested index link; все type/index/6 links корректны, product/spec/code/tracker unchanged | PASS |
| Portable direct use | Plan/implementation/review вне RIS без других skill loads/config/tracker; meaningful 5-method unittest и fingerprints; отсутствие baseline честно оставило delta review unverified | PASS для portable operation/отказа, не для исторической delta |
| Selection | Natural Russian plan request выбрал `ris-plan-task` и сохранил plan; neighboring commit-message request не загружал task/review/publish skills; отдельная description classification остальных соседей | PASS в проверенном контексте |

Проверенные Git snapshots fixtures:

- Первый проект: task commit `dc67de729f4a98fd480cfdf3b63cedcc0a7c3776`,
  approved tree `dd2cb888b4c589fe8e85377eeaf81cadf319734b`; поздняя интегрированная
  ревизия после upstream change `61be98455ae8900fb751cf55b517d2a24fbb1a0c`
  отдельно проверена новым review.
- Второй проект: commit `8c5de0c0a035de5dc08ee3d8cacccf1f8d3fd755`,
  approved tree `8d137d4fc7177c8348ade75703113f181952ad2c`; финальный
  independent review и no-op publication проверили полный Git snapshot.

## Ревью и исправление

Первое независимое general review нашло **F-01, средний**: fingerprint смешивал
approval subject с локальным tracker claim/отчётами/tooling; два прогона по-разному
оценивали соответствие будущему Git commit. Начальный push второго fixture
доказал транспорт, но не считается успешной проверкой первоначального gate.

Исправлены portable implementation/review и project review/publication:
до review объявляется полный предмет публикации, отдельно контекст и исключения;
публикующий сравнивает exact staged/committed/integrated snapshot и не вводит
исключения задним числом. После исправления получены новые независимые reviews
и повторные фактические snapshot checks. Предыдущее blocked/historical evidence
сохранено в локальных reports, а не заменено заявлением об успехе.

## Пределы

Единичные прогоны одной среды/модели, не оценка стабильности всех клиентов.
Description classification не выдаётся за end-to-end routing всех запросов.
Не проверены distributed tracker writers, сетевой отказ реального Git hosting,
каждая ветка worktree recovery и полный продуктовый feature verification.
Последний принадлежит отдельной задаче плана; локальные tests/review не закрывают
родительскую фичу. Проверяемый итог реальной ris-npn и опубликованный Git SHA
сохраняются в её Beads-записи; локальные logs не обязательный удалённый вход.
