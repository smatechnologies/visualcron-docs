---
sidebar_label: 'Task VMWare - [Guest] List Process'
hide_title: 'true'
---

## Task VMWare - [Guest] List Process

The VMWare - [Guest] List Process Task lists the processes that run in the guest operating system.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix"; "vSphere" and "vSphere 7" do not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Guest List process(es) Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Guest%20Section/Guest%20List%20Process.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

_Guest OS Credentials_ is required: select the Credential of a user account inside the virtual machine. Before it signs in, the Task waits up to 60 seconds for VMware Tools to run in the guest, whatever the timeout says. It signs in with the VMware option that requires an interactive session, so that user must be signed in to the guest desktop.

### Output and errors

The output is an XML list with each process's name, process ID, owner, command line, start time and whether a debugger is attached. When VMware reports an error, the Task fails.
