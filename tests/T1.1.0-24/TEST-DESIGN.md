# Test design

T24 retains T23's boot RAM/flash mapping, lower-socket presentation, and simulation architecture. It removes all custom-name editing and restoration code while preserving labels supplied by OneROM `chip[0]`.

The terminal command remains silent: no response poll and no DOS `CLOSE15` follow it. Only local C64 cleanup runs afterward. Success requires BASIC `READY.`, two directory reads, and a second selector run without resetting the C64 or physical drive.

The separate VICE build differs from the physical build by one initialization value: `SM=1`. This bypasses device polling and all IEC/RBCP calls, injects deterministic OneROM-like menu and mapping values, and exercises menu selection plus simulated save and clean exit. The physical build sets `SM=0`.

The hardware regression must verify that S still persists and boots a different selected ROM now that the unrelated custom-name NV service has been removed.
