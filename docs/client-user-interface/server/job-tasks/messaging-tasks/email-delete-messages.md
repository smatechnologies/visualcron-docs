---
sidebar_label: 'Task Messaging - Email - Delete Messages'
hide_title: 'true'
---

## Task Messaging - Email - Delete Messages

The Email Delete Messages Task removes one or more messages.

:::tip Supported protocols

This task supports **POP3**, **IMAP4**, **Exchange EWS**, and **Microsoft Graph** connections. When using a Microsoft Graph connection, messages matching the filter conditions are deleted via the Graph API.

:::

**Email - Delete messages > Main settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20delete%20messages.png)

**Connection**

To use Email Tasks you need to create a [Connection](../../../server/global-connections) first. Click the Settings icon to open the Manage Connections dialog. Supported connection types: [POP3](../../../server/connection-pop3), [IMAP4](../../../server/connection-imap4), [Exchange EWS](../../../server/connection-exchange-ews), and [Microsoft Graph](../../../server/connection-microsoft-graph).

**Mail folder**

If desired, change to Use specified folder and use manual folder specification or click the Folder icon. When using Microsoft Graph, you can specify a folder by display name (e.g., `Inbox`, `Deleted Items`). VisualCron resolves the folder name to the Graph folder ID automatically.

**Decryption by**

If email decryption is used, enter certificate name.

**Email - Delete messages > Conditions** sub tab

See the [Task Messaging - Email - Get headers](email-get-headers) > **Email - Get headers > Conditions** sub tab

**Email - Delete messages > Attachment filter** sub tab

See the [Task Messaging - Email - Get headers](email-get-headers) > **Email - Get headers > Attachment filter** sub tab
