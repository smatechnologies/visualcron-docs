---
sidebar_label: 'Custom Time Triggers'
hide_title: 'true'
---

## Custom Time Triggers

Use a Custom Time Trigger when a schedule is defined by calendar values, for example "every 30 minutes from 08:00 to 17:30, Monday to Friday". You set it on the ***Custom*** tab of the Time Trigger window, which is available when _Custom time trigger_ is selected on the ***Settings*** tab. For how it differs from an Interval Time Trigger, see [Choosing between Interval and Custom](time-triggers#choosing-between-interval-and-custom).

![Time Trigger window, Custom tab, Year sub-tab: Every year selected. The Choose year(s) list of twenty years, all checked, its Deselect all button and the Between years lists joined by "and:" are unavailable. The Interval tab is unavailable and the status bar shows Next run.](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Custom%20Time%20Trigger.png)

The ***Custom*** tab has a sub-tab for each time unit: ***Year***, ***Month***, ***Day***, ***Hour***, ***Minute*** and ***Second***. Most sub-tabs have three options. For example, the ***Year*** sub-tab has _Every year_, _Choose year(s)_ and _Between years_. The ***Day*** sub-tab has five options (see [Day sub-tab](#day-sub-tab)).

* **Every**: the unit places no restriction. This is the default for every unit except Second, which defaults to _Choose second(s)_ with "0" checked, so the Job runs at the start of each matching minute.
* **Choose**: check one or more values in the list. _Deselect all_ under the list clears it. The year list covers the current year and the next 19 years.
* **Between**: choose a first value and a last value in the two lists joined by _and:_. The range includes both values. When the first value is later than the last, the range wraps around: _Between weekday(s)_ "Friday" and "Tuesday" covers Friday, Saturday, Sunday, Monday and Tuesday, and _Between hours_ "22" and "5" covers 22:00 to 05:59. Years are the exception: a reversed year range covers the same years as the range written the other way around.

:::warning

When you switch a unit to a Choose option, its list can already have values checked, for example after you used the Every or Between option. Click _Deselect all_ first, then check only the values you want. Otherwise the unit can still match every value, and the Job can run, for example, every minute instead of once an hour.

:::

Depending on the regional format of the Client computer, the hour lists can show 12-hour values such as "12 AM" and "11 PM" instead of 0 to 23. This happens when the format defines an AM symbol.

### How the time units combine

Every time unit must match for the Job to run. The units are combined, not treated as alternatives, so the schedule is the overlap of all of them.

Because each unit is set separately, one schedule can limit the hour, the minute and the weekday at the same time.

A unit left at _Every_ places no restriction. A Trigger with Minute = _Choose minute(s)_ "0" and every other unit left at its default runs at the start of every hour, on every day, in every month.

### Day sub-tab

The ***Day*** sub-tab has five options in one group, _Day(s) or weekday(s)_: _Every day_, _Choose day(s)_ (1 to 31), _Between days_, _Choose weekday(s)_ (Monday to Sunday) and _Between weekday(s)_. Only one of them can be selected, so one Trigger cannot combine days of the month with weekdays. If you choose day "31", the Job runs only in months that have 31 days. For a schedule such as "the first Monday of the month", use the numbered weekday option of an [Interval Time Trigger](interval-time-trigger).

### Worked examples

Each of these leaves any unit not mentioned at its default (_Every_, and Second = _Choose second(s)_ "0"). Before you check values in a Choose list, click _Deselect all_.

* **At the start of every hour**: Minute = _Choose minute(s)_ "0".
* **Once a day at 23:45**: Hour = _Choose hour(s)_ "23", Minute = _Choose minute(s)_ "45".
* **Every 30 minutes from 08:00 to 17:30 on weekdays**: Hour = _Between hours_ "8" and "17" ("8 AM" and "5 PM" on a 12-hour list), Minute = _Choose minute(s)_ "0" and "30", Day = _Choose weekday(s)_ "Monday", "Tuesday", "Wednesday", "Thursday" and "Friday".
* **Twice an hour, overnight only**: Hour = _Between hours_ "22" and "5", Minute = _Choose minute(s)_ "0" and "30". The range wraps past midnight, so the Job runs from 22:00 to 05:30.
* **06:00 on the first day of each quarter**: Month = _Choose month(s)_ "January", "April", "July" and "October", Day = _Choose day(s)_ "1", Hour = _Choose hour(s)_ "6", Minute = _Choose minute(s)_ "0".

:::note

If you select a Choose option and leave its list empty, VisualCron does not save the Trigger when you click _Ok_. It shows a message such as "You have to select at least one hour!", or for seconds "A job must be executed on a given second, default is 0." Leave second "0" checked unless the Job must run at other seconds within the minute. The year list is the exception: if no year is checked, the Trigger runs every year.

:::

### Next run

The status bar at the bottom of the window shows _Next run_ as a preview of the settings. For what it shows and when the Trigger takes effect, see [Next run](time-triggers#next-run).
