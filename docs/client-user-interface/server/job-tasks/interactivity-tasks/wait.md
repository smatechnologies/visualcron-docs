---
sidebar_label: 'Task Interactivity - Wait'
hide_title: 'true'
---

## Task Interactivity - Wait

The Wait Task pauses the Job for a set time. The next Task starts when the wait ends.

![Wait tab with fields for days, hours, minutes, seconds and milliseconds](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Interactivity%20Tasks/Wait.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Wait tab

Enter the length of the wait in one or more of the fields in the _Wait/Sleep_ group. The Task adds them up, so values larger than the unit allow, such as "90" minutes, are accepted. Each field is "0" by default and accepts a [Variable](../../global-variables) that resolves to a number.

- _days_
- _hours_
- _minutes_
- _seconds_
- _milliseconds_

The wait counts from the start of the Task. If the ***TimeOut*** tab sets a shorter time, the Task times out before the wait ends.

### Output and errors

- If a field is empty, or holds a value that is not a number, the Task fails
