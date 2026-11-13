---
sidebar_label: 'Task MSMQ - Send Message'
hide_title: 'true'
---

## Task MSMQ - Send Message

The MSMQ - Send message Task sends a message to a Microsoft Message Queuing (MSMQ) queue on the Server computer or on a remote computer.

![MSMQ - Send message tab, with the scope, the queue and the message settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/MSMQ%20Tasks/MSMQ%20-%20send%20message.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### MSMQ - Send message tab

**Scope**

- _Credential_: the Credential the Task runs as when it connects to the queue. Available with _Remote MSMQ_. A Credential saved earlier is still used after switching to _Local MSMQ_; see [Credentials](../../global-credentials)
- _Local MSMQ_ (default): the queue is on the Server computer
- _Remote MSMQ_: the queue is on another computer
- _Host name_: the host name or IP address of the remote computer. Available with _Remote MSMQ_

**Queue**

The queue to send the message to. A journal queue cannot be used. Click the refresh button to fill the list with the queues of the selected computer.

**Message**

- _Label_: the label of the message. Required
- _Message serialization_: how the message body is written to the queue:
  - "Xml serialization" (default): as XML
  - "String serialization": as a string
  - "Binary serialization": as binary data
- _Message_: the body of the message. Required

Label and message may contain Variables.

### Output and errors

The output is the label of the sent message. If the queue is not found or the message cannot be sent, the Task fails.
