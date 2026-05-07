---
sidebar_label: 'Jobs and Tasks'
sidebar_position: 1
description: Understand the Job and Task hierarchy — the core execution model in VisualCron.
---

# Jobs and Tasks

In VisualCron, a **Job** is the container for automation. A **Task** is the unit of work inside that container. Every piece of automation starts with a Job.

## The execution model

```
Trigger → (Condition) → Task(s) → (Notification)
```

| Object | Role |
|--------|------|
| **Job** | Container. Holds triggers, tasks, conditions, and notifications. |
| **Trigger** | What fires the job — a schedule, a file event, an email, etc. |
| **Condition** | Optional guard evaluated before the job or a task runs. |
| **Task** | The actual work. There are 416+ task types. |
| **Notification** | An action (e.g., send an email) taken on success, failure, or completion. |

## Jobs

A Job defines:
- **One or more triggers** — when it runs
- **One or more tasks** — what it does
- **Flow rules** — what happens on success/failure (retry, run another job, send notification)
- **Conditions** — whether to run at all

Jobs appear in the **Server/Job/Task grid** in the main window. They can be enabled/disabled, run manually, cloned, and grouped.

### Job execution order

Tasks within a job run **sequentially by default**, in the order they appear in the task list. You can change this using the **Flow** tab to branch, skip, or loop based on results.

## Tasks

A task is the atomic unit of work. VisualCron ships with 416+ task types organized into categories:

| Category | Examples |
|----------|---------|
| **Process** | Execute, PowerShell, .NET Execute, Robot |
| **File Operations** | Copy, Delete, Rename, Read, Write, Sync |
| **Network** | FTP, HTTP, SSH, Ping, Web Service |
| **Messaging** | Email Send, Slack, Teams, Telegram |
| **Database** | SQL, SSIS, SSRS, BigQuery |
| **Cloud** | AWS EC2/S3, Azure VMs, Google Drive |
| **System** | Services, Registry, Windows Update, Event Log |

Each task has:
- **Main settings** — the task-specific configuration
- **Credentials** — run as a specific Windows user (optional)
- **Flow** — on-success / on-error / on-complete actions
- **Notifications** — task-level alerts

## Task output

Every task produces output that can be:
- **Viewed** in the Output and Result window
- **Passed** to the next task via [Variables](variables)
- **Stored** in the log database

## Related

- [Triggers](triggers) — how jobs get fired
- [Conditions](conditions) — flow control guards
- [Variables](variables) — passing data between tasks
- [Flows](flows) — on-success / on-error routing
