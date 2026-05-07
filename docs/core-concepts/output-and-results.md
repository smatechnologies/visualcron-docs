---
sidebar_label: 'Output and Results'
sidebar_position: 9
description: Understand how VisualCron captures, displays, and passes task output and execution results.
---

# Output and Results

Every task execution in VisualCron produces **output** and a **result**. Understanding these is essential for debugging, chaining tasks, and using variables.

## Output types

| Output | Description |
|--------|-------------|
| **Standard output** | Text written to stdout by the task |
| **Error output** | Text written to stderr |
| **Task result** | Task-specific structured data (command line used, SQL query, row count, etc.) |
| **CPU usage** | CPU consumption during execution |
| **Execution time** | How long the task ran |
| **Execution result** | Success or Failure |

## Viewing output

Double-click a task row in the grid to open the Output and Result window:

- Click the **Output** column → shows standard output
- Click the **Output (error)** column → shows error output
- Click the **Result** column (success/failure icon) → shows task result details

You can also right-click a task and choose **Result > Task result**.

## Output window features

| Feature | Description |
|---------|-------------|
| **Find** | Search within the output text |
| **Go to line** | Jump to a specific line |
| **Get full output** | Fetches the complete output from the server (default: 2000 chars loaded) |
| **Date picker** | Browse output from previous executions by date |
| **Time selector** | Choose a specific execution time for that date |

## Task result detail

Each task type provides its own result data. Examples:

- **Execute task** — command line, arguments, process ID
- **SQL task** — connection string, query, row count
- **Web Macro task** — video or screenshots of playback
- **Robot task** — video of the playback

Enable **Extra Task debugging** in a task's Main Settings to increase result detail.

## Execution history

The **Date picker** in the output window shows all dates where at least one execution occurred. Selecting a date populates the **Time** list with each execution time. A color-coded icon shows success (green) or failure (red).

Click the **Success/Failure button** to view a chart of execution results over a selected range. Use **Ctrl+Scroll** to zoom in/out.

## Passing output to other tasks

Task output is accessible as a [Variable](variables):

```
{TASK(taskId, Output)}         — standard output
{TASK(taskId, OutputError)}    — error output
{TASK(taskId, ExitCode)}       — exit code
```

Drag and drop these variables into any field of a downstream task to chain output between steps.

## Storage

How much output history is retained is controlled by **Server > Settings > Log Settings** — the database log settings determine retention days and size limits.

## Related

- [Variables](variables) — reference task output in downstream tasks
- [Flows](flows) — act on success/failure/output
- [Conditions](conditions) — condition based on output or exit code
