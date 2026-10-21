---
sidebar_label: 'Time Triggers'
hide_title: 'true'
---

## Time Triggers

For Time trigger select one of _Interval_ or _Custom_ types.
 
**Job > Triggers > Add > Time trigger > Interval/Custom**

**Settings tab**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Interval%20Time%20Trigger%20Settings.png)

The Settings tab contains the **Main settings** group with the following fields:

**Description**

Enter a description that distinguishes the Trigger from others in the trigger list.

**Auto description**

When checked, the _Description_ field is generated automatically from the Trigger type and its current settings. Enabled by default.

**Auto refresh description**

When checked, the auto‑generated description is refreshed whenever the Trigger settings change, even if the _Description_ field already contains text. Only effective when _Auto description_ is checked.

**Time trigger type**

A pair of mutually exclusive radio buttons that select which type of time schedule is applied:

* **Interval time trigger** — use the schedule configured on the [Interval Time Trigger](interval-time-trigger) tab (default)
* **Custom time trigger** — use the schedule configured on the [Custom Time Trigger](custom-time-trigger) tab

Only the selected type is used. Switching between them does not discard the settings on the other tab, so a schedule can be built on both tabs and swapped between while testing.

**Choosing between Interval and Custom**

Both types use the same underlying scheduling engine, and the Interval type is a simplified front end to it.

* Use **Interval** for a schedule that repeats on one unit, such as every 15 minutes, every other hour, weekdays only, or the last working day of the month
* Use **Custom** when different time units need different rules at the same time, for example "every 30 minutes, but only between 08:00 and 18:00, and only Monday to Friday". That combination cannot be expressed with a single interval

:::note

A Time Trigger fires on the Server's clock, not the clock of the machine running the Client. The _Next run_ value shown at the bottom of the Job window is always calculated using Server time.

:::
 
**Interval tab**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Interval%20Time%20Trigger.png)

This time trigger is a simplified Custom time trigger. Different Interval options are available.
 
**Custom tab**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Custom%20Time%20Trigger.png)

The Custom time trigger also allows setting of time details when a Job should be triggered.
 
**Expire tab**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Time%20Trigger%20Expire.png)

The expiration date/time for the time trigger may be set. Also the handling (Deactivate/Delete trigger) of the expired trigger is selected.
