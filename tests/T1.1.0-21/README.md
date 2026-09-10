# T1.1.0-21 final clean-exit test

This test combines T19's exact OneROM v0.7.2 `LOAD_AND_EXIT` transmission with T20's local C64 cleanup. It never sends `CLOSE15` after the terminal command.

1. **Power-cycle the physical 1541 first.** A C64 or 1541 Ultimate reset is not sufficient.
2. Verify one directory read.
3. Run `ONEROMT11021`, make no selection change, and press Q.
4. Continue only if protocol is `0.1.2`, current RAM is valid (normally `1`), menu flash is `0`, and the screen says `MAPPING VALID`.
5. Press RETURN once. Never press RUN/STOP.
6. Expected: `SENDING LOAD+EXIT NOW`, then `CLEAN EXIT COMPLETE`, then BASIC `READY.`.
7. Immediately read the directory twice without resetting or rebooting anything.

If current RAM is `255`, the safety check will transmit nothing. Power-cycle the physical drive before retrying.

