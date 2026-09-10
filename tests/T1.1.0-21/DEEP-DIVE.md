# Interpretation

T19's LED behavior was not proof of recovery because directory access occurred only after a full 1541 Ultimate/C64 reboot. T20 demonstrated that local C64 cleanup reaches `READY.`, but correctly aborted when OneROM returned current RAM `255`. T21 repeats the guarded command from a known fresh-drive state and separates the final visible stages so a hang can be located precisely.
