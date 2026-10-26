# Fast: полный короткий цикл ограниченной работы
Feature-ID: ris-ci3.1
Summary: Существующий Fast выполняет одну ограниченную задачу от идеи до проверенного Git-, локального или смешанного результата одним основным агентом, с условным независимым ревью.

## Требования S1

### 1. Статус и основание

S1 — предлагаемые подробные требования, ещё не принятые человеком.

Основание: согласованные границы предварительной фичи ris-ci3.1 в эпике ris-ci3,
зафиксированные 26.10.2026. Они принимают направление и планирование, но не
заменяют принятие этой версии требований или отдельного дизайна.

Наблюдаемая исходная версия RIS:
89af19ccc773cdf7548f559adbc959fa55799b13.

Действующий Fast пока требует отдельного reviewer, Git-oriented completion и
отдельного closure-субагента. Настоящая спецификация предлагает согласованно
изменить эти обязанности только в обозначенном Fast scope. До реализации
изменений действуют текущие правила.

### 2. Цель, пользователи и границы

Пользователь может поручить небольшую работу или ограниченную идею и получить
применённый, проверенный и по применимости опубликованный результат без
отдельного подготовительного проекта и обязательных промежуточных артефактов.

Перерабатывается существующий ris-proj-flow-execute-simple-task. Команда
/risp-run-simple-task <поручение или ID> сохраняется. Подходящий естественный
запрос также может выбрать этот контракт: знание slash-команды не требуется.

Fast допускает одну небольшую, локальную по последствиям, понятную и проверяемую
задачу, не требующую изменения продуктовой логики, архитектуры или существенного
общего/публичного контракта. Небольшая неясность разрешается адресно в этом же
диалоге.

Классификация опирается на последствия, границы и способ проверки, а не на
расширение файла, число строк или закрытый список операций. Допустимы код,
конфигурация, документы, инструменты, versioned/ignored части проекта и явно
выбранные внешние файлы. Установка стороннего скила — только пример.

Fast не допускает:
- изменение продуктовой логики, архитектуры или существенного общего контракта;
- несколько самостоятельных результатов, требующих координации;
- широкие или неизвестные существенные последствия;
- отсутствие достаточного способа проверить результат.

При выходе за эти границы агент объясняет конкретную причину и согласует только
необходимое расширение или подготовку. Автоматически перезапускать весь SDLC
нельзя. Независимая безопасная работа может продолжаться.

Существующие feature/bug/container сохраняют свои настоящие обязательства.
Нельзя объявить их ordinary task ради обхода требований, приёмки, composition,
bug basis или других обязательных gates.

### 3. Короткий цикл и исполнители

Цикл: понять и взять → сделать и проверить → применимо опубликовать и завершить.

Один основной агент непосредственно применяет существующих владельцев.
По умолчанию субагентов нет. Обязательные отдельные интервью, spec/design,
декомпозиция, план, handoff/implementation/review-файлы и журналы не вводятся.

Достаточны поручение, адресные ответы, необходимые существенные решения и
проверяемые критерии. Отдельного согласования технической карточки не нужно.
Пустой запрос не выбирает работу из очереди: агент спрашивает о поручении.

Внутренние действия не требуют передачи собственного контекста между сессиями.
Загрузка владельца не означает обязательного отдельного исполнителя.

### 4. Учёт и полномочия

В RIS обязателен один короткий ordinary task Beads: существующий подходящий ID
переиспользуется; без ID сначала проверяется идентичность во всей относящейся
all-status выборке, затем создаётся одна запись.

Запись содержит достаточные цель, границы, проверку, существенные решения с
атрибуцией и итог. Не создаются искусственные epic/feature/children, readiness
schema или параллельный backlog. Реальное существующее parent membership
сохраняется, но не выводится из синтаксиса ID.

Сохраняются нужные claim/ownership/status/composition/directed-blocker checks,
native guards, sandbox и обнаружение конфликтов. Наличие доступа, claim, копии
или инструмента не расширяет разрешённый объём.

В других проектах task accounting включается переданным ID или действующей
политикой проекта, а не одним наличием adapter в конфигурации.

### 5. Место изменения и сохранность

Для versioned Git edits обязательны одна собственная ветка и один dedicated
worktree на всю задачу через существующего preparer. Пригодная связанная копия
переиспользуется между стадиями и сессиями. Ordinary source folder не становится
площадкой разработки.

Ignored/external файлы меняются в явном фактическом месте назначения. Для
local-only результата не создаются пустой worktree, фиктивный коммит или
неработающая копия настройки внутри worktree.

В mixed задаче versioned часть меняется в своей копии, локальная часть — в
разрешённых фактических targets. Worktree не изолирует Beads, ignored/external
targets и другие shared resources: их конфликты проверяются отдельно.

Чужие tracked/untracked/ignored данные и незавершённая работа сохраняются.
Не разрешены скрытые setup/scripts, установка зависимостей, расширение прав
или автоматический перенос dirty work. Необозримые побочные эффекты блокируют
зависимую мутацию, а не оправдываются малым размером задачи.

### 6. Проверки и условное независимое ревью

Самопроверка обязательна:
- текст — чтение фактического результата и diff;
- конфигурация — применимая валидация;
- логика — содержательные затронутые и регрессионные тесты;
- внешнее/локальное изменение — проверка фактического target и полезного эффекта.

Обязательные проверки и применимый TDD сохраняются.

Независимое ревью требуется, когда есть хотя бы одно основание:
1. явное поручение человека;
2. обязательная применимая политика целевого проекта;
3. конкретно названный существенный риск с объяснёнными последствиями.

Примеры последнего основания: риск потери важных данных, нарушения границы
доступа/безопасности либо существенная труднообратимая ошибка, не покрываемая
обычной самопроверкой. Это не разрешает работу вне допуска Fast. Если последствия
слишком широки или проверка недостаточна, применяется отказ/расширение scope,
а не формальное добавление reviewer.

Изменение кода, внешнее расположение файла и сам факт Git push не являются
самостоятельными безусловными основаниями ревью.

Агент не спрашивает каждый раз, нужно ли ревью, не создаёт отчёт об отказе
и при неактивной ветке не загружает review-роль/формат. Существующая общая норма
RIS о независимом ревью не должна неявно отменять новое Fast-исключение:
действующие нормы и их consumers изменяются согласованно.

При активной ветке reviewer действительно независим от всех авторов/исправителей.
По умолчанию достаточно результата в сессии; YAML не обязателен.
Явно требуемое сохранение использует существующий review format owner.

Обязательное недоступное ревью блокирует зависимый gate. Self-check не выдаётся
за независимое approval. Обнаруженные существенные findings нельзя игнорировать
из-за условности этапа: high/medium требуют исправления, затронутых проверок и
применимого нового независимого рассмотрения. Low получают разумное решение.

При изменении snapshot проверяется применимость evidence. Если ревью требуется,
нужна независимая переоценка нового subject с допустимым переиспользованием
незатронутых свидетельств. Если ревью не требуется, автор выполняет затронутую
самопроверку; это не называется independent approval. Новые последствия могут
активировать ревью или вывести работу за допуск Fast.

### 7. Завершение по реальным каналам

Git-only:
- применяются настоящие commit/integration/non-force push/remote confirmation;
- публикуется только разрешённый результат и допустимая исходящая история;
- no-change проверяет необходимое существующее состояние без пустого commit/push.

Local-only:
- достаточно разрешённого применённого и проверенного фактического результата;
- Git commit/SHA/push не требуются и не имитируются;
- ограничения локальной доступности и переносимости называются честно.

Mixed:
- отдельно проверяются Git-часть и локальные targets;
- частичный успех одного канала не завершает другой.

При task accounting краткий итог сохраняется, native exact close выполняется
отдельно после применимых критериев и fresh native predicates, затем отдельно
проверяется tracker publication. Для tracked local-only задачи отсутствие Git SHA
не препятствует verified completion. Публикация Dolt не является Git push
локальных файлов.

При реальном родителе Fast выполняет короткий child-based каскад основным
агентом через существующего владельца. Обязательного container-completion
субагента нет. Без родителя — no-op. На каждом уровне сохраняются полный
непустой direct-child set, все дети closed, parent blockers, native close/read-back
и отдельная tracker publication; остановка на первом неподходящем родителе.
Каскад не повторяет содержательную приёмку и не выполняет соседние задачи.

Подтверждённый remote Git отделён от разрешённого source-copy maintenance.
Применимые safe-FF guards и отдельный незавершённый maintenance debt сохраняются;
они не отменяют уже подтверждённую публикацию и не блокируют допустимые
exact close/Dolt по действующему контракту.

### 8. Ошибки, partial и recovery

На неоднозначном результате сначала сверяются фактические эффекты тем же владельцем.
Не повторяются подтверждённые create/push/close, не создаются новый ID/копия
ради обхода конфликта, не используется force/reset/stash или автоматический rollback.

Продолжение использует тот же ID, пригодную copy/branch, реальные Git/Beads/target
данные, доступные решения и применимые проверки. Handoff-файл не обязателен.

Потерянные необходимые воспроизводимые проверки повторяются адресно.
Independent review восстанавливается или честно проводится заново только когда
оно применимо/требуется; отсутствие не требовавшегося review не создаёт долг.
Известный adverse result или нарушение не исчезают из-за нового выбора маршрута.
Потерянное существенное решение нельзя выдумать.

Итог различает выполненные, неподтверждённые и оставшиеся эффекты по каналам;
называет конкретный блокер. Local-only не называется удалённо опубликованным.

### 9. Поставка, совместимость и исключения

Внутри этой фичи согласуются необходимые изменения Fast и общих owners/consumers,
нормативных product/rules/AGENTS, команды, README/catalog/help/status/next и
source/install. Нельзя вернуть безусловное ревью, Git SHA или closure-субагента
через publisher/completion/recovery/common instructions.

Вне этого Fast scope сохраняются полные feature-preparation, full task,
registered-bug, review и publication контракты. Прямой publisher не получает
общего разрешения обходить review. Самостоятельный direct review не отключается.

Не вводятся новые skill/command/task types, dispatcher, workflow engine,
readiness registry, обязательные отчёты или migration исторических данных.
Закрытые записи, исторические спецификации/решения и их provenance не переписываются.

Проверка инструкций: содержательное чтение, независимое ревью самой поставки
по действующему полному маршруту, затронутая статика, ссылки/dependencies и
source/install parity. Для исполняемых изменений нужны необходимые обычные
программные тесты с применимым TDD. Новые live/session/scenario tests поведения
агентов запрещены. Из текста или тестов программ нельзя обещать измеренные
ускорение, стоимость, надёжность либо повторяемость поведения.

### 10. Критерии приёмки

AC-001. Для явно выбранного /risp-run-simple-task и подходящего естественного
поручения описан один существующий Fast; пустой запрос не выбирает очередь.
Проверка: прочитать flow, command и тексты навигации/help.

AC-002. Допуск/отказ определяется последствиями, границами и проверяемостью,
включает code/config/docs/tools/ignored/external и не сводится к установке скилов
или размеру diff. Материальное расширение согласуется адресно.
Проверка: чтение обычного, неподходящего и уточняемого вариантов инструкций.

AC-003. Default route имеет одного основного агента, ноль субагентов и не требует
подготовительных стадий, файлов или передачи собственного контекста.
Проверка: пройти обязательные зависимости инструкций на бумаге.

AC-004. В RIS используется одна короткая ordinary Beads task с identity reuse,
достаточным поручением/критериями/решениями; claim/composition/blocker guards
сохранены. Существующие feature/bug/container не понижаются.
Проверка: чтение tracker branch и соответствующих adapter contracts.

AC-005. Versioned edits требуют одной собственной branch/worktree с reuse;
local-only использует реальные targets без пустой copy/фиктивного Git;
mixed сохраняет обе границы и чужие данные.
Проверка: чтение Fast worktree branch, preparer contracts и local/mixed flow.

AC-006. Самопроверка и обязательные проверки/TDD сохраняются; review условно
ровно по применимым основаниям и не становится обязательным из-за кода/Git.
При неактивной ветке нет review role/format load или отказного отчёта.
Проверка: чтение Fast, rules/common quality и обязательных consumers.

AC-007. Активное review действительно независимо; mandatory-unavailable и
существенные findings блокируют зависимое продвижение; repairs и changed
snapshot получают применимую переоценку. Без review нет фиктивного approval.
Проверка: чтение reviewer/publisher/recovery и risky/changed-snapshot веток.

AC-008. Git-only/local-only/mixed и no-change имеют разные применимые финалы.
Git сохраняет outgoing/integration/non-force/remote gates; local-only не требует
SHA и не выдаётся за push; partial mixed не называется завершённым.
Проверка: сквозное чтение Fast → publisher/adapter completion.

AC-009. Tracker result, exact close/read-back и Dolt publication остаются
отдельными действиями; tracked local-only completion поддержан без Git SHA.
Проверка: tracker/standalone/completion/publication contracts.

AC-010. При реальном parent Fast выполняет child-based каскад основным агентом
без обязательного closure-субагента, без parent — no-op; full/bug маршруты
сохраняют собственный fresh-subagent контракт.
Проверка: общий ancestor resource и оба вызывающих flow.

AC-011. Recovery сохраняет ID/copy/foreign work, сверяет uncertain effects и
не повторяет confirmed push/close; не требует handoff или неприменимого review.
Проверка: чтение прерванных Git/local/mixed/review/ancestor веток.

AC-012. Нормы, owners/consumers, command, bilingual help/navigation, README/catalog
и source/install согласованы без ослабления full/feature/bug/direct-review gates
и без переписывания исторических решений.
Проверка: affected reference search, link/dependency review и parity oracle.

AC-013. Поставка проверена допустимой статикой и независимым ревью по текущим
правилам; исполняемые изменения покрыты необходимыми обычными тестами.
Нет новых agent-behavior tests и недоказанных claims ускорения/надёжности.
Проверка: фактический diff, применимые check results и независимое review.

Ссылки на критерии: ris-ci3.1#AC-001 … ris-ci3.1#AC-013.
Нумерация и смысл сохраняются при дальнейших ревизиях.

## Технический дизайн D1

### 1. Версия, сущность и граница

D1 — предлагаемый дизайн против полного кандидата S1 выше; оба ещё не приняты.
Исходный код: 89af19ccc773cdf7548f559adbc959fa55799b13.

Сохраняем существующие навыки и инфраструктурные алгоритмы. Fast выбирает
применимые действия и держит один авторский контекст; preparer, publisher,
adapter, reviewer и container owner продолжают владеть своими результатами.

Два новых различения в существующих контрактах:
- review требуется или не требуется для конкретного допустимого Fast subject;
- результат Git-only, local-only либо mixed.

Это семантические входы/выводы существующих владельцев, не новый runtime,
persisted schema, state machine, dispatcher или registry.

Новых технологий, зависимостей, task types и slash-команд нет. Главный компромисс:
часть независимой проверки в подходящем Fast заменяется обязательной
самопроверкой; поэтому критичны честная классификация и отсутствие скрытого
возврата к безусловным gates.

### 2. Наблюдаемая исходная система

В skills/ris-proj-flow-execute-simple-task/SKILL.md уже есть прямое применение
owners основным агентом, достаточный request без spec/plan и тонкая команда.
Однако сейчас flow заранее требует task-review role, отдельный review launch,
Git-oriented publication/completion и delegated ancestor tail.

Его references/tracker.md, worktree.md и recovery.md содержат существующие
границы accounting, copy и recovery, которые переиспользуются.

skills/ris-proj-op-publish-task/SKILL.md содержит один общий алгоритм Git и
безусловный independent whole-snapshot gate. Его нельзя обойти только правкой Fast.

skills/ris-proj-adapter-beads-tasks/references/standalone.md и completion.md уже
владеют ordinary result/verified completion; их wording о revision/review нужно
согласовать с local-only и conditional review, не создавать новый close engine.

skills/ris-proj-flow-execute-task/references/ancestor-completion.md сейчас
требует fresh subagent и для full, и для Fast. Container predicates остаются у
ris-proj-op-complete-container и adapter.

Текущие общие нормы также требуют independent review; исключение должно быть
явно внесено в действующие нормативные тексты вместе с consumers.

### 3. Ответственность и направления зависимостей

Fast:
- устанавливает admissible bounded request, действительный kind и критерии;
- выбирает применимые output channels и review applicability по S1;
- применяет существующих owners и проверяет combined result;
- возвращает материальные решения человеку, а не принимает их сам.

Tracker resource → selected tasks adapter:
- identity/create/reuse, actor/claim, live guards, short result, exact close,
  отдельная publication;
- actual type/parent/edges/status остаются данными трекера.

Worktree resource → task/portable preparer → selected worktree adapter:
- только для действительно versioned Git edits;
- ordinary/local-only claim и target protection не требуют фиктивного worktree;
- existing preparers не начинают обслуживать произвольные внешние файлы.

Implementation → ris-port-op-implement-change:
- достаточное поручение, разрешённые фактические targets, выбранные mandatory
  checks/TDD; вне target-copy файлов действуют их реальные owner/config правила;
- docs operation применяется лишь для разрешённой документации.

Git → ris-proj-op-publish-task:
- получает проверенный versioned subject из prepared copy и conditional review
  basis; сохраняет единственный integration/outgoing/non-force/remote алгоритм.

Review → ris-proj-op-review-task:
- применяется и получает configured task-review role только при активной ветке;
- substantive assessment и independence остаются существующими;
- no-file Fast result допустим; optional save использует прежний format owner.

Ancestor tail → ris-proj-op-complete-container → adapter:
- один общий ascent/predicate/recovery контракт;
- Fast выполняет его основным агентом, full/bug — fresh configured recipient.

Common/context не классифицируют задачи и не начинают lifecycle сами.
Context разрешает только нужные настройки; shared-primary/workspace/roles
не запрашиваются без соответствующей операции. Настройки валидируются полностью.

### 4. Review contract без скрытого обхода или возврата

Решение о применимости review принадлежит Fast по S1, не publisher и не
форматному валидатору. Оно основывается на фактических правилах целевого проекта,
явном поручении и конкретном риске. В сессии достаточны выбранный scope,
существенные основания и текущая проверяемая версия; отдельного receipt,
skip-file, registry field или отказного отчёта нет.

Publisher допускает отсутствие review только для проверенного допустимого
Fast invocation, включая выбор естественным запросом, с неприменимостью всех
обязательных оснований. Произвольное "review not needed" от caller не выключает
общий gate. Прямые Documents, feature preparation, full task и bug publication
сохраняют обязательный независимый review.

Если review требуется, существующий whole snapshot/base/input/independence и
finding gate применяется полностью. Если не требуется, publisher всё равно
проверяет authority, target, full outgoing history, actual candidate, checks,
preservation и remote result, но не требует независимого approval.

При интеграции upstream/hook/doc changes:
- сверяются новый full snapshot, критерии, допуск Fast и риски;
- повторяются затронутые проверки;
- при required review выполняется независимая переоценка нового subject;
- при not-required review выполняется авторская самопроверка нового subject;
- новое обязательное основание включает review, выход за допуск возвращается
  человеку до зависимого push.

Common quality/artifacts, reviewer consumers и recovery используют этот же
scope. Утрата отсутствовавшего и не требовавшегося review не образует recovery
gap; известный adverse result не обнуляется классификацией.

### 5. Основные потоки и состояние

Versioned:
request → admissibility/accounting/claim → same own copy → edit/check →
conditional review/repair → common Git publisher → short result →
verified exact close → tracker publication → applicable ancestor tail.

Local-only:
request → admissibility/accounting/claim при нужном accounting →
inspect actual target/permissions/conflicts → edit/check target →
conditional review/repair → short local result → verified exact close →
tracker publication → applicable ancestor tail.
Git publisher/preparer не вызываются ради формы.

Mixed:
общие admission/claim и один author context;
versioned changes в own copy, local changes в реальных targets;
проверяются оба результата; Git публикуется общим owner;
task завершает свой обязательный результат только после выполнения обеих частей.
Remote publication и policy-required source-maintenance remainder учитываются
по прежнему отдельному контракту.

No-change:
проверяется фактическое достижение поручения; если нужен опубликованный Git
результат — его applicable checks/remote visibility; для local target — реальное
состояние. Пустых commit/push или invented SHA нет.

Durable work state: Beads ordinary request/result/status/edges и реальные
Git/target данные. Review/check evidence остаётся в доступной сессии либо
разрешённом существующем артефакте. Новый журнал не создаётся.
Local targets не становятся автоматически доступными другой машине:
tracker хранит достаточный краткий результат/проверку/ограничения, не секреты
или полную копию конфигурации.

### 6. Ошибки, конкуренция, повтор и completion

До каждой новой mutation batch свежо проверяются применимые ownership/status/
blockers и конкретные target conflicts. Branch/worktree/claim не изолируют
общую базу и внешние ресурсы и не обещают CAS.

Native tracker mutations остаются sandboxed; публикация — отдельной.
Completion consumes verified useful result и только применимые Git/review
обязательства. Для local-only passed criteria и actual-target evidence
заменяют неприменимую Git revision, но не проверку результата.
Это ordinary verified close, не administrative shortcut.

Частичная mixed задача не закрывается как выполненная, пока не завершены её
собственные обязательные части. Отдельный policy-required maintenance debt
сохраняет прежнее разрешение exact close/Dolt после подтверждённого remote Git.

Неоднозначные create/write/push/close возвращаются их инфраструктурному owner
для read/reconcile до retry. На resume не пересоздаются ID/copy и не повторяются
подтверждённые эффекты. Lost applicable checks повторяются адресно; required review
восстанавливается или проводится честно заново. Чужая работа не откатывается.

Общий ancestor resource разделяет admission/delegation caller и actual ascent:
Fast использует ascent в текущем контексте; full/bug сохраняет mandatory fresh
recipient. Ascent в обоих случаях вызывает того же complete-container owner
и не дублирует native CLI. Parent-close failure сохраняет leaf completion,
но остаётся явным combined remainder.

### 7. Изменяемые поверхности и совместимость

Основные:
- skills/ris-proj-flow-execute-simple-task/SKILL.md и его tracker/worktree/recovery;
- skills/ris-proj-op-publish-task/SKILL.md;
- adapter standalone/completion;
- общий ancestor-completion resource и его Fast/full callers;
- common quality/artifacts, review-task и другие непосредственные consumers,
  если их обязательное wording иначе восстанавливает отменённый gate.

Нормативная поставка:
- AGENTS.md, README.md, docs/development.md, docs/skills.md;
- затронутые product 01/06/07/08 и rules development/architecture owner map;
- command risp-run-simple-task;
- help owner, bilingual fixed pages в plugins/opencode/ris-help/pages/;
- show-plan/suggest-continuation только в части фактического Fast selection/
  recommendation, без нового dispatch table;
- соответствующая установка .opencode/skills, command и plugin pages.

Исторические accepted specs/evidence сохраняются. Текущие нормы явно ограничивают
новое исключение Fast, а не ретроспективно отменяют прошлые обязательства.
Existing YAML /1 и /2 не меняются и не мигрируются; validator не получает флаг,
подменяющий независимость. Набор ролей/config не расширяется: существующие
task-review/container-completion остаются для активных или full маршрутов.

Правки OKF product/rules выполняются их существующим владельцем с явно выбранным
bundle/root/scope, а не массовым Markdown replacement.

### 8. Test seams и способ проверки

Каждый seam проверяется на фактическом итоговом diff/версии, без agent sessions.

A. Admission/navigation seam — Fast, command, help/status/next.
Oracle: одинаковые допуск, отрицательные границы и естественный/явный выбор;
нет закрытого operation allowlist или size threshold.
Покрывает AC-001, AC-002, AC-012.

B. Mandatory-load/call seam — Fast main и conditional resources.
Oracle: ordinary path не требует reviewer/closure role, review format,
spec/plan/handoff или внутреннего нового executor.
Покрывает AC-003, AC-006, AC-010.

C. Accounting/isolation seam — tracker/worktree → adapter/preparers/context.
Oracle: same-ID/native-kind/claim/composition/blockers; versioned own copy;
local-only real target; shared-resource protection без фиктивного Git.
Покрывает AC-004, AC-005.

D. Quality/publication seam — Fast → publisher/reviewer/common.
Oracle: not-required и required ветки, mandatory-unavailable, findings/repair,
changed integrated snapshot; full/direct-doc/feature/bug gates не ослаблены.
Покрывает AC-006, AC-007, AC-008, AC-012.

E. Completion/ancestor seam — tracker → standalone/completion/publication;
shared ancestor resource → complete-container.
Oracle: Git/local/mixed/no-change channels различены; exact close/read-back/Dolt
раздельны; Fast inline/full delegated; native child/blocker gates сохранены.
Покрывает AC-008, AC-009, AC-010.

F. Recovery seam — прерывание до/после Git, local apply, exact close и Dolt.
Oracle: actual-effect reconciliation, same copy/ID, no confirmed replay,
потеря только необходимых checks/review, явный partial mixed.
Покрывает AC-011.

G. Delivery seam — references/frontmatter/dependencies/link/byte-type-mode parity,
билингвальные fixed help pages и затронутые обычные program tests.
Покрывает AC-012, AC-013.

Необходимая совместная проверка — содержательное независимое рассмотрение всей
цепочки A–G на одной integrated revision; это не live/scenario test агента.

Существующие deterministic test entrypoints:
- python3 -m unittest discover -s tests/package_installation -p 'test_*.py' -v;
- PYTHONDONTWRITEBYTECODE=1 RIS_TEST_BASH=/bin/bash python3 -m unittest discover
  -s tests/package_installation_integration -p 'test_*.py' -v;
- bash -n skills/ris-port-op-manage-installation/scripts/ris-install.sh;
- node --test tests/client_help/help.test.mjs для затронутых fixed pages.

Применимость и достаточность каждого запуска проверяет исполнитель по diff и
действующим правилам. Если меняется исполняемый механизм, к нему добавляются
содержательные regression tests с применимым TDD. Никаких новых live/session/
scenario agent tests. Не требуется новая test harness или validator dependency
ради instruction-only изменения; недоступная обязательная проверка не становится pass.

### 9. Зависимости, риски и решения

Внешнего implementation prerequisite от ris-ci3.2 нет. Общие файлы сами по себе
не создают blocks. ris-ci3.2 владеет изменением inherited acceptance и облегчением
feature preparation; D1 его не реализует и не потребляет ещё не согласованный
контракт. При фактическом upstream изменении общих contracts проверяется только
затронутая совместимость.

Материальные риски:
- безусловное review возвращается через общий publisher/rules/recovery;
- слишком широкое исключение выключает full/feature/bug gates;
- local target ошибочно переносится в недействующую worktree-копию;
- local-only completion требует фиктивный Git SHA или mixed закрывается частично;
- общий ancestor resource возвращает обязательного Fast-субагента;
- тексты source/install/help расходятся.

Защита: один Fast-owned applicability decision, явные scoped consumers,
неизменённые инфраструктурные владельцы, seams A–G и независимое ревью поставки.

Содержательное изменение границы Fast и review/completion obligations требует
точного принятия S1/D1. Отдельный ADR не нужен: достаточное решение сохраняется
в acceptance области этой спецификации без дублирующего артефакта.
Новых труднообратимых форматов или миграций нет.

Существенных неразрешённых вопросов для показа этих кандидатов не выявлено.
S1/D1 — предложения до решения человека, не действующие изменённые правила.

## Принятие S1 и D1 — 2026-10-26

Это отдельная область фактического решения, не часть content selectors S1/D1.
Полные тексты кандидатов выше сохранены без изменения, включая формулировки
«ещё не приняты»: они отражают статус на момент показа кандидата, а не статус
после приведённого здесь решения. Действительное принятие обоих scopes — ниже;
принятие спецификации не означает реализации или изменения действующих правил.

Acceptor: Aleksei Slivka, пользователь проекта RIS.
Decision date: 2026-10-26.
Decision provenance: текущий диалог полного ris-proj-flow-prepare-feature для
ris-ci3.1. Ведущий показал доступный полный кандидат и точно спросил о принятии
обоих полных scopes: «Требования S1» (включая AC-001–013) и «Технический дизайн D1».
До вопроса были раскрыты сущность дизайна и риски. Ответ пользователя: «Принимаю.».
Этот один attributable акт явно относится к обеим независимо различимым
областям/версиям. Атрибуция и точный scope решения переданы ведущим автору
ограниченного accepted-local-save; автор не принимал содержание за человека.

### Решение о требованиях S1

- path: docs/specs/ris-ci3.1/spec.md
- section: Требования S1 (полный раздел со всеми подразделами и AC-001–013;
  до следующего H2 «Технический дизайн D1»)
- version: S1
- revision: containing-commit
- decision: accepted
- acceptor: Aleksei Slivka
- date: 2026-10-26
- basis: общий акт «Принимаю.» с приведённой выше provenance, отдельно принимающий S1.

### Решение о дизайне D1

- path: docs/specs/ris-ci3.1/spec.md
- section: Технический дизайн D1 (полный раздел со всеми подразделами;
  до следующего H2 «Принятие S1 и D1 — 2026-10-26»)
- version: D1
- requirements: docs/specs/ris-ci3.1/spec.md, section Требования S1, version S1,
  revision containing-commit; решение «Решение о требованиях S1» этого раздела принятия.
- revision: containing-commit
- decision: accepted
- acceptor: Aleksei Slivka
- date: 2026-10-26
- basis: тот же общий акт «Принимаю.» с приведённой выше provenance, отдельно принимающий D1.

Immutable Git addresses пока не назначены: сохранение локальное, без commit/push.
После публикации containing-commit разрешается от исходного immutable адреса
соответствующего решения в этом документе; последующая неизменённая копия
решения не возобновляет принятие и не перепривязывает исходную ревизию.
