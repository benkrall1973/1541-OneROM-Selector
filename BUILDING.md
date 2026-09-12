# Rebuilding v1.1.0

The production selector, disk image, and universal bootloader can be reproduced
with Python 3. No change is made to the hardware-tested release files.

From the repository root, run:

```text
py -3 scripts/build_release.py
```

On Linux or macOS, use:

```text
python3 scripts/build_release.py
```

The build performs three byte-for-byte checks:

1. Tokenizes `src/1541-OneROM-Selector-v1.1.0.bas` and compares it with the
   released PRG.
2. Replaces the PRG in the released single-file D64 layout and compares the
   result with the released D64.
3. Applies the documented selector-specific patch to the retained original
   bootloader image and compares it with the released universal bootloader.

Successful output ends with `Release reproduction passed.` To retain copies of
the rebuilt artifacts, add `--output-dir build`.

## Bootloader provenance

The bootloader began as the retained original/base OneROM-compatible 1541
bootloader. The selector project modified that image so its boot-time RBCP
setup works with OneROM installed in either the upper or lower 1541 ROM socket.
`scripts/patch_universal_bootloader.py` records that binary modification,
requires the exact base SHA-256, and requires the resulting universal SHA-256.
This makes the distributed universal image reproducible from the retained base
artifact even though the original bootloader assembler source was not present
in the supplied OneROM source archive.

The upstream OneROM firmware and CLI are separate projects and are not rebuilt
by this script. Copyrighted 1541 DOS ROM images are intentionally excluded.
