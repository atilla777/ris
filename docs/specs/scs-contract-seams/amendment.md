# Поправка стыков публикации и продолжения RIS — ris-3hv

## Решение и область

Версия: **scs-contract-seams-v1**, 19.10.2026. Самостоятельная ordinary-задача
Beads `ris-3hv`, key `ris:scs-contract-seams:2026-10-19`.
Пользователь текущего ведущего диалога поручил исследовать и исправить четыре
связанные проблемы, отдельно разрешил локальный Beads-учёт **RIS** и ответил
«Принять (Recommended)» на полное предложение четырёх изменений ниже, включая
preflight/post-push FF и блокировку нового push при заранее известной невозможности
локальной синхронизации. Это принятие направления изменения контрактов, не
приёмка окончательного diff, независимое ревью или поведенческое доказательство.
Идентификатор ведущего диалога здесь не заявляется.

Разрешены исходники RIS, затронутая документация, локальные заметки/Beads RIS,
статические проверки и независимое read-only ревью. Не разрешены изменения scs,
его Beads, установка/переустановка пакета, commit/push Git или публикация Dolt.
Новые агентные эксперименты не разрешены и не требуются для проверки инструкций.

**Последующее разрешение публикации:** после получения локального результата и
независимого ревью без замечаний пользователь ответил «Публикуй!» на предложение
закоммитить/опубликовать Git, отдельно завершить `ris-3hv` и опубликовать Beads.
Затем выбрал «Полная публикация (Recommended)»: сохранить наш коммит, публиковать
из отдельной копии, безопасно вернуть чистую основную копию RIS на существующую
`main` при подготовке и после подтверждения push обновить её только FF. Это
адресное разрешение подготовки, не право публикатора молча переключать занятую
копию. Исходные ограничения выше описывают прежнюю фазу исследования; установка
пакета, изменения scs и новые поведенческие эксперименты по-прежнему не разрешены.
Разрешение не является доказательством фактической публикации или закрытия.

## Принятые изменения

1. **Полный Git-результат:** publisher сохраняет интеграцию/коммиты/конфликты в
   собственной ветке. До нового push проверяет primary identity/authority и
   безопасную возможность локального обновления; после независимого remote
   read-back повторно проверяет и только безопасно FF-обновляет уже выбранную
   локальную основную ветку/дерево. Не переключает занятую копию, не выполняет
   reset/pull/autostash, не перезаписывает tracked/untracked/ignored или чужую
   работу. Полный результат, remote published + pending local sync и явно
   ограниченный remote-only различаются. Последнее нельзя выбрать молча.
   Известная заранее невозможность полного результата блокирует новый push;
   проблема после push сохраняет remote effect и оставляет только local recovery.
   Конкурентное изменение требует свежей сверки; не обещается CAS произвольных
   filesystem writers или вечное равенство remote/local. При неустановленной
   безопасности копии — точный blocker, а не попытка принудительного обновления.
2. **Сохранённые входы:** project + exact ID, permanent slug/association и
   сохранённые immutable refs позволяют читать принятую версию/отдельное решение
   без предыдущего чата и receipt. Старый checkout — отдельная диагностика.
   Pinned read, applicability к целевой ревизии и copy preparation — разные
   действия. Нет второго реестра, mandatory receipt или ручного переноса между
   завершёнными этапами. Явная передача полного кандидата/решения остаётся для
   промежуточных unsaved/not-yet-discoverable результатов.
3. **Обзор:** до сравнения не начатого контейнера с потомками выявляется его
   собственный следующий результат. Если он не выявлен и работа уже представлена
   потомками, продвигается она, а не родитель по меньшему ID. Текущая собственная
   приёмка/сверка состава/иной результат контейнера не теряется; eventual финальная
   приёмка не конкурирует с ещё необходимой дочерней работой. Started, priority,
   directed blockers, assignee и явная область сохраняются; точный запрос по
   контейнеру не подменяется молча дочерним ID.
4. **Навигация:** необходимость результата проверяется до команды. Для epic
   сначала учитываются существующие features и существенные сохранённые результаты.
   Если вывод зависит от acceptance, читаются exact content и separate decisions.
   Принятые requirements+design без определённого состава работы поддерживают
   рекомендацию decomposition owner, который проверяет и one-task случай.
   Ссылка не acceptance, дизайн не implementation readiness, отсутствие детей не
   обязательство создавать детей. Нет второй жёсткой машины стадий/dispatch table.

Изменяются существующие RIS-specific владельцы и их реальные consumers, без новых
skills/portable layers. Общий условный source-reading resource принадлежит common,
проверка path/primary identity — context, FF completion — publisher, candidate
selection — show-plan, необходимость рекомендации — suggest-continuation.

**Альтернатива local-main-first отклонена:** она использует общую копию для
интеграции, увеличивает конкуренцию и меняет локальную main до возможного отказа
push. Post-confirmation FF сохраняет изоляцию и даёт честный recoverable partial
result без безусловного pull/reset/копирования файлов.

Это адресная поправка прежнего запрета менять local main при публикации и
parent/child tie-break. Исторические принятые spec/design/decisions по continuity,
plan-status и simplification не переписываются и не переобъявляются принятыми.

## Подтверждённые исходные факты

19.10.2026 выполнено только чтение scs: local main/HEAD
`9560cfd6a640e3dfe22275b3a026ca3645248bf0`; `git ls-remote origin refs/heads/main`
подтвердил `3755ca963bd198bd9ec60acb0c23c858410cfd34`. Локально untracked
`.opencode/`, `AGENTS.md`, `docs/`, `ris.yaml`; зарегистрирована preparation copy
`/tmp/opencode/scs-nrt-render-preparation` @ `3755ca9`. Точный read Beads:
`scs-vfl` epic/open/P2, `scs-vfl.1` task/current feature-record/open/P2, slug
`nrt-render`, оба published refs на `3755ca9`. Children feature=[], active typed
blocks feature/epic=[]. `git show` прочитал pinned `decisions.md`: самостоятельные
actual acceptance требований `nrt-render-requirements-v1` и дизайна
`nrt-render-design-v2`; историческое принятие v1 дизайна не перенесено на v2.
Это не проверка SC-реализации, достаточности test seams или execution readiness.

Исходные контракты publisher прямо запрещали обновление shared local main без
иного владельца синхронизации; show-plan сохранял ancestor/descendant как peers
для priority/ID tie-break. При этом требования читать linked accepted versions
и decisions **уже присутствовали** у continuation/decomposition. Поэтому
наблюдавшийся пропуск чтения — также ошибка исполнения существующего контракта;
её нельзя объяснить только отсутствием ещё одной инструкции. Поправка делает
опасные shortcut и диагностику stale checkout конкретнее, не доказывает, что
агент больше никогда не пропустит проверку.

## Восемь случаев: статическое сопоставление

Ниже — предписания новой редакции, **не результаты живых прогонов**.

| Случай | Ожидаемое предписание и владелец |
|---|---|
| 1. Epic + accepted requirements/design feature, состав не определён | show-plan не даёт ancestor выиграть по ID без own next result; continuation читает refs/decisions и рекомендует decomposition feature ID, не реализацию/обязательное создание детей |
| 2. Epic без выбранной feature | После достаточной проверки composition остаётся собственная необходимость feature selection; continuation сверяет действительный select-feature contract/command |
| 3. Container с собственным текущим результатом | show-plan сохраняет его кандидатом; status counters не подменяют принятие, не создаётся автоматический child preference |
| 4. Published docs, старый checkout | common published-inputs читает commit:path/decision; context диагностирует local-path gap; decomposition сравнивает с intended target отдельно, без синхронизации scs |
| 5. Proposed design / historical-malformed record | Нет acceptance по ссылке/флагу; adapter diagnostic сохраняется, dependent readiness/writes не утверждаются |
| 6. Busy primary / untracked collision | Publisher preflight блокирует новый full push; post-push drift даёт partial с сохранённым remote, защищает файлы и не повторяет push |
| 7. Полная публикация | Publisher требует remote read-back + safe FF + local tree/status/protected paths read-back + equality с последним observed remote tip; future races не исключены |
| 8. Новая сессия: project + ID | Common, specify/design/decompose и prepare completion используют saved identity/refs/decisions; chat/ignored notes/receipt не обязательны для сохранённых входов |

Соседние/direct calls: select-feature не требует новой спецификации для уже
подготовленной feature; direct publisher и no-change/recovery сохраняют full/local
gate; prepare/specify/design/execution/simple/init потребляют изменённый Git-result,
не копируя FF-алгоритм. Read-only next/status/context ничего не обновляют;
document-only/intermediate local save не превращается в full publication.

Статические проверки и независимое ревью фиксируются по фактическому результату
в локальных заметках ris-3hv и кратком Beads-итоге. Установка и source/install
parity этой редакции не выполнены ввиду явного ограничения; расхождение должно
быть показано, не объявлено pass. Новых live/scenario/behavioral tests нет;
надёжность, стоимость, runtime concurrency и повторяемость не установлены.
