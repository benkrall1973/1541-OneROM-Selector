# Test design

T23 retains T22's boot RAM/flash mapping. The physical build changes only the lower-socket status presentation plus dormant simulation branches.

The terminal command remains silent: no response poll and no DOS `CLOSE15` follow it. Only local C64 cleanup runs afterward. Success requires BASIC `READY.`, two directory reads, and a second selector run without resetting the C64 or physical drive.

The separate VICE build differs from the physical build by one initialization value: `SM=1`. This bypasses device polling and all IEC/RBCP calls, injects deterministic OneROM-like menu and mapping values, and exercises the same menu/edit/restore dispatch plus a simulated save and clean-exit screen. The physical build sets `SM=0`.
