---
sidebar_label: 'Task VMWare - Register VM'
hide_title: 'true'
---

## Task VMWare - Register VM

The VMWare - Register VM Task adds a virtual machine to the inventory of the VMware server, using a VMWare Connection.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task needs a VMWare Connection with the _Authentication type_ "Vix" or "vSphere"; "vSphere 7" does not support it (see [Connection support](overview#connection-support)). See also [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Register VM Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Register%20VM.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

Enter the path of the virtual machine's ".vmx" file in _Server VMX path_. A virtual machine that is not registered yet is not in the list that the _Refresh_ icon fills. With a "vSphere" Connection, enter the datastore path, for example `[datastore1] folder/name.vmx`; a path without the datastore name in brackets makes the Task fail.

### Output and errors

When VMware reports an error, the Task fails.
