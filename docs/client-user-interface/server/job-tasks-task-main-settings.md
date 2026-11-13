---
sidebar_label: 'Task - Main Settings'
hide_title: 'true'
---

## Task - Main Settings

A set of different Task types can be defined using the **Add/Edit Job > Tasks** tab, then press the Add button to display the list of Tasks.
 
**Add Job > Tasks > Add** tab

![Add Job window, Tasks tab, opened with Add Job on the toolbar](../../../static/img/Client%20User%20Interface/Toolbar/Add%20Job.png)

After selecting a Task, in this case *Export settings* from the *Internal* group, the **_Main settings_** tab is displayed. Also, the selected Task is preset as *Task type* but this may be changed.
 
**Add/Edit Task > Main settings** tab

![Edit Task window, Main settings tab, opened from a Task on the Job's Tasks tab](../../../static/img/Client%20User%20Interface/Toolbar/Task%20Main%20Settings.png)

:::tip Note 

If several Tasks are defined for a Job and the Tasks are under execution, the Task information fields will include just executed, present and previous information. In the Add/Edit Job > Tasks window, adjust the Change Task order in which the Tasks are executed.

::: 

**Name**

The name of the Task.
 
**Description**

A description of the Task.

**Encoding**

Sets the code page the Task uses to read and write text. A new Task gets the Server's default code page. Not every Task type uses this setting.
 
**Execution context**

Click the Change button to set [Execution context](../server/task-main-settings-execution-context).
 
**Processor affinity settings**

This controls whether the CPU usage of a Task is handled *Automatically* (divided over processors/cores) or run on specific processors/cores (*Custom*). Click the *Set affinity* button to choose the option and, for *Custom*, the individual processors/cores.
 
**Store standard output / Store standard error**

By default, VisualCron is capturing and storing all output from executed processes. If you don't want this and want Windows to capture all output you uncheck these options.
 
**Extended Task debug logging**

When selected, the Task writes additional debug entries to the Server log, and some Task types also add debug information to the Task's output, where later Tasks and Notifications that use the output also receive it. Support may ask you to select it to investigate a problem; clear it again afterward.
 
**Task order**

The task order can be changed by either clicking on the up/down arrows next to each Task or select a Task row and edit the Change Task order numeric field.
 
**Edit Job > Tasks** tab

![Tasks tab of the Edit Job window with a list of Tasks](../../../static/img//Client%20User%20Interface/Toolbar/List%20of%20Tasks.png)

**Loop**

Loops can be added to one or more Tasks, read more about [loops](../server/job-tasks-loop-functionality) here.
