---
sidebar_label: 'Task VMWare - Install Tools'
hide_title: 'true'
---

## Task VMWare - Install Tools

The VMWare - Install Tools Task installs VMware Tools in the guest operating system, using a VMWare Connection or VMware Workstation on the VisualCron Server computer.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix"; "vSphere" and "vSphere 7" do not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Install tools Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Install%20Tools.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

The Task uses the VMware automatic upgrade option, so an existing VMware Tools installation in the guest is upgraded without prompts.

### Output and errors

When VMware reports an error, the Task fails.
