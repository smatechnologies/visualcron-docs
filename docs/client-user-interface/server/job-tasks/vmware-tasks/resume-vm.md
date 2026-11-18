---
sidebar_label: 'Task VMWare - Resume VM'
hide_title: 'true'
---

## Task VMWare - Resume VM

The VMWare - Resume VM Task resumes a paused virtual machine, using VMware Workstation on the VisualCron Server computer or a VMWare Connection.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task works with every _Authentication type_ of the VMWare Connection; see [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Resume VM Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Resume%20VM.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

Each time the Task opens, _Local VMWare workstation_ is selected, even if the Task was saved with _Remote VMWare server_. Check the selection before you click _OK_.

### Output and errors

With a "vSphere" or "vSphere 7" Connection, the Task powers the virtual machine on, the same as the [Start VM](start-vm) Task. When VMware reports an error, the Task fails.
