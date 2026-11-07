---
sidebar_label: 'Task VMWare - Reset VM'
hide_title: 'true'
---

## Task VMWare - Reset VM

The VMWare - Reset VM Task resets (restarts) a virtual machine, using a VMWare Connection or VMware Workstation on the VisualCron Server computer.

:::warning

With a "vSphere" or "vSphere 7" Connection, _Stop type_ is not used: the virtual machine is always reset at once, as if the power were cycled, so unsaved work in the guest can be lost. For a clean restart of the guest, use a "Vix" Connection or _Local VMWare workstation_ with "Soft".

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

With _Remote VMWare server_, this Task works with every _Authentication type_ of the VMWare Connection; see [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Reset VM Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Reset%20VM.png)

The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

### VM Task settings sub tab

![VM Task settings sub tab of the VMWare Reset VM Task, with the Stop type combo box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Reset%20VM%20Settings.png)

- _Stop type_: how the virtual machine is reset, "Soft" by default:
  - "Hard": resets the virtual machine at once, as if the power were cycled
  - "Soft": asks the guest operating system to restart through VMware Tools
  - "TrySoft": works the same as "Soft"; there is no fallback to "Hard" when the guest does not restart

### Output and errors

When VMware reports an error, the Task fails.
