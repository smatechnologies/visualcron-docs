---
sidebar_label: 'Task Amazon EC2 - List Instance'
hide_title: 'true'
---

## Task Amazon EC2 - List Instance

The Amazon EC2 - List instance(s) Task lists existing Amazon EC2 instances that match a filter, using an Amazon Connection.

![EC2 - List instance(s) Task settings, with the Connection and Filter fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/List%20Instance(s).png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### EC2 - List instance(s) tab

- _Connection_: the Amazon Connection to use; see [Connection - Amazon](../../connection-amazon). Click the button next to the list to manage Connections. The Client asks you to select a Connection before it saves the Task
- _Filter_: the filter for the instances, in the format of the example below. Variables are not resolved in this field

:::tip Example

`@{Name="instance-type"; Values=("t2.micro","m1.medium")}`

:::

### Output and errors

The Task writes one line for each instance to the Task output, with these values separated by `|`: architecture, hypervisor, image ID, instance ID, kernel ID, key name, launch time, private DNS name, private IP address, root device name, root device type, subnet ID, state transition reason, virtualization type and VPC ID.

When the Connection cannot be found, or Amazon returns an error, the Task fails. To change how the Task responds to errors, see [Task - On error](../../task-on-error).
