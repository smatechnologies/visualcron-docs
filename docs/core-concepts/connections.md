---
sidebar_label: 'Connections'
sidebar_position: 5
description: Shared connection objects in VisualCron — configure once, reuse everywhere.
---

# Connections

A **connection** is a reusable, centrally-stored configuration for connecting to an external system — an FTP server, SQL database, email server, cloud storage provider, and more.

Connections are managed at **Server > Global Objects > Connections**.

## Why connections matter

Instead of entering server addresses, credentials, and settings in every task:

1. Create a connection once
2. Reference it from any task or trigger that needs it
3. When settings change (e.g., a password rotation), update the connection in one place — all tasks using it update automatically

## Supported connection types

| Protocol | Use case |
|----------|---------|
| FTP / FTPS (Implicit/Explicit) / TLS | File transfer |
| SFTP | Secure file transfer |
| SCP | Secure copy |
| SSH | Remote command execution |
| TCP | Raw TCP communication |
| SMTP | Send email |
| POP3 | Receive email |
| IMAP | Receive email |
| Exchange EWS | Microsoft Exchange email/calendar |
| Microsoft Graph | Microsoft 365 (OAuth) |
| WebDAV | WebDAV file operations |
| SQL | Database queries (any ADO.NET provider) |
| Amazon S3 | AWS cloud storage |
| Microsoft Azure | Azure VMs, queues, storage |
| Google Drive / Google Storage / BigQuery | Google cloud services |
| Dropbox / OneDrive / Box | Cloud file storage |
| SharePoint | SharePoint lists and files |
| VMware | vSphere / vSphere7 / VIX |
| Dynamics CRM | Microsoft Dynamics |
| Slack / Telegram / Twitter / Facebook | Messaging and social |
| AMQP | RabbitMQ / Azure Service Bus |
| SAP / PeopleSoft / AS/400 | Enterprise systems |
| VisualCron | Remote VisualCron server |

## Creating a connection

1. Go to **Server > Global Objects > Connections**.
2. Click **Add**.
3. Select the connection type.
4. Fill in the required fields (server address, port, credentials).
5. Click **Test** to verify the connection.
6. Click **OK** to save.

## Using connections in tasks

When configuring a task that requires a connection (e.g., an FTP task), a **Connection** dropdown appears. Select the connection from the list, or click **Add** to create a new one inline.

## Explorer

Many connection types include an **Explorer** button that opens a file/database browser using the selected connection — useful for testing and navigating remote file systems or databases.

## Related

- [Connections reference](../connections/overview) — per-protocol setup guides
- [Credentials](credentials) — Windows user credentials for task execution
- [Global Objects > Connections](../global-objects/connections)
