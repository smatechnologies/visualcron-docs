---
sidebar_label: 'Task VMWare - Delete VM Snapshot'
hide_title: 'true'
---

## Task VMWare - Delete VM Snapshot

The VMWare - Delete VM Snapshot Task deletes a snapshot of a virtual machine, using a VMWare Connection or VMware Workstation on the VisualCron Server computer.

![Connection sub tab of the VMWare Delete snapshot Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Delete%20Snapshot.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix" or "vSphere"; "vSphere 7" does not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

### VM Task settings sub tab

![VM Task settings sub tab of the VMWare Delete snapshot Task, with the Snapshot name field](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Delete%20Snapshot%20settings.png)

- _Snapshot name_: the name of the snapshot to delete. Variables are replaced in this field

The _Refresh_ icon next to the field does not fill the list in this version; type the snapshot name.

:::warning

The snapshot is deleted without asking for confirmation.

:::

### Output and errors

If the snapshot is not found, the Task fails.

:::warning

With a "Vix" Connection or _Local VMWare workstation_, the Task starts the deletion but does not wait for VMware to finish it. An error from the deletion is not reported, and the Task reports success. To confirm the result, run the [List VM Snapshots](list-vm-snapshots) Task afterward.

:::
