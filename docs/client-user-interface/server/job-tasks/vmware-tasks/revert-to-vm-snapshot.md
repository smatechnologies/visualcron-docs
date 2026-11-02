---
sidebar_label: 'Task VMWare - Revert to VM Snapshot'
hide_title: 'true'
---

## Task VMWare - Revert to VM Snapshot

The VMWare - Revert to VM Snapshot Task returns a virtual machine to the state of a snapshot, using a VMWare Connection or VMware Workstation on the VisualCron Server computer.

:::warning

Reverting replaces the current state of the virtual machine with the snapshot, without asking for confirmation. Changes made since the snapshot are lost unless you create a snapshot first.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix" or "vSphere"; "vSphere 7" does not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Revert to snapshot Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Revert%20to%20Snapshot.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

### VM Task settings sub tab

![VM Task settings sub tab of the VMWare Revert to snapshot Task, with the Snapshot name field](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Revert%20to%20Snapshot%20settings.png)

- _Snapshot name_: the name of the snapshot to revert to. Variables are replaced in this field

The _Refresh_ icon next to the field does not fill the list in this version; type the snapshot name.

### Output and errors

If the snapshot is not found, the Task fails. When VMware reports an error, the Task fails.
