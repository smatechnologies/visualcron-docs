---
sidebar_label: 'Custom Time Triggers'
hide_title: 'true'
---

## Custom Time Triggers

**Time Trigger -> Custom** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Custom%20Time%20Trigger.png)

The _Year, Month, Day, Hour, Minute_ and _Second_ time parameters may be defined.
 
For each time unit, Every, Choose or Between can be selected. The Between ... option specifies a range of values for the specific time unit. For example, Between weekdays "Friday" and "Tuesday" means that the Job will run on "Friday", "Saturday", "Sunday", "Monday" and "Tuesday".
 
**Examples**

* Choosing for example day "31" results in that the Job will only execute on months with 31 days
* By default, Second = "0" is checked. In order to be able to set a correct time on a Job, a Job must have a least one second specified. Second "0" is the first second in a minute.
* Exemptions remain valid up to the top of the hour. For example, an exemption is considered active through 4:59. A time‑based exemption applies when the current time falls between 2 and 4 minutes past the hour.

**Next run**

Next run is calculated every second. Next run is based on the values you enter in time settings using the time on the server. Note that next run is an indicative value, that is if you are about to add or edit a Job and you set that Job to run every minute it won't run every minute until you have finished the add/edit window and the Job has appeared in the Job list.
 
:::note

Calculation of next run does not take any time exceptions into account.

:::