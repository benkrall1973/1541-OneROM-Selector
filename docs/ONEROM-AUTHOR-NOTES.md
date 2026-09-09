# OneROM Author Notes for v1.1.0

These points are project requirements derived from direct feedback from the OneROM author.

- OneROM v0.7.2 is merged into the official OneROM `main` branch.
- The current v1.0.0 selector was successfully tested on a real 1541 using the in-development v0.7.2 firmware, with OneROM in the lower socket at IEC device 8.
- For a multi-ROM slot, RBCP returns the label from `chips[0]`. Documentation or configurations that attach the friendly label according to physical upper/lower address are incorrect.
- The selector source queries slot metadata and uses the label returned by RBCP; it does not contain a separate choice of the physical upper ROM label.
- The idle menu needs an obvious exit/cancel option that makes no persistent change.
- Cancel must first close/clean up communication. It must not save NV data or issue a ROM switch.
- Firmware v0.7.2 does not make mid-transaction interruption safe. Cancel is an idle-menu operation, not an abort mechanism for an active RBCP/DOS transaction.
- The warning screen and timer may be removed only when the clean idle-menu cancel path is available and hardware-proven.
- OneROM ORA/plugin APIs are considered stable and public unless marked deprecated or expected to become deprecated.
- Preserve the existing selector layout and colors for the first test.
- Use the credit text `BUILT WITH CHATGPT`.
- OneROM test-fixture and full-CI guidance used by the separate 1541HUD project is outside the scope of this selector repository.
