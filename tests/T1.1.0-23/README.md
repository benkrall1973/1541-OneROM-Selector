# T1.1.0-23 lower-socket display and VICE simulation test

This test retains T22's v0.7.2 boot-pair `LOAD_AND_EXIT` behavior. It removes the duplicate `SEARCHING...` line during the lower-socket retry and explicitly reports `ONEROM FOUND IN LOWER SOCKET` when that retry succeeds.

Two builds are included:

- `bin/` and `disk/` contain the physical-hardware test.
- `vice/` contains a simulation build that supplies seven mock ROM names, boot RAM 13, boot flash 0, current RAM 255, and protocol 0.1.2 without performing IEC or RBCP communication.

## Physical hardware

1. **Power-cycle the physical 1541 first.** A C64 or 1541 Ultimate reset is not sufficient.
2. Verify one directory read.
3. Run `ONEROMT11023`, make no selection change, and press Q.
4. Continue only if protocol is `0.1.2`, the boot RAM/flash pair is valid, and the screen says `MAPPING VALID`.
5. Press RETURN once. Never press RUN/STOP.
6. Expected: `SENDING LOAD+EXIT NOW`, then `CLEAN EXIT COMPLETE`, then BASIC `READY.`.
7. Immediately read the directory twice without resetting or rebooting anything.
8. Run the same PRG again without resetting either machine, press Q, and repeat the two directory reads.
9. Repeat once with a ROM change and SAVE to confirm the existing save path is unchanged.

`CURRENT RAM 255` is diagnostic information only in this test. The terminal pair comes exclusively from `GET_BOOT_SLOT_INFO`, as specified by the v0.7.2 host-control documentation.

## VICE simulation

1. Attach the D64 under `vice/disk/` and load its only PRG.
2. Run it. No real or emulated 1541 communication is attempted.
3. Confirm the screen displays one `SEARCHING...` line followed by `ONEROM FOUND IN LOWER SOCKET`.
4. Exercise menu movement, edit, restore, simulated save, and Q.
5. At the Q checkpoint, confirm `CURRENT RAM 255`, `BOOT RAM 13`, and `BOOT FLASH 0` are shown.
6. Press RETURN and confirm the program terminates at BASIC `READY.`.
7. Run it again without resetting VICE and repeat.

The simulation validates C64-side flow and presentation only. It cannot validate actual OneROM, RBCP, IEC timing, or physical-drive recovery.
