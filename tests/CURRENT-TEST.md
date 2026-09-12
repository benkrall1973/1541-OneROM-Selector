# Final v1.1.0 test baseline

[`T1.1.0-47`](T1.1.0-47/README.md) is the hardware-proven baseline promoted to Selector v1.1.0.

Confirmed on a physical Commodore 1541 with OneROM firmware v0.7.2:

- launch from a physical floppy and from 1541 Ultimate;
- ROM selection and Save/Reboot;
- repeated Q-Quit runs without ROM corruption;
- repeated directory reads after Q-Quit; and
- repeated selector runs without resetting the C64 or power-cycling the drive.

The production source preserves T1.1.0-47 behavior exactly. Only its on-screen selector and firmware title strings changed for release.

Future development must use the next unused test identifier and preserve T1.1.0-47 unchanged as the release evidence.
