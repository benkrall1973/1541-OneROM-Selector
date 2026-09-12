#!/usr/bin/env python3
"""Reproduce the tested universal bootloader from the retained base image."""

from pathlib import Path
import argparse
import hashlib


BASE_SHA256 = "b89951c4883c559f7aa6b6639a890a8e76a10f67685f2124a2a0e7eebbe87152"
UNIVERSAL_SHA256 = "7313b07f26fcc3778664b0c53f1aff46af883ed8b0a3cbf525efc9bb40432b0e"
PATCH_OFFSET = 1056
PATCH_BYTES = bytes.fromhex(
    "ad0504c9c0f0034c1407a9e08d05048d08048d0b048d0e048d11048d14048d1f04"
    "8d27048d3704a9e18d3f048d47048d57048d6c048d7d048dbd058d44068d57068d"
    "f5064cd206"
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def patch(base: bytes) -> bytes:
    if digest(base) != BASE_SHA256:
        raise ValueError("base bootloader checksum does not match the proven image")
    result = bytearray(base)
    result[985] = 0x46
    result[PATCH_OFFSET:PATCH_OFFSET + len(PATCH_BYTES)] = PATCH_BYTES
    if digest(result) != UNIVERSAL_SHA256:
        raise ValueError("patched universal bootloader checksum mismatch")
    return bytes(result)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(patch(args.base.read_bytes()))


if __name__ == "__main__":
    main()
