# T37 failure interpretation

T37 demonstrated that `LOAD_AND_EXIT` executed: the program reached BASIC and the red drive LED turned off. The subsequent directory request turned the LED solid and left the drive inaccessible until reboot. This indicates that terminal OneROM exit occurred, but the restored 1541 DOS or IEC command state was not ready for the next transaction.

T38 keeps the v0.7.2 mapping logic intact and adds explicit cleanup around the transition: close the C64 command channel, restore default IEC channels, wait for DOS, then issue DOS initialize through a newly opened channel. This is a narrow test of restored-DOS readiness rather than another mapping experiment.

The screen-rendering change is independent: strings are prepared outside visible screen RAM and copied in one short 6502 loop, making them appear effectively atomically.
