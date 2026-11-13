---
sidebar_label: 'Task VMWare - Unregister VM'
hide_title: 'true'
---

## Task VMWare - Unregister VM

The VMWare - Unregister VM Task removes a virtual machine from the inventory of the VMware server, using a VMWare Connection. The files of the virtual machine are not deleted.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task works with every _Authentication type_ of the VMWare Connection; see [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Unregister VM Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Unregister%20VM.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

### Output and errors

When VMware reports an error, the Task fails.
