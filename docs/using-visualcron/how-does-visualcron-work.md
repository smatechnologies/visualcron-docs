---
sidebar_label: 'How Does VisualCron Work?'
hide_title: 'true'
---

## How Does VisualCron Work?

This page explains how the VisualCron objects work together when a Job runs. Read it before you build your first Job.

VisualCron works much like the Unix/Linux cron utility, but it can also react to events. It can run a program, or any of its built-in Tasks, at set times, at intervals down to the second, once, or when something happens on the system.

### The objects in a Job

**Triggers** start the Job. A Job can have several Triggers. [Time Triggers](../client-user-interface/server/time-triggers), [Interval Time Triggers](../client-user-interface/server/interval-time-trigger) and [Custom Time Triggers](../client-user-interface/server/custom-time-trigger) start a Job at a time or interval. [Event Triggers](../client-user-interface/server/event-triggers) start it when something happens, for example when a file is created.

**Condition Sets** are checks. A Job can have a Condition Set that is evaluated when the Job starts, and each Task can have one that is evaluated just before the Task runs. The result decides whether the Job or Task continues. See [Job - Conditions](../client-user-interface/server/job-conditions) and [Task - Conditions](../client-user-interface/server/task-conditions).

**Tasks** do the work. A Job holds one or more Tasks of different types. By default, they run one after another, in the order of the Job's Task list. If _Run Tasks in order_ is unchecked in the Job's settings, VisualCron starts the Tasks without waiting for each one to finish. The Tasks' _On success_, _On error_ and _On complete_ Flow then runs only Notifications. Other Flow actions, such as a retry, are not carried out. Flow can also change the order. See [Job - Tasks](../client-user-interface/server/job-tasks) and [Job - Main Settings](../client-user-interface/server/job-main-settings).

**Flow** decides what happens next when a Job or Task starts, succeeds, fails or completes, or runs longer than a set time. A Flow action can continue to the next Task, stop the Job, retry, go to another Task, run another Job, or run a Notification such as an email. See [Task - Flow](../client-user-interface/server/task-flow), [Job - Flow](../client-user-interface/server/job-flow) and [Global - Notifications](../client-user-interface/server/global-notifications).

### What happens when a Job runs

When a Job runs, VisualCron completes these steps:

1. A Trigger fires, or you run the Job manually.
2. The Job's Condition Set, if any, is evaluated.
3. The Job's _On start_ Flow runs.
4. Each Task runs. Before it starts, its Condition Set, if any, is evaluated, and then its _On start_ Flow runs.
5. When a Task ends, its _On success_, _On error_ or _On complete_ Flow decides what happens next.
6. When the Job ends, its _On success_, _On error_ or _On complete_ Flow runs.

A Job or Task Flow can also act while the Job or Task is still running, with _On running longer than_.

When you run a Job manually, the Job's own Condition Set is checked, but its action is applied only if you right-click the Job and select _Run Job_ -> _With Conditions_, or one of its items _From first Task_ and _From this Task_. The same applies to _Run selected Jobs_ -> _With Conditions_. The Condition Sets of its Tasks are always applied. When you run a single Task manually, the Task's own Condition Set is not checked, but the Job's Condition Set is. See [Job - Conditions](../client-user-interface/server/job-conditions).

### Where Tasks run

Each Task run has its own status and output, which you can see in the Client. Most Tasks run inside the VisualCron service. Some Task types start a separate Windows process. Tasks set to run in the foreground run through the [Tray Client](visualcron-tray-client) in a logged-on user's session. For each Task run, VisualCron saves statistics such as how long the Task took.

### Running a Job once

If _Run once (can be reactivated later)_ is checked in the Job's settings, the Job is deactivated as soon as it starts. It stays in the Job list, and you can activate it again later. See [Job - Main Settings](../client-user-interface/server/job-main-settings).