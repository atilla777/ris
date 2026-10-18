"""Opt-in ordinary TUI ABI test, never an agent-behavior test.

RIS_OPENCODE_RUNTIME=/absolute/path/opencode python3 -B -m unittest discover
    -s tests/client_help -p test_runtime.py -v
All config/data/state/cache and the project are disposable. Semantic admission
uses the real client/server schema with resume=False, so no agent is started.
"""

import json
import os
from pathlib import Path
import pty
import select
import shutil
import signal
import subprocess
import tempfile
import time
import unittest

ROOT = Path(__file__).resolve().parents[2]


@unittest.skipUnless(
    os.environ.get("RIS_OPENCODE_RUNTIME"), "explicit installed runtime required"
)
class Runtime(unittest.TestCase):
    def test_installed_tui_loader_rendering_and_prompt_schema_without_agent(self):
        with tempfile.TemporaryDirectory(
            prefix="ris-help-runtime-", dir="/tmp/opencode"
        ) as raw:
            base = Path(raw)
            project = base / "project"
            plugin = project / ".opencode/plugins/ris-help"
            shutil.copytree(ROOT / "plugins/opencode/ris-help", plugin)
            (plugin / "tui.tsx").rename(plugin / "production.tsx")
            # Instrument only the external admission boundary, not a fabricated
            # context. Everything else is the actual installed host implementation.
            (plugin / "tui.tsx").write_text("""
import { Plugin } from "@opencode/plugin/tui";
import production from "./production.tsx";
import { writeFileSync } from "node:fs";
export default Plugin.define({id:"ris.help.runtime-test", async setup(ctx) {
  const calls = [];
  let admitted;
  const prompt = ctx.client.session.prompt.bind(ctx.client.session);
  ctx.client.session.prompt = async input => {
    calls.push(input);
    admitted = prompt({...input, resume:false});
    return admitted;
  };
  await production.setup(ctx);
  setTimeout(async () => {
    try {
      for (const input of ["simple", "full", "кратко", "полный"]) {
        await ctx.keymap.dispatch("ris.help", input);
        await new Promise(resolve => setTimeout(resolve, 120));
        ctx.ui.dialog.clear();
      }
      if (calls.length) throw Error("fixed views admitted a prompt");
      await ctx.keymap.dispatch("ris.help", "what is RIS?");
      for (let i=0; i<50 && !admitted; i++) await new Promise(resolve => setTimeout(resolve, 100));
      if (calls.length !== 1) throw Error("semantic admission missing");
      await admitted;
      const session = await ctx.client.session.get({sessionID:calls[0].sessionID});
      writeFileSync(process.env.RIS_RUNTIME_RESULT, JSON.stringify({version:ctx.app.version,calls,session}));
    } catch(error) { writeFileSync(process.env.RIS_RUNTIME_RESULT, JSON.stringify({error:String(error)})); }
  }, 1500);
}});
""")
            skill = project / ".opencode/skills/ris-proj-op-show-help/SKILL.md"
            skill.parent.mkdir(parents=True)
            skill.write_text(
                "---\nname: ris-proj-op-show-help\ndescription: Runtime ABI fixture only\n---\nFixture, not an agent test.\n"
            )
            result = base / "result.json"
            env = {k: v for k, v in os.environ.items() if not k.startswith("OPENCODE_")}
            for key in ("CONFIG", "DATA", "CACHE", "STATE"):
                p = base / key.lower()
                p.mkdir()
                env[f"XDG_{key}_HOME"] = str(p)
            env.update(TERM="xterm-256color", RIS_RUNTIME_RESULT=str(result))
            master, slave = pty.openpty()
            proc = subprocess.Popen(
                [env["RIS_OPENCODE_RUNTIME"], "--standalone", str(project)],
                stdin=slave,
                stdout=slave,
                stderr=slave,
                env=env,
                start_new_session=True,
            )
            os.close(slave)
            output = bytearray()
            try:
                deadline = time.monotonic() + 20
                while (
                    time.monotonic() < deadline
                    and proc.poll() is None
                    and not result.exists()
                ):
                    if select.select([master], [], [], 0.1)[0]:
                        try:
                            output.extend(os.read(master, 65536))
                        except OSError:
                            break
                self.assertTrue(
                    result.exists(), output.decode(errors="replace")[-5000:]
                )
                data = json.loads(result.read_text())
                self.assertNotIn("error", data, data)
                self.assertEqual(data["version"], "2.0.32")
                self.assertEqual(data["calls"][0]["text"], "what is RIS?")
                self.assertEqual(
                    data["calls"][0]["skills"][0]["name"], "ris-proj-op-show-help"
                )
                self.assertEqual(data["calls"][0]["delivery"], "queue")
                self.assertEqual(data["session"]["cost"], 0)
                self.assertEqual(data["session"]["tokens"]["input"], 0)
                self.assertEqual(data["session"]["tokens"]["output"], 0)
                self.assertIn(b"RIS", output)
                print("Real OpenCode ABI:", json.dumps(data, ensure_ascii=False))
            finally:
                if proc.poll() is None:
                    os.killpg(proc.pid, signal.SIGTERM)
                try:
                    proc.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    os.killpg(proc.pid, signal.SIGKILL)
                    proc.wait()
                os.close(master)


if __name__ == "__main__":
    unittest.main()
