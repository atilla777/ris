# RIS — инструкции агенту

Выполнение задачи следует принятой [S1 §4 / D1 §5](docs/specs/sdlc-feature-lifecycle/acceptance.md):
без отдельного planner, обязательного плана и журнала реализации; исполнитель
проверяет достаточность принятых входов, актуальный код и выбирает подход.
TDD сохраняется, но история RED/GREEN не является отчётом или гейтом ревью/recovery.
Основной агент может применять существующих владельцев, reviewer реально независим.
Явно выбранный `ris-proj-flow-execute-simple-task` (`/risp-run-simple-task`)
сохраняет [fast-исключение](docs/rules/development.md#узкое-исключение-явно-выбранный-fast)
без обязательного файла ревью.
Краткий Beads-учёт в RIS и собственная ветка в выделенном worktree обязательны,
включая fast и общие документы; пригодная подтверждённая копия переиспользуется.
Исходная папка не площадка разработки. Полный flow сохраняет
свои copy/claim, quality, publication и отдельные completion/tracker gates.

Подготовка фичи отдельно следует принятой [S1 §3 / D1 §§2–4](docs/specs/sdlc-feature-lifecycle/acceptance.md): ранний ID и одна safe copy, один диалог требований/дизайна с двумя точными accepted scopes (возможен один акт), независимое ревью/Git, same-record refs и existing decomposition до проверенного one-task либо children/blocks и отдельной публикации трекера. Отдельный исполнитель каждого внутреннего действия не обязателен; reviewer реально независим. Direct specify/design/decompose сохраняют scoped результаты. Подготовка не разрешает реализацию автоматически.

По принятой [поправке ris-wcv](docs/specs/ris-wcv/spec.md) прежние same-record refs/JSON и обязательное saved verification сняты: новые feature-документы — `sources.specs/<full feature ID>/spec.md`, читаемый H1 и column-zero Feature-ID/Summary/optional Keywords; фактическое независимое принятие требований/дизайна сохраняется. Старые ссылки/payload — только hints к реальным документам/решениям, без schema gate, миграции и переписывания истории. Нет нового реестра.

Bugfix использует versioned basis по [product §4.1](docs/product/06-artifacts-and-handoff.md#41-воспроизводимое-основание-bugfix):
полные использованные поля точной версии истории трекера и immutable Git sources/decisions,
без новой полной копии в notes/файле; historical read/locator append/retry — у адаптера.
Старые snapshots и история не переписываются.

Обычное проектное ревью сохраняется одним локальным `review.yaml` по [ris.review/1](skills/ris-proj-op-review-task/references/report-format.md); в Beads — адрес/раунд, не копия verdict/findings. Fast остаётся без обязательного файла; optional save использует тот же формат. Отчёт не заменяет журнал реализации и не содержит его перенесённых полей.

По принятым правилам штатные действия полного поручения
не требуют повторных технических разрешений на границах владельцев. Context
по [ris-ppw S1/D1](docs/specs/ris-ppw/spec.md) вычисляет исходную папку из фактического общего `.git` в схеме один repo — один
проект, без saved-primary cascade и права менять checkout. Workspace leaves имеют
defaults даже в выбранном config, явные leaf overrides их заменяют; sources — из
текущей копии. Actor нового назначения — explicit/configured,
иначе проверенный ID сессии; это не право забрать прежний claim/copy. Проверенный
remote Git — обычный полный результат без local update; только явное поручение
включает отдельный safe FF без branch switching. Пропуск/ошибка локального
обновления не блокирует close/Dolt; явно порученное обновление остаётся отдельным
долгом. В RIS действует постоянная shared Dolt policy из development rules,
без автонастройки других проектов. Все substantive/review/claim/non-force gates
сохранены; противоположные прежние primary-sync нормы заменены в этой области.

По поправке ris-oub обычное закрытие родительского контейнера доверяет закрытым
прямым детям: полный непустой all-status список, все `closed`, нет активных
блокировок родителя, native exact close/read-back и отдельная Dolt-публикация.
Не повторять приёмку, Git/review или аудит декомпозиции и потомков. Проверка
возможности закрытия — те же чтения без записи; содержательная verify/verify-and-close
только по явному запросу. Фича без детей сохраняет проверку собственного результата.
Это заменяет прежние обязательные whole-container gates только для обычного
закрытия родителя, не для leaf/one-task execution или явной содержательной проверки.

Для автономной работы с явно выбранным OKF-бандлом используй `ris-port-op-manage-okf-bundle`; для OKF-операции в выбранном RIS-проекте — `ris-proj-op-manage-okf-bundle` с явными project/root/operation/scope. Обычные Markdown-спецификации не обрабатываются как OKF автоматически.

Перед работой прочитай [README.md](README.md) и применяй [правила разработки](docs/rules/development.md) целиком: они определяют согласование задачи, очередь Beads, локальные заметки, проверки, ревью и публикацию Git и Dolt. Не считай планы уже реализованными функциями. Для проектных путей RIS используй корневой [ris.yaml](ris.yaml); расположение конфигурации относительно этого файла — корень проекта.

В этом проекте пакет установлен в `.opencode/skills/`; исходные скилы с ресурсами хранятся в `skills/`, команды — в `commands/opencode/`, установка синхронизируется из них. Для автономного скила используй `ris-port-op-author-skill` (команда `/risb-skill`), для RIS-интеграции явно загрузи `ris-proj-op-author-skill` без slash-команды. Компактные команды `risp-`/`risb-` явно выбирают один проектный/автономный контракт, их имена не совпадают с техническими именами скилов. Общие правила принадлежат `ris-proj-lib-common`, подготовка настроек — `ris-proj-op-resolve-context`. Полная [карта перехода](docs/skill-command-naming-migration.md) объясняет исторические имена без алиасов. Источник продукта RIS и нормативной методики — [docs/product/index.md](docs/product/index.md), правила репозитория — [docs/rules/index.md](docs/rules/index.md): это отдельные OKF 0.2-бандлы по [профилю корпуса](docs/product/knowledge-profile.md). Наличие product-бандла не доказывает принятие или готовность его материалов для конкретной операции. Планы поставок — обычный Markdown в [docs/specs/](docs/specs/README.md). Состояния и зависимости новых задач разработки RIS — в Beads; старые `PLAN-*` в игнорируемой `tasks/` — исторический архив, новые локальные заметки — в игнорируемой `.sdlc/tasks/<подтверждённый ID>/`.
