---
sidebar_label: 'Task Office365 - Get Calendar Events'
hide_title: 'true'
---

## Task Office365 - Get Calendar Events

The Office365 - Get calendar event(s) Task writes information about the calendars of a Microsoft 365 user, and their events, to the Task output, using an [Office365 Connection](../../connection-office365). The fields work as filters: a field left empty is not used.

![Office365 - Get calendar event(s) tab with the Connection and Event parameters pattern groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office365%20Tasks/O365%20Get%20calendar%20events.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks). This Task also has its own ***Output*** tab.

### Office365 - Get calendar event(s) tab

#### Connection

- _Connection_: The [Office365 Connection](../../connection-office365) to use. The Task works on the calendars of the Microsoft 365 user the Connection signs in as. Click the _Settings_ icon to open _Manage Connections_

#### Event parameters pattern

Text fields take a value or a pattern: `*` matches any characters, `?` one character, `#` one digit, and `[` starts a character list.

- _Calendar name pattern_: The calendars to read; not case-sensitive
- _Event start date/time from_: Only events that start at or after this time
- _Event start date/time to_: Only events that start at or before this time
- _Is all day_: Selected for all-day events only, cleared for other events only, indeterminate for both
- _Event subject pattern_: Only events whose subject matches
- _Event location pattern_: Only events whose location name matches
- _Event body pattern_: Only events whose body preview, the start of the body text, matches
- _Reminder minutes pattern_: Only events whose reminder time, in minutes, matches
- _Importance_: "None" for any importance, or "Low", "Normal" or "High"
- _Response requested_: Selected or cleared to filter on whether responses are requested; indeterminate for both

[Variables](../../global-variables) are resolved in the text and date fields. For a recurring event, the Task lists its occurrences within the start dates set, or around the series dates when none are set.

### Output tab

- _Show information_: The values to write. Calendar values: "Id", "Name", "Color", "CanShare", "CanViewPrivateItems", "CanEdit" and "Owner"; "Events" adds the events of each calendar, with the event values "EventId", "EventSubject", "EventStartDate", "EventEndDate", "EventBody", "EventLocation", "EventImportance", "EventAttendee", "EventRecurrence" and "IsAllDay". The calendar values and "Events" are selected by default
- _Include field names_: Puts the name of each value in front of it
- _Field separator_, _Text qualifier_ and _Line break_: The characters used between and around the values

### Output and errors

:::warning

If Microsoft 365 rejects the request, or a calendar cannot be read, the error is written to standard error, and the Task reports success.

:::
