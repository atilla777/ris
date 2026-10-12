# Project rules authoring — W5 и интегрированная приёмка W6

Дата наблюдений: 12 октября 2026 года. Требования: [принятая v1](spec.md#подтверждение-принятия),
AC-001–023; состав: [W1–W6](delivery-plan.md), Beads `ris-dlk.1`–`.5`, родитель
`ris-dlk`. Этот отчёт фиксирует проверки; итоговые Git-ревизия, независимое
ревью и отдельные операции завершения/публикации фиксируются в Beads.
До подтверждения публикации результат этого файла — проверенный кандидат W6.

## Среда и идентичность

- OpenCode **1.18.33**, `opencode run --pure --format json`,
  модель **openai/gpt-6.1-sol**, Linux; Beads **1.3.1**.
- Исходная интегрированная ревизия: `d0c3973`; проверяемая поставка — эта ревизия
  плюс изменения W5 в содержащем отчёт Git-коммите. Принятые требования и
  предметные основы W1/W2 не изменены.
- В отдельные Git fixtures установлены полные восемь папок:
  `ris-common`, `ris-context`, `ris-okf`, `ris-interview-base`, две
  `ris-formulate-*-rules-base` и два `ris-author-*-rules`.
- SHA-256 JSON-манифеста путей и SHA-256 всех файлов этих восьми исходных папок:
  `789cfa08af2ba4d2c288b78bd2c45f4202110526dc656e43f4af17d712386f77`.
  Проверены source/installed bytes. Этот предоставленный package identity
  реально сохранён в результатах, не выдаётся за digest candidate или OKF.
- После независимого ревью уточнены только spelling путей optional example в
  двух wrappers: все пути теперь полные от installed `ris-common`. Реальные
  прогоны уже читали именно эти файлы. Финальный package manifest SHA-256:
  `74698e3be11d041a899d048925c6008503b1c6ea0226a1d96368354a6724aaab`.
  Resources, normative алгоритмы и прочие файлы package не изменились;
  прежние поведенческие результаты применимы, parity/format audit повторён.
- `external_directory`, `bash`, `task`, `webfetch` в поведенческих fixtures
  запрещены; доступ к исходному RIS отсутствует для исполнителя. Инфраструктурные
  файлы, создаваемые OpenCode, учитывались отдельно от нормативных записей.
- Полные запросы, JSONL tool traces, тексты кандидатов/принятия, before/after
  hashes и физический audit сохранены локально по правилам проекта. Они не
  являются обязательным удалённым входом; ниже приведены воспроизводимые
  сценарии, результаты и пределы свидетельств.

## W5: упаковка и документы

Один [образец](../../../skills/ris-common/assets/rules-example/index.md)
`rules-example/1` принадлежит `ris-common` как упаковочному владельцу.
Architecture и engineering примеры производны от своих предметных баз, не
являются независимо сопровождаемыми нормативными основами. Общие основы и
Rails/DragonRuby/Odin профили остаются у соответствующих баз; трёх полных копий
rules-бандла нет. Оба автора читают образец только при полезности иллюстрации
первого бандла, только корень и свою предметную область. Обычный update не
требует образца или другого автора.

Проверка всех пяти Markdown-файлов образца: parseable YAML/nonempty string
`type` у трёх концептов; корневой index с `okf_version: "0.2"`, вложенный
index без frontmatter; обе knowledge directories индексированы, все ссылки
разрешены. **PASS OKF 0.2 и профиль RIS**, по закреплённой спецификации,
без внешнего validator. Индексы не копируют нормы, ложных verified/принятий нет.

README, нормативная методика и каталог обновлены по фактическим четырём
скилам. Применимые упоминания неопределённого `ris-setup-project-rules`
заменены двумя предметными авторами, настройка остаётся отдельной работой.
Принятая спецификация/план сохраняют историческую отправную точку;
docs/concepts и docs/rules остаются разными бандлами после миграции,
delivery specs — обычным Markdown. Чужая миграция не расширялась.

## Новые реальные интеграционные диалоги

Каждый вызов: сначала показать точные normative content/version/files и место
decision/provenance без записи; отдельным следующим сообщением fixture-owner
принимает именно показанный кандидат и разрешает bounded save. Проверяются
сохранённые файлы, а не только ответ агента. Всего **14 успешных turns в шести
операциях**, включая два дополнительных provenance-уточнения; не 14 независимых
сквозных сценариев.

| Сценарий | Вход и последовательность | Фактический результат |
|---|---|---|
| Rails: architecture → engineering | Новый малый проект заявок, нет product/кода/tracker/ris.yaml; Rails 7.2/Ruby 3.3, одна БД, domain owns request, controller передаёт ввод, public read-only view, идемпотентный close; затем Minitest/Omakase, locked inputs, CI отсутствует, owner approval | r2 создал `docs/rules/index.md`, `architecture/index.md`, `architecture/requests.md`; d1 добавил `development.md` и навигацию. Нормы A1–A7 покрывают state/contracts/dependencies/atomicity и ошибки, без Service Layer. E1–E8 поддерживают их и оставляют patch/commands отложенными. Все architecture hashes сохранены при engineering save. |
| DragonRuby: engineering → architecture | Другой путь `knowledge/policies/` через v2 config; неизвестный SDK, Linux desktop, два пробела/manual review, runtime tests и target smoke, CI нет; затем input→simulation, presentation view, reset, reuse по пользе | g2 создал `index.md` и `development.md`; a1 добавил `architecture/index.md`, `principles.md` и навигацию. Engineering hash неизменен при architecture save. Host MRI/RuboCop/headless не объявлены совместимыми; runtime APIs/exit semantics отложены до SDK. Обязательное рассмотрение reuse не стало extraction. |
| Odin: architecture → engineering | Odin Linux x64, один поток, app→simulation→math, borrowed view до следующего step, caller allocator/owned free, partial init cleanup; затем pinned dev-2026-09, существующий manual formatting, check/test/build по version-matched help | o1 создал `knowledge/policies/index.md`, `architecture/index.md`, `principles.md`; od1 добавил `development.md` и навигацию. Engineering ссылается на lifetime/error/reuse обязанности, не меняет architecture hashes. Неподтверждённые compiler flags отложены, formatter/graphics/ECS/CI не навязаны. |

До каждого принятия нормативный delta пуст. После него изменились только
принятые concepts и необходимые indexes. Физический audit сравнил normative
body показанного кандидата с сохранённым, исключив объявленные decision/
acceptance/lifecycle metadata, **PASS**. Полные бандлы проходят OKF/RIS/links.
Tool traces подтверждают реальные common/context/OKF/base и только применимый
профиль; другой предметный автор не загружен, исходники RIS не прочитаны.
В Rails первом вызове прочитаны только root и architecture example, в игровом
engineering create — только root и development example.

Первоначальные Rails/DragonRuby предложения честно блокировали полноту
provenance: bash запрещён, вычислить digest было нечем. Harness вычислил и
предоставил package identity; авторы показали **новые** кандидаты r2/g2,
которые были приняты отдельно. Никаких выдуманных digest или записи старого
кандидата после изменения не было.

Сохранённые бандлы отдельно скопированы в три каталога **без установленных
скилов/шаблонов**: hashes совпадают, internal links и OKF/RIS проходят.
Это подтверждает независимость нормативного результата от installed package,
а не автоматическое нормативное подключение образца.

## Покрытие полного состава AC

Обозначения: W1 опубликован `34e9ade`, W2 `2d30772`, W3 `2384ccb`, W4 `8ae95b6`.
Прежние свидетельства сверены с исходными traces/audits и actual fixtures:
W1 — 12 observations вне RIS; W2 — 6; W3 — 26; W4 — 25 успешных observations.
Технический 500/timeout старого W4 не считается положительным свидетельством.
Точные критерии не заменяются количеством прогонов.

| AC | Свидетельство и наблюдение | Вердикт |
|---|---|---|
| 001 | W1/W2 create и W3/W4; новые Rails/игровые create без product/tracker/full design | PASS |
| 002 | W1 DragonRuby reset/Odin reuse; W2 scoped update; W3/W4 real bounded update/missing input, чужие нормы preserved | PASS |
| 003 | W1/W2 три профиля; новые реальные файловые результаты обоих авторов на Rails, DragonRuby, Odin | PASS |
| 004 | W1 principles/profile cases; новые ответственность/state/public contracts/dependencies, малый проект без инфраструктурного разрастания | PASS |
| 005 | W1 Odin interview/deferred; новые Rails без Service Layer, Odin renderer/ECS deferred | PASS |
| 006 | W1 game reuse justified/unjustified; новые DragonRuby/Odin нормативные consideration/extraction boundaries | PASS |
| 007 | W1 neighbor collision; W3/W4 related conflict без чужой записи; новые engineering ссылки на architecture, отдельные version/tool решения | PASS |
| 008 | W2 profiles/source rationale и existing-tool update; новые manual formatting/Minitest retained, неизвестная совместимость видна | PASS |
| 009 | W1 Odin prerequisite interview+answer, W2 engineering interview start, W3 create interview; confirmed ответы новых вызовов не повторяются | PASS |
| 010 | W3/W4 decline/no acceptance; новые separate acceptance, exact normative body, accessible decisions и package provenance | PASS |
| 011 | W3/W4 foreign baseline edit: zero writes; injected lost-ack/multi-file partial: actual reread, bounded partial, no blind retry | PASS |
| 012 | W3/W4 one-area create; новые оба порядка, neighbor bytes unchanged, shared index только навигация | PASS |
| 013 | W3/W4 scoped legacy-neighbor checks; полный образец и три новых целых бандла OKF/RIS/links | PASS |
| 014 | W3/W4 real worktrees: current overridden rules path, primary bytes unchanged; новые отдельные установки/defaults/override | PASS |
| 015 | W4 удаление base/profile без изменения saved rules; новые самостоятельные копии бандлов без всего package | PASS |
| 016 | W2/W4 existing transition policy; новые scoped obligations не называются исправлением кода или migration backlog | PASS |
| 017 | W1/W2/W3/W4 owner routing для audit/CI/library/design/impact/irrelevant; ближайшие чужие операции не выполняются | PASS |
| 018 | W1/W2 substantive proposals вне RIS, no normative writes/config/tracker; base источники неизменны | PASS |
| 019 | W3/W4 actual base и missing-base/OKF block; новые traces обоих авторов, usable resources | PASS |
| 020 | W1–W4 и новые proposal→accepted→saved, документные checks не названы implementation compliance | PASS |
| 021 | W1–W4 isolated installation; новые all resources installed, external source denied, один профиль/без чужого автора; source/installed parity | PASS |
| 022 | W2/W4 process preserved; новые только rules/index deltas, owner approval сохранён; no tools/code/CI/tracker writes | PASS |
| 023 | W3/W4 Markdown/0.1/future/unconverted inputs, включая acceptance после proposal: no hidden migration; scoped legacy соседа не переписан | PASS |

### Применимость прежних проверок к общей ревизии

Сравнение current source с опубликованными W1/W2: **никаких изменений** баз и
всех их профилей/интервью. W3/W4 получили только семь строк optional layout
illustration, не изменение алгоритма acceptance/write/format/conflict. Этот
новый путь реально проверен новыми create; остальные ветви bounded update и
ошибок сохраняют прежние инструкции/ресурсы. Обязательные common resources,
context/configuration, pinned OKF и interview также не изменены с W4; common
получил только необязательное описание asset. Форматная миграция собственного
корпуса RIS не изменила установленную методику. Эти причины позволяют
использовать прежние негативные/worktree/portable наблюдения, не выдавая их за
новые прогоны и не повторяя неизменённые дорогие сценарии.

## Пределы и завершение

Проверена одна среда/модель; принятие тестовых проектов выполнял явно
уполномоченный fixture channel, не реальный владелец игрового продукта.
Runtime/compiler/framework совместимость самих приложений, настроенный CI,
все версии стеков, полноценный естественный routing benchmark и соответствие
кода новым нормам не заявляются. Это пределы проверяемой поставки инструкций,
не пропуски её AC. Системные race гарантии не выводятся из file reread.

Независимое ревью конкретной поставки и этих свидетельств обязательно до
публикации. Родитель закрывается отдельно, только после W5 publication/closure
и повторной проверки полного обязательного состава W1–W5; Git и Dolt remote
results проверяются независимо. Отчёт не закрывает контейнер автоматически.
