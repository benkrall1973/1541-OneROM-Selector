# T1.1.0-16 Test Design

## Hardware evidence from T15

After the physical OneROM firmware and automatically selected plugins were
updated, T15 displayed `255.1.2`. RBCP protocol versions are four response-data
bytes `{major, minor, patch, reserved}` and the current plugin returns
`{0,1,2,0}`.

On Commodore BASIC, `GET#` represents a received NUL byte as an empty string.
T15 initialized the major field to 255 and changed it only when `LEN(A$)` was
nonzero. Thus the display was a host-side decoding artifact, not an old plugin.

## T16 change

The protocol fields now initialize to zero before optional `ASC()` conversion:

```basic
PV=0:PN=0:PP=0
```

No RBCP framing or terminal-command logic changed. Once `0.1.2` passes the
gate, the selector requests `GET_BOOT_SLOT_INFO` and stops at the guarded
checkpoint. The tester must photograph that checkpoint before authorizing
`LOAD_AND_EXIT` with RETURN.
