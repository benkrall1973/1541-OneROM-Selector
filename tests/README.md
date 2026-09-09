# Test Builds

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
