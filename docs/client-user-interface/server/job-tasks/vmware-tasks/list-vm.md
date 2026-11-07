---
sidebar_label: 'Task VMWare - List VM'
hide_title: 'true'
---

## Task VMWare - List VM

The VMWare - List VM Task lists the virtual machines on a VMware server, using a VMWare Connection.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task works with every _Authentication type_ of the VMWare Connection; see [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare List VM Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/List%20VM.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

Only _Remote VMWare server_ can be used, and _Server VMX path_ is not used.

### VM Task settings sub tab

![VM Task settings sub tab of the VMWare List VM Task, with the VM listing status filter check boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/List%20VM%20Settings.png)

- _VM listing status filter_: the states to include. Check one or more of "Powered on", "Powered off", "Suspended", "Stuck" and "Unknown". None is checked by default, and with none checked the list is empty. With a "vSphere" or "vSphere 7" Connection, "Stuck" and "Unknown" match nothing

### Output and errors

The output is an XML list of the matching virtual machines, with each one's path and whether it is powered on.

:::warning

With a "vSphere 7" Connection, an error from vCenter after sign-in gives an empty list, and the Task reports success.

:::

Otherwise, when VMware reports an error, the Task fails.
