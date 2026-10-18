import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { registerHelp } from '../../plugins/opencode/ris-help/help.mjs';

function fixture(locale = 'en_US.UTF-8', route = { type: 'session', sessionID: 'ses_test' }) {
  const seen = { commands: [], shown: [], requests: [], errors: [] };
  const pages = { en: { daily: '# English daily', full: '# English full' }, ru: { daily: '# Русская краткая', full: '# Русская полная' } };
  const context = {
    keymap: { layer(factory) { seen.commands.push(...factory().commands); } },
    ui: { router: { current: () => route }, toast: { show: x => seen.errors.push(x) } },
    data: { location: { default: () => ({ directory: '/fixture' }), skill: {
      async sync() {}, list: () => [{ id: 'discovered-help-id', name: 'ris-proj-op-show-help' }],
    } } },
    client: { session: {
      async create(input) { seen.requests.push(['create', input]); return { id: 'ses_created' }; },
      async prompt(input) { seen.requests.push(['prompt', input]); },
    } },
  };
  context.ui.router.navigate = x => seen.requests.push(['navigate', x]);
  registerHelp(context, markdown => seen.shown.push(markdown), pages, locale);
  assert.equal(seen.commands.length, 1, 'register exactly one client command');
  const command = seen.commands[0];
  assert.deepEqual(command.slash, { name: 'ris-help', arguments: true });
  return { seen, context, command, pages };
}

test('fixed daily/full paths render exact bilingual Markdown and never contact server', async () => {
  for (const [locale, input, expected] of [
    ['en_US', undefined, '# English daily'], ['ru_RU', '', '# Русская краткая'],
    ['ru_RU', 'simple', '# English daily'], ['en_US', 'кратко', '# Русская краткая'],
    ['en_US', 'полный', '# Русская полная'], ['ru_RU', ' FULL ', '# English full'],
    ['en_US', 'подробная справка', '# Русская полная'], ['ru_RU', 'detailed', '# English full'],
  ]) {
    const f = fixture(locale);
    await f.command.run(input);
    assert.deepEqual(f.seen.shown, [expected]);
    assert.deepEqual(f.seen.requests, [], 'static views cannot invoke model/session APIs');
  }
});

test('semantic question attaches exact help skill and preserves question, not a fake slash alias', async () => {
  const f = fixture();
  await f.command.run('explain full task vs simple task');
  assert.deepEqual(f.seen.shown, []);
  assert.deepEqual(f.seen.requests, [['prompt', {
    sessionID: 'ses_test', text: 'explain full task vs simple task',
    skills: [{ id: 'discovered-help-id', name: 'ris-proj-op-show-help' }], delivery: 'queue',
  }]]);
});

test('home question creates a location-scoped session and navigates after admission', async () => {
  const f = fixture('en', { type: 'home' });
  await f.command.run('what is RIS?');
  assert.deepEqual(f.seen.requests.map(x => x[0]), ['create', 'prompt', 'navigate']);
  assert.deepEqual(f.seen.requests[0][1].location, { directory: '/fixture' });
  assert.equal(f.seen.requests[1][1].sessionID, 'ses_created');
});

test('forwarding failure is visible and is never retried or silently replaced', async () => {
  const f = fixture();
  f.context.client.session.prompt = async () => { throw new Error('skill not installed'); };
  await f.command.run('where to start?');
  assert.equal(f.seen.errors.length, 1);
  assert.match(f.seen.errors[0].message, /skill not installed/);
  assert.deepEqual(f.seen.shown, []);
});

test('missing or ambiguous skill prevents session creation and model admission', async () => {
  for (const skills of [[], [{ id: 'one', name: 'ris-proj-op-show-help' }, { id: 'two', name: 'ris-proj-op-show-help' }]]) {
    const f = fixture('en', { type: 'home' });
    f.context.data.location.skill.list = () => skills;
    await f.command.run('how do I start?');
    assert.deepEqual(f.seen.requests, []);
    assert.equal(f.seen.errors.length, 1);
  }
});

test('standalone bilingual pages preserve the same operation inventory without an agent facade', () => {
  const read = name => readFileSync(new URL(`../../plugins/opencode/ris-help/pages/${name}.md`, import.meta.url), 'utf8');
  const identifiers = page => [...page.matchAll(/\/(?:ris-help|risp-[a-z-]+|risb-[a-z-]+)|ris-(?:port|proj)-[a-z-]+/g)].map(x => x[0]);
  for (const view of ['daily', 'full']) {
    const en = read(`${view}.en`), ru = read(`${view}.ru`);
    assert.deepEqual(identifiers(ru), identifiers(en));
    assert.ok(en.startsWith('# RIS · '));
    assert.ok(ru.startsWith('# RIS · '));
    assert.ok(!en.includes('Return only the Markdown'));
  }
  assert.equal(existsSync(new URL('../../commands/opencode/ris-help.md', import.meta.url)), false);
});
