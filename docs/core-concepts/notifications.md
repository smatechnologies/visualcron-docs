---
sidebar_label: 'Notifications'
sidebar_position: 7
description: Configure reusable notifications in VisualCron to alert on job and task events.
---

# Notifications

A **notification** is a reusable task that gets triggered by a job or task event — such as a failure, success, or completion. Any VisualCron task type can be used as a notification (email, Slack, Teams, etc.).

Notifications are managed at **Server > Global Objects > Notifications**.

## How notifications work

1. Create a notification (e.g., an Email Send task configured with your failure message).
2. In a Job or Task's **Flow** tab, add a flow event (e.g., *On error*) and select the notification to run.
3. When the event fires, VisualCron executes the notification task.

Notifications are **global** — defined once, reused across any number of jobs and tasks.

## Creating a notification

1. Go to **Server > Global Objects > Notifications**.
2. Click **Add**.
3. Select a task type (e.g., **Email Send**).
4. Configure the task as you would any normal task.
5. Click **OK** to save.

## Attaching notifications to jobs and tasks

**Job level**: In **Add/Edit Job > Flow**, add a flow entry with the desired event type and select a notification.

**Task level**: In **Add/Edit Task > Flow**, add a flow entry referencing the notification.

## Flow events for notifications

| Event | When it fires |
|-------|--------------|
| On start | Before the job/task begins |
| On complete | When the job/task finishes, regardless of result |
| On success | When the job/task completes successfully |
| On error | When the job/task fails |
| On running longer than | If execution exceeds a time threshold |

## Using variables in notifications

Variables are available inside notification tasks. For example, in an email notification body:

```
Job {JOB(id,Name)} failed at {DATETIME(HH:mm:ss)}.
Output: {TASK(id,OutputError)}
```

:::note Variable availability

Not all variables are available at all events. Task output variables (e.g., `{TASK(id,Output)}`) are only available in *On complete* / *On success* / *On error* events — not *On start*.

:::

## Related

- [Flows](flows) — how notifications plug into flow routing
- [Variables](variables) — dynamic content in notification messages
- [Email Send task](../tasks/messaging/email-send)
