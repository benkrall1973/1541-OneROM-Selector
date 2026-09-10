# 1541 OneROM Selector T1.1.0-07 — FAILED HARDWARE TEST

> **Do not use this build.** Real-hardware testing on OneROM v0.7.2 failed during Q=Quit.

T1.1.0-07 attempted to use the selector's SAVE-style inactive-slot loading sequence without writing NV data.

## Hardware result

The program displayed:

```text
CLEAN ROM LOAD FAILED
RBCP ERROR 3
POWER-CYCLE DRIVE
```

OneROM rejected the LOAD_SLOT request before the terminal slot switch. The operator power-cycled the drive as instructed.

## Conclusion

This method is retired:

1. Query the active RAM slot.
2. Choose the inactive RAM slot.
3. Load the currently selected flash ROM into that inactive slot.
4. Switch to it and exit.

Neither direct active-slot restoration nor inactive-slot same-ROM loading is accepted as a clean quit implementation for the selector.

Do not retry T1.1.0-07. Use it only as a recorded failed test.
