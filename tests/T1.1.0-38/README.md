# T1.1.0-38 restored-DOS cleanup and instant fixed text

T38 addresses the physical T37 result where ROM Select Q returned to BASIC and turned off the red LED, but the following directory request produced a solid red LED until the drive was rebooted.

The v0.7.2 `GET_BOOT_SLOT_INFO` mapping and `LOAD_AND_EXIT` command are unchanged. After sending the terminal command, T38 now closes logical file 15, restores the C64 IEC channels, waits three seconds for the original 1541 DOS to resume, sends DOS `I`, closes channel 15 again, and then returns to a cleared BASIC screen.

T38 also replaces visible BASIC screen-memory drawing with a small buffered machine-code copy. The footer, screen label, LOAD warning, and IEC countdown label now appear as complete text rather than being painted slowly from left to right.

## Hardware test

1. Power-cycle the physical 1541 and verify a directory read.
2. Run `ONEROMT11038` and verify fixed footer/warning text appears without left-to-right animation.
3. Continue to ROM Select and press Q.
4. Allow the three-second restored-DOS initialization delay and verify BASIC `READY.` appears on a cleared screen.
5. Read the physical disk directory twice without resetting either the C64 or drive; the drive LED must remain off after each completed read.
6. Run the selector again without a reboot and repeat the ROM-Q and directory test.
7. Complete a Save/Boot regression with a changed ROM.

T35 remains the VICE interface-simulation build. T38 is intended for physical-drive testing.

## Size comparison

- T35 combined physical/simulation PRG: 21,672 bytes
- T36 hardware-only PRG: 20,574 bytes
- Removed with simulation: 1,098 bytes
- Original selector v1.0.0 PRG: 18,963 bytes
- T36 versus v1.0.0: 1,611 bytes larger (about 8.5%)
