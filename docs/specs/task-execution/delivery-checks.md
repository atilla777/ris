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
