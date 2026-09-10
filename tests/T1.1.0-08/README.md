# 1541 OneROM Selector T1.1.0-08 — Logged Q Diagnostic

This build diagnoses the slot mapping used by Q and then exits through the selector's existing hardware-proven Save pathway. It does **not** use the failed T1.1.0-02 through T1.1.0-07 cleanup methods.

## What Q does

1. Queries GET_RAM_SLOT_INFO_ALL using a complete reset/knock/command-response sequence.
2. Displays the returned RAM-slot count, active RAM slot, ROM type, and reserved byte.
3. Displays the selector's active menu index, selected menu index, and menu count.
4. Replaces and writes T11008LOG on device 9.
5. Pauses only after the query has completed.
6. On RETURN, discards menu/name edits and invokes the exact existing Save finalization for the originally active ROM.

The Save pathway may rewrite the existing selection value, but Q deliberately sets it to the ROM active when the menu opened and clears all name-edit flags.

## Hardware setup

- Physical OneROM-equipped 1541: device 8.
- 1541 Ultimate-II+ used for the program and log: device 9.
- OneROM firmware: v0.7.2.

## Test

1. Power-cycle drive 8.
2. Confirm a directory can be read.
3. Mount 1541-OneROM-Selector-T1.1.0-08.d64 on device 9.
4. Run ONEROMT11008.
5. Make no changes.
6. Press Q.
7. Photograph the CHECKPOINT 1 COMPLETE screen.
8. Press RETURN. Do not press RUN/STOP.
9. Wait for the normal Save/boot pathway to complete.
10. Confirm a directory can be read from drive 8 and the same ROM remains active.
11. Read T11008LOG from device 9 with a text viewer or Ultimate filesystem access.

## Stop conditions

- If ACTIVE SLOT QUERY FAILED appears, record the displayed error and slot, then power-cycle drive 8.
- If the checkpoint values look impossible, photograph them before continuing.
- Never press RUN/STOP after Q begins.
- Do not rerun a failure without first power-cycling drive 8 and confirming a directory.

## Expected log

    T08,QUERY,RAMCOUNT=...,ACTIVE=...,TYPE=...,RES=...
    T08,MAP,MENUACTIVE=...,CHOICE=...,COUNT=...
    T08,NEXT,PROVEN-SAVE-PATH,ROM=...

## Important limitation

This build proves discovery and mapping and tests Q through the already working Save finalizer. It does not yet test a corrected direct LOAD_AND_EXIT. That change should be made only after the raw values from this test are captured.
