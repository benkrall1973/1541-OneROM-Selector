# 1541 OneROM Selector T1.1.0-16 — Updated v0.7.2 Clean-Q Test

> **Hardware result: boot-slot decoding bug found.** T16 correctly reported
> RBCP `0.1.2` and boot RAM 13, but displayed boot flash 255 because flash slot
> zero arrived as a BASIC empty string. It sent nothing and was recovered by
> power cycle. T1.1.0-17 supersedes this test.

T1.1.0-16 corrects the T15 diagnostic zero-byte bug. The updated physical
OneROM reported RBCP `0.1.2`; Commodore BASIC returned the zero major-version
byte as an empty string, and T15 incorrectly retained its diagnostic default
of 255.

T16 initializes all three version fields to zero. A real `0.1.2` response now
passes the compatibility gate and proceeds to `GET_BOOT_SLOT_INFO`.

## Test

1. Power-cycle the drive and confirm directory access.
2. Run `ONEROMT11016` and make no changes.
3. Press Q.
4. Photograph the complete checkpoint screen.
5. **Do not press RETURN yet.** Send the photograph for review first.

The checkpoint should report protocol `0.1.2`, valid boot flash/RAM slots, and
the same active RAM slot returned by the RAM information query. RETURN sends
the terminal `LOAD_AND_EXIT` command only after those safety checks pass.

Never press RUN/STOP during this diagnostic.
