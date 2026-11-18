---
sidebar_label: 'Task VMWare - Get VM Status'
hide_title: 'true'
---

## Task VMWare - Get VM Status

The VMWare - Get VM Status Task checks whether a virtual machine is powered on, using a VMWare Connection or VMware Workstation on the VisualCron Server computer.

![Main settings tab of the VMWare Get VM status Task](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Get%20VM%20Status.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task works with every _Authentication type_ of the VMWare Connection; see [Connection - VMWare](../../connection-vmware).

### Connection sub tab

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

### Output and errors

The output is "True" when the virtual machine is powered on, and "False" in every other state.

:::warning

With a "vSphere" Connection, a virtual machine that is not found also gives "False". With a "vSphere 7" Connection, an error from vCenter after sign-in also gives "False", and the Task reports success.

:::

Otherwise, when VMware reports an error, the Task fails.
