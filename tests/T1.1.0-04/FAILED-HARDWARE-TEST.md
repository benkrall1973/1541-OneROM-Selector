# T1.1.0-04 failed hardware testing

Do not use this build.

On 2026-09-10, a physical 1541 with OneROM v0.7.2 reported `ACTIVE SLOT QUERY FAILED / ERROR 1 / SLOT 187`.

Error 1 means the query received no response token. The query helper failed to reset/knock and enter command-response mode before issuing `GET_RAM_SLOT_INFO_ALL`. The non-overlapping C64-side backup architecture remains in T1.1.0-05 with the required session-entry sequence added.
