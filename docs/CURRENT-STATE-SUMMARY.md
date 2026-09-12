# Current State — v1.1.0

Selector v1.1.0 is the current hardware-proven release for OneROM firmware v0.7.2.

The production build is derived from T1.1.0-47. Its behavior is unchanged; only the on-screen test identifiers were replaced by the production titles `1541 ONEROM SELECTOR V1.1.0` and `ONEROM FW V0.7.2`.

Real-hardware testing covered:

- PRG launch from 1541 Ultimate
- PRG loading from a physical floppy in a real 1541
- OneROM discovery and ROM-label retrieval
- Save/Reboot with a changed ROM
- Q-Quit without changing the ROM
- repeated selector runs without rebooting
- repeated physical-disk directory reads after Q-Quit

T1.1.0-47 remains in `tests/` as the detailed test record. The release artifacts are the root D64, `bin/` PRG, and matching `src/` BASIC source.
