---
sidebar_label: 'Task VMWare - Pause VM'
hide_title: 'true'
---

## Task VMWare - Pause VM

The VMWare - Pause VM Task pauses a running virtual machine, using VMware Workstation on the VisualCron Server computer or a VMWare Connection.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix"; "vSphere" and "vSphere 7" do not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Pause VM Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Pause%20VM.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

Each time the Task opens, _Local VMWare workstation_ is selected, even if the Task was saved with _Remote VMWare server_. Check the selection before you click _OK_.

### Output and errors

When VMware reports an error, the Task fails. To continue a paused virtual machine, use the [Resume VM](resume-vm) Task.
