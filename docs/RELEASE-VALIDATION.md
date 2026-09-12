# Release Validation — v1.1.0

## Proven baseline

The production source was derived from hardware-tested T1.1.0-47. A source comparison confirms that only the selector and firmware title strings changed.

Hardware testing covered physical-floppy and 1541 Ultimate launches, ROM switching, Save/Reboot, repeated Q-Quit runs, repeated directory reads after quitting, and repeated selector runs without resetting or power-cycling.

## Mechanical checks

- BASIC source: `src/1541-OneROM-Selector-v1.1.0.bas`
- Tokenized PRG: `bin/1541-OneROM-Selector-v1.1.0.PRG`
- Disk image: `1541-OneROM-Selector-v1.1.0.d64`
- D64 directory filename: `ONEROMV110`
- The D64's embedded PRG is byte-for-byte identical to the standalone PRG.
- The BASIC source contains 324 ordered, unique line numbers.
- The longest approximate tokenized line record remains below the 255-byte BASIC limit.
- Both release configuration files parse as valid JSON and pass repository label-placement validation.
- The universal v1.1.0 bootloader is byte-for-byte identical to the proven universal v1.0.0 bootloader.
- `scripts/validate_repository.py` passes.

## Runtime dependencies

- OneROM firmware v0.7.2
- RBCP protocol v0.1.2 or later
- USB and host-control plugins resolved by the current OneROM CLI

## Checksums

`SHA256SUMS.txt` covers the distributed repository files other than itself. Text checksums describe canonical LF content; the repository validator accepts equivalent CRLF working-tree files on Windows.
