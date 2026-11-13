---
sidebar_label: 'Task VMWare - Delete VM'
hide_title: 'true'
---

## Task VMWare - Delete VM

The VMWare - Delete VM Task deletes a virtual machine, using a VMWare Connection or VMware Workstation on the VisualCron Server computer.

![Connection sub tab of the VMWare Delete VM Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Delete%20VM.png)

:::warning

The virtual machine is deleted without asking for confirmation. With a "vSphere" or "vSphere 7" Connection, its files are deleted from the datastore as well.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task works with every _Authentication type_ of the VMWare Connection; see [Connection - VMWare](../../connection-vmware).

### Connection sub tab

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

Each time the Task opens, _Remote VMWare server_ is selected, even if the Task was saved with _Local VMWare workstation_. Check the selection before you click _OK_.

### Output and errors

When VMware reports an error, the Task fails.
