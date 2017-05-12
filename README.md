# dkms_e1000e_bootfix

DKMS package applying fixes to Intel e1000e kernel module.

Applies patch https://patchwork.kernel.org/patch/9254367/ to
Linux kernel v4.10.14 e1000e module to workaround 
"e1000e: probe of 0000:00:19.0 failed with error -3"
errors on cold boot of Intel 82578DC Gigabit Ethernet PHY for some 
affected hardware/BIOS configurations.
