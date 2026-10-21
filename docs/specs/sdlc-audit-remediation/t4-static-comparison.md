# T4 — статическое сравнение инструкций и условий загрузки

Основание: T4, AC-013–016 и общие ограничения
[`spec.md`](spec.md) в принятой версии
`ff79c496b733756a86003b44e70eb72c60efa532`, отдельное решение V1 там же.
Сравниваемая исходная реализация:
`564375b22f3e2d70a1437793e147fe422b9d02eb`.
После — сопровождающая этот документ редакция исходников; это не новая версия
требований, решение принятия или журнал исполнения.

## Границы и владельцы (AC-013, AC-015)

| Повтор / предмет | До | После / сохранённый gate вызывающего |
|---|---|---|
| Применимость saved review | Flow и publisher повторяли подробности формата/history consumer | Короткий вызов `ris-proj-op-review-task/references/report-format.md` с expected subject, purpose, tree/base/exclusions, inputs/checks и actual launch/all-author evidence; вызывающий требует внешний approval gate, не verdict |
| Tracker publication | Full flow пересказывал confirm-first, S/L/R, new-write и remote-read алгоритм адаптера | Flow передаёт разрешённую область, destination, точную required/recovered revision и evidence; требует свежего remote confirmation. Полный алгоритм остаётся в adapter `references/dolt-publication.md` |
| Primary return/FF | Fast повторял часть publisher preflight/completion | Fast передаёт проверенную primary/subject/copy/branch association и полномочия; требует remote и local evidence. Guards остаются у publisher в неизменённом `references/primary-sync.md` |

Сходные слова не означают одинаковый предмет проверки: свежие claim/children/
blockers перед правками и публикацией, точный review subject, независимость всех
авторов/исправителей и remote/local read-back остаются отдельными gates.
Не изменены portable bases, common/context, границы standalone операций или
выбор ролей. Новый слой/flow/реестр/журнал и обязательный implementation report
не вводятся. Уже доступные актуальные инструкции переиспользуются по common;
publisher и review wrapper явно напоминают об этом. Ресурсы разрешаются относительно
своего installed skill, не относительно RIS checkout.

## Условия чтения и сохранность маршрутов (AC-014, AC-016)

Это сравнение предписаний чтением, **не исполнение запросов агентами**.

| Запрос / ветка | До → после | Сохраняемый результат / отказ |
|---|---|---|
| Обычный fresh fast, ясный ordinary ID, свободная своя ветка, session-only review | Bug-подробности находились в обязательных main-файлах review/publisher, feature-preparation exception — в claim. Теперь они в условных owned resources. YAML-правила явно не загружаются без saved review | Достаточные входы, собственная ветка, актуальные claim/composition/blockers, содержательные checks, реально отдельный reviewer, reassessment изменённого whole tree, Git и раздельные tracker effects |
| Fast с optional saved review / обычный full task | Сохраняется report-format; потребители обращаются к его алгоритму вместо копии | Полный YAML, exact round, validity отдельно от внешней применимости, no verdict-only approval, safe append/read-back. Full flow не получает fast no-file exception |
| Повторное review, prior dispositions, конфликт history | Детальный алгоритм был inline в report-format; теперь явное условие чтения `review-history.md` рядом с ним | Все prior finding IDs, chronological previous links, reasoned disposition; later adverse/invalid/unknown запрещает fallback. Формат/валидатор не меняются |
| Нужна отрицательная иллюстрация формата/history | Таблица всегда находилась в report-format; теперь optional `report-examples.md` | Синтетические oracles сохранены, не выдаются за evidence. Полный исходный YAML example остаётся byte-identical в report-format, поскольку его читает существующий program-test fixture |
| Native bug: pre-execution document либо fix, включая mixed fix/docs | Inline review/publisher ветки вынесены в собственные `references/bug-subject.md`, читаемые до выбора basis при supplied native bug | Document branch не требует будущего execution snapshot и не принимает дизайн/фикс; fix/mixed требует полного historical snapshot и сравнения с current report/criteria/decisions. Subject-specific gates обоих владельцев сохранены, не слиты в общий алгоритм |
| Feature-preparation claim | Inline exception вынесен в adapter `claim-preparation.md`, читаемый до admission/own-claim reuse только при явно выбранном purpose и подтверждённой feature | Каждый active blocker должен быть доказан execution-only для конкретного разрешённого preparation action; обычное execution такого исключения не получает |
| Resume, interrupted/ambiguous effects | Существующие fast recovery/tracker и full recovery/evidence ресурсы остаются условными, без нового recovery engine | Reconcile actual effects до retry; confirmed push/close не повторяется; недоступные essential evidence/association/independence блокируют только зависимое действие |
| Dirty context, exclusions, ambiguous snapshot membership | Существующие portable implementation/review `references/publication-snapshot.md` остаются условными | Полный prospective subject, predeclared exclusions, base bytes для excluded tracked paths и отдельная applicability фактически проверенных bytes; нет after-the-fact exclusions |
| Соседний portable review без RIS | Portable base не изменён и не получает RIS-зависимостей | Read-only semantic assessment без YAML/config/tracker; не сохраняет проектный отчёт и не публикует |
| Соседние Documents/pre-ID и bug design | Publisher оставляет явный Documents subject, без fabricated ID/future implementation evidence | Independent whole-tree document review, требуемое отдельное content acceptance и все Git gates |

T1 primary-sync, T2 same-copy design/execution, T3 self-review/validator и T7
delegated-role/actual-independent-launch контракты сохранены. T6 сохраняет отдельную
execution readiness, не следующую из создания задачи. T5 отменена принятой ris-wcv:
feature registry, pin и saved verification не возвращаются.

## Объём текста — не токены и не время (AC-016)

Подсчёт: UTF-8 bytes и строки (`splitlines`) точных файлов относительно baseline.
Каждый файл считается один раз. Это выбранный затронутый текст, **не весь prompt**,
не наблюдение фактической загрузки и не оценка токенизатора.

| Файл под `skills/` | Строки до → после | Bytes до → после |
|---|---:|---:|
| `ris-proj-flow-execute-simple-task/SKILL.md` | 182 → 176 | 12771 → 12306 |
| `ris-proj-op-review-task/SKILL.md` | 140 → 118 | 9725 → 8082 |
| `ris-proj-op-publish-task/SKILL.md` | 218 → 197 | 15743 → 14003 |
| `ris-proj-adapter-beads-tasks/references/claim.md` | 50 → 43 | 3508 → 2942 |
| **Эти четыре файла обычного tracked fast** | **590 → 534** | **41747 → 37333** |
| `ris-proj-flow-execute-task/SKILL.md` | 343 → 337 | 23773 → 23314 |
| `ris-proj-op-review-task/references/report-format.md` | 259 → 240 | 17669 → 15667 |

Другие инструкции маршрута (common/context, adapter, implementation base, tracker,
publisher primary-sync и т. д.) в эту сумму не включены и не объявляются исчезнувшими.
Четыре файла сокращены на 56 строк / 4414 bytes независимо от трактовки прежней
загрузки YAML на fast: эта неоднозначность теперь снята явным saved-file условием.

Пять новых условных ресурсов: claim-preparation — 20 строк / 1280 bytes;
publisher bug-subject — 32 / 2045; review bug-subject — 28 / 1986;
review-history — 21 / 1356; report-examples — 25 / 2273.
Все затронутые инструкции вместе с новыми ресурсами: 1192 → 1237 строк,
83189 → 85254 bytes. Общий source объём **увеличен** на пояснения условий и границ;
сокращается текст обычных вызывающих, а не весь пакет любой ценой. Этот документ
сравнения не входит в operational instruction totals.

## Проверки и пределы

Проверяются полный diff, имена/frontmatter, существование owned ресурсов и
ссылок, dependency direction/availability, точные условия чтения и сохранность
соседних/условных предписаний. YAML example, scripts, requirements и tests не
меняются; новые program/agent tests для текстовой поправки не добавляются.
Независимое review и последующие Git/close/Dolt gates остаются отдельными действиями.
Installed `.opencode` не синхронизируется: это отдельная T8. Source-ready не означает
observed agent behavior, измеренную скорость, стоимость, надёжность или runtime
совместимость; такие выводы из этого сравнения не следуют.
