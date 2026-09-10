# Test design

T31 changes only alignment. A semicolon after the clear-screen character prevents BASIC `PRINT` from advancing to the second row; removal of the two header strings' leading spaces aligns them at column zero. The ROM-count result deliberately retains one leading content-space.

The three screen names and the existing credit are rendered by one direct screen-memory footer routine. It clears only the 40 cells of the bottom row, writes the screen name from the left, and writes the credit from the right. It does not use `PRINT`, move the BASIC cursor, scroll, or alter highlighted menu rows.

Only the VICE simulation adds observation pauses. The physical path relies on the real IEC and OneROM operation time and receives no new artificial wait.

The terminal command remains silent: no response poll and no DOS `CLOSE15` follow it. Successful paths clear the C64 screen immediately before `END`; the physical Save path performs that local clear before sending its terminal command. Success requires a clean-screen BASIC `READY.`, two directory reads, and a second selector run without resetting the C64 or physical drive.

The separate VICE build differs from the physical build by one initialization value: `SM=1`. This bypasses device polling and all IEC/RBCP calls, injects deterministic OneROM-like menu and mapping values, and exercises menu selection plus simulated save and clean exit. The physical build sets `SM=0`.

The hardware regression must verify that S still persists and boots a different selected ROM now that the unrelated custom-name NV service has been removed.

The VICE simulation supplies deterministic devices 8 and 9 so the IEC selector can be exercised without OneROM or a 1541. Its Save and Quit paths perform local C64 cleanup, clear the screen, and execute `END`; neither returns to the ROM menu.

The initial menu entry still clears and draws the complete screen. Subsequent Up/Down events store the old selection, update the selection index, redraw the old row normally, redraw the new row in reverse video, and return directly to the key loop without executing `PRINT CHR$(147)`. A visible blank row remains between `ACTIVE:` and the first ROM.
