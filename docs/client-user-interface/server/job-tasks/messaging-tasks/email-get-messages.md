---
sidebar_label: 'Task Messaging - Email - Get Messages'
hide_title: 'true'
---

## Task Messaging - Email - Get Messages

The Email Get Messages Task retrieves one or more messages.

:::tip Supported protocols

This task supports **POP3**, **IMAP4**, **Exchange EWS**, and **Microsoft Graph** connections. When using a Microsoft Graph connection, messages are retrieved via the Graph API with support for server-side OData filtering, automatic paging for large result sets, and folder resolution by display name.

:::

**Email - Get messages > Main settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/email%20-%20get%20messages.png)

**Connection**

To use Email Tasks you need to create a [Connection](../../../server/global-connections) first. Click the Settings icon to open the Manage Connections dialog. Supported connection types: [POP3](../../../server/connection-pop3), [IMAP4](../../../server/connection-imap4), [Exchange EWS](../../../server/connection-exchange-ews), and [Microsoft Graph](../../../server/connection-microsoft-graph).

**Mail folder**

If desired, change to Use specified folder and use manual folder specification or click the Folder icon. When using Microsoft Graph, you can specify a folder by display name (e.g., `Inbox`, `Archive`). VisualCron resolves the folder name to the Graph folder ID automatically.

**Message on server**

If desired, change message on server options.

**Decryption by**

If email decryption is used, enter certificate name.

**Save email**

If desired, change save email options. For credential, click the Settings icon to open the Manage Credentials dialog.

**Email - Get messages > Conditions** sub tab

See the [Task Messaging - Email - Get headers](email-get-headers) > **Email - Get headers > Conditions** sub tab

**Email - Get messages > Attachment filter** sub tab

See the [Task Messaging - Email - Get headers](email-get-headers) > **Email - Get headers > Attachment filter** sub tab
