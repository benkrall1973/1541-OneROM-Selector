# Test design

T25 retains T24's boot RAM/flash mapping, lower-socket presentation, simulation architecture, and removal of custom-name editing. It removes the `SELECTED:` line and replaces full menu re-entry after Up/Down with a two-row redraw helper.

The terminal command remains silent: no response poll and no DOS `CLOSE15` follow it. Only local C64 cleanup runs afterward. Success requires BASIC `READY.`, two directory reads, and a second selector run without resetting the C64 or physical drive.

The separate VICE build differs from the physical build by one initialization value: `SM=1`. This bypasses device polling and all IEC/RBCP calls, injects deterministic OneROM-like menu and mapping values, and exercises menu selection plus simulated save and clean exit. The physical build sets `SM=0`.

The hardware regression must verify that S still persists and boots a different selected ROM now that the unrelated custom-name NV service has been removed.

The initial menu entry still clears and draws the complete screen. Subsequent Up/Down events store the old selection, update the selection index, redraw the old row normally, redraw the new row in reverse video, and return directly to the key loop without executing `PRINT CHR$(147)`.
