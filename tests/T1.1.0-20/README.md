# T1.1.0-20 clean-exit return test

T1.1.0-19 proved that OneROM v0.7.2 `LOAD_AND_EXIT 1,0` cleanly restores the drive. Its only remaining problem was the C64 hanging while attempting `CLOSE15` after OneROM had already terminated the RBCP session.

T1.1.0-20 performs only local C64 cleanup after the terminal command: it calls KERNAL `CLRCHN`, clears the KERNAL logical-file count, and ends normally.

## Test

1. Power-cycle the drive and verify a directory read.
2. Run `ONEROMT11020`, make no menu change, and press Q.
3. Confirm the mapping is valid and press RETURN once.
4. Do not press RUN/STOP.
5. Expected: `CLEAN EXIT COMPLETE`, followed automatically by the BASIC `READY.` prompt.
6. Read the directory twice without resetting the C64 or power-cycling the drive.

Report the final screen, both directory results, and LED state.

