---
sidebar_label: 'Task Office365 - Get Calendar Events'
hide_title: 'true'
---

## Task Office365 - Get Calendar Events

The Office365 - Get Calendar event(s) Task lets you retrieve calendar events from the Office365 cloud. The values entered below act as filter criteria — only fields that you fill in are used to narrow the result. The Task uses the [Office365 Connection](../../connection-office365).

**Office365 - Get calendar events** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office365%20Tasks/O365%20Get%20calendar%20events.png)

**Connection**

To use the Office365 Tasks you need to create a [Connection](../../global-connections) first. Click the *Settings* icon to open the *Manage Connections* dialog.

**Calendar name**

The name of the calendar to read from. Leave empty to use the default calendar.

**Event start date/time**

Restrict the result to events starting on or after this date and time.

**Event end date/time**

Restrict the result to events ending on or before this date and time.

**All day**

Filter on the all-day flag. Check to include only all-day events, uncheck to exclude them, or use the indeterminate (greyed) state to ignore this filter.

**Event subject**

Restrict the result to events whose subject matches the value entered.

**Event location**

Restrict the result to events whose location matches the value entered.

**Event body**

Restrict the result to events whose body matches the value entered.

**Reminder minutes before start**

Restrict the result to events whose reminder is set to the specified number of minutes before start.

**Importance**

Restrict the result to events with the selected importance level. Available options:

* _Low_
* _Normal_
* _High_

**Response requested**

Filter on the response-requested flag. Use the indeterminate (greyed) state to ignore this filter.

**Output**

Configure how the matching events are written to standard output, including which calendar information columns to include, whether to include column names, the field separator, the text qualifier and the line break style.
