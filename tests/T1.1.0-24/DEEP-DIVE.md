# Interpretation

T21 proved that `LOAD_AND_EXIT` can cleanly return to BASIC and leave the physical drive usable on the first run. Its second-run guard rejected `CURRENT RAM 255`, even though the v0.7.2 host-control documentation does not identify that value as a terminal-command argument.

`GET_BOOT_SLOT_INFO` returns the flash slot that booted and the RAM slot into which it was loaded. The documentation explicitly says this is the pair a host needs for `LOAD_AND_EXIT`. T24 therefore treats the current active RAM value as diagnostic only and sends the returned boot RAM/flash pair. No command bytes, response handling, or post-terminal cleanup are otherwise changed.

The repeated `SEARCHING...` display came from printing it in both the lower-socket transition and the shared search routine. T24 leaves the text only in the shared routine and adds an explicit success message after a successful lower-socket query.

VICE cannot emulate OneROM's hardware RBCP registers directly. The included simulation build therefore bypasses communication before the command channel is opened and injects fixed successful responses. It is deliberately unable to claim hardware protocol correctness, but it permits repeatable testing of the surrounding C64-side interface and return-to-BASIC behavior.

Name editing required more than its small visible input routine. It also required loading saved custom names during startup, uploading dedicated NV read/write helpers to the drive, maintaining original-name and dirty-state arrays, and writing up to 28 bytes per changed name. Removing that complete path reduced the PRG by 2,720 bytes. OneROM configuration labels remain available and continue to come from `chip[0]`.
