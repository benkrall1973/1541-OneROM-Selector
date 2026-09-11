# T1.1.0-39 terminal-safe soft-reset recovery

T38 worked once after a physical drive restart but failed on the second run, and its post-terminal `CLOSE15` contradicted the OneROM v0.7.2 terminal-command rules. T39 removes that unsafe close and the ineffective DOS `I` experiment.

The v0.7.2 `GET_BOOT_SLOT_INFO` mapping and `LOAD_AND_EXIT` bytes remain unchanged. After the silent terminal command, T39 abandons the obsolete channel locally with `CLRCHN` and the KERNAL file-count reset, waits three seconds, sends DOS `UJ` through a fresh command channel, abandons that reset channel locally, waits another three seconds, and returns to a cleared BASIC screen.

The instant fixed-text renderer introduced in T38 is retained.

## Hardware test

1. Power-cycle the physical 1541 and verify a directory read.
2. Run `ONEROMT11039` and verify fixed footer/warning text appears without left-to-right animation.
3. Continue to ROM Select and press Q.
4. Allow the automatic restored-DOS soft-reset sequence to finish and verify BASIC `READY.` appears on a cleared screen.
5. Read the physical disk directory twice without resetting either the C64 or drive; the drive LED must remain off after each completed read.
6. Run the selector again without a reboot and repeat the ROM-Q and directory test.
7. Complete a Save/Boot regression with a changed ROM.

T35 remains the VICE interface-simulation build. T39 is intended for physical-drive testing.

## Size comparison

- T35 combined physical/simulation PRG: 21,672 bytes
- T36 hardware-only PRG: 20,574 bytes
- Removed with simulation: 1,098 bytes
- Original selector v1.0.0 PRG: 18,963 bytes
- T36 versus v1.0.0: 1,611 bytes larger (about 8.5%)
