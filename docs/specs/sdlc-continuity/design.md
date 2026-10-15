# Сквозная связность RIS — дизайн-кандидат D1

**Статус: proposed, не принят.** Разрешены подготовка/review/публикация кандидата,
не реализация. [Требования v1](spec.md), [решения](acceptance.md),
[фактический аудит A1](audit.md). Baseline `2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae`.
Имена существующих owners ниже относятся к baseline; naming `ris-1fq` идёт отдельно.

## 1. Минимальная архитектура изменения

Сохранить project operation → portable method + common/context + selected adapter.
Изменить существующих предметных owners, добавить только самостоятельную
read-only навигацию. Ей не нужна portable base: результат зависит от реального
RIS-проекта, выбранного трекера, доступного пакета и текущих результатов.
Никакого собственного scheduler, state store, handoff schema или глобального
runtime registry. Состояние — у tracker/Git, локальное evidence — по project conventions.

| Область | Предлагаемый owner / изменение |
|---|---|
| Обнаружение project/primary/settings | ris-context: проверяемые входы/diagnostics, не выбор стадии; bounded восстановление primary из уже доступного подтверждённого association |
| Общий восстанавливаемый итог | ris-common/references/artifacts.md: достаточность адреса/версии/решения/каналов, без обязательного next-skill prompt |
| Standalone постановка/декомпозиция | ris-specify-feature, ris-design-feature, ris-decompose-feature: различимые feature-record и standalone branches, без механической миграции существующих records |
| Git публикация | Расширить ris-publish-main на разрешённый document/change subject, включая до-ID, без обязательного implementation evidence для чисто документального subject |
| Tracker publication | Выбранный adapter: существующий dolt.publish и полный outgoing scope; не встраивать SQL/Git алгоритмы в планировщики |
| Pre-ID independent review | ris-review-base для конкретного document subject; task-bound ris-review при наличии применимого ID |
| Прямые finished planning operations | Roadmap/epic/specify/design/decompose вызывают publication owner в нужной точке; явно limited component contribution сохраняется |
| Task delivery | prepare-task-worktree/plan-task/TDD/docs/review/publish и execute-task сохраняют собственные owners/guards; child closure не ищет parent closure |
| Container verification/closure | ris-complete-container: добавить самостоятельный task-container branch; не требовать feature payload там, где scope подтверждён обычной записью |
| Ручное продолжение | Один новый project read-only skill, рабочее proposed имя `ris-proj-op-suggest-continuation`; команда одноимённа после принятия D1 и проверки actual namespace |
| Authoring/static review | ris-author-skills и portable author проверяют contract sufficiency; не добавляют common/Beads в portable targets |

Новое имя выше — **кандидат, не установленная команда**. Применяет принятую naming
схему; не вводится в текущую карту 41/37 задним числом. Не добавлять отдельный
publisher только ради симметрии: reuse существующих двух каналов предпочтителен.

## 2. Вход и восстановление по идентичности

Direct task-bound invocation получает ID; project определяется cwd/instructions,
config — по context, tracker — selected adapter. Через точное чтение получить
type/key/content/spec links/current composition/blockers и материализовать только
релевантные refs. Проверить версию/acceptance/applicability. Ссылки в ребёнке
достаточны для собственного scope; чтение parent может проверить currency/состав,
но не определяет вместо ребёнка его критерии и не даёт права закрыть parent.

В feature-record branch сохраняются current payload/immutable refs и строгие
checks; historical payload не переписывается. В standalone branch использовать
обычную record content и точные источники/решения без feature JSON; для simple
task достаточно accepted constraints, не искусственного design файла. Для
многозадачной поставки требуется достаточный независимо принятый дизайн там,
где он материален. Adapter operations проверяются по actual capability; common
tasks v1 не расширяется до tool-specific standalone create/reparent скрыто.

Primary можно восстановить лишь при проверяемом однозначном project/repository
association и существующем адресе shared workspace из task evidence/инструкций;
Git main worktree или имя ветки сами по себе не доказательство. Explicit input
имеет приоритет. Неоднозначность/foreign association блокирует shared-path часть.
Выбранная copy проверяется current facts, не создаётся consumer-скилом.

Для interrupted preparation до task ID брать уже разрешённые document/candidate
addresses и известную идентичность scope. Не писать unaccepted candidate в accepted
path. Если сохранение разрешено, caller сохраняет существенные решения в имеющемся
подходящем артефакте; иначе возвращает несохранённый результат и recovery gap.
Обязательного нового draft store нет. Это не обещание восстановить утраченный чат.

## 3. Публикационные границы

Планировщик владеет semantic outcome/acceptance и вызывает publisher с exact subject,
evidence/decision addresses, channel, destination из project evidence и allowed
effects. Это смысловой handoff, не новый YAML API. Publisher возвращает проверенные
revision/ref/remote/effects/limits; вызывающий проверяет применимость и целое.

| Операция | Finished direct | Явно limited contribution |
|---|---|---|
| Roadmap/epic refinement | Проверенные tracker writes + tracker publication, если были изменения/остался публикационный долг выбранного scope | Proposal либо проверенная локальная запись с явной local boundary |
| Specify/design | Saved accepted content/decision → Git publication → record create/update при необходимости → tracker publication | Formulate/save exact accepted candidate; no hidden task create/push |
| Decompose | Ready inputs → verified one-task result либо writes → publication новых/оставшихся tracker effects | Proposal/read-only verification либо явно разрешённые local writes |
| Prepare-feature scenario | Coordinated component contributions → independent document review → Git → feature record → tracker read-back | Компонентам передаётся точная ограниченная цель, сценарий удерживает transitions |
| Leaf cycle | Local plan/change/docs/review → approved Git owner → exact leaf completion → tracker publication | Каждый компонент заканчивает своим вкладом; произвольная вложенность не publisher mode |

No-change проверяет существующую пригодность/нужную опубликованность, но не
создаёт пустой commit/push. Git/трекер evidence независимы. Ошибка Git останавливает
зависимую record запись; ошибка tracker после Git сохраняет Git и продолжает
только missing operation. Unknown push сверяется до повтора. Publisher не принимает
контент и не закрывает задачу; planning permission не разрешает unknown history.

Для pre-ID документов Git owner принимает предмет/проверенные inputs без фиктивного
task ID и без требования ещё не существующего дизайна к requirements-only publication.
Не ослаблять complete snapshot/independent review/preservation/outgoing/remote gates.
Ни spec/design, ни scenario не получают собственную копию Git/Dolt алгоритма.

## 4. Завершение standalone-контейнера

Вход: exact ID/kind, отдельно разрешённое закрытие, accepted mandatory outcomes/
состав, предметные refs/criteria и integrated evidence. Feature-record branch и
epic branch сохраняются. Новая standalone task-container ветка не определяется
по одному отсутствию детей: вид и назначение подтверждаются записью/источниками.

Применить portable verification к достаточным explicit feature-like inputs, если
предмет имеет общие AC; для иной bounded composition оценить её собственные
outcomes и evidence. Не навязывать всем task одну SHA или feature schema. Persist
результат через actual adapter, с защитой нужных predicates; отдельно exact-ID close.
Дети/блокеры свежие и полные, cancellation требует scope disposition. Полнота
существования обязательного состава проверяется отдельно от native close guard.
Не открывать/закрывать родителей/детей для получения удобного статуса.

## 5. Read-only навигация

Самостоятельный результат — рекомендация, не выполнение. Direct input: task/
container ID; до ID — явный source/scope locator. Cwd/project config применяются
обычно. Не invent ID из title, не брать latest session или соседний task молча.

1. Прочитать current record и relevant sources/evidence; определить желаемый
   уровень работы: выбранная задача/подготовка/контейнер, не весь backlog.
2. Проверить, есть ли proven unfinished scenario/operation. При доказанном
   scenario remainder рекомендовать его resume; его recovery сам определит
   missing stage. Не выбирать child вместо явного ID без нового поручения.
3. Если результат закончен, сопоставить следующий нужный результат с реально
   доступными описаниями/контрактами. Загружать только подходящие кандидаты,
   не весь набор методик. Контракты владельцев остаются источником истины;
   краткая карта SDLC — ориентир, не вторая независимо изменяемая процедура.
4. Выдать один обоснованный prompt, либо существенные варианты с необходимым
   решением. Не заявлять полную readiness без проверки executing owner. При
   incompatible owner/handoff дать blocked и exact gap, не обходной алгоритм.

Нулевые project/tracker/Git writes; не claims/acceptance/push/closure/launch.
Нет execution role по умолчанию: прямой read-only вызов самостоятельный.
Subagent invocation возвращает recommendation вызывающему, не управляет им.

Примеры формы (не свидетельство текущей готовности): `Выполни ris-plan-task для
ris-1fq` — только при установленном имени и подходящем scope; `Продолжи
ris-execute-task для ris-1fq` — только при доказанном unfinished execution.
Во время naming migration имена заново читаются, историческая строка не executable
authority. До установки нового navigation skill никакая slash-команда здесь
не является реальным входом. Блокировка честнее fake prompt.

## 6. Адресные изменения норм и потребителей

Нормативная модель — docs/concepts/01,03,04,06,08; рабочее общее handoff —
ris-common/artifacts, context paths — configuration resource. Сохранить запрет
назначать next skill в атомарных wrappers, уточнить исключение для самостоятельного
рекомендательного результата навигации и сценариев. Общая норма не должна
перечислять все installed skills или превращаться в dispatch table.

Owners из §1 получают только свою ответственность и conditional resources.
Scenario prepare-feature заменяет generic публикационный алгоритм явным owner;
execute-task сохраняет проверку route/receipts, recovery не дублируется в навигаторе.
Standalone decomposition проверяет children собственной достаточности до записи.
Documentation/source/install/commands меняются совместно в будущей реализации;
реальные concepts/rules бандлы требуют project OKF owner с explicit root/scope,
обычные spec/design им не становятся.

## 7. Static seams и покрытие AC

| AC | Статический oracle и адрес ответственности |
|---|---|
| 001–002 | Direct short-call contract у task-bound owners: discovery из ID, mandatory inputs/readiness и exact diagnostics; explicit exceptions не универсальная анкета |
| 003–005 | Feature vs standalone modes decompose/complete, child contract/parent guards, full membership/outcome trace; отсутствие artificial records/recursive closure |
| 006 | Common artifacts + отчёты всех затронутых owners: discoverable result/version/decision/channel, nested return, no next-skill assignment |
| 007,014 | Navigation main/description/command: real locator/owner, read-only, unfinished vs next vs blocked; no stale names/refs or fake readiness; portable exclusions preserved |
| 008–010 | Direct/limited table §3 → actual calls to publisher/adapter, receipt use, full-vs-local status; leaf components без промежуточного push |
| 011–013 | Producer partial output → same consumer required inputs, actual-effect reconcile, fresh guards, changed acceptance/evidence handling; closed pending route без reopen |
| 015 | Все строки audit §3 + scenario chains §4 проверены в обоих направлениях; каждая самостоятельная стадия применяет владельца, условия его входа и stop |
| 016 | Metadata/name/resource/link checks, command $ARGUMENTS/one target, source-install manifest/bytes/modes; affected OKF norms and independent full-snapshot review |

Для каждой существенной строки ручная матрица success/partial/interruption/revision
плюс direct/component: declared output + storage/discovery + acceptance/publication
→ mandatory input + current guards + owner + stop. Один grep не подтверждает
семантику. Детерминированные проверки формата/ссылок допустимы, но agent tests,
сценарные сессии и новые harness не пишутся/не запускаются. Static evidence не
выдаётся за live behavior. Необходимость иных проверок возвращается на отдельное
согласование, а не добавляется скрыто.

## 8. Impact, альтернативы и продолжение

Naming D1 принят и реализуется отдельно в ris-1fq. Эта подготовка не меняет его
карту/AC и не добавляет blocker чужой задаче. В будущей реализации установить
actual package baseline: если naming уже опубликован, использовать новые имена
и mapping; если нет — согласовать порядок и при необходимости реальную dependency
после подтверждения implementation IDs. Не поручать ris-1fq функциональные правки
этих контрактов: его AC-011 сохраняет алгоритмы/права. Installer N1 не меняется.
Новый navigation source не входит в исторические 41/37; установка учитывает
актуальный пакет и принятый naming contract. Конкретная Gas City integration
не исследована и не заявляется поддержанной; никаких её APIs/ролей не выдумывается.

Отвергнуты: обязательные next prompts во всех атомарных owners (coupling),
универсальный SDLC orchestrator/registry (не нужен для результата), обязательный
Beads для portable/no-ID операций, копирование publisher/recovery в навигатор,
автоматическое принятие D1 и создание реализации на основании этой публикации.

До реализации отдельно предъявить и принять D1, затем определить минимальные
проверяемые единицы и необходимые зависимости. Этим документом implementation
tasks не созданы. Подготовку ris-bxc можно завершить по её собственным критериям,
оставив D1 proposed; новая сессия читает его по published references из ris-bxc.
