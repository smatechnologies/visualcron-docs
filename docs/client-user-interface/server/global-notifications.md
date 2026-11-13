---
sidebar_label: 'Global - Notifications'
hide_title: 'true'
---

## Global - Notifications

A notification is a Task that is stored once on the Server and run from the Flow of any Job or Task. A typical notification is an Email Task that reports a failure. Use a notification when several Jobs or Tasks should do the same thing on an event: when you change the notification, every Flow that runs it uses the new settings.

This page covers the _Manage Notifications_ window, the window where you add and edit a notification, the Variables you can use in a notification, what to check when a notification does not run, and the Notification log.

To open the window, click _Server_ -> _Global objects_ -> _Notifications_. The Settings icon next to the notification list in [Job Flow](job-flow) and [Task Flow](task-flow) opens the same window. [Load Balancing](../servers/load-balancing-flows) actions can also run a notification.

### Manage Notifications window

![Manage Notifications window with the Add, Edit, Delete, Clone and Audit log toolbar and one notification, Email - Send, in the Name column](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Notifications/Notifications.png)

The grid lists each notification with the icon of its Task type and its _Name_, sorted by name. Double-click a notification to edit it.

The toolbar has these commands:

- _Add_: choose the Task type of the new notification
- _Edit_: edit the selected notification
- _Delete_: delete the selected notifications
- _Clone_: copy the selected notification, see [Clone or delete a notification](#clone-or-delete-a-notification)
- _Audit log_: open the [Audit log](../tools/objects-audit-log) for all notifications

Right-click a notification for these commands:

- _Add_, with the Task types as a submenu
- _Edit_ and _Delete_
- _Audit log_: the Audit log for the selected notification
- _Versions.._: the [version history](../tools/audit-log-versions) of the notification
- _Object relations_: the Jobs and Tasks whose Flow runs the notification, see [Object relations](../tools/object-relations)
- _Notification log_: the [Notification log](#notification-log) for the selected notifications
- _Export ..._: export the selected notifications with [Export settings](../file/export-settings)
- _Send to connection ..._ and _Send to server connection ..._: send a copy of the notification to another VisualCron Server

Press Delete to delete the selected notifications, or Ctrl+A to select all of them.

### Add or edit a notification

1. In the _Manage Notifications_ window, click _Add_ and choose the Task type.
2. On the ***Main settings*** tab, change _Name_ to a name that says what the notification does, for example "Email ops on failure". A new notification is named after its Task type, for example "Email - Send", so several notifications can otherwise look the same in the Flow list.
3. On the tab named after the Task type, fill in the settings of that Task. See the page for that Task.
4. Click _OK_.

The _Add/Edit Notification_ window has these tabs:

- ***Main settings***: _Task type_ (choose a Task type from the list, or type in the search box to find one), _Name_ and _Encoding_
- The Task type tab: the settings of the Task, including any Connection or Credential it uses
- ***Output***: only for Task types that have output settings, for example SQL or Web Service. See the page for that Task type

Click _Variables_ in the status bar to insert a Variable, see [Variables](#variables).

When you edit a notification, the window shows the link _Copy Notification id_. Click it to copy the notification's Id to the clipboard. Right-click it to change the Id: enter the new Id, which must be a GUID. VisualCron shows how many objects refer to the notification. Click _Yes_ to change the Id and update the Jobs and Tasks that use it, _No_ to see the list of objects first, or _Cancel_. If another notification already uses that Id, VisualCron asks for a different value. The new Id is saved on the Server as soon as you click _Yes_; clicking _Cancel_ in the _Add/Edit Notification_ window does not undo it. Scripts or API calls that use the old Id are not updated.

### Clone or delete a notification

_Clone_ opens a copy of the selected notification, with all its settings, in the _Add/Edit Notification_ window. The copy gets a new Id and is saved when you click _OK_. It has the same name as the original, so change the name to tell them apart. Jobs and Tasks that run the original keep running the original.

When you delete a notification that other objects use, VisualCron tells you how many objects use it. Open _Object relations_ to see them before you delete.

:::warning

A Flow action that runs a deleted notification runs nothing. Change those Flows to run another notification before you delete one.

:::

### Run a notification from Flow

In the Flow of a Job or a Task, choose the event, for example _On error_, and select _Run Notification_ with the notification to run. See [Job Flow](job-flow) and [Task Flow](task-flow). This example shows a Job's Flow that runs the notification "Email - Send" on error:

![Edit Job window on the Flow tab, and the Job Flow window with the event On error and Run Notification set to Email - Send](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Notifications/Job%20Notification%20Flow.png)

### Variables

You can use [Variables](global-variables) in any field of a notification. The notification runs as its own Task, started by the Flow of a Job or a Task. This decides what the Variables refer to:

- `{JOB(Active|<property>)}`: the Job whose Flow ran the notification, or the Job of the Task whose Flow ran it
- `{TASK(PrevTask|<property>)}`: the Task whose Flow ran the notification. In a Job's Flow, this is the last Task that ran, or for _On running longer than_ the Task that is still running. In the Variables window, choose _PrevTask (previous or last context sensitive Task)_ to insert it
- `{TASK(Active|<property>)}`: the notification itself

For example, an Email notification run on _On error_ can use the subject `{JOB(Active|Name)} failed` and the body `{TASK(PrevTask|Name)}: {TASK(PrevTask|StdErr)}`. `StdOut` and `StdErr` have a value only if that Task stores its standard output or standard error, see [Task - Main Settings](job-tasks-task-main-settings).

The values of the Task that ran the notification are current only for events after that Task has run, such as _On success_, _On error_ and _On complete_. For _On start_ and _On running longer than_, they still hold the values of the Task's previous run.

:::note

A notification run by a Job's Flow on _On start_ runs before any Task of the Job. `{TASK(PrevTask|...)}` then returns the values of the notification itself.

:::

### When a notification does not run

- Check that the Flow of the Job or Task has a _Run Notification_ action for the event that happened, and that the action's condition, for example _Always_ or _If exit code_, matches. See [Run a notification from Flow](#run-a-notification-from-flow)
- Check in _Object relations_ that the notification is still used by that Flow. A Flow action that runs a deleted notification runs nothing
- Open the [Notification log](#notification-log). If the run is listed, check _Exit code_ and _Output (error)_

### Notification log

The Notification log shows each run of a notification: when it ran, which Flow event ran it, and its exit code and output. To open it, right-click one or more notifications in the _Manage Notifications_ window and click _Notification log_. The window title is _Notification history_, followed by the notification's name when you open it for one notification. The ***Historic - Notification*** tab of the [Log](information-log) window shows the same log. There you can also limit it to a Job and a Task, and the grid has no _Job name_ and _Task name_ columns.

#### Filter the log

- The notification list at the top: a checkbox for each notification. The notifications you selected before opening the log are checked. When you close the list, the dates are reset to the logged runs of the checked notifications and the log reloads. If no notification is checked, the log is cleared
- The _Filter.._ box at the top of the notification list: type to narrow the list by name or description. The button next to the box clears it
- The two date boxes: the date range, from the first date to the second. When the window opens, the range covers all logged runs of the checked notifications, and those runs are loaded. Each date covers the whole day. If there are no logged runs, the date boxes and _Get_ are unavailable
- _Get_: load the runs in the date range from the Server
- The _Filter..._ button: show or hide the filter row of the log grid, where you can filter on any column

:::tip

When every notification shown in the list is checked, closing the list resets the dates but does not reload the log. Click _Get_ to reload it.

:::

#### Log grid

The newest runs are listed first. The grid has these columns (the order on screen can differ):

- The Task type icon of the notification
- The notification name
- _Event time_: when the notification started
- _Exit code_ and _Execution time_
- _Output (standard)_ and _Output (error)_: double-click a cell to open the output, if the notification stored it
- _Event type_: the Flow event that ran the notification: _On start_, _On error_, _On success_, _On complete_ or _On running longer than_
- An icon that shows success, failure or still waiting
- _Job name_ and _Task name_: the Job and Task whose Flow ran the notification. These columns are shown only when you open the log from the _Manage Notifications_ window
- _Result_: double-click a cell to open the result, if there is one
