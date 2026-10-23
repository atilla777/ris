# Постоянное полномочие проекта на безопасную синхронизацию основной копии

Task-ID: ris-3a4
Summary: Принятая ограниченная политика проекта может включать local maintenance после подтверждённой Git-публикации.

## Основание и область

23.10.2026 пользователь поручил проверить explicit-only ограничение и при
подтверждении реализовать предложенную policy-ветку, сохранив guards, remote-only
без политики, исторические specs и отдельные Git/local/close/Dolt эффекты.
Проверка исходников на `e4ea9ddba8c20144c05a248e70e4c0ed9c8fcb05` подтвердила:
publish-task и primary-sync признавали только отдельный явный local-update request.
Это намеренный прежний контракт, но он не учитывал уже принятые проектом полномочия.
Наблюдение пользователя об устаревшем node_modules не выдаётся за независимо
воспроизведённую runtime-причину. Yamboid и другие проекты этой работой не меняются.

Это самостоятельная bounded maintenance-поправка по поручению пользователя, не
новая feature lifecycle/specification и не переоценка прежних принятий. Она адресно
заменяет explicit-only норму текущих инструкций; исторические ris-ppw S1/D1,
scs-contract-seams, sdlc-continuity, task-execution, fast-task-execution и их
acceptance/design/delivery evidence остаются неизменными.

## Принятый объём и реализационное решение

1. Явное поручение **или применимая принятая политика проекта** — два допустимых
   источника полномочия. Без обоих local mutations нет, default remote-only.
   Caller проверяет/передаёт действительный источник/версию/принятие политики и
   её границы; publisher читает сам источник, в том числе при direct/no-change/recovery.
2. Политика явно называет post-confirmation primary FF, source copy, local branch/
   remote ref, разрешённые эффекты, условия и исключения. Допустимы literal names
   либо однозначные привязки к установленным project targets. Общего «синхронизировать»,
   разрешения push или предложенного текста недостаточно. Более узкие ограничения
   сохраняются; конфликт/неизвестное authority блокирует только зависимый local effect.
3. Existing publisher и его primary-sync остаются единственным владельцем Git/FF.
   Нет нового portable base: это тот же operational Git result. Context отвечает
   только за paths/provenance; callers — за scope и combined result. Ни нового
   скила/реестра, ни ключа `ris.yaml`, ни глобальной auto-sync политики не вводится.
4. Все прежние guards сохраняются: уже primary symbolic HEAD, чистые tracked/index,
   нет незавершённых операций, untracked/ignored path/type collisions, неизвестных
   hooks и конфликтующих писателей; ancestry, pinned fresh remote tip после
   independent remote confirmation; только `merge --ff-only --no-edit`, без
   checkout/switch/reset/stash/autostash/pull/force, read-back и bounded retry.
5. Dependency refresh — отдельный условный local effect: точные command/cwd/trigger/
   outputs/side effects и безопасность, не следствие FF permission. У `npm ci`
   учитываются замена node_modules и lifecycle scripts. Lockfile сравнивается за
   весь before/after FF range; recovery не принимает unchanged HEAD за доказательство
   актуальности зависимостей. Неизвестные эффекты сначала сверяются, не повторяются вслепую.
6. Confirmed remote Git успешен независимо от local skipped/failed/unknown.
   Local/dependency result и before/after сообщаются отдельно. Обязательный по
   политике/поручению local remainder не позволяет объявить combined result
   завершённым, но не блокирует отдельные exact close/Dolt и не требует повторять push.
7. Только для RIS закрепляется bounded standing FF policy: обычная source copy,
   локальная `main` → установленный `origin/main` (`git@github.com:atilla777/ris.git`)
   после remote confirmation, со всеми guards, без dependency setup. Другие проекты
   не перенастраиваются; их собственная действующая политика проверяется отдельно.

## Проверяемые критерии и границы свидетельств

- Политика с достаточными границами включает safe FF; без политики/поручения —
  remote-only; dirty/detached/divergent/busy/collision copy остаётся нетронутой с
  точной причиной local skipped. Это сценарии чтения и независимого ревью
  инструкций, не разрешение на agent/live/scenario tests.
- Источники и installed mirrors скилов/команд/help совпадают по файлам/байтам/режимам;
  актуальные normative docs, AGENTS и help не противоречат authority-ветке.
  Исторические explicit-only формулировки допустимы только в исторических документах.
- Существующие client_help и package_installation suites, whitespace/static/resource/
  link проверки и независимое ревью полного publication tree; direct non-force
  origin/main push и independent remote read-back. Exact close/Dolt — отдельно.
- Статические проверки и program tests не доказывают live-надежность агента;
  фактический safe FF RIS при поставке относится лишь к этой проверенной копии/ревизии.
