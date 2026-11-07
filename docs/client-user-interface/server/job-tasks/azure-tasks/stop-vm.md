---
sidebar_label: 'Task Azure - Stop VM'
hide_title: 'true'
---

## Task Azure - Stop VM

The Azure - Stop VM Task stops an existing virtual machine in Azure, using a Microsoft Azure Connection.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Azure - Stop VM tab

![Azure - Stop VM tab with the Connection list, the Classic and Resource manager options, and the VM name and Service name lists with their Refresh buttons, and the Deallocate check box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Azure%20Tasks/Stop%20VM.png)

- _Connection_: the Microsoft Azure Connection to use; see [Connection - Microsoft Azure](../../connection-microsoft-azure). Click the _Settings_ icon to open _Manage Connections_. With "Resource manager", the Connection must use the "Application" authentication type. When the Connection does not suit the selected option, the Task window shows a warning and the Task stops with an error

**Type**

Select the deployment model of the target virtual machine. Available options:

* _Classic_ - the virtual machine was deployed using the classic deployment model
* _Resource Manager_ - the virtual machine was deployed using Azure Resource Manager

- _VM name_: the name of the Azure virtual machine. Click _Refresh_ to fill the list

**Service name / Resource group**

The Azure service name (when *Type* is set to _Classic_) or the resource group (when *Type* is set to _Resource Manager_). The label changes to match the selected *Type*. Click the *Refresh* icon to populate the drop-down list.

- _Deallocate_: when selected, the virtual machine is stopped and deallocated, which releases its compute resources so that they no longer accrue charges. When cleared, the virtual machine is stopped but its compute resources stay reserved

### Output and errors

When Azure reports that the operation succeeded, the output is "Succeeded". When the Connection is missing, or Azure returns an error, the Task fails.

:::warning

When Azure reports another status for the operation, the status is written to standard error, the output is empty, and the Task reports success.

:::
