# OneROM GET_BOOT_SLOT_INFO Failure Analysis

## T16 update

The physical OneROM has now been updated and reports RBCP `0.1.2`. T15 showed
this as `255.1.2` because Commodore BASIC returned the zero major-version byte
as an empty string while the diagnostic default remained 255. T16 corrects
that host-side display and gating bug. The earlier `0.1.1` result was from the
previous physical firmware/plugin installation.

## Finding

T14’s `BOOT QUERY FAILED 3` cannot be explained by missing boot metadata in the current OneROM host-control implementation. The handler always writes a four-byte response and returns success. Unknown boot metadata is represented by flash slot `$FF` and RAM slot `$FF`.^1

The failure therefore narrows to two realistic cases:

1. the installed host-control plugin predates `GET_BOOT_SLOT_INFO` and treats command `$08` as unknown; or
2. the helper did not place `$08` on the command stream as intended.

The removed pre-v0.7.2 T1.1.0-15 diagnostic distinguished these states by preserving the reported RBCP version and raw response header. It remains available in Git history only.

## Current implementation behavior

The current host-control command dispatcher assigns read command `$08` to `exec_get_boot_slot_info()`. That function constructs `{boot_flash_slot, boot_ram_slot, 0, 0}`, writes it at response-data offset zero, logs both slot numbers and returns `true` unconditionally.^1

At plugin initialization, both boot fields default to `$FF`. Firmware v0.7.2 metadata calls populate them when the firmware knows the boot flash and active RAM slots. An older firmware or unavailable metadata leaves `$FF,$FF`, but the query itself still succeeds.^1

## Protocol compatibility

`GET_BOOT_SLOT_INFO` and `LOAD_AND_EXIT` were added in RBCP 0.1.2. During the 0.x series, the minor version must match and the device patch version must be at least the version targeted by the host. A 0.1.2 host can accept 0.1.2 or a later 0.1 patch, but must not assume the command exists on 0.1.1.^2

An unknown command can consume a different number of bytes than a newer host expects. The reference implementation consequently checks protocol version before using 0.1.2 commands.^3 T14 performed that check only at the final safety gate, after it had already issued `$08`. T15 corrects the order.

## Meaning of wrapper stage 3

The selector’s resident helper uses a three-stage result convention. Stage 3 means the command was framed and observed through the token/progress process, but the response status was failed. It is not a detailed OneROM error enumeration.

The raw header is therefore more useful than stage 3 alone. The eight bytes identify the last command, token, progress, response and reserved fields. T15 captures them immediately after failure, before another RBCP command can overwrite the evidence.

## Test decision tree

- If the reported protocol is older than 0.1.2, T15 does not send `$08`. The installed host-control plugin must be updated.
- If the protocol reports 0.1.2+ but the raw last-command bytes do not identify read command `$08`, the C64 helper or its self-modifying command byte is wrong.
- If the header identifies read `$08` and reports failure, the installed plugin behavior differs from current upstream source. The raw header and installed plugin version should be sent to the OneROM author.
- If `$08` succeeds with `$FF,$FF`, the command exists but firmware boot metadata is unavailable; `LOAD_AND_EXIT` must not be attempted.
- If `$08` returns valid slots, T15 can proceed to its existing guarded terminal checkpoint.

## Safety

Neither failure path sends a terminal command. However, closing Commodore DOS channel 15 does not leave RBCP command-response mode, so the drive must be power-cycled after the screen is photographed. A BASIC `READY` prompt is not proof that the served ROM is clean.

## Sources

1. Piers Finlayson, “[OneROM host-control implementation](https://github.com/piersfinlayson/one-rom/blob/main/plugins/user/host-control/src/host_control_main.c),” command definitions, boot metadata and `exec_get_boot_slot_info()`.
2. Piers Finlayson, “[ROM Bus Control Protocol v0.1.2](https://github.com/piersfinlayson/rom-bus-control-protocol/blob/main/spec/rbcp.md),” version compatibility, response header and read command `$08`.
3. Piers Finlayson, “[RBCP x86 reference host](https://github.com/piersfinlayson/rom-bus-control-protocol/tree/main/reference/host/x86/romsel),” protocol gating for 0.1.2 commands.
