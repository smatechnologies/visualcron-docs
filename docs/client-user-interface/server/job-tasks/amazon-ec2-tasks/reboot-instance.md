---
sidebar_label: 'Task Amazon EC2 - Reboot Instance'
hide_title: 'true'
---

## Task Amazon EC2 - Reboot Instance

The Amazon EC2 - Reboot instance Task requests a reboot of an EC2 instance. The underlying RebootInstances call is asynchronous on the AWS side: it queues a reboot request, returns immediately, and succeeds as long as the instance is valid and belongs to the account on the selected Connection. Requests to reboot terminated instances are silently ignored. The Task itself does not wait for the instance to come back up.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/Reboot%20Instance.png)

**Connection**

To use Amazon EC2 Tasks you need to create an Amazon [Connection](../../connection-amazon) first. The Connection supplies the access key, secret access key and region used by the Task. Click the *Settings* icon to open the *Manage Connections* dialog. Only Amazon connections are listed.

**Instance**

The ID of the instance to reboot. Click the *Refresh* icon to query the selected Connection and populate the drop-down with the instance IDs available in that account/region. Variables can be entered manually if the instance ID is determined at run time.
