---
sidebar_label: 'Task VMWare - [Guest] Capture Screen'
hide_title: 'true'
---

## Task VMWare - [Guest] Capture Screen

The VMWare - [Guest] Capture Screen Task takes a screenshot of the guest operating system and saves it as a PNG file on the VisualCron Server computer.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix"; "vSphere" and "vSphere 7" do not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Guest Capture screen Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Capture%20Screen.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

_Guest OS Credentials_ is required: select the Credential of a user account inside the virtual machine. Before it signs in, the Task waits up to 60 seconds for VMware Tools to run in the guest, whatever the timeout says. It signs in with the VMware option that requires an interactive session, so that user must be signed in to the guest desktop.

### VM Task settings sub tab

![VM Task settings sub tab of the VMWare Guest Capture screen Task, with the Image path field](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Capture%20Screen%20Settings.png)

- _Image path_: the full path of the PNG file on the VisualCron Server computer. The _File_ icon opens a file browser on the computer that runs the Client. Variables are replaced in this field

:::warning

If a file with this path exists, it is replaced without asking for confirmation.

:::

### Output and errors

When VMware reports an error, the Task fails.
