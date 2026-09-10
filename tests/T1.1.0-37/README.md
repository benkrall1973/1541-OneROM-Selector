# T1.1.0-37 IEC Quit and LOAD warning

T37 builds on the hardware-only T36 selector with two interface safeguards:

- IEC Select now shows `Q=QUIT` on the same line as the movement and Return controls.
- Pressing Q on IEC Select clears the screen and returns directly to BASIC `READY.`
- LOAD shows a centered `DO NOT PRESS RUN/STOP` warning on row 22.
- Row 23 remains blank between the warning and the screen/credit footer on row 24.

The IEC quit occurs before the drive channel and OneROM service are opened, so no drive-side cleanup is required. The ROM Select Q path continues to use the v0.7.2 boot RAM/flash pair and `LOAD_AND_EXIT` clean shutdown.

## Hardware test

1. Power-cycle the physical 1541 and verify a directory read.
2. Run `ONEROMT11037`.
3. On IEC Select, verify the single control line reads `UP/DOWN=SELECT RETURN=CONTINUE Q=QUIT`.
4. Press Q and verify a cleared screen at BASIC `READY.`
5. Run it again, continue from IEC Select, and verify the centered LOAD warning and blank row above the footer.
6. Complete the existing repeated-run ROM Quit and Save/Boot regressions.

T35 remains the VICE interface-simulation build. T37 is intended for physical-drive testing.

## Size comparison

- T35 combined physical/simulation PRG: 21,672 bytes
- T36 hardware-only PRG: 20,574 bytes
- Removed with simulation: 1,098 bytes
- Original selector v1.0.0 PRG: 18,963 bytes
- T36 versus v1.0.0: 1,611 bytes larger (about 8.5%)
