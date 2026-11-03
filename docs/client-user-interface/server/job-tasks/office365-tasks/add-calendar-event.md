---
sidebar_label: 'Task Office365 - Add Calendar Event'
hide_title: 'true'
---

## Task Office365 - Add Calendar Event

The Office365 - Add calendar event(s) Task adds an event, or a recurring series, to a calendar of a Microsoft 365 user, using an [Office365 Connection](../../connection-office365).

![Office365 - Add calendar event(s) tab with the Connection, Event parameters and Event recurrence groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office365%20Tasks/O365%20Add%20Calendar%20events.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Office365 - Add calendar event(s) tab

#### Connection

- _Connection_: The [Office365 Connection](../../connection-office365) to use. The Task works on the calendars of the Microsoft 365 user the Connection signs in as. Click the _Settings_ icon to open _Manage Connections_

#### Event parameters

- _Calendar name_: A calendar to check before the event is added, matched exactly. If the named calendar cannot be edited, the event is not added. The event is created in the user's default calendar
- _Event start date/time_: When the event starts, in the Server computer's time zone. Required unless _Is all day_ is selected. A value that cannot be read as a date makes the event start at the next full hour
- _Event end date/time_: When the event ends, in the Server computer's time zone. Required unless _Is all day_ is selected. A value that cannot be read as a date makes the event end two full hours after the hour the Task runs
- _Is all day_: When selected, the event is an all-day event on the day the Task runs; the start and end values are not used
- _Event subject_: The subject of the event. Required
- _Event location_: The name of the location. Text after a `;` is read as the location's e-mail address and address, so do not use `;` in a plain location name
- _Reminder minutes_: The number of minutes before the start that the reminder appears. A value that is not a whole number is ignored
- _Importance_: "Low", "Normal" or "High". With none selected, the importance is not set
- _Event body_: The text of the event, sent as plain text
- _Response requested_: Selected or cleared sets whether responses are requested; the indeterminate state leaves it unset

[Variables](../../global-variables) are resolved in the text and date fields.

#### Event recurrence

- _Range start date/time_: The first date of the series. Empty: the day the Task runs
- _Range end date/time_: The last date of the series. Used only when _Range start date/time_ is set. Empty: the series has no end
- _Type_: Empty for a single event, or "Daily", "Weekly", "Monthly" or "Yearly". The controls next to it change with the type:
  - "Daily": _Every_ with a number of days, from "1" to "5", or _Every workday_, Monday to Friday
  - "Weekly": _Interval_ every "1" to "5" weeks, and the days of the week
  - "Monthly": _Interval_ every "1" to "5" months, and either _Day_ with the day of the month, or _Every_ with the week, "First" to "Last", and the day of the week
  - "Yearly": _Interval_ every "1" to "5" years, _Month_, and either _Day_ with the day of the month, or _Every_ with the week and the day of the week

### Output and errors

The output is "Success:" followed by the ID of the new event.

:::warning

If Microsoft 365 rejects the request, or a calendar cannot be read, the error is written to standard error, and the Task reports success.

:::
