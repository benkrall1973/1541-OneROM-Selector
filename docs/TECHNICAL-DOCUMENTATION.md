# Technical Documentation

## Components

1. A Commodore BASIC V2 selector running on the C64.
2. A 6502 service embedded in the BASIC source and uploaded to 1541 RAM.
3. The universal bootloader in the first non-plugin OneROM multi-chip set.
4. OneROM firmware v0.7.2 with USB and host-control support.

## Operation

The selector polls IEC devices 8-11, uploads the drive service, and probes OneROM first through the upper socket command/back-channel pages. If absent, it patches the service and retries through the lower socket pages. It then uses RBCP v0.1.2 functions to retrieve slot information and configured labels.

The first non-plugin multi-chip set is the universal bootloader. The following one to seven sets are selectable DOS ROMs. Each selectable set must put its single friendly label on `chips[0]`.

## Save/Reboot

The selector writes and verifies the selected slot in OneROM NV storage, prepares the requested ROM, and switches to it. This path is hardware-proven and should not be reordered without new real-hardware testing.

## Q-Quit

Q-Quit obtains the active/back-channel RAM slot with `GET_RAM_SLOT_INFO_ALL`, then calls `LOAD_AND_EXIT` with that RAM slot and the flash slot of the active menu ROM. A returned RAM slot of zero is valid even though BASIC represents its NUL byte as an empty string.

After terminal exit, the C64 waits three seconds, closes the old command channel, sends DOS `I`, clears the screen, and returns to BASIC `READY.`. This sequence preserves normal disk access and repeated selector runs on tested hardware.

## Release files

`src/1541-OneROM-Selector-v1.1.0.bas` is the readable source corresponding to `bin/1541-OneROM-Selector-v1.1.0.PRG`. The root D64 contains that PRG byte-for-byte.

The release bootloader is `firmware/1541-OneROM-Bootloader-Universal-v1.1.0.bin`. Its executable bytes are unchanged from the proven universal v1.0.0 bootloader; the new filename and label identify the v1.1.0 release package.

## Reproducible release build

`scripts/build_release.py` rebuilds the tokenized PRG from the ASCII BASIC
source, reconstructs the single-file D64, and reproduces the universal
bootloader by applying the selector-specific patch to the retained base
bootloader. Every result must match the hardware-tested release byte-for-byte.
See `BUILDING.md` for Windows, Linux, and macOS commands.

The supplied OneROM source snapshot identifies upstream commit
[`ce5ae6b86e16e4d69cdbf8e2f453934267f23f63`](https://github.com/piersfinlayson/one-rom/commit/ce5ae6b86e16e4d69cdbf8e2f453934267f23f63).
