---
sidebar_label: 'Task MSMQ - Send Message'
hide_title: 'true'
---

## Task MSMQ - Send Message

The MSMQ - Send message Task sends a message to the specified queue.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/MSMQ%20Tasks/MSMQ%20-%20send%20message.png)

**Local MSMQ**

Select this radio button if the queue is hosted on the local computer.

**Remote MSMQ**

Select this radio button if the queue is hosted on a remote computer. The *Credential* and *Host name* fields below are enabled only when this option is selected.

**Credential**

Select a [Credential](../../global-credentials) for connecting to the remote computer. The Credential must match a user name and password that has access to the remote MSMQ host. Click the *Settings* icon to open *Manage credentials* in order to add or edit Credentials.

**Host name**

The host name or IP address of the remote computer.

**Queue**

The name of the queue to send the message to. Click the *Refresh* icon to populate the drop-down list of available queues on the selected MSMQ host.

**Label**

The label of the message to be sent. Required.

**Message**

The text of the message to be sent. Required.

**Message serialization**

Selects how the message body is serialized when written to the queue. Available options:

* _Xml serialization_ - serialize the message as XML (default)
* _String serialization_ - serialize the message as a plain string
* _Binary serialization_ - serialize the message as a binary payload
