# Experimental Development Warning

The `develop-v1.1.0` branch and all `T1.1.0-XX` builds are test material, not stable releases.

- Stable v1.0.0 remains on `main`.
- Do not overwrite a known-good setup unless you can restore it.
- Record the exact OneROM firmware, plugin versions, drive address, and socket for every test.
- Keep each PRG with its exact BASIC source, D64, test notes, and checksums.
- A successful VICE run does not replace testing on a physical 1541.
- If a test hangs or leaves the drive unresponsive, record the stage and LED state before resetting or power cycling.

No development build should be promoted to a release until the hardware checklist passes.
