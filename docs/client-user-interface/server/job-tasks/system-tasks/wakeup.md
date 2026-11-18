---
sidebar_label: 'Task System - Wakeup'
hide_title: 'true'
---

## Task System - Wakeup

The Wake up Task sets a time at which the VisualCron Server computer wakes up from standby or hibernation.

![Wake up Task settings, with the Wake up check box and the three wake-up options](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Wake%20up.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Wake up tab

- _Wake up_ (_Wake up_ group): makes the options below available. The Task sets the wake-up time whether or not this check box is selected
- _At a certain date and time_: wakes the computer at the date and time entered. Selected by default
- _At a certain time_: wakes the computer at the time entered, on the day the Task runs. A time that has already passed that day does not set a wake-up for the next day
- _After a certain time (hour,minute,second)_: meant to wake the computer after the hours, minutes and seconds entered

:::warning

_After a certain time (hour,minute,second)_ does not use the hours, minutes and seconds entered: the computer is set to wake within a minute, and the Task reports success. Use _At a certain date and time_ or _At a certain time_ instead.

:::

On success, the output is "Wake up set success". The Task does not put the computer into standby or hibernation; use the [Standby](standby) or [Hibernate](hibernate) Task for that.

:::info Note

**Remark on Wake Up**

Some computers can wake up from standby and not from hibernation, some work for both, and some for none. It all depends on the BIOS and the APM/ACPI capabilities, your motherboard, and your ATX power supply version.

:::
