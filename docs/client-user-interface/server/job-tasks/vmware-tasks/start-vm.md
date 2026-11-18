---
sidebar_label: 'Task VMWare - Start VM'
hide_title: 'true'
---

## Task VMWare - Start VM

The VMWare - Start VM Task starts (powers on) a virtual machine on a VMware server, using a VMWare Connection, or in VMware Workstation on the VisualCron Server computer.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks). The Task-type tab has two sub tabs, ***Connection*** and ***VM Task settings***.

With _Remote VMWare server_, this Task works with every _Authentication type_ of the VMWare Connection; see [Connection - VMWare](../../connection-vmware).

### Connection sub tab

![Connection sub tab of the VMWare Start VM Task, with the Remote VMWare server and Local VMWare workstation options, Guest OS Credentials and the timeout](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Start%20VMWare.png)

The ***Connection*** sub tab is the same for every VMWare Task. Some Task types select an option for you or turn a field off; each Task's page says which.

- _Remote VMWare server_: control a virtual machine on a VMware host or vCenter Server through a VMWare Connection
- _Connection_: the VMWare Connection to use. Click the _Settings_ icon to add or edit Connections; see [Connection - VMWare](../../connection-vmware)
- _Server VMX path_: the virtual machine on the server. Click the _Refresh_ icon to list the virtual machines that the Connection can reach. With a "vSphere 7" Connection, each entry is the virtual machine ID followed by its name in parentheses. Variables are not replaced in this field
- _Local VMWare workstation_: control a virtual machine in VMware Workstation on the VisualCron Server computer
- _Local VMX path_: the full path of the virtual machine's ".vmx" file on the VisualCron Server computer. The _File_ icon opens a file browser on the computer that runs the Client. Variables are replaced in this field. If the file does not exist on the Server computer, the Task fails with "VMX file not found."
- _Guest OS Credentials_: the [Credential](../../global-credentials) of a user account inside the virtual machine. It is available, and required, only for the [Guest] Task types
- _Timeout in seconds (Timeout tab overrides)_: how long each VMware operation can take, from "1" to "36000" seconds, "180" by default. When the Task's ***TimeOut*** tab is in use, its time is used instead. With a "Vix" Connection, the Connection's _Timeout_ is the time allowed to open the virtual machine; with _Local VMWare workstation_, opening it can take up to 10 seconds

With _Remote VMWare server_, the Connection's user name and password sign in to the VMware server: over HTTPS with "vSphere" and "vSphere 7", and through the VMware VIX API with "Vix".

When you click _OK_, the Client checks that the Connection's _Authentication type_ supports the Task type; see [Connection support](overview#connection-support).

### VM Task settings sub tab

![VM Task settings sub tab of the VMWare Start VM Task, with the Launch GUI check box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/VMWare%20Tasks/Start%20VMWare%20Settings.png)

- _Launch GUI_: open the virtual machine in the VMware Workstation window when it starts. Not checked by default. It is not used with "vSphere" or "vSphere 7" Connections

### Output and errors

When VMware reports an error, the Task fails.
