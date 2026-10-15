"""Production package CLI checks, never agent sessions.

Capture the complete candidate (tracked + nonignored untracked files) before
building a disposable upstream. CI requires its tree to equal checked-out HEAD.
Only external network and deterministic utility-fault boundaries are substituted.
"""

import hashlib
import importlib
import json
import os
from pathlib import Path
import selectors
import shutil
import signal
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests/package_installation"))
w1 = importlib.import_module("test_cli")


def candidate():
    paths = subprocess.check_output(
        [
            "git",
            "-C",
            str(ROOT),
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
            "-z",
        ]
    ).split(b"\0")
    files = {}
    for raw in sorted(set(filter(None, paths))):
        path = os.fsdecode(raw)
        p = ROOT / path
        if not p.exists() and not p.is_symlink():
            continue  # Tracked deletion is part of the candidate.
        if p.is_symlink():
            files[path] = (0o120000, os.fsencode(os.readlink(p)))
        elif p.is_file():
            files[path] = (
                0o100755 if p.stat().st_mode & 0o111 else 0o100644,
                p.read_bytes(),
            )
        else:
            raise AssertionError(f"unsupported candidate entry: {path}")
    manifest = [
        {"path": p, "mode": f"{m:o}", "sha256": hashlib.sha256(b).hexdigest()}
        for p, (m, b) in sorted(files.items())
    ]
    fingerprint = hashlib.sha256(
        json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return files, manifest, fingerprint


class ProductionPackage(unittest.TestCase):
    # Attributes initialized by the explicitly composed W1 setup seam.
    project: Path
    fixture: Path
    base: Path
    bin: Path
    rules: Path
    git: str
    env: dict[str, str]
    # Reuse bounded W1 seams/oracle without inheriting its phase test matrix.
    g = w1.CLI.g
    put = w1.CLI.put
    commit = w1.CLI.commit
    cli = w1.CLI.cli
    ok = w1.CLI.ok
    journal = w1.CLI.journal
    rule = w1.CLI.rule
    apply_rule = w1.CLI.apply_rule
    offline_recovery = w1.CLI.offline_recovery

    @classmethod
    def setUpClass(cls):
        cls.files, cls.manifest, cls.fingerprint = candidate()
        print(
            f"\nW2 candidate manifest sha256={cls.fingerprint} files={len(cls.files)}",
            flush=True,
        )

    def setUp(self):
        w1.CLI.setUp(self)
        # W1 setup supplies utility shims. None of its minimal package is used:
        # remove every fixture payload and replace it with the complete candidate.
        for p in self.fixture.iterdir():
            if p.name == ".git":
                continue
            if p.is_dir() and not p.is_symlink():
                shutil.rmtree(p)
            else:
                p.unlink()
        for path, (mode, data) in self.files.items():
            p = self.fixture / path
            p.parent.mkdir(parents=True, exist_ok=True)
            if mode == 0o120000:
                p.symlink_to(os.fsdecode(data))
            else:
                p.write_bytes(data)
                p.chmod(mode & 0o777)
        self.a = self.commit("Complete actual W2 candidate")
        self.tree = self.g("rev-parse", "HEAD^{tree}")
        # Do not let fixture ignore/filter configuration silently omit input.
        entries = self.g("ls-tree", "-r", "HEAD").splitlines()
        actual = {}
        for entry in entries:
            meta, path = entry.split("\t", 1)
            mode, kind, oid = meta.split()
            actual[path] = (int(mode, 8), oid)
        expected_files = {
            path: (
                mode,
                hashlib.sha1(
                    b"blob " + str(len(data)).encode() + b"\0" + data
                ).hexdigest(),
            )
            for path, (mode, data) in self.files.items()
        }
        self.assertEqual(
            actual,
            expected_files,
            "disposable upstream must capture every candidate byte/mode",
        )
        if os.environ.get("CI"):
            expected = subprocess.check_output(
                [self.git, "-C", str(ROOT), "rev-parse", "HEAD^{tree}"], text=True
            ).strip()
            self.assertEqual(
                self.tree, expected, "CI must exercise the exact checked-out tree"
            )
        self.g("tag", "-f", "v-candidate")
        print(f"W2 upstream candidate commit={self.a} tree={self.tree}", flush=True)
        # Explicit derived transition fixture, never represented as shipped.
        self.put(
            "skills/ris-retired/SKILL.md",
            "---\nname: ris-retired\n---\nDerived transition only\n",
        )
        self.put("skills/ris-retired/resources/old", "retired resource\n")
        self.put("commands/opencode/ris-retired.md", "Derived transition only\n")
        self.put(
            "skills/ris-port-op-manage-installation/retired-resource", "old resource\n"
        )
        self.b = self.commit("Derived retirement fixture")
        self.g("reset", "--hard", self.a)
        self.g("tag", "-a", "v-candidate-annotated", "-m", "Candidate")
        self.foreign = {}
        for name in (
            "AGENTS.md",
            "ris.yaml",
            "docs/file",
            "tasks/local",
            "ris-outside",
            ".agents/skills/ris-x/data",
            ".opencode/skill/ris-x/data",
            ".opencode/commands/ris-x.md",
            ".opencode/opencode.json",
            ".opencode/skills/grilling/data",
            ".opencode/command/grillme.md",
        ):
            p = self.project / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes((name + "\n").encode())
            self.foreign[name] = p.read_bytes()

    @property
    def installed(self):
        return (
            self.project
            / ".opencode/skills/ris-port-op-manage-installation/scripts/ris-install.sh"
        )

    def preserved(self):
        for path, data in self.foreign.items():
            self.assertEqual((self.project / path).read_bytes(), data, path)
            self.assertFalse((self.project / path).is_symlink(), path)
            self.assertEqual((self.project / path).stat().st_mode & 0o777, 0o644, path)
        if hasattr(self, "git_before"):
            self.assertEqual(w1.oracle(self.project / ".git"), self.git_before)
            self.assertFalse((self.project / ".gitignore").exists())

    def git_ledger(self):
        self.ok(w1.run(self.git, "-C", str(self.project), "init", env=self.env))
        self.git_before = w1.oracle(self.project / ".git")

    def pause_update(self):
        # Full-package acquisition/backup is larger than W1's tiny fixtures.
        # The same real apply-copy boundary gets a bounded 90-second wait.
        self.rules.write_text(json.dumps([self.apply_rule()]))
        er, ew = os.pipe()
        cr, cw = os.pipe()
        env = dict(self.env, EVENT_FD=str(ew), CONTROL_FD=str(cr))
        p = subprocess.Popen(
            [w1.BASH, str(self.installed), "update", "--project", str(self.project)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
            start_new_session=True,
            pass_fds=(ew, cr),
        )
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
        with selectors.DefaultSelector() as selector:
            selector.register(er, selectors.EVENT_READ)
            self.assertTrue(
                selector.select(90), "production apply boundary not reached in 90s"
            )
            event = os.read(er, 100)
        if not event:
            self.fail(f"CLI exited before boundary: {p.communicate(timeout=5)}")
        self.assertEqual(event, b"boundary\n")
        return kill

    def exact(self, result, revision=None):
        self.ok(result)
        revision = revision or self.a
        self.assert_package(revision)
        version = self.project / ".opencode/ris-installation"
        self.assertEqual(
            version.read_text(),
            f"format=1\nsource=https://github.com/atilla777/ris.git\nrevision={revision}\nharness=opencode\n",
        )
        self.assertIn(f"revision={revision}", result.stdout)
        self.assertIn(str(self.project), result.stdout)
        if revision == self.a:
            self.assertIn("skills=42 commands=38", result.stdout)
        self.assertFalse(self.journal.exists())
        self.preserved()

    def assert_package(self, revision):
        w1.CLI.assert_package(self, revision)  # Raw blob bytes/types/executable bits.
        expected_dirs = set()
        for raw in subprocess.check_output(
            [self.git, "-C", str(self.fixture), "ls-tree", "-rz", revision],
            env=self.env,
        ).split(b"\0"):
            if not raw:
                continue
            path = os.fsdecode(raw.split(b"\t", 1)[1])
            if path.startswith("skills/ris-"):
                parent = Path(".opencode") / Path(path).parent
                while str(parent).startswith(".opencode/skills/ris-"):
                    expected_dirs.add(str(parent))
                    parent = parent.parent
        actual_dirs = {
            p
            for p, entry in w1.oracle(self.project).items()
            if entry[0] == "dir" and p.startswith(".opencode/skills/ris-")
        }
        self.assertEqual(
            actual_dirs, expected_dirs, "no stale/extra managed directories"
        )

    def test_complete_candidate_default_tag_sha_and_self_lifecycle(self):
        self.assertFalse((self.project / ".git").exists())
        self.exact(self.cli())
        self.assertFalse((self.project / ".git").exists())
        self.git_ledger()
        for ref in ("v-candidate", "v-candidate-annotated", self.a):
            with self.subTest(ref=ref):
                self.exact(self.cli("install", "--ref", ref))
        (
            self.project / ".opencode/skills/ris-port-op-manage-installation/SKILL.md"
        ).write_text("local edit")
        self.put_target(".opencode/command/ris-collision.md", "collision")
        self.exact(self.cli("install", "--ref", self.a))
        self.exact(self.cli("update", "--ref", self.b, script=self.installed), self.b)
        self.exact(self.cli("update", "--ref", self.a, script=self.installed))
        self.ok(self.cli("uninstall", script=self.installed))
        self.assertFalse(self.installed.exists())
        self.assertFalse((self.project / ".opencode/ris-installation").exists())
        self.assertEqual(list((self.project / ".opencode/skills").glob("ris-*")), [])
        self.assertEqual(
            list((self.project / ".opencode/command").glob("ris-*.md")), []
        )
        self.env["OFFLINE"] = "1"
        r = self.cli("uninstall")
        self.ok(r)
        self.assertIn("offline no-op", r.stdout)
        self.assertFalse(self.journal.exists())
        self.preserved()

    def put_target(self, path, text):
        p = self.project / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def test_manual_no_version_and_git_visibility(self):
        self.exact(self.cli("install", "--ref", self.b), self.b)
        (self.project / ".opencode/ris-installation").unlink()
        outside = self.base / "external target"
        outside.write_bytes(b"external\0data")
        (self.project / ".opencode/command/ris-old-link.md").symlink_to(outside)
        self.git_ledger()
        self.exact(self.cli("update", "--ref", self.a))
        self.assertEqual(outside.read_bytes(), b"external\0data")
        status = w1.run(
            self.git,
            "-C",
            str(self.project),
            "status",
            "--short",
            "--untracked-files=all",
            env=self.env,
        )
        self.ok(status)
        self.assertIn(".opencode/ris-installation", status.stdout)
        self.assertIn(
            ".opencode/skills/ris-port-op-manage-installation/SKILL.md", status.stdout
        )
        self.assertFalse((self.project / ".gitignore").exists())

    def test_real_package_apply_failure_and_offline_sigkill_recovery(self):
        self.git_ledger()
        self.exact(self.cli("install", "--ref", self.b), self.b)
        before = w1.oracle(self.project)
        self.rules.write_text(json.dumps([self.apply_rule("fail")]))
        r = self.cli("update", "--ref", self.a, script=self.installed)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("restored", r.stderr)
        self.assertEqual(w1.oracle(self.project), before)
        self.assertFalse(self.journal.exists())
        kill = self.pause_update()
        self.assertTrue(self.journal.exists())
        self.assertNotEqual(w1.oracle(self.project), before)
        kill()
        self.offline_recovery()  # Restore must complete before failed clone.
        self.assertEqual(w1.oracle(self.project), before)
        self.assert_package(self.b)
        self.preserved()
        self.exact(self.cli("update", "--ref", self.a, script=self.installed))

    def test_readme_checked_download_and_same_pin(self):
        # Execute the actual documented block, changing only user inputs. The
        # curl shim supplies raw bytes of the requested Git blob, or a failure.
        readme = self.files["README.md"][1].decode()
        block = readme.split("```bash\n", 1)[1].split("```", 1)[0]
        block = block.replace(
            "project='/absolute/path/to/project'", "project=" + repr(str(self.project))
        )
        block = block.replace("ref=''", "ref=" + repr(self.a))
        shim = self.bin / "curl"
        shim.write_text("""#!/usr/bin/env python3
import os,sys,subprocess
from pathlib import Path
a=sys.argv[1:]
url=next(x for x in a if x.startswith("https://"))
Path(os.environ["CURL_LOG"]).write_text(url)
if os.environ.get("CURL_FAIL"): sys.exit(22)
prefix="https://raw.githubusercontent.com/atilla777/ris/"
assert url.startswith(prefix)
ref,path=url[len(prefix):].split("/",1)
data=subprocess.check_output([os.environ["REAL_GIT"],"-C",os.environ["FIXTURE"],"show",ref+":"+path])
Path(a[a.index("--output")+1]).write_bytes(data)
""")
        shim.chmod(0o755)
        self.env["CURL_LOG"] = str(self.base / "curl-url")
        self.exact(w1.run(w1.BASH, "-c", block, env=self.env))
        self.assertEqual(
            Path(self.env["CURL_LOG"]).read_text(),
            f"https://raw.githubusercontent.com/atilla777/ris/{self.a}/skills/ris-port-op-manage-installation/scripts/ris-install.sh",
        )
        before = w1.oracle(self.project)
        # A poisoned downloaded file makes accidental execution observable.
        self.env["CURL_FAIL"] = "1"
        shim.write_text(
            shim.read_text().replace(
                'if os.environ.get("CURL_FAIL"): sys.exit(22)',
                'if os.environ.get("CURL_FAIL"):\n Path(a[a.index("--output")+1]).write_text(\'touch -- "$EXECUTION_MARKER"\\n\')\n sys.exit(22)',
            )
        )
        self.env["EXECUTION_MARKER"] = str(self.base / "executed ' $ ; marker")
        r = w1.run(w1.BASH, "-c", block, env=self.env)
        self.assertNotEqual(r.returncode, 0)
        self.assertFalse(Path(self.env["EXECUTION_MARKER"]).exists())
        self.assertEqual(w1.oracle(self.project), before)
        self.preserved()

        # Positive control for the negative oracle: a disposable in-memory
        # regression executes the failed download but still exits nonzero.
        # The marker must reveal execution despite spaces/shell metacharacters.
        unsafe_block = block.replace(
            "    exit 1\n", '    bash "$installer"\n    exit 1\n', 1
        )
        self.assertNotEqual(unsafe_block, block)
        control = w1.run(w1.BASH, "-c", unsafe_block, env=self.env)
        self.assertNotEqual(control.returncode, 0)
        self.assertTrue(
            Path(self.env["EXECUTION_MARKER"]).is_file(),
            "negative oracle must detect deliberate poison execution",
        )
        self.assertEqual(w1.oracle(self.project), before)
        self.preserved()


if __name__ == "__main__":
    unittest.main()
