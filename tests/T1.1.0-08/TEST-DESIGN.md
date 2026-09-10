# T1.1.0-08 Test Design

T1.1.0-08 is a diagnostic bridge between the failed custom cleanup implementations and a future corrected direct exit.

## Removed assumptions

- No active_ram_slot XOR 1.
- No assumption that a menu index is an RBCP flash-slot index.
- No SLOT_POKE into the live back-channel.
- No direct LOAD_SLOT, SWITCH_AND_EXIT, LOAD_AND_EXIT, or EXIT_CMD_RESP_RESTORE from the Q routine.

## Logged variables

| Field | Meaning |
|---|---|
| RAMCOUNT | Byte 0 returned by GET_RAM_SLOT_INFO_ALL |
| ACTIVE | Byte 1 returned by GET_RAM_SLOT_INFO_ALL |
| TYPE | Byte 2 returned by GET_RAM_SLOT_INFO_ALL |
| RES | Byte 3 returned by GET_RAM_SLOT_INFO_ALL |
| MENUACTIVE | Selector variable G, captured when the menu opened |
| CHOICE | Selector variable C at Q |
| COUNT | Number of selectable menu entries |

## Exit behavior

After logging, the program sets C=G, clears all F() edit flags, and branches to the original Save routine. This gives the exact finalization sequence already shown to switch successfully between Stock and JiffyDOS on the test hardware.
