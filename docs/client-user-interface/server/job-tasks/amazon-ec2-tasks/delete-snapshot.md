---
sidebar_label: 'Task Amazon EC2 - Delete Snapshot'
hide_title: 'true'
---

## Task Amazon EC2 - Delete Snapshot

The Amazon EC2 - Delete snapshot Task deletes an Amazon EBS snapshot, using an Amazon Connection. Periodic snapshots of a volume are incremental: each new snapshot saves only the blocks that changed since the last one.

![EC2 - Delete snapshot Task settings, with the Connection and Snapshots fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/Delete%20Snapshot.png)

:::warning

The Task deletes the snapshot in AWS. VisualCron cannot undo the deletion.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### EC2 - Delete snapshot tab

- _Connection_: the Amazon Connection to use; see [Connection - Amazon](../../connection-amazon). Click the button next to the list to manage Connections. The Client asks you to select a Connection before it saves the Task
- _Snapshots_: the ID of the snapshot to delete. Click the refresh button to fill the list with the snapshots that the Server finds with the Connection. Variables are not resolved in this field

### Output and errors

When the snapshot is deleted, the Task writes the snapshot ID that Amazon returns to the Task output.

When the Connection cannot be found, or Amazon returns an error, the Task fails. To change how the Task responds to errors, see [Task - On error](../../task-on-error).
