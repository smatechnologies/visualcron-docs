---
sidebar_label: 'Task Amazon EC2 - Terminate Instance'
hide_title: 'true'
---

## Task Amazon EC2 - Terminate Instance

The Amazon EC2 - Terminate instance Task terminates an Amazon EC2 instance, using an Amazon Connection. To keep the instance and its EBS root volume for later use, use [Stop Instance](stop-instance) instead.

![EC2 - Terminate instance Task settings, with the Connection and Instance fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/Terminate%20Instance.png)

:::warning

Termination cannot be undone: the instance cannot be started again. Data on the local (ephemeral) drives of the instance is lost, and EBS volumes that are set in AWS to delete on termination are deleted.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### EC2 - Terminate instance tab

- _Connection_: the Amazon Connection to use; see [Connection - Amazon](../../connection-amazon). Click the button next to the list to manage Connections. The Client asks you to select a Connection before it saves the Task
- _Instance_: the ID of the instance to terminate. Click the refresh button to fill the list with the instances that the Server finds with the Connection. Variables are not resolved in this field

### Output and errors

When Amazon accepts the request, the Task writes the result that Amazon returns to the Task output.

When the Connection cannot be found, or Amazon returns an error, the Task fails. To change how the Task responds to errors, see [Task - On error](../../task-on-error).
