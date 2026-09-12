# Changelog

## v1.1.0 - 2026-09-12

- Targets OneROM firmware v0.7.2 and its RBCP v0.1.2 host-control functions.
- Uses current OneROM CLI named-plugin resolution for USB and host-control support.
- Adds reliable `Q` quit-without-saving from the idle selection screens.
- Restores the active ROM mapping, waits for terminal exit, initializes DOS, clears the C64 screen, and returns to BASIC `READY.`.
- Preserves normal disk access after Q-Quit and supports repeated selector runs without rebooting the C64 or drive.
- Retains Save/Reboot ROM selection and NV verification.
- Supports OneROM in either 1541 ROM socket and IEC device addresses 8-11.
- Removes custom ROM-name editing and uses labels defined in the OneROM configuration.
- Reworks the IEC Select, LOAD, and ROM Select interfaces and eliminates full-screen flashing during menu movement.
- Includes matching BASIC source, PRG, D64, documentation, and checksums.
- Promoted from hardware-proven test build T1.1.0-47; production code differs only in on-screen release titles.

## v1.0.0 - 2026-08-26

First cleaned public-release baseline.

- Established the selector and universal bootloader as v1.0.0.
- Added a ready-to-run D64, matching PRG and BASIC source.
- Added sanitized upper/lower-socket configuration examples.
- Bundled the then-current USB v0.2.1 and host-control v0.1.2 plugins.
- Added licensing, attribution, documentation, and release checksums.
