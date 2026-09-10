# T1.1.0-22 repeated-run boot-pair test

This test keeps T21's hardware-proven terminal command and local C64 cleanup, but passes the RAM/flash pair returned by v0.7.2 `GET_BOOT_SLOT_INFO` to `LOAD_AND_EXIT`. It never sends `CLOSE15` after the terminal command.

1. **Power-cycle the physical 1541 first.** A C64 or 1541 Ultimate reset is not sufficient.
2. Verify one directory read.
3. Run `ONEROMT11021`, make no selection change, and press Q.
4. Continue only if protocol is `0.1.2`, the boot RAM/flash pair is valid, and the screen says `MAPPING VALID`.
5. Press RETURN once. Never press RUN/STOP.
6. Expected: `SENDING LOAD+EXIT NOW`, then `CLEAN EXIT COMPLETE`, then BASIC `READY.`.
7. Immediately read the directory twice without resetting or rebooting anything.
8. Run the same PRG again without resetting either machine, press Q, and repeat the two directory reads.
9. Repeat once with a ROM change and SAVE to confirm the existing save path is unchanged.

`CURRENT RAM 255` is diagnostic information only in this test. The terminal pair comes exclusively from `GET_BOOT_SLOT_INFO`, as specified by the v0.7.2 host-control documentation.
