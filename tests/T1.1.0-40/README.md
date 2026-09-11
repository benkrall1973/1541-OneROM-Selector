# T1.1.0-40 active-slot clean-exit correction

T40 returns to T21's hardware-proven `LOAD_AND_EXIT` model while retaining the optimized interface.

T40 reloads the RAM slot actively serving the RBCP back-channel from the flash slot of the active menu ROM. This repairs the exact image whose bytes RBCP displaced. It also treats an empty BASIC `GET#` result as legitimate RAM slot zero instead of incorrectly leaving the value at 255.

The instant fixed-text renderer introduced in T38 is retained.

## Hardware test

1. Power-cycle the physical 1541 and verify a directory read.
2. Run `ONEROMT11040` and verify fixed footer/warning text appears without left-to-right animation.
3. Continue to ROM Select and press Q.
4. Verify the diagnostic identifies the active back-channel pair, then press Return once.
5. Read the physical disk directory twice without resetting either the C64 or drive; the drive LED must remain off after each completed read.
6. Run the selector again without a reboot and repeat the ROM-Q and directory test.
7. Complete a Save/Boot regression with a changed ROM.

T35 remains the VICE interface-simulation build. T40 is intended for physical-drive testing.

## Size comparison

- T35 combined physical/simulation PRG: 21,672 bytes
- T36 hardware-only PRG: 20,574 bytes
- Removed with simulation: 1,098 bytes
- Original selector v1.0.0 PRG: 18,963 bytes
- T36 versus v1.0.0: 1,611 bytes larger (about 8.5%)
