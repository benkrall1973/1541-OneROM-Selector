# Failed hardware test

T39 corrupted the served ROM after Q. The delayed DOS `UJ` experiment did not repair the underlying issue and must not be reused.

Comparison with T21 and OneROM v0.7.2 identified the actual distinction: T21 reloaded the active RAM slot containing the RBCP back-channel, while T22 through T39 reloaded the separate boot RAM slot. That left the displaced bytes in the actively served ROM image unrestored.
