---
sidebar_label: 'Task Amazon EC2 - List Volume'
hide_title: 'true'
---

## Task Amazon EC2 - List Volume

The Amazon EC2 - List volume(s) Task lists the Amazon EBS volumes that match a filter, with their status properties, using an Amazon Connection.

![EC2 - List volume(s) Task settings, with the Connection, Filter and Volume Ids fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/List%20Volume(s).png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### EC2 - List volume(s) tab

- _Connection_: the Amazon Connection to use; see [Connection - Amazon](../../connection-amazon). Click the button next to the list to manage Connections. The Client asks you to select a Connection before it saves the Task
- _Filter_: the filter for the volumes, in the format of the example below. Variables are not resolved in this field
- _Volume Ids_: shown in the Client, but not used when the Task runs. To list particular volumes, use _Filter_

:::tip Example

`@{Name="status"; Values="available"}`

:::

### Output and errors

The Task writes one line for each volume to the Task output, with these values separated by `|`: availability zone, creation time, IOPS, size, snapshot ID, state, volume ID and volume type.

When the Connection cannot be found, or Amazon returns an error, the Task fails. To change how the Task responds to errors, see [Task - On error](../../task-on-error).
