---
sidebar_label: 'Job - Conditions'
hide_title: 'true'
---

## Job - Conditions

The **_Conditions_** tab of the Job window chooses the Condition Set that the Server checks at the start of each Job run, before any of its Tasks. Use it when the whole Job should run only if something is true at that moment. To check something before one Task instead, use the **_Conditions_** tab of the Task window, see [Task - Conditions](task-conditions).

A Job uses one Condition Set or none. Check _Use_ for the set you want, or clear it to use none. The choice is saved when you save the Job. Changes to sets made on this tab are saved at once and apply to every Job and Task that uses the set. For the rest of the tab, see [Choose the Condition Set for a Job or Task](global-conditions#choose-the-condition-set-for-a-job-or-task).

### When the Job's Condition Set is checked

The Server checks the Job's Condition Set at the start of each Job run, before any Task starts and before the Job's _On start_ Flow entries. Whether it applies the action depends on how the run was started:

- Started by a Trigger: applied
- Started by the "Run Job" action of a Condition Set: applied
- Started by a Task Flow entry with _Stop Job and run specified Job_: applied
- Started by a _Run Job_ Flow entry of another Job, or by a Flow entry of this Job that waits and retries it (_Wait_ … _and retry Job_): applied only if it was applied to the run that contains that Flow entry. For example, Job A has a _Run Job_ Flow entry that starts Job B. If a Trigger starts Job A, Job B's set is applied. If you start Job A with _Run Job_, Job B's set is not applied either
- Started by a Job/Task Control Task with the action "Job - Run Job": checked, but the action is not applied, as on a manual run
- Started by a Job/Task Control Task with the action "Task - Run Task": applied, and the Task's own Condition Set is applied too
- A run that waited in the Job queue, for example because the Job has _Put Job in queue_ checked: applied when the run starts from the queue, even if the command that queued it did not apply conditions
- A missed run that the Server starts when it starts up, for a Job with _Run missed Job once at start_ checked: applied
- Run manually: see [Manual runs](#manual-runs)

The result selects an action on the **_Actions_** tab of the set. In a Job's Condition Set, "Continue" runs the Job and "Retry" checks again. "Next", "Exit", "Run Job" and "Run Task" end the Job before any Task runs, and "Run Job" and "Run Task" then start the chosen Job or Task. See [Conditions - Actions](conditions-actions) for the details and warnings. If the set no longer exists, see [Errors and missing Condition Sets](conditions-actions#errors-and-missing-condition-sets).

### When a Condition Set ends the Job

When a Job's Condition Set ends the Job before any Task runs:

- The Server still records a run of the Job, with a successful result
- The Job's _On start_ Flow entries do not run
- The Job's _Run Notification_ Flow entries do not run
- The Job's other Flow entries for _On success_ and _On complete_ run if their _Event condition_ is "Always" or "If other value". An entry with "If exit code" does not run, because no Task has an exit code yet
- VisualCron Event Triggers that watch this Job for _Job completed_ or _Job completed - successfully_ fire
- VisualCron Event Triggers that watch this Job for _Job started_ fire when the run starts, before the set is checked

When a Task's Condition Set ends the Job ("Exit", "Run Job", or "Run Task" with a Task of another Job), the Job's result comes from the Tasks that already ran. If no Task ran, the run is recorded as successful. The Job's Flow entries, including _Run Notification_, and its completion events then run as for any other run with that result.

:::warning

A Job that a Condition Set ends before any Task has run is recorded as successful. Its _On success_ and _On complete_ Flow entries that run another Job or retry this Job, unless their _Event condition_ is "If exit code", and the [Event Trigger - VisualCron](event-trigger-visualcron) Triggers on its completion, still start Jobs. If another Job must run only after this Job has done its work, start it from a Flow entry of this Job's last Task, with the _On success_ event and _Stop Job and run specified Job_ (see [Task - Flow](task-flow)), instead of from the Job's Flow or a completion Trigger.

:::

### Manual runs

How a manual run treats the Job's Condition Set depends on the command you use. On the shortcut menu, each command includes the name of the Job or Task, for example _Run Job 'Backup settings' with options_. The table leaves the name out.

| Command | Job's Condition Set | Task Condition Sets |
|---|---|---|
| _Run Job_ | Checked, action not applied | Applied |
| _Run Job_ button on the ribbon | Checked, action not applied | Applied |
| _Run Job_ -> _Without Conditions_ -> _From first Task_ or _From this Task_ | Checked, action not applied | Applied |
| _Run Job_ -> _Without raising Trigger events_ | Checked, action not applied | Applied |
| _Run Job_ -> _With Conditions_ -> _From first Task_ or _From this Task_ | Applied | Applied |
| _Run selected Jobs_ -> _Without Conditions_ | Checked, action not applied | Applied |
| _Run selected Jobs_ -> _With Conditions_ | Applied | Applied |
| _Run Job with options_ (see [Run Job With Options](../server-group-job-task-area/job-list/run-job-with-options)) | Applied only when _With Conditions_ is checked, which it is not by default | Applied |
| _Run Task_ on a single Task | Applied. If it ends the Job, the Task does not run | Not applied |
| _Run Task_ -> _Without raising Trigger Events_ | Applied. If it ends the Job, the Task does not run | Not applied |

When the Job's action is not applied, the log shows the message "Skipping Condition check because the Job was run manually."

:::note

When its action is not applied, the Job's Condition Set is still checked, so its conditions run, including the code of a .NET condition. With _Extended debug logging_ checked on the set, the check is written to the log.

:::
