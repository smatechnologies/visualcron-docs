---
sidebar_label: 'Task Amazon EC2 - List Key Pairs'
hide_title: 'true'
---

## Task Amazon EC2 - List Key Pairs

The Amazon EC2 - List key pair(s) Task is meant to list your key pairs, using an Amazon Connection.

![EC2 - List key pair Task settings, with the Connection and Filter fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Amazon%20EC2%20Tasks/List%20Key%20Pair.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### EC2 - List key pair tab

- _Connection_: the Amazon Connection to use; see [Connection - Amazon](../../connection-amazon). Click the button next to the list to manage Connections. The Client asks you to select a Connection before it saves the Task
- _Filter_: the filter for the key pairs, in the format of the example below. Variables are not resolved in this field

:::tip Example

`@{Name="key-name"; Values="websvr-keypair"}`

:::

:::warning

The Task does not send a request to Amazon and does not use its settings: it writes no output, and the Task reports success. To see your key pairs, use the AWS console or tools, or the refresh button of _Key pair name_ in the [Launch Instance](launch-instance) Task.

:::

### Output and errors

The Task writes no output and does not fail, even when the Connection does not exist.
