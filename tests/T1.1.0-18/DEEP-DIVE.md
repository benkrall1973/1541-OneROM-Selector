# Current RAM Versus Boot RAM

T17 established that the OneROM boot metadata is flash slot 0 and RAM slot 13,
while the selector's Q-time query sees RAM slot 1 currently being served.

Current upstream `LOAD_AND_EXIT` copies the supplied flash slot into the
supplied RAM slot and then leaves command-response mode. It does not activate a
different RAM slot. Therefore the safe target must be the RAM slot containing
the active back-channel, not an inactive boot-time RAM slot.

For this selector, visible menu entries are one-based while RBCP flash slots
are zero-based. With menu item 1 active, its candidate flash slot is 0. T18
validates that relationship and records the candidate repair pair without
executing it. A later test may use `LOAD_AND_EXIT(current RAM, menu flash)`
only after this mapping is confirmed on hardware.
