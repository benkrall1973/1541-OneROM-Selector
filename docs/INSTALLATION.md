# Installation

## Requirements

- Commodore 64 or compatible system
- Commodore 1541 drive
- OneROM Fire 24E running firmware v0.7.2
- Current OneROM CLI with USB and host-control plugins
- Universal bootloader from `firmware/`
- One to seven legally obtained 1541 DOS ROM sets

## Choose the OneROM socket

For an upper-socket installation, install OneROM in `$E000-$FFFF`, remove the lower ROM, connect X1 to pin 20 of the empty `$C000-$DFFF` socket, and use `config/1541-OneROM-Config-Upper-Socket-v1.1.0.example.json`.

For a lower-socket installation, install OneROM in `$C000-$DFFF`, remove the upper ROM, connect X1 to pin 20 of the empty `$E000-$FFFF` socket, and use `config/1541-OneROM-Config-Lower-Socket-v1.1.0.example.json`.

Verify orientation, socket condition, and X1 wiring before applying power.

## Configure ROM files

Replace the placeholder paths with legally obtained 8 KB upper-ROM images. Every selectable set must contain exactly one `label` on `chips[0]`; that is the friendly name returned to the selector.

Keep the universal bootloader as the first non-plugin multi-chip set. The following one to seven sets are the selectable DOS ROM sets.

## Program OneROM

From the repository root, program the appropriate config with the current CLI:

```powershell
onerom program --config config/1541-OneROM-Config-Upper-Socket-v1.1.0.example.json --board fire-24-e --plugin usb --plugin host-control --scan-slots
```

Use the lower-socket config when appropriate. The CLI resolves and incorporates the compatible plugins, builds the firmware, flashes OneROM, and then displays the slots. Power-cycle the drive afterward and verify a disk directory.

## Run the selector

1. Mount `1541-OneROM-Selector-v1.1.0.d64`, or copy `bin/1541-OneROM-Selector-v1.1.0.PRG` to a C64-accessible disk.
2. Load and run the PRG.
3. Choose an available IEC drive with cursor up/down and RETURN.
4. Wait while the selector uploads its drive service, locates OneROM, and retrieves ROM information.
5. Select a ROM with cursor up/down.
6. Press `S` to save and reboot into that ROM, or `Q` to quit without changing it.

Do not press RUN/STOP while the LOAD screen is communicating with the drive. Power-cycle the drive if a transaction is interrupted.
