---
sidebar_label: 'Task VMWare - Reset VM'
hide_title: 'true'
---

## Task VMWare - Reset VM

The VMWare - Reset VM Task resets a virtual machine.

**Reset VM > Connection** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Reset%20VM.png)

The Connection sub tab is the same for all VMWare Task types. See [Start VM](start-vm) for details.

**Reset VM > VM Task settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Reset%20VM%20Settings.png)

**Stop type**

Specifies how the virtual machine is powered off as part of the reset. Available options:

* _Hard_ - powers off the virtual machine immediately, equivalent to pulling the power plug
* _Soft_ - asks the guest operating system to shut down cleanly through VMWare Tools
* _Trysoft_ - tries a soft shutdown first and falls back to a hard power off if the soft shutdown does not succeed
