---
sidebar_label: 'Task Azure - Create VM'
hide_title: 'true'
---

## Task Azure - Create VM

The Azure - Create VM Task creates a virtual machine in Azure, using a Microsoft Azure Connection.

:::warning

The two _Password_ boxes show the passwords as they are typed, and the Task stores them without encryption in its settings.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Azure - Create VM tab

![Azure - Create VM tab with the Connection list, the Classic and Resource manager options, and the virtual machine settings from VM name to Resized size in GB](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Azure%20Tasks/Create%20VM.png)

- _Connection_: the Microsoft Azure Connection to use; see [Connection - Microsoft Azure](../../connection-microsoft-azure). Click the _Settings_ icon to open _Manage Connections_. With "Resource manager", the Connection must use the "Application" authentication type. When the Connection does not suit the selected option, the Task window shows a warning and the Task stops with an error

**Type**

Select the deployment model to use for the new virtual machine. Available options:

* _Classic_ - create the virtual machine using the classic deployment model
* _Resource Manager_ - create the virtual machine using Azure Resource Manager

The labels of several fields below change to match the selected *Type*.

- _VM name_: the name to give the new virtual machine

**Service name / Resource group**

The Azure service name (when *Type* is set to _Classic_) or the resource group (when *Type* is set to _Resource Manager_) in which the virtual machine will be created.

**Storage name / Availability set**

The Azure storage account that will host the virtual machine's disks (when *Type* is set to _Classic_) or the availability set the virtual machine should join (when *Type* is set to _Resource Manager_). Click the *Refresh* icon to populate the drop-down list.

- _Region_: the Azure region to create the virtual machine in. Click _Refresh_ to fill the list
- _Role size_: the size of the virtual machine. Click _Refresh_ to list the sizes available in the selected _Region_

**OS image**

The operating system image to deploy. Click the *Refresh* icon to populate the drop-down (Classic) or to open the image search dialog (Resource Manager).

**Deployment slot / Disk type**

The deployment slot for the virtual machine (when *Type* is set to _Classic_) or the disk type (when *Type* is set to _Resource Manager_). Click the *Refresh* icon to populate the drop-down list.

- _Admin name_: the administrator user name for the new virtual machine
- _Password_ (below _Admin name_): the administrator password
- _User name_: the standard user to create on the new virtual machine
- _Password_ (below _User name_): the password of the standard user
- _Host_: the host name to give the new virtual machine
- _Resized size in GB_: the size of the virtual machine's disk, in gigabytes. It must be a whole number, or the Task fails

### Output and errors

When Azure reports that the virtual machine was created, the output is "Succeeded". When the Connection is missing, or Azure returns an error, the Task fails.

:::warning

When Azure reports another status, the status is written to standard error and the Task reports success. When Azure returns no status, the output is empty and the Task reports success.

:::
