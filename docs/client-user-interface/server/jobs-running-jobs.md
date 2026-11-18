---
sidebar_label: 'Jobs - Running Jobs'
hide_title: 'true'
---

## Jobs - Running Jobs

The _Running Jobs_ window shows the Jobs, Tasks and processes the Server is running now, and lets you stop them. It includes work that does not appear in Windows Task Manager, for example a web request.

To open it, click the main menu _Server_ -> _Jobs_ -> _Running Jobs_. You need the "Processes" permission with "Read" to open the window, and with "Delete" to stop a process (see [Main - User Permissions](main-user-permissions)). The same list is on the **_VisualCron Jobs_** tab of [Task Manager](../tools/task-manager).

_Server_ -> _Jobs_ -> _Running Jobs_

![Running Jobs window opened from the Jobs group of the Server tab of the main menu, with Viewstyle set to Trigger > Job > Task > Task process, Update interval 3 and the Stop button, and an empty grid with the Name, Description, CPU time and CPU % columns](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Task%20Main%20Settings/Jobs%20-%20Running%20Jobs.png)

### Job processes and Task processes

When VisualCron runs a Job, it starts a Job process: a temporary working copy of the Job. A Job exists once, but several Job processes can come from it, for example when the same Job runs several times at once. The Job process:

- Keeps track of the Tasks to run
- Checks Conditions
- Sends Notifications
- Updates the Client with the status of each Task

When a Task runs, a Task process is created: a temporary copy of the Task. The Task process:

- Tells the Client when the Task starts and ends
- Performs the action, for example runs a command or sends a POST request to a website

Each Task process has an ID, which is used to control it. A Task exists once, but several Task processes can come from it when several Job processes run at the same time.
 
### Toolbar

- _Viewstyle_: how the list is arranged; the options are "Trigger > Job > Task > Task process", "Job > Task > Task process", "Job > Triggers", "Task process" and "Job process > Task process" (the default)
- _Update interval_: how often, in seconds, the _Runtime_, _CPU time_ and _CPU %_ columns are updated; default "3"
- _Stop_: stops the selected row (see [Stopping processes](#stopping-processes))

Your _Viewstyle_ and _Update interval_ choices are saved with your Client settings.

### Columns

Depending on the row and the view, the list shows:

- _Name_ and _Description_
- _Started_ and _Runtime_ for Job processes and Task processes
- _Windows PID_ for Task processes, and _Job process id_ in the views that list Task processes under Tasks
- _CPU time_: the processor time used since the previous update
- _CPU %_: the share of the whole computer's processor capacity used since the previous update, divided over all logical processors

Right-click a row for _Stop_ and _Go to process_. _Go to process_ works only when the list is shown in Task Manager; in the _Running Jobs_ window it does nothing. In Task Manager it switches to the **_System processes_** tab and selects the Windows process of the selected Task process.
 
### Stopping processes

Select a row and click _Stop_, or right-click the row and click _Stop_. The result depends on the row:

- Job: stops all running Job processes of the Job and their Task processes, and removes the Job's queued runs
- Job process: stops that Job process and its Task processes
- Task: stops all Task processes started from that Task
- Task process: stops that single Task process

Stopping a Job, Job process or Task row is recorded in the [Objects - Audit Log](../tools/objects-audit-log). Stopping a single Task process is not recorded there.

:::warning

_Stop_ acts immediately and does not ask for confirmation. Stopping a Job row also removes that Job's queued runs, so they do not run. To stop only the current run and keep the queued runs, stop the Job process row instead.

:::

:::warning

In the "Trigger > Job > Task > Task process" view, _Stop_ on a Job row does not stop the Job. To stop all runs of a Job, select the Job row in the "Job > Task > Task process" view.

:::