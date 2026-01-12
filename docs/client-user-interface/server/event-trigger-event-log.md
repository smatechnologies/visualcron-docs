---
sidebar_label: 'Event Trigger - Event Log'
hide_title: 'true'
---

## Event Trigger - Event Log

The Event log trigger is watching the Windows event log for changes. Many applications and Windows itself logs directly to the event log. With this trigger you can monitor the common logs or specific logs for changes based on event ID, source, message etc.
 
Some applications create their own log files and it is possible for you to create one or view events by the Windows application "Event viewer" which is found in Windows Control Panel -> Administrative tools. This event trigger is based on **WMI**.
 
**Triggers > Add > Event Trigger > Event log** tab

![](../../../../visualcron-docs/static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Event%20Log.png)

You can choose what kind of conditions to use by first enabling the setting and then enter a value in the text window or select a value. When enabling a condition you can choose to use "AND" or "OR". Think of it's as a query.
 
**Log file**

Probably you know what log file to look for. Select a specific log file or you may be flooded with Event log events from other log files.
 
**Category id**

Each application (event source) can define its own numbered categories and the text strings to which they are mapped. The Event Viewer can use the category to filter events in the log. The categories must be numbered consecutively beginning with number 1.
 
**Category**

This is a description of the numeric value, which could be, for example: "Kernel" or "Disk". Each application (event source) can define its own numbered categories and the text strings to which they are mapped. The text strings associated with the category are stored in the computer's registry. The Event Viewer can use the category to filter events in the log.
 
**Event id**

Event code is a numeric value to further distinguish an entry.
 
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