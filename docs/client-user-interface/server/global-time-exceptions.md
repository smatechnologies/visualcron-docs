---
sidebar_label: 'Global - Time Exceptions'
hide_title: 'true'
---

## Global - Time Exceptions

A time exception is a period when a Job must not be started by its Triggers, for example a public holiday. Time exceptions are grouped in collections. For example, a collection named "USA - holidays" can hold one exception for each US public holiday. A Job that runs every day and uses that collection skips those days.

This page covers the _Time exceptions_ window, collections, exceptions, and how to import, export and download collections. To choose the collections a Job uses, see [Job - Time Exceptions](job-time-exceptions).

To open the window, click _Server_ -> _Global objects_ -> _Time exceptions_. You can also add and edit collections and exceptions on the ***Time exceptions*** tab of the Job window.

### How a time exception works

- When a Time Trigger fires inside an exception, the Job does not run. The run is skipped, not postponed. The same applies to an Event Trigger that reacts to an event as it happens, for example a File Trigger that watches a folder
- An Event Trigger that polls does not poll during an exception. Examples are the Remote File, Cloud File, SQL, Mail and RSS Triggers, and a File Trigger with _Use polling (Samba compatible)_ checked. When the exception ends, the next poll still finds the files, rows or messages that arrived during the exception, and the Job can run for them then
- When the Server runs missed Jobs, it skips a missed run that falls inside an exception
- Runs started manually, by a _Run Job_ action in a Flow, by a Job/Task control Task, or by _Trigger on existing files_ on a File, Cloud File or SharePoint File Trigger are not blocked. A Job started by a VisualCron Event Trigger on another Job's event, for example when that Job completes, is a Trigger run and is blocked
- Each check that falls inside an exception raises the VisualCron event _Job missed_: each skipped Time Trigger or Event Trigger run, each poll that a polling Trigger skips, each missed run that the Server skips, and each _Trigger on existing files_ run, although that run is not blocked. A Job with a [VisualCron Event Trigger](event-trigger-visualcron) on _Job missed_ runs each time, so it can run many times during one exception
- When _Extended Job debug logging_ is checked on the Job, the Server logs each skipped run with the names of the exception and the collection, see [Job - Main Settings](job-main-settings). A missed run that the Server skips is always logged, without those names
- The Job's _Next run_ does not skip excepted times. It shows the next Trigger time even if that time is inside an exception. After a run is skipped, VisualCron calculates the next one
- If a collection that a Job uses is deleted, it no longer blocks that Job, and the Server logs an error each time it checks that Job. Before you delete a collection, use _Object relations_ to find the Jobs that use it, and remove it from their ***Time exceptions*** tab

:::warning

Do not add the collections of the Jobs you watch to a Job that runs on _Job missed_, and check _Ignore current Job_ on its VisualCron Event Trigger. If that Job is blocked by the same exception and its Trigger reacts to its own _Job missed_ events, the events can repeat without end.

:::

:::warning

A change to a collection changes every Job that uses it. Before you edit or delete a collection, right-click it and click _Object relations_ to see which Jobs use it.

:::

### Time exceptions window

![Time exceptions window opened from the Time exceptions button in the Global objects ribbon group, with the Collections and Exceptions toolbar and menu bar, and the collection USA - holidays expanded to show exceptions with past dates, each with Next exception Never](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Time%20Exceptions/Time%20Exceptions.png)

The grid lists the collections with a checkbox, _Name_ and _Description_. Expand a collection to see its exceptions with _Name_, _Description_ and _Next exception_. _Next exception_ is the next time the exception is in effect, or "Never" if it will not be in effect again. It is updated every minute.

The checkbox beside a collection selects it. In this window it only marks the collections for _Collections_ -> _Export selected_: checking a collection here does not make any Job use it. On a Job's ***Time exceptions*** tab, the checkbox sets which collections the Job uses, and checked collections are listed first.

The toolbar has two groups and two more commands:

- _Collections:_ _Add_, _Edit_, _Clone_ and _Delete_
- _Exceptions:_ _Add_, _Edit_ and _Delete_. Select an exception to edit or delete it
- _Download_: download holiday collections published by VisualCron, see [Download collections](#download-collections)
- _Audit log_: open the [Audit log](../tools/objects-audit-log) for time exceptions

The menu bar has the same _Collections_ and _Exceptions_ commands, but not _Download_ or _Audit log_. It also has:

- _Collections_ -> _Select all_ and _Deselect all_: check or clear every collection
- _Collections_ -> _Import_: import collections from a file, see [Import collections](#import-collections)
- _Collections_ -> _Export selected_: save the checked collections to an XML file, see [Export collections](#export-collections)

The menu bar is only in this window, not on a Job's ***Time exceptions*** tab.

Right-click a row for these commands:

- _Add collection_, _Edit collection_, _Clone collection_ and _Delete collection_
- _Add exception_, _Edit exception_ and _Delete exception_
- _Audit log_: the Audit log for all time exceptions
- _Versions_: the [version history](../tools/audit-log-versions) of the collection
- _Object relations_: the Jobs that use the collection, see [Object relations](../tools/object-relations)
- _Export ..._: export the collection with [Export settings](../file/export-settings)
- _Send to connection ..._ and _Send to server connection ..._: send a copy of the collection to another VisualCron Server

_Versions_ and _Object relations_ always apply to the collection, even when an exception is selected.

Double-click a row to edit it. Press Delete to delete the selected collection or exception.

### Add or edit a collection

The _Add/Edit collection_ window has _Name_ and _Description_. After you add a collection, select it and add its exceptions.

When you edit a collection, the window shows the link _Copy Time Exception collection id_. Click it to copy the collection's Id to the clipboard. Right-click it to change the Id: enter the new Id, which must be a GUID. If another collection already uses that Id, VisualCron asks for a different value. VisualCron shows how many objects refer to the collection. Click _Yes_ to change the Id and update the Jobs that use it, _No_ to see the list of objects first, or _Cancel_. The new Id is saved on the Server as soon as you click _Yes_; clicking _Cancel_ in the _Add/Edit collection_ window does not undo it. Scripts or API calls that use the old Id are not updated.

:::warning

After you change the Id of a collection, the Jobs that use it can stop being blocked by it until the VisualCron service restarts, and the Server logs an error each time it checks those Jobs. Do not change the Id of a collection that Jobs use.

:::

### Clone or delete a collection

_Clone_ opens the _Add/Edit collection_ window for a copy of the collection. The window shows only _Name_ and _Description_, but the copy also gets all the exceptions of the original. The copy and its exceptions get new Ids and are saved when you click _OK_. The copy has the same name as the original, so change the name to tell them apart. Jobs that use the original keep using the original.

When you delete a collection that Jobs use, VisualCron tells you how many objects use it.

### Add or edit a time exception

Select a collection and click _Add_ in the _Exceptions:_ group. The _Time exception_ window has a ***Main settings*** tab with _Name_ and _Description_, and six time tabs:

- ***Year***: _Every year_, _Choose year(s)_ or _Between years_. The lists cover the current year and the next 19 years
- ***Month***: _Every month_, _Choose month(s)_ or _Between months_
- ***Day***: _Every day_, _Choose day(s)_, _Between days_, _Choose weekday(s)_ or _Between weekday(s)_
- ***Hour***: _Every hour_, _Choose hour(s)_ or _Between hours_
- ***Minutes***: _Every minute_, _Choose minute(s)_ or _Between minutes_
- ***Second***: _Every second_, _Choose second(s)_ or _Between seconds_

The exception is in effect at every moment that matches all six time tabs, ***Year*** to ***Second***. The status bar shows _Next exception_ and updates it while you change the settings.

For example, to skip runs all day on 4 July every year: on ***Year***, select _Every year_. On ***Month***, select _Choose month(s)_ and check July. On ***Day***, select _Choose day(s)_ and check 4. Leave ***Hour***, ***Minutes*** and ***Second*** at _Every_.

:::warning

A new exception starts with _Every_ on every tab, and a _Choose_ option with nothing checked also counts as _Every_. An exception that you save without narrowing any tab blocks every Job that uses the collection at all times. Check that _Next exception_ in the status bar shows the date you expect before you click _Ok_.

:::

:::warning

An exception whose chosen years (_Choose year(s)_) have all passed shows "Never" and blocks nothing. Those years are not in the year list, so if you open the exception and click _Ok_, it applies to every year. Click _Cancel_ to leave it unchanged, or choose the years it should apply to before you click _Ok_. To retire an exception, delete it.

:::

### Import collections

Click _Collections_ -> _Import_ in the _Time exceptions_ window and choose an XML or CSV file.

The XML file must be one saved with _Collections_ -> _Export selected_, on this or another Server. Collections are matched by Id: a collection with the same name but a different Id is added as a second collection. If a collection in the file is already on the Server, VisualCron asks what to do:

- _Replace_: replace the collection with the one in the file. Exceptions that are not in the file are removed
- _Skip_: keep the collection on the Server
- _Replace all_: replace this and every following collection without asking

The question does not show which collection it is about. To decide per collection, import files that hold one collection each.

A CSV file has one line per exception, with five fields separated by commas: collection name, collection description, exception name, exception description and date:

`<collection name>,<collection description>,<exception name>,<exception description>,<yyyy-MM-dd>`

For example: `USA - holidays,US federal holidays,Independence Day 2027,,2027-07-04`

Each line adds an exception for that date only, for the whole day. Collections and exceptions are matched by name, including upper and lower case: a new name adds a collection or an exception, and an existing collection is updated without asking. For an existing collection, the collection description in the file is ignored. A field can be empty, but names and descriptions cannot contain commas. Do not add a header line: a line whose date cannot be read stops the import, and nothing is imported. VisualCron shows no message when the import succeeds; the collections appear in the window.

:::warning

If a line names an exception that already exists, VisualCron changes that exception: it adds the month and day to the ones already chosen, replaces its first chosen year with the year of the line, and sets hours, minutes and seconds to every. The exception can then match other days than you expect. For example, an exception "Holiday" for 2027-12-25 that receives the line `...,Holiday,,2027-07-04` then matches 4 and 25 July and 4 and 25 December 2027. Give each date its own exception name, for example with the year in it.

:::

### Export collections

To move collections to another Server, check them and click _Collections_ -> _Export selected_. VisualCron saves them to an XML file, by default named `timeexceptions<yyyyMMdd>.xml`. On the other Server, import the file with _Collections_ -> _Import_. You can also right-click a collection and click _Send to connection ..._ or _Send to server connection ..._ to send a copy directly.

The shortcut-menu _Export ..._ uses [Export settings](../file/export-settings). Import that file with [Import settings](../file/import-settings), not with _Collections_ -> _Import_.

### Download collections

VisualCron publishes holiday collections for a number of countries. To add one:

1. In the _Time exceptions_ window, click _Download_. The _Time exceptions - download_ window lists the published collections with a flag, the name and the date of the last update.
2. Check _Import_ for each collection you want.
3. Click _Import_. The window closes and the collections appear in the _Time exceptions_ window.

To fetch the list again, click _Reload_. The Client fetches the list from the VisualCron website, so the computer that runs the Client needs internet access.

:::warning

If a downloaded collection is already on the Server, for example because you downloaded it before, _Import_ replaces it without asking. Exceptions you added to it are removed. Jobs that use the collection keep using it.

Keep your own exceptions in a separate collection and let the Job use both.

:::

After a download, check _Next exception_ for each exception. Exceptions for dates that have passed show "Never" and block nothing. If every exception of a collection shows "Never", check _Last Update_ in the download window: if the published collection has a newer update, download it again (this replaces it, see the warning). Otherwise add the dates you need as new exceptions in your own collection. Do not open and save an expired exception, see [Add or edit a time exception](#add-or-edit-a-time-exception).

For reference, the US Office of Personnel Management publishes the [US federal holidays](https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays).

### Where the settings are stored

The Server stores all collections in the file "timeexceptions.xml" in its settings folder. By default this is the "settings" folder under the installation folder, "C:\Program Files (x86)\VisualCron\settings" on 64-bit Windows. You can change the folder under _Settings folder_ on the ***Folders*** tab of the Server settings, see [Settings - Folders](settings-folders).
