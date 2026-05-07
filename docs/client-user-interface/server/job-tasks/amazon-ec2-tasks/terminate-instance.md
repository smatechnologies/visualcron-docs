---
sidebar_label: 'Task Amazon EC2 - Terminate Instance'
hide_title: 'true'
---

## Task Amazon EC2 - Terminate Instance

The Amazon EC2 - Terminate instance Task terminates an EC2 instance. Termination is permanent — the underlying virtual machine is released and the instance's root EBS volume is deleted (unless the volume's *Delete on Termination* attribute has been set to false on the AWS side). To preserve the EBS volume for later reuse, use [Stop Instance](stop-instance) instead.

The Task issues the TerminateInstances call and reports the call result; it does not wait for the instance to reach the *terminated* state.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/Terminate%20Instance.png)

**Connection**

To use Amazon EC2 Tasks you need to create an Amazon [Connection](../../connection-amazon) first. The Connection supplies the access key, secret access key and region used by the Task. Click the *Settings* icon to open the *Manage Connections* dialog. Only Amazon connections are listed.

**Instance**

The ID of the instance to terminate. Click the *Refresh* icon to query the selected Connection and populate the drop-down with the instance IDs available in that account/region. Variables can be entered manually if the instance ID is determined at run time.
