---
sidebar_label: 'Task VMWare - Suspend VM'
hide_title: 'true'
---

## Task VMWare - Suspend VM

The VMWare - Suspend VM Task suspends a virtual machine, using a VMWare Connection or VMware Workstation on the VisualCron Server computer. VMware saves the state of the virtual machine and stops it.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task works with every _Authentication type_ of the VMWare Connection; see [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Suspend VM Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Suspend%20VM.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

### Output and errors

When VMware reports an error, the Task fails. To run the virtual machine again, use the [Start VM](start-vm) Task.
