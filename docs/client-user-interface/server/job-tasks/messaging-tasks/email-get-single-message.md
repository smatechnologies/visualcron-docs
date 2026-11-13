---
sidebar_label: 'Task Messaging - Email - Get Single Messages'
hide_title: 'true'
---

## Task Messaging - Email - Get Single Message

The Email - Get single message Task reads one message, found by its ID or its index, using a POP3, IMAP4, Exchange EWS, Exchange WebDAV or Microsoft Graph API Connection. It can save the message and its attachments to disk, mark it as read or delete it on the server.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Email - Get single message: Main settings tab

![Email - Get single message tab, Main settings tab with the Connection, Mail identifier, Mail folder, Message on Server, Decryption by and Save email groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/email%20-%20get%20single%20messages.png)

- _Connection_: the Connection to the mailbox, of one of these types: [Connection - POP3](../../connection-pop3), [Connection - IMAP4](../../connection-imap4), [Connection - Exchange EWS](../../connection-exchange-ews), [Connection - Exchange WebDAV](../../connection-exchange-webdav) or [Connection - Microsoft Graph API](../../connection-microsoft-graph-api)
- _Mail identifier_: fill in _ID_ or _Index_
  - _ID_: the unique ID of the message, as written in the ID field by [Task Messaging - Email - Get Headers](email-get-headers). Variables are resolved
  - _Index_: the position of the message in the folder. It changes as messages arrive or are deleted, so prefer _ID_

  If both are filled in, the Task takes the first message in the folder whose ID or index matches, which can be a different message from the one that _ID_ names. Fill in only _ID_, in particular with _Delete message on Server_.

- _Mail folder_: the folder that holds the message
  - _Use default folder_ (default): the default folder of the mailbox, the Inbox
  - _Use specified folder_: type the folder path, or click the folder button to choose it from the server. Choosing is not possible with POP3, and with POP3 the setting is ignored. If the folder does not exist, the Task fails with the error `Folder "<name>" not found`
  - _Is public folder_: select it when the specified folder is an Exchange public folder. It is applied with Exchange EWS and Microsoft Graph API Connections only

- _Message on Server_: what happens on the server to the message
  - _Leave message on Server_ (default): the message is not deleted. It is marked as read if _Mark as read (not POP3)_ is selected
  - _Mark as read (not POP3)_: marks the message as read. It has no effect with POP3
  - _Delete message on Server_: deletes the message

:::warning

If _Mark as read (not POP3)_ is selected, the message is only marked as read, even when _Delete message on Server_ is selected. Clear _Mark as read (not POP3)_ to delete.

With _Delete message on Server_, the message is deleted even when an attachment was not saved: for example, when a file with the same name exists and neither _Overwtite existing_ nor _Expand existing file name_ is selected, or when saving fails. To keep the message, select _Expand existing file name_ or _Overwtite existing_, or leave the message on the server and delete it in a later Task.

:::

- _Decryption by..._: _Certificate_ is the certificate that decrypts an encrypted message; see [Global - Certificates](../../global-certificates). If the message is encrypted and no certificate is selected, or the certificate cannot decrypt it, the message is not saved, marked or deleted
- _Save email_: what is saved to disk
  - _Save email_: saves the whole message as an .eml file named after its ID. An existing file of that name is replaced
  - _Save attachment(s)_: saves the attachments that match the [Email - Get single message: Attachment filter tab](#email---get-single-message-attachment-filter-tab)
  - _Overwtite existing_: replaces an attachment file of the same name. Enabled with _Save attachment(s)_. If neither this nor _Expand existing file name_ is selected, an existing file is kept and the attachment is not saved
  - _Expand existing file name_: when a file of the same name exists, adds a number to the new name, for example `report1.pdf`. Enabled with _Save attachment(s)_
  - _Save to default folder_ (default): saves under `<VisualCron installation folder>\data\email\`
  - _Save to folder_: saves under the folder you type. _Credential_ is used to access this folder, and only this folder
  - _Create folder tree based on each email_: selected by default. The message gets a folder named after its ID: it is saved as `<ID>\<ID>.eml`, and its attachments in `<ID>\attachments\`. When cleared, all files are saved directly in the folder

:::tip

In folder and file names, characters of the mail ID that are not allowed in file names are replaced with the Unicode replacement character, U+FFFD (�). To get the same name in another Task, apply the Variable function _Encode FileName (replace invalid chars with: provided masking string / empty string / unicode equivalents)_ under _File variables_ to the mail ID: `{PATH(EncodeFileName|<mail ID>|MASK)}`. `MASK` replaces each character that is not allowed with U+FFFD.

:::

### Email - Get single message: Attachment filter tab

The fields are the same as on the ***Attachment filter*** tab of [Task Messaging - Email - Get Headers](email-get-headers). Here the filter only chooses which attachments are saved; it does not decide whether the message is read.

### Email - Get single message: Test tab

_Test get message_ runs the current settings on the Server and shows the result. The test does not save, mark or delete the message.

### Output tab

The fields are the same as on the ***Output*** tab of [Task Messaging - Email - Get Headers](email-get-headers), and Body can also be chosen. When _Save email_ or _Save attachment(s)_ is selected, the output line lists the saved paths instead: the .eml file path, then _Field separator_ when attachments are saved too, then the paths of the attachment files that were written, separated by `;`. With _Include field names_, the line starts with "EMail file path" and "Attachment file path(s)", with no line break before the paths. Otherwise the line holds the fields chosen in _Show mail headers_.

### Output and errors

- If the message cannot be downloaded from the server, the Task fails
- If the Connection is missing, the Task fails with "Connection not found". If the specified folder does not exist, it fails with the error `Folder "<name>" not found`

:::warning

When no message matches, "Message not found" is written to standard error, and the Task reports success.

If the message is encrypted and cannot be decrypted, or its .eml file cannot be saved, nothing is written to the output, the message is not marked or deleted, and the Task reports success.

If an attachment cannot be saved, the error is written to the Server log, the message is still marked or deleted as selected, and the Task reports success.

If an attachment is not saved because a file of the same name exists and neither _Overwtite existing_ nor _Expand existing file name_ is selected, no error is raised, the message is still marked or deleted as selected, and the Task reports success.

If the message cannot be deleted on the server, the error is written to the Server log, nothing is written to the output, and the Task reports success. If it cannot be marked as read, the error is written to the Server log, and the Task reports success.

:::