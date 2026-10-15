"""Real filesystem/CLI tests; Python is a development dependency only."""
import os
import json
import selectors
import signal
import hashlib
from pathlib import Path
import shutil
import stat
import subprocess
import tempfile
import unittest

BASH = os.environ.get("RIS_TEST_BASH", "/bin/bash")
SCRIPT = Path(__file__).resolve().parents[2] / "skills/ris-port-op-manage-installation/scripts/ris-install.sh"


def run(*args, **kw):
    return subprocess.run(args, text=True, capture_output=True, **kw)


def oracle(root):
    result = {}
    def visit(p):
        s = p.lstat()
        key = str(p.relative_to(root))
        mode = stat.S_IMODE(s.st_mode)
        if p.is_symlink():
            result[key] = ("link", mode, os.readlink(p))
        elif p.is_dir():
            result[key] = ("dir", mode)
            for child in sorted(p.iterdir()):
                visit(child)
        else:
            result[key] = ("file", mode, p.read_bytes())
    for p in sorted(root.iterdir()):
        visit(p)
    return result


class Feasibility(unittest.TestCase):
    def test_g0_copy_and_fd_lock(self):
        with tempfile.TemporaryDirectory(prefix="ris G0 ") as d:
            p = Path(d)
            a = p / "source"
            a.mkdir(mode=0o751)
            (a / "empty dir").mkdir(mode=0o711)
            (a / "file").write_bytes(b"bytes\x00\n")
            (a / "file").chmod(0o641)
            (a / "link").symlink_to("missing outside")
            r = run("cp", "-pPR", str(a), str(p / "copy"))
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(oracle(a), oracle(p / "copy"))
            self.assertEqual(stat.S_IMODE(a.stat().st_mode), stat.S_IMODE((p / "copy").stat().st_mode))
            lock = p / "lock"
            owner = subprocess.Popen([BASH, "-c", 'exec 8>"$1"; flock -n 8 || exit; printf "ready\\n"; read answer', "g0", str(lock)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
            assert owner.stdout is not None
            with selectors.DefaultSelector() as s:
                s.register(owner.stdout, selectors.EVENT_READ)
                self.assertTrue(s.select(5), "G0 lock owner did not start")
            self.assertEqual(owner.stdout.readline(), "ready\n")
            contender = [BASH, "-c", 'exec 8>"$1"; flock -n 8', "g0", str(lock)]
            self.assertNotEqual(run(*contender).returncode, 0)
            owner.kill()
            owner.communicate(timeout=5)
            self.assertEqual(run(*contender).returncode, 0)


class CLI(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ris CLI ")
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.project = self.base / "project space"
        self.project.mkdir()
        self.fixture = self.base / "fixture"
        self.fixture.mkdir()
        self.git = shutil.which("git")
        assert self.git is not None
        self.env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                        GIT_AUTHOR_DATE="2026-01-01T00:00:00Z", GIT_COMMITTER_DATE="2026-01-01T00:00:00Z")
        self.g("init", "-b", "delivery")
        self.g("config", "user.email", "test@example.invalid")
        self.g("config", "user.name", "Fixture")
        self.put("skills/ris-port-op-manage-installation/SKILL.md", "---\nname: ris-port-op-manage-installation\n---\nFixture only\n")
        self.put("skills/ris-port-op-manage-installation/scripts/ris-install.sh", SCRIPT.read_text(), 0o755)
        self.put("commands/opencode/ris-port-op-manage-installation.md", "Fixture only\n")
        self.put("skills/ris-old/SKILL.md", "---\nname: ris-old\n---\n")
        self.put("skills/ris-old/resources/file space", "old\n")
        self.put("commands/opencode/ris-old.md", "old\n")
        self.a = self.commit("A")
        self.g("tag", "v-a")
        shutil.rmtree(self.fixture / "skills/ris-old")
        (self.fixture / "commands/opencode/ris-old.md").unlink()
        self.put("skills/ris-new/SKILL.md", "---\nname: ris-new\n---\n")
        self.put("skills/ris-new/resources/new", "new\n")
        self.b = self.commit("B")
        self.g("tag", "-a", "v-b", "-m", "annotated")
        self.bin = self.base / "bin"
        self.bin.mkdir()
        shim = self.bin / "git"
        shim.write_text('''#!/usr/bin/env python3
import os,sys,subprocess
a=sys.argv[1:]
if "clone" in a and os.environ.get("OFFLINE"): sys.exit(73)
if "cat-file" in a and "blob" in a and os.environ.get("MUTATE_TAG"):
    subprocess.run([os.environ["REAL_GIT"],"-C",a[a.index("-C")+1],"update-ref","refs/tags/v-a",os.environ["MUTATE_TAG"]],check=True)
a=[os.environ["FIXTURE"] if x=="https://github.com/atilla777/ris.git" else x for x in a]
os.execv(os.environ["REAL_GIT"],[os.environ["REAL_GIT"]]+a)
''')
        shim.chmod(0o755)
        self.env.update(PATH=str(self.bin) + os.pathsep + os.environ["PATH"], FIXTURE=str(self.fixture), REAL_GIT=self.git)
        self.rules = self.base / "rules.json"
        self.rules.write_text("[]")
        self.env["FAULT_RULES"] = str(self.rules)
        for utility in ("cp", "mv", "rm", "mkdir", "rmdir"):
            real = shutil.which(utility)
            shim = self.bin / utility
            shim.write_text('''#!/usr/bin/env python3
import json,os,sys,subprocess
from pathlib import Path
p=Path(os.environ["FAULT_RULES"])
rules=json.loads(p.read_text())
rule=rules[0] if rules else None
match=rule and rule["tool"]==Path(sys.argv[0]).name and all(x in "\\0".join(sys.argv[1:]) for x in rule["contains"]) and ("last" not in rule or sys.argv[-1]==rule["last"])
if match:
    p.write_text(json.dumps(rules[1:]))
    if rule["action"]=="fail": sys.exit(71)
if not match or rule.get("when","after")=="after":
    r=subprocess.run([REAL]+sys.argv[1:])
    if r.returncode: sys.exit(r.returncode)
if match:
    os.write(int(os.environ["EVENT_FD"]),b"boundary\\n")
    os.read(int(os.environ["CONTROL_FD"]),1)
    if rule.get("when")=="before": sys.exit(subprocess.run([REAL]+sys.argv[1:]).returncode)
''' .replace("REAL", repr(real)))
            shim.chmod(0o755)

    def g(self, *args):
        r = run(self.git, "-C", str(self.fixture), *args, env=self.env)
        self.assertEqual(r.returncode, 0, r.stderr)
        return r.stdout.strip()

    def put(self, path, text, mode=0o644):
        p = self.fixture / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        p.chmod(mode)

    def commit(self, msg):
        self.g("add", "-A")
        self.g("commit", "-m", msg)
        return self.g("rev-parse", "HEAD")

    def cli(self, op="install", *args, script=None):
        return run(BASH, str(script or SCRIPT), op, "--project", str(self.project), *args, env=self.env)

    def ok(self, r):
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_install_exact_package(self):
        self.ok(self.cli("install", "--ref", "v-a"))
        oc = self.project / ".opencode"
        self.assertEqual((oc / "skills/ris-old/resources/file space").read_text(), "old\n")
        self.assertEqual((oc / "ris-installation").read_text(), f"format=1\nsource=https://github.com/atilla777/ris.git\nrevision={self.a}\nharness=opencode\n")
        self.assertTrue(os.access(oc / "skills/ris-port-op-manage-installation/scripts/ris-install.sh", os.X_OK))
        self.assertFalse((oc / ".ris-install-transaction").exists())
        self.assert_package(self.a)

    def assert_package(self, revision):
        assert self.git is not None
        entries = subprocess.check_output([self.git, "-C", str(self.fixture), "ls-tree", "-rz", revision], env=self.env).split(b"\0")
        expected = {}
        for entry in filter(None, entries):
            meta, path = entry.split(b"\t", 1)
            mode, kind, oid = meta.split()
            path = os.fsdecode(path)
            if path.startswith("skills/ris-"):
                dest = ".opencode/" + path
            elif path.startswith("commands/opencode/ris-"):
                dest = ".opencode/command/" + path.removeprefix("commands/opencode/")
            else:
                continue
            data = subprocess.check_output([self.git, "-C", str(self.fixture), "cat-file", "blob", oid.decode()], env=self.env)
            expected[dest] = ("file", 0o755 if mode == b"100755" else 0o644, data)
        actual = {k: v for k, v in oracle(self.project).items() if v[0] != "dir" and
                  (k.startswith(".opencode/skills/ris-") or k.startswith(".opencode/command/ris-"))}
        self.assertEqual(actual, expected)

    def old_manual(self):
        oc = self.project / ".opencode"
        (oc / "skills/ris-manual/empty dir").mkdir(parents=True)
        (oc / "skills/ris-manual/empty dir").chmod(0o711)
        (oc / "skills/ris-manual").chmod(0o751)
        (oc / "skills/ris-manual/file").write_bytes(b"old\x00bytes")
        (oc / "skills/ris-manual/file").chmod(0o641)
        outside = self.base / "outside"
        outside.write_text("do not touch")
        (oc / "skills/ris-manual/link").symlink_to(outside)
        (oc / "command").mkdir()
        (oc / "command/ris-link.md").symlink_to(outside)
        (oc / "skills/foreign").mkdir()
        (oc / "skills/foreign/data").write_text("foreign")
        (oc / "config.json").write_text("config")
        return oracle(self.project)

    def test_lifecycle_refs_and_self_removal(self):
        self.old_manual()
        self.ok(self.cli("update", "--ref", self.a))
        oc = self.project / ".opencode"
        self.assertFalse((oc / "skills/ris-manual").exists())
        (oc / "skills/ris-old/resources/file space").write_text("edit")
        self.ok(self.cli("install", "--ref", "v-a"))
        self.assertEqual((oc / "skills/ris-old/resources/file space").read_text(), "old\n")
        installed = oc / "skills/ris-port-op-manage-installation/scripts/ris-install.sh"
        self.ok(self.cli("update", "--ref", "v-b", script=installed))
        self.assertFalse((oc / "skills/ris-old").exists())
        self.assertTrue((oc / "skills/ris-new").is_dir())
        self.ok(self.cli("uninstall", script=installed))
        self.assertFalse(installed.exists())
        self.ok(self.cli("uninstall"))
        self.assertEqual((oc / "skills/foreign/data").read_text(), "foreign")
        self.assertEqual((self.base / "outside").read_text(), "do not touch")

    def test_apply_error_restores_exact_manual_snapshot(self):
        before = self.old_manual()
        self.rules.write_text(json.dumps([dict(tool="cp", contains=[], last=str(self.project / ".opencode/skills") + "/", action="fail")]))
        r = self.cli()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("restored", r.stderr)
        self.assertEqual(oracle(self.project), before)

    def test_invalid_source_and_refs_do_not_mutate(self):
        before = self.old_manual()
        for ref in ("delivery", "HEAD~1", "v-a^{commit}", "missing", "0" * 40):
            with self.subTest(ref=ref):
                self.assertNotEqual(self.cli("install", "--ref", ref).returncode, 0)
                self.assertEqual(oracle(self.project), before)
        self.put("skills/ris-new/link", "placeholder")
        (self.fixture / "skills/ris-new/link").unlink()
        (self.fixture / "skills/ris-new/link").symlink_to("/outside")
        self.commit("invalid link")
        self.assertNotEqual(self.cli().returncode, 0)
        self.assertEqual(oracle(self.project), before)

    @property
    def journal(self):
        return self.project / ".opencode/.ris-install-transaction"

    def rule(self, tool, suffix, action="barrier", when="after"):
        return dict(tool=tool, contains=[str(self.journal / suffix)], action=action, when=when)

    def apply_rule(self, action="barrier"):
        return dict(tool="cp", contains=[], last=str(self.project / ".opencode/skills") + "/", action=action)

    def pause(self, rules, op="install"):
        self.rules.write_text(json.dumps(rules))
        er, ew = os.pipe()
        cr, cw = os.pipe()
        env = dict(self.env, EVENT_FD=str(ew), CONTROL_FD=str(cr))
        p = subprocess.Popen([BASH, str(SCRIPT), op, "--project", str(self.project)],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env,
                             start_new_session=True, pass_fds=(ew, cr))
        os.close(ew)
        os.close(cr)
        self.addCleanup(os.close, er)
        self.addCleanup(os.close, cw)
        def kill():
            try:
                os.killpg(p.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            p.communicate(timeout=10)
        self.addCleanup(kill)
        with selectors.DefaultSelector() as s:
            s.register(er, selectors.EVENT_READ)
            self.assertTrue(s.select(20), "phase boundary not reached")
            event = os.read(er, 100)
        if not event:
            self.fail(f"CLI exited before boundary: {p.communicate(timeout=5)}")
        self.assertEqual(event, b"boundary\n")
        return p, cw, kill

    def offline_recovery(self):
        self.env["OFFLINE"] = "1"
        r = self.cli()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("not changed", r.stderr)
        self.env.pop("OFFLINE")
        self.assertFalse(self.journal.exists())

    def test_crash_before_and_during_apply(self):
        before = self.old_manual()
        for rule in (self.rule("mkdir", ""), self.rule("cp", "backup/.opencode/skills"), self.rule("mv", "prepared"),
                     self.apply_rule(), self.rule("mv", "committed", when="before")):
            with self.subTest(rule=rule):
                p, control, kill = self.pause([rule])
                kill()
                self.offline_recovery()
                self.assertEqual(oracle(self.project), before)

    def test_repeated_interrupted_rollback(self):
        before = self.old_manual()
        p, control, kill = self.pause([self.apply_rule("fail"), self.rule("cp", "backup/.opencode/skills/ris-manual")])
        kill()
        backup = oracle(self.journal / "backup")
        for _ in range(2):
            p, control, kill = self.pause([self.rule("cp", "backup/.opencode/skills/ris-manual")])
            kill()
            self.assertEqual(oracle(self.journal / "backup"), backup)
        self.offline_recovery()
        self.assertEqual(oracle(self.project), before)

    def test_terminal_cleanup_crashes(self):
        self.old_manual()
        for terminal in ("committed", "rolled-back"):
            for tool, suffix, when in (("mv", terminal, "after"), ("rm", "backup", "after"), ("rm", terminal, "after")):
                with self.subTest(terminal=terminal, suffix=suffix):
                    rules = [] if terminal == "committed" else [self.apply_rule("fail")]
                    rules.append(self.rule(tool, suffix, when=when))
                    p, control, kill = self.pause(rules)
                    state = oracle(self.project)
                    expected = {k: v for k, v in state.items() if ".ris-install-transaction" not in k}
                    kill()
                    self.offline_recovery()
                    self.assertEqual(oracle(self.project), expected)

    def test_rollback_failure_preserves_snapshot_for_retry(self):
        before = self.old_manual()
        self.rules.write_text(json.dumps([self.apply_rule("fail"), self.rule("cp", "backup/.opencode/skills/ris-manual", action="fail")]))
        r = self.cli()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("recovery required", r.stderr)
        self.assertTrue((self.journal / "prepared").is_file())
        self.offline_recovery()
        self.assertEqual(oracle(self.project), before)

    def test_busy_alias_and_child_lock_lifetime(self):
        self.old_manual()
        p, control, kill = self.pause([self.apply_rule()])
        at_boundary = oracle(self.project)
        alias = self.base / "alias"
        alias.symlink_to(self.project, target_is_directory=True)
        self.project = alias
        r = self.cli()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("busy", r.stderr)
        self.assertEqual(oracle(self.project), at_boundary)
        p.kill()  # Active utility still holds inherited FD 8.
        r = self.cli()
        self.assertIn("busy", r.stderr)
        kill()
        self.offline_recovery()

    def test_corrupt_journal_is_preserved(self):
        self.old_manual()
        p, control, kill = self.pause([self.rule("mv", "prepared")])
        kill()
        for name, content in (("schema", b"999\n"), ("manifest", b"../../outside\0"),
                              ("oracle", b"corrupt"), ("committed", b"1\n")):
            path = self.journal / name
            original = path.read_bytes() if path.exists() else None
            path.write_bytes(content)
            if name == "committed":
                (self.journal / "rolled-back").write_text("1\n")
            before = oracle(self.project)
            r = self.cli()
            self.assertNotEqual(r.returncode, 0)
            self.assertIn(str(self.journal), r.stderr)
            self.assertEqual(oracle(self.project), before)
            if original is None:
                path.unlink()
            else:
                path.write_bytes(original)
            if name == "committed":
                (self.journal / "rolled-back").unlink()
        self.offline_recovery()

    def test_terminal_cleanup_failure_reports_applied_even_after_last_marker(self):
        self.old_manual()
        self.rules.write_text(json.dumps([self.rule("rmdir", "", action="fail")]))
        r = self.cli()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("applied/cleanup incomplete", r.stderr)
        self.assertTrue((self.project / ".opencode/skills/ris-new").is_dir())
        self.offline_recovery()
        self.assertTrue((self.project / ".opencode/skills/ris-new").is_dir())

    def test_unsafe_parent_and_special_old_entries(self):
        before = self.old_manual()
        fifo = self.project / ".opencode/skills/ris-manual/fifo"
        os.mkfifo(fifo)
        self.assertNotEqual(self.cli().returncode, 0)
        self.assertTrue(stat.S_ISFIFO(fifo.lstat().st_mode))
        fifo.unlink()
        self.assertEqual(oracle(self.project), before)
        shutil.rmtree(self.project / ".opencode")
        outside = self.base / "outside-dir"
        outside.mkdir()
        (outside / "sentinel").write_text("outside")
        (self.project / ".opencode").symlink_to(outside)
        self.assertNotEqual(self.cli().returncode, 0)
        self.assertEqual((outside / "sentinel").read_text(), "outside")

    def test_dependency_preflight(self):
        # Version check is part of the contract; do not invoke target Git.
        shim = self.bin / "git"
        shim.write_text('#!/bin/sh\nif [ "$1" = --version ]; then printf "git version 2.19.0\\n"; exit 0; fi\nexit 88\n')
        r = self.cli("uninstall")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("Git 2.20", r.stderr)

    def test_foreign_reserved_looking_temp_file_is_not_overwritten(self):
        self.old_manual()
        p = self.project / ".opencode/.ris-version.tmp"
        p.write_text("foreign data")
        before = oracle(self.project)
        r = self.cli()
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(oracle(self.project), before)

    def test_malformed_frontmatter_rejected_before_snapshot(self):
        before = self.old_manual()
        for content in ("---\nname: ris-new\nno closing delimiter\n", "---\nname: wrong\nname: ris-new\n---\n"):
            self.put("skills/ris-new/SKILL.md", content)
            self.commit("bad frontmatter")
            self.assertNotEqual(self.cli().returncode, 0)
            self.assertEqual(oracle(self.project), before)

    def test_full_sha_must_be_commit_object_not_tag_object(self):
        before = self.old_manual()
        tag_object = self.g("rev-parse", "refs/tags/v-b")
        self.assertNotEqual(tag_object, self.b)
        self.assertNotEqual(self.cli("install", "--ref", tag_object).returncode, 0)
        self.assertEqual(oracle(self.project), before)

    def test_failed_uninstall_and_first_install_restore(self):
        self.rules.write_text(json.dumps([self.rule("mv", "committed", action="fail")]))
        r = self.cli()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("restored", r.stderr)
        self.assertFalse(self.journal.exists())
        self.assertEqual(list((self.project / ".opencode/skills").iterdir()), [])
        self.ok(self.cli())
        before = oracle(self.project)
        self.rules.write_text(json.dumps([self.rule("mv", "committed", action="fail")]))
        r = self.cli("uninstall")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("restored", r.stderr)
        self.assertEqual(oracle(self.project), before)

    def test_signal_rolls_back_and_interrupted_uninstall(self):
        before = self.old_manual()
        for sig in (signal.SIGTERM, signal.SIGINT):
            p, control, kill = self.pause([self.apply_rule()])
            os.kill(p.pid, sig)
            os.write(control, b"x")
            stdout, stderr = p.communicate(timeout=15)
            self.assertNotEqual(p.returncode, 0)
            self.assertIn(b"restored", stderr)
            self.assertEqual(oracle(self.project), before)
        p, control, kill = self.pause([self.rule("mv", "committed", when="before")], op="uninstall")
        kill()
        self.offline_recovery()
        self.assertEqual(oracle(self.project), before)

    def test_offline_noop_update_guard_and_default_head(self):
        self.env["OFFLINE"] = "1"
        noop = self.cli("uninstall")
        self.ok(noop)
        self.assertIn(str(self.project), noop.stdout)
        self.assertIn("skills=0 commands=0", noop.stdout)
        self.assertIn("Restart OpenCode", noop.stdout)
        r = self.cli("update")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("use install", r.stderr)
        self.assertEqual(oracle(self.project), {})
        self.env.pop("OFFLINE")
        self.ok(self.cli())
        self.assert_package(self.b)

    def test_project_foreign_ledger_and_git_visibility(self):
        foreign = ("AGENTS.md", "ris.yaml", "docs/file", "tasks/local", "ris-outside", ".agents/skills/ris-x/data",
                   ".opencode/skill/ris-x/data", ".opencode/commands/ris-x.md", ".opencode/config.json",
                   ".opencode/skills/custom/data", ".opencode/command/custom.md")
        for name in foreign:
            p = self.project / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(name)
        self.ok(run(self.git, "-C", str(self.project), "init", env=self.env))
        config = (self.project / ".git/config").read_bytes()
        for op in ("install", "update", "uninstall"):
            self.ok(self.cli(op))
            for name in foreign:
                self.assertEqual((self.project / name).read_text(), name)
            self.assertEqual((self.project / ".git/config").read_bytes(), config)
            self.assertFalse((self.project / ".git/index").exists())
            self.assertFalse((self.project / ".gitignore").exists())
            if op != "uninstall":
                status = run(self.git, "-C", str(self.project), "status", "--short", "--untracked-files=all", env=self.env)
                self.assertIn(".opencode/ris-installation", status.stdout)

    def test_symlink_bootstrap_is_copied_without_changing_source_mode(self):
        engine = self.base / "bootstrap-original"
        engine.write_bytes(SCRIPT.read_bytes())
        engine.chmod(0o644)
        link = self.base / "bootstrap-link"
        link.symlink_to(engine)
        self.ok(self.cli(script=link))
        self.assertEqual(stat.S_IMODE(engine.stat().st_mode), 0o644)

    def test_project_root_ending_in_newline(self):
        project = self.base / "project\n"
        project.mkdir()
        self.project = project
        self.ok(self.cli())
        self.assert_package(self.b)

    def test_external_selfcopy_cleanup_failure_is_nonzero(self):
        self.rules.write_text(json.dumps([dict(tool="rm", contains=["/tmp/ris-install."], action="fail")]))
        r = self.cli()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("cleanup incomplete", r.stderr)
        self.assert_package(self.b)

    def test_empty_unpublished_marker_is_recoverable_building(self):
        before = self.old_manual()
        self.journal.mkdir(mode=0o700)
        (self.journal / "schema.tmp").write_bytes(b"")
        self.offline_recovery()
        self.assertEqual(oracle(self.project), before)

    def test_corrupt_prepared_backup_never_applies_new_request(self):
        self.old_manual()
        p, control, kill = self.pause([self.rule("mv", "prepared")])
        kill()
        backup_file = self.journal / "backup/.opencode/skills/ris-manual/file"
        backup_file.write_bytes(b"damaged")
        before = oracle(self.project)
        r = self.cli()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("recovery", r.stderr)
        self.assertEqual(oracle(self.project), before)

    def test_tag_mutation_after_resolution_cannot_mix_package(self):
        self.env["MUTATE_TAG"] = self.b
        self.ok(self.cli("install", "--ref", "v-a"))
        self.assert_package(self.a)
        self.assertIn(self.a, (self.project / ".opencode/ris-installation").read_text())

    def test_missing_management_command_rejected(self):
        before = self.old_manual()
        (self.fixture / "commands/opencode/ris-port-op-manage-installation.md").unlink()
        self.commit("incomplete package")
        r = self.cli()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("missing management package", r.stderr)
        self.assertEqual(oracle(self.project), before)

    def git_context(self, **settings):
        self.env["GIT_CONFIG_COUNT"] = str(len(settings))
        for i, (key, value) in enumerate(settings.items()):
            self.env[f"GIT_CONFIG_KEY_{i}"] = key
            self.env[f"GIT_CONFIG_VALUE_{i}"] = value

    @staticmethod
    def raw_blob(data):
        return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

    def test_raw_hash_crlf_package_with_autocrlf(self):
        data = b"first\r\nsecond\r\n"
        self.put("skills/ris-new/resources/crlf", data.decode())
        revision = self.commit("raw CRLF blob")
        self.git_context(**{"core.autocrlf": "true"})
        self.ok(self.cli())
        self.assertEqual((self.project / ".opencode/skills/ris-new/resources/crlf").read_bytes(), data)
        self.assert_package(revision)

    def test_raw_hash_package_ignores_required_clean_filter(self):
        attrs = self.base / "global attributes"
        attrs.write_text("* filter=ris-review\n")
        self.git_context(**{"core.attributesFile": str(attrs),
                            "filter.ris-review.clean": "false",
                            "filter.ris-review.required": "true"})
        self.ok(self.cli())
        self.assert_package(self.b)

    def test_raw_hash_recovery_survives_git_context_change(self):
        # CRLF in root also exercises the raw stdin lock key. No target Git needed.
        self.project = self.base / "physical root\r\n"
        self.project.mkdir()
        self.old_manual()
        file = self.project / ".opencode/skills/ris-manual/file"
        data = b"old\r\nbytes\r\n"
        file.write_bytes(data)
        (self.project / ".opencode/skills/foreign/data").write_bytes(b"foreign\r\n")
        before = oracle(self.project)
        self.git_context(**{"core.autocrlf": "true"})
        p, control, kill = self.pause([self.rule("mv", "prepared")])
        kill()
        ledger = (self.journal / "oracle").read_bytes()
        foreign = (self.journal / "foreign").read_bytes()
        manifest = (self.journal / "manifest").read_bytes()
        self.git_context(**{"core.autocrlf": "false"})
        self.offline_recovery()
        self.assertEqual(oracle(self.project), before)
        records = ledger.split(b"\0")[:-1]
        checksums = {records[i]: records[i + 3] for i in range(0, len(records), 4)}
        self.assertEqual(checksums[b".opencode/skills/ris-manual/file"], self.raw_blob(data).encode())
        self.assertIn(self.raw_blob(b"foreign\r\n").encode(), foreign.split(b"\0"))
        self.assertEqual(manifest, b".opencode/skills/ris-manual\0.opencode/command/ris-link.md\0")
        key = self.raw_blob(os.fsencode(str(self.project.resolve())))
        self.assertTrue((Path(f"/tmp/ris-install-locks-{os.getuid()}") / (key + ".lock")).is_file())

    def test_raw_hash_legacy_filtered_schema1_ledger_is_not_rewritten(self):
        self.old_manual()
        data = b"legacy\r\nbytes\r\n"
        (self.project / ".opencode/skills/ris-manual/file").write_bytes(data)
        before = oracle(self.project)
        p, control, kill = self.pause([self.rule("mv", "prepared")])
        kill()
        self.assertEqual((self.journal / "schema").read_bytes(), b"1\n")
        ledger_path = self.journal / "oracle"
        raw = ledger_path.read_bytes()
        raw_hash = self.raw_blob(data).encode()
        filtered_hash = self.raw_blob(data.replace(b"\r\n", b"\n")).encode()
        self.assertNotEqual(raw_hash, filtered_hash)
        self.assertEqual(raw.split(b"\0").count(raw_hash), 1)
        # Disposable historical-data fixture, not an installer migration:
        # schema-1 encoding with the old writer's EOL-normalized checksum.
        ledger_path.write_bytes(raw.replace(raw_hash, filtered_hash))
        retained = oracle(self.project)
        self.git_context(**{"core.autocrlf": "true"})
        r = self.cli()
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("invalid backup", r.stderr)
        self.assertEqual(oracle(self.project), retained)
        # Controller restores its own original test data; runtime never rewrites it.
        ledger_path.write_bytes(raw)
        self.offline_recovery()
        self.assertEqual(oracle(self.project), before)

    def test_invalid_cli_has_diagnostic(self):
        r = run(BASH, str(SCRIPT), "install", "--project", "/", "--project", "/")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("duplicate", r.stderr)
        before = oracle(self.project)
        for args in (("uninstall", "--project", str(self.project), "--ref", "v-a"),
                     ("install", "--project", str(self.project), "--source", "other"),
                     ("install", "--project", str(self.project), "--ref", "v-a", "--ref", "v-b"),
                     ("install", "--project", "relative"), ("install",)):
            self.assertNotEqual(run(BASH, str(SCRIPT), *args, env=self.env).returncode, 0)
            self.assertEqual(oracle(self.project), before)


if __name__ == "__main__":
    unittest.main()
