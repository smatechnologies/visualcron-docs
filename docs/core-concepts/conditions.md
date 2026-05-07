---
sidebar_label: 'Conditions'
sidebar_position: 3
description: Use conditions in VisualCron to control whether a job or task runs based on evaluated criteria.
---

# Conditions

A **condition** is a logical check that VisualCron evaluates before running a job or task. If the condition is not met, the job or task is skipped (or an alternative action is taken).

Conditions are managed at **Server > Global Objects > Conditions**.

## How conditions work

A **condition set** groups one or more individual conditions. Each condition set evaluates to true or false. You apply a condition set to:

- A **Job** — evaluated before the job starts
- A **Task** — evaluated before that specific task runs
- A **Flow event** — evaluated when a flow event fires (on-error, on-success, etc.)

## Condition types

| Type | What it checks |
|------|---------------|
| **File** | File exists, file size, age, content match |
| **Folder** | Folder exists, item count |
| **Process** | Process is running or not |
| **Variable** | A variable equals / contains / matches a value |
| **VisualCron** | Job/task status, last run result, running state |
| **.NET** | Custom logic written in C# / VB.NET |

## Creating a condition set

1. Go to **Server > Global Objects > Conditions**.
2. Click **Add**.
3. On the **Conditions** tab, click **Add** to add one or more conditions.
4. For each condition, choose the **type** and configure the parameters.
5. On the **Actions** tab, define what happens when the condition set matches (or does not match).

## Using conditions in jobs and tasks

- **Job level**: In the **Add/Edit Job** window, go to the **Conditions** tab and select a condition set.
- **Task level**: In the **Add/Edit Task** window, go to the **Conditions** tab.
- **Flow level**: In the **Flow** tab, each flow event can have an associated condition that must be true before the flow action fires.

## Example

**Scenario**: Only run a backup task if the source folder contains at least one file.

1. Create a Folder condition: *Folder item count > 0* for `C:\Data\Export`
2. Apply this condition set to the backup task
3. If the folder is empty, the task is skipped

## Related

- [Flows](flows) — on-error/on-success routing that can use conditions
- [Variables](variables) — pass dynamic values into condition checks
- [Jobs and Tasks](jobs-and-tasks)
