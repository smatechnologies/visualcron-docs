---
sidebar_label: 'Task VMWare - Create VM Snapshot'
hide_title: 'true'
---

## Task VMWare - Create VM Snapshot

The VMWare - Create VM Snapshot Task creates a snapshot from the current state of a virtual machine, using a VMWare Connection or VMware Workstation on the VisualCron Server computer.

![Connection sub tab of the VMWare Create snapshot Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Create%20Snapshot.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix" or "vSphere"; "vSphere 7" does not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

### VM Task settings sub tab

![VM Task settings sub tab of the VMWare Create snapshot Task, with the Name and Description fields and the Include memory check box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Create%20Snapshot%20settings.png)

- _Name_: the name of the snapshot. Variables are replaced in this field
- _Description_: a description of the snapshot. Variables are replaced in this field
- _Include memory_: capture the memory of a running virtual machine as well. Checked by default

### Output and errors

When VMware reports an error, the Task fails.
