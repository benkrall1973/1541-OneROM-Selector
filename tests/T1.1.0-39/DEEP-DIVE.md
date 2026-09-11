# T38 failure interpretation

T38 succeeded once after a physical restart, failed on its second run, and later left the OneROM LED flashing. Its immediate `CLOSE15` after `LOAD_AND_EXIT` repeated the behavior T20 had already identified as unsafe.

The v0.7.2 host-control source confirms that `LOAD_AND_EXIT` restores the complete ROM image and silently leaves command-response mode. The host must not poll or write the former response channel afterward. Therefore T39 performs only local cleanup after the terminal command.

Because a physical drive reboot consistently restores directory access while DOS `I` did not, T39 then tries a standard DOS `UJ` soft reset over a newly opened channel. The reset channel is abandoned locally rather than closed after the drive resets.
