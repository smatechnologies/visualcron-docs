---
sidebar_label: 'Overview'
hide_title: 'true'
---

## Overview

The VMWare Tasks control VMware virtual machines: power operations, snapshots, and file and process operations inside the guest operating system.

**External library**

The VMWare Tasks require download and install of the VMWare VIX API on the VisualCron server:

[https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/5_0](https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/5_0)
 
Each VMWare Task connects either to a VMware host or vCenter Server through a [VMWare Connection](../../connection-vmware) (_Remote VMWare server_), or to VMware Workstation on the VisualCron Server computer (_Local VMWare workstation_). The ***Connection*** sub tab is the same for every VMWare Task; see [Start VM](start-vm#connection-sub-tab) for each field.

### Connection support

When you click _OK_, the Client checks that the _Authentication type_ of the selected VMWare Connection supports the Task type:

- "Vix": every VMWare Task
- "vSphere": every VMWare Task except Pause VM, Install Tools and the [Guest] Tasks
- "vSphere 7": Start VM, Stop VM, Suspend VM, Resume VM, Reset VM, Get VM Status, Clone VM, Delete VM, Unregister VM and List VM

With a "vSphere" or "vSphere 7" Connection, the Stop VM and Reset VM Tasks always act at once, without shutting down the guest; see [Stop VM](stop-vm) and [Reset VM](reset-vm).

### Available VMWare Tasks

Virtual machines:

* [List VM](list-vm)
* [Get VM Status](get-vm-status)
* [Start VM](start-vm)
* [Stop VM](stop-vm)
* [Reset VM](reset-vm)
* [Pause VM](pause-vm)
* [Resume VM](resume-vm)
* [Suspend VM](suspend-vm)
* [Clone VM](clone-vm)
* [Delete VM](delete-vm)
* [Register VM](register-vm)
* [Unregister VM](unregister-vm)
* [Install Tools](install-tools)

Snapshots:

* [Create VM Snapshot](create-vm-snapshot)
* [Delete VM Snapshot](delete-vm-snapshot)
* [List VM Snapshots](list-vm-snapshots)
* [Revert to VM Snapshot](revert-to-vm-snapshot)

Guest operations (these need _Guest OS Credentials_, VMware Tools running in the guest, and a user signed in to the guest desktop):

* [Capture Screen](guest-capture-screen)
* [Copy File](guest-copy-file)
* [Create Directory](guest-create-directory)
* [Create Temp File](guest-create-temp-file)
* [Delete Directory](guest-delete-directory)
* [Delete File](guest-delete-file)
* [Directory Exists](guest-directory-exists)
* [File Exists](guest-file-exists)
* [Kill Process](guest-kill-process)
* [List Process](guest-list-process)
* [Open URL](guest-open-url)
* [Rename File](guest-rename-file)
* [Run Command](guest-run-command)
