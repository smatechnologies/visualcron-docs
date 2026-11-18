---
sidebar_label: 'Job - Flow'
hide_title: 'true'
---

## Job - Flow

The Flow can be set both at Job and Task level. Job flows react to the Job as a whole; to react to one Task's result, use [Task - Flow](task-flow).
 
### History

Flow was introduced in version 7.0.1. It combines the earlier **On error** handling, basic **Condition** handling and Notifications, to control what happens at each stage of a Job or Task.
 
### Job Flow

Job Flow has its own tab in the Job window. Job Flow adds controls what happens at different events:
* *On start*
* *On error*
* *On success*
* *On complete*
* *On running longer than*
 
For example, upon failure you can choose to wait a couple of seconds and then retry the Job. Another thing you can do is to send you a Notification when the Job has failed. Besides the event you can add a condition that needs to be matched before continuing with the action in the flow.
 
**Add/Edit Job > Flow** tab

![Job Flow window opened with Add on the Job's Flow tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Task%20Main%20Settings/Job%20Flow.png)

The list of flows is shown on the **_Flow_** tab, with each flow's event, condition and action. Use *Add*, *Edit*, *Clone* and *Delete* to manage the flows.
 
New Jobs created in the *Add Job* window get the [default flows](settings-default-flows) automatically. For other Jobs, click *Get default flows* to add all default Job flows; a default flow the Job already has is replaced by the current default, so changes you made to it are lost.
 
**Add/Edit Job > Flow > Add/Edit** window

![Job Flow window with the Job Condition and Job flow control groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Task%20Main%20Settings/Edit%20Job%20Flow.png)

The Job Flow window is divided in two parts:
* Job Condition
* Job flow control
 
### Job Condition

The Job Condition controls when and with what conditions the flow should be started.
 
**Event type**

* On start - performs the action after the Job's Conditions are met, before the first Task runs
* On error - performs the action when the Job has failed
* On success - performs the action when the Job returns success result
* On complete - performs the action when the Job completes - regardless of result
* On running longer than - performs the action if the Job runs longer than specified time
 
**On running longer than**

This option lets you control what happens if the Job runs longer than a specified time. Click *Edit timeout* to open the *Timeout* window and enter *Hours*, *Minutes* and *Seconds*; each can be a Variable. *Validate Variables when saving* checks that each value is a whole number. A time entered as numbers cannot be 0.
 
**Event condition**

Event conditions contain some basic conditions that are optionally evaluated when the event type is matched. If you do not want to use any conditions you set it to the "Always" which means that the flow will continue whenever the event has been raised.
* Always - will continue without evaluating any condition
* If other value - matches any two values, which can be Variables or a mix; click the Variables icon to open the Variables list
* If exit code - matches a value with the exit code of the last Task that finished in the Job (for *Run Notification* on *On running longer than*, the Task that is running)

:::warning

This is a Task's exit code, not the Job's result. To act on one Task's exit code, add the flow to that Task ([Task - Flow](task-flow)).

:::

The *If exit code* condition is not available for the *On start* event, since no exit code exists yet at that point.
 
**Type/Condition**

When you have selected an event condition you decide how to match this condition - with what value and data type. The data type can be *Boolean*, *Decimal*, *Double*, *Int32*, *Int64* or *String*.

The available match operators depend on the selected data type:

* *String* - Equal, Not equal, Contains, Not contains
* *Boolean* - Equal, Not equal
* *Decimal*, *Double*, *Int32*, *Int64* - Equal, Not equal, Smaller than, Larger than, Smaller than or equal, Larger than or equal
 
**Value/Variable**

Enter a value or click the Variables icon to open the Variables list.

### Job flow control

The flow control group controls what happens when the Job Condition has been matched with event and condition.

**Stop Job**

Available only with *On running longer than*. Stops the running Tasks and the Job. The Job ends as failed, with the exit code of a failed Task (which can be the Task that was stopped) or 77777, and its *On error* and *On complete* flows then run. The Job stays active, so its Triggers start it again as usual.
 
**Wait ... and retry Job**

Waits the time you set and then runs the Job again, up to the number of times you set. Each retry is a new run, with its own result. Used with *On success* or *On complete*, it runs a Job that succeeded again.
 
**Run Job**

Runs another Job. Check *Run asynchronous* to start the other Job without waiting for it to complete, or leave it unchecked to run it synchronously.
 
**Run Notification**

Runs the specified Notification. Select it in the list; the *Settings* icon opens the *Manage Notifications* window.
 
**Deactivate Job**

Select to also deactivate the Job after the selected action. With *Wait* ... *and retry Job*, the Job is deactivated only when the retries are used up. It is not available for the *On start* event. See [Activate/Deactivate Job](../server-group-job-task-area/job-list/activate-deactivate-job).

:::warning

*Deactivate Job* has no effect with *Stop Job*, although it can be selected. The Job stays active and runs again on its next Trigger.

:::
