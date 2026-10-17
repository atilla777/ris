# ris-17f — проверки текстовой поставки

## Область и версия

Кандидат реализации V2/D1 подготовлен в `task/ris-17f` на базе
`f6f8aa96160670c4bda111963def07e5a0cb7bc9` (tree
`6fe6dfb18df790167edd134017d00af34953bb8d`). Это текстовый source/install-кандидат,
ожидающий отдельного независимого ревью и интеграции; не подтверждение main/push,
закрытия задачи или поведения агента. Полный candidate tree с добавлениями,
удалениями и режимами передаётся вызывающему отдельно в implementation receipt;
этот документ не служит журналом переходов или обязательным удалённым входом.

Требования: весь [spec.md](spec.md) V2 на
`b6fa4cbda883066f7f58857a10b5ccfa3ca35b9d`, отдельное
[решение требований](https://github.com/atilla777/ris/blob/b6fa4cbda883066f7f58857a10b5ccfa3ca35b9d/docs/specs/worktree-preparation-simplification/acceptance.md#требования-v2).
Дизайн: весь [design.md](design.md) D1 на базе выше, отдельное
[решение D1](https://github.com/atilla777/ris/blob/f6f8aa96160670c4bda111963def07e5a0cb7bc9/docs/specs/worktree-preparation-simplification/acceptance.md#дизайн-d1).
Исходные принятия не перепривязаны. Условие без журналов и соразмерная сохранность
адресно заменяют соответствующие положения исторических
[task-worktree-preparation](../task-worktree-preparation/design.md) и
[task-execution](../task-execution/design.md); их snapshots, решения и результаты
не переписаны. Совместимый [fast D2](../fast-task-execution/design.md) на
`7601bf7bb0730d3caf19bbdb4282a9fb63d35804` не переносит в полный flow свои исключения
по плану/делегированию. Новых CLI, ролей, config, реестра или движка исполнения нет.

## Обязательные чтения до/после

Сравниваются предписания базы выше и кандидата. Обычный случай: точный ordinary
task ID, свободные path/branch, явный проверенный primary, Git, без setup/hooks
и прежних/неясных эффектов. Каждый исполнитель загружает свои зависимости; уже
доступное актуальное содержание не перечитывается формально. Это не замер времени,
токенов, числа фактических вызовов или надёжности.

| Инструкции | До | После |
|---|---|---|
| Project preparation `SKILL.md`; common `SKILL.md`, `artifacts.md` для результата, `quality.md` для проверки | Обязательны | Обязательны; dialogue только перед вопросом/решением |
| Context `SKILL.md`, `configuration.md`, `paths.md`, `shared-primary.md`; применимые правила проекта | Обязательны для этих настроек/общих путей | Сохранены; whole-config validity не сокращена |
| Selected tasks adapter `SKILL.md` | Exact typed task/content/assignee/blockers | Сохранён; при новом claim его `claim.md` + `concurrency.md`, при уже собственном claim — свежие reads |
| Portable preparation `SKILL.md`, `worktrees-contract.md` | Обязательны; reuse/preservation перемешаны с create | Обязательны; обычный create имеет явную ограниченную область |
| Selected Git adapter `SKILL.md`, `git.md` | Обязательны; preservation oracle сформулирован широко | Обязательны; file-byte oracle явно условен для reuse/защищаемых ресурсов |
| Full flow `SKILL.md`, context `execution-roles.md` | Дополнительно проверяются три роли и реальные вызовы | Сохранены; no-ID inventory только при действительном выборе/диагностике |
| Flow `evidence.md` перед первым handoff/report | Обязателен | Не загружается по этому поводу; краткие transition proof gates в основном SKILL |
| Flow `text-work.md` | При text-only реализации | Условие сохранено; методы следующих этапов получает их исполнитель |

Точные условия редких ресурсов:

- Новый base-owned `preservation.md`: **до** reuse, существующей ветки без копии,
  сверки partial/ambiguous эффекта или hooks/setup с защищаемыми ресурсами.
- `environment.md`: до зависимой мутации при запрошенных/обязательных setup/hooks;
  отсутствие setup не отменяет проверки наличия hooks/filters адаптером.
- Worktrunk `SKILL.md`/`worktrunk.md`: только если он выбран явно/однозначным правилом;
  `effects.md` — до его create, copy-ignored section — только при разрешённом copy.
  Git oracle внутри Worktrunk не означает fallback.
- Flow `evidence.md`: recovery либо недостаточная/противоречивая transition proof;
  `recovery.md`: own unfinished, прежний/частичный эффект, interruption или closed
  pending-publication. До это последнее условие уже было; изменён источник proof.
- Context roles остаются условными для caller, требующего роль; direct preparation
  их не требует. Tracker create/completion/publication-ресурсы не нужны лишь для
  exact-read подготовки, но подключаются их владельцем перед соответствующим действием.

## Обязательные действия до/после

| Действие | До | После |
|---|---|---|
| Права, точный ID/actor, claim/status/blockers, primary/association | Свежие checks перед зависимой мутацией | Сохранены, включая receiver/retry guards |
| Tool/repository, полные регистрации, target/ref, hooks/filters, pinned full base | Preflight, non-force create, независимое read-back | Сохранены; полная регистрация не означает обход всех копий |
| Сохранность обычного create | Широкая формулировка bytes/index/files, без трёх явных областей | Только регистрации/target/ref/base/новая копия; нет whole-primary/sibling hash или заявления byte equality |
| Reuse / hooks/setup | Сохранение имеющегося состояния и эффектов | Явно scoped: выбранные HEAD/refs/index/changed-protected bytes либо конкретные защищаемые ресурсы/outputs; не reset/overwrite |
| Recipient context | Любое changed/missing config блокирует handoff | Whole selected config valid; сравниваются используемые operation/recipient settings, tracker/primary/rules/shared paths; unused valid product difference не blocker |
| Отчёт подготовки | Optional witness имел именованный путь worktree.md | Компактный checked handoff; нет default file/read requirement |
| Full-flow evidence | Обязательный execution.md, append/history и evidence load до первого handoff | Нет обязательного файла или записи каждого перехода; live facts + exact results и проверяемые предпосылки |
| План, ход/итог, independent review, Beads result | Обязательны по правилам RIS | Сохранены; не замаскированный transition ledger |
| Partial/retry | Проверить факты, не повторять подтверждённый эффект | Сохранено; нестандартная association/non-idempotent setup/process/ambiguous effect требует compact addressable result перед зависимым необратимым действием либо точного blocker |

## Покрытие критериев и границы проверок

Это чтение предписаний и адресная статика, не выполненные сценарии агента.

| AC | Инспекция кандидата / применимый oracle |
|---|---|
| 001 | Direct wrapper/base и full-flow main не требуют журналов; review discovery не требует execution.md; repeat использует live copy/claim и доступную association, отсутствие журнала само по себе не blocker |
| 002 | Таблицы выше фиксируют обязательные чтения/действия на двух версиях и точные условия редких веток; измеренное ускорение не заявлено |
| 003 | Base, worktrees/1 и оба адаптера явно ограничивают ordinary create; status не объявлен byte oracle для protected data |
| 004 | Preservation/environment и flow recovery сохраняют dirty associated copy, refs/index/files и completed setup; collision/unfinished Git/unknown association/partial create/setup останавливают только зависимое действие без force/reset/delete/blind retry; plan/progress/result/review/tracker obligations остаются |
| 005 | Wrapper отличает valid unused product от invalid config, другого tracker/используемого shared path. Context schema/primary protocol остаются прежними; defaults/config не подставляются, вторая база не создаётся |
| 006 | Wrapper требует fresh claim/blockers и permissions перед mutation; context проверяет explicit→verified available primary; Git default/explicit Worktrunk/no fallback; copy и environment verdict раздельны |
| 007 | Проверяются frontmatter/name, owned resources/dependency links, ссылки затронутых документов, source/install path/byte/type/mode parity, полный diff и whitespace; независимое whole-snapshot review — отдельный ещё не выполненный gate |

Проверки имён/ресурсов/parity и `git diff --check` относятся к текстовым файлам.
В source/install меняются только затронутые каталоги внутри task copy; primary
установка и чужие данные не синхронизируются. Правки двух явных OKF 0.2-корней
`docs/rules/index.md` и `docs/concepts/index.md` ограничены существующими концептами,
их type-frontmatter/навигация сохранены; whole-bundle audit/conformance не заявлены.
Обычные spec/design/acceptance не конвертируются в OKF. Исполняемый код/installer/
manifest/bootstrap не меняются: их runtime/CLI-тесты неприменимы к этому diff.
Live/scenario agent tests не запускались. Старые behavioural/T1/T2 observations
не становятся pass для новой версии. Static check pass не заменяет независимого
ревью, интеграционной переоценки или подтверждения публикации.
