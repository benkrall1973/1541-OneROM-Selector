# Test design

The proven OneROM command and mapping from T1.1.0-19 are unchanged. The sole functional change is after `M-E` launches the resident helper:

- Removed `CLOSE15`, because it starts another IEC operation after OneROM has terminated the session.
- Added `SYS 65484` (`CLRCHN`) to restore local C64 input/output channels.
- Added `POKE 152,0` to clear the KERNAL logical-file table locally.
- The program then prints completion and executes `END` so BASIC displays `READY.`.

