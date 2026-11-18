---
sidebar_label: 'Task - Flow'
hide_title: 'true'
---

## Task - Flow

The Task Flow controls what happens at start, complete, success and failure of a Task with additional conditions based on output, exit code etc. One or more Flows can be created depending on how you want to control the Flow in various situations.
 
This feature was introduced with version 7.0.1 and replaced existing Notifications tab.
 
**Add/Edit Task > Flow** tab

The screenshot shows the Job Flow window, which offers fewer actions than the Task's **_Flow_** tab.

![Job Flow window with the condition and flow control settings](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Edit%20Job%20Flow.png)

The main listing above contains a verbose description of when (On error/On success/On complete) and what happens - the flow action.
 
To add the default flows to a Task created before they were defined, select the *Get default flows* icon. It adds all default Task flows to the Task. For more information about Default flows, see [Server > Settings > Default flows](settings-default-flows).

The Task Flow window is divided into two parts:

* Task Condition
* Task flow control
 
**Task Condition**

The Task Condition controls when and with what conditions the flow should be started.
 
**Event type**

* *On start* - with *If other value*, the condition is checked before the Task runs and again after it
  has started, so a *Run Notification* action can run twice. With *Always*, the
  action runs after the Task has started; only *Stop Job*, *Stop Job and run specified Job* and
  *Run Notification* work, and *Stop Job* lets the started Task finish before the Job stops
* *On error* - performs the action when the Task has failed
* *On success* - performs the action when the Task returns success result
* *On complete* - a *Run Notification* action runs after every run, whatever the result. Any other action
  runs only when no *On success* or *On error* flow matched; a new Task gets an *On success* and an
  *On error* flow by default, so such an action usually does not run
* *On running longer than* - applies when the Task runs longer than the time set with *Edit timeout*. Use
  it with *Run Notification*. This is separate from the Task's **_Timeout_** tab

:::warning
With *On running longer than*, any action other than *Run Notification* stops the running Task, and the
selected action is not carried out.
:::

**Event condition**

Event conditions contains some basic conditions that are optionally evaluated when the event type is matched. If you do not want to use any conditions you set it to the "Always" which means that the flow will continue whenever the event has been raised.

* Always - will continue without evaluating any condition
* If output - matches a value you enter with output of the Task
* If error output - matches a value you enter with output (err) of the Task
* If other value - If other value/Variable - matches any two values - could be two Variables or a mix. Click the Variables icon to open the Variables list.
* If exit code - matches a value with the exit code of the Task
 
**Type/Condition**

When you have selected an event condition you decide how to match this condition - with what value and data type. The data type can be *Boolean*, *Decimal*, *Double*, *Int32*, *Int64* or *String*.

The available match operators depend on the selected data type:

* *String* - Equal, Not equal, Contains, Not contains
* *Boolean* - Equal, Not equal
* *Decimal*, *Double*, *Int32*, *Int64* - Equal, Not equal, Smaller than, Larger than, Smaller than or equal, Larger than or equal
 
**Value/Variable**

Enter a value or click the *Variables* icon to open the Variables list.
 
**Task Flow control**

:::warning
For the *On success*, *On error* and *On complete* events, *Stop Job*, *Continue to next Task in order*,
*Wait*, *Go to Task* and *Stop Job and run specified Job* take effect only when the Job has
*Run Tasks in order* selected (see [Job - Main Settings](job-main-settings)). Otherwise only
*Run Notification* actions run.
:::

The flow control group controls the action when the Task Condition has been matched with event and condition.
(Before version 7.0.1, these settings were on the **_On error_** tab.)
 
**Stop Job**

Stops the Job execution immediately. No further Tasks will be run.
 
**Continue to next Task in order**

Ignores the error and continue to the following Task.
 
**Wait and retry**

Waits a specified time and then try to run the Task again. You can choose how many times VisualCron will try to do this before stopping the Job completely. Optionally you can check *If finally failing, go to Task* to set it to continue with other Task if it has failed for all specified retry times.
 
**Go to Task**

Runs a specified Task in the same Job. You also have option to continue running the following Tasks in order - after that Task.
 
**Run following Tasks in order**

The default behavior which means that it will run all Tasks defined after this Task. If you only want it to run the specified Task then uncheck this option.
 
**Stop Job and run specified Job**

Stops the current Job and executes another Job.
 
**Run Notification**

Runs the specified Notification. Select it in the list; the *Settings* icon opens the *Manage Notifications* window.
 
The following options can be selected together with any action, except in an *On start* flow with
*Always*:

**Deactivate Task**

Deactivates the current Task after the action. In an *On start* flow with *If other value*, it currently
deactivates the previous Task instead, and with *Run Notification* it also deactivates the current Task.
On the first Task of a Job there is no previous Task, and the Job fails.

**Deactivate Job**

Deactivates the current Job after the action. With *Wait* ... *and retry Task*, it is ignored when the last
retry fails and the Job stops. See
[Activate/Deactivate Job](../server-group-job-task-area/job-list/activate-deactivate-job).
