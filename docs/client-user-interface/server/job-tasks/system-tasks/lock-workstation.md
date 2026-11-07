---
sidebar_label: 'Task System - Lock Workstation'
hide_title: 'true'
---

## Task System - Lock Workstation

The Lock workstation Task locks the desktop of a user who is logged on to the VisualCron Server computer.

![Lock workstation Task settings, with the Credentials group and an empty Lock settings group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Lock%20Workstation.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Lock workstation tab

- _Credentials_: not used by this Task

The _Lock settings_ group has no settings. By default, the Task locks the active desktop session of the VisualCron Server computer. With foreground execution in the Task's execution context, it locks the session selected there; see [Task Main Settings - Execution Context](../../task-main-settings-execution-context).

When no user is logged on, the Task fails. On success, the Task writes no output.
