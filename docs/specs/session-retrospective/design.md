# Технический дизайн session-retrospective

Версия `session-retrospective/design-v2`, узкая поправка принята пользователем
14 октября 2026 года: [решение design-v2](acceptance.md#решение-design-v2).
Предшественник design-v1 — Git `de208d617de8d9d71c31b11b2316342aba7b7f41`;
историческое [решение design-v1](acceptance.md#решение-design-v1) сохраняется
по первоначальному адресу. V2 локальна, immutable refs ожидают Git-публикации.
Фича `ris-01r.2`, открытый эпик `ris-01r`. Адрес принятого результата:
`docs/specs/session-retrospective/design.md`, весь файл.

## 1. Входы, baseline и результаты исследования

Этот раздел сохраняет baseline и результаты **исследования v1**, не описывает
текущее состояние очереди или новые выполненные проверки. Вход текущей v2 —
локально принятые requirements-v2, `spec.md` целиком и отдельное решение
[requirements-v2](acceptance.md#решение-requirements-v2). Поправка касается
только CLI-служебных эффектов/AC-013; прежние требования применимы в остальном.
Основания поправки, влияние на потребителей и новые проверки — §11.

Принятые требования v1: `docs/specs/session-retrospective/spec.md`, section null,
Git `af3ec62dcf7207a7798a28d6f66a78dfeaffad81`; отдельное решение requirements-v1:
https://github.com/atilla777/ris/blob/af3ec62dcf7207a7798a28d6f66a78dfeaffad81/docs/specs/session-retrospective/acceptance.md#решение-requirements-v1.
Содержание и решение прочитаны, diff рабочей версии требований пуст;
fetch origin и ancestry origin/main подтверждают опубликованный commit.
Исходную requirements reference сохраняем целиком без repin.

Исследован RIS на том же HEAD, конфигурация — корневой `ris.yaml` v2:
sources.rules `docs/rules/`, sources.specs `docs/specs/`, adapter
`ris-beads-adapter`. Sources.product `docs/product/` отсутствует: concepts
не подменяет авторский product. Это ограничение product currency, а не
блокировка проектного дизайна по принятым требованиям и действующим правилам.
Полная очередь всех состояний, эпики, дети и прямые blocks прочитаны:
у ris-01r.2 детей и прямых блокеров нет; зависимость эпика от ris-p20 сохранена.

Применимые нормы: `docs/rules/development.md`,
`docs/rules/architecture/repository.md`, `docs/concepts/01-architecture.md`
и `05-adoption-and-validation.md`. В рабочей копии есть незавершённая
поставка ris-01r.1.1 и её изменения README/concepts/config/ris-execute-task;
они не выдаются за опубликованную реализацию. Активный принятый соседний
дизайн task-execution: `docs/specs/task-execution/design.md` на
`4fb35ee0ff469b53717311f613ab4d61fb0f9ac0`; общий контракт не меняется.

Технический baseline — OpenCode 1.18.33. Проверены CLI help/list и экспорт
одной ранее остановленной сессии ses_ec99eb1a0ffegeOIwokodnKBAw:
34 сообщения, 32 step-finish, 75 tool parts. Два task-вызова ссылались на
одну ветку ses_ec999c8a0ffeRZV2SjFsq64ayR; её отдельный экспорт содержит
13 сообщений и совпадающий info.parentID. Родительский экспорт не содержит
самих сообщений ребёнка. Это проверка источника, не ретроспектива этих сессий.

Проверены исходники OpenCode тега v1.18.33:
- [export.ts](https://github.com/anomalyco/opencode/blob/v1.18.33/packages/opencode/src/cli/cmd/export.ts):
  export = {info,messages}; sanitize удаляет текст, tool input/output/metadata;
- [session.ts CLI](https://github.com/anomalyco/opencode/blob/v1.18.33/packages/opencode/src/cli/cmd/session.ts):
  list использует roots:true, не перечисляет субагентов;
- [session.ts](https://github.com/anomalyco/opencode/blob/v1.18.33/packages/opencode/src/session/session.ts):
  children по parentID, messages без limit проходит страницы; getUsage
  отделяет noncached input, cache read/write, output и reasoning;
- [message-v2.ts](https://github.com/anomalyco/opencode/blob/v1.18.33/packages/opencode/src/session/message-v2.ts):
  model history фильтруется/преобразуется отдельно от экспортируемой истории;
- [task.ts](https://github.com/anomalyco/opencode/blob/v1.18.33/packages/opencode/src/tool/task.ts):
  state.metadata содержит sessionId/parentSessionId; повторный task_id
  может продолжать того же ребёнка.

Проверены [публичные GET API](https://opencode.ai/docs/server/): session,
status, children, messages. Работающего OpenCode HTTP listener в этой среде
не обнаружено: реальные GET/вложенное дерево не проверены, это seam поставки.
CLI export в pipe дал обрезанный JSON (139264 bytes), при выводе в обычный
исследовательский файл JSON был полон. Не обобщаем это до всех установок;
в будущем reader обязан валидировать JSON и не считать exit 0 полнотой.
Дополнительно проверен capture через Python os.memfd_create и subprocess:
exit 0, 141413 bytes полного sanitized JSON, 34 сообщения. Постоянный файл
экспорта для этого прогона не создавался. Это подтверждает способ в данной
Linux-среде, не универсальную гарантию или готовность будущего reader.

Установлен локальный Langfuse observability plugin 0.4.0:
`dist/index.js` traceGeneration использует session.id, metadata.messageID,
parentID и usage input/output/reasoning/cache_read/cache_write.
Локальный retrotrace-langfuse.js задаёт service.name из project.id и имени.
Это факты данной установки, не обязательные атрибуты любого проекта.
Live Langfuse API и полнота телеметрии не проверялись; никакой новый SDK,
плагин или сервер фичей не устанавливается.

## 2. Компоненты и ответственность

Публичные имена: **ris-retrospect-session-base** и **ris-retrospect-session**.

| Владелец | Ответственность |
|---|---|
| База | Переносимый обзор истории, эпизоды, причинный анализ, метрики по их объявленной семантике, предложения и структура отчёта |
| RIS-обёртка | Точная сессия/проект, получение веток, context, исторические/current материалы RIS, применение базы, проверенный общий отчёт |
| Reader внутри обёртки | Детерминированное read-only получение/индексирование OpenCode, адреса событий, расчёт известных метрик и контроль охвата |
| ris-context / common | Настройки и существующие общие правила, только по условиям их контрактов |
| Условные исполнители | Ограниченное исследование ветки/эпизода, без владения итогом и без побочных эффектов |

Reader — небольшой `scripts/opencode_read.py` на Python 3 standard library,
не новый скил-адаптер и не workflow engine. Его самостоятельная причина —
большие JSON, точные адреса, корректное объединение интервалов/usage и
необходимость воспроизводимых проверок вместо одноразовых SQL/скриптов.
Никакой предметный диагноз, рейтинг или рекомендация в reader не переносится.
База не зависит от этого скрипта или от OpenCode; ей достаточно истории
и понятных адресов/ограничений в произвольном представлении.

Направление: обёртка → common/context + база; reader принадлежит обёртке.
База не вызывает wrapper/context/Beads/Langfuse. Общая методика не копируется.
State owners неизменны: исходники истории принадлежат среде, документы Git,
задачи выбранному tracker. Индекс/карта анализа не становятся реестром.

## 3. Входной и выходной контракты

Прямой вход обёртки: выбранный project root; точный session ID **либо**
адрес предоставленного экспорта; optional exports детей, cutoff, разрешённый
существующий endpoint, отдельные телеметрические свидетельства и report path.
Beads ID и execution role не обязательны. Если ID отсутствует, короткий список
root sessions выбранного проекта (по умолчанию 5) и один вопрос выбора.
Название и совпадение текста не устанавливают session/project identity.

База получает семантически определённые, а не обязательно JSON-входы:
- цель и изменения задания; участники и доказанные связи;
- история с адресами, последовательностью/временем, содержанием и статусами;
- источники/версии/cutoff, доступность и просмотренный охват;
- usage и интервалы с единицами/семантикой, неизвестными полями;
- полученные исторические инструкции отдельно от текущих материалов;
- ограничения чтения, редактирования выдержек и доступа к источникам.

Обёртка может передать это по частям/через адреса, не загружая весь журнал
за один запрос. Отсутствующее значение = неизвестно, не 0/успех/отсутствие.
Адрес OpenCode: session ID / message ID / part ID; usage — step-finish ID;
Langfuse — trace ID / observation ID; документ — repo/path/revision/section.
Для чужого формата допустимы устойчивые номера событий/диапазоны строк.

Reader возвращает машинно проверяемые overview/pages/detail/metrics:
source identity/version/fingerprint, participant links, диапазоны и gaps,
event references, known metrics с provenance/quality. Неподдерживаемая схема,
обрезанный JSON, расхождение ID, изменившийся snapshot — явная ошибка/конфликт
со сохранением независимого результата, без молчаливого пропуска.

База возвращает карту, покрытие, классифицированные эпизоды, findings,
hypotheses, justified signals и limitations. Обёртка перечитывает ключевые
основания, устраняет дубли и выдаёт один отчёт по spec §9.
Готовый полезный отчёт может иметь неполный охват; полный охват не заявляется
без соответствующих свидетельств. После отчёта операция останавливается.

## 4. Получение истории и snapshot

Приоритеты: предоставленный экспорт → штатный `opencode --pure export ID`
→ GET API **уже доступного явно выбранного** сервера для недостающих данных.
CLI запускается в выбранном проекте, version проверяется. --pure подавляет
внешние плагины, но сам по себе не доказывает допустимость иных side effects;
проверка initialized read path по scoped oracle §9 входит в приёмку.
Фиксированный allowlist, shell=False, без argv из transcript:
`opencode --pure --version`, `opencode --pure export <точный sessionID>` и
`opencode --pure session list --format json --max-count 5` (выбор, не auto-export).
Разрешены лишь runtime metadata проекта, housekeeping существующей БД/WAL
и логи OpenCode по §8 вне разрабатываемого проекта. Read-path fitness и
разрешение CLI проверяются до вызова; `--allow-cli` не заменяет их и не
разрешает произвольные записи. При неизвестных/выходящих за границу эффектах
CLI остаётся gated. Если установка требует
bootstrap/migration, read-only операция использует переданный экспорт и
сообщает ограничение. Не запускать новый serve, не import и не читать SQLite
напрямую. В данной поставке SQL не является запасным способом чтения истории.

Reader принимает export/stdin либо вызывает разрешённый CLI/API. Все данные
обрабатываются в памяти; собственные временные файлы и кэш на диске не нужны.
Для Linux stdout большого CLI export можно захватить в anonymous memfd
(os.memfd_create), затем проверить полный JSON: это RAM, не файл проекта
и не постоянный scratch. На других платформах обычный capture pipe с такой
же валидацией; при обрезании — доступный GET/предоставленный экспорт, не
самовольная запись журнала на диск. Capture memfd проверен на одном реальном
экспорте данной среды; надёжность будущего reader на больших/ошибочных данных
проверяет контрактный сценарий поставки, без него полнота для всех установок
не обещается.

Reader не создаёт daemon/server. При последовательных CLI-запросах повторное
чтение сверяется по fingerprint: страницы разных снимков не смешиваются.
Приёмка проверяет время/память и отсутствие лишних чтений на длинной fixture;
нет обещания потокового парсинга произвольно больших JSON. При исчерпании
лимита памяти/API/контекста показываются граница и непросмотренное.

Для snapshot фиксируются время получения, session.time.updated, последние
message/part IDs и fingerprint выбранного содержания (локальная техническая
идентичность, не новый published evidence protocol). GET status, если доступен,
и отсутствие новых событий объясняют текущую остановку, но не доказывают успех.
Если остановка не доказана или история возобновилась — отчёт о явно обозначенном
snapshot/cutoff, не обо всей завершённой сессии. Событие, пересекающее cutoff,
сохраняется как незавершённое; поздние поля не переносятся назад во времени.
Пользовательский экспорт сам задаёт снимок; отсутствующие timestamp/версии
вносятся в gaps. Стабильный повторный экспорт не является атомарной блокировкой.

Различаем snapshot, действительно захваченный на границе, и исторический
cutoff, запрошенный позже на текущем экспорте. Второй не восстанавливает версии
изменяемых записей: step-finish не имеет собственного timestamp, текстовое
время опционально, metadata связи не датирует момент её появления.
Для исторического cutoff поле используется только при доказанной временной
принадлежности (например, завершённый до границы шаг с подтверждённым
интервалом либо отдельный захваченный тогда снимок). Пересекающиеся tool/text
parts и недатированные изменяемые поля показываются как доступные в позднем
снимке с неизвестным состоянием на cutoff; их результат/usage не входит
в точные исторические итог/peak/sums. Недатированный step-finish нельзя
датировать по его ID или позиции без дополнительного основания. То же правило
действует для child linkage: поздняя/недатированная связь не доказывает
участие до cutoff; такая ветка и её метрики отделяются от подтверждённого
исторического охвата. Данные не удаляются из карты gaps и поздних свидетельств.

Дерево: читаем task parts, state.metadata.sessionId/parentSessionId и проверяем
info.parentID отдельного экспорта; API children рекурсивно дополняет обнаружение.
Visited set устраняет повторные task_id и предотвращает циклы; каждый ребёнок
имеет своё покрытие/cutoff. Task reference к чужой parent-сессии отмечается
как связанная ветка с ограничением, не переписывает ancestry. Подтверждённые
вложенные ветки включаются. Отсутствующий ребёнок, удалённый task part,
неполная enumeration или недоступный API означают неполноту дерева.
Fork без подтверждённого task/parent linkage не добавляется по похожему тексту.

Sanitized export принимается, но redacted текст и linkage — gaps; он не
позволяет полноценно объяснить скрипты/инструкции. На локальном полном источнике
redaction применяется к показываемым выдержкам; нельзя объявлять --sanitize
достаточной гарантией удаления любых секретов (например, error/default parts).

## 5. Обзор, углубление и исторические материалы

1. Обзорно пройти все доступные страницы всех доказанных участников, сохраняя
   карту событий и coverage ranges. Индекс перечисляет все события, а обзор
   читает их содержательные страницы; список метаданных не считается обзором.
2. Завести реестр эпизодов: каждый script/SQL/обход обязан получить итог
   «исследован / оправдан / проблема / неизвестно из-за gap». Независимые
   сигналы ошибок, SDLC, делегирования, времени, контекста и вредных требований
   выявляются даже при отсутствии числовых превышений.
3. После обзора углубить выбранные диапазоны, ссылки на входы/инструменты,
   handoff и фактический результат. На очень длинной истории допускается
   промежуточный анализ с точным неполным охватом, без заявления завершённого
   обзора и окончательного отсутствия находок.
4. Проверить альтернативы и причинность; целевой текущий документ читается
   для каждого подтверждённого дефекта, не сканируется весь проект.

Reader выдаёт страницы с устойчивыми ID и continuation; большое содержимое
одного события делится по диапазонам, omission явно обозначен. Поиск сигналов
помогает навигации, но не заменяет просмотр остальных событий. Compaction
summary/pruned tool output не восстанавливают утраченный оригинал.

Исторические tool skill/read outputs доказывают полученное содержание.
Указанный Git commit/file history может восстановить материал, но сам файл
на этом commit не доказывает загрузку. Системные инструкции/tool schema,
не сохранённые в export, остаются неизвестными; текущий SKILL.md не является
их исторической копией. Доступные Langfuse generation input — дополнение,
также с проверкой полноты, а не гарантированный полный system prompt.

Для скрипта/обхода сравниваем потребность, реально доступный интерфейс тогда,
его обнаружимость, наблюдаемые издержки и риски. Необходимая разовая обработка
данных оправдана; недостаток операции принадлежит адаптеру/инструменту;
необнаружимость — навигации; игнорирование доступного интерфейса — отдельная
причина. Итог задачи сверяется только с требовавшимися тогда критериями.
Beads read через выбранный adapter нужен лишь при конкретной связи эпизода
с задачей; отсутствие tracker не мешает остальному анализу. Текущий статус
не доказывает исторический статус. Git чтения — show/log/diff, не fetch/push
как автоматическая часть будущей ретроспективы. Никакие тесты не повторяются.

## 6. Метрики и доказательность

Для OpenCode 1.18.33 единица запроса — step-finish; при одном проверенном шаге
можно использовать message.info.tokens как fallback. Нельзя складывать оба
представления одного шага. Для нескольких шагов в сообщении message usage
не считается суммой/пиком без установленной семантики.

input-context = tokens.input + tokens.cache.read + tokens.cache.write:
getUsage сохраняет noncached input отдельно. Output/reasoning не входят во
входной контекст; tokens.total может включать output. Session.info.tokens —
aggregate, не отдельный запрос. По каждому участнику отдельно: max known
request context, coverage запросов, sums неперекрывающихся usage и cache.
Для исследованной сессии max=164301, тогда как session cache.read=3501824:
пример показывает различие peak и aggregate, не оценку эффективности.

Эта формула применима только к подтверждённой семантике версии/источника.
Неизвестная версия или пропущенное поле дают unknown/estimate, а не 0.
Нулевые значения могут означать default SDK, не достоверное измерение.
Измеренный или оценочный peak строго >150000 обязательно углубляется;
приближение отмечается. Если известные поля дают лишь нижнюю границу >150000,
сигнал всё равно исследуется; отсутствие полного peak не позволяет исключить
превышение. Граничные 150000 и 150001 проверяются отдельно.

Время: wall span событий, не просто session.updated-created, отдельно known
intervals model generation, tools, retries/recovery и ожидания. Message
created/completed может включать tools; это elapsed assistant span, не чистая
генерация. Langfuse generation timing используется лишь после проверки типа.
По категориям считаем union интервалов; общий active union across participants
не складывает родительский task wait и работу ребёнка дважды. Категории могут
пересекаться и не обязаны складываться в wall time. Human/external wait только
по свидетельствам; неразмеченный остаток = unclassified, не потеря. Нет
абсолютного порога длительности. Generation duration не называется thinking.

Каждая находка имеет независимые confidence(problem) и confidence(cause),
например high/medium/low с основанием; это не статистические вероятности.
Severity high/medium/low выводится из последствий, не токенов/уверенности.
Причина-гипотеза сохраняет альтернативы и missing check; наблюдаемые последствия
отделяются от рисков. Проверка current applicability: сохраняется/устранена/
неизвестно. Предложение содержит owner, episode refs, механизм изменения,
проверку улучшения и стоимость (контекст/действия/сопровождение).

## 7. Langfuse и делегирование — условные ветки

Langfuse читается только для конкретного gap или эпизода и при доступном
разрешённом источнике. Условный ресурс обёртки загружает installed langfuse
для schema/help и bounded list/get; отсутствие skill/auth/API оставляет локальный
анализ полезным. Не используется полный workflow retrotrace за семь дней.
Runtime discovery проверяет доступную версию CLI/API, фильтры и pagination;
фича не закрепляет неподтверждённую версию чужого CLI и не добавляет SDK.

Join: repository/service identity + точный session ID; generation по messageID,
tool по callID, если source schema его предоставляет. Текст/time proximity
не заменяют ID. При plugin 0.4.0 cache metrics повторяют OpenCode, а не новое
независимое измерение; fallback total в plugin не включает cache и не используется
как peak. Дубликаты относятся к одному event; конфликтующие значения сохраняются
с provenance, не усредняются. Подробности fetch только нужного эпизода,
неизвестные связи исключаются из числового объединения. Live join остаётся
обязательным интеграционным сценарием, не утверждается проверенным сейчас.

Привязка observation к сообщению и соответствие конкретному запросу — разные
отношения. MessageID сам по себе не связывает observation с step-finish.
Числовое дополнение неизвестного local step usage допустимо только при
доказанном one-to-one request mapping (явный идентификатор шага или проверенный
контракт инструмента с единственным запросом) и совместимой семантике полей.
При нескольких шагах без такого mapping LF остаётся свидетельством уровня
сообщения: его usage не добавляется к local sums и не становится request peak.
Несколько observations с общим messageID не удаляются как дубли автоматически.
Повторную доставку дедуплицируем по trace/observation ID; разные значения
одного ID сохраняются как версии/конфликт, не суммируются. Разные IDs с общей
привязкой требуют выяснения granularity, а не сложения. Если LF независимо
доказывает отдельный request, его known peak можно показать как отдельную
метрику источника с ограниченным coverage, без вымышленного cross-source join.

Делегирование допустимо при наличии разрешённого read-only исполнителя и
пользы: самостоятельная крупная ветка/эпизод/Langfuse; ведущий сначала делает
общий обзор. Новой обязательной execution роли нет. Предпочтительно использовать
доступного явно выбранного read-only агента; отсутствие безопасного исполнителя
даёт последовательный режим, без настройки среды в рамках ретроспективы.
Handoff: точный источник/snapshot, bounded ranges, вопрос исследования, уже
известные факты, запреты, безопасные source refs; ответ — coverage, finding,
consequences/cause alternatives, confidence/metrics/gaps. Ведущий перечитывает
ключевые события и проверяет измерения; непроверенное «готово» не принимается.
Нет двух параллельных исследований одного эпизода без отдельной причины.

## 8. Read-only и состав устанавливаемых ресурсов

Основные SKILL.md содержат выбор, входы, владельцев, минимальный порядок,
условия ресурсов, запреты и остановку. Предлагаемый состав:

```text
ris-retrospect-session-base/
  SKILL.md
  references/analysis.md       # при анализе: каталог/эпизоды/причины
  references/metrics.md        # когда метрики доступны или есть metric gap
  references/report.md        # перед финальным отчётом
ris-retrospect-session/
  SKILL.md
  references/opencode.md      # при получении/проверке локальной истории
  references/langfuse.md      # только для дополняющей телеметрии
  references/delegation.md    # только перед реальным делегированием
  references/save-report.md   # только при явной записи отчёта
  scripts/opencode_read.py
```

Обязательный локальный путь не загружает Langfuse/delegation/save-report.
Ресурсы читаются от установленного владельца, не от исходного RIS repo.
При supplied portable history база вообще не читает opencode.md.

Read-only — запрет новых изменений разрабатываемого проекта (включая source,
docs, config и Git), исследуемых сообщений/parts и смысловых связей истории,
tracker/телеметрии и воспроизведения команд. Узкое CLI-исключение requirements
§8 разрешает только служебные project metadata/housekeeping существующей БД
(включая WAL/checkpoint)/собственные логи OpenCode вне проекта. Путь сам по
себе не оправдывает запись: message/part content в том же storage защищён.
Schema migration, bootstrap, plugins, новый serve/import, SQL/storage bypass,
reader-owned disk export/temp/cache по-прежнему запрещены. При пересечении
service paths с проектом или непроверенных эффектах используется export/GET,
а не расширяется write scope. Supplied-export/GET сохраняют прежние ограничения.
Обычная новая история самой аналитической
сессии, создаваемая harness, не считается изменением исследуемой сессии;
аналитик не запускает явные telemetry write API. Reader разрешает только
свои фиксированные read argv/GET; журнал никогда не становится shell code.
Разрешения скила — поведенческий контракт, не доказанная sandbox-изоляция.
Ключевые негативные тесты проверяют actual tool calls и состояние хранилищ.

Отчёт по умолчанию в ответе. По явному запросу записывается только указанный
report path, с предварительным чтением существующего файла и сохранением
прежнего содержания: новая отделённая версия append, либо отдельная версия
файла по согласованному адресу. Не создавать каталог по guessed Beads ID.
Unexpected change перед записью — conflict, без overwrite. Только безопасные
выдержки и refs, без секретов/посторонних данных; экспорт не вставляется в отчёт.

## 9. Проверочные границы до декомпозиции

Механические tests проверяют reader на synthetic JSON/HTTP stub без LLM;
семантические сценарии — реальное выполнение скилов в изолированной среде
с наблюдением действий и рубрикой. Fixtures не требуют секретов или live
проектных записей. Приёмка различает fixture, реальный read и непроверенное.

| AC | Seam / oracle |
|---|---|
| 001 | Portable transcript вне RIS без CLI/Beads/config: полный bounded отчёт; wrapper actual invocation базы и её проверяемый вклад |
| 002 | Root/child/nested/reused-child/foreign-parent/missing-child, ID/export/no ID, resumed cutoff: точные связи и gaps; поздний export с пересекающим text/tool, недатированным step-finish и поздней child linkage не становится доказанным состоянием до cutoff |
| 003 | Длинная история и большое событие, находка на первой/средней/последней странице: все ranges обозрены до deep dive; omission видим |
| 004 | Три эпизода: оправданный Python, SQL при доступном API, обход из-за missing operation: три разных причинных итога/owners |
| 005 | 150000/150001, большой aggregate при малом peak, cache включён/неизвестен, несколько step-finish, missing usage: правильные signals/unknown без double count |
| 006 | Human wait, короткий повтор без прогресса, parent wait + parallel children: oracle union intervals, unclassified gaps, нет thinking-time ярлыка |
| 007 | Historical skill output A/current file B, absent historic system: A объясняет эпизод, B проверяет актуальность, missing не подменён |
| 008 | Claimed push без evidence и явно failed push: unverified vs failure; адресное чтение, ноль replay/test/build |
| 009 | Handoff loss, missing RED, skill overload/conflicting rule: episode→owner→minimal fix→check, допустимое сокращение |
| 010 | Absent/incomplete/duplicate/conflicting Langfuse, unmatched message ID; два step-finish с partial usage и несколько observations того же messageID, одна доставлена повторно: нет request join по одному messageID, повтор одного observation ID не суммируется, локальный результат и selective loads сохраняются |
| 011 | Actual bounded read-only subagent и sequential fallback: проверенные source refs, один отчёт, непроверенный ответ не становится finding |
| 012 | No findings, confirmed+hypothesis+justified signals: все секции §9, severity и две confidence раздельно |
| 013 | Injection в transcript, secret в error part, предложенный SQL/test, report existing/change: запреты соблюдены по журналу вызовов/снимкам; CLI service-only effects отдельно классифицированы по scoped oracle ниже, только явно разрешённый отчёт сохранён |
| 014 | Natural routing к ретроспективе/review/acceptance/fix/retrotrace, isolated install ресурсов, source parity, два проекта с разными paths, independent review без high/medium |

Обязательные интеграционные проверки: реальный CLI export большого журнала
без обрезания (включая memfd), branch export + public GET children/status
на контролируемом OpenCode 1.18.33, compaction/pruned output, live доступное
соответствие Langfuse IDs либо явная непроверенность этой ветки. Контроль
side effects учитывает runtime самого CLI, а не только код reader; обязательный
gate — scoped oracle ниже, а не ноль всех записей OpenCode storage.
Нет обещания полной истории удалённых сообщений или точного полного system
prompt: такие данные не предоставляет проверенный export.

### Scoped oracle CLI-служебных эффектов (requirements-v2 / AC-002, AC-013)

1. До прогона зафиксировать exact installation/version, CLI argv/cwd, reader
   bytes, initialized schema, выбранный проект/Git/tracker, сессии и ветки,
   фактические service storage/log paths. Service paths должны быть вне проекта;
   совпадение или неизвестная принадлежность блокируют CLI. Fixture provisioning
   и обычная analytical harness history отделяются от collection interval.
2. Сопоставить actual calls и before/after witnesses проекта (включая hidden
   source/config/docs и Git), task content/state/edges, исследуемых session
   identities/linkage, message/part content и schema. Защищённые объекты неизменны;
   telemetry write API, replay/test/build, plugins/serve/import/bootstrap/migration
   отсутствуют. Нужны content witnesses, не только изменённый mtime файла БД.
3. Отдельно перечислить записи OpenCode runtime и их provenance: project metadata,
   housekeeping существующей БД/WAL/checkpoint, собственные логи. Database/WAL
   bytes могут измениться; это допускается лишь при подтверждённой service-only
   классификации и сохранности защищённых объектов/schema. Неразобранная запись
   или неизвестное содержимое не считаются pass. Наблюдение filesystem writes
   и снимки имеют явный охват; не заявлять универсальное отсутствие syscalls.
4. Совместно подтвердить полный валидный большой memfd/pipe export, отдельный
   branch export и список roots без автоматического выбора; проверить повторный
   monitored initialized run. Честно отражать неполноту/изменение snapshot.
   Одна разрешённая log/project запись не означает успешной collection.
5. Supplied-export и existing selected GET проходят свои прежние негативные
   проверки; CLI-исключение к ним не применяется. Test-owner может применять
   независимо разрешённые read-only storage witnesses как instrumentation;
   product reader не получает прямого SQL/SQLite доступа. Поведение server
   bootstrap не оправдывается использованием GET.

Fitness: база не требует RIS/OpenCode; wrapper не дублирует анализ;
нет SQL/storage bypass/запрещённых записей/automatic next step; типичный load trace не
содержит редких ресурсов; installed folder работает без исходного repo.
Лексические assertions не заменяют реальные selection/behavior проходы.

## 10. Альтернативы, совместимость и принятие

Выбраны штатные CLI/GET + компактный owned reader. Прямой SQLite/SQL даёт
зависимость от внутреннего хранения и read-only риск; не нужен. Один только
sanitize export исключён для полного causal analysis из-за потери текста.
Langfuse-only не обеспечивает доступность/полноту локальных событий. Новый
сервер/универсальный адаптер добавляет эксплуатационные издержки без отдельного
результата. Только текстовые инструкции без reader оставляют нестабильные
ручные подсчёты/одноразовые скрипты и плохо проверяемое chunk coverage.

Совместимость: ris-context v2/common и существующие state owners сохраняются;
нет нового config key или обязательной роли, команды/автоматического перехода
из ris-execute-task. Соседние review/verify/implement/retrotrace различаются
по результату; task-execution поставляет evidence, не исполняется повторно.
Необходимой новой blocks-связи с ris-01r.1.1/1.2 нет: reader и переносимая
методика проверяются независимо; реальный журнал соседа — optional fixture.

При реализации добавляются source/install обеих папок, соответствующий README
и ограниченное актуальное описание в concepts/architecture map после проверки
поставки. Исторические spec/requirements decisions остаются по первоначальным
Git-адресам; текущая узкая v2 имеет новые отдельные requirements/design decisions.
ADR не нужен: нет нового глобального инварианта/state owner; технические
границы закреплены этим design. Независимое ревью проверяет достаточность
дизайна и затем отдельно поставку, особенно read-only/metrics/coverage.

Следующие два абзаца сохраняют **исторический handoff design-v1**; pending
refs/design:null относились к его сохранению. Текущее состояние v2/потребителей
и post-publication prerequisites — §11, не повтор этой ранней операции.

Открытых продуктовых/архитектурных альтернатив, требующих нового интервью,
не осталось; reader/GET/live Langfuse имеют названные проверочные seams,
а не вымышленные результаты. Пользователь отдельно принял кандидат design-v1.
Сохранены design.md и отдельное attributable design-v1 решение;
immutable refs до Git-публикации pending. Combined feature-record
update требует опубликованных refs и реального короткого окна защищённой
записи над ris-01r.2/составом/blocks/evidence. Старое окно публикации требований
истекло и не считается доступным сейчас. До этого design:null в Beads
сохраняется; подготовка дизайна не означает его реализацию или закрытие фичи.

## 11. Поправка v2: R1, применимость и координация потребителей

Основание — выбор пользователя «Делаем 2 вариант ведь ретро не бдует менять сам
разрабываемый проект»: именно разрешение служебных CLI-записей вне проекта,
а не удаление CLI/no-ID из поставки. Отдельно приняты requirements-v2 и design-v2;
поправка не меняет владельцев базы/wrapper/reader, метрики, cutoff/tree, Langfuse
join, отчёт, роли/config и запрет replay. Новый ADR/global invariant не требуется.
Исходные full refs requirements-v1/design-v1 сохраняются в acceptance.md.

Исследованные implementation/review v2 T2: base
`a62efad3f8f3837e02b724c54ef408b02ed7e686`, overlay manifest
`240ead657e3d6158475454c1574a1e73030f8f3558052f0011fbff4c38826608`.
Ревью признало R2–R4 исправленными, но оставило R1 высоким конфликтом прежнего
контракта: writable initialized export меняет project rows/log/WAL, readonly
эксперимент падает на открытии opencode.log. Это сохранённые факты, не новые
выполненные проверки и не доказательство попытки последующей DB-записи в failed
run. Поправка разрешает такую категорию service effects в принципе; R1 не
закрывается автоматически, новый runtime/oracle и независимое ревью ещё нужны.

| Связанный критерий | Влияние v2 / применимость evidence |
|---|---|
| AC-002 | CLI exact-ID/branch и no-ID roots остаются обязательны. Нужно переоценить fitness/selection по scoped oracle; успешный supplied-export/GET не заменяет их. |
| AC-013 | Изменён только service-write gate CLI. Нужны разрешённые service witnesses рядом с нулём запрещённых project/history/task/Git/telemetry изменений и отрицательные случаи выхода за границы. Export/GET/injection/secrets/report-save ограничения прежние. |
| AC-014 | Требуется актуальная source/install/docs parity и независимое ревью нового полного snapshot без high/medium; прежний review не одобряет новые bytes. |
| AC-001,003–012 | Содержательная методика, владельцы, метрики/tree/cutoff/joins/отчёт не изменены. Evidence переиспользуется лишь для доказанно неизменных механизмов на identified input/runtime; combined T3 проверка остаётся обязательной. |

Read-only tracker inspection при поправке: feature `ris-01r.2` open,
T1 `ris-01r.2.1` closed, T2 `ris-01r.2.2` in_progress (assignee
`opencode-ris-01r.2.2-20261014-run1`), T3 `ris-01r.2.3` open, pending consumer.
Это наблюдённые статусы, не claim/разрешение запуска T3; active T3 design/scope
нуждается в handoff до dependent implementation/combined acceptance.

- **T1:** база не владеет collection; код/задачу/закрытие/исходные v1 refs
  менять или repin не нужно. Portable запреты строже и совместимы с v2;
  T1 evidence остаётся scoped portable, не CLI evidence.
- **T2:** владелец реализации актуализирует CLI permission/fitness инструкции,
  source/install, meaningful tests и scoped runtime witnesses, затем full
  snapshot/re-review и integration/docs reassessment на newer main. Ноль
  запрещённых записей остаётся gate; v2 не является blanket `--allow-cli`.
- **T3:** передать v2/impact владельцу Langfuse/delegation/save и combined checks;
  сохранить запреты/rare loads/joins/report history. Связать inherited CLI gate
  с новым scoped oracle и пересмотреть applicability T1/T2 на одной integrated
  SHA. Делегату передаются те же границы, не общие write permissions.

После отдельной Git-публикации и проверки exact content/decision commits
уполномоченный tracker owner сверяет текущее состояние под independently
established short writer windows: feature `ris-01r.2`, затронутые T2/T3,
их composition/blocks/evidence. Обновляются requirements и design **вместе**
на реально опубликованные v2 full refs и разные decision anchors, verification
остаётся/сбрасывается в null; slug/spec_path и несвязанный prose сохраняются.
Нужно явно согласованное обновление pinned independent input objects и
CLI-критериев T2/T3, а не молчаливый repin. T1 остаётся исторически на v1.
До публикации tracker refs не меняются; local v2 не выдаётся за published input.
Git и Dolt publication отдельны. Ни одна зависимость не меняется:
T2 → T1, T3 → T2, `ris-01r → ris-p20`; inherited exception **KEEP EDGES**.
