# Сквозная связность RIS — предложение плана P1

**Статус: proposed, не принят.** Это результат подготовки для следующего решения
пользователя, не разрешение создавать перечисленные записи или начинать реализацию.
U1–U3 — локальные метки предложения, не Beads IDs. Текущая подготовительная задача
`ris-vxw` не является контейнером поставки.

## 1. Входы и минимальное разделение

Требования v1 и их решение — Git
`73b135bb2c0ef096b23aca314e6060e54f0c9202`, `spec.md`, section null,
`acceptance.md#требования-v1`. [Уточнённый D1](design.md) отдельно принят по
[решению](acceptance.md#дизайн-d1); его full SHA и immutable decision address
устанавливаются после фактической публикации этой подготовки. До этого зависимая
запись задач реализации не получает выдуманного published ref.

Наблюдаемый baseline — `80efd559dfe1dd8b09beb08114f0c4e4a972ad2e`: 41 скил,
37 команд, naming поставлена, функциональные изменения D1 ещё отсутствуют.
Актуальные consumers и параллельный installer проверяются заново перед исполнением.

Одна task была бы возможна технически, но объединила бы изменение общих входов/
публикатора, всех планировочных стыков и новую самостоятельную операцию навигации.
Три единицы дают проверяемые результаты: общий используемый foundation; полный
путь существующими операциями; затем навигация по реально поставленным контрактам.
Это не разбиение по файлам, тестам или стадиям реализации.

После согласования предлагается standalone task-контейнер без искусственного
эпика и feature-record, с обязательными результатами U1–U3 и собственной общей
приёмкой. Общие AC не копируются во всех детей; каждый получает собственный scope,
критерии, точные принятые refs и необходимые seams. Принятие P1 разрешит оформление
записей, но не заменит отдельное поручение начать выбранную задачу.

## 2. Проверяемые единицы

### U1. Публиковать адресуемый результат без фиктивной задачи

**Результат:** существующий `ris-proj-op-publish-task` принимает task/change и
pre-ID documents с одним Git алгоритмом и независимым review/remote gate.
Context восстанавливает primary по принятому правилу; common задаёт достаточный
восстанавливаемый итог. Нормативные и рабочие контракты этих responsibilities
согласованы, исходники и установка синхронны.

**Состав:** `ris-proj-op-publish-task`, `ris-proj-op-resolve-context` и configuration
resource, `ris-proj-lib-common/references/artifacts.md`; относящиеся нормы и
текущие потребители primary/handoff, включая worktree/plan/review inputs, которым
нужно убрать противоречащее требование всегда повторять explicit primary.
Существующий Beads `dolt.publish` переиспользуется без нового алгоритма.

**Проверка:** чтение task vs pre-ID gates; requirement-only не требует дизайна/
implementation/ID, но сохраняет snapshot/review/outgoing/permission/remote checks;
explicit/valid saved/missing/conflicting primary различимы; отчёт содержит result
locator/version/decision/channel/limits без обязательного next skill.

**Покрытие:** AC-006,009,013; основа AC-001,002,008,010,011,014,016.
**Исключения:** создание standalone records, новый навигатор и изменение предметных
portable методик. Не утверждать выполнение всего AC-008 из одной готовности publisher.

### U2. Продолжать планирование и поставку по ID, включая standalone

**Результат:** существующие операции образуют законченный короткий ID-путь с
явными full/limited boundaries, публикацией планирования и отдельным завершением
standalone-контейнера. Каждый ребёнок содержательно самостоятелен.

**Состав:** `ris-proj-op-specify-feature`, `ris-proj-op-design-feature`,
`ris-proj-op-decompose-feature`, roadmap/refine-epic и необходимые selected-adapter
standalone операции с явной областью возможностей, не скрытым расширением tasks v1;
`ris-proj-op-complete-container`; оба существующих flow и затронутые task owners/
resources, документы/команды/установка. Portable owners переиспользуются без новых
обязательных RIS/Beads-зависимостей. Accepted inputs/decisions остаются раздельными.

**Проверка:** producer→consumer матрица по audit §§3–4 в актуальных именах:
direct finished/limited; one-task/multiple; feature/standalone; success/partial/
interrupt/revision. Реальные вызовы U1 и adapter receipts; sufficient child scope;
container evidence/mandatory composition/cancellation/blocker guards и запрет
recursive closure; неизвестные/unsupported records не мигрируются молча.
Git/Dolt publication раздельны; closed pending route не переоткрывает контейнер.

**Покрытие:** AC-001–005,008,010–013,015; применение AC-006,009,014,016.
**Prerequisite:** U2 → U1: прямые завершённые операции должны вызывать уже
доступного publisher с pre-ID контрактом и использовать новые context/handoff inputs.
**Исключения:** навигатор, новый SDLC engine/registry, интеграция Gas City,
автоматический запуск реализации и изменение чужой installer-поставки.

### U3. Подсказывать продолжение по поставленным контрактам

**Результат:** `ris-proj-op-suggest-continuation` и одноимённая тонкая команда
дают обоснованный короткий вызов, человеческое решение или exact blocker по
текущим фактам. Source folder самодостаточен после установки.

**Состав:** новый project skill без portable пары; conditional discovery реальных
owners, ID либо explicit no-ID locator; common/context/selected adapter только
по предметной необходимости; README/inventory и синхронизированная установка.

**Проверка:** статическое чтение unfinished operation/scenario vs next result vs
return to caller vs human decision vs missing compatible owner. Нулевые persistent
writes/claim/acceptance/push/closure/launch; никакой копии recovery. Примеры
используют реальные имена/refs/IDs и не выдают recommendation за readiness.

**Покрытие:** AC-007,014; применение AC-002,006,011,015,016.
**Prerequisite:** U3 → U2: навигация должна ссылаться на принятые и уже поставленные
standalone/publication/recovery routes, не маскировать отсутствие владельца.
Черновая независимая работа возможна, dependent acceptance ждёт U2.

## 3. Общая приёмка контейнера

На одной идентифицированной интегрированной ревизии проверить все AC-001–016,
обе карты SDLC, применимость independent review, нормы и owner-relative resources,
thin commands и source/install paths/bytes/types/modes. Состав baseline 41/37
не вечная константа: с одним навигатором без иных поставок 42/38; installer может
добавить собственный компонент, его фактический baseline учитывается отдельно.

Основные seams: короткий ID/readiness, feature vs standalone, child/parent,
direct/component публикация, partial/retry/revision, navigation read-only.
Владельцы совместного результата — контейнер и отдельная операция его завершения,
а не последний ребёнок. Отдельная задача только ради общей проверки не создаётся.

Все проверки инструкций — статические и независимое read-only review, без agent
behavioral tests, live runs или нового harness. Тесты, зеркалящие текст, не нужны.
Git publication, exact task completion и Dolt publication/read-back проверяются
отдельно. При недоступной публикации фиксируются реальные partial effects.

## 4. Impact и следующее решение

Нормы concepts/rules меняются через проектного OKF owner с explicit root/scope.
Skills/resources/commands изменяются через `ris-proj-op-author-skill` с применением
`ris-port-op-author-skill` там, где это его предмет. Specs остаются обычным Markdown.
Перед записью P1 перечитать all-status tasks и links: не создавать дубль, сохранить
историю закрытых `ris-bxc`/`ris-1fq`, не менять чужие записи/installer blockers.
Общие README/package inventory правки согласуются при интеграции, не дают сами по
себе права менять installer scope или добавлять cross-initiative dependency.

**Предложение для пользователя:** согласовать standalone контейнер и три единицы
U1–U3 с направленными prerequisites U2→U1, U3→U2, затем разрешить их оформление
в Beads с опубликованными refs. Пока согласования нет, implementation IDs отсутствуют.
