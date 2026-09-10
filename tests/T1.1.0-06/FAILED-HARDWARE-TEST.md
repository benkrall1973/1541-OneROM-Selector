# T1.1.0-06 failed hardware testing

Do not use this build.

On 2026-09-10, terminal `LOAD_AND_EXIT` completed without a reported RBCP error, but reloading the active RAM slot left the 1541 running a corrupted ROM image with a blinking red OneROM indication. A power cycle restored normal boot and directory access.

T1.1.0-07 instead loads the same flash ROM into the inactive RAM slot, verifies that operation, and only then switches to the completed copy.
