# Принятие требований session-retrospective

## Решение requirements-v1

- `decision`: `accepted`.
- Дата: 14 октября 2026 года.
- Принявшая сторона: пользователь текущего интервью о ретроспективе RIS-сессий.
- Принятый кандидат: итоговое предложение «целостное предложение методики
  и устройства пары скилов», разделы 1–8, после пошагового интервью.
- Ответ пользователя: «ок»; затем разрешение «публикуй изменения»
  и после снятия режима только чтения — «делай 1 - 4».
- Путь принятого содержания: `docs/specs/session-retrospective/spec.md`.
- `section`: `null` (весь файл).
- `revision`: `containing-commit` — полный опубликованный Git-коммит,
  содержащий это решение и спецификацию; до публикации ссылка pending.

Сохранённая v1 структурирует решения интервью и формулирует AC-001–AC-014
как проверяемое выражение принятого поведения, не как свидетельства реализации.
Рабочие имена пары скилов остаются предложенными; окончательный выбор — в дизайне.

## Область разрешения и дальнейшие этапы

Пользователь разрешил: сохранить спецификацию и принятие, провести независимое
ревью с исправлением замечаний, опубликовать только документы этой работы
в Git, создать фичу под `ris-01r`, отдельно опубликовать Beads/Dolt и проверить
удалённое состояние. Ссылка в `docs/specs/README.md` входит в сохранение.

Это принятие требований. Дизайн и verification отсутствуют; готовность
к декомпозиции и реализации не установлена. Поручение не разрешает начать
реализацию пары скилов, захватывать существующие задачи, менять их содержание,
закрывать новую фичу либо родительский эпик. Первая запись фичи хранит
`design: null` и `verification: null`.

Планируемая принадлежность: открытый эпик `ris-01r`, явно включающий
ретроспективу; постоянный slug `session-retrospective`, устойчивый ключ
`ris:session-retrospective:v1`. Принадлежность не означает приёмку результата
эпика или изменение его блокеров. Перед созданием повторно проверяются
полная очередь и опубликованные ссылки.

Базовая Git-ревизия при подготовке: `4fb35ee0ff469b53717311f613ab4d61fb0f9ac0`.
Репозиторий: RIS; конфигурация — корневой `ris.yaml` v2;
адаптер задач — `ris-beads-adapter`. Чужие текущие изменения по исполнению
задач не являются частью публикации этих документов.

## Решение design-v1

- `decision`: `accepted`.
- Дата: 14 октября 2026 года.
- Принявшая сторона: пользователь диалога «Технический дизайн ris-01r.2
  по спецификации» (OpenCode session `ses_ec6da4344ffe85HLvhjZy84Flc`).
- Принятый кандидат: `session-retrospective/design-v1`, весь файл
  `.sdlc/tasks/ris-01r.2/design-proposal.md`, представленный после независимого
  ревью и устранения замечаний среднего уровня R1/R2.
- Проверенная локальная версия кандидата, SHA-256:
  `b451f3d14c9e5674bde55039a915b6eaa901fa019182fc1e5928f3dc58b55e63`.
  Это свидетельство идентичности локального кандидата, не tracker revision.
- Вопрос принятия: «Принимаете этот дизайн v1 для сохранения в
  docs/specs/session-retrospective/design.md с отдельным решением принятия?».
- Ответ пользователя: «да».
- Путь принятого содержания: `docs/specs/session-retrospective/design.md`.
- `section`: `null` (весь файл).
- `revision`: `containing-commit` — commit, содержащий новый design.md и это
  отдельное решение design-v1; до Git-публикации immutable address pending.

При сохранении кандидат перемещён в проектный адрес; изменены только вводные
сведения о статусе/адресе принятия и заключительный абзац о факте принятия
и сохранения. Технические решения, границы, исследовательские свидетельства,
ограничения и проверочные сценарии сохранены без изменения.

Решение requirements-v1 выше — историческое решение от подготовки требований,
его `containing-commit` по-прежнему разрешается в первоначальную опубликованную
ревизию `af3ec62dcf7207a7798a28d6f66a78dfeaffad81`, а не в будущий commit
дизайна. Исходный requirements reference и отдельное решение не перепринимаются.

Это отдельное принятие и разрешение сохранить дизайн. Реализация, декомпозиция
и закрытие фичи/эпика не выполняются этой операцией. Запись design reference
в существующий feature record требует опубликованных design/decision refs и
нового независимо обеспеченного короткого exclusive writer window над
ris-01r.2, её составом, blockers и evidence. До выполнения этих prerequisites
в Beads сохраняются `design: null` и `verification: null`.

## Исторические адреса v1 при поправке v2

Разделы requirements-v1 и design-v1 выше сохранены без изменения как история
своих операций. Их прежние утверждения «дизайн/дети отсутствуют» относятся к
тому времени, не к текущему feature record. Копирование решений в этот файл
не переопределяет их `containing-commit`:

- Requirements-v1, content commit `af3ec62dcf7207a7798a28d6f66a78dfeaffad81`,
  `docs/specs/session-retrospective/spec.md`, `section: null`; решение:
  https://github.com/atilla777/ris/blob/af3ec62dcf7207a7798a28d6f66a78dfeaffad81/docs/specs/session-retrospective/acceptance.md#решение-requirements-v1.
- Design-v1, content commit `de208d617de8d9d71c31b11b2316342aba7b7f41`,
  `docs/specs/session-retrospective/design.md`, `section: null`; решение:
  https://github.com/atilla777/ris/blob/de208d617de8d9d71c31b11b2316342aba7b7f41/docs/specs/session-retrospective/acceptance.md#решение-design-v1.

## Решение requirements-v2

- `decision`: `accepted` (локальная ограниченная поправка, Git refs pending).
- Дата: 14 октября 2026 года.
- Принявшая сторона: пользователь текущего диалога разрешения R1 по T2
  `ris-01r.2.2`; действительный session/invocation ID не предоставлен.
- Точный ответ пользователя: «Делаем 2 вариант ведь ретро не бдует менять сам разрабываемый проект».
- Предъявленный и выбранный вариант 2 разрешает служебные записи CLI OpenCode
  в его storage/logs вне разрабатываемого проекта при сохранении запрета менять
  проект, исследуемые сообщения и задачи. Переданный запрос явно подтверждает
  scoped acceptance требований **и** технического решения этой поправки;
  это не принятие произвольных новых требований.
- Принятый локальный результат: `session-retrospective/requirements-v2`,
  `docs/specs/session-retrospective/spec.md`, `section: null`.
- Область delta: §8 и AC-013 — только runtime project metadata, housekeeping
  существующей БД/WAL/checkpoint и собственные логи OpenCode вне проекта;
  сообщения/parts/связи истории, source/docs/config/Git, tracker/telemetry
  защищены. Только фиксированные `--pure` read argv, без plugins/serve/import/
  bootstrap/migration/transcript execution; reader не пишет disk export/temp/cache.
  Supplied-export/GET, анализ, метрики и отчёт сохраняют прежние ограничения.
- Предшественник: полный requirements-v1 ref и отдельное решение из раздела
  исторических адресов выше; не переадресуется на commit v2.
- `revision`: `containing-commit` — будущий фактический commit, содержащий
  эту локальную v2 и решение; до публикации immutable address **pending**.

Новая формулировка выражает принятую границу, не свидетельствует об успешной
реализации. Проверка нуля всех storage writes заменяется scoped oracle:
разрешённые service effects отделены от запрещённых project/history/task
изменений. Охват, источник решения и unchanged material areas достаточны
для bounded save без нового интервью. Никакие иные требования не добавлены.

## Решение design-v2

- `decision`: `accepted` (отдельная локальная design-поправка, Git refs pending).
- Дата и принявшая сторона: тот же пользователь текущего диалога R1;
  session/invocation ID не предоставлен и не выдумывается.
- Точный ответ: «Делаем 2 вариант ведь ретро не бдует менять сам разрабываемый проект».
- Основание отдельного design acceptance: переданный запрос явно ограничивает
  выбранный вариант requirements **и design** коррекцией R1. Requirements-v2
  само по себе не подменяет это отдельное решение.
- Принятый локальный результат: `session-retrospective/design-v2`,
  `docs/specs/session-retrospective/design.md`, `section: null`.
- Применимый вход: локальные requirements-v2 и решение requirements-v2 выше;
  immutable refs обоих результатов ожидают публикации.
- Delta: §§4,8–9 и impact §11. Fixed read argv/version/list/export с `--pure`,
  initialized scoped fitness и классификация metadata/DB housekeeping/logs
  вне проекта; ноль запрещённых изменений защищённых объектов. Memfd/pipe,
  валидность полного export и обязательный CLI/no-ID gate сохраняются.
  Нет plugins/serve/import/bootstrap/migration, SQL/storage bypass, replay,
  новых прав export/GET/телеметрии или автоматического перехода.
- Предшественник: полный design-v1 ref и отдельное решение из исторических
  адресов выше; его исходный content/decision commit не меняется.
- `revision`: `containing-commit` — commit, действительно содержащий эту v2
  и отдельное решение; до Git-публикации immutable address **pending**.

## Область операции v2 и публикационный handoff

Разрешено сохранить только spec.md/design.md/acceptance.md текущей task copy
и append impact/evidence в primary `.sdlc/tasks/ris-01r.2.2/execution.md`.
Provider короткого защищённого read/write/verify окна — пользователь;
scope — согласованные документы/локальная заметка этой операции. Окно не
выдаётся за CAS или новую защиту для будущих feature/T3 tracker writes.
Применены noninteractive document-only save ветки владельцев требований
и дизайна. Код/claim/tracker refs/commit/push/closure не входят в эту операцию;
publication остаётся у последующего уполномоченного владельца.

Связанные AC и T1/T2/T3, применимость старых evidence, необходимые новые
runtime checks и безопасный post-publication feature/child update описаны
в design §11. T1 collection не принадлежит и не требует mutation/reopen/repin;
T2 — следующий implementation owner; T3 — pending потребитель для conditional
веток/combined integrated acceptance. Существующие refs всех записей пока v1,
verification null; ни R1, ни T2/фича не объявляются принятыми этой записью.
После проверенной Git-публикации нужны реальные full content commits и
immutable отдельные anchors requirements-v2/design-v2, защищённое согласованное
обновление feature и affected T2/T3 refs/CLI criteria, без silently repinning
исторического T1. Git/Dolt и container acceptance отдельны; **KEEP EDGES**.
