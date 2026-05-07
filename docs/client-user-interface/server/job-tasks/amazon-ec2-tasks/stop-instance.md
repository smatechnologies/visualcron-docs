---
sidebar_label: 'Task Amazon EC2 - Stop Instance'
hide_title: 'true'
---

## Task Amazon EC2 - Stop Instance

The Amazon EC2 - Stop instance Task stops a running EC2 instance that uses an Amazon EBS (Elastic Block Store) volume as its root device. When an instance is stopped, the underlying virtual machine is released and per-hour charges stop, but the attached EBS root volume is preserved (data on the EBS volume remains available, while data on any local/ephemeral storage is lost as usual). The key difference between *stopping* and *terminating* is that stopping preserves the EBS volume, allowing the instance to be started again later.

The Task issues the StopInstances call and reports the call result; it does not wait for the instance to reach the *stopped* state.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/Stop%20Instance.png)

**Connection**

To use Amazon EC2 Tasks you need to create an Amazon [Connection](../../connection-amazon) first. The Connection supplies the access key, secret access key and region used by the Task. Click the *Settings* icon to open the *Manage Connections* dialog. Only Amazon connections are listed.

**Instance**

The ID of the instance to stop. Click the *Refresh* icon to query the selected Connection and populate the drop-down with the instance IDs available in that account/region. Variables can be entered manually if the instance ID is determined at run time.

**Force**

If checked, the instance is forced to stop (the underlying call is made with the `-ForceStop` flag). Forcing a stop does not give the operating system a chance to flush file system caches or shut down cleanly, so it can leave the file system in an inconsistent state. Not recommended for Windows instances.
