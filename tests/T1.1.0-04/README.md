# 1541 OneROM Selector T1.1.0-04 — Non-overlapping cleanup test

T1.1.0-04 replaces the failed T1.1.0-02/03 cleanup architecture.

## Root cause corrected

The older tests copied the saved 187-byte OneROM back-channel image into 1541 RAM at `$0610-$06CA`. That range overlaps the selector's resident RBCP machine code, so cleanup damaged the routines it then attempted to call.

T1.1.0-04 keeps the complete backup in C64 memory. It:

1. Queries the active OneROM RAM slot using a helper at `$0700-$0725`.
2. Reads each back-channel byte from offset 8 through 186.
3. Sends only changed bytes through a five-byte argument area at `$0780-$0784`.
4. Restores each changed byte with a helper at `$0740-$0778`.
5. Places only the final eight header bytes at `$07C8-$07CF`.
6. Sends terminal `EXIT_CMD_RESP_RESTORE` from `$0790-$07C2`.

These helper, argument, result and header ranges do not overlap one another or the shared RBCP implementation.

## First test

1. Power-cycle the 1541 and confirm a directory command works.
2. Run `ONEROMT11004`.
3. Do not move the selection, edit, restore or save.
4. Press Q.
5. Wait for the final message. This test can take longer than the earlier versions because the C64 checks the restoration byte by byte.
6. Immediately verify a directory command.
7. Stop and report the exact screen if any query or restore offset fails.

Do not press RUN/STOP during cleanup. This remains experimental hardware-test software.
