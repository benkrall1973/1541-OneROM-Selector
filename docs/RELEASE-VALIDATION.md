# Release Validation — v1.0.0

This file records mechanical checks performed on the public v1.0.0 package.

## D64 and PRG

- D64 size: 174,848 bytes (standard 35-track image).
- Disk name: `ONEROM SEL V100`.
- Disk ID: `10`.
- Directory contains one closed PRG: `ONEROMSELV100`.
- Directory block count: 75; sector-chain count: 75.
- BAM/free-sector map is internally consistent with the directory and PRG chains.
- Embedded PRG is byte-for-byte identical to `bin/1541-OneROM-Selector-v1.0.0.PRG`.
- PRG load address: `$0801`.
- Tokenized BASIC link chain: 321 valid, strictly increasing line numbers.
- Longest tokenized BASIC line record: 200 bytes (line 600), below the 255-byte line-record limit.
- The included D64/PRG has been successfully loaded and run in **VICE 3.9** using `x64sc.exe` (64-bit) on Windows 10.

## BASIC source

- `src/1541-OneROM-Selector-v1.0.0.bas` contains the same 321 BASIC line numbers as the PRG.
- Source lines are stored in numeric BASIC line order for clean retokenization/editing.

## Universal bootloader

- File size: 8,192 bytes.
- SHA-256: `7313b07f26fcc3778664b0c53f1aff46af883ed8b0a3cbf525efc9bb40432b0e`.
- NMI vector: `$E000`.
- RESET vector: `$E000`.
- IRQ vector: `$E000`.
- The tested universal bootloader and the verified generic base bootloader are distributed; older socket-specific bootloader variants are absent.

## OneROM configurations

Both sanitized JSON examples:

- Parse as valid JSON.
- Validate against the OneROM configuration schema supplied with the audited OneROM source tree.
- Use current `chip_sets` / `chips` property names.
- Contain eight multi-chip sets total: one bootloader set plus seven selectable user sets.
- Keep exactly one `label` per selectable set, attached to the upper `$E000-$FFFF` ROM. For the selector, this label is functionally required for a friendly display name; without it, the ROM filename/path is displayed instead.
- Keep `label` as the final member of that upper-ROM object. This is the tested project convention; the OneROM schema permits `label` but does not require final-member placement.
- Reference only the included universal bootloader, public stock-ROM URLs, and sanitized local placeholder filenames.

## Licensing and third-party material

- Root `LICENSE`: MIT for original 1541 OneROM Selector project material.
- `licenses/OneROM-LICENSE.md`: verified byte-for-byte against the OneROM license file supplied in the audited upstream source archive.
- `licenses/RBCP-MIT.txt`: preserves the RBCP MIT notice.
- Bundled RBCP reference-source snapshots were removed because they are not required to use the release and included platform-specific reference configuration that could be mistaken for 1541 build source.
- OneROM plugin binaries remain explicitly identified as third-party components.
- Release installation documentation explicitly requires the OneROM CLI `program` command with the configuration plus both plugin binaries; the JSON configuration alone does not install plugins.

## Integrity

`SHA256SUMS.txt` covers every distributed file except itself. Verify from the repository root with a SHA-256 utility appropriate to your operating system.


## Base bootloader reference

The repository also retains `1541-OneROM-Bootloader-Base-v1.0.0.bin` as the verified original/base bootloader binary used during development.

SHA-256:

`b89951c4883c559f7aa6b6639a890a8e76a10f67685f2124a2a0e7eebbe87152`

This is retained for development/reproducibility reference. The release configs use the universal bootloader, whose SHA-256 is:

`7313b07f26fcc3778664b0c53f1aff46af883ed8b0a3cbf525efc9bb40432b0e`

## CLI documentation

The release documentation uses the current OneROM CLI command structure. The beginner workflow is:

```powershell
onerom --version
onerom scan
onerom inspect info
onerom scan --slots
```

When multiple OneROM devices are connected, the serial number reported by `onerom scan` can be supplied with the global `--serial` option. The v1.0.0 programming examples use:

```powershell
onerom program --config <configuration.json> --board fire-24-e --plugin file=plugins/usb_plugin_v0.2.1.bin --plugin file=plugins/host-control_plugin_v0.1.2.bin
```

This is intentional: the JSON configuration alone does not install the plugins. The CLI must compile the configuration with the required plugin binaries and download the resulting firmware to the OneROM.

The command syntax and plugin mechanism were cross-checked against the official OneROM CLI manual: https://github.com/piersfinlayson/one-rom/blob/main/docs/CLI-MANUAL.md.
