---
sidebar_label: 'Task Azure - Update VM'
hide_title: 'true'
---

## Task Azure - Update VM

This Task is using the [Microsoft Azure Connection](../../connection-microsoft-azure).

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Azure%20Tasks/Update%20VM.png)

**Connection**

Select the Microsoft Azure Connection to use. Only connections of type Azure are shown.

**Virtual machine**

**Classic / Resource manager**

Select the VM deployment model.

* _Classic_ - uses the Azure Classic deployment model; the service name field is labeled _Service name_
* _Resource manager_ - uses the Azure Resource Manager model; the service name field is labeled _Resource group_

If the selected connection type does not match the selected mode, a warning is displayed.

**VM name**

The name of the virtual machine to update. Click the Refresh button to populate the list from the Azure connection.

**Service name / Resource group**

The cloud service name (Classic mode) or resource group name (Resource Manager mode) that contains the virtual machine. Click the Refresh button to populate the list. This field is automatically populated when a VM is selected.
