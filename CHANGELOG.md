# Changelog

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
