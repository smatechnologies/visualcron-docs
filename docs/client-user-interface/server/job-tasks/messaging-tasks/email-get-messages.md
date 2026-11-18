---
sidebar_label: 'Task Messaging - Email - Get Messages'
hide_title: 'true'
---

## Task Messaging - Email - Get Messages

The Email - Get messages Task reads the messages in a mail folder that match its conditions and attachment filter, using a POP3, IMAP4, Exchange EWS, Exchange WebDAV or Microsoft Graph API Connection. It can save each message and its attachments to disk, mark it as read or delete it on the server, and it writes one line per message to the output.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Email - Get messages: Main settings tab

![Email - Get messages tab, Main settings tab with the Connection, Mail folder, Message on Server, Decryption by and Save email groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/email%20-%20get%20messages.png)

- _Connection_: the Connection to the mailbox, of one of these types: [Connection - POP3](../../connection-pop3), [Connection - IMAP4](../../connection-imap4), [Connection - Exchange EWS](../../connection-exchange-ews), [Connection - Exchange WebDAV](../../connection-exchange-webdav) or [Connection - Microsoft Graph API](../../connection-microsoft-graph-api)
- _Mail folder_: the folder to read
  - _Use default folder_ (default): the default folder of the mailbox, the Inbox
  - _Use specified folder_: type the folder path, or click the folder button to choose it from the server. Choosing is not possible with POP3, and with POP3 the setting is ignored. If the folder does not exist, the Task fails with the error `Folder "<name>" not found`
  - _Is public folder_: select it when the specified folder is an Exchange public folder. It is applied with Exchange EWS and Microsoft Graph API Connections only

- _Message on Server_: what happens on the server to each message that the Task reads
  - _Leave message on Server_ (default): the message is not deleted. It is marked as read if _Mark as read (not POP3)_ is selected
  - _Mark as read (not POP3)_: marks the message as read. It has no effect with POP3
  - _Delete message on Server_: deletes the message

:::warning

If _Mark as read (not POP3)_ is selected, the message is only marked as read, even when _Delete message on Server_ is selected. Clear _Mark as read (not POP3)_ to delete.

With _Delete message on Server_, the message is deleted even when an attachment was not saved: for example, when a file with the same name exists and neither _Overwrite existing_ nor _Expand existing file name_ is selected, or when saving fails. To keep such messages, select _Expand existing file name_ or _Overwrite existing_, or leave the messages on the server and delete them in a later Task.

Before you select _Delete message on Server_, check which messages match with the [Email - Get messages: Test tab](#email---get-messages-test-tab), or with an Email - Get headers Task that uses the same Connection, folder and conditions. With IMAP4 and Exchange WebDAV Connections, _From address_ conditions select more messages than their names say; see the [Email - Get messages: Conditions tab](#email---get-messages-conditions-tab).

:::

- _Decryption by..._: _Certificate_ is the certificate that decrypts encrypted messages; see [Global - Certificates](../../global-certificates)

:::warning

When a certificate is selected, an encrypted message that it decrypts is skipped: it is not saved, marked or deleted, and nothing is written to the output. An encrypted message that it cannot decrypt is skipped too. So with a certificate selected, this Task cannot save or delete encrypted messages. When no certificate is selected, or the selected certificate has been removed from [Global - Certificates](../../global-certificates), an encrypted message is processed as it is, still encrypted, and can be saved, marked or deleted.

:::

- _Save email_: what is saved to disk for each message
  - _Save email_: saves the whole message as an .eml file named after its ID. An existing file of that name is replaced
  - _Save attachment(s)_: saves the attachments that match the [Email - Get messages: Attachment filter tab](#email---get-messages-attachment-filter-tab)
  - _Overwrite existing_: replaces an attachment file of the same name. Enabled with _Save attachment(s)_. If neither this nor _Expand existing file name_ is selected, an existing file is kept and the attachment is not saved
  - _Expand existing file name_: when a file of the same name exists, adds a number to the new name, for example `report1.pdf`. Enabled with _Save attachment(s)_
  - _Save to default folder_ (default): saves under `<VisualCron installation folder>\data\email\`
  - _Save to folder_: saves under the folder you type. _Credential_ is used to access this folder, and only this folder
  - _Create folder tree based on each email_: selected by default. Each message gets a folder named after its ID: the message is saved as `<ID>\<ID>.eml`, and its attachments in `<ID>\attachments\`. When cleared, all files are saved directly in the folder

:::tip

In folder and file names, characters of the mail ID that are not allowed in file names are replaced with the Unicode replacement character, U+FFFD (�). To get the same name in another Task, apply the Variable function _Encode FileName (replace invalid chars with: provided masking string / empty string / unicode equivalents)_ under _File variables_ to the mail ID: `{PATH(EncodeFileName|<mail ID>|MASK)}`. `MASK` replaces each character that is not allowed with U+FFFD.

:::

### Email - Get messages: Conditions tab

The fields and limits are the same as on the ***Conditions*** tab of [Task Messaging - Email - Get Headers](email-get-headers). A message is read only when it matches every condition that is set.

:::warning

With IMAP4 and Exchange WebDAV Connections, every _From address_ condition acts as "Contains (=%)". "Not equal (!=)" and "Not contains (!=%)" select the messages from that address instead of excluding them, and "Equal (=)" also matches longer addresses that contain the value. With _Delete message on Server_, those messages are deleted. With POP3, Exchange EWS and Microsoft Graph API Connections, _From address_ is applied as set.

:::

### Email - Get messages: Attachment filter tab

The fields are the same as on the ***Attachment filter*** tab of [Task Messaging - Email - Get Headers](email-get-headers). When _File mask_ is not `*`, or a size check is selected, a message is read only when at least one attachment matches, and only the matching attachments are saved.

If both size checks are selected, the value of _Check if file is smaller than x size_ is treated as 0, so with "AND" no attachment matches. Select only one size check.

### Email - Get messages: Test tab

_Show filtered messages_ runs the current settings on the Server and shows the result. _Number lines in the result_ limits how many lines are shown. The test does not save, mark or delete any message.

### Output tab

The fields are the same as on the ***Output*** tab of [Task Messaging - Email - Get Headers](email-get-headers), and Body can also be chosen. Each line holds the fields chosen in _Show mail headers_. The paths of saved files are not written to the output. When _Include field names_ is selected together with _Save email_ or _Save attachment(s)_, the output starts with "Email file path" and "Attachment file path(s)" instead of the field names, joined to the first line with no line break.

### Output and errors

- When no message matches, the output is empty, and the Task succeeds
- If a message cannot be downloaded from the server, the Task stops with an error. Messages handled before it stay saved, marked or deleted
- If the Connection is missing, the Task fails with "Connection not found". If the specified folder does not exist, it fails with the error `Folder "<name>" not found` (the "No folder(s) found" cause on the ***On error*** tab)

:::warning

If an attachment cannot be saved, the error is written to the Server log, the message is still marked or deleted as selected, and the Task reports success.

If an attachment is not saved because a file of the same name exists and neither _Overwrite existing_ nor _Expand existing file name_ is selected, no error is raised, the message is still marked or deleted as selected, and the Task reports success.

If the .eml file of a message cannot be saved, or the message cannot be deleted on the server, the error is written to the Server log, the Task goes on with the next message, and the Task reports success. A message whose .eml file was not saved is not marked or deleted, and no line is written for it.

If a message cannot be marked as read, the error is written to the Server log, the message stays unread, and the Task reports success.

:::