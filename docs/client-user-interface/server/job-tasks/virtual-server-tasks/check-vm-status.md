---
sidebar_label: 'Task Virtual Server - Check VM Status'
hide_title: 'true'
---

## Task Virtual Server - Check VM Status

The Virtual Server - Check VM status Task retrieves the status of a specific virtual machine.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Virtual%20Server%20Tasks/Check%20VM%20Status.png)

**Remote VMWare server / Local VMWare workstation**

Select _Remote VMWare server_ to connect to a remote VMWare server, or _Local VMWare workstation_ to use the local machine.

**Connection**

Select the VMWare connection to use. Only enabled when _Remote VMWare server_ is selected.

**Server VMX path**

The path to the virtual machine's VMX file on the remote server. Click the _Refresh_ button to populate the list from the selected connection. Only enabled when _Remote VMWare server_ is selected.

**Local VMX path**

The path to the virtual machine's VMX file on the local machine. Click the File icon to browse. Only enabled when _Local VMWare workstation_ is selected.

**Timeout in seconds**

The number of seconds to wait before timing out the operation. Minimum is 1, maximum is 36000, default is 180. Note that a Timeout tab setting on the task overrides this value.
