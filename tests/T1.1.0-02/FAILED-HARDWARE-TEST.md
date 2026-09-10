# T1.1.0-02 failed hardware testing

Do not use this build.

On 2026-09-10, the Q cleanup path failed on a physical Commodore 1541 with OneROM v0.7.2. The program displayed `CLEANUP FAILED - ERROR 1` and the drive required a power cycle.

Code review found that the restore loop preserved its index in `$F8` before an RBCP call but failed to reload the 6502 X register afterward. Development continues in T1.1.0-03.
