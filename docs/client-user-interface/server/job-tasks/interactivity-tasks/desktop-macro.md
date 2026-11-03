---
sidebar_label: 'Task Interactivity - Desktop Macro'
hide_title: 'true'
---

## Task Interactivity - Desktop Macro

The Desktop macro Task records mouse moves and keystrokes on a desktop and plays them back when the Task runs.

:::note

The Desktop macro Task is obsolete. Use the [Robot Task](robot-task/overview) for new automation.

:::

Typical uses are:

- web automation
- testing
- automating manual work
- working with Excel

The Task needs a desktop to play back onto. The [VisualCron Server](../../../../using-visualcron/visualcron-server) runs as a service, so playback runs in the [VisualCron Tray Client](../../../../using-visualcron/visualcron-tray-client) on a logged-on desktop, and the Task must run in the foreground; see [Task Main Settings - Execution Context](../../task-main-settings-execution-context). If the Server finds no Tray Client connection for the Task, the Task fails with "Could not find the specified Connection for execution."

![Desktop macro tab with the Macro info, Record and Playback groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Desktop%20Macro.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Desktop macro tab

#### Macro info

- _Edit_: Opens _Desktop macro - steps_, the list of recorded steps, where you can open a keyboard or mouse step and change it. Available when the macro has steps
- _Length_: The playback length of the macro at "Normal" speed

#### Record

- _Start Recording_: Minimizes the VisualCron windows and starts recording. Perform the steps you want the Task to repeat. Press CTRL + ALT + S, or click the stop button in the record stop window, to stop recording. Work slowly: the time a program or window takes to open can vary from run to run
- _Show record stop dialog_: When cleared, the record stop window is not shown, and CTRL + ALT + S is the only way to stop recording

#### Playback

- _Show playback window_: When selected, the Tray Client shows a notification that the macro is playing and that holding ESC stops it
- _Suppress error message boxes_: When selected, a playback error is not shown in a message box on the desktop. The error is written to standard error in either case
- _Abort if no window is found_: Saved with the Task, but playback does not use it: when a window from the recording is not found, playback continues with the next step
- _Playback speed_: How fast the macro plays back:
  - "Normal": the pauses between steps are the recorded pauses
  - "High": the pauses are half the recorded pauses
  - "Ultra": the pauses are a quarter of the recorded pauses

### Output and errors

- When a playback error occurs, the Task fails, and the error is written to standard error
- Holding ESC during playback stops the macro, and the Task reports success
