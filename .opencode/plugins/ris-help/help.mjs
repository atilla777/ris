// Client-only command registration. Kept free of UI/runtime imports for unit tests.
export function registerHelp(context, show, pages, locale = 'en') {
  const target = 'ris-proj-op-show-help';
  const fixed = new Map([
    ['', ['daily', /^ru\b|^ru_/i.test(locale) ? 'ru' : 'en']],
    ...['simple', 'brief'].map(x => [x, ['daily', 'en']]),
    ...['простой', 'кратко'].map(x => [x, ['daily', 'ru']]),
    ...['full', 'detailed'].map(x => [x, ['full', 'en']]),
    ...['полный', 'подробная справка'].map(x => [x, ['full', 'ru']]),
  ]);
  context.keymap.layer(() => ({
    mode: 'global',
    commands: [{
      id: 'ris.help', title: 'RIS help', group: 'RIS', palette: true,
      slash: { name: 'ris-help', arguments: true },
      async run(input) {
        const text = (input ?? '').trim();
        const view = fixed.get(text.toLowerCase());
        if (view) {
          show(pages[view[1]][view[0]]);
          return;
        }
        try {
          const location = context.location ?? context.data.location.default();
          await context.data.location.skill.sync(location);
          const skills = (context.data.location.skill.list(location) ?? []).filter(x => x.name === target);
          if (skills.length !== 1) throw new Error(`Expected one installed ${target}; found ${skills.length}. Restart OpenCode after installing RIS.`);
          const route = context.ui.router.current();
          const sessionID = route.type === 'session' ? route.sessionID
            : (await context.client.session.create({ location, title: 'RIS help' })).id;
          await context.client.session.prompt({
            sessionID, text, skills: [{ id: skills[0].id, name: skills[0].name }],
            // A help question must not steer an already running task.
            delivery: 'queue',
          });
          if (route.type !== 'session') context.ui.router.navigate({ type: 'session', sessionID });
        } catch (error) {
          context.ui.toast.show({ title: 'RIS help', variant: 'error', message: String(error) });
        }
      },
    }],
  }));
}
