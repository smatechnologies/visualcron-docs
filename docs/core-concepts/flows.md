---
sidebar_label: 'Flows'
sidebar_position: 8
description: Control job and task execution flow in VisualCron — retry, branch, skip, and notify on events.
---

# Flows

**Flows** control what happens when a job or task fires an event — success, failure, completion, or timeout. They replace simple on-error/on-success handling with a flexible, condition-aware routing system.

Flows are configured on the **Flow** tab of any Job or Task.

## Flow events

| Event | When it fires |
|-------|--------------|
| **On start** | Before the job/task runs |
| **On error** | When the job/task fails |
| **On success** | When the job/task completes successfully |
| **On complete** | When the job/task finishes (regardless of result) |
| **On running longer than** | If execution time exceeds a threshold |

## Flow actions

For each event, you choose an action:

| Action | What it does |
|--------|-------------|
| **Wait and retry** | Waits N seconds then retries (configurable max attempts) |
| **Run Job** | Fires another job |
| **Run Task** | Jumps to a specific task in the current job |
| **Stop Job** | Stops the job immediately |
| **Send Notification** | Runs a [Notification](notifications) |
| **Set Variable** | Sets a variable to a value |
| **Continue** | Proceeds normally (default) |

## Flow conditions

Each flow entry can have an optional **condition** that must be true before the action fires:

- **Always** — fire unconditionally
- **If other value/Variable** — compare two values or variables
- **If exit code** — match the exit code of the job/task

This lets you create conditional branching: *if exit code is 1, retry; if exit code is 2, run a cleanup job*.

## Example: Retry on failure

1. Open a job and go to the **Flow** tab.
2. Click **Add**.
3. Set **Event type** to *On error*.
4. Set **Action** to *Wait and retry*.
5. Configure: wait 30 seconds, retry up to 3 times.
6. Click **OK**.

Now if the job fails, VisualCron automatically waits 30 seconds and retries — up to 3 times.

## Default flows

Server-level default flows can be defined at **Server > Settings > Default Flows**. These apply to all new jobs automatically. To apply a default flow to an existing job, click **Get default flows** on the job's Flow tab.

## Task-level vs job-level flows

- **Job-level flows** control what happens to the entire job.
- **Task-level flows** control what happens after an individual task, including which task runs next.

Task flows are especially useful for branching: run Task B on success, run Task C on failure.

## Related

- [Notifications](notifications) — reusable tasks used as flow actions
- [Conditions](conditions) — condition sets used in flow entries
- [Jobs and Tasks](jobs-and-tasks)
