---
sidebar_label: 'Task Azure - Start VM'
hide_title: 'true'
---

## Task Azure - Start VM

The Azure - Start VM Task starts an existing virtual machine in the Azure cloud. This Task is using the [Microsoft Azure Connection](../../connection-microsoft-azure).
 
**Azure - Start VM** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Azure%20Tasks/Start%20VM.png)

**Connection**

To use the Azure Tasks you need to create a [Connection](../../global-connections) first. Click the *Settings* icon to open the *Manage Connections* dialog.
 
**Type**

Select the deployment model of the target virtual machine. Available options:

* _Classic_ - the virtual machine was deployed using the classic deployment model
* _Resource Manager_ - the virtual machine was deployed using Azure Resource Manager

**VM name**

The Azure virtual machine name. Click the *Refresh* icon to populate the drop-down VM name list.

**Service name / Resource group**

The Azure service name (when *Type* is set to _Classic_) or the resource group (when *Type* is set to _Resource Manager_). The label changes to match the selected *Type*. Click the *Refresh* icon to populate the drop-down list.
