---
sidebar_label: 'Task Messaging - Telegram - User Send Message'
hide_title: 'true'
---

## Task Messaging - Telegram - User Send Message

The Telegram - User Send message Task sends a Telegram message from a Telegram user account to another Telegram user, using a Telegram Connection.

![Telegram - User Send message tab, Message tab with the Connection, Phone number and Message fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Telegram%20-%20user%20send%20message.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Telegram - User Send message: Message tab

- _Connection_: the Telegram Connection of the user account that sends the message; see [Connection - Telegram](../../connection-telegram)

  Required. The Task uses the proxy set on the Connection.

- _Phone number_: the phone number of the recipient

  Enter it with the country code, as in `+<country code><phone number>`. The Task window does not check this value.

- _Message_: the text to send

  Required: the Task cannot be saved while it is empty.

Variables are resolved in _Phone number_ and _Message_.

### Output and errors

The output of the Task is the response from Telegram. If the Connection cannot sign in, or Telegram rejects the message, the Task fails.
