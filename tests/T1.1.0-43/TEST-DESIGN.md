# Test design

T43 turns the hardware-proven T40 active-slot clean-exit test into a normal
user-facing Q-Quit path. The `LOAD_AND_EXIT` arguments, queries, validation,
and terminal sequence are unchanged.

The selector sends `LOAD_AND_EXIT(RA,G-1)`, where `RA` comes from `GET_RAM_SLOT_INFO_ALL` and `G-1` is the flash image of the ROM active when Q was pressed. The boot pair remains diagnostic only. BASIC represents a returned zero byte as an empty string, so `RA` now initializes to zero before reading the fixed-length response.

Fixed text is staged in an off-screen buffer at `$C100` and copied to screen/color RAM by a 19-byte routine at `$C000`. This removes visible BASIC-loop rendering without changing selection redraw behavior.

The successful path no longer prints internal mapping values or waits for an
extra Return key. It displays `QUITTING`, performs cleanup, clears the screen,
and returns to BASIC. Safety failures still stop before the terminal command
and provide an actionable error.
