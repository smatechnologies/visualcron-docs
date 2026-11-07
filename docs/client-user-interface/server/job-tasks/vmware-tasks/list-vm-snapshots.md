---
sidebar_label: 'Task VMWare - List VM Snapshots'
hide_title: 'true'
---

## Task VMWare - List VM Snapshots

The VMWare - List VM Snapshots Task lists the snapshots of a virtual machine, using a VMWare Connection or VMware Workstation on the VisualCron Server computer.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix" or "vSphere"; "vSphere 7" does not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare List snapshots Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/List%20snapshots.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

### Output and errors

The output is the list of snapshots. With a "Vix" Connection or _Local VMWare workstation_, it is XML, with each snapshot's name, description and power state nested under its parent snapshot. With a "vSphere" Connection, it is plain text, one snapshot name per line.

:::warning

With a "vSphere" Connection, if the virtual machine is not found, the output is empty, and the Task reports success.

:::

Otherwise, when VMware reports an error, the Task fails.
