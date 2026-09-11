# Test design

T42 is an interface-only successor to the hardware-proven T40 active-slot
clean-exit test. The `LOAD_AND_EXIT` arguments and terminal sequence are not
changed.

The selector sends `LOAD_AND_EXIT(RA,G-1)`, where `RA` comes from `GET_RAM_SLOT_INFO_ALL` and `G-1` is the flash image of the ROM active when Q was pressed. The boot pair remains diagnostic only. BASIC represents a returned zero byte as an empty string, so `RA` now initializes to zero before reading the fixed-length response.

Fixed text is staged in an off-screen buffer at `$C100` and copied to screen/color RAM by a 19-byte routine at `$C000`. This removes visible BASIC-loop rendering without changing selection redraw behavior.

The IEC countdown is drawn during initial screen construction, the redundant
selected-drive transition is removed, and the ROM result explicitly describes
the entries as ROMs/ROM sets.
