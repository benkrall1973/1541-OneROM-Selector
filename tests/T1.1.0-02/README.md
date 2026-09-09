# 1541 OneROM Selector T1.1.0-02 — Tonight's Test

This is an experimental hardware test for OneROM firmware v0.7.2. It has been structurally validated but has not yet run on a physical 1541.

## What changed

- Preserves the v1.0.0 layout, colors, selection, edit, restore, and SAVE logic.
- Removes the old warning screen and its countdown.
- Adds `Q=QUIT WITHOUT SAVING` to the idle menu.
- Saves the original 187-byte RBCP back-channel before entering command-response mode.
- On Q, restores changed back-channel data bytes with RBCP `SLOT_POKE`, restores the eight-byte header with `EXIT_CMD_RESP_RESTORE`, and exits without an NV write or ROM-switch command.
- Uses `chips[0]` labels returned by RBCP; there is no upper-ROM label selection in the program.
- Displays `T1.1.0-02`, `V0.7.2`, and `BUILT WITH CHATGPT`.

## Important

When Q is pressed, the screen displays `QUITTING - CLEANING COMMUNICATION`. Do not press RUN/STOP during this stage. Cleanup may take several seconds because each changed byte is restored safely. Wait for `QUIT COMPLETE - NO CHANGES` and the BASIC screen.

Q is available only from the idle menu. It is not an abort mechanism for SAVE or another active transaction.

## First test — device 8, lower socket

1. Confirm a normal directory command works before starting.
2. Record the active ROM and saved names.
3. Load and run `ONEROMT11002` from the supplied D64, or use the standalone PRG.
4. Confirm the menu appears with the normal colors and ROM names.
5. Without editing or moving the selection, press Q.
6. Wait for `QUIT COMPLETE - NO CHANGES`.
7. Immediately run a directory command against the same 1541.
8. Run the selector again and confirm the active ROM and names are unchanged.

## If the first test passes

1. Highlight another ROM without saving, press Q, and confirm the original active ROM remains.
2. Edit a name without saving, press Q, restart, and confirm the edit was discarded.
3. Repeat on device 9.
4. Only after those Q tests pass, perform one normal SAVE regression test.

## Stop and record

If cleanup reports an error, hangs, changes ROM, or leaves the drive unresponsive, record the last screen text and drive/OneROM LED state, then power-cycle the drive. Do not repeatedly retry the failing operation.

## Implementation note

The exact back-channel image is captured before RBCP entry. The quit helper obtains the currently active RAM slot, restores only data bytes that differ, and sends terminal RBCP 0.1.2 control command `$00/$06` with the original header. It does not call the selector's existing load/switch routine.

