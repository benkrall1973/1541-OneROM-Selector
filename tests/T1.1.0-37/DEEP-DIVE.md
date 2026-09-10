# Interface safety change

IEC Select is still entirely on the C64 side. Q can therefore clear the screen and end the BASIC program without issuing an RBCP command or closing a drive channel that has not yet been opened.

LOAD is different: it uploads and executes drive-resident software and performs the OneROM discovery and service setup. RUN/STOP can strand that transaction, so T37 explicitly warns against interruption instead of pretending Q can safely cancel it.

The warning is drawn at screen row 22, with row 23 intentionally unused and the standard LOAD/credit footer on row 24.
