---
sidebar_label: 'Task VMWare - Stop VM'
hide_title: 'true'
---

## Task VMWare - Stop VM

The VMWare - Stop VM Task stops (powers off) a virtual machine.

**Stop VM > Connection** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Stop%20VM.png)

The Connection sub tab is the same for all VMWare Task types. See [Start VM](start-vm) for details.

**Stop VM > VM Task settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Stop%20VM%20settings.png)

**Stop type**

Specifies how the virtual machine is powered off. Available options:

* _Hard_ - powers off the virtual machine immediately, equivalent to pulling the power plug
* _Soft_ - asks the guest operating system to shut down cleanly through VMWare Tools
* _Trysoft_ - tries a soft shutdown first and falls back to a hard power off if the soft shutdown does not succeed
