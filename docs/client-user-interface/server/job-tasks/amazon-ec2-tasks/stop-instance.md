---
sidebar_label: 'Task Amazon EC2 - Stop Instance'
hide_title: 'true'
---

## Task Amazon EC2 - Stop Instance

The Amazon EC2 - Stop instance Task stops an Amazon EC2 instance that uses an Amazon EBS (Elastic Block Store) volume as its root device, using an Amazon Connection. A stopped instance is shut down and you are no longer charged for instance usage. Unlike termination, stopping does not delete the attached bootable EBS volume, and the data on the EBS volume remains. To start the instance again, use [Start Instance](start-instance).

![EC2 - Stop instance Task settings, with the Connection and Instance fields and the Force check box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/Stop%20Instance.png)

:::warning

When the instance stops, the data on its local (ephemeral) drives is lost.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### EC2 - Stop instance tab

- _Connection_: the Amazon Connection to use; see [Connection - Amazon](../../connection-amazon). Click the button next to the list to manage Connections. The Client asks you to select a Connection before it saves the Task
- _Instance_: the ID of the instance to stop. Click the refresh button to fill the list with the instances that the Server finds with the Connection. Variables are not resolved in this field
- _Force_ (_Other settings_ group): forces the instance to stop. Unchecked by default. This may cause file system problems and is not recommended for Windows instances

### Output and errors

When Amazon accepts the request, the Task writes the result that Amazon returns to the Task output.

When the Connection cannot be found, or Amazon returns an error, the Task fails. To change how the Task responds to errors, see [Task - On error](../../task-on-error).
