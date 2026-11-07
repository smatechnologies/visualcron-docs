---
sidebar_label: 'Task VMWare - Stop VM'
hide_title: 'true'
---

## Task VMWare - Stop VM

The VMWare - Stop VM Task stops (powers off) a virtual machine, using a VMWare Connection or VMware Workstation on the VisualCron Server computer.

:::warning

With a "vSphere" or "vSphere 7" Connection, _Stop type_ is not used: the virtual machine is always powered off at once, as if the power were pulled, so unsaved work in the guest can be lost. For a clean shutdown of the guest, use a "Vix" Connection or _Local VMWare workstation_ with "Soft".

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task works with every _Authentication type_ of the VMWare Connection; see [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Stop VM Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Stop%20VM.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

### VM Task settings sub tab

![VM Task settings sub tab of the VMWare Stop VM Task, with the Stop type combo box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Stop%20VM%20settings.png)

- _Stop type_: how the virtual machine is powered off, "Soft" by default:
  - "Hard": powers off the virtual machine at once, as if the power were pulled
  - "Soft": asks the guest operating system to shut down through VMware Tools
  - "TrySoft": works the same as "Soft"; there is no fallback to "Hard" when the guest does not shut down

### Output and errors

When VMware reports an error, the Task fails.
