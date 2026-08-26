# Installation

## Requirements

- Commodore 64 or compatible environment capable of running the selector PRG
- Commodore 1541 drive for real-hardware use
- OneROM Fire 24E
- OneROM firmware v0.7.1 for the tested baseline
- USB plugin v0.2.1
- host-control plugin v0.1.2
- Universal bootloader from `firmware/`
- One to seven selectable 1541 DOS ROM sets
- Legally obtained ROM images

## Choose the OneROM socket

### Upper ROM socket

- Install OneROM in the upper `$E000-$FFFF` ROM socket.
- Remove the lower ROM.
- Connect X1 to pin 20 of the empty lower `$C000-$DFFF` socket.
- Use `config/1541-OneROM-Config-Upper-Socket-v1.0.0.example.json`.

### Lower ROM socket

- Install OneROM in the lower `$C000-$DFFF` ROM socket.
- Remove the upper ROM.
- Connect X1 to pin 20 of the empty upper `$E000-$FFFF` socket.
- Use `config/1541-OneROM-Config-Lower-Socket-v1.0.0.example.json`.

Verify orientation, socket condition, and wiring before applying power.

## Configure ROM files

The stock example ROMs are referenced by HTTPS URL. Commercial/custom ROMs are not included.

Place legally obtained custom 8 KB upper-ROM images in `config/roms/` using the placeholder filenames documented in `config/roms/README.md`, or edit the paths and labels for your own collection.

Preserve these rules:

1. Keep the chip ordering appropriate to the physical OneROM/X1 installation.
2. Give every selectable ROM set exactly one `label` and keep it on the upper `$E000-$FFFF` ROM. The selector uses this as the friendly display name; if it is omitted, the ROM filename/path will be displayed instead.
3. Keep `label` as the final member of that upper-ROM object for consistency with the tested supplied examples. This ordering is a project convention, not a JSON-schema requirement.
4. Keep the universal bootloader as the first non-plugin multi-chip set.

## Program OneROM

Use the matching **`onerom program`** command in `docs/CLI-COMMANDS.md`. This is important: the configuration JSON does **not** install the plugins by itself. The CLI must be given the configuration plus both plugin binaries so it can compile the complete firmware and download it to the OneROM.

For the v1.0.0 tested baseline, use the bundled USB v0.2.1 and host-control v0.1.2 plugin binaries by file path. Do not program a firmware image that was built without those plugin arguments, and do not assume that merely copying or selecting the JSON configuration installs the plugins.

The `onerom firmware build` command shown in `docs/CLI-COMMANDS.md` is optional for creating a reusable firmware file. The normal installation path is the `onerom program --config ... --plugin ... --plugin ...` command because it compiles the configuration with the required plugins and downloads the result to the connected OneROM.

After programming, power-cycle the drive and confirm that it initializes and can read a disk directory.

## Run the selector

1. Mount/use the root-level `1541-OneROM-Selector-v1.0.0.d64`, or copy `bin/1541-OneROM-Selector-v1.0.0.PRG` to another C64-accessible medium.
2. Load and run the PRG.
3. The selector polls IEC devices 8-11 and displays the drives it can see.
4. Choose a drive with cursor up/down and RETURN. If no input is made, the highlighted drive is accepted after the countdown.
5. Read the safety warning. Press RETURN to continue or `Q` to quit **before** RBCP initialization. The countdown also continues automatically.
6. After OneROM is found, use cursor up/down to select a ROM.
7. Use `E` to edit a display name or `R` to restore the compiled label.
8. Press `S` to SAVE. The selector writes/verifies the NV data and switches to the selected DOS.

After RBCP communication begins, SAVE is the supported normal completion path. If the program is unexpectedly ended and the drive misbehaves, power-cycle the 1541 to recover.
