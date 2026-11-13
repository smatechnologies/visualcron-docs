---
sidebar_label: 'Time Triggers'
hide_title: 'true'
---

## Time Triggers

A Time Trigger starts a Job on a schedule. This page describes the Time Trigger window. On the ***Settings*** tab you describe the Trigger and choose its type. The ***Interval***, ***Custom*** and ***Expire*** tabs each have their own page.

To open the window, go to the Job's ***Triggers*** tab and click _Add_ -> _Time Trigger_ -> _Interval_ or _Add_ -> _Time Trigger_ -> _Custom_. The _Add_ menu is on the toolbar and on the shortcut menu of the Trigger list (right-click the list). The item you click preselects the Time trigger type.

### Settings tab

![Time Trigger window, Settings tab: the Main settings group with an empty Description box, Auto description and Auto refresh description checked, and Time trigger type set to Interval time trigger. The Custom tab is unavailable and the status bar shows Next run.](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Interval%20Time%20Trigger%20Settings.png)

The ***Settings*** tab contains the _Main settings_ group with the following fields:

**Description**

Enter a description that distinguishes the Trigger from others in the Trigger list. With the default settings, VisualCron replaces what you type here when you click _Ok_. To keep your own text, clear _Auto refresh description_.

**Auto description**

When checked, VisualCron fills _Description_ from the Trigger's settings when you click _Ok_, if _Description_ is empty. Checked by default.

**Auto refresh description**

When checked, VisualCron regenerates the description every time you click _Ok_ and replaces any text in _Description_. Available only when _Auto description_ is checked. Checked by default.

**Time trigger type**

Two options select the type of schedule:

* _Interval time trigger_ (default): use the schedule on the ***Interval*** tab. See [Interval Time Triggers](interval-time-trigger).
* _Custom time trigger_: use the schedule on the ***Custom*** tab. See [Custom Time Triggers](custom-time-trigger).

Only the selected type's tab is available. Selecting _Interval time trigger_ makes the ***Custom*** tab unavailable, and selecting _Custom time trigger_ makes the ***Interval*** tab unavailable. While the window is open, you can switch between the types without losing what you entered on either tab. When you click _Ok_, only the selected type's schedule is used, and it is what you see when you reopen the Trigger. Settings you entered on the other tab are not kept.

### Choosing between Interval and Custom

Interval and Custom are two different ways to describe a schedule. Neither type can express everything the other can.

* An _Interval time trigger_ counts from a start time. It runs every N days, hours, minutes or seconds, on chosen days of the week (every week, or every N weeks for a single day), or on chosen days of the month every N months. The days of the month can include the last day, a numbered weekday (for example, the second Tuesday) and a numbered workday. Use it for "every 3 days", "every 15 minutes" or "the second Tuesday of the month". See [Interval Time Triggers](interval-time-trigger) for the settings that need care.
* A _Custom time trigger_ matches calendar values. The Job runs at every moment whose year, month, day, hour, minute and second all match your choices. Use it to limit a schedule to certain hours or weekdays, for example "every 30 minutes from 08:00 to 17:30, Monday to Friday". An Interval time trigger cannot express that combination.

### Interval tab

![Time Trigger window, Interval tab: Interval set to Daily, Every set to 1 Day(s), and a Start time date and time at the bottom. The Custom tab is unavailable and the status bar shows Next run.](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Interval%20Time%20Trigger.png)

Sets a schedule that is counted from a start time. Available when _Interval time trigger_ is selected. See [Interval Time Triggers](interval-time-trigger).

### Custom tab

![Time Trigger window, Custom tab, Year sub-tab: Every year selected. The Choose year(s) list of twenty years, all checked, its Deselect all button and the Between years lists are unavailable. The Interval tab is unavailable.](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Custom%20Time%20Trigger.png)

Sets a schedule by matching year, month, day, hour, minute and second values. Available when _Custom time trigger_ is selected. See [Custom Time Triggers](custom-time-trigger).

### Expire tab

![Time Trigger window, Expire tab: the Time expiration group with Use trigger expiration cleared, and the Expiration date and time, Deactivate trigger (selected) and Delete trigger unavailable.](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Time%20Trigger%20Expire.png)

Check _Use trigger expiration_ to set an _Expiration_ date and time. Then choose what happens to the Trigger at that moment: _Deactivate trigger_ (default) or _Delete trigger_. Before you turn expiration on, read the warning about the default date on [Time Trigger - Expiration](time-trigger-expiration).

### Next run

The status bar at the bottom of the Time Trigger window shows _Next run_ for this Trigger. It updates automatically as you change the settings and is calculated in Server time. The status bar of the Job window also shows a _Next run_ value: that one is for the Job as a whole, based on its active Time Triggers.

_Next run_ is a preview. The Trigger takes effect after you click _Ok_ in the Time Trigger window and then _Ok_ in the Job window.

_Next run_ can show:

* A date and time: the next run that matches the current settings
* "Never": the settings do not produce a run (a Custom Time Trigger looks no more than 20 years ahead)
* "Server off": the Server is turned off, so it does not run schedules or activate Triggers

### Server time and missed runs

Time Triggers use the Server's local time and time zone. A Trigger has no time zone setting, and the times you enter in the Time Trigger window are Server times.

If the VisualCron service was stopped when a Job was due, the Job runs once when the service starts. This happens only if the Job is active, _Run missed Job once at start_ is checked on the Job's ***Main settings*** tab, and the Server is not turned off. See [Job - Main Settings](job-main-settings). The missed run starts the Job directly: it does not wait for a [Trigger dependency](job-triggers#how-a-trigger-dependency-works).

Time exceptions are applied when a run is due, not in _Next run_. _Next run_ can show a time that falls inside one of the Job's time exceptions, and that run is skipped. A missed run at start that falls inside a time exception is skipped too. See [Job - Time Exceptions](job-time-exceptions).
