# 1541 OneROM Selector v1.0.0

A Commodore 64 BASIC front end and universal Commodore 1541 bootloader for selecting and persistently saving 1541 DOS ROM sets on a OneROM-equipped drive.

## Release status

This repository is the clean public **v1.0.0** baseline.

Tested project baseline:

- Commodore 1541 with OneROM Fire 24E
- OneROM firmware v0.7.1
- USB plugin v0.2.1
- host-control plugin v0.1.2
- Universal bootloader v1.0.0
- Selector v1.0.0
- OneROM installed in either the upper `$E000-$FFFF` or lower `$C000-$DFFF` ROM socket
- Selector supports IEC drive addresses 8-11

The included D64 has been filesystem-checked and the exact included PRG has been successfully loaded and run in **VICE 3.9** using `x64sc.exe` (64-bit) on Windows 10.

## What it does

The selector polls IEC devices 8-11, lets the user choose an available drive, searches for OneROM in either physical ROM socket, reads compiled ROM labels and saved custom names, shows the active/selected ROM, allows names to be edited or restored, saves the selected ROM in OneROM NV storage, verifies the save, and switches the drive to the selected ROM set.

The universal bootloader reads the saved selection at drive startup and boots the selected DOS ROM after a power cycle.

## Repository layout

- `1541-OneROM-Selector-v1.0.0.d64` - ready-to-run C64 disk image
- `bin/` - tokenized C64 PRG
- `src/` - ASCII BASIC source corresponding to the release PRG
- `config/` - sanitized upper/lower-socket OneROM configuration examples
- `firmware/` - tested universal 1541 OneROM bootloader binary
- `plugins/` - exact OneROM plugin binaries used by the tested baseline
- `docs/` - installation, CLI, technical, current-state, and release-validation documentation
- `LICENSE` - MIT license for this project's original material
- `licenses/` and `THIRD-PARTY-NOTICES.md` - third-party licensing and attribution
- `SHA256SUMS.txt` - release-file checksums

## Configuration examples

The public configs are intentionally sanitized. They contain a stock 1541 ROM example plus placeholder upper-ROM filenames for the remaining selectable slots. Replace the placeholders with legally obtained 8 KB upper-ROM images.

Both examples use the current `chip_sets` / `chips` naming. OneROM has retained backward compatibility with the older `rom_sets` / `roms` names, but the current names also validate against the current schema.

For this selector, each selectable ROM set **must have exactly one `label`** if a clean human-readable ROM name is desired. The selector reads OneROM metadata for the display name; without a `label`, OneROM supplies the ROM filename/path instead, so the selector will display that path rather than the intended friendly name.

The `label` belongs to the **upper `$E000-$FFFF` ROM object** in every selectable set, even when OneROM is physically installed in the lower socket. In the supplied examples it is intentionally the **last member** of that upper-ROM object. This last-member placement is a tested project convention, not a JSON-schema requirement.

Commercial ROM images are not included.

## OneROM CLI quick start

New users should start with the OneROM CLI itself:

```powershell
onerom --version
onerom scan
onerom inspect info
onerom scan --slots
```

`onerom scan` reports the connected OneROM serial number and board information. `onerom inspect info` provides the device identity and firmware details, and `onerom scan --slots` shows the ROM slots. When more than one OneROM is connected, use `--serial "YOUR_SERIAL_NUMBER"` to select the intended device. The official OneROM CLI documents these as the standard discovery and inspection commands.

See `docs/CLI-COMMANDS.md` for the complete beginner workflow and the exact programming commands for this release.

## OneROM programming

See `docs/INSTALLATION.md` and `docs/CLI-COMMANDS.md`.

**Important:** the OneROM configuration JSON files do not install the plugins by themselves. To get the USB and host-control plugins installed into the OneROM firmware, use the OneROM CLI `program` command with the configuration JSON and both plugin binaries supplied on the command line. The CLI compiles the configuration and downloads the resulting firmware to the OneROM as part of that programming operation.

Do not treat the JSON files as standalone firmware images, and do not program a separately built firmware image that was created without the required plugin arguments. If the plugins are omitted from the CLI programming command, the selector's RBCP/host-control functions will not have the required plugin firmware installed.

The commands in this repository use the included plugin binaries by file path so the tested USB v0.2.1 and host-control v0.1.2 versions are reproducible. Users may instead use OneROM's named plugin resolution if they deliberately want newer compatible plugin versions, but the bundled file-based commands are the authoritative v1.0.0 path.

## Safety

Once the selector begins RBCP communication with the drive, use **SAVE** as the normal completion path. Unexpectedly ending the program can leave the 1541 requiring a power cycle. The program displays this warning before communication starts.

Verify ROM images, OneROM orientation, socket wiring, and X1 wiring before applying power. This project is provided **AS IS**, without warranty. Use it at your own risk.

## Licensing

Original 1541 OneROM Selector material is released under the MIT License. See `LICENSE`.

OneROM and RBCP remain third-party projects with their own notices. See `THIRD-PARTY-NOTICES.md` and `licenses/`.

## Release notes

See `CHANGELOG.md`. Mechanical release checks are recorded in `docs/RELEASE-VALIDATION.md`.


## Bootloader binaries

- `firmware/1541-OneROM-Bootloader-Universal-v1.0.0.bin` is the tested universal bootloader used by the release configs.
- `firmware/1541-OneROM-Bootloader-Base-v1.0.0.bin` is the verified original/base bootloader binary retained as a development reference. It is not the recommended release bootloader.
