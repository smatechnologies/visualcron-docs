---
sidebar_label: 'Task System - Control Monitor'
hide_title: 'true'
---

## Task System - Control Monitor

The Control monitor Task turns the monitor of a logged-on user's desktop on or off. Depending on the monitor type, the amount of power saved when turning off a monitor varies, but the monitor accounts for a large part of the total power consumption.

Some typical power consumption levels (watts) for computer equipment are:

* Desktop computer: 60W
* CRT (Cathode Ray Tube) monitor: 75W
* Flat screen monitor: 25W
* Laser jet printer: 7.2W

![Control monitor Task settings, with the Turn on and Turn off options](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Control%20Monitor.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Control monitor tab

- _Turn on_: powers the monitor on
- _Turn off_: powers the monitor off. Selected by default

The Task runs through the [VisualCron Tray Client](../../../../using-visualcron/visualcron-tray-client), so a user must be logged on to the VisualCron Server computer with the Tray Client connected. To choose the desktop session, use foreground execution in the Task's execution context; see [Task Main Settings - Execution Context](../../task-main-settings-execution-context). When no Tray Client session is found, the Task fails.
