# Test design

T47 tests automated reproduction of the manual recovery that restored
`LOAD"$",8` after Q-Quit. T46 showed that initializing before upload regresses
both disk-loaded and Ultimate-injected launches, so T47 restores T45 startup.

The selector sends `LOAD_AND_EXIT(RA,G-1)`, where `RA` comes from `GET_RAM_SLOT_INFO_ALL` and `G-1` is the flash image of the ROM active when Q was pressed. The boot pair remains diagnostic only. BASIC represents a returned zero byte as an empty string, so `RA` now initializes to zero before reading the fixed-length response.

Fixed text is staged in an off-screen buffer at `$C100` and copied to screen/color RAM by a 19-byte routine at `$C000`. This removes visible BASIC-loop rendering without changing selection redraw behavior.

After `LOAD_AND_EXIT`, the C64 waits three seconds for the drive to leave RBCP
command-response mode and restore the active ROM. It then closes logical file
15, opens the DOS command channel with `I`, closes it, clears the screen, and
ends. No command is sent during the terminal transition itself.
