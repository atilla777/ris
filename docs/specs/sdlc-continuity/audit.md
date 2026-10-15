# Сквозная связность RIS — адресный read-only аудит A1

## 1. Предмет, baseline и пределы

Аудит текущего содержания, не delta-review реализации. Основной baseline:
Git `2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae`, tree
`07f9e807030129fc8c6f06fcc1ea7dad3ba28bc2`; source skills tree
`52148e19f600480dc5b2e44e5399ea876f63aea7`.
В начале исследования HEAD был `05ff12f7ce1a3fc52ae0032fbd1f0e2afd8cee11`;
параллельная подготовка именования опубликовала `2ddd88f…`. Источники скилов,
команд, config и нормы между этими наблюдениями не менялись.

Прочитаны все 41 SKILL.md, 8 command templates, AGENTS/README/development/ris.yaml,
нормативные архитектура/композиция/контракты/артефакты/SDLC, релевантные owned
acceptance/save, feature-record, concurrency/publication, execution recovery/evidence/
text-work, snapshot, current-copy и worktrees resources. Нерелевантные stack profiles
и полный форматный OKF snapshot не нужны для вывода о SDLC-передаче и не заявляются
как содержательно проверенные. Сравнение source/install `diff -qr` не нашло различий
байтов/состава; только дополнительные grilling/grillme. Mode parity этой командой
не доказывается. `git diff --check` исходного tracked delta прошёл.

Beads 1.3.1, embedded Dolt, проект RIS подтверждён where/context. Полные all-state
reads: 45 task/2 epic после создания реализации именования, 46 task после ris-bxc.
Трекер менялся параллельно: это наблюдения с привязкой к моменту, не замороженная
база. Работа ris-bxc только сохраняет аудит/требования/кандидат, не принимает
features по закрытым статусам. Нет agent behavioral tests, живых прогонов или
измерений стоимости. Аудит ведущим не является независимым publication approval;
независимое ревью документов подготовки — отдельная проверка.

## 2. Полный фактический каталог и результаты

35 операций = 15 переносимых + 20 проектных; 2 сквозных сценария,
3 технических адаптера и 1 общая библиотека. Вложенная методика не превращает
операцию в сценарий. Имена ниже именно baseline, не будущая naming map.

| Переносимый владелец | Проектный владелец | Вход → собственный результат / обнаружение |
|---|---|---|
| ris-plan-roadmap-base | ris-plan-roadmap | Цель/знания/текущий baseline → предложение в ответе / проверенные эпики и directed links трекера |
| ris-interview-base | ris-interview-feature | Тема/известные решения → sourced handoff в ответе; проектная операция добавляет coverage требований, не сохранение |
| ris-formulate-spec-base | ris-specify-feature | Решения/поведение → proposal / принятые spec и decision; document-only локально, combined ещё feature task с published refs |
| ris-design-feature-base | ris-design-feature | Принятые требования/контракты → design proposal / принятый дизайн+decision, optional combined record update |
| ris-decompose-spec-base | ris-decompose-feature | Требования+достаточный дизайн → work proposal / одна feature task либо children+blockers и coverage |
| ris-plan-task-base | ris-plan-task | Одна задача/технические входы → plan / default primary workspace.tasks/ID/plan.md |
| ris-prepare-worktree-base | ris-prepare-task-worktree | Work identity/repo/base → copy+environment handoff; проектный владелец добавляет task/claim/context, optional worktree.md |
| ris-implement-base | ris-tdd-implement-task | Принятый change/optional findings → проверенные code/tests; проектный владелец добавляет обязательный TDD/claim/docs и default implementation.md |
| ris-review-base | ris-review | Конкретный snapshot/inputs/checks → report; проектный default review.md, независимость устанавливает вызывающий |
| ris-verify-feature-base | ris-complete-container | Полные AC/принятые refs/integrated revision → read-only assessment / verification+отдельное exact-ID закрытие feature либо собственного эпика |
| ris-retrospect-session-base | ris-retrospect-session | Адресуемая история → report; wrapper собирает exact OpenCode session, default response-only, редкие branches условны |
| ris-formulate-architecture-rules-base | ris-author-architecture-rules | Факты/границы → normative proposal / accepted saved scoped rules и decision, без Git push |
| ris-formulate-development-rules-base | ris-author-development-rules | Tool/practice evidence → engineering proposal / accepted saved scoped rules и decision, без настройки инструментов/push |
| ris-okf-base | ris-okf | Explicit root/operation/scope → форматная операция; wrapper добавляет project/config/permissions, не принятие содержания |
| ris-author-skills-base | ris-author-skills | Проработанные требования → source folder; RIS-владелец проверяет integration, не устанавливает/публикует автоматически |

Пары в таблице означают применение, не одинаковый предметный охват всех branches.

| Прочий владелец | Вход → результат / граница |
|---|---|
| ris-context | Calling operation/project/needed fields → checked config/path provenance, changes=[]; не выбирает документы/стадию |
| ris-plan-epic | Exact epic/goal/ambiguity → refinement и optional verified epic update; не выбирает фичу |
| ris-select-next-feature | Roadmap/epic/current evidence → read-only choice/recommendation; не пишет/не стартует интервью |
| ris-update-documentation | Inspected tree/integration+authorized docs → verified changes/no-change; не принимает продукт/дизайн |
| ris-publish-main | Approved full task/change snapshot+authority → integrated Git commit и remote confirmation; не Dolt/closure |
| ris-beads-adapter | Exact bounded operation/IDs/scope → fresh verified tracker effect; dolt.publish отдельно |
| ris-git-worktree-adapter | Exact repo/path/branch/commit → worktrees/1 list/read/create, independent Git oracle |
| ris-worktrunk-adapter | То же с explicit wt → bounded tool effect/hooks/config evidence; не выбирает ownership |
| ris-common | Shared scope/dialogue/artifact/quality rules; не самостоятельный этап |
| ris-prepare-feature-work | Roadmap scope/known decisions → separately accepted reviewed published requirements/design и remote feature ID; без decomposition |
| ris-execute-task | Ready exact ID либо разрешённый выбор → один task cycle, review/repair/Git/completion/tracker publication; recovery возвращает к тем же owners |

Portable response-only результаты не становятся доступными другой сессии сами.
Проектные локальные plan/review/implementation обнаружимы по ID в primary, но не
обязательные remote inputs. Feature refs/decisions публикуются в Git, текущие
identity/status/composition/blockers принадлежат трекеру, не файлам roadmap.

## 3. Карта стыков: атомарные операции → полный путь

| Стык | Фактический output → required input / оценка |
|---|---|
| Goals/knowledge/rules → roadmap | Принятая цель+минимальная архитектура достаточны; authoring правил не равно setup/compliance; создание product knowledge не обязательная новая стадия |
| Roadmap → epic/selection | Saved goal identity/outcome/boundary/blockers → adapter reads по ID; refinement только при неясности |
| Selection → interview/specify | Choice+sources+known answers → substantive requirements; response-only choice может быть недоступен новой сессии |
| Interview → formulation | Sourced status-aware answers → proposal; наличие интервью не доказывает completeness или acceptance |
| Requirements → design | Scoped accepted content+separate decision → design; document-only допускает checked local pending refs |
| Docs → feature-record | Saved accepted content недостаточно: нужны published full revisions/immutable separate decisions; прямые wrappers не публикуют |
| Feature-record → decomposition | ID открытой task под epic, both refs, current applicability/contracts/blockers; хорошо заданный восстановимый ID-вход |
| Decomposition → execution | Real child IDs, AC/refs/seams/prerequisites → task readiness; tracker publication не входит в promised decomposition result |
| Copy → plan | Verified current copy/association+explicit primary → local plan; planning не требует claim и не создаёт copy |
| Plan → implementation | Current accepted inputs+plan/constraints → checked change; stale scope возвращается owner, claim/blockers заново |
| Implementation → docs | Inspected code/tree+authorized paths → truthful docs, pre-integration/current различены |
| Implementation/docs → review | Exact complete snapshot+criteria/checks → findings/verdict/provenance; self-review не independent gate |
| Review → repair → review | Stable IDs+current applicability → bounded fixes/checks/fresh independent review; low не запускает цикл автоматически |
| Approved snapshot → Git | Full approved tree/authority → integrated remote commit; changed integrated tree требует reassessment |
| Git → leaf completion | Published revision+own criteria+mandatory scope → adapter exact-ID result/close; общего ris-complete-task пока не нужно |
| Integrated feature → completion | Полные AC/refs/common revision → portable verification + safe persistence/closure; closed children не acceptance |
| Epic → completion | Собственные outcomes/composition/evidence → epic branch; не навязывает feature AC или одну SHA всем релизам |
| Local tracker effects → remote | Entire authorized outgoing history → adapter dolt.publish/read-back; Git/close не заменяют |
| Delivery → retrospective | Exact session ID/export/history → separate report; task ID автоматически не заменяет session locator |
| Revision/interrupt → resume | Actual effects+version applicability → same owner/missing operation; полнота доказательств важнее stage flag |

## 4. Сценарии → тот же полный путь

```text
Goals/knowledge/rules → roadmap/selection
  → ris-prepare-feature-work
  → отдельная ris-decompose-feature
  → ris-execute-task для выбранной задачи (не всего контейнера)
  → отдельное завершение многозадачной фичи/контейнера/эпика
  → отдельная ретроспектива
```

Эти ручные/внешние переходы намеренны; отсутствие full-SDLC mega-flow не дефект.
[Подготовка](https://github.com/atilla777/ris/blob/2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae/skills/ris-prepare-feature-work/SKILL.md#L68-L158)
действительно назначает select/interview/formulate/specify/design и adapter,
сохраняет один человеческий диалог и отдельные принятия; проверяет receipts,
не просто перечисляет имена. Review/Git publication делегируются как операции,
но переиспользуемый owner назван менее определённо, чем в execution.
[Execution](https://github.com/atilla777/ris/blob/2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae/skills/ris-execute-task/SKILL.md#L141-L232)
явно использует prepare/plan/TDD либо bounded text owner/review/publish/adapter и
complete-container для выбранной one-task feature. Recovery применяет тех же owners,
не отдельный маршрут; closed pending work не переоткрывает.

Command templates тонкие, сами эти гарантии не добавляют. Роли `general` в config
не доказывают launch. В текущем интерфейсе этого аудита доступен `explore`, а
configured general не проверялся живым запуском; runnable весь scenario здесь
не заявляется. Независимый reviewer подготовки вызывается отдельно, без
утверждения выполнения configured scenario role.

## 5. Находки и намеренные границы

Уровень отражает влияние на [согласованную модель](spec.md), не объявляет новое
требование уже действующей обязанностью всех старых скилов. High не установлены.

| ID / уровень | Конкретное основание и следствие | Минимальное направление |
|---|---|---|
| A1 / средний | [decompose:29–35,78–99](https://github.com/atilla777/ris/blob/2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae/skills/ris-decompose-feature/SKILL.md#L27-L99) требует epic+feature-record; [complete:24–30](https://github.com/atilla777/ris/blob/2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae/skills/ris-complete-container/SKILL.md#L22-L30) распознаёт такую feature либо epic. Реальные standalone ris-1fq/ris-lr1 не имеют равноценного project route подготовки/общего завершения | Расширить существующих предметных owners на различимый standalone scope, не создавать искусственные parent records |
| A2 / средний | [specify save:54–70](https://github.com/atilla777/ris/blob/2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae/skills/ris-specify-feature/references/acceptance-and-save.md#L54-L70), [design save:84–115](https://github.com/atilla777/ris/blob/2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae/skills/ris-design-feature/references/acceptance-and-save.md#L84-L115) сохраняют локально, combined ждёт публикации вызывающего; decomposition не обещает tracker push. По новой модели direct finished planning остаётся неполным | Прямой finished owner вызывает reusable publication, явно limited вклад сохраняется |
| A3 / средний | [prepare:101–135](https://github.com/atilla777/ris/blob/2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae/skills/ris-prepare-feature-work/SKILL.md#L101-L135) описывает Git шаги generic executor; [publish:21–25](https://github.com/atilla777/ris/blob/2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae/skills/ris-publish-main/SKILL.md#L19-L25) ориентирован на task implementation/change evidence. Pre-ID docs publication/review не имеют столь же явного reused owner. Это недоопределённость, не доказанный факт runtime-копирования | Проверить достаточность существующего Git owner и portable review, передавать bounded subject без фиктивного ID |
| A4 / средний | [selection:121–143](https://github.com/atilla777/ris/blob/2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae/skills/ris-select-next-feature/SKILL.md#L121-L143), [interview:103–118](https://github.com/atilla777/ris/blob/2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae/skills/ris-interview-feature/SKILL.md#L101-L118) response-only. Без доступного источника выбор/answers не восстановимы по epic ID | Сохранность существенного промежуточного результата обеспечивает permitted caller; иначе honest blocked, не обязательный новый store |
| A5 / низкий | [config:100–105](https://github.com/atilla777/ris/blob/2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae/skills/ris-context/references/configuration.md#L100-L105) запрещает неявно обнаруживать primary; [copy:38–45,89–94](https://github.com/atilla777/ris/blob/2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae/skills/ris-prepare-task-worktree/SKILL.md#L38-L94) требует association, witness optional. ID может вызвать дополнительный вопрос даже при inspectable evidence | В дизайне определить проверяемое восстановление без угадывания/нового registry |

Required относительно целевой модели: A1–A4. Optional исследование/уточнение: A5.
Намеренные человеческие gates: отдельные requirements/design acceptance, выбор
при реальной неоднозначности, отдельное разрешение container completion,
непокрытые writer predicates. Неподтверждённые текущие случаи: runtime любых
новых переходов, Gas City integration, фактическая доступность general.

Первоначальная гипотеза о необходимости отменить запрет next-skill naming в
атомарных скилах **снята**: [architecture:39](https://github.com/atilla777/ris/blob/2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae/docs/concepts/01-architecture.md#L39)
и author:79–84 сохраняют полезную композиционную границу. Новая навигация имеет
собственный рекомендательный результат. Дублирующиеся field/ref checks у
потребителя и адаптера сами по себе не подтверждают неверного копирования:
subject applicability и storage protocol — разные проверки; убирать нужно
только доказанную лишнюю копию, не независимый review.

## 6. ris-bsy — историческое свидетельство, не текущая остановка

Первоначальный [P1 §§7–8](https://github.com/atilla777/ris/blob/05ff12f7ce1a3fc52ae0032fbd1f0e2afd8cee11/docs/specs/skill-command-naming/delivery-plan.md)
подтверждает accepted v1/D1/N1, подготовительную ris-bsy без feature-record,
one-task proposal U и остановку на неопубликованных входах; полный decompose-feature
неприменим. Содержательная база и tool-specific adapter позволяли ручной путь,
но не предоставляли готовый project transition.

Во время аудита другой исполнитель опубликовал входы в `05ff12f…`, оформил
ordinary task `ris-1fq`, blocker `ris-lr1.1 → ris-1fq` с сохранением W2→W1,
затем [итог §9](https://github.com/atilla777/ris/blob/2ddd88f51dc1e2fd0bd37b33eb11c6e8d49301ae/docs/specs/skill-command-naming/delivery-plan.md#9-последующее-оформление-и-публикация)
в `2ddd88f…` и отдельно закрыл ris-bsy. Remote Git refs прочитаны; независимый
Dolt read-back этой чужой публикации аудитом не выполнялся. Позднее перед
созданием ris-bxc ris-1fq уже in_progress в отдельной copy: это состояние
текущей параллельной реализации, не её принятие/завершение.

Успешное ручное продолжение не устраняет A1–A4 и не доказывает достаточность
короткого project call. Ни ris-bsy, ни ris-1fq этим аудитом не продолжались.

## 7. Статический способ сверки будущего изменения

Для каждой строки §3 и каждого обещанного сценария: producer output/address/
version/decision → consumer required input; direct/limited invocation; success/
partial/interrupt/revision; channel state; fresh permissions/claim/guarantees;
явный owner результата/перехода. Проверить настоящие calls и использование receipts,
не просто dependency names. Сверить metadata/installed names/resources/commands,
source-install parity и затронутые нормативные ссылки. Ручная семантическая
матрица допустима; автоматическое извлечение всего графа из прозы не обещается.
Подробное покрытие AC и seams — в proposed D1. Никакой из этих checks не является
live behavior test или доказательством совместимости внешней платформы.
