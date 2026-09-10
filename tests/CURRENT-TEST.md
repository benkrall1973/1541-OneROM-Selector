# Current test candidate

The current OneROM v0.7.2 test candidate is
[`T1.1.0-31`](T1.1.0-31/README.md).

The latest hardware-proven baseline remains
[`T1.1.0-21`](T1.1.0-21/README.md) until T22 completes physical testing.

Confirmed on a physical Commodore 1541:

- ROM selection and switching works.
- The first clean-exit attempt after a physical drive start returns the C64 to
  BASIC `READY.`.
- A physical-disk directory can be read immediately without resetting the C64
  or power-cycling the 1541.
- A second invocation may report current RAM `255`; its guard rejects that
  state and sends no terminal command.

Continue development with the next unused test identifier. Do not renumber the
retained tests because their identifiers are tied to hardware photographs,
checksums, and Git history.
