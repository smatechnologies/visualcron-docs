---
sidebar_label: 'Task VMWare - [Guest] Kill Process'
hide_title: 'true'
---

## Task VMWare - [Guest] Kill Process

The VMWare - [Guest] Kill Process Task ends one or more processes in the guest operating system.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix"; "vSphere" and "vSphere 7" do not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Guest Kill process(es) Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Kill%20Process.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

_Guest OS Credentials_ is required: select the Credential of a user account inside the virtual machine. Before it signs in, the Task waits up to 60 seconds for VMware Tools to run in the guest, whatever the timeout says. It signs in with the VMware option that requires an interactive session, so that user must be signed in to the guest desktop.

### VM Task settings sub tab

![VM Task settings sub tab of the VMWare Guest Kill process(es) Task, with the Process name and Process Id options](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20Kill%20Process%20Settings.png)

Select one of the two options:

- _Process name_: end every process with this name. Selected by default. The name must match exactly, including case; the Task repeats until no process with the name is left. Variables are replaced in this field
- _Process Id_: end the process with this numeric ID. Variables are replaced in this field

The _Refresh_ icons next to the fields do not fill the lists in this version; type the name or ID.

:::warning

The processes are ended without asking for confirmation, so unsaved work in them can be lost.

:::

### Output and errors

When VMware reports an error, the Task fails.
