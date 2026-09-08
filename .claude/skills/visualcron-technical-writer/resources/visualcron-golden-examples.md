# Golden Examples

Complete, fully-compliant reference examples for each documentation type.
Use these to calibrate output quality. Every element in these examples —
front matter, structure, tone, formatting, and cross-references — follows
the standards in visualcron-documentation-standards.md and is appropriate
for the target audience per visualcron-learner-roles.md.

> **How to use this file:** When writing or reviewing a page, find the
> golden example that matches the documentation type and audience
> complexity. Use it as a quality benchmark — the finished page should be
> structurally and stylistically comparable.

---

## Conceptual Example

Target audience: Automation Engineer (moderate-to-high technical background)

```markdown
---
sidebar_label: 'How Conditions Work'
hide_title: 'true'
---

## How Conditions work

A Condition is a check that VisualCron evaluates before a Job or a Task
runs. Conditions let you gate automation on the real state of the system —
a file exists, a service is running, a variable has a certain value — so a
Job only proceeds when it makes sense to.

## Why Conditions matter

Time alone is not always enough to decide whether work should run. If a
nightly export depends on an input file that sometimes arrives late, a
Condition can hold the Task until the file is present instead of failing
on a fixed schedule. This makes automation resilient to real-world timing.

## Condition types

VisualCron supports several Condition types, each checking a different part
of the system:

| Type | Checks |
|---|---|
| File | Whether a file exists, or its size, date, or content |
| Folder | Whether a folder exists or contains items |
| Process | Whether a process is running |
| Service | Whether a Windows service is in a given state |
| Variable | Whether a VisualCron variable matches a value |
| .NET | A custom check written in .NET code |

## How a Condition set is evaluated

A Condition set resolves to a match outcome — **On Match All**,
**On Match Any**, **On Match None**, or **On Match Error** — and the Flow
action attached to that outcome decides what happens next: **Continue**,
**Next**, **Retry**, **Exit**, **Run Job**, or **Run Task**.

## How Conditions relate to Triggers and Flow

A Trigger decides when a Job starts. A Condition decides whether it should
proceed once started. Flow decides what to do based on the result. Together
they let you separate scheduling from decision-making.

:::note
Job Conditions are not checked when a Job is started manually.
:::

**Related topics:**

- [Add a Condition to a Job](../server/job-conditions.md)
- [How Triggers work](how-triggers-work.md)
- [How Flow works](../server/job-flow.md)
```

---

## Procedural Example

Target audience: Automation Engineer (technical, task-focused)

```markdown
---
sidebar_label: 'Add a Time Trigger to a Job'
hide_title: 'true'
---

## Add a Time Trigger to a Job

Add a Time Trigger to run a Job on a schedule — on a fixed interval or at
specific dates and times. A Job needs at least one Trigger to run
automatically.

:::note
The Job must exist before you can add a Trigger. See
[Add a Job](../server/jobs-jobs.md).
:::

To add a Time Trigger, complete the following steps:

1. In the Grid, right-click the Job and select _Edit_. The _Edit Job_ dialog is displayed.
2. Select the **_Triggers_** tab.
3. Select the _Add_ button. The _Add Trigger_ dialog is displayed.
4. Select the _Time_ option.
5. Select the Trigger type you need:

    | Option | Use when |
    |---|---|
    | **Interval time trigger** | You want the Job to run every N seconds, minutes, or hours |
    | **Custom time trigger** | You want the Job to run on specific days and times |

6. Configure the schedule settings for the type you selected.
7. Select the _Save_ button. The Trigger is added to the Job.

:::tip
A Job can have more than one Trigger. By default, multiple Triggers combine
as an OR relationship, so any one of them can start the Job.
:::

**Related topics:**

- [How Triggers work](../using-visualcron/how-triggers-work.md)
- [Add an Event Trigger to a Job](event-triggers.md)
- [Add a Time exception](global-time-exceptions.md)
```

---

## Procedural Pattern: Inline Note with Table

When a step requires the user to choose between options and there is relevant context to share before they choose, place the note inside the step before the table. Indent both the note and the table at 4 spaces to keep them attached to the step in Docusaurus.

```markdown
4. Select how the Tasks should run:

    :::note
    Running Tasks in order stops the Job at the first failed Task unless
    Flow is configured to continue. Running in parallel starts all Tasks
    at once.
    :::

    | Option | Use when |
    |---|---|
    | **Run Tasks in order** | Later Tasks depend on earlier ones |
    | (cleared) | Tasks are independent and can run at the same time |

5. Select the _Save_ button. The Job settings are saved.
```

---

## Reference Example

Target audience: Operations Staff and Automation Engineer (scanning for specific information)

```markdown
---
sidebar_label: 'Job and Task States'
hide_title: 'true'
---

## Job and Task states

This page lists the states a Job or Task can be in and what each state
means, so you can respond correctly during monitoring.

## Job states

| State | Meaning |
|---|---|
| Active | The Job's Triggers are enabled and it will run when a Trigger fires. |
| Inactive | The Job is deactivated; its Triggers will not fire. |
| Running | The Job is currently running one or more Tasks. |
| Queued | The Job is waiting because a run is already in progress or a queue limit applies. |

## Task states

| State | Meaning |
|---|---|
| Active | The Task will run as part of the Job. |
| Inactive | The Task is skipped when the Job runs. |
| Running | The Task process is currently executing. |
| Completed | The Task finished; check the exit code and output for the result. |

**Related topics:**

- [Monitor Jobs in the Grid](../server-group-job-task-area/overview.md)
- [Read Task output](../server/task-output-and-result.md)
```

---

## Why These Examples Matter for AI Workflows

Golden examples serve as implicit calibration for AI output. When the AI
has seen a complete, compliant example of each documentation type, it can
pattern-match against the example rather than assembling output purely from
rules. This produces higher-quality first drafts because:

- Structure is internalized, not just described
- Tone is demonstrated, not just specified
- Cross-reference patterns are shown in context
- Front matter is modeled with the correct `sidebar_label` / `hide_title` shape
- VisualCron's italics-for-UI and `->` menu conventions are shown in use
- The contrast between conceptual brevity and procedural precision is visible
