---
sidebar_label: 'Task Event Log - Event Log Write'
hide_title: 'true'
---

## Task Event Log - Event Log Write

The Event log - write Task writes an entry to a Windows event log on the Server computer or on a remote computer.

![Event log - write tab, with the scope settings and the event log entry settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Event%20Log%20Tasks/Event%20Log%20-%20write.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Event log - write tab

**Scope**

- _Local_ (default): writes to the event log of the Server computer
- _Remote_: writes to the event log of another computer. Enter its host name or IP address in the box next to it, or select it from the list of network computers. The host name cannot contain Variables
- The Credential: the Credential the Task runs as when it writes the entry. Click the settings button to open _Manage credentials_; see [Credentials](../../global-credentials)

**Event log entry**

- _Event log_: the event log to write to, "Application" by default
- _Source_: the source name of the entry. If the source does not exist on the computer, the Task creates it for the selected event log, which needs administrator rights
- _Entry type_: "Information" (default), "Error", "Warning", "SuccessAudit" or "FailureAudit"
- _Event ID_: the event ID, a number, "0" by default
- _Category ID_: the category number, "0" by default
- _Message_: the text of the entry. Text beyond 32,766 characters is cut off

Event log, source, event ID, category ID and message may contain Variables.

### Output and errors

The output is the event ID of the written entry. If the entry cannot be written, for example because the event ID or category ID is not a number, the Task fails.
