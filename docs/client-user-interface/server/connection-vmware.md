---
sidebar_label: 'Connection - VMWare'
hide_title: 'true'
---

## Connection - VMWare

The VMWare Connection stores connect and logon properties for guest and remote VMWare instances.
 
The VMWare Connection is used for connecting to remote VMWare instances in the following Tasks:

* [VMWare - Start VM](../../client-user-interface/server/job-tasks/vmware-tasks/start-vm)
* [VMWare - Stop VM](../../client-user-interface/server/job-tasks/vmware-tasks/stop-vm)
* [VMWare - Suspend VM](../../client-user-interface/server/job-tasks/vmware-tasks/suspend-vm)
* [VMWare - Pause VM](../../client-user-interface/server/job-tasks/vmware-tasks/pause-vm)
* [VMWare - Resume VM](../../client-user-interface/server/job-tasks/vmware-tasks/resume-vm)
* [VMWare - Reset VM](../../client-user-interface/server/job-tasks/vmware-tasks/reset-vm)
* [VMWare - Get VM status](../../client-user-interface/server/job-tasks/vmware-tasks/get-vm-status)
* [VMWare - Create VM snapshot](../../client-user-interface/server/job-tasks/vmware-tasks/create-vm-snapshot)
* [VMWare - Revert to VM snapshot](../../client-user-interface/server/job-tasks/vmware-tasks/revert-to-vm-snapshot)
* [VMWare - Delete VM snapshot](../../client-user-interface/server/job-tasks/vmware-tasks/delete-vm-snapshot)
* [VMWare - List VM snapshots](../../client-user-interface/server/job-tasks/vmware-tasks/list-vm-snapshots)
* [VMWare - Delete VM](../../client-user-interface/server/job-tasks/vmware-tasks/delete-vm)
* [VMWare - Clone VM](../../client-user-interface/server/job-tasks/vmware-tasks/clone-vm)
* [VMWare - Install tools](../../client-user-interface/server/job-tasks/vmware-tasks/install-tools)
* [VMWare - Register VM](../../client-user-interface/server/job-tasks/vmware-tasks/register-vm)
* [VMWare - Unregister VM](../../client-user-interface/server/job-tasks/vmware-tasks/unregister-vm)
* [VMWare - List VM](../../client-user-interface/server/job-tasks/vmware-tasks/list-vm)
* [VMWare - Capture screen (guest)](../../client-user-interface/server/job-tasks/vmware-tasks/guest-capture-screen)
* [VMWare - Copy files (guest)](../../client-user-interface/server/job-tasks/vmware-tasks/guest-copy-file)
* [VMWare - Rename file (guest)](../../client-user-interface/server/job-tasks/vmware-tasks/guest-rename-file)
* [VMWare - Delete files (guest)](../../client-user-interface/server/job-tasks/vmware-tasks/guest-delete-file)
* [VMWare - Directory exists (guest)](../../client-user-interface/server/job-tasks/vmware-tasks/guest-directory-exists)
* [VMWare - File exists (guest)](../../client-user-interface/server/job-tasks/vmware-tasks/guest-file-exists)
* [VMWare - Delete directory (guest)](../../client-user-interface/server/job-tasks/vmware-tasks/guest-delete-directory)
* [VMWare - Create directory (guest)](../../client-user-interface/server/job-tasks/vmware-tasks/guest-create-directory)
* [VMWare - Create temp file (guest)](../../client-user-interface/server/job-tasks/vmware-tasks/guest-create-temp-file)
* [VMWare - Run command (guest)](../../client-user-interface/server/job-tasks/vmware-tasks/guest-run-command)
* [VMWare - Open URL (guest)](../../client-user-interface/server/job-tasks/vmware-tasks/guest-open-url)
* [VMWare - Kill processes (guest)](../../client-user-interface/server/job-tasks/vmware-tasks/guest-kill-process)
* [VMWare - List processes (guest)](../../client-user-interface/server/job-tasks/vmware-tasks/guest-list-process)
 
**Manage Connections > Add > VMWare > Common settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/VMWare/VMWare.png)

**Name**

The unique name for the Connection
 
**Group**

The group that the connection is a part of.
 
**Timeout**

The connection timeout in seconds. Connection will fail after this time period.

**Code page**

Code page being used.
 
**Manage Connections > Add > VMWare > Connection settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/VMWare/Settings.png)

**Address**

The address to the VMWare server.

**Authentication type**

Choose between VIX or vSphere. VIX stands for the old API that uses COM libraries to manage vSphere. This is supported up to version 6.0 of vSphere. For future version the new vSphere API is used which is based on web services. The VMware vSphere® Web Services SDK includes all the components necessary to work with the VMware vSphere API, including WSDL files, sample code, and libraries. The vSphere Web Services SDK facilitates development of client applications that target the VMware vSphere API. With the vSphere Web Services SDK, developers can create client applications to manage, monitor, and maintain VMware vSphere components, as deployed on VMware® VMware vSphere® ESX®, ESXi™, and VMware® vCenter™ Server systems.
 
**Username**

The username for the server.
 
**Password**

The password for the server.
 
 
### Troubleshooting

*The protocol requested by peer '0 0 9 1' does not match expected '3 1 0 0'. Make sure both sides agree on protocol id and version.*
Please upgrade remote server to AMQP 1.0. VisualCron supports AMQP 1.0 or later.