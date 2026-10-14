# Свежий запуск task-execution — проверки поставки T1

Поставка `ris-01r.1.1`, принятые [требования](spec.md) и [дизайн](design.md).
Это evidence свежего маршрута, а не полная приёмка фичи `ris-01r.1`:
full resume и combined AC-001–016 verification принадлежат `ris-01r.1.2`.

## Среда и проверяемый результат

OpenCode 1.18.33, модель `openai/gpt-6.1-sol`, Beads 1.3.1, Dolt 2.4.1.
Исходник `skills/ris-execute-task/`, installed copy с обоими ресурсами идентична.
Один сценарий без новой базы; методики этапов остались у прежних владельцев.
Три настроенные роли реально запускались в отдельных контекстах; independent
reviewers отличны от implementation/repair authors. Изолированные fixtures
находятся в `/tmp/opencode/ris-01r-11-behavior/`, локальные подробные отчёты —
`.sdlc/tasks/ris-01r.1.1/`. Эти локальные адреса не являются переносимыми входами
для будущего запуска скила. Commit данного документа идентифицирует редакцию
поставки; исходные skill bytes за время поведенческих прогонов не менялись.

## Реальные успешные маршруты

| Проект/цель | Git commit / полное дерево | Отдельный Dolt snapshot |
|---|---|---|
| g2-code / g2-code-6b0 | `f2e967a3ecdbea2efbb89abbb24991e5020bebba` / `c6d2c5d4d743724db01470fbf086fe43f21de0dd` | `6rcvcen6uo2o17tgsjv5p3qck3mb416p` |
| g2-text / g2-text-ha2 | `cb4ea0dce1f7fe75170fb4ed5d7603f63d60c7c8` / `788a7546685df5bf791a33aa02f2fac3a1e515c9` | `qo2g3fkv15sr4dhjprurahplsvoogalc` |
| exp-feature / exp-feature-mt6.1 | `ad576ffabf8e088a88bec97bbd886edd2407ec3e` / `1b6e41a77a0bdbf5e3b4b27eecf56dc50f98a9d3` | `m99lalf13v2mcv9jdbeck26fbj939h0l` |

Code и text проекты различаются правилами и путями (`scratch/tasks` против
`local/evidence`), используют настоящий выбранный Beads и разные Git/Dolt remotes.
Проверены actual claim/copy/plan, code ожидаемый RED до production edit и GREEN
после (5 tests), substantive text checks, fresh independent review, Git push с
NEW clone readback, DISTINCT exact closure, отдельный Dolt push с full outgoing
history inspection и NEW clone AS OF readback. Чужие staged/unstaged/untracked
named files, рабочие байты/режимы и index blobs сохранены. Seed publications
отделены от task publications; один канал не заменял другой.

Пример сохранённой code chronology из actual host export: test patch
`prt_13899dfe8001qQMRt20cWNVz97`; expected RED exit 1
`prt_13899ee2a001ECywx8zTqKAOqv`; первая production patch
`prt_1389a4cbf001E7j1G0yAF4X5pG`; GREEN exit 0
`prt_1389a5e73001PE69MK0rrpISfg`. Independent acceptance reviewer
`ses_ec749d312ffeNVqnOtHk5Txs87` отдельно создал новые Git/Dolt clones и проверил
полные trees/records, chronology и сохранность чужих файлов.

## Наблюдаемые границы T1

| Критерии | Фактическое evidence и предел |
|---|---|
| AC-001–002 | Actual all-state selection: numeric priority, parsed age, equal priority/time lex ID; multi-own dk7→n28→ynb; own blocked победил unrelated ready; explicit live foreign и unready ID не подменялись. Closed g2 ID не переоткрывался. |
| AC-003–004 | Missing accepted input, typed active blocker и open mandatory child дают конкретный stop; container рекомендует ребёнка без claim. Own ambiguity требует решения. No-ready closed-only queue выдаёт подготовительный шаг без интервью. |
| AC-005–007 | Configured actual role children, missing-review-role pre-mutation stop; copy/foreign preservation; code RED/GREEN и text checks; два разных проекта. |
| AC-008–009 | Controlled real greeting fault → stable medium GREETING-R001 → original owner repair/checks → fresh review PASS. Low-only замечание рассмотрено без нового цикла. Отдельная no-progress controlled branch: тот же medium, неизменные bytes, отсутствующее разрешение на исправление → сохранённый stop, без произвольного лимита раундов. |
| AC-010 (часть T1) | История, actor/copy/input/snapshot/review/channel evidence сохранены; повтор partial execution только reconciles и stops. Автоматический full resume не проверен и не поставлен. |
| AC-011 | В feature route опубликованный main drift изменил полный integrated tree; publisher остановился до push, affected checks и fresh integrated reviewer проверили новое дерево, затем exact approved tree отправлено. Direct-push prohibition реально предотвратил эффект. |
| AC-012 | Реальные Git/closure/Dolt результаты разделены. Actual rejecting Git hook сохранил local commit при remote seed. Withheld protected window предотвратило notes/closure после Git success. Unavailable Dolt store дал actual fetch error после Git success/local closure; push не выполнялся. |
| AC-013 | Selected one-task greeting feature: весь accepted AC set, integration/architecture/docs проверены на published integrated revision; verification persisted/read back, потом separate close и tracker push/readback. Полная parent epic row неизменна/open. |
| AC-014–016 | Успешные/частичные отчёты, actual fresh next recommendation без claim; two-project portability; source/install parity и actual natural neighboring-request routing. |

Multi-own check actual configured child `ses_ec63c8749ffewnvcReBRgws7Zx` создал
только отдельно разрешённые fixture setup records; selection stage не изменил
ни одну из 16 записей. Own tie с одинаковыми priority/time отдельно не построен:
lex-ID ветка наблюдалась на другой actual fixture-паре того же сортировщика.

Changed integrated review `ses_ec6d87c4bffeIf67sijWlOIGVn`, publisher
`ses_ec6d0a602ffeQkv8JP1mAK1Z0m`, full feature completion
`ses_ec6c92a3affeOuVijtRMjt5Ps6` — разные actual contexts. Feature requirements
и design refs/отдельные decisions сохранили исходный seed `face1a994582740ec301cfc414f4659a7d832fbe`.
Parent `exp-feature-mt6` revision `1563444444675963352` неизменна; не создавались
искусственные children и не закрывался epic.

Natural routing actual children: selection `ses_ec6e1f3f3ffeDaLMTfA6jHXAys`, full
unready run `ses_ec6e1e053ffeUOGDEyXsQTypX3`, plan `ses_ec6d8bf21ffezch3aaXxlBC4KF`,
review `ses_ec6d8bc46ffe7v36jgSt2haVRN`, publication `ses_ec6d0da77ffeR3P29lCOb0K9ry`,
feature preparation `ses_ec6d0add4ffecR63hEcAqvXJh9`, irrelevant translation
`ses_ec6d0f049ffevJqt1KnM5IB655`. Реальные loads и permitted operations прочитаны
из сохранённых receipts/host exports; не использовалось лексическое сопоставление
вместо фактического выбора.

## Ошибки испытаний и ограничения

Первые прогоны выявили ошибки тестового исполнения: timeout/permission routes,
hashing созданной директории, неверный synthetic snapshot hash, misrouting локальных
заметок. Они сохранены в истории; не названы дефектами поставляемого скила и не
выданы за успешные тесты. Исправлены bounded named-file witnesses, native Git
temporary-index snapshots и короткие actual stage receipts. Старые partial задачи
не переисполнялись как fresh runs. После утраты первого `/tmp` выполнена сверка
и созданы новые independent fixtures, не восстановлена произвольная очередь.

No-progress и fault injection — контролируемые boundary scenarios, не доказательство
устойчивости каждого автономного запуска. Closure failure — реально prevented
write из-за отсутствующего окна, не выдуманный неуспешный `bd close`. Dolt failure —
actual selected-remote fetch error `operation not valid on a file`, dependent push
unattempted; точный numeric fetch exit исходным child не сохранён.

Fixture protected windows обеспечены controller-exclusive sequential ownership
локальных баз/remotes. Это не CAS Beads и не гарантия отсутствия production remote
writers. Не проверены другие адаптеры/клиенты, universal stability и full resume.
История не скрывает ошибки harness и ограничения evidence; raw receipts остаются
локальными и архивируются отдельно от Git payload.

## T2 — controlled interruption/resume и combined evidence

14 октября 2026 года, `ris-01r.1.2`. Эта секция добавлена в candidate branch;
интеграция и независимое одобрение итогового T2 снимка ещё не выполнены.
История T1 выше сохранена. Combined матрица AC-001–016 составлена по actual
source diff и сохранённым versioned receipts, без повторного запуска suites или
поведенческих эффектов. Это bounded author assessment, не принятие/закрытие
родительской фичи `ris-01r.1` или эпика.

### Версия и применимость

База T1 — `4974bcf46ebe68e2c4d971d663976f4ad90877bb`, полное дерево
`e4439a35f588e3645b019fc070ade2d19879f6b4`. T2 меняет selection/remaining-role
gates, reconciliation/transition и evidence contract, добавляет условный owned
`references/recovery.md`. Восемь numbered этапов и их самостоятельные владельцы
сохранены; остальные source skill folders не изменены. Поэтому T1 runtime не
переиспользуется целиком: каждая строка матрицы отдельно удерживает неизменные
owner/check результаты и добавляет наблюдения изменённых seams.

| Проверенный T2 ресурс | SHA256 (source и installed одинаковы) |
|---|---|
| SKILL.md | `3d72ef284cc1c63fb21e258d0c9b7dbbe0c8068d860678d568abfbd30dcd3e88` |
| references/evidence.md | `706879b0890437d8857082577f23d7d189bf0c5371f80538414ea1c49a403c12` |
| references/recovery.md | `9f3c26cb4df33ea10edb9c13c1a0ebc44b9041dd4788efbb1d1da09eed75c797` |
| references/text-work.md (не менялся) | `ef5288e9695da20dda04bd75eedf42a5847588e77b4fcd90bdeb691cf5f74bef` |

Единственный полный candidate tree/package fingerprint, полный состав task
overlay с additions/modes, версии отчётов и per-AC applicability сохранены в
PRIMARY `.sdlc/tasks/ris-01r.1.2/{candidate-snapshot,combined-matrix}.md`.
Snapshot построен native Git temporary index поверх всей базы, с включением
новых recovery ресурсов; реальный index не менялся. Эти ignored адреса —
локальное audit evidence, не обязательный переносимый вход скила. Секция не
включает собственный full-tree hash, что исключает self-referential fingerprint;
Git-ревизия этого документа при будущей публикации идентифицирует его payload.

### Реальные границы и каналы

CODE `r12code-4y8` использует отдельный RIS-проект с handbook/proposals и
scratch/evidence/scratch/copies. После реальных prep, plan, TDD implementation,
fresh independent review и Git publication каждый invocation завершался на
заданной границе; новый native general invocation читал актуальные receipts,
трекер, copy и версии и выполнял только остаток. Это R-PREP, R-PLAN, R-IMPL,
R-REVIEW, R-GIT, а не повтор preparation. Два TDD slices дали реальные expected
RED до соответствующих production patches, затем GREEN (пять методов, всего
четыре test runs). Полный checked/reviewed 13-entry candidate совпал с отправленным
деревом и NEW independent Git clone.

TEXT `exp-closefail-n8f` использует policies/accepted/work/tasks/work/copies.
После исторически подтверждённого Git отдельные свежие операции сохранили
criterion result, затем отдельно закрыли точный ID (R-CLOSE), отправили полный
audited outgoing Dolt snapshot и остановились до readback (R-TRACKER-SENT).
Следующий fresh invocation создал NEW independent selected-remote clone,
проверил полный decoded issue AS OF sent snapshot и пустой typed graph;
повторный push/close/result update не понадобился.

| Fixture | Git commit / полное дерево | Отдельный tracker результат |
|---|---|---|
| r12code-4y8 | `6dbfdaa093ee10264cbbd7c94668c1b376ea89d3` / `ef35a9a299223da8335261c88f9fe4a4cf0a2178` | После Git остановлен; result/closure/Dolt delivery не выполнены |
| exp-closefail-n8f | `8f2bf43739a073b17ef5af54cc572cbafdc88a8f` / `170471a9e1af3534a1f0aba5256301fb45415ad0` | Result `e5f6kiqlrf2s06gu8v4pf9mj8u1j5lme`; distinct closure/sent/independently confirmed `er9ukic2faumbea9ob38c1faaiv6j4k6` |

CODE durable totals: claim/copy-add/plan/implementation/review/task commit/FF/Git
push — по одному; после preparation claim/add не повторялись, после checked
implementation тесты/правки не повторялись для review/publish. TEXT totals:
claim/plan/text implementation/review/Git commit/Git push/result/close/Dolt send —
по одному; readback resume добавил только independent confirmation, остальные
lifecycle effects — ноль. Это counts durable effects, не всех исторических команд.
CODE foreign staged/unstaged/untracked bytes/modes/native index entries сохранены;
PRIMARY raw index при FF менялся только для двух intended integrated файлов.

Leading host сохранил actual native mappings в локальном host-invocations.md,
не полагаясь на child statement «ID недоступен». Code implementation
`ses_ec59f824affe40Z5BOAsG5o33P`, независимый reviewer
`ses_ec5981d6cffeS6RRpV26YWa737`, Git owner
`ses_ec592ccb0ffeldiZftJ8sXEXoD` — разные contexts. Text sender
`ses_ec583c21affe7JUQSJpHh8gly2` и fresh readback
`ses_ec57c3cceffevS2ok5ip5qJw62` также разные. Синтез не запускал новых executors.

### Combined criterion checks и отрицательные outcomes

| AC | Применимый вклад T1 + наблюдения T2 |
|---|---|
| 001–004 | T1 priority/age/ID, foreign/unready, mandatory child и no-ready guards; T2 actual 16-row own dk7→n28→ynb, blocked-own stop без fallback/claim, closed report и fresh closed-only preparation recommendation. Own exact-time tie отдельно не построен. |
| 005–007 | Неизменные stage owners; actual T2 native prep/plan/TDD/review/publication и copy reuse с foreign witnesses. Remaining-role case: CODE без требуемой дальнейшей review role остановлен до repair; completed TEXT report-only разрешён без implementation/review roles. T1 text checks удержаны только при полном tree/input/rule equality. |
| 008–009 | T1 реальный controlled GREETING-R001 repair/check/fresh review и low-only disposition применимы к неизменным owner methods. T2 сохраняет pending R1-001 medium и permission-induced no-progress: Wrong.LF неизменён, repair отсутствует, никакого нового успеха/round cap. Исторические неполные host mappings этой ветки не восстановлены одним новым launch. |
| 010 | Реальные controlled ends/resumes CODE/TEXT выше; материальные accepted constraints v2 (`?` вместо `!`) вызвали только replan с сохранением v1/history/Git effects. Старые whole-output GREEN/review не принимают v2; новая реализация намеренно не выполнялась. |
| 011–012 | T1 changed-integrated-tree reassessment и refusing Git/Dolt/window boundaries удержаны адресно. T2 NEW remote Git clone подтвердил unsent existing commit, retry/duplicate commit не делались; actual alternate direct-push prohibition остановила путь. Result/close/send/readback разделены; missing confirmation не стала поводом для второго push. |
| 013–014 | T1 complete one-task feature verification на `ad576ffabf8e088a88bec97bbd886edd2407ec3e`, tree `1b6e41a77a0bdbf5e3b4b27eecf56dc50f98a9d3`, sent Dolt `m99lalf13v2mcv9jdbeck26fbj939h0l`: T2 проверил полный subject/basis equality и две полные rows/typed edge independent sent snapshot. Verification/close/push не повторялись; весь parent row unchanged/open. Partial и success reports отделяют channels и рекомендуют остаток/подготовку без нового claim. |
| 015–016 | Два real differently configured проекта с выбранным Beads, current source/install bytes/modes/resources и bounded doc/link checks. T1 natural neighboring routing сохраняется только для неизменных owners; T2 natural resume выбрал execute-task/recovery, natural review — ris-review/base без scenario/repair/publication loads. |

Snapshot stimulus: дополнительный LF сделал Ready.LF восьмибайтовым результатом,
full tree отличался от PASS; guard потребовал affected content/check assessment
и fresh review, сохранил commit, не разрешил publish по старому PASS. Controller
затем восстановил оригинальные семь bytes; later direct review увидел clean
identical tree. Restoration — setup effect, не scenario repair или новая approval.

Missing-notes stimulus: intact reports временно moved outside fixture. Guard
восстановил actual Git visibility, closed record и content observations, но
оставил **conflict** по execution/copy linkage и **blocked** по missing review/check
provenance и unavailable selected Dolt remote. Он не выдумал историю или повторил
claim/implementation/close. Controller вернул 16 файлов intact; marker remote
остался unavailable. Последующий успешный resume этой ветки не заявляется.

Natural routing actual contexts: resume `ses_ec54aa6e3ffea03Xh3EjWSVmuy`, direct
review `ses_ec54aa6d5ffeQvylFV1sULAiyq`. Resume read retained closed/sent result,
не повторял эффекты; latest Dolt head в этой конкретной операции не fetch-ился,
поэтому её вывод относится к proven sent snapshot. Более ранний role-guard fetch
отдельно подтвердил тот же выбранный remote/sent snapshot, не заменяя этот предел.

### Статус и честные пределы

Матрица AC-001–016 **составлена**, bounded combined evidence поддерживает описанные
representative checks. Требуемый следующий gate — **fresh independent review
единственного полного candidate snapshot**, затем reassessment при изменении
integration tree. Ни авторский синтез, ни closure fixture не означают independent
approval, full parent acceptance или закрытие RIS-задачи.

Все interruption boundaries — реальные контролируемые завершения invocation,
**не process crashes**. CODE intentionally partial после Git; later boundaries
покрыты TEXT, не семь раз в каждом проекте. Не проверены отдельный own exact-time
tie, новый successful resumed repair/low-only, дополнительный material rule/package
change stimulus, unknown-live timeout/process termination, competing production
writers, другие adapters/clients. Fixture ALL-writer sequential ownership —
не Beads CAS и не universal concurrency guarantee. Missing historical provenance
не превращено в доказанную независимость. Source/install не менялись для тестов;
история harness ошибок сохранена. Raw evidence локальна; опубликованный документ
сохраняет hashes, outcomes и пределы, но не заменяет недоступные receipts.
