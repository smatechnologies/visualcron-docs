---
sidebar_label: 'Task VMWare - Clone VM'
hide_title: 'true'
---

## Task VMWare - Clone VM

The VMWare - Clone VM Task clones a virtual machine, using VMware Workstation on the VisualCron Server computer or a VMWare Connection.

![Connection sub tab of the VMWare Clone VM Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Clone%20VM.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task works with every _Authentication type_ of the VMWare Connection; see [Connection - VMWare](../../connection-vmware).

### Connection sub tab

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

Each time the Task opens, _Local VMWare workstation_ is selected, even if the Task was saved with _Remote VMWare server_. Check the selection before you click _OK_.

### VM Task settings sub tab

![VM Task settings sub tab of the VMWare Clone VM Task, with the Snapshot name and Cloned file path fields and the Full clone check box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Clone%20VM%20settings.png)

- _Snapshot name (optional - otherwise using latest)_: the snapshot to clone from. Leave it empty to clone the current state. If no snapshot has this name, the current state is cloned without an error. With a "vSphere" Connection, this field is not used, and the clone is always taken from the current state. Variables are replaced in this field
- _Cloned file path_: with _Local VMWare workstation_ or a "Vix" Connection, the path of the ".vmx" file for the clone. With a "vSphere" or "vSphere 7" Connection, the name of the new virtual machine. The _File_ icon opens a file browser on the computer that runs the Client. Variables are replaced in this field
- _Full clone_: create a full, independent copy. When not checked (the default), the Task creates a linked clone, which shares virtual disks with the parent virtual machine and uses less disk space as long as the two do not change much. With a "vSphere" or "vSphere 7" Connection, the clone is always a full clone, whatever this check box says

The _Refresh_ icon next to _Snapshot name (optional - otherwise using latest)_ does not fill the list in this version; type the snapshot name.

### Output and errors

When VMware reports an error, the Task fails.
