---
sidebar_label: 'Task Amazon EC2 - Create Snapshot'
hide_title: 'true'
---

## Task Amazon EC2 - Create Snapshot

The Amazon EC2 - Create snapshot Task creates a snapshot of an Amazon EBS volume, which Amazon stores in Amazon S3, using an Amazon Connection. Use snapshots for backups, to make copies of volumes, and to save data before you shut down an instance.

![EC2 - Create snapshot Task settings, with the Connection, Volume ID and Description fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/Create%20Snapshot.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### EC2 - Create snapshot tab

- _Connection_: the Amazon Connection to use; see [Connection - Amazon](../../connection-amazon). Click the button next to the list to manage Connections. The Client asks you to select a Connection before it saves the Task
- _Volume ID_: the ID of the EBS volume. Click the refresh button to fill the list with the volumes that the Server finds with the Connection. Variables are not resolved in this field
- _Description_: a description of the snapshot and what it is used for. Variables are not resolved in this field

### Output and errors

When the snapshot is created, the Task writes the ID of the new snapshot to the Task output.

When the Connection cannot be found, or Amazon returns an error, the Task fails. To change how the Task responds to errors, see [Task - On error](../../task-on-error).
