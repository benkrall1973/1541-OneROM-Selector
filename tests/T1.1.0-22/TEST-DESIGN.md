# Test design

T22 changes only the two `LOAD_AND_EXIT` argument bytes and their guards. T21 sent the current active RAM slot plus the menu flash slot. T22 sends the boot RAM and boot flash values returned by `GET_BOOT_SLOT_INFO`, which the v0.7.2 host-control documentation identifies as the pair required by `LOAD_AND_EXIT`.

The terminal command remains silent: no response poll and no DOS `CLOSE15` follow it. Only local C64 cleanup runs afterward. Success requires BASIC `READY.`, two directory reads, and a second selector run without resetting the C64 or physical drive.
