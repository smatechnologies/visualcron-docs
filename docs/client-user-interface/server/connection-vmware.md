---
sidebar_label: 'Connection - VMWare'
hide_title: 'true'
---

## Connection - VMWare

The VMWare Connection stores the address, sign-in and security settings that the following VMWare Tasks use to connect to a VMware host or vCenter Server:

- [VMWare - Start VM](job-tasks/vmware-tasks/start-vm)
- [VMWare - Stop VM](job-tasks/vmware-tasks/stop-vm)
- [VMWare - Suspend VM](job-tasks/vmware-tasks/suspend-vm)
- [VMWare - Pause VM](job-tasks/vmware-tasks/pause-vm)
- [VMWare - Resume VM](job-tasks/vmware-tasks/resume-vm)
- [VMWare - Reset VM](job-tasks/vmware-tasks/reset-vm)
- [VMWare - Get VM status](job-tasks/vmware-tasks/get-vm-status)
- [VMWare - Create VM snapshot](job-tasks/vmware-tasks/create-vm-snapshot)
- [VMWare - Revert to VM snapshot](job-tasks/vmware-tasks/revert-to-vm-snapshot)
- [VMWare - Delete VM snapshot](job-tasks/vmware-tasks/delete-vm-snapshot)
- [VMWare - List VM snapshots](job-tasks/vmware-tasks/list-vm-snapshots)
- [VMWare - Delete VM](job-tasks/vmware-tasks/delete-vm)
- [VMWare - Clone VM](job-tasks/vmware-tasks/clone-vm)
- [VMWare - Install tools](job-tasks/vmware-tasks/install-tools)
- [VMWare - Register VM](job-tasks/vmware-tasks/register-vm)
- [VMWare - Unregister VM](job-tasks/vmware-tasks/unregister-vm)
- [VMWare - List VM](job-tasks/vmware-tasks/list-vm)
- [VMWare - Capture screen (guest)](job-tasks/vmware-tasks/guest-capture-screen)
- [VMWare - Copy files (guest)](job-tasks/vmware-tasks/guest-copy-file)
- [VMWare - Rename file (guest)](job-tasks/vmware-tasks/guest-rename-file)
- [VMWare - Delete files (guest)](job-tasks/vmware-tasks/guest-delete-file)
- [VMWare - Directory exists (guest)](job-tasks/vmware-tasks/guest-directory-exists)
- [VMWare - File exists (guest)](job-tasks/vmware-tasks/guest-file-exists)
- [VMWare - Delete directory (guest)](job-tasks/vmware-tasks/guest-delete-directory)
- [VMWare - Create directory (guest)](job-tasks/vmware-tasks/guest-create-directory)
- [VMWare - Create temp file (guest)](job-tasks/vmware-tasks/guest-create-temp-file)
- [VMWare - Run command (guest)](job-tasks/vmware-tasks/guest-run-command)
- [VMWare - Open URL (guest)](job-tasks/vmware-tasks/guest-open-url)
- [VMWare - Kill processes (guest)](job-tasks/vmware-tasks/guest-kill-process)
- [VMWare - List processes (guest)](job-tasks/vmware-tasks/guest-list-process)
 
### Common settings

![VMWare Connection, Common settings tab with the Test button](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/VMWare/VMWare.png)

The ***Common settings*** tab is the same for every Connection type that has it; see [Common settings](global-connections#common-settings).

For a VMWare Connection, the _Test_ button is shown, but it only shows "Connection protocol type not supported for testing." The VMWare Tasks use _Timeout_, in seconds, as the time to wait when they open a virtual machine. _Code page_ is not used.
 
### Main settings

![VMWare Connection, Main settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/VMWare/Settings.png)

These fields are on ***Connection settings*** -> ***Main settings***. _Address_ and _Username_ are required.

- _Address_: the host name or IP address of the VMware host or vCenter Server. For "vSphere" and "vSphere 7", enter it without `https://` or a path, because VisualCron adds them. For "Vix", the value is passed to the VMware VIX API as entered
- _Authentication type_: see the options below. A new Connection uses "Vix"
- _Username_: the user name for the VMWare server
- _Password_: the password for the VMWare server

The API used to connect to the VMWare server. Available options:

* _Vix_ - uses the legacy VIX COM API. Supported up to vSphere version 6.0.
* _vSphere_ - uses the VMware vSphere Web Services SDK, which is based on web services. Recommended for vSphere versions after 6.0.
* _vSphere 7_ - uses the vSphere Web Services SDK targeting vSphere version 7 and later.

"Vix" needs the VMware VIX API installed on the Server computer. "vSphere" signs on through the single sign-on service on port 7444 of the host.
