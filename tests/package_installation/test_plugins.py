"""Plugin ownership and transaction checks against real CLI/filesystem fixtures."""

import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).parent))
import test_cli as w1


class Plugins(unittest.TestCase):
    g = w1.CLI.g
    put = w1.CLI.put
    commit = w1.CLI.commit
    cli = w1.CLI.cli
    ok = w1.CLI.ok
    rule = w1.CLI.rule
    journal = w1.CLI.journal
    pause = w1.CLI.pause
    offline_recovery = w1.CLI.offline_recovery

    def setUp(self):
        w1.CLI.setUp(self)
        self.put("plugins/opencode/ris-help/index.ts", "export default 'server';\n")
        self.put("plugins/opencode/ris-help/tui.tsx", "export default 'client';\n")
        self.put("plugins/opencode/ris-help/pages/daily.en.md", "# Daily\n")
        self.put(
            "plugins/opencode/ris-help/help.mjs", "export function registerHelp() {}\n"
        )
        for page in ("daily.ru", "full.en", "full.ru"):
            self.put(f"plugins/opencode/ris-help/pages/{page}.md", "# Help fixture\n")
        self.put(
            "skills/ris-port-op-manage-installation/references/plugin-ownership.txt",
            "ris-help\n",
        )
        self.plugin_revision = self.commit("Plugin fixture")
        foreign = self.project / ".opencode/plugins/foreign/index.ts"
        foreign.parent.mkdir(parents=True)
        foreign.write_bytes(b"foreign\0plugin")
        self.foreign = foreign

    def test_plugin_install_update_remove(self):
        self.ok(self.cli())
        plugin = self.project / ".opencode/plugins/ris-help"
        self.assertTrue((plugin / "tui.tsx").is_file(), "client plugin must be shipped")
        self.assertEqual((plugin / "tui.tsx").read_text(), "export default 'client';\n")
        (plugin / "local-edit").write_text("package directory is owned")
        self.ok(self.cli("update"))
        self.assertFalse((plugin / "local-edit").exists())
        self.ok(self.cli("uninstall"))
        self.assertFalse(plugin.exists())
        self.assertEqual(self.foreign.read_bytes(), b"foreign\0plugin")

    def test_foreign_collision_and_unsafe_parent_unchanged(self):
        plugin = self.project / ".opencode/plugins/ris-help"
        plugin.mkdir()
        (plugin / "index.ts").write_text("foreign same name")
        before = w1.oracle(self.project)
        result = self.cli()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ownership", result.stderr)
        self.assertEqual(w1.oracle(self.project), before)

    def test_plugin_apply_failure_rolls_back(self):
        self.ok(self.cli())
        before = w1.oracle(self.project)
        self.rules.write_text(
            json.dumps(
                [
                    {
                        "tool": "cp",
                        "contains": ["stage/.opencode/plugins/ris-help"],
                        "action": "fail",
                    }
                ]
            )
        )
        result = self.cli("update")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("restored", result.stderr)
        self.assertEqual(w1.oracle(self.project), before)

    def test_incomplete_plugin_source_is_rejected_before_target_changes(self):
        (self.fixture / "plugins/opencode/ris-help/pages/full.ru.md").unlink()
        self.commit("Incomplete plugin fixture")
        before = w1.oracle(self.project)
        result = self.cli()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("plugin", result.stderr)
        self.assertEqual(w1.oracle(self.project), before)

    def test_plugin_manifest_format_header_and_rejected_duplicates(self):
        manifest = (
            "skills/ris-port-op-manage-installation/references/command-ownership.txt"
        )
        self.put(manifest, "format=2\n")
        self.commit("Plugin package capability gate")
        self.ok(self.cli())
        self.ok(self.cli("update"))
        before = w1.oracle(self.project)
        self.put(manifest, "format=2\nformat=2\n")
        self.commit("Malformed duplicate capability gate")
        result = self.cli("update")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid plugin package format", result.stderr)
        self.assertEqual(w1.oracle(self.project), before)
        self.ok(self.cli("uninstall"))
        self.assertFalse((self.project / ".opencode/plugins/ris-help").exists())
        self.assertEqual(self.foreign.read_bytes(), b"foreign\0plugin")

    def test_plugin_sigkill_recovery_and_retirement(self):
        self.ok(self.cli())
        before = w1.oracle(self.project)
        _, _, kill = self.pause(
            [
                {
                    "tool": "cp",
                    "contains": ["stage/.opencode/plugins/ris-help"],
                    "action": "barrier",
                }
            ],
            "update",
        )
        kill()
        self.assertEqual((self.journal / "schema").read_text(), "2\n")
        self.offline_recovery()
        self.assertEqual(w1.oracle(self.project), before)
        self.ok(self.cli("update", "--ref", self.a))
        self.assertFalse((self.project / ".opencode/plugins/ris-help").exists())
        self.assertEqual(self.foreign.read_bytes(), b"foreign\0plugin")

    def test_unsafe_plugin_parent_and_link_collision(self):
        import shutil

        plugins = self.project / ".opencode/plugins"
        outside = self.base / "outside"
        outside.mkdir()
        shutil.rmtree(plugins)
        plugins.symlink_to(outside, target_is_directory=True)
        before = w1.oracle(self.project)
        self.assertNotEqual(self.cli().returncode, 0)
        self.assertEqual(w1.oracle(self.project), before)
        plugins.unlink()
        plugins.mkdir()
        (plugins / "ris-help").symlink_to(outside, target_is_directory=True)
        before = w1.oracle(self.project)
        self.assertNotEqual(self.cli().returncode, 0)
        self.assertEqual(w1.oracle(self.project), before)
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
