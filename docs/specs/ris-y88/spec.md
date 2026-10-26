# Адресные проверки и доверие результатам SDLC
Feature-ID: ris-y88
Summary: Переиспользовать подтверждённые результаты этапов без универсального повторного preflight.

## Требования S1

Этап доверяет подтверждённому результату предыдущего владельца, пока нет
конкретного основания считать его неприменимым. Это относится к prepare-feature,
execute-task, common published-inputs/handoff, resolve-context и потребителям:
save, decomposition, implementation, review, publication и tracker operations.

- **AC-001.** Входные проверки устанавливают только необходимые для действия
  project/scope, источники/версии/basis, copy и capabilities. Доступный достаточный
  результат владельца заменяет повторное исследование, но не голый `ok`.
- **AC-002.** Условная перепроверка имеет конкретный триггер: релевантное изменение
  content/config/target/association, потеря evidence, противоречие либо риск.
  Переход между owners сам по себе не триггер. Неизменившиеся scopes/решения не
  перечитываются и не перепринимаются только из-за перехода.
- **AC-003.** Критические проверки принадлежат выполняющему действие владельцу:
  свежие условия конкурентной записи, права, ownership/status/action blockers,
  сохранность worktree/чужого содержимого; Git target/outgoing/full reviewed tree,
  non-force и remote confirmation; Dolt scope/direction/reachability и read-back.
  Они не заменяются прежним preflight и не расширяются до полного SDLC-аудита.
- **AC-004.** Handoff передаёт только недостающие точные входы/версии, результат,
  ограничения и полномочия. В одной сессии нет повторного отчёта/рестарта context;
  другая сессия восстанавливает минимальный необходимый контекст из существующих
  источников. Нет новых журналов, реестров, metadata, кэшей, обязательных артефактов.
- **AC-005.** Независимое содержательное review, затронутые проверки, полный новый
  snapshot после интеграционных изменений и корректное partial recovery сохранены.
  Reviewer сам оценивает необходимые полные тексты; доверие не заменяет независимость.
  Подтверждённые push/close/setup не повторяются ради утраченного handoff.
- **AC-006.** Источники, installed mirrors и текущая документация согласованы;
  проверка чтением/diff, предусмотренными статическими проверками и независимым
  review. Live/scenario agent tests запрещены. Уменьшение предписанных операций —
  статический вывод, не измеренная экономия токенов или гарантия поведения.

Вне объёма: новые инструменты/слои, изменение схемы config/review/tracker,
ослабление native guards, поведенческие прогоны, переписывание исторических решений.

## Аудит исходных контрактов

Исходная версия: `4154d9e74169172c607d32d6c60903c4bee51ac6`.
Повтор не считается лишним без учёта его назначения:

| Источник | Назначение / избыточность | Решение и последствия |
| --- | --- | --- |
| common SKILL Conditional resources vs published-inputs §§Discover/Policy | Уже разрешён reuse, но каждому consumer предписано чтение полного basis и checkout diagnosis | Проверять basis один раз для точных scopes; downstream использует проверенное основание. Checkout diagnosis только когда действие зависит от локальной копии. Неполное/противоречивое evidence не становится достоверным. |
| resolve-context SKILL/configuration; prepare copy recipient validation | Полная schema validation защищает от invalid config, повтор её на каждом owner не добавляет гарантий | Полная проверка при выборе/изменении config; при смене copy проверить association и различия config/нужных путей. Invalid поле по-прежнему ошибка, валидный unused diff не блокер. |
| prepare-feature preflight/stage prerequisites/save/reconcile/decompose | Ранний preflight предотвращает заведомо невыполнимую поставку, поздние повторы снова исследуют те же capabilities/decisions | Один ранний capability/authority preflight; затем только gates конкретной записи/публикации. При drift повторить затронутое. |
| execute-task step 1; implementation input discovery | Copy safety и достаточные входы обязательны, но уже проверенный preparer/basis дублируется | Потреблять достаточный результат, preparer вызывать для отсутствующей/неясной copy/setup. Native execution admission остаётся свежим. |
| review/publish inputs and policy discovery | Самостоятельные входы и точный snapshot обязательны; discovery не механизм независимости | Передавать точные locators/provenance. Reviewer самостоятельно читает и оценивает полный предмет, publisher сопоставляет snapshot/authority, не повторяя авторский анализ basis. |
| adapter version/workspace/capability checks, decomposition final reread | Entry checks смешаны с mutation safety | Переиспользовать capability/workspace в неизменившемся окружении; перед записью свежие затронутые поля/структура, после — read-back. Финальная coverage использует уже проверенные immutable inputs. |
| artifacts handoff/recovery | Полнота спасает от foreign-chat assumptions, но повторные перечисления провоцируют полную передачу | Только недостающие факты и ограничения; после потери контекста восстановить нужное, неизвестные эффекты сверить до retry. |

## Дизайн D1

Существующий common SKILL владеет одной короткой классификацией: входные,
условные, критические. Это правило применения существующих результатов, не новый
протокол или infrastructure. Published-inputs владеет проверкой достаточного basis
и неизменяемых locators, context — config/path association, adapter — свежестью
конкурентных predicates/read-back и Dolt, publisher — Git, reviewer — независимой
оценкой полного subject. Владельцы сохраняются; новый portable base не нужен.

В consumers заменить безусловные повторные discovery/read/preflight адресным
потреблением результата. Прямой вызов без такого результата выполняет свои входные
проверки; внутренний вклад не повторяет entry ceremony. Изменение копии само по
себе не отменяет immutable content/решение: обновляются локальные association,
пути и изменившиеся настройки. Изменение upstream требует оценки применимости
затронутых inputs и независимой переоценки нового полного snapshot, не нового
принятия неизменившихся решений. Реальный конфликт или неизвестность блокирует
только зависимое действие.

Handoff остаётся сообщением/существующим locator без обязательного файла.
Отдельный агент нужен для независимого review, не для каждого внутреннего owner.
В новой сессии не доверять пересказу: восстановить нужное content/basis/evidence из
точных доступных источников; не восстанавливать весь жизненный цикл.

Проверка AC-001–006: чтение изменённых contracts и соседних direct/resume веток,
static contract checks, links/resources/source-install parity, diff check и
независимое publication-purpose review полного дерева. Combined check — на
интегрированной ревизии той же задачи; программные/live agent tests не добавляются.

## Основание S1 и D1

Отдельно принятые scopes: `Требования S1` (AC-001–006 и exclusions) и `Дизайн D1`,
версия каждого — `containing-commit` этой исходной decision; audit — объяснение
вывода, не новый runtime evidence. Policy acceptance выполнено 26.10.2026 внутри
полного prepare по явному поручению пользователя «Проведи аудит и реализуй …
Выполняй работу автономно … доведи … до реализации и публикации».
Поручение выбирает принцип доверия, три категории, минимальный handoff, все
сохраняемые гарантии и запрет live tests. Новых нерешённых продуктовых/
архитектурных альтернатив нет; отдельного формального согласования не запрошено.
Настройка: `ris.yaml` в Git
`4154d9e74169172c607d32d6c60903c4bee51ac6`,
`workflows.prepare_feature.auto_accept: true` (явный boolean, config целиком
валиден); overrides отсутствуют. Автор/действующий prepare context:
`opencode:ses_e86c624f7ffeYWdhW0WUD9I0zn`. Это policy basis, не выдуманный human
approval. Последующие редакции сохраняют исходный immutable decision address.
