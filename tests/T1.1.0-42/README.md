# T1.1.0-42 IEC transition and status-text polish

T42 preserves T40's hardware-proven repeated clean-exit behavior and T41's
spacing polish while making three interface adjustments:

- renders the initial IEC countdown with the screen name and credit;
- removes the intermediate `DRIVE X SELECTED` transition screen;
- changes the result to `X ROMS/ROM SETS FOUND`.

The Q-Quit implementation is unchanged from T40. It reloads the RAM slot
actively serving the RBCP back-channel from the flash slot of the active menu
ROM and treats an empty BASIC `GET#` result as legitimate RAM slot zero.

The instant fixed-text renderer introduced in T38 is retained.

## Hardware test

1. Power-cycle the physical 1541 and verify a directory read.
2. Run `ONEROMT11042` and verify the three spacing changes on IEC Select, Load,
   and ROM Select.
3. Continue to ROM Select and press Q.
4. Verify the diagnostic identifies the active back-channel pair, then press Return once.
5. Read the physical disk directory twice without resetting either the C64 or drive; the drive LED must remain off after each completed read.
6. Run the selector again without a reboot and repeat the ROM-Q and directory test.
7. Complete a Save/Boot regression with a changed ROM.

T35 remains the VICE interface-simulation build. T42 is intended for physical-drive testing.

## Size comparison

- T35 combined physical/simulation PRG: 21,672 bytes
- T36 hardware-only PRG: 20,574 bytes
- Removed with simulation: 1,098 bytes
- Original selector v1.0.0 PRG: 18,963 bytes
- T36 versus v1.0.0: 1,611 bytes larger (about 8.5%)
