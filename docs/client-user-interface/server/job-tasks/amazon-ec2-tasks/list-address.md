---
sidebar_label: 'Task Amazon EC2 - List Address'
hide_title: 'true'
---

## Task Amazon EC2 - List Address

The Amazon EC2 - List address(es) Task requests the Elastic IP addresses that match a filter, using an Amazon Connection.

![EC2 - List address(es) Task settings, with the Connection and Filter fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/List%20Address(es).png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### EC2 - List address(es) tab

- _Connection_: the Amazon Connection to use; see [Connection - Amazon](../../connection-amazon). Click the button next to the list to manage Connections. The Client asks you to select a Connection before it saves the Task
- _Filter_: the filter for the Elastic IP addresses, in the format of the example below. Variables are not resolved in this field

:::tip Example

`@{Name="domain"; Values="vpc"}`

:::

:::warning

The Task output holds only empty lines, one for each address: it does not contain the addresses or their properties, and the Task reports success. To read the addresses, use the AWS console or tools.

:::

### Output and errors

The Task writes one empty line for each address that Amazon returns, and no address details.

When the Connection cannot be found, or Amazon returns an error, the Task fails. To change how the Task responds to errors, see [Task - On error](../../task-on-error).
