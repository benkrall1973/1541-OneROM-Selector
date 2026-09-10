# Interpretation

T21 proved that `LOAD_AND_EXIT` can cleanly return to BASIC and leave the physical drive usable on the first run. Its second-run guard rejected `CURRENT RAM 255`, even though the v0.7.2 host-control documentation does not identify that value as a terminal-command argument.

`GET_BOOT_SLOT_INFO` returns the flash slot that booted and the RAM slot into which it was loaded. The documentation explicitly says this is the pair a host needs for `LOAD_AND_EXIT`. T22 therefore treats the current active RAM value as diagnostic only and sends the returned boot RAM/flash pair. No command bytes, response handling, or post-terminal cleanup are otherwise changed.
