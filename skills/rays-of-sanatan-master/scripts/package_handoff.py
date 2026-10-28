#!/usr/bin/env python3
"""Package a validated project without dependencies, outputs or obvious secret files.

This is a bounded precaution, not a guarantee that every secret can be detected.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import tempfile
import zipfile

from check_project import safe_file, validate_project


EXCLUDED_PARTS = {
    "node_modules", ".git", "out", "dist", "build", "coverage", ".cache",
    "__pycache__", ".venv", "venv", ".next", ".turbo", ".DS_Store",
}
REQUIRED = (
    "TASK.md", "README.txt", "TEST-NOTE.txt", "package.json", "package-lock.json",
    "remotion.config.ts", "src/index.ts", "production-contract.json",
)
SECRET_NAME = re.compile(r"(?:^\.env(?:\..*)?$|\.(?:pem|key|p12|pfx|keystore)$|^(?:id_rsa|id_ed25519|credentials(?:\.json)?|service-account(?:\.json)?)$)", re.IGNORECASE)
SECRET_CONTENT = re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\b(?:sk-[A-Za-z0-9_-]{24,}|AIza[A-Za-z0-9_-]{30,})\b")
TEXT_SUFFIXES = {".md", ".txt", ".log", ".json", ".ts", ".tsx", ".js", ".jsx", ".py", ".yaml", ".yml", ".toml", ".css", ".html", ".sh"}


def excluded(path: Path) -> bool:
    return any(part.lower() in {name.lower() for name in EXCLUDED_PARTS} or part.lower().startswith(".env") for part in path.parts) or bool(SECRET_NAME.search(path.name))


def package_project(project_root: str | Path, output_zip: str | Path) -> tuple[int, list[str]]:
    original = Path(project_root).absolute()
    if original.is_symlink():
        raise ValueError("project root must not be a symlink")
    root = original.resolve()
    requested_output = Path(output_zip).absolute()
    if requested_output.is_symlink():
        raise ValueError("output archive must not be a symlink")
    output = requested_output.resolve()
    if output.is_relative_to(root):
        raise ValueError("output archive must be outside the project directory")
    report = validate_project(root)
    if not report.ok:
        raise ValueError("contract validation failed:\n" + "\n".join(report.errors))
    for path in REQUIRED:
        safe_file(root, path)

    files: list[Path] = []
    skipped: list[str] = []
    for directory, folders, names in os.walk(root, followlinks=False):
        current = Path(directory)
        retained = []
        for name in sorted(folders):
            child = current / name
            relative = child.relative_to(root)
            if excluded(relative):
                skipped.append(relative.as_posix() + "/")
            elif child.is_symlink():
                raise ValueError(f"symlink not allowed in handoff: {relative}")
            else:
                retained.append(name)
        folders[:] = retained
        for name in sorted(names):
            path = current / name
            relative = path.relative_to(root)
            if excluded(relative):
                skipped.append(relative.as_posix())
                continue
            if path.is_symlink():
                raise ValueError(f"symlink not allowed in handoff: {relative}")
            if not path.is_file():
                raise ValueError(f"non-regular file in handoff: {relative}")
            if path.suffix.lower() == ".zip":
                raise ValueError(f"nested ZIP requires explicit inspection; remove it from project: {relative}")
            if path.suffix.lower() in TEXT_SUFFIXES and SECRET_CONTENT.search(path.read_bytes()):
                raise ValueError(f"possible secret detected in {relative}; inspect privately before packaging")
            files.append(path)
    # A contract must never reference a file silently omitted by the package rules.
    import json
    document = json.loads((root / "production-contract.json").read_text(encoding="utf-8"))
    for asset in document["assets"]:
        if excluded(Path(asset["path"])):
            raise ValueError(f"declared asset would be excluded from archive: {asset['path']}")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(prefix=".handoff-", suffix=".zip", dir=output.parent, delete=False) as temporary:
            temporary_path = Path(temporary.name)
        with zipfile.ZipFile(temporary_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(files):
                archive.write(path, (Path(root.name) / path.relative_to(root)).as_posix())
        with zipfile.ZipFile(temporary_path) as archive:
            bad_file = archive.testzip()
            if bad_file:
                raise ValueError(f"archive integrity failed: {bad_file}")
            if len(archive.namelist()) != len(set(archive.namelist())):
                raise ValueError("duplicate archive entry")
            for name in archive.namelist():
                parts = name.split("/")
                if name.startswith("/") or ".." in parts or "\\" in name:
                    raise ValueError("unsafe archive member")
        os.replace(temporary_path, output)
        temporary_path = None
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
    return len(files), skipped


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        count, skipped = package_project(args.project, args.output)
    except (ValueError, OSError, zipfile.BadZipFile) as error:
        print(f"PACKAGE FAILED: {error}")
        return 1
    print(f"PACKAGED: {count} files -> {args.output}")
    if skipped:
        print("Excluded: " + ", ".join(skipped))
    print("Integrity checked. This does not certify a render or detect every secret.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
