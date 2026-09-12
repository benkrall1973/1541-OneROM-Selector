# 1541 OneROM Selector v1.1.0

A Commodore 64 BASIC front end and universal Commodore 1541 bootloader for selecting and persistently saving 1541 DOS ROM sets on a OneROM-equipped drive.

## Release status

Version 1.1.0 is the current hardware-tested release. It targets:

- Commodore 1541 with OneROM Fire 24E
- OneROM firmware v0.7.2
- USB and host-control plugins resolved automatically by the current OneROM CLI
- OneROM in either the upper `$E000-$FFFF` or lower `$C000-$DFFF` ROM socket
- IEC drive addresses 8-11

The selector was repeatedly tested from both a physical floppy disk and a PRG mounted with 1541 Ultimate. ROM selection, Save/Reboot, Q-Quit, repeated runs, and post-quit directory access all completed successfully on real hardware.

## What it does

The selector polls IEC devices 8-11, lets the user choose an available drive, searches both 1541 ROM sockets for OneROM, retrieves configured ROM labels, displays the active ROM, saves the selected ROM in OneROM NV storage, verifies the save, and reboots into the selected ROM set.

`Q` exits without changing the saved ROM. The v1.1.0 cleanup path restores normal drive DOS operation and returns the C64 to a clear BASIC `READY.` screen.

## Repository layout

- `1541-OneROM-Selector-v1.1.0.d64` - ready-to-run C64 disk image
- `bin/1541-OneROM-Selector-v1.1.0.PRG` - tokenized C64 program
- `src/1541-OneROM-Selector-v1.1.0.bas` - matching ASCII BASIC source
- `config/` - sanitized upper/lower-socket OneROM configuration examples
- `firmware/` - tested universal 1541 OneROM bootloader binary
- `docs/` - installation, CLI, technical, and release-validation documentation
- `tests/` - retained v1.1.0 development history and hardware-test evidence
- `SHA256SUMS.txt` - SHA-256 checksums for the release files

## Configuration

The public examples contain a stock 1541 ROM example and placeholder filenames for other legally obtained 8 KB upper-ROM images. Commercial ROM images are not included.

Each selectable multi-chip ROM set must have exactly one friendly `label`, located on `chips[0]`. RBCP returns the `chips[0]` label to the selector. Without it, the ROM filename or path is displayed instead.

Use the config matching the physical socket:

- `config/1541-OneROM-Config-Upper-Socket-v1.1.0.example.json`
- `config/1541-OneROM-Config-Lower-Socket-v1.1.0.example.json`

## OneROM programming

Firmware v0.7.2 and the required plugins are installed by the current OneROM CLI. Use named plugin resolution so the CLI obtains the compatible USB and host-control plugins:

```powershell
onerom program --config config/1541-OneROM-Config-Upper-Socket-v1.1.0.example.json --board fire-24-e --plugin usb --plugin host-control
```

Substitute the lower-socket config when appropriate. See `docs/INSTALLATION.md` and `docs/CLI-COMMANDS.md` for the complete workflow.

## Controls

- IEC Select: cursor up/down, RETURN to continue, or `Q` to quit
- ROM Select: cursor up/down, `S` to Save/Reboot, or `Q` to quit

Do not press RUN/STOP while the LOAD screen is communicating with the drive. If communication is interrupted, power-cycle the 1541 before continuing.

## Bootloader

`firmware/1541-OneROM-Bootloader-Universal-v1.1.0.bin` is the tested universal bootloader used by both release configs. It is release-labeled v1.1.0 so it cannot be confused with the earlier package; its executable bytes are unchanged.

`firmware/1541-OneROM-Bootloader-Base-v1.0.0.bin` is retained only as a development reference.

## Licensing

Original project material is released under the MIT License. OneROM and RBCP remain third-party projects with their own notices. See `LICENSE`, `THIRD-PARTY-NOTICES.md`, and `licenses/`.

Verify ROM images, OneROM orientation, socket wiring, and X1 wiring before applying power. This project is provided **AS IS**, without warranty.
