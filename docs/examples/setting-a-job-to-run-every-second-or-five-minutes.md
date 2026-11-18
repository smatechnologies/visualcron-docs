---
sidebar_label: 'Setting a Job to Run Every Second Minute or Five Minutes'
hide_title: 'true'
---

## Setting a Job to Run Every Second Minute or Five Minutes

To run a Job every second minute or every five minutes, add a Time Trigger to the Job. An Interval Time Trigger is the simplest way. A Custom Time Trigger gives the same result by listing the minutes.

### Use an Interval Time Trigger

1. In the ***Add Job*** or ***Edit Job*** window, click the ***Triggers*** tab.
2. Click ***Add*** -> ***Time Trigger*** -> ***Interval***.
3. Click the ***Interval*** tab.
4. In _Interval_, select "Minutely".
5. In _Every_, enter "2" for every second minute, or "5" for every five minutes.
6. In _Server Start time_, set the date and time the schedule starts from.
7. Click ***Ok***.

:::note

The schedule is counted from _Server Start time_. To run at minutes 0, 5, 10 and so on, set a start time on a whole multiple of five minutes, for example 08:00. See [Interval Time Triggers](../client-user-interface/server/interval-time-trigger).

:::

### Use a Custom Time Trigger

1. In the ***Add Job*** or ***Edit Job*** window, click the ***Triggers*** tab.
2. Click ***Add*** -> ***Time Trigger*** -> ***Custom***.
3. Click the ***Custom*** tab.
4. Click the ***Minute*** tab.
5. Select _Choose minute(s)_.
6. Check the minutes to run on: 0, 2, 4 and so on up to 58 for every second minute, or 0, 5, 10 and so on up to 55 for every five minutes.
7. Click the ***Hour*** tab, and check that _Every hour_ is selected.
8. Click ***Ok***.

All time units of a Custom Time Trigger must match for the Job to run, so _Every hour_ is needed to run in every hour. See [Custom Time Triggers](../client-user-interface/server/custom-time-trigger) and [Job Triggers](../client-user-interface/server/job-triggers).
