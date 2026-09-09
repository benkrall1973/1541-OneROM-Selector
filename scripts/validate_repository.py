#!/usr/bin/env python3
"""Mechanical checks for 1541 OneROM Selector development branches."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEST_RE = re.compile(r"^T1\.1\.0-\d{2}$")
errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def validate_configs() -> None:
    for path in sorted((ROOT / "config").glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue

        sets = data.get("chip_sets")
        if not isinstance(sets, list):
            fail(f"{path.relative_to(ROOT)}: chip_sets must be a list")
            continue

        for index, chip_set in enumerate(sets):
            if chip_set.get("type") != "multi":
                continue
            chips = chip_set.get("chips")
            if not isinstance(chips, list) or not chips:
                fail(f"{path.relative_to(ROOT)}: chip_sets[{index}] has no chips")
                continue
            locations = [i for i, chip in enumerate(chips) if "label" in chip]
            if locations != [0]:
                fail(
                    f"{path.relative_to(ROOT)}: chip_sets[{index}] must have "
                    f"exactly one label on chips[0], found {locations}"
                )


def parse_checksums(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", line)
        if not match:
            fail(f"{path.relative_to(ROOT)}:{number}: invalid checksum line")
            continue
        entries[match.group(2)] = match.group(1).lower()
    return entries


def validate_test_bundles() -> None:
    tests = ROOT / "tests"
    if not tests.is_dir():
        fail("tests directory is missing")
        return

    for directory in sorted(p for p in tests.iterdir() if p.is_dir()):
        version = directory.name
        if not TEST_RE.fullmatch(version):
            fail(f"tests/{version}: expected a unique T1.1.0-XX directory name")
            continue

        required_dirs = [directory / "source", directory / "bin", directory / "disk"]
        for required in required_dirs:
            if not required.is_dir():
                fail(f"{required.relative_to(ROOT)}: required directory is missing")

        readme = directory / "README.md"
        sums = directory / "SHA256SUMS.txt"
        if not readme.is_file():
            fail(f"tests/{version}/README.md is missing")
        elif version not in readme.read_text(encoding="utf-8", errors="replace"):
            fail(f"tests/{version}/README.md does not name {version}")
        if not sums.is_file():
            fail(f"tests/{version}/SHA256SUMS.txt is missing")
            continue

        bas = list((directory / "source").glob("*.bas")) if required_dirs[0].is_dir() else []
        prg = list((directory / "bin").glob("*.PRG")) if required_dirs[1].is_dir() else []
        d64 = list((directory / "disk").glob("*.d64")) if required_dirs[2].is_dir() else []
        for kind, found in (("BASIC source", bas), ("PRG", prg), ("D64", d64)):
            if len(found) != 1:
                fail(f"tests/{version}: expected exactly one {kind}, found {len(found)}")
            for path in found:
                if version not in path.name:
                    fail(f"{path.relative_to(ROOT)}: filename must contain {version}")

        entries = parse_checksums(sums)
        for relative, expected in entries.items():
            target = directory / relative
            if not target.is_file():
                fail(f"tests/{version}: checksum target is missing: {relative}")
                continue
            actual = hashlib.sha256(target.read_bytes()).hexdigest()
            if actual != expected:
                fail(f"tests/{version}: checksum mismatch: {relative}")

        expected_files = bas + prg + d64
        for target in expected_files:
            relative = target.relative_to(directory).as_posix()
            if relative not in entries:
                fail(f"tests/{version}: checksum missing for {relative}")


def validate_private_rom_guard() -> None:
    allowed = {
        "1541-OneROM-Bootloader-Universal-v1.0.0.bin",
        "1541-OneROM-Bootloader-Base-v1.0.0.bin",
    }
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        lower = path.name.lower()
        if path.suffix.lower() in {".rom"}:
            fail(f"{path.relative_to(ROOT)}: ROM files must not be committed")
        if path.suffix.lower() == ".bin" and path.name not in allowed:
            if "plugins" not in path.parts:
                fail(f"{path.relative_to(ROOT)}: unapproved BIN file")


def main() -> int:
    validate_configs()
    validate_test_bundles()
    validate_private_rom_guard()
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
