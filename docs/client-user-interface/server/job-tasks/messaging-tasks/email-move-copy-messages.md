---
sidebar_label: 'Task Messaging - Email - Move/Copy Messages'
hide_title: 'true'
---

## Task Messaging - Email - Move/Copy Messages

The Email Move/Copy Messages Task moves or copies one or more messages from one mail folder to another. Messages matching the configured conditions are moved or copied to the specified destination folder.

:::tip Supported protocols

This task supports **IMAP4**, **Exchange EWS**, and **Microsoft Graph** connections. POP3 does not support move/copy operations. When using a Microsoft Graph connection, messages are moved or copied via the Graph API with batch processing for large result sets.

:::

**Email - Move/Copy messages > Main settings** sub tab

**Connection**

To use Email Tasks you need to create a [Connection](../../../server/global-connections) first. Click the Settings icon to open the Manage Connections dialog. Supported connection types: [IMAP4](../../../server/connection-imap4), [Exchange EWS](../../../server/connection-exchange-ews), and [Microsoft Graph](../../../server/connection-microsoft-graph).

**Mail folder**

The source folder to move or copy messages from. Change to Use specified folder and use manual folder specification or click the Folder icon. When using Microsoft Graph, you can specify a folder by display name (e.g., `Inbox`). VisualCron resolves the folder name to the Graph folder ID automatically.

**Action**

Select the operation to perform:

* **Move** — moves matching messages to the destination folder (removes from source folder)
* **Copy** — copies matching messages to the destination folder (leaves originals in source folder)

**Destination folder**

The target folder for moved or copied messages. You can specify a folder by name or browse for it using the Folder icon. When using Microsoft Graph, folder names are resolved to Graph folder IDs automatically.

**Decryption by**

If email decryption is used, enter certificate name.

**Email - Move/Copy messages > Conditions** sub tab

See the [Task Messaging - Email - Get headers](email-get-headers) > **Email - Get headers > Conditions** sub tab

**Email - Move/Copy messages > Attachment filter** sub tab

See the [Task Messaging - Email - Get headers](email-get-headers) > **Email - Get headers > Attachment filter** sub tab
