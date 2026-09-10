# Hardware result and correction

T1.1.0-19 succeeded at the OneROM level: after resetting only the C64, the unchanged 1541 read a directory normally. This proves the drive was not corrupted and isolates the visible hang to the C64-side `CLOSE15` instruction.

Because `LOAD_AND_EXIT` is terminal, no further operation should be directed at the former RBCP command channel. T1.1.0-20 therefore abandons that logical file locally and returns BASIC's channels to their defaults without asking the drive to close anything.
