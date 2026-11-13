---
sidebar_label: 'Task Amazon EC2 - List Security Group'
hide_title: 'true'
---

## Task Amazon EC2 - List Security Group

The Amazon EC2 - List security group Task lists the security groups that match a filter, using an Amazon Connection.

![EC2 - List security group Task settings, with the Connection and Filter fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/List%20Security%20Group.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### EC2 - List security group tab

- _Connection_: the Amazon Connection to use; see [Connection - Amazon](../../connection-amazon). Click the button next to the list to manage Connections. The Client asks you to select a Connection before it saves the Task
- _Filter_: the filter for the security groups, in the format of the example below. Variables are not resolved in this field

:::tip Example

`@{Name="vpc-id"; Values="vpc-1a2b3c4d"}`

:::

### Output and errors

The Task writes one line for each security group to the Task output, with these values separated by `|`: description, group ID, group name, owner (AWS account) ID and VPC ID.

When the Connection cannot be found, or Amazon returns an error, the Task fails. To change how the Task responds to errors, see [Task - On error](../../task-on-error).
