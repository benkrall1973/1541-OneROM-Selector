# Current State Summary — v1.0.0

## Working behavior

The project has been developed and tested on a real Commodore 1541 with OneROM Fire 24E and OneROM firmware v0.7.1. Universal upper/lower socket operation, ROM switching, label handling, NV persistence, and normal disk operation have all been exercised during development.

The final release D64 included here has also been checked structurally, and its embedded PRG is byte-for-byte identical to `bin/1541-OneROM-Selector-v1.0.0.PRG`. That exact D64/PRG has been successfully loaded and run in **VICE 3.9** using `x64sc.exe` (64-bit) on Windows 10.

## Current selector flow

1. Poll IEC devices 8-11.
2. Let the user choose an available drive; a countdown accepts the current selection automatically.
3. Display the pre-initialization warning and allow `Q` to exit before RBCP starts.
4. Search the upper OneROM socket interface first.
5. If needed, patch the uploaded helper and retry the lower socket interface.
6. Read the saved selection, compiled labels, and custom-name records.
7. Display the discovered ROM names and then open the menu.
8. Allow selection, edit, restore, and SAVE operations.
9. On SAVE, write and verify modified names and the selected slot, then switch ROM sets.

## Release artifacts

- `1541-OneROM-Selector-v1.0.0.d64`
- `bin/1541-OneROM-Selector-v1.0.0.PRG`
- `src/1541-OneROM-Selector-v1.0.0.bas`
- `firmware/1541-OneROM-Bootloader-Universal-v1.0.0.bin`
- Upper- and lower-socket sanitized OneROM configuration examples
- USB v0.2.1 and host-control v0.1.2 plugin binaries
- Documentation and third-party license notices

## Known operating constraint

Once RBCP communication has begun, SAVE is the supported normal completion path. There is no supported quit-without-saving cleanup path after initialization. If the program is unexpectedly terminated and the drive is left in a bad state, power-cycle the 1541.

## Maintenance rules

- Keep exactly one label attached to the upper `$E000-$FFFF` ROM in each selectable set. The selector uses it as the friendly ROM display name; without it, the ROM filename/path is shown instead.
- Preserve physical chip ordering in the upper/lower socket configs.
- Keep the universal bootloader as the first non-plugin set.
- Do not modify SAVE/NV verification/final switching behavior without hardware testing.
- Do not distribute commercial ROM images without permission.
- Recalculate `SHA256SUMS.txt` after any release-file change.
