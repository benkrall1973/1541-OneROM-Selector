#!/usr/bin/env python3
"""Rebuild and byte-verify the released selector artifacts."""

from pathlib import Path
import argparse
import hashlib
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
VERSION = "v1.1.0"
SOURCE = ROOT / "src" / f"1541-OneROM-Selector-{VERSION}.bas"
PRG = ROOT / "bin" / f"1541-OneROM-Selector-{VERSION}.PRG"
D64 = ROOT / f"1541-OneROM-Selector-{VERSION}.d64"
BASE_BOOT = ROOT / "firmware" / "1541-OneROM-Bootloader-Base-v1.0.0.bin"
UNIVERSAL_BOOT = ROOT / "firmware" / f"1541-OneROM-Bootloader-Universal-{VERSION}.bin"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_identical(rebuilt: Path, released: Path) -> None:
    if rebuilt.read_bytes() != released.read_bytes():
        raise SystemExit(
            f"MISMATCH: {rebuilt.name} does not reproduce {released.relative_to(ROOT)}"
        )
    print(f"MATCH {released.relative_to(ROOT)}  {sha256(released)}")


def run(*args: str) -> None:
    subprocess.run([sys.executable, *args], check=True, cwd=ROOT)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir", type=Path,
        help="also copy verified rebuilt artifacts to this directory",
    )
    args = parser.parse_args()

    with tempfile.TemporaryDirectory(prefix="onerom-selector-build-") as temporary:
        temp = Path(temporary)
        rebuilt_prg = temp / PRG.name
        rebuilt_d64 = temp / D64.name
        rebuilt_boot = temp / UNIVERSAL_BOOT.name

        run("scripts/tokenize_basic_v2.py", str(SOURCE), str(rebuilt_prg))
        require_identical(rebuilt_prg, PRG)

        run(
            "scripts/update_single_prg_d64.py", str(D64), str(rebuilt_prg),
            str(rebuilt_d64), "--file-name", "ONEROMV110",
            "--disk-name", "ONEROM V1.1.0",
        )
        require_identical(rebuilt_d64, D64)

        run("scripts/patch_universal_bootloader.py", str(BASE_BOOT), str(rebuilt_boot))
        require_identical(rebuilt_boot, UNIVERSAL_BOOT)

        if args.output_dir:
            args.output_dir.mkdir(parents=True, exist_ok=True)
            for source in (rebuilt_prg, rebuilt_d64, rebuilt_boot):
                (args.output_dir / source.name).write_bytes(source.read_bytes())

    print("Release reproduction passed.")


if __name__ == "__main__":
    main()
