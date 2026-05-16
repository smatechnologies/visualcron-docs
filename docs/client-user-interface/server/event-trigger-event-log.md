---
sidebar_label: 'Event Trigger - Event Log'
hide_title: 'true'
---

## Event Trigger - Event Log

The Event log trigger is watching the Windows event log for changes. Many applications and Windows itself logs directly to the event log. With this trigger you can monitor the common logs or specific logs for changes based on event ID, source, message etc.
 
Some applications create their own log files and it is possible for you to create one or view events by the Windows application "Event viewer" which is found in Windows Control Panel -> Administrative tools. This event trigger is based on **WMI**.
 
**Triggers > Add > Event Trigger > Event log** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Event%20Log.png)

Each condition has an operator dropdown next to it with three options: **Ignore**, **AND**, or **OR**. Setting the operator to _Ignore_ disables that condition, while _AND_ or _OR_ enables the value field and combines the condition with the others. Think of it as building a query.

Note: the **Description contains** condition only supports _Ignore_ and _AND_ — it cannot be combined using _OR_.
 
**Log file**

Probably you know what log file to look for. Select a specific log file or you may be flooded with Event log events from other log files.
 
**Category id**

Each application (event source) can define its own numbered categories and the text strings to which they are mapped. The Event Viewer can use the category to filter events in the log. The categories must be numbered consecutively beginning with number 1.
 
**Category**

This is a description of the numeric value, which could be, for example: "Kernel" or "Disk". Each application (event source) can define its own numbered categories and the text strings to which they are mapped. The text strings associated with the category are stored in the computer's registry. The Event Viewer can use the category to filter events in the log.

**Event code**

A numeric value that further distinguishes an event log entry. Enter the event code that the trigger should match.
 
**Event type**

There exist some predefined event types which can be selected from the combo box. The predefined event types are:
* "Error" - An error event, indicates a significant problem the user should be aware of; usually a loss of functionality or data
* "Warning" - A warning event, indicates a problem that must not be taken care of immediately, but may indicate conditions that could cause future problems
* "Information" - An information event, indicates a significant and successful operation
* "SuccessAudit" - A success audit event, indicates a security event that occurs when an audited access attempt is successful; for example, logging on successfully
* "FailureAudit" - A failure audit event, indicates a security event that occurs when an audited access attempt fails; for example, a failed attempt to open a file
 
**Description contains**

The formatted, localized text for the message. This includes associated replacement strings. Enter a text that exists in a part of the description/message.
 
**Source**

The event source indicates what initiated the event. It is often an application name or the name of a subcomponent of the application if the application is large. Applications and services usually write to (and therefore are sources for) the Application log or a custom log. Device drivers usually write to the System log.
 
**Main settings** tab
 
**Polling interval**

This value is also used for Event log trigger, in the case where (usually) the remote host is temporarily unavailable to start Windows event log tracking. A number of repeated attempts to connect to the remote host will be made at the specified time intervals.
