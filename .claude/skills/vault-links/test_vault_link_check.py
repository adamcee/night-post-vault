#!/usr/bin/env python3
"""Tests for vault-link-check.py core functions.

Usage:
  python3 test_vault_link_check.py -v

Stdlib only. Each test builds a throwaway vault in a temp directory, so the
tests never read or write the real vault.
"""

import os
import shutil
import tempfile
import unittest
from pathlib import Path

# Import the module under test (its filename has hyphens, so load it by path)
import importlib.util
SCRIPT = Path(__file__).parent / "vault-link-check.py"
spec = importlib.util.spec_from_file_location("vault_link_check", SCRIPT)
vlc = importlib.util.module_from_spec(spec)


def load_module():
    """Load the module's functions without running main."""
    vlc.__dict__["__file__"] = str(SCRIPT)
    with open(SCRIPT, encoding="utf-8") as f:
        exec(compile(f.read(), "vault-link-check.py", "exec"), vlc.__dict__)


class TestExtractLinks(unittest.TestCase):
    """Tests for extract_links_from_content."""

    def setUp(self):
        load_module()

    def test_basic_link(self):
        content = "See [[some/note]] for details."
        links = vlc.extract_links_from_content(content)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0][2], "some/note")  # target path

    def test_aliased_link(self):
        content = "See [[some/note|display text]] for details."
        links = vlc.extract_links_from_content(content)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0][2], "some/note")

    def test_heading_link(self):
        content = "See [[some/note#Section One]] for details."
        links = vlc.extract_links_from_content(content)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0][2], "some/note")

    def test_aliased_heading_link(self):
        content = "See [[some/note#Section|display]] for details."
        links = vlc.extract_links_from_content(content)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0][2], "some/note")

    def test_block_ref_link(self):
        content = "See [[some/note#^block-id]] for details."
        links = vlc.extract_links_from_content(content)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0][2], "some/note")

    def test_same_note_heading_link_skipped(self):
        content = "Jump to [[#Findings]] below."
        links = vlc.extract_links_from_content(content)
        self.assertEqual(links, [])

    def test_multiple_links_on_one_line(self):
        content = "Both [[note-a]] and [[note-b]] matter."
        links = vlc.extract_links_from_content(content)
        self.assertEqual(len(links), 2)
        targets = {l[2] for l in links}
        self.assertEqual(targets, {"note-a", "note-b"})

    def test_skips_frontmatter(self):
        content = "---\ntags: [[not-a-link]]\n---\nBody [[real-link]]."
        links = vlc.extract_links_from_content(content)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0][2], "real-link")

    def test_skips_code_blocks(self):
        content = "Before\n```\n[[code-link]]\n```\nAfter [[real-link]]."
        links = vlc.extract_links_from_content(content)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0][2], "real-link")

    def test_skips_tilde_code_blocks(self):
        content = "Before\n~~~\n[[code-link]]\n```\n[[still-code]]\n~~~\nAfter [[real-link]]."
        links = vlc.extract_links_from_content(content)
        self.assertEqual([l[2] for l in links], ["real-link"])

    def test_skips_inline_code(self):
        content = "Use `[[not-a-link]]` but also [[real-link]]."
        links = vlc.extract_links_from_content(content)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0][2], "real-link")

    def test_escaped_pipe_in_table(self):
        """Obsidian escapes | as \\| inside table cells."""
        content = "| [[decisions/technical/ADR-T001-example\\|ADR-T001]] | desc |"
        links = vlc.extract_links_from_content(content)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0][2], "decisions/technical/ADR-T001-example")

    def test_no_links(self):
        content = "Just plain text with no links at all."
        links = vlc.extract_links_from_content(content)
        self.assertEqual(len(links), 0)

    def test_line_numbers_correct(self):
        content = "Line one.\n[[link-on-two]]\nLine three.\n[[link-on-four]]"
        links = vlc.extract_links_from_content(content)
        self.assertEqual(links[0][0], 2)  # line number
        self.assertEqual(links[1][0], 4)


class TestBuildResolutionIndex(unittest.TestCase):
    """Tests for build_resolution_index."""

    def setUp(self):
        load_module()

    def test_includes_path_without_extension(self):
        files = {"some/note.md", "other.md"}
        index = vlc.build_resolution_index(files)
        self.assertIn("some/note", index)
        self.assertIn("other", index)

    def test_includes_basename(self):
        files = {"deep/path/to/note.md"}
        index = vlc.build_resolution_index(files)
        self.assertIn("note", index)
        self.assertIn("deep/path/to/note", index)

    def test_includes_attachments_with_extension(self):
        index = vlc.build_resolution_index(set(), {"assets/map.png"})
        self.assertIn("assets/map.png", index)
        self.assertIn("map.png", index)
        self.assertNotIn("map", index)


class TestIsExempt(unittest.TestCase):
    """Tests for is_exempt."""

    def setUp(self):
        load_module()

    def test_archive_folders_exempt(self):
        self.assertTrue(vlc.is_exempt("archive/old.md"))
        self.assertTrue(vlc.is_exempt("research/archive/old.md"))

    def test_journal_exempt(self):
        self.assertTrue(vlc.is_exempt("journal/2026-01-01.md"))

    def test_untouched_originals_exempt(self):
        self.assertTrue(vlc.is_exempt("research/_source-report.md"))

    def test_regular_files_not_exempt(self):
        self.assertFalse(vlc.is_exempt("research/report.md"))
        self.assertFalse(vlc.is_exempt("archive-notes.md"))
        self.assertFalse(vlc.is_exempt("concepts/archive.md"))


class TestFindVaultRoot(unittest.TestCase):
    """Tests for find_vault_root."""

    def setUp(self):
        self.tmpdir = Path(tempfile.mkdtemp()).resolve()
        self.old_cwd = os.getcwd()
        load_module()

    def tearDown(self):
        os.chdir(self.old_cwd)
        shutil.rmtree(self.tmpdir)

    def test_finds_agents_md_above_cwd(self):
        (self.tmpdir / "AGENTS.md").write_text("# Test vault")
        sub = self.tmpdir / "research" / "deep"
        sub.mkdir(parents=True)
        os.chdir(sub)
        self.assertEqual(vlc.find_vault_root(), self.tmpdir)

    def test_ignores_claude_md(self):
        """CLAUDE.md is a pointer file; only AGENTS.md marks the vault root."""
        (self.tmpdir / "AGENTS.md").write_text("# Test vault")
        sub = self.tmpdir / "nested"
        sub.mkdir()
        (sub / "CLAUDE.md").write_text("# Pointer")
        os.chdir(sub)
        self.assertEqual(vlc.find_vault_root(), self.tmpdir)


class VaultTestCase(unittest.TestCase):
    """Base class: a throwaway vault with AGENTS.md at its root."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        Path(self.tmpdir, "AGENTS.md").write_text("# Test vault")
        load_module()
        # Override VAULT_ROOT for tests
        vlc.VAULT_ROOT = Path(self.tmpdir)

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def _write(self, rel_path, content):
        full = Path(self.tmpdir) / rel_path
        full.parent.mkdir(parents=True, exist_ok=True)
        full.write_text(content)

    def _check(self, rel_path, ignore=None):
        md_files = vlc.get_all_md_files(Path(self.tmpdir))
        index = vlc.build_resolution_index(
            md_files, vlc.get_attachment_files(Path(self.tmpdir)))
        exact, prefixes = vlc.load_ignore_patterns(
            Path(self.tmpdir) / '.link-check-ignore')
        return vlc.check_file(str(Path(self.tmpdir) / rel_path), index, exact, prefixes)


class TestCheckFileIntegration(VaultTestCase):
    """Integration tests using a temporary vault."""

    def test_valid_links_pass(self):
        self._write("notes/alpha.md", "# Alpha")
        self._write("notes/beta.md", "See [[notes/alpha]] for details.")
        self.assertEqual(self._check("notes/beta.md"), [])

    def test_broken_link_detected(self):
        self._write("notes/beta.md", "See [[notes/nonexistent]] for details.")
        broken = self._check("notes/beta.md")
        self.assertEqual(len(broken), 1)
        self.assertEqual(broken[0]['target'], "notes/nonexistent")
        self.assertEqual(broken[0]['file'], "notes/beta.md")

    def test_aliased_link_resolves(self):
        self._write("decisions/technical/README.md", "# Tech decisions")
        self._write("guide.md", "In [[decisions/technical/README|decisions/technical/]].")
        self.assertEqual(self._check("guide.md"), [])

    def test_basename_resolution(self):
        self._write("deep/path/my-note.md", "# My Note")
        self._write("other.md", "See [[my-note]].")
        self.assertEqual(self._check("other.md"), [])

    def test_root_file_resolves(self):
        self._write("session-history.md", "# Session History")
        self._write("doc.md", "See [[AGENTS]] and [[session-history]].")
        self.assertEqual(self._check("doc.md"), [])

    def test_heading_link_resolves_if_note_exists(self):
        self._write("notes/alpha.md", "# Alpha\n## Section")
        self._write("notes/beta.md", "See [[notes/alpha#Section]].")
        self.assertEqual(self._check("notes/beta.md"), [])

    def test_frontmatter_links_ignored(self):
        self._write("test.md", "---\nsee: [[fake-note]]\n---\n# Body")
        self.assertEqual(self._check("test.md"), [])

    def test_mixed_valid_and_broken(self):
        self._write("real.md", "# Real note")
        self._write("checker.md", "Valid: [[real]]. Broken: [[fake]].")
        broken = self._check("checker.md")
        self.assertEqual(len(broken), 1)
        self.assertEqual(broken[0]['target'], "fake")

    def test_case_insensitive_resolution(self):
        self._write("strategy/audience/early-adopter.md", "# Early adopter")
        self._write("doc.md", "See [[Early-Adopter]] for details.")
        self.assertEqual(self._check("doc.md"), [])

    def test_escaped_pipe_in_table_resolves(self):
        self._write("decisions/technical/ADR-T001-example.md", "# ADR")
        self._write("doc.md", "| [[decisions/technical/ADR-T001-example\\|ADR-T001]] | desc |")
        self.assertEqual(self._check("doc.md"), [])

    def test_md_extension_in_link_resolves(self):
        self._write("notes/alpha.md", "# Alpha")
        self._write("doc.md", "See [[notes/alpha.md]].")
        self.assertEqual(self._check("doc.md"), [])

    def test_attachment_link_resolves(self):
        self._write("assets/map.png", "not really a png")
        self._write("doc.md", "![[assets/map.png]] and [[map.png]].")
        self.assertEqual(self._check("doc.md"), [])

    def test_link_into_archive_resolves(self):
        self._write("research/archive/old-study.md", "# Old")
        self._write("doc.md", "Superseded [[research/archive/old-study]].")
        self.assertEqual(self._check("doc.md"), [])

    def test_hidden_dirs_not_targets(self):
        self._write(".obsidian/hidden-note.md", "# Hidden")
        self._write("doc.md", "See [[hidden-note]].")
        self.assertEqual(len(self._check("doc.md")), 1)


class TestLoadIgnorePatterns(unittest.TestCase):
    """Tests for load_ignore_patterns and is_ignored."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        load_module()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def _write_ignore(self, content):
        p = Path(self.tmpdir) / '.link-check-ignore'
        p.write_text(content)
        return p

    def test_no_ignore_file(self):
        exact, prefixes = vlc.load_ignore_patterns(Path(self.tmpdir) / 'nonexistent')
        self.assertEqual(exact, set())
        self.assertEqual(prefixes, [])

    def test_exact_match(self):
        p = self._write_ignore("prototype/specs/future-spec\n")
        exact, prefixes = vlc.load_ignore_patterns(p)
        self.assertIn("prototype/specs/future-spec", exact)
        self.assertTrue(vlc.is_ignored("prototype/specs/future-spec", exact, prefixes))
        self.assertFalse(vlc.is_ignored("prototype/specs/other", exact, prefixes))

    def test_prefix_match(self):
        p = self._write_ignore("github/*\n")
        exact, prefixes = vlc.load_ignore_patterns(p)
        self.assertTrue(vlc.is_ignored("github/user/repo", exact, prefixes))
        self.assertTrue(vlc.is_ignored("github/anything", exact, prefixes))
        self.assertFalse(vlc.is_ignored("notgithub/foo", exact, prefixes))

    def test_comments_and_blanks_skipped(self):
        p = self._write_ignore("# This is a comment\n\nreal-target\n  \n# Another comment\n")
        exact, prefixes = vlc.load_ignore_patterns(p)
        self.assertEqual(exact, {"real-target"})
        self.assertEqual(prefixes, [])

    def test_case_insensitive(self):
        p = self._write_ignore("Future-Note\n")
        exact, prefixes = vlc.load_ignore_patterns(p)
        self.assertTrue(vlc.is_ignored("future-note", exact, prefixes))
        self.assertTrue(vlc.is_ignored("FUTURE-NOTE", exact, prefixes))

    def test_trailing_slash_exact(self):
        p = self._write_ignore("architecture/\n")
        exact, prefixes = vlc.load_ignore_patterns(p)
        self.assertTrue(vlc.is_ignored("architecture", exact, prefixes))

    def test_prefix_with_slash_star(self):
        p = self._write_ignore("research/interviews/*\n")
        exact, prefixes = vlc.load_ignore_patterns(p)
        self.assertTrue(vlc.is_ignored("research/interviews/user-03", exact, prefixes))
        self.assertFalse(vlc.is_ignored("research/surveys/survey-01", exact, prefixes))


class TestIgnoreIntegration(VaultTestCase):
    """Integration test: ignore file suppresses broken link reports."""

    def test_ignored_target_not_reported(self):
        self._write("doc.md", "See [[fake-note]] and [[github/user/repo]].")
        self._write(".link-check-ignore", "fake-note\ngithub/*\n")
        self.assertEqual(self._check("doc.md"), [])

    def test_non_ignored_target_still_reported(self):
        self._write("doc.md", "See [[fake-note]] and [[real-broken]].")
        self._write(".link-check-ignore", "fake-note\n")
        broken = self._check("doc.md")
        self.assertEqual(len(broken), 1)
        self.assertEqual(broken[0]['target'], "real-broken")


if __name__ == '__main__':
    unittest.main()
