---
sidebar_label: 'Event Trigger - Event Log'
hide_title: 'true'
---

## Event Trigger - Event Log

The Event log Trigger fires when an entry is written to a Windows event log, on the Server computer or on a remote computer. Conditions on the log, the event ID, the source, the level and the description select which entries fire it.

The Trigger reads the event log through the Windows Event Log service, not through WMI, and receives entries as they are written. To watch another computer, enter its name or IP address in *Computer name* on ***Main settings*** and select a Credential under *Credentials*. To view the logs, open Event Viewer (`eventvwr.msc`).
 
The settings are on the ***Event log*** tab.

![Event log tab of the Add/Edit event window with the Log file, Category id, Category, Event id, Event type, Description contains and Source conditions, each set to Ignore](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Event%20Log.png)

Each condition has an operator list next to it: *Ignore*, *AND* or *OR*. *Ignore* turns the condition off; *AND* and *OR* turn it on and make its field available. *Description contains* offers only *Ignore* and *AND*. A new Trigger has every condition set to *Ignore*.

The conditions combine as follows:

* An entry must match every condition set to *AND*
* An entry that matches a condition set to *OR* fires the Trigger, even if it does not match a condition set to *AND*
* A condition set to *OR* that an entry does not match does not exclude the entry; if you use only *OR* conditions, every entry fires the Trigger

:::warning

With every condition set to *Ignore*, each entry written to the Application log fires the Trigger. Set at least one condition to *AND* to select the entries, and use *OR* only when any single match should fire the Trigger.

:::
 
**Log file**

The event log to watch. The list shows the classic logs of the Server, such as "Application", "Security" and "System". You can also type a log name, for example a full channel name such as `Microsoft-Windows-TaskScheduler/Operational`. Set the operator to *AND*. The name must match exactly, including case, so select it from the list or copy it from Event Viewer. With *Ignore*, the Trigger watches only the Application log. With *OR*, every entry of the log fires the Trigger, because the Trigger receives only entries from that log. The field can contain Variables.
 
**Category id**

The task category number of the entry. Event Viewer shows the category as text in *Task Category*; the number is the `Task` value in the entry's XML view on the *Details* tab. Enter a number.
 
**Category**

Compared with the same task category number as *Category id*, not with the category text, so text such as "Logon" never matches. Use *Category id* instead.

**Event id**

The event ID that Event Viewer shows in the *Event ID* column, for example 7036. Enter a number.
 
**Event type**

The level of the entry. The list offers *Error*, *Warning*, *Information*, *SuccessAudit* and *FailureAudit*. The Trigger compares the number of the selected type with the entry's level, so the types match these Event Viewer levels:

| Event type | Matches entries with the level |
|---|---|
| *Error* | Critical |
| *Warning* | Error |
| *Information* | Information |
| *SuccessAudit* | none |
| *FailureAudit* | none |

:::warning

To react to entries that Event Viewer shows as Error, select *Warning*. No type matches Warning or Verbose entries. No type matches entries with level 0 either. These include Security log audit entries and other entries that Event Viewer shows as Information. Select those entries by *Event id* or *Source* instead, for example *Event id* 4625 for a failed logon.

:::
 
**Description contains**

Text that must appear in the entry's description, the message that Event Viewer shows on the *General* tab. The comparison is case-sensitive. Only *Ignore* and *AND* are available. The field can contain Variables.
 
**Source**

The name of the provider that wrote the entry, for example "Service Control Manager". Copy it from the `Name` of `Provider` in the entry's XML view on the *Details* tab. It must match exactly, including case. The field can contain Variables.

:::note

Some entries cannot be compared with a condition: an entry without a task category (*Category id*), an entry without a level (*Event type*), or an entry whose description cannot be read (*Description contains*), for example because the message file of its source is not installed, which is common for entries read from a remote computer. For such an entry, VisualCron logs an error, the entry passes that condition, and the conditions below it on the tab, such as *Source*, are not checked. If such entries fire the Trigger, set a condition above it on the tab, such as *Log file* or *Event id*, to *AND* so that it still selects the entries.

:::
 
This setting is on the ***Main settings*** tab.
 
**Polling interval**

The Trigger does not poll for entries. If it cannot start reading the log, for example because the remote computer is not available, it tries again after this many seconds (default 60). After three failed attempts, the Trigger is deactivated.

### Result Variables

Each time the Trigger fires, it sets result Variables for the entry, for example its event ID, `{TRIGGER(Active|LastTrigger|EventLog.Result.EventId)}`. With *Last trigger* (`Active|LastTrigger`), a Variable reads the result of the firing that started the run. All Event log Trigger result Variables are described in [Variables](global-variables).
