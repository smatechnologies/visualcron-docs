---
sidebar_label: 'Task Messaging - Email - Delete Messages'
hide_title: 'true'
---

## Task Messaging - Email - Delete Messages

The Email - Delete messages Task deletes the messages in a mail folder that match its conditions and attachment filter, using a POP3, IMAP4, Exchange EWS, Exchange WebDAV or Microsoft Graph API Connection.

:::warning

The Task deletes every message in the folder that matches the [Email - Delete messages: Conditions tab](#email---delete-messages-conditions-tab) and the [Email - Delete messages: Attachment filter tab](#email---delete-messages-attachment-filter-tab). The Task window's ***Conditions*** tab only decides whether the Task runs; it does not select messages. With the default settings nothing is filtered, so every message in the folder is deleted. VisualCron keeps no copy of a deleted message. Before you schedule the Task, set at least one condition on the [Email - Delete messages: Conditions tab](#email---delete-messages-conditions-tab), and run an Email - Get headers Task with the same Connection, folder and conditions to see which messages match; see [Task Messaging - Email - Get Headers](email-get-headers).

With an Exchange EWS Connection, the _From address_, _Subject_ and _Body_ conditions are not applied when deleting. Only _Read option_, _Received date_ and the attachment filter are, so Email - Get headers with the same conditions can list fewer messages than this Task deletes. With IMAP4 and Exchange WebDAV Connections, _From address_ does not work as its list values say; see the [Email - Delete messages: Conditions tab](#email---delete-messages-conditions-tab).

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Email - Delete messages: Main settings tab

![Email - Delete messages tab, Main settings tab with the Connection, Mail folder and Decryption by groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20delete%20messages.png)

- _Connection_: the Connection to the mailbox, of one of these types: [Connection - POP3](../../connection-pop3), [Connection - IMAP4](../../connection-imap4), [Connection - Exchange EWS](../../connection-exchange-ews), [Connection - Exchange WebDAV](../../connection-exchange-webdav) or [Connection - Microsoft Graph API](../../connection-microsoft-graph-api)
- _Mail folder_: the folder to delete from
  - _Use default folder_ (default): the default folder of the mailbox, the Inbox
  - _Use specified folder_: type the folder path, or click the folder button to choose it from the server. Choosing is not possible with POP3, and with POP3 the setting is ignored. If the folder does not exist, the Task fails with the error `Folder "<name>" not found`
  - _Is public folder_: select it when the specified folder is an Exchange public folder. It is applied with Exchange EWS and Microsoft Graph API Connections only
- _Decryption by..._: _Certificate_ is the certificate that decrypts encrypted messages; see [Global - Certificates](../../global-certificates). An encrypted message is skipped, and not deleted, when no certificate is selected or the certificate cannot decrypt it

### Email - Delete messages: Conditions tab

The fields and their limits are the same as on the ***Conditions*** tab of [Task Messaging - Email - Get Headers](email-get-headers): _From address_, _Subject_, _Body_, _Received date_ and _Read option_. A message is deleted only when it matches every condition that is set. On this Task, these limits apply too:

- With an Exchange EWS Connection, _From address_, _Subject_ and _Body_ are not applied
- With a POP3 Connection, _Read option_ is not applied, so _Only read emails_ and _Only unread emails_ delete all matching messages
- With an Exchange EWS Connection, "Equal (=)" on _Received date_ does not need the exact time: when the value has no seconds, the date is compared to the minute; with no minutes either, to the hour; and with no time, to the day

:::warning

With IMAP4 and Exchange WebDAV Connections, every _From address_ condition acts as "Contains (=%)". "Not equal (!=)" and "Not contains (!=%)" select the messages from that address for deletion instead of excluding them, and "Equal (=)" also matches longer addresses that contain the value. _From address_ is applied as set only with POP3 and Microsoft Graph API Connections. Before you schedule the Task, run an Email - Get headers Task with the same Connection, folder and conditions, and check which messages it lists.

:::

### Email - Delete messages: Attachment filter tab

The fields are the same as on the ***Attachment filter*** tab of [Task Messaging - Email - Get Headers](email-get-headers). When _File mask_ is not `*`, or a size check is selected, a message is deleted only when it has attachments and every attachment matches. Email - Get headers lists a message when any attachment matches, so it can list messages that this Task does not delete.

### Output and errors

- For each deleted message, standard output has the line `<ID> successfully deleted`
- When no message matches, the output is "No messages to delete", and the Task succeeds
- If a message cannot be downloaded from the server, the Task stops with an error. Messages deleted before it stay deleted
- If the Connection is missing, the Task fails with "Connection not found". If the specified folder does not exist, it fails with the error `Folder "<name>" not found` (the "No folder(s) found" cause on the ***On error*** tab)

:::warning

If a message is downloaded but cannot be deleted, the error is written to the Server log, no line is written for that message, the Task goes on with the next message, and the Task reports success.

An encrypted message that is skipped because no certificate is selected, or because the certificate cannot decrypt it, is not deleted, no line is written for it, and the Task reports success.

:::