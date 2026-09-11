# Test design

T38 isolates the post-`LOAD_AND_EXIT` failure seen in T37. The boot RAM/flash pair and terminal RBCP command remain unchanged; only the host cleanup and restored-DOS initialization sequence changes.

The new sequence closes logical file 15, calls the C64 KERNAL `CLRCHN`, waits 180 jiffies, opens command channel 15 with DOS `I`, closes it, and calls `CLRCHN` again before clearing the screen.

Fixed text is staged in an off-screen buffer at `$C100` and copied to screen/color RAM by a 19-byte routine at `$C000`. This removes visible BASIC-loop rendering without changing selection redraw behavior.
