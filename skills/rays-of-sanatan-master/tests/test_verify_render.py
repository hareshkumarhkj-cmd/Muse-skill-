from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import unittest
from unittest.mock import patch

import test_tools
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from verify_render import verify_render


class RenderChecks(unittest.TestCase):
    """Mock ffprobe to test comparison logic, not actual video decoding."""

    def setUp(self):
        test_tools.ProjectChecks.setUp(self)
        self.video = self.base / "render.mp4"
        self.video.write_bytes(b"not a real video; subprocess is mocked")
        self.observed = {"streams": [{"codec_type": "video", "width": 1080, "height": 1920,
                                    "avg_frame_rate": "30/1", "nb_read_frames": "450", "duration": "15.000000"}],
                         "format": {"duration": "15.000000"}}

    tearDown = test_tools.ProjectChecks.tearDown
    write_contract = test_tools.ProjectChecks.write_contract

    def run_probe(self, observed=None, returncode=0, stderr=""):
        payload = self.observed if observed is None else observed
        completed = subprocess.CompletedProcess(args=[], returncode=returncode, stdout=json.dumps(payload), stderr=stderr)
        with patch("verify_render.shutil.which", return_value="/mock/ffprobe"), patch("verify_render.subprocess.run", return_value=completed) as run:
            report = verify_render(self.root, self.video)
        if run.called:
            self.assertIsInstance(run.call_args.args[0], list)
            self.assertFalse(run.call_args.kwargs.get("shell", False))
        return report

    def test_metadata_valid(self):
        self.assertTrue(self.run_probe().ok)

    def test_metadata_wrong_duration(self):
        self.observed["streams"][0]["duration"] = "16"
        self.assertTrue(any("duration:" in e for e in self.run_probe().errors))

    def test_metadata_one_frame_tolerance(self):
        self.observed["streams"][0]["duration"] = "15.03"
        self.assertTrue(self.run_probe().ok)

    def test_metadata_wrong_fps(self):
        self.observed["streams"][0]["avg_frame_rate"] = "30000/1001"
        self.assertTrue(any("fps:" in e for e in self.run_probe().errors))

    def test_metadata_wrong_count(self):
        self.observed["streams"][0]["nb_read_frames"] = "449"
        self.assertTrue(any("frame count:" in e for e in self.run_probe().errors))

    def test_metadata_bad_count(self):
        self.observed["streams"][0]["nb_read_frames"] = "N/A"
        self.assertTrue(any("frame count" in e for e in self.run_probe().errors))

    def test_metadata_extra_audio_in_silent(self):
        self.observed["streams"].append({"codec_type": "audio"})
        self.assertTrue(any("no audio" in e for e in self.run_probe().errors))

    def test_metadata_sound_only_audio_present(self):
        self.contract["project"]["audio_mode"] = "sound-only"
        test_tools.ProjectChecks.add_audio_asset(self)
        self.write_contract()
        self.observed["streams"].append({"codec_type": "audio"})
        self.assertTrue(self.run_probe().ok)

    def test_metadata_sound_only_audio_missing(self):
        self.contract["project"]["audio_mode"] = "sound-only"
        test_tools.ProjectChecks.add_audio_asset(self)
        self.write_contract()
        self.assertTrue(any("sound-only contract requires an audio stream" in e for e in self.run_probe().errors))

    def test_metadata_missing_audio_in_voiced(self):
        audio = self.root / "public" / "voice.wav"
        audio.write_bytes(b"test voice fixture")
        import hashlib
        self.contract["project"]["audio_mode"] = "voiced"
        self.contract["assets"].append({"path": "public/voice.wav", "kind": "audio", "origin": "user-supplied",
                                        "rights_note": "User test fixture", "sha256": hashlib.sha256(audio.read_bytes()).hexdigest()})
        self.contract["narration"] = [{"text": "Test", "start_frame": 0, "end_frame": 90, "audio_file": "public/voice.wav"}]
        self.write_contract()
        self.assertTrue(any("none observed" in e for e in self.run_probe().errors))
        self.observed["streams"].append({"codec_type": "audio"})
        self.assertTrue(self.run_probe().ok)

    def test_metadata_multiple_video_streams(self):
        self.observed["streams"].append(copy.deepcopy(self.observed["streams"][0]))
        self.assertFalse(self.run_probe().ok)

    def test_metadata_missing_video_file(self):
        self.video.unlink()
        self.assertFalse(self.run_probe().ok)

    def test_metadata_missing_ffprobe(self):
        with patch("verify_render.shutil.which", return_value=None):
            self.assertFalse(verify_render(self.root, self.video).ok)

    def test_metadata_ffprobe_error(self):
        self.assertTrue(any("exit 1" in e for e in self.run_probe(returncode=1, stderr="decode error").errors))

    def test_metadata_ffprobe_malformed_json(self):
        completed = subprocess.CompletedProcess(args=[], returncode=0, stdout="not JSON", stderr="")
        with patch("verify_render.shutil.which", return_value="/mock/ffprobe"), patch("verify_render.subprocess.run", return_value=completed):
            self.assertFalse(verify_render(self.root, self.video).ok)

    def test_metadata_malformed_rate(self):
        self.observed["streams"][0]["avg_frame_rate"] = "0/0"
        self.assertFalse(self.run_probe().ok)

    def test_metadata_wrong_dimensions(self):
        self.observed["streams"][0]["width"] = 720
        self.assertTrue(any("width:" in e for e in self.run_probe().errors))

    def test_metadata_invalid_root_json(self):
        self.assertFalse(self.run_probe(observed=[]).ok)


if __name__ == "__main__":
    import unittest
    unittest.main()
