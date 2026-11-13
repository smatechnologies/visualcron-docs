---
sidebar_label: 'Task - On Error'
hide_title: 'true'
---

## Task - On Error

The **On error** tab in the Task window controls what is causing an error in VisualCron. Compare this with [Task Flow](task-flow) which controls what happens when a Task completes.
 
**Add/Edit Task > On error** tab

![Edit Task window, On error tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Task%20Main%20Settings/On%20Error%20Settings.png)

**Error causes**

Different Task types have different reasons to fail, so the list of errors on this tab depends on the Task type. For example, the FTP Task lists "Unaccepted FTP server reply" and "No file(s) downloaded". Every Task type also lists "IO exception", "Permission denied", "Task times out" and "Unhandled errors". Select which of them count as an error for this Task.
 
**Error cause categories**

VisualCron evaluates a set of different error categories that will trigger the Task into error state:

* "All errors" - all kinds of errors raise a Task error

* "Only selected errors" - only the items that you select in the list raise a Task error

* "All except selected" - only the items that you have not selected in the list raise a Task error

A Task can also meet an error that is not in its list. For example, the FTP Task meets "Connection not found" when its Connection no longer exists, but "Connection not found" is not in the FTP Task's list. With "Only selected errors", which is the default, VisualCron ignores such an error: the Task continues without that step and can finish as successful. To have such an error raise a Task error, select "All errors" or "All except selected".
 
**Exit code collection**

Exit codes control the result of the Task. A new Task uses the Server's *Default exit code collection*, which is the Windows collection unless it was changed: 0 is success and other codes are errors defined by Microsoft. You can create your own collection of exit codes to control which codes count as success and how they are described. See [Task - Exit Code Collection](task-exit-code-collection).
 
**Output/Variable error handling**

It is possible to control if the Task should raise an error based on output, output (err) and any Variable/value that matches a certain condition at runtime. It is also possible to do the opposite, override an error based on these conditions.
 
**Raise error**

**Not set** 

Default setting which means that there will be no other error handling than the "Error cause" on top of **On error** tab.

**Raise error** 

This means that if the conditions below match any success of Task will be overridden with an error and specified exit code.

**Do not raise error** 

If the conditions below match and the Task's exit code equals the *Exit code* value, a failure is changed to success. Set *Exit code* to the code the Task returns for that failure: with the default 77777, only a failure with exit code 77777 is changed. The exit code itself is not changed.
 
**Exit code**

With *Raise error*, the exit code the Task gets when the condition matches. With *Do not raise error*, the exit code that must match for a failure to be changed to success. The default value is 77777.
 
**Check type**

Select *If output*, *If error output* (the default) or *If other value*. With *If other value*, use both text fields to compare two values or Variables.
 
**Type**

This controls with what data type the comparison is made.
 
**Condition**

This is the type of condition that it is trying to match on; Equal, Contains, Not equal etc.
 
**Value/Variable**

This is the field where you enter the value you want to match the condition with. Click the Variables icon to open the Variables list.