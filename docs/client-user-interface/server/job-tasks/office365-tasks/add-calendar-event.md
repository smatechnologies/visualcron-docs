---
sidebar_label: 'Task Office365 - Add Calendar Event'
hide_title: 'true'
---

## Task Office365 - Add Calendar Event

The Office365 - Add Calendar Event Task lets you add a Calendar event in the Office365 cloud. The Task uses the [Office365 Connection](../../connection-office365).
 
**Office365 - Add calendar event** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office365%20Tasks/O365%20Add%20Calendar%20events.png)

**Connection**

To use the Office365 Tasks you need to create a [Connection](../../global-connections) first. Click the *Settings* icon to open the *Manage Connections* dialog.

**Calendar name**

The name of the calendar in which the event should be created. Leave empty to use the default calendar.

**Event subject**

The subject (title) of the calendar event. Required.

**Event start date/time**

The start date and time of the event. Required when *All day* is unchecked.

**Event end date/time**

The end date and time of the event. Required when *All day* is unchecked.

**All day**

When checked, the event is created as an all-day event and the start and end date/time fields are disabled.

**Event body**

The body text of the event.

**Event location**

The location of the event.

**Reminder minutes before start**

The number of minutes before the start time at which a reminder should be raised.

**Importance**

The importance flag stored on the event. Available options:

* _Low_
* _Normal_
* _High_

**Response requested**

Sets whether responses are requested from invited attendees. Use the indeterminate (greyed) state to leave the value unset.

**Recurrence range start / end**

The first and last date on which the recurring event should occur. Leave empty for a non-recurring event.

**Recurrence pattern type**

How often the event repeats. Available options:

* _Daily_
* _Weekly_
* _Monthly_
* _Yearly_

The recurrence sub-fields below show or hide automatically based on the selected *Type*.

**Interval**

The interval between recurrences (for example, "every 2 weeks"). Hidden for *Daily*.

**Month**

The month in which the event recurs. Used only for *Yearly*.

**Day / Every**

The day-of-the-month or recurrence anchor for the event. The label and behavior change with the selected *Type*.

**Day of month**

The numeric day of the month on which the event recurs.

**Index**

For relative monthly or yearly recurrence, selects the occurrence within the month (First, Second, Third, Fourth, Last).

**Days of week**

The days of the week on which the event recurs. Multiple days can be selected.
