#!/usr/bin/env python3
"""Compare decoded video metadata to a validated production contract.

Requires ffprobe on PATH. Metadata checks do not establish perceptual quality.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
import shutil
import subprocess

from check_project import Report, safe_file, validate_project


def _positive_count(value: object) -> int:
    if isinstance(value, str) and value.isascii() and value.isdigit() and int(value) > 0:
        return int(value)
    if type(value) is int and value > 0:
        return value
    raise ValueError("decoded frame count is missing, invalid, or unavailable")


def verify_render(project_root: str | Path, video_file: str | Path) -> Report:
    report = validate_project(project_root)
    report.warnings.append("Render metadata does not verify visual quality, pronunciation, lip sync, narration content, SFX timing, or factual accuracy; perform perceptual QC.")
    if not report.ok:
        return report
    root = Path(project_root).resolve()
    video = Path(video_file).absolute()
    if not video.is_file() or video.is_symlink():
        report.errors.append("video must be an existing regular local file, not a symlink")
        return report
    ffprobe = shutil.which("ffprobe")
    if not ffprobe:
        report.errors.append("ffprobe is not installed or not available on PATH")
        return report
    command = [
        ffprobe, "-v", "error", "-count_frames", "-show_entries",
        "stream=codec_type,width,height,avg_frame_rate,nb_read_frames,duration:format=duration",
        "-of", "json", str(video),
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=180, check=False)
    except (OSError, subprocess.SubprocessError) as error:
        report.errors.append(f"ffprobe could not run: {error}")
        return report
    if result.returncode != 0:
        report.errors.append(f"ffprobe failed (exit {result.returncode}): {result.stderr.strip()}")
        return report
    try:
        observed = json.loads(result.stdout)
    except (ValueError, TypeError) as error:
        report.errors.append(f"ffprobe returned malformed JSON: {error}")
        return report
    if not isinstance(observed, dict) or not isinstance(observed.get("streams"), list):
        report.errors.append("ffprobe JSON must contain a streams array")
        return report
    streams = observed["streams"]
    if any(not isinstance(stream, dict) for stream in streams):
        report.errors.append("ffprobe streams contain a malformed stream object")
        return report
    videos = [stream for stream in streams if stream.get("codec_type") == "video"]
    audios = [stream for stream in streams if stream.get("codec_type") == "audio"]
    if len(videos) != 1:
        report.errors.append(f"expected exactly 1 video stream, observed {len(videos)}")
        return report
    try:
        project = json.loads(safe_file(root, "production-contract.json").read_text(encoding="utf-8"))["project"]
    except (OSError, ValueError, KeyError) as error:
        report.errors.append(f"could not reread validated contract: {error}")
        return report
    stream = videos[0]
    for dimension in ("width", "height"):
        actual = stream.get(dimension)
        if type(actual) is not int or actual != project[dimension]:
            report.errors.append(f"{dimension}: expected {project[dimension]}, observed {actual!r}")
    try:
        actual_fps = Fraction(str(stream.get("avg_frame_rate", "")))
        if actual_fps != Fraction(project["fps"]):
            report.errors.append(f"fps: expected {project['fps']}, observed {actual_fps}")
    except (ValueError, ZeroDivisionError):
        report.errors.append("video avg_frame_rate is missing or malformed")
    try:
        count = _positive_count(stream.get("nb_read_frames"))
        if count != project["duration_frames"]:
            report.errors.append(f"frame count: expected {project['duration_frames']}, observed {count}")
    except ValueError as error:
        report.errors.append(str(error))
    observed_format = observed.get("format")
    fallback_duration = observed_format.get("duration") if isinstance(observed_format, dict) else None
    raw_duration = stream.get("duration", fallback_duration)
    try:
        duration = Fraction(str(raw_duration))
        expected_duration = Fraction(project["duration_frames"], project["fps"])
        tolerance = Fraction(1, project["fps"])
        if duration <= 0 or abs(duration - expected_duration) > tolerance:
            report.errors.append(f"duration: expected {float(expected_duration):.6f}s within one frame, observed {raw_duration!r}")
    except (ValueError, ZeroDivisionError):
        report.errors.append("video duration is missing or malformed")
    if project["audio_mode"] == "silent" and audios:
        report.errors.append(f"silent contract requires no audio stream; observed {len(audios)}")
    elif project["audio_mode"] in {"voiced", "sound-only"} and not audios:
        report.errors.append(f"{project['audio_mode']} contract requires an audio stream; none observed")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("video", type=Path)
    args = parser.parse_args()
    report = verify_render(args.project, args.video)
    for warning in report.warnings:
        print(f"WARNING: {warning}")
    for error in report.errors:
        print(f"ERROR: {error}")
    print("RENDER METADATA CHECK: " + ("PASS" if report.ok else "FAIL"))
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
