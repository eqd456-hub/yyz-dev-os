#!/usr/bin/env python3
"""Build or verify the generated YYZ Dev OS plugin Skill snapshot."""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "yyz-dev-os"
SNAPSHOT_ROOT = PLUGIN_ROOT / "skills" / "yyz-dev-os"
PUBLISHED_FILES = (
    "SKILL.md",
    "VERSION",
    "CHANGELOG.md",
    "README.md",
    ".gitignore",
    ".gitattributes",
)
PUBLISHED_DIRECTORIES = ("agents", "references", "assets", "scripts", "tests")


def is_publishable(path: Path) -> bool:
    return "__pycache__" not in path.parts and path.suffix not in {".pyc", ".pyo"}


def source_files() -> dict[Path, Path]:
    files: dict[Path, Path] = {}
    for relative in PUBLISHED_FILES:
        source = ROOT / relative
        if not source.is_file():
            raise RuntimeError(f"Missing published file: {relative}")
        files[Path(relative)] = source
    for directory in PUBLISHED_DIRECTORIES:
        source_directory = ROOT / directory
        if not source_directory.is_dir():
            raise RuntimeError(f"Missing published directory: {directory}")
        for source in sorted(
            path
            for path in source_directory.rglob("*")
            if path.is_file() and is_publishable(path.relative_to(ROOT))
        ):
            files[source.relative_to(ROOT)] = source
    return files


def validate_snapshot_target() -> None:
    expected_plugin_root = ROOT / "plugins" / "yyz-dev-os"
    expected_snapshot_root = expected_plugin_root / "skills" / "yyz-dev-os"
    if PLUGIN_ROOT != expected_plugin_root or SNAPSHOT_ROOT != expected_snapshot_root:
        raise RuntimeError("Snapshot target is not the expected plugin Skill path")
    if not SNAPSHOT_ROOT.resolve().is_relative_to(ROOT.resolve()):
        raise RuntimeError("Snapshot target escapes the plugin root")
    if SNAPSHOT_ROOT.is_symlink():
        raise RuntimeError("Snapshot target must not be a symbolic link")


def snapshot_files() -> dict[Path, Path]:
    if not SNAPSHOT_ROOT.is_dir():
        return {}
    return {
        path.relative_to(SNAPSHOT_ROOT): path
        for path in SNAPSHOT_ROOT.rglob("*")
        if path.is_file() and is_publishable(path.relative_to(SNAPSHOT_ROOT))
    }


def check_snapshot() -> list[str]:
    expected = source_files()
    actual = snapshot_files()
    failures: list[str] = []
    for relative, source in expected.items():
        target = actual.get(relative)
        if target is None:
            failures.append(f"Missing plugin snapshot file: {relative}")
        elif not filecmp.cmp(source, target, shallow=False):
            failures.append(f"Plugin snapshot differs: {relative}")
    for relative in sorted(set(actual) - set(expected)):
        failures.append(f"Unexpected plugin snapshot file: {relative}")
    return failures


def build_snapshot() -> None:
    validate_snapshot_target()
    expected = source_files()
    if SNAPSHOT_ROOT.exists():
        shutil.rmtree(SNAPSHOT_ROOT)
    for relative, source in expected.items():
        target = SNAPSHOT_ROOT / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail when snapshot differs")
    args = parser.parse_args()
    try:
        if args.check:
            failures = check_snapshot()
            if failures:
                print("YYZ plugin snapshot check FAILED")
                for failure in failures:
                    print(f"- {failure}")
                return 1
            print("YYZ plugin snapshot check PASSED")
            return 0
        build_snapshot()
        failures = check_snapshot()
        if failures:
            print("YYZ plugin snapshot build FAILED")
            for failure in failures:
                print(f"- {failure}")
            return 1
        print(f"YYZ plugin snapshot built: {SNAPSHOT_ROOT.relative_to(ROOT)}")
        return 0
    except (OSError, RuntimeError) as exc:
        print(f"YYZ plugin snapshot failed: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
