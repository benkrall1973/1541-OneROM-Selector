# Preserved active-slot root cause

T21 and T22 use identical drive helpers but different terminal arguments. T21 names current active RAM plus active ROM flash; T22 through T39 name boot RAM plus boot flash.

The v0.7.2 host-control source records `s_state.active_slot` as both the served slot and the destination of every back-channel write. `LOAD_AND_EXIT` repairs the entire image when the named RAM slot is the one being served. Reloading a different slot can exit command-response mode without repairing the served ROM.

T21's apparent second-run RAM value 255 had a separate parsing cause: valid slot zero is a NUL byte, which BASIC `GET#` returns as an empty string. Initializing `RA` to 255 made zero look missing. T42 initializes it to zero and still rejects an explicit byte 255.

T42 deliberately changes no RBCP, IEC-selection logic, or exit behavior from
T40. Its functional source delta is limited to when fixed IEC text is drawn,
removing the redundant transition screen, and revising the ROM-count label.
