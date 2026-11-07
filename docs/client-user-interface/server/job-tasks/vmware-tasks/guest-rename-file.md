---
sidebar_label: 'Task VMWare - [Guest] Rename File'
hide_title: 'true'
---

## Task VMWare - [Guest] Rename File

The VMWare - [Guest] Rename File Task renames a file in the guest operating system.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix"; "vSphere" and "vSphere 7" do not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Guest Rename file Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Rename%20File.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

_Guest OS Credentials_ is required: select the Credential of a user account inside the virtual machine. Before it signs in, the Task waits up to 60 seconds for VMware Tools to run in the guest, whatever the timeout says. It signs in with the VMware option that requires an interactive session, so that user must be signed in to the guest desktop.

### VM Task settings sub tab

![VM Task settings sub tab of the VMWare Guest Rename file Task, with the Old file path and New file path fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Rename%20File%20Settings.png)

- _Old file path_: the full path of the file in the guest. Variables are replaced in this field
- _New file path_: the new full path of the file in the guest. Variables are replaced in this field

The _File_ icons open a file browser on the computer that runs the Client, not in the guest.

### Output and errors

When VMware reports an error, the Task fails.
