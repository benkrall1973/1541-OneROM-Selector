# Test Builds

## Active v0.7.2 test history

The active test collection begins with `T1.1.0-16`, the first test where the
physical OneROM returned the real RBCP v0.1.2 protocol response after its
firmware was upgraded to OneROM v0.7.2.

`T1.1.0-02` through `T1.1.0-15` were removed from the active tree because the
physical OneROM was still running older firmware. Those results cannot be used
to evaluate the v0.7.2 functions. The deleted files remain recoverable from Git
history if they are ever needed for historical investigation.

`T1.1.0-21` is the current hardware-proven baseline. On a fresh physical-drive
start it has successfully changed ROMs, exited to BASIC `READY.`, and allowed
an immediate directory read without resetting either machine. A second run can
return current RAM `255`; the safety check rejects that state without sending a
terminal command.

See [`CURRENT-TEST.md`](CURRENT-TEST.md) for the concise current-state pointer.

Retained tests:

- `T1.1.0-16` through `T1.1.0-20`: v0.7.2 diagnostics and development steps.
- `T1.1.0-21`: hardware-proven first-run clean-exit baseline.
- `T1.1.0-22`: current candidate; uses the boot RAM/flash pair returned by
  `GET_BOOT_SLOT_INFO` to test clean exit on repeated runs.
- `T1.1.0-23`: adds a deterministic VICE simulation and corrects the
  lower-socket search/success messages.
- `T1.1.0-24`: removes custom ROM-name editing and its NV helpers, reducing
  the tokenized PRG by 2,720 bytes while retaining `chip[0]` labels.

## Packaging rules

Every test must use a unique directory such as `tests/T1.1.0-01/`.

Required contents:

```text
tests/T1.1.0-01/
├── README.md
├── source/
│   └── 1541-OneROM-Selector-T1.1.0-01.bas
├── bin/
│   └── 1541-OneROM-Selector-T1.1.0-01.PRG
├── disk/
│   └── 1541-OneROM-Selector-T1.1.0-01.d64
└── SHA256SUMS.txt
```

Copy `TEST-RESULTS-TEMPLATE.md` into the test directory as `README.md` and complete it during hardware testing. Never reuse a test version number, even when a build fails.
