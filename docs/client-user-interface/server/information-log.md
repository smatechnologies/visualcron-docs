---
sidebar_label: 'Information - Log'
hide_title: 'true'
---

## Information - Log

The _Log_ window shows log events from your Client and from the Server as they happen. It also lets you search the log history the Server keeps in its log database. Use it to follow what the Server is doing, or to find past Job, Task, Notification and transfer events.

To open it, click the main menu _Server_ -> _Information_ -> _Log_. You need the "Log" permission with "Read" (see [Main - User Permissions](main-user-permissions)). The window stays open next to the main window until you close it.

The filters in this window change only what you see. What the Server logs, and how long it keeps the log, is set in [Settings - Log Settings](settings-log-settings).

_Server_ -> _Information_ -> _Log_

![Log window opened from the Information group of the Server tab of the main menu, showing the File and Filter menus, the Realtime - general tab and five Historic tabs, a list of debug-level Client events, the Set extra filter lists with Clear filter, and the log count in the status bar](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Information%20-%20Log/Log%20Information.png)

### Tabs

- **_Realtime - general_**: live events; when the window opens, this tab receives the recent events the Server holds in memory (about the latest 1000) and your Client's own events, then adds new events as they occur
- **_Historic - general_**, **_Historic - Job_**, **_Historic - Task_**, **_Historic - Notification_** and **_Historic - transfers_**: search the Server's log database; choose the date range (on **_Historic - Task_**, **_Historic - Notification_** and **_Historic - transfers_**, also the Job and Task) and click _Get_; _Filter..._ adds filters on the columns, and the **_Historic - Job_** and **_Historic - Task_** tabs also have _Export.._ and a search in the output text

The Historic tabs show data only when _Log to database_ is on in [Settings - Log Settings](settings-log-settings), and only as far back as the log is kept. _Clear memory_ in [Information - Server Info](information-server-info) empties the Server's in-memory events, so a Log window opened after that starts with fewer realtime events.

### Extra filter

On the **_Realtime - general_** tab, _Set extra filter:_ filters the list on one column: "No filter", "Source", "Message", "Event time", "Event type", "Job name", "JobId" or "TaskId". For "Message", "Event time" and "Job name", type the text to look for; for "Source" and "Event type", pick a value from the second list. "JobId" and "TaskId" filter on the Job or Task the Log window was opened for; text typed in the box is not used. _Clear filter_ removes the extra filter.

### File menu

- _Export_: saves the **_Realtime - general_** list as an Excel file (.xls); choose a folder, enter a file name and click _Save_
- _Close window_: closes the Log window

### Filter menu

The _Filter_ menu shows or hides one type of event in the realtime list: _Debug_, _Information_, _Error_ or _Communication_. Click a type to hide it, and click it again to show it. The icon changes to show which types are hidden. Your choices are saved with your Client settings. They change only what this window shows, not what is logged.
 
### Columns

The realtime list has these columns:

- _Source_: whether the event came from the Server or from your Client
- _DateEvent_: when the event happened; if you are connected remotely, the Server's time can differ from your computer's time
- _EventType_: an icon for the type of event, matching one of the types in the _Filter_ menu
- _Job_: the Job the event belongs to, if any
- _Task_: the Task the event belongs to, if any
- _Message_: the description of the event
 
### Status bar

The status bar shows _Log count_ (the number of events shown and the total number of events) and _Last event_ (the time of the most recent event).
