# Test design

T21 changes no OneROM command bytes or slot mapping. It adds a visible checkpoint immediately before the terminal command and retains local-only C64 cleanup afterward. A valid test starts from a physical 1541 power-cycle and is successful only if BASIC returns to `READY.` and two directory reads work without any intervening reset.

