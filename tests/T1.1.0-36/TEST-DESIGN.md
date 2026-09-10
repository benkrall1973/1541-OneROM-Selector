# Test design

T36 proves that the production hardware path does not depend on the VICE simulator. It starts directly with physical IEC polling and contains no `SM` variable or jumps to simulated startup, Save, or Quit routines.

T35 is preserved unchanged as the deterministic VICE build. This separation allows the hardware PRG to remain smaller without losing the reusable simulator and its source.

The hardware regression covers initial Quit, repeated-run Quit, directory access after each Quit, and Save/Boot with a changed ROM.
