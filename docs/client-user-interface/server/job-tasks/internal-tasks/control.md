---
sidebar_label: 'Task Internal - Job/Task Control'
hide_title: 'true'
---

## Task Internal - Job/Task Control

The Job/Task Control Task runs, stops, activates or inactivates a Job or Task, or activates or inactivates a Trigger, on this VisualCron Server or on another one. For another Server, it uses a [VisualCron Connection](../../../server/connection-visualcron). All settings are in the *Control Job or Task* group.

![Job/Task Control Task settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Internal%20Tasks/Job%20Task%20Control.png)

**Action**

Select what to do. Defaults to *Task - Run Task*. The actions are:

* *Job - Run Job*, *Job - Stop Job*, *Job - Activate Job*, *Job - Inactivate Job*
* *Task - Run Task*, *Task - Stop Task*, *Task - Activate Task*, *Task - Inactivate Task*
* *Trigger - Activate Trigger*, *Trigger - Inactivate Trigger*

Every action needs a Job. Task actions also need a Task under *Tasks*, and Trigger actions apply to the Triggers selected under *Trigger*. Job Variables can be passed only with *Job - Run Job* and *Task - Run Task*.

**Run synchronous (wait for completion)**

Selected by default; available for *Job - Run Job*, *Task - Run Task* and *Job - Stop Job*. This Task waits until the Job or Task has finished before the next Task runs. A Job that is queued is not waited for. With *Job - Stop Job*, it waits until the Job has stopped, only on this Server and only when the Job is not this Task's own Job.

When cleared, this Task succeeds once the Job or Task is started, without waiting for its result, and the *Inherit exit code from child Job/Task* and *Inherit output from child Task* options are cleared and unavailable.

**Inherit exit code from child Job/Task**

Selected by default; for *Job - Run Job* and *Task - Run Task* with *Run synchronous (wait for completion)*. The exit code of the Job or Task that runs becomes this Task's exit code, so this Task fails when that Job or Task fails. When cleared, this Task succeeds: with *Job - Run Job*, a failure is written to this Task's error output; with *Task - Run Task*, the result, for example "Failure", is written to its output.

**Inherit output from child Task**

Cleared by default; for *Task - Run Task* with *Run synchronous (wait for completion)*. When selected, the output and error output of the Task that runs are copied to this Task's output and error output.

**VisualCron Server location**

*Local VisualCron Server* / *Remote VisualCron Server*

Select whether to run the action on this Server or on a remote VisualCron Server. Defaults to *Local VisualCron Server*.

Every action can be used on a remote Server, through a VisualCron Connection. When you select *Job - Stop Job*, *Remote VisualCron Server* becomes unavailable for that Task, also when you open it again, but a remote selection made before is kept; to stop a Job on a remote Server, select *Remote VisualCron Server* and the Connection first, and then *Job - Stop Job*.

**VisualCron Connection**

Select the [VisualCron Connection](../../../server/connection-visualcron) to use for the remote Server. Only available when *Remote VisualCron Server* is selected.

**Job**

Select the Job to target from the list.

**Reload**

Click *Reload* to refresh the list; for a remote Server, this loads it from the Connection.

**Job Variables..**

Values to pass to the Job, for *Job - Run Job* and *Task - Run Task*. See [Job Variables](../../../server/job-variables). Each value replaces the Job Variable with the same key, or is added if the Job has no Variable with that key. In the *Job Variables* window, click *Get current Variables* to load the Job's current Variables; values you entered in this Task for the same keys are overwritten by the Job's current values.

**Translate Variables before sending**

Selected by default. Variables in the values are replaced by this Task before the values are passed. When cleared, the values are passed as written.

**Update Job Variables**

Selected by default, and selected again whenever you choose *Job - Run Job* or *Task - Run Task*, so clear it after you choose the action. When selected, the passed values are saved to the Job, and all changes the run makes to the Job's Variables are kept. When cleared, the Job's Variables are set back to their values from before the run when it ends: keys added during the run are removed, and changes made from other Jobs are undone, but a change that a Set Job Variable Task in that Job makes to an existing key is kept (see [Job Variables](../../../server/job-variables)).

With *Job - Run Job* on this Server and this option selected, the user who started this Task's Job needs the *Edit* permission for *Variables* (set for the user's group, not per Job), even if no values are passed; otherwise this Task fails (see [User permissions](../../../server/main-user-permissions)). Runs started by a Trigger are not checked. On a remote Server, *Job - Run Job* saves the passed values to the Job whether or not this option is selected.

**Trigger**

**All**

Selected by default: the action applies to all of the Job's Triggers. When cleared, select one or more Triggers in the list.

**Reload**

Click *Reload* to refresh the list; for a remote Server, this loads it from the Connection.

**Tasks**

Select the specific Task to target from the list.

**Reload**

Click *Reload* to refresh the list; for a remote Server, this loads it from the Connection.

**Result**

When the Job or Trigger is not found, this Task writes the reason to its error output and succeeds. With *Task - Run Task* on this Server, a missing Job or Task makes this Task fail. With *Job - Run Job*, a Job that is queued or not started is reported in the output, and one that is not started because it is already running, in the error output; this Task succeeds in each case.

With *Task - Run Task* on this Server, the Task is not run if the user who started this Task's Job does not have the *Execute* permission on that Task, or if that Task's Job is already running and *Do not start if job is already running* is selected for it. This Task then succeeds: with *Run synchronous (wait for completion)*, its output gives the result as "NotSet" (select *Inherit output from child Task* to see the reason); without it, the output says the Task was started. Check this Task's output and error output when you set it up, and after you change or delete the Jobs, Tasks or Triggers it targets.

:::warning

On this Server, the Task's [***Timeout***](../../../server/task-timeout) tab applies. For a remote Server, the ***Timeout*** tab is used, and if no timeout is set there, the timeout of the VisualCron Connection is used. The wait for the remote Server uses the hours value in place of the minutes, so minutes are ignored and 1 hour waits 1 hour and 1 minute; leave the minutes at 0 and set the hours and seconds. When the timeout on the ***Timeout*** tab is reached, a Job or Task started with *Job - Run Job* or *Task - Run Task* on the remote Server is stopped.

:::
