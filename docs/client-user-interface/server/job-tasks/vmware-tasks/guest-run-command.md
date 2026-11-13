---
sidebar_label: 'Task VMWare - [Guest] Run Command'
hide_title: 'true'
---

## Task VMWare - [Guest] Run Command

The VMWare - [Guest] Run Command Task runs a program in the guest operating system.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix"; "vSphere" and "vSphere 7" do not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Guest Run command Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Run%20Command.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

_Guest OS Credentials_ is required: select the Credential of a user account inside the virtual machine. Before it signs in, the Task waits up to 60 seconds for VMware Tools to run in the guest, whatever the timeout says. It signs in with the VMware option that requires an interactive session, so that user must be signed in to the guest desktop.

### VM Task settings sub tab

![VM Task settings sub tab of the VMWare Guest Run command Task, with the Full path to command and Argument fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Run%20Command%20Settings.png)

- _Full path to command_: the full path of the program, batch file or script in the guest. The _File_ icon opens a file browser on the computer that runs the Client and enters only the file name, so complete the path by hand. Variables are replaced in this field
- _Argument_: the arguments to pass to the program. Variables are replaced in this field

### Output and errors

The Task waits for the program to end, for up to _Timeout in seconds_ (or the time on the ***TimeOut*** tab). If the program runs longer, the Task fails. The output of the program is not captured.

:::warning

The Task does not check the exit code of the program, so when the program fails in the guest, the error is not reported, and the Task reports success.

:::

When VMware itself reports an error, the Task fails.
