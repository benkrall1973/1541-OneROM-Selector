# Test design

T45 is a wording-only successor to T44. The `LOAD_AND_EXIT` arguments, queries,
validation, and terminal sequence are unchanged.

The selector sends `LOAD_AND_EXIT(RA,G-1)`, where `RA` comes from `GET_RAM_SLOT_INFO_ALL` and `G-1` is the flash image of the ROM active when Q was pressed. The boot pair remains diagnostic only. BASIC represents a returned zero byte as an empty string, so `RA` now initializes to zero before reading the fixed-length response.

Fixed text is staged in an off-screen buffer at `$C100` and copied to screen/color RAM by a 19-byte routine at `$C000`. This removes visible BASIC-loop rendering without changing selection redraw behavior.

The IEC polling label loses its ellipsis, the ROM count gains brackets, and
the Save control now states that its result operation reboots the drive.
