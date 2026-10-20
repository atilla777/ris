# Дизайн упрощённого SDLC

Версия: **D1**, 20.10.2026. **Принята пользователем, не реализована.**
Вход — принятая [S1](spec.md). Подготовка — ordinary `ris-b1a`.
Точное основание и область решения: [принятие S1/D1](acceptance.md).
Baseline: `b0567574f973560075afc08de267c3c9564bbae5`, Beads 1.3.1.
Всё устройство ниже — предложение, а не описание действующего RIS.

## 1. Суть решения

Оставить существующих предметных владельцев и изменить их стыки:
ранняя feature-запись → её worktree → один диалог требований/дизайна →
точное согласование → независимое review → Git-публикация → обновление той же
записи → existing decomposition → отдельная публикация трекера.
Реализация задачи начинается у исполнителя без planner и implementation-report.
Независимый reviewer оценивает результат; project wrapper сохраняет полный YAML.
Новых skills, адаптеров, workflow engine, registry или CLI не требуется.

Главные изменения публичного контракта: `tasks.feature-record/2`,
один акт принятия двух различимых областей, конец prepare после декомпозиции,
новый формат review и удаление active plan-task contracts. Цена — необходимость
одновременно обновить зависимые инструкции и точные unsupported diagnostics.
Локальные review остаются локальными: это сознательно не distributed archive.

## 2. Владельцы и композиция

| Владелец | Предлагаемая ответственность |
|---|---|
| `ris-proj-flow-prepare-feature` | Ранний учёт, единый диалог/согласование, переходы, reuse, достаточность совокупного результата до decomposition/tracker publication |
| `ris-proj-op-interview-feature`, portable interview/spec/design | Существующие самостоятельные методики и coverage; без второй копии алгоритмов в flow |
| `ris-proj-op-specify-feature` | Project requirements/identity/source reconciliation; early registration как явно ограниченная ветка без фиктивных published refs |
| `ris-proj-op-design-feature` | Достаточный дизайн и отдельная адресуемая область, scoped acceptance/save/update; принимает собственную часть общего решения |
| tasks adapter | Единственный owner encoding /2, create/read/update/verification/complete и родственных native guards/read-back; отдельная Dolt publication |
| `ris-proj-op-prepare-task-worktree` + portable prepare + выбранный worktrees adapter | Подготовка копии для feature preparation либо execution с разными readiness gates; без дублирования Git/wt алгоритмов |
| `ris-proj-op-decompose-feature` + portable base | Существующая полная методика, one-task/multi-task reconciliation/coverage; одинаково при direct/flow вызове |
| portable implement + `ris-proj-op-implement-task-tdd` | Актуальные входы/код/подход, code/tests/authorized docs, обязательный TDD проектной обёртки; нет report persistence |
| portable review + `ris-proj-op-review-task` | База: независимая содержательная оценка; обёртка: project inputs и YAML save/формат, не процессный аудит имплементатора |
| `ris-proj-op-publish-task`, completion/verify owners | Прежние final-snapshot, integration, remote/primary sync и отдельные acceptance/close guarantees |
| common/context | Общие границы, acceptance evidence и recovery honesty; проверенные settings/paths. Не выбирают lifecycle, не хранят второй реестр |

Подготовка и исполнение используют ведущего и пригодных исполнителей гибко,
без обязательной отдельной сессии для каждой операции. Полезный существующий
контекст реализации/исправлений переиспользуется. Независимое ревью обязательно
в действительно отдельном от всех авторов/исправителей контексте. Имена ролей
сохраняются для явно делегированных операций; не требуют запуска неиспользуемой
роли. Изменение не распространяется автоматически на несвязанные flow, например init.
Project wrappers сохраняют direct вызов и не назначают следующий stage;
совокупные переходы остаются у flow/caller. Новая portable/project пара не нужна.

## 3. Ранняя запись: `tasks.feature-record/2`

Несовместимая семантика получает новую capability `tasks.feature-record/2`,
schema и literal markers `ris.feature-record/2 begin/end`. Native type остаётся
`task`, не Beads `feature`. Родительский epic может отсутствовать; при наличии
проверяется настоящий parent-child. Предлагается не добавлять его копию в payload.

Сохранить ровно прежние шесть top-level полей:

```json
{"schema":"ris.feature-record/2","slug":null,"spec_path":null,"requirements":null,"design":null,"verification":null}
```

- `slug` и `spec_path`: либо оба null, либо согласованная непустая пара.
  Пара закрепляется один раз перед первой записью документов после collision
  checks; затем неизменяема. Название, ID и worktree не переименовываются.
  Не вводится временный slug. Даже если документы исчезли, закреплённая пара
  не переиспользуется для другой фичи.
- `requirements`, `design`: null или прежний published ref
  `{path, revision, section, acceptance:{address, decision:"accepted"}}`.
  Non-null требуют закреплённой пары и проверенных настоящих документов/решения.
  Ref path может указывать разные непересекающиеся области одного spec.md.
  Requirements соответствует spec_path; design принадлежит согласованным
  документам этой фичи. Design без requirements не записывается как готовый input.
- `verification`: null или прежний содержательный результат integrated verification,
  с точными /2 accepted refs, SHA, полным AC set, integration/architecture/docs
  outcomes/evidence и limitations. Любое изменение accepted ref сбрасывает его
  в null, если отдельно не получен новый применимый verification.
- Ни draft refs, ни acceptance flags до принятия, ни history, phase/ready поля
  не добавляются. Git хранит историю принятых документов и решений.

До ID используется устойчивый ключ поручения (existing external_ref mechanism),
а не заголовок. Для create/reuse: полная all-status проверка относящихся key,
известных slug/spec и historical collisions → native create → exact read-back
и повторная collision проверка. Недостаток спецификации не блокирует раннюю
регистрацию; недостаток прав/identity блокирует запись. Несколько совпадений —
conflict с известными ID. Strict uniqueness не обещается и global lock не нужен.
Неоднозначный create сначала сверяется, никогда не повторяется вслепую.

`tasks` v1 сохраняет ordinary операции. Его feature-specific требование published
spec/epic переносится в зависимый /2 readiness gate, а не применяется ко всем task
create. Ранний feature create заявляется явно как /2 capability, не ordinary fallback.
Опциональное добавление epic позже — отдельно разрешённая existing structure
операция; не скрытый побочный эффект обновления requirements.

Политика ris-e26 остаётся: после поставки новый operational контракт поддерживает
только /2; /1 и иные исторические формы читаются как unchanged historical/unsupported,
без auto migration, repinning, fallback или создания копии записи. Все текущие
feature records на исследованной базе закрыты; единственная open task — ordinary
`ris-b1a`. Это наблюдение 20.10.2026, не гарантия будущей очереди. Перед rollout
нужно свежо проверить появившуюся работу; непредусмотренный material impact вернуть
пользователю, не мигрировать молча. Administrative exact status-only close сохраняется.

### Вычисляемые допуски

| Операция | Достаточные основания, помимо собственных прав/identity guards |
|---|---|
| Ранний учёт | Явно выбранная фича, цель/название/устойчивый ключ; известный epic проверен, неизвестный не выдуман |
| Worktree подготовки | Exact ID, открытая собственная preparation work/claim, допустимые подготовительные действия и safe copy; accepted refs не требуются |
| Документы | Проверенная собственная копия, закреплённые пути, write scope; черновик явно не принят |
| Декомпозиция | Опубликованные применимые принятые requirements + sufficient design, test seams/constraints и разрешённые blocker conflicts |
| Исполнение leaf | Собственный достаточный task scope, принятые inputs, integrated prerequisites, claim/свежие blockers/copy и проверки; не наличие plan/report |
| Verified completion | Прежняя полная integrated criterion/composition verification и exact native close guards |

`design:null` означает отсутствие принятого достаточного дизайна, а не отсутствие
design.md. Короткий дизайн ссылается на различимую принятую секцию spec.md.
Status/next обнаруживают ранние /2 records и называют первый реальный пробел;
наличие ID, closed children или файла само по себе не даёт readiness.

## 4. Worktree, единое согласование и подготовка

Wrapper подготовки копии различает purpose `feature-preparation` и `execution`
как семантический вход, не новую config/machine state. Первый не требует spec/
design и не трактует блокер исполнения автоматически как запрет выяснять
требования: проверяется, какое именно подготовительное действие он запрещает.
Реальный блокер выбранного действия не обходится. Сохраняются открытая работа,
actor/claim, отсутствие чужого исполнения, association и сохранность ресурсов.
Обычные execution blockers/gates не ослабляются. Portable owner и Git/Worktrunk
адаптеры не получают feature schema или роли трекера.

По подтверждённому ID используются существующие naming/paths; при reuse текущая
ассоциация и состояние проверяются заново. Создание/публикация документов — в
одной копии подготовки. Setup/hook failures оставляют точные эффекты и тот же ID;
нет повторного setup/создания/удаления по отсутствию журнала.

Flow применяет совместно существующие методики и показывает полный кандидат.
Общий акт принятия содержит acceptor/provenance и список двух content selectors:
requirements и design, каждый с path/section/version и decision accepted.
Один человек/сообщение/decision section может принять оба, если оба явно названы.
Project wrappers проверяют свою область того же решения; не требуют нового
человеческого подтверждения только из-за своего отдельного вызова.

Новая обязательная acceptance-file/schema не вводится: обычная decision section
в согласованном документе достаточна. Прежний immutable Git locator и проверка
content/section/revision сохраняются; `containing-commit` разрешён только в
decision для одноимённого commit, в tracker всегда full published SHA.
Позднее копирование решения не обновляет принятие. Ref двух областей может
указывать один decision address, но каждая область обязана явно входить в решение.

Independent review и publisher получают точный полный subject. После verified Git
publication обновляются refs той же записи; затем existing decompose получает
ID, принятые версии и действующие ограничения. Он возвращает one-task result либо
проверенные child records/blocks, не Markdown backlog. Limited local-write вклад
используется явно, а flow владеет единственной необходимой итоговой tracker
publication; standalone decompose сохраняет full default с собственным publisher.
Раннюю запись можно отдельно публиковать до готовых документов при разрешении:
published existence не означает published acceptance. Дополнительный обязательный
push после каждого вопроса/действия не вводится.

## 5. Удаление plan и implementation-report

Сопоставление planner и implement методов на baseline показало: outcome/scope,
текущий код, interfaces/constraints, критерии→тесты, локальные решения, material
revision, минимальный decisive probe, affected checks и честные limits уже есть
в `ris-port-op-implement-change`. Добавить только компактную явность выбора
подхода в актуальном коде и проверки достаточности входов без plan. Не переносить
ordered steps, plan-readiness, alternative sections и persistence.

Предлагается вывести `ris-port-op-plan-task`, `ris-proj-op-plan-task` и
`/risp-plan-task` из active source/install/catalog/help. После переноса отдельной
обязанности у них не остаётся: продуктовая декомпозиция, feature design и
implementation остаются у своих владельцев. Это D1 proposal, не выполненное
удаление и не повод удалять исторические specs/отчёты/принятия. Old plans можно
читать добровольно; их отсутствие/устаревание не создаёт новый planning stage.

Убрать сохранение и ожидание implementation.md у producers/consumers. Не переносить
его поля в review/Beads/новый файл. Существующие обязательные итоговые gates остаются
собственными проверками их владельцев. Review.yaml содержит выводы и проверки
reviewer, а не скопированный отчёт имплементатора. Краткий tracker result не
расширяется в промежуточный implementation log.

Требования TDD остаются у исполнителя: ожидаемый RED до production edit, GREEN,
регрессии и запрет выдавать test-last за TDD. Не предписывается обязательное
сохранение хронологии циклов в отчёт или её аудит reviewer/recovery/publication.
После interruption исполнитель исследует текущий код/тесты, продолжает недостающую
работу и запускает нужные проверки; отсутствие старой истории RED не блокирует
приёмку итогового результата и не разрешает заявлять доказанное прошлое TDD.
Реальное известное нарушение обязательного правила не скрывается и не становится pass.

Recovery не требует plan/implementation report, не реконструирует их и не
создаёт замены. Git/Beads/remote факты и существующий independent review нужны
для соответствующих собственных эффектов, а не чтобы восстановить прежний журнал.
Текущие проверки можно повторить при необходимости; утраченный review получить
заново. Unknown effect требует investigation до replay; это не требование вести
процессный лог или сохранять сведения о каждом шаге.

## 6. Review YAML: предлагаемый контракт `ris.review/1`

### 6.1. Размещение и владение

Единый owner сериализации/типов — ресурс `references/report-format.md` существующего
`ris-proj-op-review-task`. База владеет содержательной оценкой и возвращает
семантический результат; wrapper не навязывает ей RIS paths/schema/config.
Ресурс доступен всем project producers/consumers, не копируется в common/flows.
Сам формат не содержит Gas City roots/attempts/metadata и пригоден для внешней
программы. Начальный профиль привязки ниже — Git; это не делает Git обязательным
для самостоятельного переносимого ревью вне данного project save-контракта.

По умолчанию `workspace.tasks/<ID>/review.yaml` в context-checked primary.
Без ID — явный разрешённый local path, без выдуманной задачи. В Beads адрес
содержит путь и round selector; публикация tracker может переносить этот адрес,
но не содержимое или verdict. Локальная недоступность на другой машине честно
ограничивает reuse. Fast может оставить результат в сессии без сериализации;
если файл отдельно запрошен, используется тот же формат, не другой review.md.

Один файл содержит `schema`, `work`, `rounds`. Каждый round — полный независимый
результат; предыдущие rounds не переписываются как исправленные/approved. Новое
review добавляет round после свежего сравнения/сверки истории и read-back;
конфликт writers не разрешается overwrite. Частично записанный/непарсируемый файл
не даёт gate. Не вводится отдельный boolean passed, latest verdict или копия в Beads.

### 6.2. Типы и правила

YAML 1.2, один UTF-8 документ, mapping keys — строки. Запрещены duplicate/merge
keys, aliases/anchors, custom tags; scalar types только string, boolean, integer,
null, плюс arrays/mappings. Неявное преобразование неизвестных полей запрещено:
фиксированные mappings имеют ровно объявленные keys. Пустые обязательные строки
и неизвестные enum/schema отклоняются. Крупные пояснения — block strings YAML.
Все перечисленные ниже поля обязательны; отсутствие значения разрешено только
там, где явно указан null. Внешние evidence не становятся достоверными от
валидности YAML.

| Mapping | Поля и типы |
|---|---|
| root | `schema`: literal `ris.review/1`; `work`: Work; `rounds`: непустой массив Round |
| Work | `project`: непустой repository/project locator; `id`: string или null для no-ID; `scope`: непустая строка |
| Round | `id`: уникальная непустая строка; `previous`: ID предыдущего round или null; `created_at`: строка RFC3339 с timezone; `purpose`: `analysis` или `publication`; `snapshot`: Snapshot; `inputs`: массив Input; `provenance`: Provenance; `coverage`: непустой массив Coverage; `checks`: массив Check; `findings`: массив Finding; `dispositions`: массив Disposition; `summary`: непустая строка; `verdict`: enum; `limitations`: массив Limitation |
| Snapshot | `repository`: locator; `object_format`: `sha1` или `sha256`; `tree`: полный Git tree OID; `base`: полный commit OID или null; `exclusions`: массив Exclusion |
| Exclusion | `path`: точный repository-relative path; `reason`: непустая строка |
| Input | `role`: строка; `address`: строка; `version`: строка; `status`: `accepted`, `observed` или `proposed` |
| Provenance | `reviewer_context`: строка; `authors`: массив уникальных context/actor IDs; `invocation_evidence`: адрес или null; `independence`: `confirmed`, `unverified` или `self`; `basis`: непустое пояснение |
| Coverage | `area`: `requirements`, `architecture`, `rules`, `correctness`, `tests` или `docs`; `basis`: строка; `outcome`: `pass`, `fail`, `unverified` или `not_applicable`; `evidence`: массив строк-адресов; `reason`: строка |
| Check | `id`: уникальная строка; `description`: строка; `required`: boolean; `outcome`: те же четыре enum Coverage; `snapshot_tree`: полный OID; `evidence`: массив строк-адресов; `reason`: строка |
| Finding | `id`: устойчивая строка; `severity`: `high`, `medium` или `low`; `status`: `open` или `resolved`; `location`: строка с файлом/символом/областью; `summary`, `basis`, `required_change`: непустые строки |
| Disposition | `finding_id`: существующий ID; `decision`: `fixed`, `not_a_defect`, `deferred` или `accepted_recommendation`; `basis`: непустая строка |
| Limitation | `description`: непустая строка; `blocks_approval`: boolean |

Git OID — lowercase hex длиной 40/64 по object_format, не branch/tag/short SHA.
Repository locator разрешает нужный local repo/object store; абсолютный путь не
считается переносимым remote guarantee. Tree связывает полное проверенное дерево,
включая unchanged base, additions/deletions/content/modes. WIP не подменяется HEAD:
его точный prospective tree устанавливается существующим snapshot owner без
изменения пользовательского index/worktree; автор отчёта не создаёт snapshot
коммит только ради ревью. Незакоммиченный объект сам по себе не является backup;
при потере объекта reuse требует восстановить точный subject либо новое review.

Exclusions объявляются до review. Для dirty tracked exclusions tree сохраняет
base bytes/modes, а не исключает tracked файл из будущего commit. Указанный tree
сравнивается с фактическим полным публикационным деревом. Saving report в ignored
local area не меняет subject. При невозможности однозначной привязки gate blocked.

Правила round:

1. `rounds` — хронологический массив добавлений; `previous` ссылается на
   непосредственно предыдущий элемент того же work, без forks/cycles;
   первый round имеет null. Existing IDs не перенумеровываются.
2. Переоценка сохраняет IDs прежних findings и содержит их текущие статусы/решения.
   Новому дефекту — новый ID; resolved требует Disposition от reviewer с основанием.
   High/medium нельзя закрыть простым `deferred`; исправление автора не меняет
   прошлый round. Low допускают коллективное решение в prose, при необходимости
   dispositions указывают соответствующие stable IDs.
3. Coverage включает ровно по одному результату каждой из шести областей;
   `fail`/`unverified` несовместимы с approved, not_applicable требует конкретного
   основания. Publication inputs идентифицируют применимые требования/правила и
   дизайн где он нужен; их отсутствие нельзя скрыть `not_applicable`.
4. Required Check с `fail`/`unverified` блокирует approval. `not_applicable`
   допускается только с проверенным основанием, не из-за отсутствия инструмента.
   Evidence обязательна для claimed pass, `snapshot_tree` каждого Check должен
   совпадать с Round.snapshot.tree; соответствие evidence этому tree проверяется
   потребителем. Checks — проверки reviewer/оценённые им применимые результаты,
   не история того, как автор разрабатывал тесты.
5. `changes_required` при открытых high/medium или установленном обязательном
   нарушении. При одновременном недостатке evidence limitations сохраняются.
   `blocked` — нет установленного исправимого блокера, но не хватает обязательных
   оснований/доступа/независимости/применимости. `approved` — достаточная coverage,
   нет обязательных нерешённых findings/failed-unverified gates/blocking limitations,
   independence confirmed. Low сами по себе допустимы. Противоречивый verdict invalid.
6. `reviewer_context` не входит в authors. Для confirmed нужна inspectable реальная
   invocation/context evidence, сопоставленная caller с фактическим запуском и всеми
   авторами/исправителями. Отчёт сам себя не удостоверяет; cryptographic attestation
   и новый trusted registry не вводятся. Самостоятельное self-review полезно как
   analysis, но не может получить независимый approved gate.

### 6.3. Два отдельных результата машинной проверки

Обычная программа может проверить синтаксис/структуру/типы/enums/ссылки раундов/
согласованность verdict → `valid|invalid|unsupported`. Это не semantic approval.
Для gate программа дополнительно получает ожидаемые project/work, purpose,
полный текущий tree/base/exclusions, актуальные input versions, необходимые
checks/coverage и доверенные caller provenance observations. Она выбирает явно
указанный round; старый approved не заменяет более позднее опровергающее review.
При любом более позднем применимом unresolved high/medium/blocked выводе старый
round не даёт gate до независимого разрешения. Invalid/unknown более поздний
round требует reconciliation, не fallback к старому approved.

`passed` возможно только для structurally valid поддерживаемого approved round,
при полном совпадении subject и применимых входов, подтверждённой независимости,
достаточных checks и отсутствии опровергающих rounds. Поле approved не заменяет
эти внешние проверки. Недоступные evidence означают отсутствие допуска, а не
автоматическое доказательство дефекта. Самостоятельная Go/иная утилита сейчас
не проектируется и не поручается; поставляется однозначный контракт формата,
а instruction consumers применяют его и существующие инструменты.

## 7. Обновление потребителей: замкнутый объём

Все пути ниже от project root; source skills зеркалируются в `.opencode/skills/`.

| Группа | Точные основные владельцы / изменение |
|---|---|
| Feature producers/adapter | `skills/ris-proj-adapter-beads-tasks/{SKILL.md,references/{feature-record,create,update,standalone,structure,completion,plan-overview}.md}`: /2, early/root/readiness/unsupported и native safeguards |
| Feature lifecycle | `ris-proj-flow-prepare-feature`, `ris-proj-op-{specify-feature,design-feature,decompose-feature}` и acceptance resources: early ID, combined decision, same-record refs, embedded design, decompose внутри prepare |
| Worktree | `ris-proj-op-prepare-task-worktree`: preparation admission, прежний portable owner/адаптеры; нет нового feature-worktree skill |
| Implementation | `ris-port-op-implement-change`, его `references/tdd.md`, `ris-proj-op-implement-task-tdd`, full execute `references/{text-work,evidence,recovery}.md`: убрать plan/report persistence и historical TDD audit gates, сохранить substantive duties |
| Review/docs/publication | `ris-proj-op-review-task`, portable review, `ris-proj-op-update-documentation`, `ris-proj-op-publish-task` и snapshot resources: нет implementation-report discovery/gate; YAML subject/independence/rounds вместо Markdown; прежняя whole-tree проверка |
| Bug route | `ris-proj-flow-fix-bug`, exact bug branches implementation/review/publisher, adapter bug-execution: нет plan/implementation report prerequisites; сохранить полный accepted bug-input snapshot, material design и отдельные fix/close effects |
| Verification/navigation | `ris-proj-op-complete-container`, portable verify, `ris-proj-op-{show-plan,suggest-continuation,show-help,select-feature}`: /2/early records, достаточный design без отдельного файла, no planner/report recommendations |
| Fast | `ris-proj-flow-execute-simple-task` и его resources: сохранить no-file exception, independent review и все publication/recovery gates; не навязывать новый report |
| Общие нормы | common `references/{artifacts,quality,published-inputs}.md`, product `01,03,04,05,06,07,08`, MVP/catalog/template при затронутости, `AGENTS.md`, `docs/rules/development.md`, architecture/repository и `docs/development.md`: убрать противоречащие обязательства, сохранить boundaries |
| Package/public interface | planning source/install skills и `commands/opencode/risp-plan-task.md`, installed facade, installer ownership/retired paths, `docs/skills.md`, README, migration guide и bilingual help pages: согласованное удаление действующих planners без aliases |

Это inventory affected contracts, не требование менять каждый файл ради списка.
Перед исполнением подтвердить точные существующие пути и новых consumers поиском.
Исторические delivery specs/results не переписываются как новые нормы; к старым
совместимым решениям добавляется адресная ссылка на новое принятое изменение
в актуальном нормативном источнике. OKF edits product/rules проходят своих owners
и требуют принятого scope, а не самостоятельного изменения product при реализации.

## 8. Проверки и трассировка до декомпозиции

| AC S1 | Граница и oracle будущей проверки |
|---|---|
| 001–002,017 | Статическое чтение adapter /2 + create/reuse/unsupported branches: ранняя null-форма, all-status collision/retry, no migration/write на /1; encoding examples parse обычным JSON parser |
| 003–004 | Admission/copy resources и direct consumers: ID→одна копия, preservation, purpose-specific readiness; affected обычные CLI checks только при изменении исполняемой worktree логики |
| 005–006 | Содержательное review acceptance refs двух selectors/одного решения, inline design и material-design coverage; отсутствие лишнего интервью/обязательного design.md |
| 007 | Prepare→existing decomposition contracts: method reuse, one-task no child, multi-task AC/seams/directed blockers, reconciliation после частичной записи |
| 008–011 | Карта consumers + поиск active plan/report/TDD-history gates; чтение implementation/review/recovery обязанностей. Исторические совпадения допустимы, активные требования — нет |
| 012–015 | Формат/производитель/потребители: типы, complete report, round/finding history, exact tree/provenance; негативные примеры invalid/unknown/stale/changes_required/high-medium и положительный approved+low проверяются чтением, YAML examples — обычным parser, без агентских сессий |
| 016 | Fast instructions сохраняют явное no-file exception и реальный независимый reviewer; нет случайного наследования mandatory save |
| 018 | Existing publication/completion/recovery contracts: отдельные Git/primary/result/close/Dolt факты, confirmation-first retry, права/guards/independent full-tree recheck |
| 019–020 | Resource/link/dependency/source-install parity, affected package installation и help program checks, independent review полного финального снимка; agent tests запрещены |

Парсер YAML подтверждает только синтаксис, не соответствие всей схеме или реальное
поведение reviewer. Пока отдельного validator нет, семантика схемы проверяется
содержательным review, не объявляется машинно доказанной. Если реализация добавит
исполняемую проверку в существующий инструмент в рамках отдельно разрешённого scope,
ей нужны обычные deterministic tests/TDD; это не основание молча расширять поставку.
Не нужны полные live matrices, измерения токенов или поведенческие эксперименты.

## 9. Риски, альтернативы и остановка

- Выбрана /2 вместо незаметного расширения /1: честная несовместимость по ris-e26,
  нет dual schema/migration layer. Это может блокировать будущую работу по старым
  записям; перед rollout нужна свежая оценка открытой очереди.
- Выбран один YAML с rounds вместо pair/Markdown frontmatter: нет двух авторитетов,
  цена — строгие типы и целостная запись. Локальный файл не доказывает происхождение
  и не гарантирует доступность вне primary; missing provenance/report блокирует gate.
- Планирование и implementation-report убираются, а не распределяются по новым
  файлам. Сознательно исключается ретроспективный аудит TDD циклов; TDD остаётся
  обязанностью исполнителя, correctness/tests — предметом независимого review.
- Не вводятся обязательный Go tool, schema registry, новые роли или round cap.
  Общепроектный отдельный ADR не требуется: публичные изменения достаточно явно
  описаны здесь и в согласованной targeted поправке нормативных owners.

Принятие S1/D1 допускает дальнейшие ревью/публикацию и подготовку исполнения,
но не саму реализацию.
Ни accepted refs, ни новая /2 запись для ris-b1a не создаются. После фактического
принятия — отдельные разрешённые review/publication сохранённых документов;
decomposition этой ordinary-задачи может использовать существующий standalone
контракт. Новый целевой lifecycle не применяется к собственной подготовке до
реализации. Реализация не запускается; Git/Dolt-публикация и закрытие, если
поручены, выполняются отдельно своими действующими владельцами и проверками.
