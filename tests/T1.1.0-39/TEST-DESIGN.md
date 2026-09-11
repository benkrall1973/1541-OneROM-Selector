# Test design

T39 corrects the post-`LOAD_AND_EXIT` cleanup based on both hardware evidence and the OneROM v0.7.2 implementation. A silent terminal command must not be followed by a close or another RBCP operation against its former channel.

The new sequence abandons the former channel locally, waits 180 jiffies, sends DOS `UJ` through a fresh command channel, abandons that channel locally because the reset invalidates it, waits another 180 jiffies, and clears the screen.

Fixed text is staged in an off-screen buffer at `$C100` and copied to screen/color RAM by a 19-byte routine at `$C000`. This removes visible BASIC-loop rendering without changing selection redraw behavior.
