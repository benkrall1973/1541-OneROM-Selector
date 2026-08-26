# ROM files

Place legally obtained 8 KB **upper 1541 ROM** images here when using the sanitized example configurations.

The example names are:

- `1541-upper-slot-2.bin`
- `1541-upper-slot-3.bin`
- `1541-upper-slot-4.bin`
- `1541-upper-slot-5.bin`
- `1541-upper-slot-6.bin`
- `1541-upper-slot-7.bin`

Edit both the `file` and final `label` fields to suit your ROM collection. Each selectable ROM set needs a `label` for a clean human-readable name in 1541 OneROM Selector; without it, the selector displays the ROM filename/path supplied by OneROM metadata. Commercial ROMs such as JiffyDOS are intentionally not included.


## Plugin installation

These JSON files describe the OneROM configuration only. They do not install the USB or host-control plugins. The required plugins must be supplied to the OneROM CLI during the `onerom program` operation so the CLI compiles them into the firmware before downloading it to the OneROM.
