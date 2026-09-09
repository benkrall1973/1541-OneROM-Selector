# Changelog

## v1.1.0 - In development

- Targets OneROM firmware v0.7.2, USB plugin v0.3.0, and host-control plugin v0.1.3.
- Corrects the multi-chip label rule: the friendly label belongs on `chips[0]`.
- Plans an explicit quit-without-saving path that avoids selection and custom-name NV writes.
- Removes the pre-initialization warning screen and delay once clean quit is hardware-proven.
- Changes the program credit to `BUILT WITH CHATGPT`.
- Requires unique temporary versions and matching source for every test build.
- Adds device-8/device-9 SAVE and QUIT regression testing.
- Keeps the v1.0.0 release artifacts unchanged on `main`.

## v1.0.0 - 2026-08-26

First cleaned public-release baseline.

- Established the selector and universal bootloader as v1.0.0.
- Publishes the tested universal bootloader plus a verified generic base bootloader retained for development/reference; older socket-specific bootloader variants are excluded.
- Added a ready-to-run D64 containing the release PRG.
- Sanitized upper/lower socket config examples and removed private/commercial ROM filenames.
- Updated config terminology to current OneROM `chip_sets` / `chips` names while preserving tested ordering and label behavior.
- Kept every `label` as the final member of its upper `$E000-$FFFF` ROM object.
- Bundled the exact tested USB v0.2.1 and host-control v0.1.2 plugin binaries.
- Added MIT licensing for the project plus OneROM/RBCP third-party notices.
- Removed stale internal handoff/future-plan documents and unused RBCP reference-source files from the public release.
- Corrected documentation for IEC 8-11 polling, the pre-initialization safety screen, lower-socket fallback, and the actual release filenames.
- Added/regenerated SHA-256 checksums for all release files.
