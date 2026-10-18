import { Plugin } from "@opencode/plugin"

// Paired server entry exposes the autodiscovered TUI entry; no server hooks.
export default Plugin.define({ id: "ris.help.server", setup() {} })
