---
sidebar_label: 'Task Azure - Stop VM'
hide_title: 'true'
---

## Task Azure - Stop VM

The Azure - Stop VM Task stops an existing virtual machine in the Azure cloud. This Task is using the [Microsoft Azure Connection](../../connection-microsoft-azure).
 
**Azure - Stop VM** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Azure%20Tasks/Stop%20VM.png)

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

**Deallocate**

If checked, the virtual machine is stopped and deallocated, releasing the underlying compute resources so that they no longer accrue charges. When unchecked, the virtual machine is stopped but the compute resources remain reserved.
