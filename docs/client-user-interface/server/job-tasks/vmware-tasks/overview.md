---
sidebar_label: 'Overview'
hide_title: 'true'
---

## Overview

A VMWare guest task is used for an individual guest operating system or numerous guest operating systems running on multiple virtual machines.

**External library**

The VMWare Tasks require download and install of the VMWare VIX API on the VisualCron server:

[https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/5_0](https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/5_0)
 
In the VMWare Tasks you can connect to VMWare Workstation or to a remote VMWare server (vSphere) depending on the Task type. The Connection sub tab is the same for all VMWare Task types — see [Start VM](start-vm) for the field-by-field description.

**Available VMWare Tasks**

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

Guest operations (require Guest OS Credentials):

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
