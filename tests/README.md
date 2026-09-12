# Test Builds

## Active v0.7.2 test history

The active test collection begins with `T1.1.0-16`, the first test where the
physical OneROM returned the real RBCP v0.1.2 protocol response after its
firmware was upgraded to OneROM v0.7.2.

`T1.1.0-02` through `T1.1.0-15` were removed from the active tree because the
physical OneROM was still running older firmware. Those results cannot be used
to evaluate the v0.7.2 functions. The deleted files remain recoverable from Git
history if they are ever needed for historical investigation.

`T1.1.0-47` is the final hardware-proven baseline promoted to v1.1.0. It passed
repeated Save/Reboot, Q-Quit, selector reload, and physical-disk directory
tests when launched from both a real floppy and 1541 Ultimate.

See [`CURRENT-TEST.md`](CURRENT-TEST.md) for the concise current-state pointer.

Retained tests:

- `T1.1.0-16` through `T1.1.0-20`: v0.7.2 diagnostics and development steps.
- `T1.1.0-21`: hardware-proven first-run clean-exit baseline.
- `T1.1.0-22`: current candidate; uses the boot RAM/flash pair returned by
  `GET_BOOT_SLOT_INFO` to test clean exit on repeated runs.
- `T1.1.0-23`: adds a deterministic VICE simulation and corrects the
  lower-socket search/success messages.
- `T1.1.0-24`: removes custom ROM-name editing and its NV helpers, reducing
  the tokenized PRG by 2,720 bytes while retaining `chip[0]` labels.
- `T1.1.0-25`: removes the redundant selected-name line and updates only the
  old/new highlighted rows during menu movement to eliminate screen flashing.
- `T1.1.0-26`: corrects the redraw row so the blank line below `ACTIVE:` is
  preserved and consolidates the controls onto one line.
- `T1.1.0-27`: makes simulated Save terminate at BASIC `READY.` and updates
  only the old/new rows while selecting an IEC device address.
- `T1.1.0-28`: clears the full screen immediately before BASIC `READY.` and
  gives the IEC selector the same compact control-label style as the ROM menu.
- `T1.1.0-29`: reports each actual loading, socket-search, service, retrieval,
  and menu stage; the VICE simulation pauses so the sequence can be watched.
- `T1.1.0-30`: names the three screens on the bottom row, labels the IEC
  countdown, clarifies Save-and-Boot, and replaces the repeated ROM-name list
  with a compact `X ROMS FOUND` result.
- `T1.1.0-31`: aligns the title/version at the top-left edge and preserves a
  one-character content margin for the compact ROM-count result.
- `T1.1.0-32`: centers the title/version and removes punctuation from the
  staged Load-screen status statements.
- `T1.1.0-33`: realigns selective ROM-row drawing after the header moved up,
  ensuring only the selected candidate remains highlighted.
- `T1.1.0-34`: centers the fixed-width automatic-selection countdown on the
  IEC screen while preserving its direct, flicker-free updates.
- `T1.1.0-35`: draws the ROM screen's bottom framing before its menu body,
  matching the visible construction order of IEC Select and Load.
- `T1.1.0-36`: preserves T35 as the VICE simulator and provides a smaller
  hardware-only build with all unreachable simulation code removed.
- `T1.1.0-37`: adds a clean IEC Select Q-to-BASIC path and a centered LOAD
  warning against RUN/STOP interruption, separated from the footer by a blank row.
- `T1.1.0-38`: closes and restores the C64 IEC channel after `LOAD_AND_EXIT`,
  initializes the resumed 1541 DOS, and renders fixed screen text without visible
  left-to-right construction.
- `T1.1.0-39`: removes the unsafe post-terminal close, retains only local IEC
  cleanup, and uses a delayed DOS `UJ` soft reset to recover the restored drive.
- `T1.1.0-40`: restores T21's active/back-channel RAM strategy, correctly
  decodes RAM slot zero, and removes the failed T38/T39 post-exit commands.
- `T1.1.0-41`: preserves T40's proven clean-exit logic while polishing Load
  spacing and adding a left margin before each bottom-left screen name.
- `T1.1.0-42`: draws all fixed IEC-screen elements immediately, removes the
  selected-drive transition screen, and clarifies the ROM/ROM-set count.
- `T1.1.0-43`: converts the proven Q diagnostic into an automatic user-facing
  quit displaying `QUITTING`, with no additional Return-key checkpoint.
- `T1.1.0-44`: aligns IEC Select address-list spacing, separator, and controls
  with the established ROM Select layout.
- `T1.1.0-45`: removes the IEC polling ellipsis, brackets the ROM count, and
  relabels the Save action as `S=SAVE/REBOOT`.
- `T1.1.0-46`: initializes DOS and waits one second before the OneROM service
  upload; hardware testing showed this regressed both launch paths.
- `T1.1.0-47`: restores T45 startup and automates the successful manual DOS
  initialization after a conservative post-`LOAD_AND_EXIT` delay.

## Packaging rules

Every test must use a unique directory such as `tests/T1.1.0-01/`.

Required contents:

```text
tests/T1.1.0-01/
├── README.md
├── source/
│   └── 1541-OneROM-Selector-T1.1.0-01.bas
├── bin/
│   └── 1541-OneROM-Selector-T1.1.0-01.PRG
├── disk/
│   └── 1541-OneROM-Selector-T1.1.0-01.d64
└── SHA256SUMS.txt
```

Copy `TEST-RESULTS-TEMPLATE.md` into the test directory as `README.md` and complete it during hardware testing. Never reuse a test version number, even when a build fails.
