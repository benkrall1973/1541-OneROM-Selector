# T1.1.0-16 Hardware Result

The checkpoint reported protocol `0.1.2`, RAM count 16, active RAM 1, boot RAM
13, and boot flash 255. The flash value is a host-side NUL-decoding artifact:
flash slot zero became an empty BASIC string while the default remained 255.

The safety gate sent no terminal command. Because the command-response session
remained open, the active RAM ROM stayed displaced until power cycle.
T1.1.0-17 initializes boot response fields to zero and supersedes T16.
