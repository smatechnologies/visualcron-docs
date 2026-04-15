---
sidebar_label: 'Task Virtual Server - List VM Machines'
hide_title: 'true'
---

## Task Virtual Server - List VM Machines

The Virtual Server - List VM machines Task retrieves a list of all virtual machines on a specific virtual machine.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Virtual%20Server%20Tasks/List%20VM%20Machines.png)

**Remote VMWare server / Local VMWare workstation**

This task requires a remote VMWare server connection. The _Local VMWare workstation_ option is disabled.

**Connection**

Select the VMWare connection to use for the remote server.

**Server VMX path**

The path to list virtual machines from on the remote server. Click the _Refresh_ button to populate the list from the selected connection.

**Timeout in seconds**

The number of seconds to wait before timing out the operation. Minimum is 1, maximum is 36000, default is 180. Note that a Timeout tab setting on the task overrides this value.

**VM listing status filter**

Select which VM power states to include in the results. Check one or more of the following:

* _Powered on_ - includes virtual machines that are running
* _Powered off_ - includes virtual machines that are powered off
* _Suspended_ - includes virtual machines that are suspended
* _Stuck_ - includes virtual machines that are stuck
* _Unknown_ - includes virtual machines with an unknown status
