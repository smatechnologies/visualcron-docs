---
sidebar_label: 'Task Messaging - SNS - Publish Message'
hide_title: 'true'
---

## Task Messaging - Amazon SNS - Publish Message

The Amazon SNS - Publish message Task publishes a message to one or more Amazon SNS topics, or as an SMS to a phone number, using an Amazon Connection.

![Amazon SNS - Publish message tab with the Connection, Message parameters and Message attributes groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Amazon%20SNS%20-%20publish%20message.png)

:::warning

This Task uses an Amazon Connection; see [Connection - Amazon](../../connection-amazon). The Task does not use the proxy set on the Connection, and it signs requests only with the _Access Key ID_ and _Secret Access Key_ of the Connection: "Public key" authentication is not used.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::note

The Amazon SNS - Publish message Task is part of the Advanced messaging feature of the license.

:::

### Amazon SNS - Publish message tab

#### Connection

- _Connection_: the Amazon Connection of the AWS account that holds the topics; see [Connection - Amazon](../../connection-amazon)

  The Task publishes in the region set on the Connection.

#### Message parameters

- _Topic name_: the name of the topic to publish to

  Click the refresh button next to the field to list the topics of the account. To publish to several topics, separate the names with commas and no spaces, as in `<topic 1>,<topic 2>`. The Task publishes to every topic whose name matches exactly. Variables are not resolved when the names are matched, so enter the names as text.

  Either _Topic name_ or _Phone number_ is required. When _Topic name_ has a value, _Phone number_ is not used.

- _Target_: when selected, the ARN of each matched topic is sent as the target ARN instead of the topic ARN

  _Topic name_ is still matched against topic names, so the Task cannot publish to a platform endpoint ARN.

- _Phone number_: the phone number to send the message to as an SMS; used only when _Topic name_ is empty
- _Subject_: the subject that the Task passes to Amazon SNS with the message. Amazon SNS uses it, for example, as the subject line of the notification that email subscribers receive
- _Message_: the text to publish, or the JSON document when the check box below it is selected
- _Different payloads are sent to endpoints subscribed to the topic, based on their delivery protocol._: when selected, _Message_ is sent as a JSON document with a separate message for each delivery protocol, for example `default`, `email` and `sms`

  When cleared, every subscriber gets the same _Message_ text.

Variables are resolved in _Phone number_, _Subject_ and _Message_.

#### Message attributes

The _Message attributes (double click to edit)_ grid holds the attributes sent with the message. Click _Add_, _Edit_, _Delete_ or _Clear all_, or double-click a row to edit it.

:::warning

Removing every attribute is currently not saved: when the grid is empty, the Task keeps the attributes it had and still sends them. To stop sending attributes, create the Task again without them.

:::

In the _Add/Edit message attribute value_ window:

- _Value type_: "String", "String.Array", "Number" or "Binary"
- _Name_: the name of the attribute
- _Value_: the value, sent exactly as entered

  Variables are not resolved in attribute values; _Variables_ only opens the list of Variables. For "String.Array", separate the values with commas; they are sent as a JSON array of strings. For "Binary", enter the value as Base64.

- _Is null_: when selected, _Value_ is unavailable and the text "(Null)" is sent as the value

  With "Binary", _Is null_ makes the Task fail.

### Output and errors

For each topic published to, `<topic name>: Success` is added to the output, with no separator between topics. For an SMS, the output is `<phone number>: Success`. If an attribute value cannot be read, for example a "Binary" value that is not Base64, the Task fails.

:::warning

If Amazon SNS rejects a request, the error is written to standard error, the topics after the one that failed are not published to, and the Task reports success. If no topic matches _Topic name_, nothing is published, and the Task reports success.

:::
