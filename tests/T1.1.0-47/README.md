# T1.1.0-47 delayed post-exit DOS initialization

T47 removes T46's regressive startup initialization and tests the manual
recovery at its successful point after `LOAD_AND_EXIT`:

- startup behavior returns to T45;
- Q uses the proven active/back-channel RAM and flash pair;
- after terminal exit, it waits three seconds, closes the old command channel,
  sends DOS `I`, and returns to a clear BASIC screen.

The Q-Quit implementation is unchanged from T40. It reloads the RAM slot
actively serving the RBCP back-channel from the flash slot of the active menu
ROM and treats an empty BASIC `GET#` result as legitimate RAM slot zero.

The instant fixed-text renderer introduced in T38 is retained.

## Hardware test

1. Power-cycle the physical 1541 and verify a directory read.
2. Load and run the D64's `ONEROMT11047` from a real disk in that same 1541.
3. Continue to ROM Select and press Q.
4. Verify `QUITTING` appears and the program returns automatically to a clear
   BASIC `READY.` screen without another keypress.
5. Read the physical disk directory twice without resetting either the C64 or
   drive; the drive LED must remain off after each completed read.
6. Reload the selector from the same disk without a reboot and repeat Q-Quit
   and the two directory reads.
7. Complete a Save/Reboot regression with a changed ROM.

T35 remains the VICE interface-simulation build. T47 is intended for physical-drive testing.

## Size comparison

- T35 combined physical/simulation PRG: 21,672 bytes
- T36 hardware-only PRG: 20,574 bytes
- Removed with simulation: 1,098 bytes
- Original selector v1.0.0 PRG: 18,963 bytes
- T36 versus v1.0.0: 1,611 bytes larger (about 8.5%)
