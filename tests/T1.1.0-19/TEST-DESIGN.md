# Test design

T1.1.0-18 established that the selector menu uses a one-based active choice while OneROM's flash slot is zero-based. T1.1.0-19 therefore computes `candidate flash = menu choice - 1`.

Before transmission it validates:

- RBCP protocol is available and returned usable values.
- RAM count and active RAM are in range.
- Candidate flash is in range.
- An unchanged menu maps back to the reported boot flash.
- No required value contains the reserved diagnostic sentinel `$AA`.

After the user presses RETURN, the resident drive helper sends RBCP control command `$05` (`LOAD_AND_EXIT`) with the current active RAM and computed flash slot. The program does not poll OneROM afterward because this command terminates the active RBCP session.

This test deliberately does not restore a ROM image or send a separate DOS initialization command.

