# Current test candidate

The current OneROM v0.7.2 test candidate is
[`T1.1.0-45`](T1.1.0-45/README.md).

The latest hardware-proven clean-exit baseline is
[`T1.1.0-40`](T1.1.0-40/README.md).

Confirmed on a physical Commodore 1541:

- ROM selection and switching works.
- The first clean-exit attempt after a physical drive start returns the C64 to
  BASIC `READY.`.
- A physical-disk directory can be read immediately without resetting the C64
  or power-cycling the 1541.
- Two consecutive Q-Quit runs completed without ROM corruption.

Continue development with the next unused test identifier. Do not renumber the
retained tests because their identifiers are tied to hardware photographs,
checksums, and Git history.
