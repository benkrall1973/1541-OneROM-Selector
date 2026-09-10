# T1.1.0-19 guarded clean-exit hardware test

This test sends the OneROM v0.7.2 `LOAD_AND_EXIT` command only after displaying and validating the active mapping.

1. Power-cycle the 1541 and confirm a directory can be read.
2. Load and run `ONEROMT11019`.
3. Do not press RUN/STOP at any point.
4. Press `Q` at the selector menu.
5. Photograph the mapping checkpoint before continuing.
6. Continue only if it shows protocol `0.1.2`, current RAM `1`, boot flash `0`, menu flash `0`, and `MAPPING VALID`.
7. Press RETURN once to send `LOAD_AND_EXIT 1,0`.
8. At the BASIC prompt, read the directory twice without power-cycling the drive.
9. Report both directory results and whether the drive LED is off, solid, or blinking.

If the mapping differs or the program reports a mismatch, do not continue. Power-cycle the drive and report the screen values.

