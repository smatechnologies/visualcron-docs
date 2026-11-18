---
sidebar_label: 'Task VMWare - [Guest] Copy File'
hide_title: 'true'
---

## Task VMWare - [Guest] Copy File

The VMWare - [Guest] Copy File Task copies files between the guest operating system and the VisualCron Server computer.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix"; "vSphere" and "vSphere 7" do not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Guest Copy file(s) Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Copy%20Files.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

_Guest OS Credentials_ is required: select the Credential of a user account inside the virtual machine. Before it signs in, the Task waits up to 60 seconds for VMware Tools to run in the guest, whatever the timeout says. It signs in with the VMware option that requires an interactive session, so that user must be signed in to the guest desktop.

### VM Task settings sub tab

![VM Task settings sub tab of the VMWare Guest Copy file(s) Task, with the Source folder, Source file(mask) and Destination folder fields and the From guest to host check box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Copy%20Files%20Settings.png)

- _Source folder_: the folder to copy from: in the guest when _From guest to host_ is checked, otherwise on the VisualCron Server computer. The _Folder_ icon is turned off. Variables are replaced in this field
- _Source file(mask)_: a file name or wildcard mask, "*" by default. The _File_ icon opens a file browser on the computer that runs the Client and enters only the file name. Variables are replaced in this field
- _From guest to host_: when checked (the default), files are copied from the guest to the VisualCron Server computer. When not checked, files are copied from the VisualCron Server computer to the guest
- _Destination folder_: the folder to copy to. The _Folder_ icon is turned off. Variables are replaced in this field

:::warning

End _Destination folder_ with a backslash, for example `C:\Data\Out\`. The Task builds each target path from the part of _Destination folder_ before its last backslash, so without the trailing backslash the files are copied to the parent folder (for `C:\Data\Out`, to `C:\Data`).

:::

### Output and errors

When VMware reports an error, the Task fails.
