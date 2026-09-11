# T1.1.0-45 interface wording polish

T45 preserves T43's automatic, hardware-proven Q-Quit behavior and makes three
wording changes:

- removes the ellipsis after `POLLING FOR AVAILABLE DRIVES`;
- displays the ROM count in brackets, such as `[7] ROMS/ROM SETS FOUND`;
- changes the ROM control label to `S=SAVE/REBOOT`.

The Q-Quit implementation is unchanged from T40. It reloads the RAM slot
actively serving the RBCP back-channel from the flash slot of the active menu
ROM and treats an empty BASIC `GET#` result as legitimate RAM slot zero.

The instant fixed-text renderer introduced in T38 is retained.

## Hardware test

1. Power-cycle the physical 1541 and verify a directory read.
2. Run `ONEROMT11045`, continue to ROM Select, and press Q.
3. Verify `QUITTING` appears and the program returns automatically to a clear
   BASIC `READY.` screen without another keypress.
4. Read the physical disk directory twice without resetting either the C64 or
   drive; the drive LED must remain off after each completed read.
5. Run the selector again without a reboot and repeat the Q-Quit and two
   directory reads.
6. Complete a Save/Boot regression with a changed ROM.

T35 remains the VICE interface-simulation build. T45 is intended for physical-drive testing.

## Size comparison

- T35 combined physical/simulation PRG: 21,672 bytes
- T36 hardware-only PRG: 20,574 bytes
- Removed with simulation: 1,098 bytes
- Original selector v1.0.0 PRG: 18,963 bytes
- T36 versus v1.0.0: 1,611 bytes larger (about 8.5%)
