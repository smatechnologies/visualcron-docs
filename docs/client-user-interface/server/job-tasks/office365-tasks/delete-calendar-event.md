---
sidebar_label: 'Task Office365 - Delete Calendar Event'
hide_title: 'true'
---

## Task Office365 - Delete Calendar Event

The Office365 - Delete Calendar event Task lets you delete a Calendar event in the Office365 cloud. The Task uses the [Office365 Connection](../../connection-office365).

**Office365 - Delete calendar event** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Office365%20Tasks/O365%20Delete%20calendar%20events.png)

**Connection**

To use the Office365 Tasks you need to create a [Connection](../../global-connections) first. Click the *Settings* icon to open the *Manage Connections* dialog.

**Calendar name**

The name of the calendar that contains the event. Leave empty to use the default calendar.

**Event subject**

The subject (title) of the calendar event to delete. Required.

**Event instance with date**

When checked, only the single occurrence of a recurring event on the specified date is deleted; the rest of the series is preserved. Enter the date of the occurrence in the field next to the checkbox. When unchecked, the event (and any series it belongs to) is deleted in full.
