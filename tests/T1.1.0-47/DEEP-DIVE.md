# Preserved active-slot root cause

T21 and T22 use identical drive helpers but different terminal arguments. T21 names current active RAM plus active ROM flash; T22 through T39 name boot RAM plus boot flash.

The v0.7.2 host-control source records `s_state.active_slot` as both the served slot and the destination of every back-channel write. `LOAD_AND_EXIT` repairs the entire image when the named RAM slot is the one being served. Reloading a different slot can exit command-response mode without repairing the served ROM.

T21's apparent second-run RAM value 255 had a separate parsing cause: valid slot zero is a NUL byte, which BASIC `GET#` returns as an empty string. Initializing `RA` to 255 made zero look missing. T47 initializes it to zero and still rejects an explicit byte 255.

T47 addresses the confirmed post-Q state: both launch paths can return
`FILE NOT FOUND` for the directory, while a manual DOS `I` immediately restores
directory access. This demonstrates a live drive with stale DOS/disk state,
not a missing file or permanently corrupted ROM.

T38/T39 cannot rule out this approach because they used the incorrect boot-slot
pair. T47 retains T40's corrected active-slot pair and introduces a conservative
three-second wait before reproducing the successful manual initialization.
