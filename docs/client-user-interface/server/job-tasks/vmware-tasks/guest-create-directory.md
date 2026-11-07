---
sidebar_label: 'Task VMWare - [Guest] Create Directory'
hide_title: 'true'
---

## Task VMWare - [Guest] Create Directory

The VMWare - [Guest] Create Directory Task creates a folder in the guest operating system.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix"; "vSphere" and "vSphere 7" do not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Guest Create directory Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Create%20Directory.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

_Guest OS Credentials_ is required: select the Credential of a user account inside the virtual machine. Before it signs in, the Task waits up to 60 seconds for VMware Tools to run in the guest, whatever the timeout says. It signs in with the VMware option that requires an interactive session, so that user must be signed in to the guest desktop.

### VM Task settings sub tab

![Connection sub tab of the VMWare Guest Create directory Task, shown again in place of the VM Task settings sub tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Create%20Directory.png)

- _Folder path_: the full path of the folder to create in the guest. Variables are replaced in this field

### Output and errors

When VMware reports an error, the Task fails.
