#!/usr/bin/env python3
"""Validate a local production contract; this does not execute or certify a render."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
from urllib.parse import urlparse


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def safe_file(root: Path, value: object) -> Path:
    """Require a normalized relative POSIX file path without symlink components."""
    if not isinstance(value, str) or not value or "\\" in value or ":" in value:
        raise ValueError("asset paths must be nonempty relative POSIX paths")
    pure = PurePosixPath(value)
    if pure.is_absolute() or value != pure.as_posix() or any(p in {".", ".."} for p in value.split("/")):
        raise ValueError(f"unsafe or unnormalized path: {value!r}")
    current = root
    for part in pure.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"symlink not allowed: {value!r}")
    resolved = current.resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError(f"path escapes project: {value!r}")
    if not current.is_file():
        raise ValueError(f"missing local file: {value!r}")
    return current


def _positive_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _list(document: dict, key: str, report: Report) -> list:
    value = document.get(key)
    if not isinstance(value, list):
        report.errors.append(f"{key} must be an array")
        return []
    return value


def _text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _choice(value: object, allowed: set[str]) -> bool:
    return isinstance(value, str) and value in allowed


def validate_project(project_root: str | Path) -> Report:
    report = Report()
    original = Path(project_root).absolute()
    if original.is_symlink():
        report.errors.append("project root must not be a symlink")
        return report
    root = original.resolve()
    if not root.is_dir():
        report.errors.append("project root is not a directory")
        return report
    try:
        contract = safe_file(root, "production-contract.json")
        document = json.loads(contract.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        report.errors.append(f"cannot read production-contract.json: {error}")
        return report
    if not isinstance(document, dict):
        report.errors.append("contract must be a JSON object")
        return report
    if type(document.get("schema_version")) is not int or document["schema_version"] != 1:
        report.errors.append("schema_version must be integer 1")
    project = document.get("project")
    if not isinstance(project, dict):
        report.errors.append("project must be an object")
        project = {}
    if not isinstance(project.get("composition_id"), str) or not re.fullmatch(r"[A-Za-z0-9-]+", project["composition_id"]):
        report.errors.append("composition_id must contain only ASCII letters, digits and hyphens")
    for name in ("width", "height", "fps", "duration_frames"):
        if not _positive_int(project.get(name)):
            report.errors.append(f"project.{name} must be a positive integer")
    duration = project.get("duration_frames") if _positive_int(project.get("duration_frames")) else 0
    for key, allowed in {
        "stage": {"visual-proof", "production"},
        "motion_mode": {"still-motion", "mixed", "full-motion"},
        "audio_mode": {"silent", "voiced", "sound-only"},
    }.items():
        if not _choice(project.get(key), allowed):
            report.errors.append(f"project.{key} must be one of {sorted(allowed)}")

    assets: dict[str, dict] = {}
    for number, asset in enumerate(_list(document, "assets", report)):
        prefix = f"assets[{number}]"
        if not isinstance(asset, dict):
            report.errors.append(f"{prefix} must be an object")
            continue
        path = asset.get("path")
        if isinstance(path, str):
            if path in assets:
                report.errors.append(f"duplicate asset path: {path}")
            assets[path] = asset
        if not _choice(asset.get("kind"), {"image", "video", "audio", "font"}):
            report.errors.append(f"{prefix}.kind is invalid")
        if not _choice(asset.get("origin"), {"generated-original", "user-supplied", "open-license", "code-generated"}):
            report.errors.append(f"{prefix}.origin is invalid")
        if not _text(asset.get("rights_note")):
            report.errors.append(f"{prefix}.rights_note is required")
        digest = asset.get("sha256")
        valid_hash = isinstance(digest, str) and re.fullmatch(r"[a-fA-F0-9]{64}", digest)
        if not valid_hash:
            report.errors.append(f"{prefix}.sha256 must contain 64 hexadecimal characters")
        try:
            local = safe_file(root, path)
            if valid_hash and hashlib.sha256(local.read_bytes()).hexdigest().lower() != digest.lower():
                report.errors.append(f"{prefix} SHA-256 mismatch: {path}")
        except (OSError, ValueError) as error:
            report.errors.append(f"{prefix}: {error}")

    scenes = _list(document, "scenes", report)
    if not scenes:
        report.errors.append("at least one scene is required")
    previous_end = 0
    scene_ids: set[str] = set()
    for number, scene in enumerate(scenes):
        prefix = f"scenes[{number}]"
        if not isinstance(scene, dict):
            report.errors.append(f"{prefix} must be an object")
            continue
        scene_id = scene.get("id")
        if not _text(scene_id):
            report.errors.append(f"{prefix}.id is required")
        elif scene_id in scene_ids:
            report.errors.append(f"duplicate scene id: {scene_id}")
        else:
            scene_ids.add(scene_id)
        start, end = scene.get("start_frame"), scene.get("end_frame")
        valid_interval = type(start) is int and type(end) is int and 0 <= start < end <= duration
        if not valid_interval:
            report.errors.append(f"{prefix} must have 0 <= start_frame < end_frame <= duration_frames")
        else:
            if start != previous_end:
                report.errors.append(f"{prefix} timing gap/overlap: expected start {previous_end}, got {start}")
            previous_end = end
        if not isinstance(scene.get("caption"), str):
            report.errors.append(f"{prefix}.caption must be a string (empty is allowed)")
        visual, path = scene.get("visual_type"), scene.get("asset")
        if not _choice(visual, {"still", "video", "code"}):
            report.errors.append(f"{prefix}.visual_type is invalid")
        elif visual == "code":
            if path is not None:
                report.errors.append(f"{prefix}: code visuals require asset: null")
        elif not isinstance(path, str) or path not in assets:
            report.errors.append(f"{prefix}: visual asset must be declared in assets")
        elif assets[path].get("kind") != {"still": "image", "video": "video"}[visual]:
            report.errors.append(f"{prefix}: visual asset kind does not match visual_type")
    if previous_end != duration:
        report.errors.append(f"scene timeline ends at {previous_end}, expected {duration}")

    narration = _list(document, "narration", report)
    mode = project.get("audio_mode")
    if mode == "silent" and narration:
        report.errors.append("silent audio_mode requires empty narration")
    if mode == "voiced" and not narration:
        report.errors.append("voiced audio_mode requires narration entries with real audio assets")
    if mode == "sound-only":
        if narration:
            report.errors.append("sound-only audio_mode requires empty narration")
        if not any(asset.get("kind") == "audio" for asset in assets.values()):
            report.errors.append("sound-only audio_mode requires at least one declared local audio asset")
    previous_voice_end = 0
    for number, line in enumerate(narration):
        prefix = f"narration[{number}]"
        if not isinstance(line, dict):
            report.errors.append(f"{prefix} must be an object")
            continue
        if not _text(line.get("text")):
            report.errors.append(f"{prefix}.text is required")
        start, end = line.get("start_frame"), line.get("end_frame")
        if not (type(start) is int and type(end) is int and 0 <= start < end <= duration):
            report.errors.append(f"{prefix}: invalid narration interval")
        elif start < previous_voice_end:
            report.errors.append(f"{prefix}: narration overlaps a prior narration entry")
        else:
            previous_voice_end = end
        path = line.get("audio_file")
        if not isinstance(path, str) or assets.get(path, {}).get("kind") != "audio":
            report.errors.append(f"{prefix}.audio_file must reference a declared local audio asset")

    for number, claim in enumerate(_list(document, "claims", report)):
        prefix = f"claims[{number}]"
        if not isinstance(claim, dict):
            report.errors.append(f"{prefix} must be an object")
            continue
        if not _text(claim.get("id")) or not _text(claim.get("sentence")):
            report.errors.append(f"{prefix}: id and sentence are required")
        classification = claim.get("classification")
        if not _choice(classification, {"verified", "tradition", "fiction", "unverified"}):
            report.errors.append(f"{prefix}.classification is invalid")
        if classification == "unverified":
            report.warnings.append(f"{prefix}: unverified claim requires removal or explicit qualification before publication")
        sources = claim.get("sources")
        if not isinstance(sources, list):
            report.errors.append(f"{prefix}.sources must be an array")
            continue
        if classification == "verified" and not sources:
            report.errors.append(f"{prefix}: verified claims require sources")
        for source_number, source in enumerate(sources):
            tag = f"{prefix}.sources[{source_number}]"
            if not isinstance(source, dict):
                report.errors.append(f"{tag} must be an object")
                continue
            url = source.get("url")
            try:
                parsed = urlparse(url) if isinstance(url, str) else None
                valid_url = bool(parsed and parsed.scheme == "https" and parsed.hostname and not parsed.username and not parsed.password)
            except ValueError:
                valid_url = False
            if not valid_url:
                report.errors.append(f"{tag}.url must be a credential-free HTTPS URL")
            for name in ("title", "retrieved_date", "notes"):
                if not _text(source.get(name)):
                    report.errors.append(f"{tag}.{name} is required")
    report.warnings.append("Static checks do not prove render success, source truth, rights ownership, audio quality, or absence of all secrets; complete runtime and human QC.")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    args = parser.parse_args()
    report = validate_project(args.project)
    for warning in report.warnings:
        print(f"WARNING: {warning}")
    for error in report.errors:
        print(f"ERROR: {error}")
    print("STATIC CONTRACT CHECK: " + ("PASS" if report.ok else "FAIL"))
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
