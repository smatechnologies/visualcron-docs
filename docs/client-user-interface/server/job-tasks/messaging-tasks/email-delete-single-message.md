---
sidebar_label: 'Task Messaging - Email - Delete Single Message'
hide_title: 'true'
---

## Task Messaging - Email - Delete Single Message

The Email Delete Single Message Task removes one message by its message ID or message index number.

:::tip Supported protocols

This task supports **POP3**, **IMAP4**, **Exchange EWS**, and **Microsoft Graph** connections. When using a Microsoft Graph connection, the message is deleted by its Graph message ID.

:::

**Email - Delete single message** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20delete%20single%20message.png)

**Connection**

To use Email Tasks you need to create a [Connection](../../../server/global-connections) first. Click the *Settings* icon to open the *Manage Connections* dialog. Supported connection types: [POP3](../../../server/connection-pop3), [IMAP4](../../../server/connection-imap4), [Exchange EWS](../../../server/connection-exchange-ews), and [Microsoft Graph](../../../server/connection-microsoft-graph).

**Mail identifier**

Specify mail ID or index number for message that is to be deleted. When using a Microsoft Graph connection, use the Graph message ID.
