# 1541 OneROM Selector T1.1.0-06 — Whole-image clean exit

T1.1.0-06 replaces the rejected active-slot `SLOT_POKE` cleanup with OneROM v0.7.2's terminal `LOAD_AND_EXIT` operation.

## T1.1.0-05 result

Hardware reached the first actual restoration byte and reported `RESTORE FAILED AT OFFSET 8 / RBCP ERROR 3`. Error 3 means OneROM completed the command but rejected the active-slot `SLOT_POKE`.

## New approach

The selector already knows the currently active flash selection and successfully queries the active OneROM RAM slot. On Q, T1.1.0-06 sends `LOAD_AND_EXIT` with those two values. OneROM reloads the entire current ROM image from flash into its active RAM slot and exits command-response mode without polling afterward.

This restores the entire ROM image, including all 187 back-channel bytes, requires no 8 KB buffer in the 1541, performs no ROM selection change, and does not write the selector's NV name storage.

## First test

1. Power-cycle the 1541 and verify a directory.
2. Run `ONEROMT11006`.
3. Make no menu changes.
4. Press Q and wait for `QUIT COMPLETE - NO CHANGES`.
5. Immediately verify a directory.
6. Restart the selector and confirm the active ROM is unchanged.

Do not press RUN/STOP during cleanup. This remains experimental hardware-test software.
