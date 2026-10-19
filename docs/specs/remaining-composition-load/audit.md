# Остаточная композиция и загрузки RIS — bounded аудит ris-vg4

## Результат и проверенная версия

**No-change для пакета:** в двух выбранных цепочках не найдено нового
доказанного расхождения владельцев или ненужной безусловной загрузки,
требующего правки после закрытых поставок. Публикуемый результат — этот отчёт
наблюдений, не новая норма, спецификация или принятие дизайна.

Проверено 19.10.2026 на полном Git
`148a9c5dbfa37a3c510d46fb45603c1d45dc2c16`. Все адреса исходников ниже относятся
к этой версии; при чтении отчёта в более позднем дереве следует открыть их именно
на указанном commit. Пять исходных предметов из ссылок задачи на `e147e4d6…`
(architecture, common, оба flow и publisher) не изменились до проверенной версии.
Область — только `prepare-feature → document owners → publisher` и
`execute-task → review → publisher`, включая их непосредственные условия
подключения общих ресурсов и адаптера, а не все 53 навыка как одну загрузку.

## Метод и общие владельцы

Для каждого перехода сопоставлены producer, consumer, предмет проверки,
условие загрузки и возвращаемое evidence. Повтор признан необходимым локальным
guard, если consumer проверяет свой предмет/свежий предикат либо независимость,
а не заново выполняет чужой алгоритм. Основание —
[архитектура, §§2–4](../../product/01-architecture.md) и
[композиция, §§5–7, 9–11](../../product/03-composition.md).
Инструкции читались для аудита: это не наблюдение фактических загрузок агента.

| Владелец | Обязательное при соответствующей операции | Условное подключение |
|---|---|---|
| [common](../../../skills/ris-proj-lib-common/SKILL.md), §Conditional resources | Короткий baseline; уже доступные актуальные инструкции переиспользуются | `references/dialogue.md` перед вопросами/решениями; `artifacts.md` перед substantive artifact, execution transfer или partial/uncertain effects; `quality.md` перед выбором проверок/оценкой. Простой exact read сам по себе их не активирует; rules-layout example не нужен этим цепочкам |
| [context](../../../skills/ris-proj-op-resolve-context/SKILL.md) | `references/configuration.md` при подготовке настроек, с whole-present-config validation | `paths.md` для путей; `shared-primary.md` только для shared workspace; `execution-roles.md` только когда caller требует роль. Известный tracker workspace допускает exact read без context |
| [Beads adapter](../../../skills/ris-proj-adapter-beads-tasks/SKILL.md), §§Capabilities and conditional resources, Read and reconcile | Main для нужных typed reads; полный own content при содержательном решении, не глобальная выгрузка для известного ID | `feature-record.md` для feature refs; `create.md`+`concurrency.md` для create; `update.md`+`concurrency.md` для update; `claim.md`+`concurrency.md` для claim/heartbeat; `completion.md`+`concurrency.md` для exact completion; `standalone.md` для ordinary source/result/close; `bug-execution.md` для native bug execution; `dolt-publication.md` для отдельной публикации/remote-gated preflight. Не все ветки одновременно |

Ресурсы в таблицах разрешаются **от папки названного владельца**; имена без
`references/` продолжают ту же папку references. Это не новые импорты/реестр.

## Цепочка 1: prepare-feature → document owners → publisher

Основной адрес — [prepare-feature](../../../skills/ris-proj-flow-prepare-feature/SKILL.md).
Flow владеет порядком, одним человеческим диалогом и достаточностью целого;
каждая standalone noninteractive операция реально делегируется. Lead не должен
загружать все дочерние методики только ради маршрутизации.

| Этап / точный раздел flow | Actual owner и обычная загрузка | Условие / ресурс | Передача и необходимый consumer guard |
|---|---|---|---|
| Scope, permissions and execution | Flow + common/context; read-only adapter/publisher preflight | Роли feature-selection / feature-preparation; common/context ресурсы по таблице выше; Dolt resource нужен уже remote-gated preflight | Права и реальные возможности, а не configured name; actual launch проверяет flow |
| Choose and accept requirements | `ris-proj-op-select-feature` для направления, не readiness | `ris-proj-op-refine-epic` только при мешающей неясности границы; исторические baseline/design evidence selection раскрывает только для recommendation-changing вопроса | Человеческий выбор возвращается lead; повторная execution readiness не назначена selector |
| Prepare the pre-ID document copy before writing | `ris-port-op-prepare-worktree` + выбранный worktree adapter; его `references/worktrees-contract.md` перед adapter operations | `preservation.md` при reuse/existing branch/partial effects/hooks; `environment.md` только для setup/hooks; Git adapter `references/git.md` для выбранного Git route | До первой записи: identity/repository/path/branch/pinned base, copy/environment facts; flow проверяет receipt и переобрабатывает context в подготовленной copy. Publisher не готовит ветку |
| Choose and accept requirements: coverage и proposal | Lead применяет только Map the material requirements и Check and hand off из `ris-proj-op-interview-feature`; предложение — `ris-port-op-formulate-feature-spec` в executor | `ris-port-op-interview` только при недостающих interdependent material answers; sufficient inputs не вызывают интервью, нового executor или coverage report | Полный candidate/version; отдельное человеческое принятие здесь. Повтор coverage на готовом candidate — иной предмет, не повтор интервью |
| Accepted local requirements save | `ris-proj-op-specify-feature`, common/context и собственный `references/acceptance-and-save.md`; coverage map/check | Явно document-only accepted-local-save: пропускает formulation/interview, не требует ID/adapter и не публикует | Writer сам читает полный accepted candidate/decision, сверяет сохранённое; это не повтор author proposal и не повтор принятия |
| Discuss and separately accept design | Предложение — `ris-port-op-design-feature`; диалог/отдельное принятие — lead; сохранение — `ris-proj-op-design-feature` с `references/acceptance-and-save.md` | Technical interview только для нерешённых взаимозависимых решений; draft-save отдельно разрешён; design applicability check при изменении требований | Accepted-local-save пропускает formulation/interview и Git/record effects; неизменённые требования не перепринимаются |
| Review, publish Git, then create the feature: review | Независимый `ris-port-op-review-change`, полный document candidate, решения и checks | Его `references/publication-snapshot.md` только при unrelated dirty paths, exclusions или ambiguous membership | Независимый предметный review не заменяет принятие. High/medium возвращаются content owner; новый snapshot получает применимое свежее review |
| Там же: Git publication | `ris-proj-op-publish-task`, Documents branch; common, context для нужных правил/путей | No ID не вызывает adapter/task-note discovery; drift вызывает affected checks и независимую reassessment | Publisher один выполняет integration/push/read-back; flow сопоставляет subject/version/receipt с обещанным результатом, не повторяет Git алгоритм |
| Там же: record reconciliation и tracker publication | `ris-proj-op-specify-feature` limited record-only, выбранный adapter; затем отдельный adapter publication | `feature-record.md` и create/concurrency при create; при существующем ID с недостающими design refs — `ris-proj-op-design-feature` limited record-only с update guards; `dolt-publication.md` отдельно | Только опубликованные Git refs/раздельные решения; local record receipt не доказывает remote publication. Нет повторного Git/Dolt push у limited document owners |

Direct контракты [specify-feature](../../../skills/ris-proj-op-specify-feature/SKILL.md)
и [design-feature](../../../skills/ris-proj-op-design-feature/SKILL.md) также прочитаны
вне flow. Full по умолчанию включает review/publication, но flow **явно** выбирает
limited local-save/record-only. Поэтому их самостоятельные full gates не являются
вторым обязательным циклом публикации в данной композиции. Их
[requirements](../../../skills/ris-proj-op-specify-feature/references/acceptance-and-save.md)
и [design](../../../skills/ris-proj-op-design-feature/references/acceptance-and-save.md)
ресурсы останавливают local save до review/push и направляют record-only сразу к
reconciliation по проверенному Git receipt.

## Цепочка 2: execute-task → review → publisher

Основной адрес — [execute-task](../../../skills/ris-proj-flow-execute-task/SKILL.md).
В таблице обычный fresh standalone route; feature/native bug и recovery ветки
указаны как условия, а не как обязательная сумма загрузок.

| Этап / точный раздел flow | Actual owner и обычная загрузка | Условие / ресурс | Передача и необходимый consumer guard |
|---|---|---|---|
| Prepare scope and executors; Select exactly one target; Verify readiness | Flow + common/context; выбранный adapter и publisher read-only preflight | Exact ID не требует global list; `feature-record.md` только actual feature-linked subject; `bug-execution.md` для exact native bug, не automatic queue | Flow определяет достаточность/права/одну цель; adapter владеет typed reads, claim и гарантиями, не содержательным принятием |
| Execution sequence, 1 | `ris-proj-op-prepare-task-worktree` + `ris-port-op-prepare-worktree` + выбранный worktree adapter | Worktree/base resources по цепочке 1; claim resources у tasks adapter; context shared-primary для shared paths | Own claim, blockers, copy association и environment отдельны; receiver обновляет свои mutable predicates, не повторяет creation |
| 2 | `ris-proj-op-plan-task` + `ris-port-op-plan-task`, common/context/adapter | Saved plan нужен по rules/sufficiency; в RIS обязателен. Direct planner всегда сохраняет; не загружает preparation skills | Plan/version/coverage, а не повтор setup или claim; при допустимом omission другой проект получает причину и sufficient input locator |
| 3 | Behavior: `ris-proj-op-implement-task-tdd` + `ris-port-op-implement-change` | Wrapper `references/current-copy.md` для task-specific/separate copy; base `references/tdd.md` перед behavior change; его `publication-snapshot.md` при unrelated dirty scope; documentation owner только перед sync | Собственные guards и содержательные проверки; RED/GREEN по реальным slices, не по расширению файла |
| 3, text-only | Flow `references/text-work.md`, затем content owner по ответственности: RIS author / portable author / doc sync / selected OKF / direct ordinary Markdown | Не загружает TDD методику только ради текста; executable slice возвращается в TDD route | Получатель свежо проверяет claim/blocker/copy, сохраняет implementation evidence; не получает право self-approval |
| 4–5 | Fresh task-review executor: `ris-proj-op-review-task` + `ris-port-op-review-change`, common/context; adapter при ID | Base `references/publication-snapshot.md` только для dirty/exclusion ambiguity; native bug implementation требует full historical snapshot, pre-execution document subject — нет | Полный snapshot, rules/accepted input и saved findings с provenance. Reviewer самостоятельно проверяет предмет; авторское evidence не независимый verdict |
| 6 | `ris-proj-op-publish-task`, Task/change branch | Adapter для ID/ownership/blockers; integration/hook drift возвращает affected checks и независимую task-review reassessment | Один Git алгоритм; publisher сверяет полное reviewed tree, исходящую историю и remote read-back. Flow принимает receipt, не реализует второй Git алгоритм |
| 7–8, граница выходов | Selected adapter для result и separate exact leaf close; отдельно tracker publication | `completion.md`, `concurrency.md`, ordinary `standalone.md` либо `bug-execution.md`; selected one-task feature — `ris-proj-op-complete-container` verify-and-close, не leaf shortcut; `dolt-publication.md` отдельно | Git, criteria/composition, close и Dolt не взаимозаменяемы; родители автоматически не закрываются |
| Recovery / insufficient transition proof | Flow `references/evidence.md`; `references/recovery.md` для own unfinished/prior/partial/interrupted/closed pending work | Не загружаются fresh run только ради первого handoff. Recovery возвращает первую missing/inapplicable operation существующей numbered route | Сохранённый эффект отделён от применимости evidence; нет новой execution engine, blind retry или обязательного transition ledger |

Проверены [review-task](../../../skills/ris-proj-op-review-task/SKILL.md),
[portable review](../../../skills/ris-port-op-review-change/SKILL.md) и
[publisher](../../../skills/ris-proj-op-publish-task/SKILL.md) как standalone consumers.
Review только оценивает/сохраняет отчёт, publisher только публикует Git;
ни один не принимает содержание, не закрывает задачу и не запускает следующую
операцию. Проверка snapshot у flow, reviewer и publisher относится соответственно
к переходу, независимой оценке и фактическим staged/integrated/published bytes.
Удалять её как повтор одного слова было бы ослаблением разных guards.

## Сравнение с закрытыми поставками и решение

Прочитаны actual Beads description/AC/result notes четырёх exact IDs, не только
их статусы; прежние planning-only фразы не использованы как текущие AC.
Git history сверена по указанным commits и текущим producer/consumer sections.
Исторические имена `ris-bf4` сопоставлены с нынешними владельцами, не восстановлены
как алиасы. Исторические agent runs/проверки не переобъявлены текущим pass.

| Закрытая работа / Git | Поставленная граница и текущая проверка | Остаток в данном scope |
|---|---|---|
| ris-9wk / `8a40f811379180598e36e631cf704cad1aa6a6ce` | Common conditional artifacts/quality; context path/shared/role resources; adapter action-resource table. Current consumers используют эти условия, а не universal handoff для exact read | Substantive candidates и execution transfer действительно активируют artifacts; это не возврат удалённой обязанности простого списка. Новый дефект не установлен |
| ris-bf4 / `e386a8559bd0bc95d22bec3edddd6f7d61b5ad1a` | Component ownership, limited contributions, отдельные принятия и публикации; Git-owned content/decisions вместо обязательных scoped digests | Flow проверяет receipts/applicability; не повторяет digest/SQL/Git алгоритмы. Local-save и record-only не делают duplicate push |
| ris-4et / `032b24c5f6c7ed8880d8554e242d884dc73a0303` | Recommendation отделена от readiness; exact-ID/compact reads, historical evidence только для material question | Flow закономерно проверяет execution readiness позже. Это другой результат, не повтор полной readiness у selector |
| R1, ris-vhm / `f60933cc9bc5005d56c8ad3a8ee6ddc4fe4fe57e` | Pre-ID copy gate перед writes; document wrappers требуют подготовленную copy; publisher не создаёт ветку | Маршрут замкнут через portable preparation без будущего ID; повторно исправлять уже закрытый разрыв не требуется |

**Адресных правок skills нет:** ни одного нового residual discrepancy с
достаточным основанием не установлено. Нет переноса текста/нового trigger,
слоёв, skills, cache или registry. Краткие повторения permission, acceptance,
recovery и independent snapshot checks оставлены как локальные предикаты
разных результатов, согласно правилу композиции «короткая ссылка допустима;
копирование полного общего алгоритма — нет».

## Проверки и границы вывода

- Статически сопоставлены оба flow, непосредственные document/review/publication
  owners, их ресурсы и общие conditional-resource triggers; имена и адреса
  проверены по сохранённым файлам. Source/install parity проверена для выбранных
  владельцев как дополнительная проверка входов; пакет не редактировался.
- Изменён только этот обычный Markdown report; whitespace, локальные ссылки и
  полный base+добавление/mode snapshot проверяются перед передачей на независимое
  ревью. Этот авторский аудит сам по себе не является независимым review verdict.
- AC-1: две карты и сравнение выше. AC-2: guards не изменены. AC-3: ресурсных
  переносов/новых слоёв и performance claims нет. AC-4: адреса, scope и limits
  сохранены; независимое review и Git/Beads/Dolt completion остаются отдельными
  последующими действиями, не заявлены выполненными этим отчётом.
- Live/scenario agent tests не писались и не запускались. Исполняемый код,
  installer, client и runtime mechanisms не менялись; их suite не запускались
  ради Markdown-отчёта. Токены, стоимость, длительность, поведенческая надёжность
  и повторяемость неизвестны. No-change не доказывает оптимальность всего пакета,
  отсутствие иных дефектов или фактическое соблюдение инструкций агентом.
