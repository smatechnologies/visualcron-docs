---
sidebar_label: 'Task Amazon EC2 - Start Instance'
hide_title: 'true'
---

## Task Amazon EC2 - Start Instance

The Amazon EC2 - Start instance Task starts a stopped EC2 instance that uses an Amazon EBS volume as its root device. The Task issues the start request and reports the call result; it does not wait for the instance to reach the *running* state.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/Start%20Instance.png)

**Connection**

To use Amazon EC2 Tasks you need to create an Amazon [Connection](../../connection-amazon) first. The Connection supplies the access key, secret access key and region used by the Task. Click the *Settings* icon to open the *Manage Connections* dialog. Only Amazon connections are listed.

**Instance**

The ID of the instance to start. Click the *Refresh* icon to query the selected Connection and populate the drop-down with the instance IDs available in that account/region. Variables can be entered manually if the instance ID is determined at run time.
