# Technical Documentation

## Release components

1. C64 BASIC V2 selector PRG.
2. Drive-side 6502 helper code embedded in the BASIC source and uploaded to 1541 RAM.
3. Universal 8 KB `$E000` bootloader in the first non-plugin OneROM multi-chip set.
4. OneROM USB v0.2.1 and host-control v0.1.2 plugins.

The release distributes the tested universal bootloader as a binary. A standalone bootloader assembler/build tree is not included, so the binary in `firmware/` is the authoritative v1.0.0 bootloader artifact.

## Drive selection and safety gate

Before RBCP initialization, the selector polls IEC devices 8-11. Available drives are presented in a selectable list with a countdown. The selected device number is stored in BASIC variable `D` and is used by subsequent command-channel opens.

After drive selection, the program displays a warning that unexpectedly quitting after communication begins can leave the 1541 requiring a power cycle. At this stage the user can press RETURN to continue or `Q` to exit safely before initialization.

## v1.1.0 API and cleanup policy

OneROM v0.7.2 is merged into the official OneROM `main` branch. ORA/plugin APIs are considered stable and public unless explicitly marked deprecated or expected to become deprecated.

An idle-menu cancel must close/clean up open communication without writing NV data or issuing a ROM switch. It must not attempt to cancel an RBCP/DOS transaction already in progress. The pre-initialization warning and timer may be removed only after this idle cleanup path passes real-hardware testing.

## Selector socket discovery

The selector initially uses:

- RBCP command page `$E000-$E0FF`
- RBCP back-channel `$E100-$E1FF`

If the upper-socket probe fails at the expected initialization stage, BASIC variable `P` changes from 224 (`$E0`) to 192 (`$C0`), the affected drive-side RAM helper bytes are patched, and the program retries through:

- RBCP command page `$C000-$C0FF`
- RBCP back-channel `$C100-$C1FF`

The same PRG therefore supports OneROM installed in either 1541 ROM socket.

## Universal bootloader

The universal bootloader is an 8 KB upper-ROM image mapped at `$E000` in the 1541 ROM set. It contains the boot-time RBCP logic needed to locate OneROM through either physical socket arrangement, read the saved selection from NV storage, select the requested ROM set, and continue through the normal 1541 reset path.

The release contains the tested universal bootloader and a verified generic base bootloader retained for development/reference. Older socket-specific bootloader variants are not distributed.

## ROM-set and NV model

| Item | Purpose |
|---|---|
| First non-plugin multi-chip set | Universal bootloader set |
| Following sets 1-7 | Selectable user DOS ROM sets |
| NV user byte 0 | Saved selectable slot number, 1-7 |
| Following NV records | Optional 28-character custom display names |

USB and host-control plugins are inserted before the configuration's normal chip sets by OneROM's plugin mechanism and are not counted as selectable DOS sets by the selector. The plugin binaries are program-time inputs to the OneROM CLI; the JSON configuration alone does not install them. The supported release installation path is `onerom program --config ... --plugin ... --plugin ...`, which compiles the configuration with the plugins and downloads the complete firmware to the OneROM.

## Label rule

For a multi-chip slot, RBCP returns the label associated with `chips[0]`. Each selectable set should therefore contain exactly one `label`, placed on `chips[0]`, regardless of which physical 1541 ROM socket that object represents.

The selector consumes the slot label returned by RBCP and does not independently choose an upper-ROM object. It uses that label as the human-readable ROM name. If it is omitted, OneROM metadata falls back to the ROM filename/path and the selector displays that path instead. JSON member order has no functional significance.

## SAVE sequence

SAVE writes modified custom-name records, writes the selected slot, reads data back for verification, prepares the selected ROM, and issues the final switch command. This sequence is treated as safety-critical project behavior and should not be casually reordered without real-hardware testing.

## BASIC source and PRG

`src/1541-OneROM-Selector-v1.0.0.bas` is the readable source corresponding to the release program. `bin/1541-OneROM-Selector-v1.0.0.PRG` is the tokenized release artifact.

No PRG build/tokenizer script is included in v1.0.0. If the source is changed, regenerate the PRG with a C64 BASIC V2-compatible tokenizer and verify that the resulting program runs correctly. C64 tokenized BASIC lines must remain within the platform's line-length constraints.
