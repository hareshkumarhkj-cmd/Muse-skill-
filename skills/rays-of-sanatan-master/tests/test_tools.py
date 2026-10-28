from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from check_project import validate_project
from package_handoff import package_project


class ProjectChecks(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.base = Path(self.temporary.name)
        self.root = self.base / "project"
        (self.root / "public").mkdir(parents=True)
        (self.root / "src").mkdir()
        (self.root / "public" / "image.png").write_bytes(b"fixture-image-content")
        for path in ["TASK.md", "README.txt", "TEST-NOTE.txt", "package.json", "package-lock.json", "remotion.config.ts", "src/index.ts"]:
            (self.root / path).write_text("{}" if path == "package.json" else "test fixture", encoding="utf-8")
        self.contract = {
            "schema_version": 1,
            "project": {"composition_id": "RaysShort01", "width": 1080, "height": 1920, "fps": 30,
                        "duration_frames": 450, "stage": "visual-proof", "motion_mode": "still-motion", "audio_mode": "silent"},
            "scenes": [{"id": "hook", "start_frame": 0, "end_frame": 90, "visual_type": "still", "asset": "public/image.png", "caption": "Hook"},
                       {"id": "end", "start_frame": 90, "end_frame": 450, "visual_type": "code", "asset": None, "caption": "End"}],
            "assets": [{"path": "public/image.png", "kind": "image", "origin": "generated-original", "rights_note": "Original fixture",
                        "sha256": hashlib.sha256(b"fixture-image-content").hexdigest()}],
            "claims": [], "narration": [],
        }
        self.write_contract()

    def tearDown(self):
        self.temporary.cleanup()

    def write_contract(self):
        (self.root / "production-contract.json").write_text(json.dumps(self.contract), encoding="utf-8")

    def test_valid_contract(self):
        self.assertTrue(validate_project(self.root).ok)

    def test_composition_underscore_rejected(self):
        self.contract["project"]["composition_id"] = "Rays_Short01"
        self.write_contract()
        self.assertTrue(any("composition_id" in e for e in validate_project(self.root).errors))

    def test_composition_hyphen_allowed(self):
        self.contract["project"]["composition_id"] = "Rays-Short01"
        self.write_contract()
        self.assertTrue(validate_project(self.root).ok)

    def add_audio_asset(self):
        content = b"test audio fixture"
        (self.root / "public" / "sound.wav").write_bytes(content)
        self.contract["assets"].append({"path": "public/sound.wav", "kind": "audio", "origin": "user-supplied",
                                        "rights_note": "User test fixture", "sha256": hashlib.sha256(content).hexdigest()})

    def test_sound_only_valid(self):
        self.contract["project"]["audio_mode"] = "sound-only"
        self.add_audio_asset()
        self.write_contract()
        self.assertTrue(validate_project(self.root).ok)

    def test_sound_only_missing_asset_fails(self):
        self.contract["project"]["audio_mode"] = "sound-only"
        self.write_contract()
        self.assertTrue(any("audio asset" in e for e in validate_project(self.root).errors))

    def test_sound_only_narration_rejected(self):
        self.contract["project"]["audio_mode"] = "sound-only"
        self.add_audio_asset()
        self.contract["narration"] = [{"text": "A line", "start_frame": 0, "end_frame": 90, "audio_file": "public/sound.wav"}]
        self.write_contract()
        self.assertTrue(any("empty narration" in e for e in validate_project(self.root).errors))

    def test_packaging_requires_lockfile(self):
        (self.root / "package-lock.json").unlink()
        with self.assertRaisesRegex(ValueError, "package-lock.json"):
            package_project(self.root, self.base / "handoff.zip")

    def test_scene_gap_fails(self):
        self.contract["scenes"][1]["start_frame"] = 91
        self.write_contract()
        self.assertTrue(any("gap/overlap" in e for e in validate_project(self.root).errors))

    def test_scene_overlap_fails(self):
        self.contract["scenes"][1]["start_frame"] = 89
        self.write_contract()
        self.assertFalse(validate_project(self.root).ok)

    def test_traversal_fails(self):
        self.contract["assets"][0]["path"] = "../outside.png"
        self.write_contract()
        self.assertFalse(validate_project(self.root).ok)

    def test_wrong_hash_fails(self):
        self.contract["assets"][0]["sha256"] = "a" * 64
        self.write_contract()
        self.assertTrue(any("mismatch" in e for e in validate_project(self.root).errors))

    def test_missing_voice_fails(self):
        self.contract["project"]["audio_mode"] = "voiced"
        self.write_contract()
        self.assertFalse(validate_project(self.root).ok)

    def test_undeclared_narration_file_fails(self):
        self.contract["project"]["audio_mode"] = "voiced"
        self.contract["narration"] = [{"text": "Test", "start_frame": 0, "end_frame": 90, "audio_file": "public/missing.wav"}]
        self.write_contract()
        self.assertFalse(validate_project(self.root).ok)

    def test_verified_claim_requires_sources(self):
        self.contract["claims"] = [{"id": "one", "classification": "verified", "sentence": "A claim", "sources": []}]
        self.write_contract()
        self.assertFalse(validate_project(self.root).ok)

    def test_malformed_ipv6_source_url_fails_without_crash(self):
        self.contract["claims"] = [{"id": "one", "classification": "verified", "sentence": "A claim", "sources": [
            {"url": "https://[broken", "title": "Source", "retrieved_date": "2026-10-28", "notes": "Checked"}
        ]}]
        self.write_contract()
        self.assertFalse(validate_project(self.root).ok)

    def test_nonarray_section_fails_without_crash(self):
        self.contract["claims"] = "not an array"
        self.write_contract()
        self.assertFalse(validate_project(self.root).ok)

    def test_boolean_frame_count_fails(self):
        self.contract["project"]["duration_frames"] = True
        self.write_contract()
        self.assertFalse(validate_project(self.root).ok)

    def test_nonstring_enumerations_fail_without_crash(self):
        self.contract["project"]["stage"] = []
        self.contract["assets"][0]["kind"] = {}
        self.contract["assets"][0]["origin"] = []
        self.contract["scenes"][0]["visual_type"] = []
        self.contract["claims"] = [{"id": "one", "classification": [], "sentence": "A claim", "sources": []}]
        self.write_contract()
        self.assertFalse(validate_project(self.root).ok)

    def test_asset_symlink_rejected(self):
        outside = self.base / "outside.png"
        outside.write_bytes(b"fixture-image-content")
        target = self.root / "public" / "image.png"
        target.unlink()
        target.symlink_to(outside)
        self.assertFalse(validate_project(self.root).ok)

    def test_unreferenced_symlink_rejected_by_packager(self):
        (self.root / "public" / "link").symlink_to(self.base)
        with self.assertRaisesRegex(ValueError, "symlink"):
            package_project(self.root, self.base / "handoff.zip")

    def test_output_inside_source_fails(self):
        with self.assertRaisesRegex(ValueError, "outside"):
            package_project(self.root, self.root / "handoff.zip")

    def test_zip_exclusions_and_integrity(self):
        for name in ["node_modules/dependency.js", ".git/config", "out/render.mp4", "dist/bundle.js", ".cache/item", ".env", "private.key"]:
            path = self.root / name
            path.parent.mkdir(exist_ok=True, parents=True)
            path.write_text("must not be shipped")
        output = self.base / "handoff.zip"
        count, skipped = package_project(self.root, output)
        self.assertGreater(count, 0)
        self.assertGreater(len(skipped), 0)
        with zipfile.ZipFile(output) as archive:
            self.assertIsNone(archive.testzip())
            names = archive.namelist()
            self.assertIn("project/public/image.png", names)
            self.assertIn("project/production-contract.json", names)
            self.assertFalse(any("node_modules" in n or "/.env" in n or "private.key" in n for n in names))

    def test_declared_excluded_asset_fails(self):
        source = self.root / "public" / "image.png"
        excluded = self.root / "out" / "image.png"
        excluded.parent.mkdir()
        excluded.write_bytes(source.read_bytes())
        self.contract["assets"][0]["path"] = "out/image.png"
        self.contract["scenes"][0]["asset"] = "out/image.png"
        self.write_contract()
        with self.assertRaisesRegex(ValueError, "excluded"):
            package_project(self.root, self.base / "handoff.zip")

    def test_suspicious_private_key_rejected(self):
        (self.root / "notes.txt").write_text("-----BEGIN PRIVATE KEY-----\nexample\n")
        with self.assertRaisesRegex(ValueError, "possible secret"):
            package_project(self.root, self.base / "handoff.zip")


if __name__ == "__main__":
    unittest.main()
