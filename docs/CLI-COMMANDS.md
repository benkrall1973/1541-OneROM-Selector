# OneROM CLI Commands

Run these commands from the repository root in PowerShell.

## Inspect the device

```powershell
onerom --version
onerom scan
onerom inspect info
onerom scan --slots
```

If multiple OneROM devices are attached, add `--serial "YOUR_SERIAL_NUMBER"` immediately after `onerom`.

## Program an upper-socket installation

```powershell
onerom program --config config/1541-OneROM-Config-Upper-Socket-v1.1.0.example.json --board fire-24-e --plugin usb --plugin host-control --scan-slots
```

## Program a lower-socket installation

```powershell
onerom program --config config/1541-OneROM-Config-Lower-Socket-v1.1.0.example.json --board fire-24-e --plugin usb --plugin host-control --scan-slots
```

The named `usb` and `host-control` arguments tell the current CLI to resolve compatible plugin versions. The configuration JSON alone does not install plugins.

## Build a firmware file without programming

```powershell
onerom firmware build --config config/1541-OneROM-Config-Upper-Socket-v1.1.0.example.json --board fire-24-e --plugin usb --plugin host-control --out 1541-OneROM-Upper-v0.7.2.bin
```

Substitute the lower-socket config and output name when appropriate.
