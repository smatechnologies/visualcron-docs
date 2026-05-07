---
sidebar_label: 'Introduction'
sidebar_position: 0
slug: '/'
description: VisualCron is an advanced automation and job scheduling tool for Windows.
---

# VisualCron Documentation

VisualCron is an advanced job and task scheduler for Windows. It runs commands, programs, scripts, and integrations on a schedule or in response to events — with no coding required.

## What can VisualCron do?

- **Schedule jobs** to run at precise times, intervals, or in response to system events
- **Automate file operations** — copy, move, sync, upload/download via FTP, SFTP, cloud storage
- **Integrate with enterprise systems** — Active Directory, Exchange, SharePoint, SAP, Dynamics CRM
- **Send notifications** via email, Slack, Teams, SMS, and more
- **Manage infrastructure** — control Windows services, processes, VMs (VMware, Hyper-V, Azure, AWS)
- **Process data** — SQL queries, XML/JSON transforms, PDF manipulation, Excel automation

## How it works

The core execution model is: **Trigger → Condition → Task → Notification**

| Object | Purpose |
|--------|---------|
| **Job** | Container that holds one or more Tasks and its Triggers |
| **Trigger** | Fires the Job (time-based or event-based) |
| **Condition** | Optional guard — evaluated before the Job or Task runs |
| **Task** | The actual unit of work (416+ task types) |
| **Notification** | Action taken on success, failure, or completion |

## Getting started

- [Installation](getting-started/installation) — download, install, and configure the server
- [First Connection](getting-started/first-connection) — connect the client to the server
- [Your First Job](getting-started/your-first-job) — create and run a basic job

## Browse by area

| Section | What's inside |
|---------|--------------|
| [Tasks](tasks/process/execute) | 416+ task types grouped by category |
| [Triggers](triggers/time-triggers/schedule) | Time, file, system, network, and messaging triggers |
| [Connections](connections/overview) | Shared connection objects (FTP, SQL, OAuth, etc.) |
| [Global Objects](global-objects/variables) | Variables, credentials, notifications, conditions |
| [API](api/overview) | REST API reference and authentication |
