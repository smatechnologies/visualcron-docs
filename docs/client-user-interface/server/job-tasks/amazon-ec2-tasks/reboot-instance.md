---
sidebar_label: 'Task Amazon EC2 - Reboot Instance'
hide_title: 'true'
---

## Task Amazon EC2 - Reboot Instance

The Amazon EC2 - Reboot instance Task requests a reboot of an Amazon EC2 instance, using an Amazon Connection. The request is asynchronous: Amazon only queues the reboot, and the request succeeds when the instance is valid and belongs to you. Requests to reboot terminated instances are ignored.

![EC2 - Reboot instance Task settings, with the Connection and Instance fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/Reboot%20Instance.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### EC2 - Reboot instance tab

- _Connection_: the Amazon Connection to use; see [Connection - Amazon](../../connection-amazon). Click the button next to the list to manage Connections. The Client asks you to select a Connection before it saves the Task
- _Instance_: the ID of the instance to reboot. Click the refresh button to fill the list with the instances that the Server finds with the Connection. Variables are not resolved in this field

### Output and errors

When Amazon accepts the request, the Task writes the result that Amazon returns to the Task output. The Task does not wait for the instance to restart.

When the Connection cannot be found, or Amazon returns an error, the Task fails. To change how the Task responds to errors, see [Task - On error](../../task-on-error).
