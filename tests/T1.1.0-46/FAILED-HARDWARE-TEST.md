# Failed hardware test

T46 added DOS `I` before the OneROM service upload. After Q-Quit,
`LOAD"$",8` returned `FILE NOT FOUND` both when the selector was loaded from
the same physical 1541 and when its standalone PRG was launched by the
1541 Ultimate.

In both cases, manually entering:

```basic
OPEN15,8,15,"I":CLOSE15
LOAD"$",8
```

restored directory access. This identifies stale post-Q DOS/disk state and
shows that pre-upload initialization is not the solution.
