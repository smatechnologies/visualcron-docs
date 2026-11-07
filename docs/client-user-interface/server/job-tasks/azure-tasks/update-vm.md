---
sidebar_label: 'Task Azure - Update VM'
hide_title: 'true'
---

## Task Azure - Update VM

The Azure - Update VM Task sends an update request for an existing virtual machine in Azure, using a Microsoft Azure Connection. The Task has no settings for what to update.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Azure - Update VM tab

![Azure - Update VM tab with the Connection list, the Classic and Resource manager options, and the VM name and Service name lists with their Refresh buttons](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Azure%20Tasks/Update%20VM.png)

- _Connection_: the Microsoft Azure Connection to use; see [Connection - Microsoft Azure](../../connection-microsoft-azure). Click the _Settings_ icon to open _Manage Connections_. With "Resource manager", the Connection must use the "Application" authentication type. When the Connection does not suit the selected option, the Task window shows a warning

**Type**

Select the deployment model of the target virtual machine. Available options:

* _Classic_ - the virtual machine was deployed using the classic deployment model
* _Resource Manager_ - the virtual machine was deployed using Azure Resource Manager

- _VM name_: the name of the Azure virtual machine. Click _Refresh_ to fill the list

**Service name / Resource group**

The Azure service name (when *Type* is set to _Classic_) or the resource group (when *Type* is set to _Resource Manager_). The label changes to match the selected *Type*. Click the *Refresh* icon to populate the drop-down list.

### Output and errors

When Azure reports that the update succeeded, the output is "Succeeded". When the Connection is missing, or Azure returns an error, the Task fails.

:::warning

When Azure reports another status, or the Connection does not suit the selected option, the error is written to standard error, the output is empty, and the Task reports success.

:::
