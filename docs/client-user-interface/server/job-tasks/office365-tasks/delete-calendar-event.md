---
sidebar_label: 'Task Office365 - Delete Calendar Event'
hide_title: 'true'
---

## Task Office365 - Delete Calendar Event

The Office365 - Delete calendar event(s) Task deletes events from the calendars of a Microsoft 365 user, using an [Office365 Connection](../../connection-office365).

![Office365 - Delete calendar event(s) tab with the Connection and Calendar event groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office365%20Tasks/O365%20Delete%20calendar%20events.png)

:::warning

_Calendar name_ and _Event subject_ are patterns, and the Task acts on every event that matches. With _Calendar name_ empty, the Task searches every calendar the user can edit. An _Event subject_ of `*` matches every event it finds. Check the values with the [Get calendar event(s)](get-calendar-events) Task first.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Office365 - Delete calendar event(s) tab

#### Connection

- _Connection_: The [Office365 Connection](../../connection-office365) to use. The Task works on the calendars of the Microsoft 365 user the Connection signs in as. Click the _Settings_ icon to open _Manage Connections_

#### Calendar event

- _Calendar name_: The name of the calendar, or a pattern: `*` matches any characters, `?` one character, `#` one digit, and `[` starts a character list. The match is not case-sensitive. Empty: every calendar the user can edit. A matching calendar the user cannot edit is skipped
- _Event subject_: The subject of the event, or a pattern with the same characters as _Calendar name_. A subject that contains `#` or `[` is read as a pattern and can match other events. A `[` with no closing `]` stops the Task with an error, possibly after some events were already processed. The match is not case-sensitive. Required
- _Event instance with date_: When selected, only the occurrence of a recurring event on the date entered in the field next to it is deleted; the rest of the series stays. An event that does not recur is deleted whole. When cleared, a recurring event is deleted with its whole series

[Variables](../../global-variables) are resolved in the text and date fields. The Task checks only the first page of calendars, and the first page of events in each calendar, that Microsoft 365 returns, so a matching event that is not on those pages is not found.

### Output and errors

The output has a line for each deleted event and for each matching calendar that cannot be edited, then "Success".

:::warning

The Task does not wait for the result of each delete request: the output reports an event as deleted even if Microsoft 365 rejects the request. Other errors are written to standard error, and the Task reports success.

:::
