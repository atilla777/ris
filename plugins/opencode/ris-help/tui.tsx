import { Plugin } from "@opencode/plugin/tui"
import { readFileSync } from "node:fs"
import { registerHelp } from "./help.mjs"

export default Plugin.define({
  id: "ris.help",
  setup(context) {
    const page = (name: string) => readFileSync(new URL(`./pages/${name}.md`, import.meta.url), "utf8")
    const pages = {
      en: { daily: page("daily.en"), full: page("full.en") },
      ru: { daily: page("daily.ru"), full: page("full.ru") },
    }
    registerHelp(context, (markdown: string) => {
      let scroll: any
      context.ui.dialog.show(() => {
        context.keymap.layer(() => ({
          mode: "modal",
          commands: [
            { bind: "j,down", run: () => scroll?.scrollBy(1) },
            { bind: "k,up", run: () => scroll?.scrollBy(-1) },
            { bind: "pagedown", run: () => scroll?.scrollBy(10) },
            { bind: "pageup", run: () => scroll?.scrollBy(-10) },
            { bind: "home", run: () => scroll?.scrollTo(0) },
            { bind: "end", run: () => scroll?.scrollTo(scroll.scrollHeight) },
          ],
        }))
        return <box flexDirection="column" padding={1}>
          <text fg={context.theme.text.base}>RIS · Esc: close · ↑/↓, PgUp/PgDn: scroll</text>
          <scrollbox ref={(value) => { scroll = value }} height={20}>
            <markdown content={markdown} conceal={true} />
          </scrollbox>
        </box>
      })
      context.ui.dialog.set({ size: "large" })
    }, pages, process.env.LC_ALL || process.env.LC_MESSAGES || process.env.LANG || "en")
  },
})
