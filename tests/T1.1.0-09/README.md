# 1541 OneROM Selector T1.1.0-09 — Screen-Only Q Diagnostic

T1.1.0-09 removes the mandatory device-9 file logger that stopped T1.1.0-08 at BASIC line 3564 with `DEVICE NOT PRESENT`.

## Confirmed by T1.1.0-08

- RAM slot count: 16
- Active RAM slot: 1
- ROM type: 2
- Fourth returned byte: 255
- Active menu entry: 2
- Selected menu entry: 2
- Menu count: 7

## Test

1. Power-cycle drive 8 and confirm a directory.
2. Run `ONEROMT11009`.
3. Make no changes and press Q.
4. Photograph the checkpoint screen.
5. Press RETURN. Do not press RUN/STOP.
6. The program discards edits and routes through the existing Save finalization with the originally active ROM selected.
7. Confirm the same ROM remains active and read a directory.

## Safety

T09 performs no device-9 logging, no XOR slot selection, and no custom LOAD_SLOT cleanup. If an error appears before RETURN, power-cycle drive 8 before further use.
