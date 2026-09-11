# T1.1.0-43 production-style Q-Quit

T43 preserves T40's hardware-proven repeated clean-exit behavior and removes
the completed Q diagnostic interaction from the normal user path:

- Q clears the screen and displays `QUITTING`;
- the proven active-slot validation and `LOAD_AND_EXIT` sequence runs
  automatically;
- no diagnostic mapping screen or additional Return key is required.

The Q-Quit implementation is unchanged from T40. It reloads the RAM slot
actively serving the RBCP back-channel from the flash slot of the active menu
ROM and treats an empty BASIC `GET#` result as legitimate RAM slot zero.

The instant fixed-text renderer introduced in T38 is retained.

## Hardware test

1. Power-cycle the physical 1541 and verify a directory read.
2. Run `ONEROMT11043`, continue to ROM Select, and press Q.
3. Verify `QUITTING` appears and the program returns automatically to a clear
   BASIC `READY.` screen without another keypress.
4. Read the physical disk directory twice without resetting either the C64 or
   drive; the drive LED must remain off after each completed read.
5. Run the selector again without a reboot and repeat the Q-Quit and two
   directory reads.
6. Complete a Save/Boot regression with a changed ROM.

T35 remains the VICE interface-simulation build. T43 is intended for physical-drive testing.

## Size comparison

- T35 combined physical/simulation PRG: 21,672 bytes
- T36 hardware-only PRG: 20,574 bytes
- Removed with simulation: 1,098 bytes
- Original selector v1.0.0 PRG: 18,963 bytes
- T36 versus v1.0.0: 1,611 bytes larger (about 8.5%)
