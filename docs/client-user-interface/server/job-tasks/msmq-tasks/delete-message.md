---
sidebar_label: 'Task MSMQ - Delete Message'
hide_title: 'true'
---

## Task MSMQ - Delete Message

The MSMQ - Delete message(s) Task deletes messages from a Microsoft Message Queuing (MSMQ) queue on the Server computer or on a remote computer. Filters select which messages are deleted.

![MSMQ - Delete message(s) tab, with the scope, the queue and the filters](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/MSMQ%20Tasks/MSMQ%20-%20delete%20message.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### MSMQ - Delete message(s) tab

**Scope**

- _Credential_: the Credential the Task runs as when it connects to the queue. Available with _Remote MSMQ_. A Credential saved earlier is still used after switching to _Local MSMQ_; see [Credentials](../../global-credentials)
- _Local MSMQ_ (default): the queue is on the Server computer
- _Remote MSMQ_: the queue is on another computer
- _Host name_: the host name or IP address of the remote computer. Available with _Remote MSMQ_

**Queue**

The queue to delete messages from. The journal queue of a private queue is listed as well. Click the refresh button to fill the list with the queues of the selected computer.

**Filters**

A message is deleted when it matches every checked filter.

- _Label filter_: compares the label of the message with the value: `Equal (=)` (default), `Not equal (!=)`, `Contains (=%)` or `Not contains (!=%)`
- _Message filter_: compares the body of the message with the value, with the same comparisons as _Label filter_
- _Date filter_: compares the time the message arrived in the queue with the date: `Smaller than (<)` (default) or `Larger than (>)`. The default date, `{DATENOWADD(Days|-7|yyyy-MM-dd)}`, is seven days ago
- _Limit and sort direction of date_: deletes at most the number of messages entered, "10" by default, taking the oldest first with "Ascending" (default) or the newest first with "Descending"

Each value may contain Variables; click the Variable button next to it.

:::warning

With no filter checked, every message in the queue is deleted.

:::

### Output and errors

The output is the number of messages deleted, for example "Deleted 3 message(s)". If the queue cannot be read, the Task fails.
