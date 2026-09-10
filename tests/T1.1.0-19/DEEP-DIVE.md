# Why this test is different

Earlier quit experiments either closed only the Commodore command channel, attempted restoration through the wrong mechanism, or used unverified slot values. They could return the C64 to BASIC while leaving the drive executing invalid or incomplete state.

OneROM v0.7.2 now responds with protocol `0.1.2` and exposes the boot/current mapping needed by this selector. T1.1.0-19 uses those returned values, proves the selector-to-OneROM index conversion on screen, and then invokes OneROM's terminal `LOAD_AND_EXIT` operation exactly once.

The key safety rule is that there is no additional RBCP query after `LOAD_AND_EXIT`. Success is judged externally by two normal directory reads and the drive LED state.
