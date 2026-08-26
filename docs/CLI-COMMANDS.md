# OneROM CLI Commands

Run these commands from the repository root in PowerShell on Windows.

This guide uses the official OneROM CLI command structure. The command shown in some older notes as something like `onerom.exe -configuration ... --usbplugin --hostcontrol` is **not** the current CLI syntax. The current workflow is `onerom program --config ...` with plugin arguments supplied using `--plugin`.

The official OneROM CLI documentation describes `onerom` (`onerom.exe` on Windows) as the tool for discovering connected One ROM devices, programming firmware, and inspecting device information.

## 1. Confirm the CLI is installed

```powershell
onerom --version
```

This confirms Windows can find `onerom.exe` and shows which CLI release is installed. The CLI documentation recommends checking the version before using the command set.

## 2. See what OneROM devices are connected

Start with:

```powershell
onerom scan
```

`scan` lists connected One ROM devices and reports information such as serial number, USB location, board type, MCU, and firmware version.

For more detail:

```powershell
onerom scan --verbose
```

The verbose form also provides additional device-identification information such as the MCU variant and chip ID.

To also show the ROM slots discovered on each device:

```powershell
onerom scan --slots
```

## 3. Record the OneROM serial number

The serial number shown by `onerom scan` is useful when more than one OneROM is connected.

You can also inspect the selected device directly:

```powershell
onerom inspect info
```

This reports the serial number, name, board type, MCU, firmware version, and hardware revision.

When multiple OneROM devices are connected, select a specific device with its serial number:

```powershell
onerom --serial YOUR_SERIAL_NUMBER inspect info
```

The CLI accepts `--serial` as a global option. It is required when multiple devices are connected and can also use `*` and `?` wildcards.

**Example:**

```powershell
onerom --serial "FC9D67248E8E8023" inspect info
```

Do not put your real serial number into public configuration examples or documentation.

## 4. Check the ROM slots before programming

```powershell
onerom inspect slots
```

This shows the ROM image slots stored on the connected OneROM and identifies the active slot.

You can also combine this with the initial scan:

```powershell
onerom scan --slots
```

## 5. Check the board and socket information

List the board types supported by the installed CLI:

```powershell
onerom board list
```

For the connected OneROM, display the programming/header information:

```powershell
onerom inspect header
```

Display the ROM socket pinout:

```powershell
onerom inspect socket
```

These commands are useful before wiring or troubleshooting an installation. The official CLI provides both device-oriented header and socket inspection commands.

## 6. Configure the ROM JSON files

The sanitized example configurations are:

```text
config/1541-OneROM-Config-Upper-Socket-v1.0.0.example.json
config/1541-OneROM-Config-Lower-Socket-v1.0.0.example.json
```

Edit the configuration so that the ROM file paths point to your legally obtained ROM images.

For the 1541 OneROM Selector, **every selectable ROM set must have exactly one `label` on the upper `$E000-$FFFF` ROM object**. The selector uses this label as the friendly ROM name. Without the label, OneROM metadata falls back to the ROM filename/path and the selector displays that path instead.

## 7. Program the OneROM with the required plugins

### This is the important part

**Do not assume the JSON file installs the plugins. It does not.**

The OneROM CLI must be given the configuration file **and both plugin binaries during the `program` command**. The CLI builds the complete firmware, including the plugins, and then downloads that firmware to the OneROM.

The official CLI uses the `program` command and `--plugin` options for this workflow. Plugin arguments can be supplied as local files, and the same plugin mechanism is used by both `program` and `firmware build`.

For this v1.0.0 release, use the bundled tested plugin binaries so the exact tested versions are reproduced:

- USB plugin v0.2.1
- host-control plugin v0.1.2

### Upper ROM socket

With one OneROM connected:

```powershell
onerom program --config config/1541-OneROM-Config-Upper-Socket-v1.0.0.example.json --board fire-24-e --plugin file=plugins/usb_plugin_v0.2.1.bin --plugin file=plugins/host-control_plugin_v0.1.2.bin
```

### Lower ROM socket

```powershell
onerom program --config config/1541-OneROM-Config-Lower-Socket-v1.0.0.example.json --board fire-24-e --plugin file=plugins/usb_plugin_v0.2.1.bin --plugin file=plugins/host-control_plugin_v0.1.2.bin
```

The CLI documentation confirms that `program` builds and flashes the firmware in one operation, and that `--plugin file=...` can supply a local plugin binary.

### Multiple OneROM devices connected

Specify the serial number so you do not accidentally program the wrong board:

```powershell
onerom --serial "YOUR_SERIAL_NUMBER" program --config config/1541-OneROM-Config-Upper-Socket-v1.0.0.example.json --board fire-24-e --plugin file=plugins/usb_plugin_v0.2.1.bin --plugin file=plugins/host-control_plugin_v0.1.2.bin
```

Replace `YOUR_SERIAL_NUMBER` with the serial reported by `onerom scan`.

## 8. Verify the programming result

After programming, scan the device again:

```powershell
onerom scan
```

Then inspect the device:

```powershell
onerom inspect info
```

And check its ROM slots:

```powershell
onerom inspect slots
```

A useful one-command check after programming is:

```powershell
onerom program --config config/1541-OneROM-Config-Upper-Socket-v1.0.0.example.json --board fire-24-e --plugin file=plugins/usb_plugin_v0.2.1.bin --plugin file=plugins/host-control_plugin_v0.1.2.bin --scan-slots
```

The official CLI documents `--scan-slots` as a post-programming option that runs `onerom scan --slots` after programming.

## 9. Optional: create a firmware file without programming

This is **not** the normal installation path, but it is useful when you want to keep a firmware artifact:

```powershell
onerom firmware build --config config/1541-OneROM-Config-Upper-Socket-v1.0.0.example.json --board fire-24-e --plugin file=plugins/usb_plugin_v0.2.1.bin --plugin file=plugins/host-control_plugin_v0.1.2.bin --out 1541-OneROM-Upper.bin
```

For the lower socket:

```powershell
onerom firmware build --config config/1541-OneROM-Config-Lower-Socket-v1.0.0.example.json --board fire-24-e --plugin file=plugins/usb_plugin_v0.2.1.bin --plugin file=plugins/host-control_plugin_v0.1.2.bin --out 1541-OneROM-Lower.bin
```

If you later program a separately built image, make sure it was built **with both required plugins**. A firmware image created without those plugin inputs will not contain the selector's required USB/RBCP functionality.

## 10. Named plugin alternative

Current OneROM CLI versions also support named plugin resolution:

```powershell
--plugin usb --plugin host-control
```

The official CLI documents both named plugins and local `file=` plugin specifications.

For this v1.0.0 release, the **file-based plugin commands above are preferred** because they pin the tested USB v0.2.1 and host-control v0.1.2 binaries. Using named plugins may retrieve newer versions.

## 11. Important distinction: JSON vs. programmed firmware

Think of the process this way:

```text
JSON configuration
       +
USB plugin binary
       +
host-control plugin binary
       |
       v
   OneROM CLI
   `onerom program`
       |
       v
complete firmware image
       |
       v
downloaded to OneROM
```

The JSON file describes the configuration. The **CLI programming command is what assembles the complete firmware and installs it on the OneROM**.

For this project, the host-control plugin is especially important because the C64 selector communicates with OneROM through RBCP. OneROM v0.7.1 specifically restored/fixed the RBCP host-control plugin.

## 12. Useful troubleshooting commands

Show CLI help:

```powershell
onerom --help
```

Show help for a specific command:

```powershell
onerom program --help
onerom scan --help
onerom inspect --help
```

Show the complete detected device information:

```powershell
onerom inspect info
```

Show ROM slots:

```powershell
onerom inspect slots
```

Show GPIO usage while the OneROM is running:

```powershell
onerom inspect gpio
```

Show the board header:

```powershell
onerom inspect header
```

Show the ROM socket pinout:

```powershell
onerom inspect socket
```

These commands are read-only inspection tools except where specifically noted by the OneROM CLI documentation.

## 13. Beginner workflow summary

For a new user, the normal sequence is:

```powershell
onerom --version
onerom scan
onerom inspect info
onerom scan --slots
```

Write down the serial number and board information from the output.

Then choose the correct upper- or lower-socket JSON, place your legally obtained ROM files where the JSON expects them, and run the matching `onerom program --config ... --plugin file=... --plugin file=...` command from above.

Finally verify:

```powershell
onerom scan
onerom inspect info
onerom inspect slots
```

If more than one OneROM is connected, prepend `--serial "YOUR_SERIAL_NUMBER"` to the programming and inspection commands.

## Unrecognised or unprogrammed devices

If the CLI cannot identify an unprogrammed/stopped device, reconnect it in the board's required bootloader mode and follow the current OneROM CLI documentation for `--unrecognised` together with the correct `--board` value. The CLI documentation states that this mode is intended for unrecognised, unprogrammed, or bricked RP2350 boards that still expose a valid picoboot USB interface.

Do not commit personal device serial numbers or absolute local filesystem paths to public configuration examples.
