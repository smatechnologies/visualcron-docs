---
sidebar_label: 'Interval Time Triggers'
hide_title: 'true'
---

## Interval Time Triggers

Use an Interval Time Trigger for a schedule that repeats from a start time, such as every 15 minutes, every 3 days or the second Tuesday of the month. You set it on the ***Interval*** tab of the Time Trigger window, which is available when _Interval time trigger_ is selected on the ***Settings*** tab. For how it differs from a Custom Time Trigger, see [Choosing between Interval and Custom](time-triggers#choosing-between-interval-and-custom).

![Time Trigger window, Interval tab: Interval set to Daily, Every set to 1 Day(s), and a Start time date and time at the bottom. The status bar shows Next run.](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Interval%20Time%20Trigger.png)

**Interval**

A list that sets how the schedule repeats. The options are _Daily_ (default), _Hourly_, _Minutely_, _Secondly_, _Specific days of the month_ and _Specific days of the week_.

**Every**

The number of units between runs. The minimum is "1" and the default is "1". The unit shown to the right of the box follows the _Interval_ setting:

* _Daily_: _Day(s)_
* _Hourly_: _Hour(s)_
* _Minutely_: _Minute(s)_
* _Secondly_: _Second(s)_
* _Specific days of the month_: _Month(s)_
* _Specific days of the week_: _Week(s)_

For example, _Interval_ = _Hourly_ with _Every_ = "2" runs the Job every other hour.

For _Specific days of the month_, the months are counted from the month of the start time: "3" runs on the chosen days in the start month and then every third month.

:::warning

With the _Day(s)_ option and _Every_ set to "2" or more, a run on a checked day that is the last day of its month moves the count: the next run is in the following month, and the count continues from there. For example, with _Every_ = "3" and days "15" and "30" checked, the runs on 15 and 30 April 2026 are followed by runs on Friday 15 May 2026 and Saturday 30 May 2026, then in August, instead of on Wednesday 15 July 2026.

To run on fixed months, such as January, April, July and October, use a [Custom Time Trigger](custom-time-trigger). Choose the months on the ***Month*** sub-tab, and set the day, hour and minute as in the [worked examples](custom-time-trigger#worked-examples).

:::

For _Specific days of the week_, weeks run from Monday to Sunday and are counted from the week of the start time: "2" with only Monday checked runs every other Monday.

:::warning

With _Every_ set to "2" or more:

* After the first run, the Job runs only on the first checked day of the week, counted from Monday. For example, with Monday and Wednesday checked, _Every_ = "2" and a start time of Monday 2 November 2026 09:00, the Job runs on 2, 16 and 30 November 2026, but not on Wednesday 4 or 18 November.
* If the start time has passed when you click _Ok_, checked days later in the current week can be skipped. For example, with only Friday checked and a start time of Wednesday 28 October 2026 09:00 that has passed, the first run is Friday 13 November 2026, not Friday 30 October 2026.

To run on several days every N weeks, add one Trigger for each day. In each Trigger, check only that day and set the start time to the date and time of its first run, in the future.

:::

**Specific days of the month**

When _Specific days of the month_ is selected, a panel of four options appears. Select one of them. No option is selected at first, and _Next run_ shows "Never" until you select one and complete it (see [Next run](time-triggers#next-run)).

* _Day(s)_: check one or more days, 1 to 31, in the list. The list is available only while this option is selected. A day that does not exist in a month, such as day 31 in April, is skipped in that month.
* _Last day of the month_: run on the last day of every month.
* Numbered weekday (the option with an ordinal list and a weekday list): run on the "1st", "2nd", "3rd", "4th" or "Last" chosen weekday of the month, for example the second Tuesday or the last Friday. The defaults are "1st" and "Monday".
* Numbered workday (the option with an ordinal list followed by "workday"): run on a numbered workday of the month. The list starts with "Last", followed by "1st" to "20th", "21th" and "22th".

:::warning

With the numbered weekday option set to "Last", the Job can run twice in one month: a week early and again on the right day. This happens in a month whose last chosen weekday falls on a day that the month of the run before it does not have, for example the 31st after a month of 30 days. For example, a Trigger for the last Friday that runs on Friday 26 November 2027 runs next on Friday 24 December 2027 and then on Friday 31 December 2027. The months after that are calculated correctly until the next such month. With a start time in the past, such a month can also be missed.

To prevent this, after the run before such a month, open the Trigger and set the start date to the first day of that month, keeping the time. Check that _Next run_ shows the last chosen weekday of that month, then click _Ok_ in the Time Trigger window and _Ok_ in the Job window.

:::

The numbered weekday and numbered workday options share one ordinal value, and VisualCron saves the ordinal that was changed last, in either list. After you select the option you want, choose its ordinal in its own list. If that list already shows the value you want, choose another value and then the one you want. Then check that _Next run_ shows the date you expect.

:::warning

Workdays are Monday to Friday, and public holidays are not considered. A Trigger set for the last workday runs on that day even when it is a public holiday. To skip holidays, add a time exception to the Job: the run is then skipped, not moved to another day. See [Job - Time Exceptions](job-time-exceptions).

:::

**Specific days of the week**

When _Specific days of the week_ is selected, a panel labeled _The following days:_ appears, with a checkbox for each day from Monday to Sunday. Check the days on which the Job should run. If no day is checked, _Next run_ shows "Never".

**Server Start time**

The date and time the schedule is counted from, set with a date box and a time box. It defaults to the current Server time at the moment you create the Trigger. For _Daily_ and the _Specific days_ options, the time of day of every run comes from this value. For _Hourly_, _Minutely_ and _Secondly_ schedules, it sets where in the hour or minute the runs fall.

Set the start time before you click _Ok_. If you leave the default, the Job runs at the time of day when you created the Trigger, for example 14:37:12.

:::note

When you reopen a Trigger whose _Next run_ showed "Never" when it was saved, the start date and time can show the current Server time instead of the saved start time, and clicking _Ok_ saves them. Set the date and time again before you click _Ok_, or click _Cancel_ to leave the Trigger unchanged.

:::

The first run is the first time that matches the schedule at or after the start time. If the start time is in the past, the first run is the next matching time after now, except for _Specific days of the week_ with _Every_ set to "2" or more (see the warning under **Every**) and for the "Last" numbered weekday (see the warning under **Specific days of the month**). For example, an _Hourly_ Trigger with _Every_ = "1" and a start time of 08:20 runs at 20 minutes past every hour, not on the hour.

**Examples**

* **Every 15 minutes**: _Interval_ = _Minutely_, _Every_ = "15". A start time of 08:07:00 gives 08:07, 08:22, 08:37 and so on.
* **Every other hour**: _Interval_ = _Hourly_, _Every_ = "2". A start time of 01:00:00 gives 01:00, 03:00, 05:00 and so on.
* **Once a day at 22:00**: _Interval_ = _Daily_, _Every_ = "1", with the start time set to 22:00:00.
* **Weekdays only**: _Interval_ = _Specific days of the week_, _Every_ = "1", with Monday to Friday checked. The time of day comes from the start time.
* **The 1st and 15th of every month**: _Interval_ = _Specific days of the month_, _Day(s)_ option, with "1" and "15" checked.
* **The last day of every month**: _Interval_ = _Specific days of the month_, _Last day of the month_ option. This works for months of any length, including February in a leap year.
* **The second Tuesday of every month**: _Interval_ = _Specific days of the month_, numbered weekday option, with "2nd" and "Tuesday".
* **The last workday of every month**: _Interval_ = _Specific days of the month_, numbered workday option, with "Last". The Job runs on the last Monday-to-Friday day of the month.

:::tip

To combine a repeat with a time window, for example every 30 minutes but only from 08:00 to 17:30 on weekdays, use a [Custom Time Trigger](custom-time-trigger).

:::
