---
sidebar_label: 'Triggers'
sidebar_position: 2
description: Overview of time-based and event-based triggers in VisualCron.
---

# Triggers

A **trigger** determines when a job fires. VisualCron supports two fundamental types of triggers: **time-based** and **event-based**.

## Trigger types

### Time triggers

Fire at a specific time or on a recurring schedule.

| Type | Description |
|------|-------------|
| **Schedule** | Cron-style scheduling — specific days, times, weekdays, months |
| **Interval** | Runs every N seconds/minutes/hours |

### File triggers

Fire when a file system event occurs.

| Type | Description |
|------|-------------|
| **Local file** | Monitors a local folder for create, modify, delete, rename |
| **Remote file** | Monitors FTP/SFTP for file changes |
| **Cloud file** | Monitors cloud storage (S3, Dropbox, etc.) |
| **WebDAV file** | Monitors a WebDAV source |
| **SharePoint file** | Monitors a SharePoint document library |

### Email trigger

Fires when an email matching a filter arrives (POP3, IMAP, Exchange EWS, Microsoft Graph).

### Database trigger

Fires when a SQL query returns a result or a row changes.

### System triggers

| Type | Description |
|------|-------------|
| **Event Log** | Windows Event Log entry matches a filter |
| **Process** | A process starts or stops |
| **Service** | A Windows service changes state |
| **Registry** | A registry key changes |
| **WMI** | A WMI event fires |
| **Session Change** | User logon/logoff/lock events |
| **System Start/Shutdown** | Machine startup or shutdown |
| **Printer** | A print job event |

### Network triggers

| Type | Description |
|------|-------------|
| **HTTP** | Listens for an incoming HTTP request |
| **HTTP REST** | REST endpoint trigger (JSON payload) |
| **TCP** | Listens on a TCP port |
| **Ping** | Fires when a host becomes reachable or unreachable |
| **Network** | Network interface change |

### Messaging triggers

| Type | Description |
|------|-------------|
| **AMQP** | RabbitMQ / Azure Service Bus message |
| **MSMQ** | Microsoft Message Queue message |
| **Amazon SQS** | AWS Simple Queue Service message |
| **Azure Queue** | Azure Storage Queue message |
| **Slack** | Incoming Slack message |
| **Teams** | Incoming Teams message |

### Custom triggers

| Type | Description |
|------|-------------|
| **PowerShell** | Runs a PowerShell script; fires when it returns a specific value |
| **.NET** | Runs .NET code as a trigger condition |
| **Web Macro** | Fires based on web page content |

### Other triggers

RSS, Variable change, MFT (Managed File Transfer), PeopleSoft, Desktop, VisualCron server events.

## Multiple triggers per job

A job can have **multiple triggers**. Any trigger firing will start the job (OR logic). If you need AND logic (all conditions must be met), use [Conditions](conditions) alongside triggers.

## Trigger variables

When a trigger fires, it exposes variables you can use in tasks. For example, a file trigger exposes `{TRIGGER(FileFullPath)}`, `{TRIGGER(FileName)}`, etc.

## Related

- [Time Triggers](../triggers/time-triggers/schedule)
- [File Triggers](../triggers/file-triggers/local-file)
- [Conditions](conditions)
- [Variables](variables)
