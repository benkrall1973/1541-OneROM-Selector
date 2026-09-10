# T1.1.0-32 centered headers and clean status text

This test retains T31's three-screen interface, centers the title and version on the 40-column display, and removes trailing periods/ellipses from every Load-screen status statement. `X ROMS FOUND` retains its one-character content margin.

The loading result now has one blank line before `X ROMS FOUND`, omits the redundant ROM-name list, and places `BOOTING TO MENU...` directly below it. The ROM menu says `S=SAVE & BOOT`, and IEC selection identifies its countdown as `AUTO SELECT IN [10]`.

The physical build adds no new delay. The VICE build pauses briefly after each simulated stage so the loading display can be observed.

The controls are consolidated to one line: `UP/DOWN=SELECT   S=SAVE   Q=QUIT`.

Removed components include the Edit and Restore commands, custom-name NV reads and writes, name buffers and flags, and their drive-side helper uploads. S continues to save and boot the selected ROM normally.

Two builds are included:

- `bin/` and `disk/` contain the physical-hardware test.
- `vice/` contains a simulation build that supplies seven mock ROM names, boot RAM 13, boot flash 0, current RAM 255, and protocol 0.1.2 without performing IEC or RBCP communication.

## Physical hardware

1. **Power-cycle the physical 1541 first.** A C64 or 1541 Ultimate reset is not sufficient.
2. Verify one directory read.
3. Run `ONEROMT11032`, make no selection change, and press Q.
4. Continue only if protocol is `0.1.2`, the boot RAM/flash pair is valid, and the screen says `MAPPING VALID`.
5. Press RETURN once. Never press RUN/STOP.
6. Expected: `SENDING LOAD+EXIT NOW`, then a cleared screen with BASIC `READY.`.
7. Immediately read the directory twice without resetting or rebooting anything.
8. Run the same PRG again without resetting either machine, press Q, and repeat the two directory reads.
9. Repeat once with a ROM change and SAVE to confirm the existing save path is unchanged.

`CURRENT RAM 255` is diagnostic information only in this test. The terminal pair comes exclusively from `GET_BOOT_SLOT_INFO`, as specified by the v0.7.2 host-control documentation.

## VICE simulation

1. Attach the D64 under `vice/disk/` and load its only PRG.
2. Run it. The simulator supplies IEC devices 8 and 9 without real drive communication.
3. Confirm the IEC instruction line reads `UP/DOWN=SELECT   RETURN=CONTINUE`. Move between devices 8 and 9 and confirm only the two address rows change, with no list redraw or flash. Select either address with RETURN.
4. Confirm the title and version are centered on the top two rows. Confirm the bottom-left labels change from `IEC SELECT` to `LOAD` and then `ROM SELECT`, while the lower-right credit remains intact.
5. Confirm the staged loading screen ends with a blank line, `7 ROMS FOUND`, and `BOOTING TO MENU...`, without printing all seven names.
6. Exercise ROM-menu movement and confirm the blank line below `ACTIVE:` remains visible.
7. Press S and confirm the screen clears and BASIC `READY.` appears without returning to the menu.
8. Run it again without resetting VICE, press Q, confirm the boot-pair checkpoint, and finish on a cleared screen at BASIC `READY.`.

The simulation validates C64-side flow and presentation only. It cannot validate actual OneROM, RBCP, IEC timing, or physical-drive recovery.

## Size result

The tokenized physical PRG is 21,676 bytes.
