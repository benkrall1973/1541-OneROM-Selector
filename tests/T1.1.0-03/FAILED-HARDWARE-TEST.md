# T1.1.0-03 failed hardware testing

Do not use this build.

On 2026-09-10, it produced the same `CLEANUP FAILED - ERROR 1` result as T1.1.0-02 on a physical Commodore 1541 with OneROM v0.7.2.

Further review identified the primary fault: both builds copied the 187-byte backup to drive RAM `$0610-$06CA`, overwriting part of the resident RBCP implementation before executing cleanup. Development continues with a non-overlapping architecture in T1.1.0-04.
