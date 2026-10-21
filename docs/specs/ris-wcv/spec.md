# Фича без JSON-карточки в Beads
Feature-ID: ris-wcv
Summary: Документы и фактические принятия вместо дублирующего реестра готовности фичи.
Keywords: Beads, feature, acceptance, simplification

## Требования — S1

- **AC-001:** обязательная JSON-карточка `ris.feature-record/2`, её producers,
  consumers, дублированные accepted refs и verification/readiness registry сняты.
  Beads хранит обычные цель, границы, критерии, состояние и зависимости.
- **AC-002:** по выбранным project/config и точному feature ID обнаруживаются
  реальные требования, достаточный inline/отдельный дизайн и их фактические
  независимые принятия. Директория нового документа устойчива к смене заголовка.
- **AC-003:** verify-and-close проверяет все критерии, обязательный состав,
  применимость evidence к интегрированной ревизии и активные блокеры; при успехе
  выполняется native exact close без обязательного сохранения verification или
  заменяющего реестра. Краткий обычный итог допустим. Verify без close read-only.
- **AC-004:** старые JSON, проза, документы и история остаются нетронутыми;
  отсутствие, старый или malformed JSON сами по себе не блокируют новый маршрут.
  Нет schema gate, совместимого parser API, миграции или массового переноса.
- **AC-005:** затронутые producers/consumers, актуальные документы и изолированные
  source/install mirrors согласованы. Содержательное принятие, ownership/claim,
  copy, независимое ревью, Git/primary-sync, exact close и Dolt gates сохранены.
- **AC-006:** нет нового обязательного JSON/YAML/metadata/sidecar-манифеста,
  registry или журнала взамен. Product/functionality index явно отложен.
- **AC-007:** аудит task/epic/bug/review структур отражён ниже. Bug snapshot не
  удаляется; его упрощение — отдельное предложение. `ris.review/1` не меняется.

Document-only, ordinary standalone и native bug сохраняют собственные контракты
и пути; feature ID/каталог им не выдумываются. Feature kind устанавливается по
явно выбранной области, реальному содержанию/источникам и релевантным нативным
связям, не по JSON, названию или одному child-parent отношению.

## Согласованные решения — D1

1. Новые документы: `sources.specs/<full feature ID>/spec.md`; default specs root
   `docs/specs/`. Никакого суффикса/slug по названию; смена title не двигает каталог.
   Требования в spec.md, достаточный дизайн — различимая область там либо соседний
   design.md. Existing legacy ссылки не требуют переноса.
2. Новый spec.md начинается Markdown H1 с читаемым именем, затем column-zero
   `Feature-ID: <ID>`, `Summary: <одна строка>`, optional
   `Keywords: <термины через запятую>`. Labels английские, содержание — язык проекта.
   Не вводятся YAML/frontmatter, sidecar или индекс функций.
3. Сохраняется существующая notation принятия: каждый полный requirements/design
   scope имеет точные path/semantic section/version и отдельное attributable
   решение. Один акт может явно принять обе полные различимые области. Литерал
   `containing-commit` разрешается по исходному commit решения; копирование не
   возобновляет принятие. Исходная provenance сохраняется ссылкой либо выясняется
   ограниченным чтением Git history; новая notation/acceptance manifest не нужны.
4. Legacy explicit source links и читаемые payload paths/refs — лишь подсказки.
   Проверяются действительные документы и решения; неоднозначная идентичность,
   недоступный источник или недоказанное принятие блокируют только зависимый шаг.
   Не строится parser/миграционная подсистема ради прежнего JSON.
5. Адресная замена прежних норм совместимости: для нового document route больше
   не действуют требования JSON `/2`, slug/spec pin, duplicate refs, saved
   verification и schema-based no-write refusal. Исторические спецификации,
   `feature-record-compatibility.md`, payloads и evidence не переписываются;
   это снятие capability, не новая `/3` или dual-schema API. Остальные проверки
   принятия/применимости и публикации остаются.
6. Пересечение ris-xxd: снятая feature-record pin/verification machinery делает
   относящиеся к ней AC-017–019 устаревшими; новый collision registry не создаётся.
   Сохраняются ordinary create/retry identity reconciliation, проверка destination/
   identity и расширение discovery по признакам конфликта. Реализация ris-xxd не
   выполняется и её критерии не объявляются выполненными. Пользователь отдельно
   разрешил административно закрыть **именно ris-xxd как obsolete только после
   проверенного удаления в ris-wcv**, без переписывания её содержания.

## Основание принятия

Уполномоченный пользователь ведущего диалога ris-wcv 21.10.2026 явно принял
S1: исходный bounded remove-JSON результат и ограничения; D1.1–4: решения
идентичности/заголовка, сохранение фактической notation принятия и bounded legacy
discovery; D1.5: scoped supersession без переписывания истории; D1.6: предложенный
overlap disposition и отдельное отложенное административное закрытие ris-xxd.
В поручении реализации эти принятые решения повторно переданы исполнителю;
разрешено сохранить их здесь. Это запись их принятого содержания, **не утверждение
о предварительном одобрении пользователем всех формулировок этого файла или
любых дополнительных implementation choices**. Published адреса этого документа
и решения ещё не установлены до Git-публикации. Факт выполнения, независимого
ревью или публикации из данного решения не следует.

## Аудит аналогичных структур

- **Feature:** прежний adapter `references/feature-record.md` владел JSON с
  identity/requirements/design/verification. Дублирование refs в verification и
  mandatory record-verification/read-back перед close — снимаемая часть.
  Обнаружение и фактическое принятие документов сохраняются у project owners;
  переносимые formulation/design/decomposition/verification методы не заменяются.
- **Ordinary task/container:** adapter `references/standalone.md` не требует
  аналогичную JSON-карточку; own outcome/scope/criteria и ordinary result сохраняются.
- **Epic:** completion `references/epic.md` запрещает второй registry; own
  mandatory outcomes/composition и checks сохраняются, не заменяются feature schema.
- **Native bug:** `references/bug-execution.md` требует полный immutable historical
  execution-input snapshot в notes с report/criteria/decisions/design. Он не JSON
  и не второй текущий report, но копирует полное содержание. Current investigation
  report имеет одного владельца; file-backed вариант не создаёт конкурирующую копию.
  **Snapshot остаётся обязательным без изменения текущего контракта.**
- **Review:** `ris.review/1` — отдельный локальный YAML независимого ревью;
  Beads хранит адрес/раунд, не копию verdict/findings. Не часть снимаемой карточки.
- **Технические форматы:** `bd --json`, Worktrunk JSON, `ris.yaml`, OKF и
  installation formats не являются реестром готовности фичи и не удаляются.

### Отдельное предложение по bug snapshot — не принято

Для file-backed immutable published report/design можно рассмотреть ссылки на
точные repository/full commit/path/semantic section и фактические решения вместо
повторения всего текста. Mutable tracker-backed входы без независимо восстанавливаемой
версии по-прежнему нуждаются в полном историческом содержании. Это снижает
дублирование, не теряя воспроизводимого основания, но требует отдельного принятия
recoverability/access/consumer контракта. Сама ссылка на текущий mutable report
не равноценна historical snapshot. Здесь предложение не реализуется.

## Проверка изменения

Чтение и адресные static checks producers/consumers, имён/ресурсов/ссылок,
source/install parity, актуальных норм и final diff; затем реально независимое
ревью. Executable changes требуют применимых ordinary program checks/TDD.
Никаких live/scenario tests поведения агентов. Статика не доказывает runtime
поведение, надёжность, экономию или повторяемость; исторические evidence сохраняют
исходные версии и ограничения. Этот документ не является implementation-report.
