# Test design

T37 tests the two remaining interface safeguards on the hardware-only path: a clean IEC Select quit before any drive-side state is opened, and a fixed LOAD-screen warning against RUN/STOP interruption.

The warning is written directly to screen row 22 and the footer remains on row 24, leaving row 23 blank. This keeps the warning and footer stable while normal LOAD progress messages use the upper body.

The hardware regression covers IEC Q, the LOAD layout, initial and repeated ROM Quit, directory access after each ROM Quit, and Save/Boot with a changed ROM.
