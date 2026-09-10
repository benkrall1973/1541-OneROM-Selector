# Interpretation

The source shows that the large drive-program upload precedes socket detection. The upper-socket probe then executes that code. If the probe fails, the selector rewrites mapping-dependent portions for the lower socket and retries. After a successful probe, it configures and starts the OneROM service, retrieves the ROM metadata, and builds the menu. T29 labels those real boundaries; it does not rearrange the protocol.

T21 proved that `LOAD_AND_EXIT` can cleanly return to BASIC and leave the physical drive usable on the first run. Its second-run guard rejected `CURRENT RAM 255`, even though the v0.7.2 host-control documentation does not identify that value as a terminal-command argument.

`GET_BOOT_SLOT_INFO` returns the flash slot that booted and the RAM slot into which it was loaded. The documentation explicitly says this is the pair a host needs for `LOAD_AND_EXIT`. T28 therefore treats the current active RAM value as diagnostic only and sends the returned boot RAM/flash pair. No command bytes, response handling, or post-terminal cleanup are otherwise changed.

The repeated `SEARCHING...` display came from printing it in both the lower-socket transition and the shared search routine. T28 leaves the text only in the shared routine and adds an explicit success message after a successful lower-socket query.

VICE cannot emulate OneROM's hardware RBCP registers directly. The included simulation build therefore bypasses communication before the command channel is opened and injects fixed successful responses. It is deliberately unable to claim hardware protocol correctness, but it permits repeatable testing of the surrounding C64-side interface and return-to-BASIC behavior.

Name editing required more than its small visible input routine. It also required loading saved custom names during startup, uploading dedicated NV read/write helpers to the drive, maintaining original-name and dirty-state arrays, and writing up to 28 bytes per changed name. Removing that complete path reduced the PRG by 2,720 bytes. OneROM configuration labels remain available and continue to come from `chip[0]`.

The menu flash was caused by both arrow-key branches jumping back to the full menu routine, whose first operation clears the screen with `PRINT CHR$(147)`. T28 positions the cursor from HOME and overwrites only the two affected 36-character rows. No static screen content is redrawn during selection movement.

T25's first redraw row was one line too high because `PRINT CHR$(147)` clears the display and then advances to the following row. The initial menu therefore placed list item 1 at row 6, while the redraw helper targeted row 5. T28 aligns the helper with the rendered list.

The IEC selector previously redrew every detected address and both instruction lines after each movement. T28 stores the previous device-list index and uses a dedicated cursor-positioned helper to repaint only the old and new address rows. Countdown updates remain independent.

T28 makes no RBCP or terminal-command changes. Its exit change is strictly local presentation: successful paths clear the C64 display immediately before BASIC regains control, so `READY.` appears on a clean screen. The IEC change likewise affects only its instruction text.
