# T1.1.0-17 Test Design

T16 proved `GET_BOOT_SLOT_INFO` succeeds under RBCP 0.1.2 and returns a boot
RAM slot of 13. Its displayed flash value 255 is the same Commodore BASIC NUL
decoding artifact previously found in the protocol major version: a returned
slot number zero produces an empty string through `GET#`.

T17 changes only the boot response defaults from `BF=255:BR=255` to
`BF=0:BR=0`. Nonzero bytes are still decoded with `ASC()`. Existing range,
active-slot, protocol, and reserved-value safety gates remain in place.

The test stops at the checkpoint before its terminal command. If the expected
pair `RAM 13, FLASH 0` is confirmed, RETURN sends `LOAD_AND_EXIT(13,0)` once,
does not poll the displaced response region, closes the DOS channel, and
returns to BASIC.
