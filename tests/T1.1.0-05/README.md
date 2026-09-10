# 1541 OneROM Selector T1.1.0-05 — Session-entry cleanup test

T1.1.0-05 retains the non-overlapping, C64-side 187-byte backup introduced in T1.1.0-04 and fixes the active-slot query.

## T1.1.0-04 result and correction

Hardware testing reported `ACTIVE SLOT QUERY FAILED / ERROR 1 / SLOT 187`. Error 1 is the selector's no-token result; 187 was the unchanged diagnostic byte, not a valid slot.

The menu is in RBCP command mode. T1.1.0-04 incorrectly issued `GET_RAM_SLOT_INFO_ALL` as though a command-response session were already open. T1.1.0-05 follows the proven selector convention: reset/knock through `$04CF`, enter command-response through `$0503`, then issue the slot query.

## First test

1. Power-cycle the 1541 and verify a directory command.
2. Run `ONEROMT11005`.
3. Make no menu changes.
4. Press Q and wait.
5. Immediately verify a directory command.
6. Report the exact screen if the active-slot query or a restore offset fails.

Do not press RUN/STOP during cleanup. This remains experimental hardware-test software.
