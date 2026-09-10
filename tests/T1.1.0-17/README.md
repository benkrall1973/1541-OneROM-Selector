# 1541 OneROM Selector T1.1.0-17 — Boot-Slot NUL Fix

T16 confirmed RBCP `0.1.2`, RAM count 16, active RAM 1, and returned boot RAM
13. It displayed boot flash 255 because flash slot 0 arrived as a NUL byte and
the BASIC diagnostic retained its 255 default. T16 correctly sent nothing and
the drive recovered by power cycle.

T17 initializes both boot-slot fields to zero. No framing or terminal-command
logic changed.

## Test

1. Power-cycle the drive and confirm directory access.
2. Run `ONEROMT11017`, make no changes, and press Q.
3. Photograph the complete checkpoint.
4. Confirm it shows protocol `0.1.2`, boot flash `0`, and boot RAM `13`.
5. **Do not press RETURN yet.** Send the photograph for review.

RETURN is the point that transmits terminal `LOAD_AND_EXIT`. Never press
RUN/STOP during the diagnostic.
