---
sidebar_label: 'Task Office365 - Update Calendar Event'
hide_title: 'true'
---

## Task Office365 - Update Calendar Event

The Office365 - Update calendar event(s) Task changes events in the calendars of a Microsoft 365 user, using an [Office365 Connection](../../connection-office365).

![Office365 - Update calendar event(s) tab with the Selected calendar event, Event parameters and Recurrence groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office365%20Tasks/O365%20Update%20calendar%20events.png)

:::warning

_Calendar name_ and _Event subject_ are patterns, and the Task acts on every event that matches. With _Calendar name_ empty, the Task searches every calendar the user can edit. An _Event subject_ of `*` matches every event it finds. Check the values with the [Get calendar event(s)](get-calendar-events) Task first.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Office365 - Update calendar event(s) tab

#### Connection

- _Connection_: The [Office365 Connection](../../connection-office365) to use. The Task works on the calendars of the Microsoft 365 user the Connection signs in as. Click the _Settings_ icon to open _Manage Connections_

#### Selected calendar event

The event or events to change:

- _Calendar name_: The name of the calendar, or a pattern: `*` matches any characters, `?` one character, `#` one digit, and `[` starts a character list. The match is not case-sensitive. Empty: every calendar the user can edit. A matching calendar the user cannot edit is skipped
- _Event subject_: The subject of the event, or a pattern with the same characters as _Calendar name_. A subject that contains `#` or `[` is read as a pattern and can match other events. A `[` with no closing `]` stops the Task with an error, possibly after some events were already processed. The match is not case-sensitive. Required
- _Event instance with date_: When selected, only the occurrence of a recurring event on the date entered in the field next to it is changed; the rest of the series stays. When cleared, a recurring event is changed for the whole series

The Task checks only the first page of calendars, and the first page of events in each calendar, that Microsoft 365 returns, so a matching event that is not on those pages is not found.

#### Event parameters

The new values. A field left empty keeps the event's current value.

- _Event start date/time_: The new start, in the Server computer's time zone
- _Event end date/time_: The new end, in the Server computer's time zone
- _Is all day_: Selected makes the event an all-day event on the day the Task runs, and the start and end values are not used; cleared makes it a timed event; the indeterminate state leaves it unchanged
- _Event subject_: The new subject
- _Event location_: The new location name. Text after a `;` is read as the location's e-mail address and address
- _Reminder minutes_: The new reminder time, in minutes. A value that is not a whole number is ignored
- _Importance_: "Low", "Normal" or "High". With none selected, the importance is unchanged
- _Event body_: The new text, sent as plain text
- _Response requested_: Selected or cleared sets whether responses are requested; the indeterminate state leaves it unchanged

[Variables](../../global-variables) are resolved in the text and date fields.

#### Recurrence

Applies to single events and whole series, not to a single occurrence.

:::warning

With _Type_ empty, a recurring event that is updated as a whole series loses its recurrence and becomes a single event. To keep a series, set _Type_ and the range again, or select _Event instance with date_ to change one occurrence.

:::

- _Range start date/time_: The first date of the series. Empty: the day the Task runs
- _Range end date/time_: The last date of the series. Used only when _Range start date/time_ is set. Empty: the series has no end
- _Type_: "Daily", "Weekly", "Monthly" or "Yearly". The controls next to it change with the type:
  - "Daily": _Every_ with a number of days, from "1" to "5", or _Every workday_, Monday to Friday
  - "Weekly": _Interval_ every "1" to "5" weeks, and the days of the week
  - "Monthly": _Interval_ every "1" to "5" months, and either _Day_ with the day of the month, or _Every_ with the week, "First" to "Last", and the day of the week
  - "Yearly": _Interval_ every "1" to "5" years, _Month_, and either _Day_ with the day of the month, or _Every_ with the week and the day of the week

### Output and errors

The output has a line for each updated event.

:::warning

If Microsoft 365 rejects the request, or a calendar cannot be read, the error is written to standard error, and the Task reports success.

:::
