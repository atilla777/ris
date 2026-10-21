# T8 — проверенный результат штатного обновления

Проверка 2026-10-21 относится к ordinary task `ris-a1z`, принятой V1
`ff79c496b733756a86003b44e70eb72c60efa532`, T8 AC-026–028 и общим ограничениям.
Отдельное поручение пользователя продолжить T8 разрешило одно штатное обновление
основного проекта после T4; сохранение V1 само по себе его не разрешало.
Это свидетельство конкретной установки, не журнал реализации и не live-проверка.

## Выбранный комплект и сохранность наложений — AC-026

- Физическая цель: `/home/aleksei/plums/ris`, независимо подтверждённая как primary
  пользователя и зарегистрированная Git-копия `main`.
- Исходная установленная ревизия по четырёхстрочному маркеру:
  `ff79c496b733756a86003b44e70eb72c60efa532`.
- Полный выбранный исходный комплект:
  `05ca4a4b815f46463ab6aaa1e9892d5dc58f8623`, tree
  `f96af380d20f4ca0cbb8dad7cf5a6b0b3e6ad0ca`.
  До эффекта `git ls-remote https://github.com/atilla777/ris.git HEAD refs/heads/main`
  вернул этот SHA для обоих refs. Подвижный HEAD не использовался вместо pin.
- Свежие Beads-чтения подтвердили native task `ris-a1z`, `in_progress`, actor
  `ris-a1z-executor`, отсутствие детей и единственный blocks prerequisite
  `ris-yxa` в состоянии `closed`. Его T1–T3/T5–T7 prerequisites также закрыты.
- До замены сравнивались реальные установленнные байты и executable modes с Git
  baseline маркера и target: 30 управляемых файлов отличались от baseline.
  Из них 18 уже точно совпадали с target; остальные 12 прочитаны в сравнении
  baseline → installation → target. Их самостоятельные полезные изменения
  сохранены в target: document-based feature inputs/acceptance вместо JSON gates,
  безопасное primary-return/FF, самостоятельность авторизованных project writers.
  Target дополнительно содержит завершённые поправки T2/T4/T6/T7.
- Эти 12 файлов: adapter `references/claim.md`, `references/create.md`;
  flows `execute-simple-task`, `execute-task`, `initialize-project`,
  `prepare-feature`; operations `decompose-feature`, `prepare-task-worktree`,
  `publish-task`, `suggest-continuation` (их `SKILL.md`);
  design `references/acceptance-and-save.md`; help `references/routes.md`.
  Полные технические имена имеют обычный префикс `ris-proj-`.
  Claim exception перенесён в target `references/claim-preparation.md`, а не удалён.
- Полезных независимых управляемых изменений, отсутствующих в target, не найдено.
  Чужие `.opencode/skills/grilling/` и `.opencode/command/grillme.md` не входят
  в пакет и не заменяются. Это отличается от правок внутри доказанного RIS namespace.

## Единственный engine и результат — AC-027

Установленный owner `ris-port-op-manage-installation` применён с его собственным
engine. Байты/mode engine совпадали у baseline, установленной копии и target;
он уже поддерживал plugin manifest format 2 и transaction schema 2.
Bootstrap или альтернативный установщик не требовались.

```bash
bash /home/aleksei/plums/ris/.opencode/skills/ris-port-op-manage-installation/scripts/ris-install.sh update --project /home/aleksei/plums/ris --ref 05ca4a4b815f46463ab6aaa1e9892d5dc58f8623
```

Один вызов, exit **0**, stdout:

```text
RIS update: /home/aleksei/plums/ris source=https://github.com/atilla777/ris.git revision=05ca4a4b815f46463ab6aaa1e9892d5dc58f8623 skills=51 commands=20. Restart OpenCode; check git status.
```

Engine проверил полный выбранный Git tree, package bytes/modes, сохранность
чужого дерева и завершение транзакции. Его алгоритм не копировался. Дополнительно
прочитаны реальные каталог/маркер: **51 skill, 20 Markdown commands, 165 package
files** (skills + commands + help plugin; маркер отдельно). Маркер имеет ровно
ожидаемые четыре строки, полный pin и `harness=opencode`.

Проверены management skill, executable installer **0755**, `risb-installation.md`,
help `index.ts`, `tui.tsx`, `help.mjs` и четыре EN/RU daily/full страницы,
`validate_review.py`/`requirements.txt`, новые conditional claim/bug/review
resources. Первое дополнительное presence assertion ошибочно использовало имя
`validate-review.py`; исправлено на реальное `validate_review.py` из исходного
комплекта. Это ошибка проверки, не дефект установки; engine не повторялся.

Дополнительный before/after ledger семи entries подтвердил неизменность bytes,
типов и modes чужого grilling skill, grillme command, `.opencode/.gitignore`,
`package.json`, `package-lock.json`. Чужих plugin entries не было. Более широкое
сохранение чужих файлов проверено самим engine, не отдельным вторым установщиком.
После успеха отсутствуют `.opencode/.ris-install-transaction/` и временный engine
`/tmp/ris-install.R721LlJJ/`. Локальные stdout/stderr/exit и verification receipts:
`/tmp/opencode/ris-a1z-installation/`; их доступность на другой машине не обещается.

## Границы и продолжение — AC-028

Не добавлены постоянная parity-проверка, автообновление или зависимости.
Нет установки в worktree/global, агентских тестов, runtime/reliability/token claims.
TDD новых программных изменений неприменим: исходный код/engine не менялись.

**Пользователю необходимо вручную выйти из OpenCode и запустить его снова.**
Текущая сессия хранит ранее загруженные инструкции; обнаружение новых skill/
command/plugin текущим клиентом не проверялось. OpenCode не завершался автоматически.
Продолжающие агенты должны заново загрузить нужные изменившиеся operational
инструкции из установленного пакета указанной новой ревизии.

Пакет в primary отслеживается Git: штатное обновление оставило собственные
изменения `.opencode/ris-installation` и package files плюс новые resources.
Они сохранены без reset/stash/discard и повторной установки. Пользователь отдельно
явно принял publication-copy association: `/home/aleksei/plums/ris`, собственная
ветка `task/ris-a1z-publication` от base
`05ca4a4b815f46463ab6aaa1e9892d5dc58f8623`, полное независимое ревью перед push
и последующим безопасным возвратом на `main`, без коммитов в `main`.
Подготовка этой association проверена отдельным исполнителем
`ses_ea185901bffezPe8LV8N4kCSNs`; исходная task worktree/ветка не менялась.
В текущий полный staged candidate включены все 27 installed paths и этот документ,
перенесённый из исходной task copy с последующим уточнением данного абзаца.
Маркер остаётся pin установленного комплекта, а не будущего коммита публикации.
Независимое ревью полного результата, Git publication + primary reconciliation
и отдельные Beads result/close/Dolt publication ещё не выполнены этим исполнителем.
