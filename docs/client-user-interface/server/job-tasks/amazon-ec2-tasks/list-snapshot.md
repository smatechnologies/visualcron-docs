---
sidebar_label: 'Task Amazon EC2 - List Snapshot'
hide_title: 'true'
---

## Task Amazon EC2 - List Snapshot

The Amazon EC2 - List snapshot(s) Task lists the Amazon EBS snapshots that are available to you and match a filter, using an Amazon Connection. Snapshots available to you include public snapshots, private snapshots that you own, and private snapshots owned by another AWS account that has given you explicit create volume permissions.

![EC2 - List snapshot(s) Task settings, with the Connection and Filter fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/List%20Snapshot(s).png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### EC2 - List snapshot(s) tab

- _Connection_: the Amazon Connection to use; see [Connection - Amazon](../../connection-amazon). Click the button next to the list to manage Connections. The Client asks you to select a Connection before it saves the Task
- _Filter_: the filter for the snapshots, in the format of the example below. Variables are not resolved in this field

:::tip Example

`@{Name="owner-alias"; Values="self"}`

:::

### Output and errors

The Task writes one line for each snapshot to the Task output, with these values separated by `|`: description, owner (AWS account) ID, progress, snapshot ID, start date, state, volume ID and volume size.

When the Connection cannot be found, or Amazon returns an error, the Task fails. To change how the Task responds to errors, see [Task - On error](../../task-on-error).
