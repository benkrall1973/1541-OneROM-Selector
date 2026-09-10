# 1541 OneROM Selector T1.1.0-07 — Verified inactive-slot quit

T1.1.0-07 uses the same safe ROM-loading pattern as the selector's proven SAVE path, without writing NV data.

## T1.1.0-06 result

`LOAD_AND_EXIT` did not report an RBCP error, but reloading the ROM directly over the active RAM slot left the drive running a corrupted image. A power cycle restored normal operation and directory access, confirming flash and hardware were unharmed.

## New approach

On Q, the selector:

1. Enters RBCP command-response mode and queries the active RAM slot.
2. Chooses the other OneROM RAM slot.
3. Loads the currently active flash ROM into that inactive slot.
4. Waits for and verifies the LOAD_SLOT response.
5. Sends terminal SWITCH_AND_EXIT to the fully loaded slot.
6. Performs no NV name or selection write.

The externally visible ROM selection remains the same. Only OneROM's internal active RAM bank changes.

## First test

1. Power-cycle and verify a directory.
2. Run `ONEROMT11007`.
3. Make no menu changes.
4. Press Q.
5. Wait for `QUIT COMPLETE - NO CHANGES`.
6. Verify a directory and confirm the active ROM is unchanged.

If `CLEAN ROM LOAD FAILED` appears, record the RBCP error and power-cycle. Do not press RUN/STOP during cleanup.
