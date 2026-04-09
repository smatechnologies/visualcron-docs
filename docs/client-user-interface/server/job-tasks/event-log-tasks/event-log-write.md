---
sidebar_label: 'Task Event Log - Event Log Write'
hide_title: 'true'
---

## Task Event Log - Event Log Write

The Event log Write Task writes an event log record value based on various parameters.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Event%20Log%20Tasks/Event%20Log%20-%20write.png)

**Scope**

Select whether to write to the event log on the local machine or a remote computer.

* _Local_ - writes to the event log on the machine where VisualCron is running
* _Remote_ - writes to the event log on a remote computer; enables the remote host field below

**Remote host**

The hostname or IP address of the remote computer. Only enabled when _Remote_ is selected.

**Credential**

Optional credential for accessing the remote computer's event log. The Credential must match the user name and password of the user you want to log in as.

**Event log entry**

**Event log**

The Windows event log to write to (e.g. Application, System, Security).

**Source**

The source name to associate with the event log entry.

**Entry type**

The type of event log entry to write. Options include Error, Information, Warning, FailureAudit, and SuccessAudit.

**Event ID**

The numeric event ID to assign to the entry.

**Category ID**

The numeric category ID to assign to the entry.

**Message**

The message text to write to the event log entry.
