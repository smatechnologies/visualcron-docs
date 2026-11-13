---
sidebar_label: 'Task Messaging - Email - Delete Single Message'
hide_title: 'true'
---

## Task Messaging - Email - Delete Single Message

The Email - Delete single message Task deletes one message, found by its ID or its index, using a POP3, IMAP4, Exchange EWS, Exchange WebDAV or Microsoft Graph API Connection.

:::warning

If both _ID_ and _Index_ are filled in, the Task deletes the first message in the folder whose ID or index matches, which can be a different message from the one that _ID_ names. Fill in only _ID_. VisualCron keeps no copy of a deleted message.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Email - Delete single message tab

![Email - Delete single message tab with the Connection and Mail identifier groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20delete%20single%20message.png)

- _Connection_: the Connection to the mailbox, of one of these types: [Connection - POP3](../../connection-pop3), [Connection - IMAP4](../../connection-imap4), [Connection - Exchange EWS](../../connection-exchange-ews), [Connection - Exchange WebDAV](../../connection-exchange-webdav) or [Connection - Microsoft Graph API](../../connection-microsoft-graph-api)
- _Mail identifier_: fill in _ID_ or _Index_
  - _ID_: the unique ID of the message, as written in the ID field by [Task Messaging - Email - Get Headers](email-get-headers). Variables are resolved
  - _Index_: the position of the message in the folder. It changes as messages arrive or are deleted, so prefer _ID_

The message is looked up in the default folder of the mailbox, the Inbox, only.

### Output and errors

- When the message is deleted, standard output has the line `<ID> successfully deleted`
- If the message cannot be deleted, the Task fails
- If the Connection is missing, the Task fails with "Connection not found"

:::warning

When no message matches, "Message not found or already deleted" or "Message not found" is written to standard error, and the Task reports success.

:::