# T1.1.0-05 failed hardware testing

Do not use this build.

On 2026-09-10, a physical 1541 with OneROM v0.7.2 reported `RESTORE FAILED AT OFFSET 8 / RBCP ERROR 3`.

The active-slot query and command-response entry succeeded. OneROM rejected the first `SLOT_POKE` directed at the active slot. T1.1.0-06 replaces all active-slot byte writes with terminal `LOAD_AND_EXIT`, reloading the whole current ROM image from its flash source.
