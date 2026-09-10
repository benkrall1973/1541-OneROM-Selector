# 1541 OneROM Selector T1.1.0-03 — Cleanup Loop Fix

This experimental build continues the clean-exit work from T1.1.0-02.

## Why T1.1.0-02 failed

T1.1.0-02 saved the cleanup loop index in drive zero-page byte `$F8` before each RBCP `SLOT_POKE`, but did not reload the 6502 X register after the shared RBCP call. That call may change X. The loop could therefore continue at the wrong back-channel offset, fail with error 1, and leave the active drive ROM image incompletely restored.

T1.1.0-03 adds `LDX $F8` immediately after every successful `SLOT_POKE`, then advances to the next byte. All affected relative branches were recalculated.

## First test

1. Power-cycle the 1541 and verify a directory command works.
2. Load and run `ONEROMT11003`.
3. Do not edit, save, restore, or move the selection.
4. Press Q once.
5. Wait for either `QUIT COMPLETE - NO CHANGES` or an error.
6. Immediately test a directory command.
7. Stop after this first result and report the exact screen text.

Do not press RUN/STOP during cleanup. This remains hardware-test software.

## Only after the first test passes

Repeat after moving the selection without saving, then after editing a name without saving. Test a normal ROM change separately; the SAVE path ends the program after switching.

The layout and colors remain unchanged. Labels continue to come from OneROM `chips[0]`, and the footer remains `BUILT WITH CHATGPT`.
