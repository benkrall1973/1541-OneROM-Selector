# Interpretation

Before T36, the physical and VICE PRGs were generated from the same source with only `SM` changed from zero to one. Commodore BASIC stores unreachable lines in the PRG, so the physical file still carried every simulator message, mock response, branch, and delay routine.

T36 removes those lines from the hardware source rather than merely bypassing them. This reduces disk load size while leaving the executable physical path byte-for-byte equivalent at the BASIC statement level, apart from removed simulation conditions that could never be true when `SM=0`.

The repository still contains complete source for both variants: T35 for VICE simulation and T36 for physical hardware.
