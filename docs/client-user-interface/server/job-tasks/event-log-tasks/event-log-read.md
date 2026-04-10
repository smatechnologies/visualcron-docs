---
sidebar_label: 'Task Event Log - Event Log Read'
hide_title: 'true'
---

## Task Event Log - Event Log Read

The Event log Read Task retrieves event log records based on a filter.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Event%20Log%20Tasks/Event%20Log%20-%20read.png)

**Scope**

Select whether to read the event log from the local machine or a remote computer.

* _Local_ - reads the event log on the machine where VisualCron is running
* _Remote_ - reads the event log on a remote computer; enables the remote host field below

**Remote host**

The hostname or IP address of the remote computer. Only enabled when _Remote_ is selected.

**Credentials**

Optional credential for accessing the remote computer's event log. The Credential must match the user name and password of the user you want to log in as.
 
**Event log entry filter**

**Event log**

The Windows event log to read from (e.g. Application, System, Security).

**Source**

Filter entries by source. Select a condition type and enter a value. The value field is disabled when the condition is set to _Not check_.

**Entry type**

Filter entries by entry type. Select a condition type and an entry type value. Available condition types: _Not check_, _Equal_, _Not equal_.

**Category ID**

Filter entries by category ID. Select a condition type and enter a numeric value. The value field is disabled when the condition is set to _Not check_.

**Event ID**

Filter entries by event ID. Select a condition type and enter a numeric value. The value field is disabled when the condition is set to _Not check_.

**Category**

Filter entries by category name. Select a condition type and enter a value. The value field is disabled when the condition is set to _Not check_.

**Message**

Filter entries by the event message text. Select a condition type and enter a value. The value field is disabled when the condition is set to _Not check_.
