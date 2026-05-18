---
sidebar_label: 'Interval Time Triggers'
hide_title: 'true'
---

## Interval Time Triggers

**Set Time Trigger > Interval** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Interval%20Time%20Trigger.png)

**Interval**

A dropdown that controls the time unit the Trigger uses. The following options are available:

* **Daily**
* **Hourly**
* **Minutely**
* **Secondly**
* **Specific days of the month**
* **Specific days of the week**
 
**Every**

A numeric editor (minimum `1`) that controls how many of the selected _Interval_ units must pass between fires. The unit suffix to the right of the field updates automatically (for example, `day(s)`, `hour(s)`, `minute(s)`). For example, _Interval = Hourly, Every = 2_ runs the Job every other hour.

**Specific days of the month**

When _Specific days of the month_ is selected, a panel appears with the following options for choosing which day(s) the Trigger fires on. Pick one of the radio modes:

* **Day(s)** — pick one or more specific calendar days from a checkbox list of 1 through 31
* **Last day of month** — fire on the last day of every month
* **First / Last (ordinal) day** — fire on the _1st_, _2nd_, _3rd_, ... or _Last_ day of the month, chosen via the ordinal dropdown
* **First / Last (ordinal) workday** — fire on the _1st_, _2nd_, _3rd_, ... or _Last_ workday of the month. A country dropdown becomes available so that the workday calculation can exclude that country's public holidays

**Specific days of the week**

When _Specific days of the week_ is selected, a panel with seven checkboxes appears (one for each weekday from Monday through Sunday). Tick the days on which the Trigger should fire.

**Server Start time**

The date and time of the first run occurrence on the Server. The field is split into a date picker and a separate time picker. The Trigger schedule is calculated relative to this start time.
