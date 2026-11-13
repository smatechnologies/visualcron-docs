---
sidebar_label: 'Task VMWare - [Guest] Delete File'
hide_title: 'true'
---

## Task VMWare - [Guest] Delete File

The VMWare - [Guest] Delete File Task deletes one or more files in the guest operating system.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix"; "vSphere" and "vSphere 7" do not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Guest Delete file(s) Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Delete%20Files.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

_Guest OS Credentials_ is required: select the Credential of a user account inside the virtual machine. Before it signs in, the Task waits up to 60 seconds for VMware Tools to run in the guest, whatever the timeout says. It signs in with the VMware option that requires an interactive session, so that user must be signed in to the guest desktop.

### VM Task settings sub tab

![VM Task settings sub tab of the VMWare Guest Delete file(s) Task, with the Source folder and Source file(mask) fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Delete%20Files%20Settings.png)

- _Source folder_: the folder in the guest to delete files from. Variables are replaced in this field
- _Source file(mask)_: a file name or mask, "*" by default. The mask uses Visual Basic pattern matching, not case-sensitive: `*` matches any characters, `?` one character, `#` one digit, and `[abc]` one of the listed characters. Variables are replaced in this field

:::warning

With the default mask "*", every file in _Source folder_ is deleted. If _Source folder_ has a subfolder that matches the mask, the Task can fail part way, after it has deleted some files.

:::

### Output and errors

When VMware reports an error, the Task fails.
