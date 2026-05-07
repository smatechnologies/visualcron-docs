---
sidebar_label: 'Task Event Log - Event Log Read'
hide_title: 'true'
---

## Task Event Log - Event Log Read

The Event log Read Task retrieves event log records based on a filter.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Event%20Log%20Tasks/Event%20Log%20-%20read.png)

**Scope**

**Local** / **Remote**

Select **Local** to read the event log on the local computer. Select **Remote** to read the event log on a remote computer. Defaults to **Local**.

**Remote host**

Enter the hostname or IP address of the remote computer, or select from the list of network computers. Only available when **Remote** is selected.

**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the *Settings* icon to open *Manage credentials* in order to add or edit Credentials.
 
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
