# T1.1.0-36 hardware-only selector

T36 is the physical-hardware counterpart to the retained T35 VICE simulation. It preserves T35's interface and OneROM v0.7.2 behavior while removing all unreachable simulation code from the PRG.

Removed from this build:

- the `SM` simulation switch and branches;
- simulated IEC devices 8 and 9;
- mock ROM names and mapping values;
- simulated Save and Quit paths;
- simulation-only observation delays.

The physical IEC, RBCP, Save/Boot, and clean Quit implementations are unchanged from T35.

## Hardware test

1. Power-cycle the physical 1541 and verify a directory read.
2. Run `ONEROMT11036`.
3. Verify IEC Select, Load, and ROM Select screens and their bottom labels.
4. Press Q and verify a cleared screen at BASIC `READY.` followed by two directory reads.
5. Run the program again without resetting either machine and repeat the Quit test.
6. Run it once more, select another ROM, and use `S=SAVE & BOOT`.

T35 remains the VICE interface-simulation build. T36 is intended for tonight's physical-drive testing.

## Size comparison

- T35 combined physical/simulation PRG: 21,672 bytes
- T36 hardware-only PRG: 20,574 bytes
- Removed with simulation: 1,098 bytes
- Original selector v1.0.0 PRG: 18,963 bytes
- T36 versus v1.0.0: 1,611 bytes larger (about 8.5%)
