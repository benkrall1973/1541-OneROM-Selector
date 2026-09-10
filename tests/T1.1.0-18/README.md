# 1541 OneROM Selector T1.1.0-18 — Current-Slot Mapping Diagnostic

T17 confirmed RBCP 0.1.2 and the authoritative boot pair flash 0 to RAM 13.
At Q, OneROM was serving current RAM 1. `LOAD_AND_EXIT` reloads a named RAM
slot but does not switch the active slot, so reloading RAM 13 would not repair
the response area currently written into RAM 1.

T18 tests the selector's current mapping without sending a terminal command.
The menu is one-based, while RBCP flash slots are zero-based, so menu item 1
corresponds to flash slot 0.

## Test

1. Power-cycle and confirm directory access.
2. Run `ONEROMT11018`, make no changes, and press Q.
3. Photograph the complete mapping checkpoint.
4. Do not press RUN/STOP. T18 sends no terminal command.
5. Power-cycle the drive after the photograph.

Expected result: current RAM 1, menu active 1, menu flash 0, boot flash 0,
candidate RAM 1/flash 0, and `MAPPING VALID - NOTHING SENT`.
