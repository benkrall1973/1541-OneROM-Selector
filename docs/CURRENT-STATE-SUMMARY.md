# Current State Summary — v1.1.0 Development

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

## Current development focus

The stable v1.0.0 program has no supported quit-without-saving cleanup path after initialization. v1.1.0 development is adding a true idle-menu cancel that cleans up communication without writing NV records or switching ROMs. This path remains experimental until hardware testing is complete.

The OneROM author successfully tested the current selector on a real 1541 with in-development v0.7.2, OneROM in the lower socket, at device 8. One SAVE on device 9 appeared to hang once, then succeeded on the next identical attempt. Repeated device-9 testing is required.

## Maintenance rules

- Keep exactly one label attached to `chips[0]` in each selectable set. RBCP returns the `chips[0]` label as the friendly ROM display name; without it, the ROM filename/path is shown instead.
- Preserve physical chip ordering in the upper/lower socket configs.
- Keep the universal bootloader as the first non-plugin set.
- Do not modify SAVE/NV verification/final switching behavior without hardware testing.
- Do not expose idle-menu cancel during an active RBCP/DOS transaction.
- Do not distribute commercial ROM images without permission.
- Give every test build a unique temporary version and keep its exact source.
- Recalculate `SHA256SUMS.txt` when preparing a release candidate.
