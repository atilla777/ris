# Проверки TDD-реализации задачи RIS

Дата: 13 октября 2026 года. Задача: `ris-cbs`.
Основание: [согласованная спецификация](spec.md), AC-001–008.
Базовая ревизия исходников: `e386a8559bd0bc95d22bec3edddd6f7d61b5ad1a`.
Это свидетельства локальной редакции; Git/Dolt-публикация и закрытие задачи
ими не утверждаются. Итоговое ревью точного снимка сохраняется в локальной
заметке задачи, не как второй источник состояния трекера.

## Метод проверки и границы

OpenCode 1.18.33, independent general review contexts, Linux, Python 3.14.7,
Git и PyYAML. Проверены source/installed metadata, полное byte parity 38 скилов,
owned resources новой пары, ссылки изменённых Markdown/OKF-concepts и diff.
Новый процесс `opencode debug skill` обнаружил `ris-tdd-implement-task` и базу
из проектной установки. Работающая исходная сессия не переоткрывает свой каталог
автоматически: для обычного выбора нового скила нужен restart OpenCode.

Два независимых reviewer-а реально применили инструкции к disposable Python
fixtures и проверили команды, выходы, файлы и hashes. Это reviewer-applied
execution, **не** доказательство автоматического routing/выбора модели во всех
новых сессиях. Отдельный reviewer проверяет весь prospective Git snapshot:
base tree + authorized overlays/additions/deletions, отдельно локальный контекст.

## Наблюдаемые результаты

| Область / критерии | Фактическое наблюдение | Результат |
|---|---|---|
| Standard / AC-001,003 | Автономная база без RIS-операций: baseline 3 tests GREEN, accepted negative-quantity guard + test, 4 tests GREEN с существующим consumer. TDD/snapshot resources ещё не читались. | PASS |
| TDD / AC-002,003 | Нулевой discount: тест добавлен без production edit; focused RED exit1, assertion 0 != 1000, production hash неизменен. Затем минимальный fix: focused GREEN 1/1, affected regression GREEN 3/3. | PASS |
| Refactor / AC-003 | GREEN 3/3 до/после локального извлечения выражения; test bytes неизменны, искусственный RED отсутствует. | PASS |
| Broken runner / AC-002 | ModuleNotFoundError exit1, behavioral tests не исполнялись; production неизменен, результат blocked/unverified, не RED и не повод сменить режим. | PASS для guard |
| Snapshot / AC-004 | Excluded dirty shipping.py даёт runtime failure 1999 != 1100; candidate с base bytes и authorized overlays проходит 2/2. Original dirty code, report и index byte-identical до/после. | PASS |
| Project composition / AC-005 | Test-only adapter exact read/guarded claim/read-back до target edits; база применена в tdd; assertion RED '' != 'anonymous' до production edit, focused GREEN и 2 affected tests GREEN. Документы inspected, justified no-change. | PASS |
| Reports / AC-006 | Default implementation.md append/read-back сохраняет sentinel history. Другие configured paths и explicit filename override project convention/default; convention bytes неизменны. | PASS |
| Separate-copy gap / AC-004,006 | current-copy.md прочитан только при supplied task-specific/separate-copy evidence; missing primary root оставил shared report unsaved/blocked, code/TDD results сохранены, 2 tests GREEN. Новый worktree не создавался. | PASS в bounded случае |
| Foreign claim / AC-005 | Guard отказал exit1 до target mutation; exact code bytes/hash и foreign owner сохранены. | PASS |
| Rename / AC-007 | Старых source/installed SKILL.md и alias нет; новая пара/ресурсы byte-identical, active README/catalog/map обновлены; прежние specs/reports не переписаны. | PASS |
| Contract review / AC-008 | Независимое ревью всех task paths не нашло high/medium замечаний; первоначальный unverified относился к ещё отсутствовавшим execution-свидетельствам. Behavioral review нашло один low wording issue, исправленный в source/install. | См. итоговое snapshot review |

BR-01 (низкий) уточнил revision gate: пересмотр нужен для изменений **beyond or
contrary to accepted requirements/design/contracts**, а не для самого уже
принятого изменения поведения. Loop/resources не изменились. Final-tree evidence
и повторная оценка исправленного wording принадлежат итоговому review.

## Воспроизводимые основания наблюдений

Portable probes: реальные функции pricing/discount/checkout, unittest assertions
с независимыми literal expectations, существующие consumers/regressions и
наблюдения modes/blobs/index. Wrapper probes: реальный пустой-name fallback,
unittest, отдельные v2 path settings и сохранённые implementation reports.
Fixture adapter использует JSON state и эксклюзивное single-reviewer окно;
guarded transaction, claim/read-back и foreign rejection наблюдались реально.
Это не production Beads, не CAS и не distributed-concurrency тест.

Полные локальные reviewer reports содержат команды, результаты, pre-change/
final hashes и критерии; публичная таблица выше сохраняет достаточное основание
без зависимости удалённого читателя от игнорируемого task workspace.

## Пределы

Единичные reviewer-applied прогоны одного Python-стека не доказывают стабильность
всех моделей/клиентов. Runtime routing на естественных запросах, остальные стеки,
real-worktree missing-primary case и production Beads concurrency не проверялись.
Feature-record protocol здесь не мигрируется: его гарантии принадлежат адаптеру,
а эта поставка проверяет сохранение границы и принятия/применимости входов.
Снимок с excluded code/local report проверен без Git-публикации; symlink/mode-
change/concurrent-write варианты не заявлены. Summary не заменяет отдельное
подтверждение опубликованной Git-ревизии, Dolt remote и критериев закрытия.
