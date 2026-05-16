---
sidebar_label: 'Custom Time Triggers'
hide_title: 'true'
---

## Custom Time Triggers

**Time Trigger -> Custom** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Custom%20Time%20Trigger.png)

The _Year, Month, Day, Hour, Minute_ and _Second_ time parameters may be defined. Each time unit is configured on its own sub‑tab within the Custom tab.

For each time unit, _Every_, _Between_ or _Choose_ can be selected:

* **Every** – the Job is eligible to run on every value of the time unit
* **Between** – specifies a range of values for the time unit, defined by a _From_ and _To_ value joined by _And_
* **Choose** – pick one or more individual values from a list

The _Between ..._ option specifies a range of values for the specific time unit. For example, Between weekdays "Friday" and "Tuesday" means that the Job will run on "Friday", "Saturday", "Sunday", "Monday" and "Tuesday".

**Day sub‑tab**

The Day sub‑tab offers additional options for weekday selection. In addition to choosing days of the month (1–31), you can:

* **Choose weekdays** – pick one or more specific weekdays (Monday through Sunday)
* **Between weekdays** – specify a range of weekdays using a _From_ and _To_ weekday
 
**Examples**

* Choosing for example day "31" results in that the Job will only execute on months with 31 days
* By default, Second = "0" is checked. In order to be able to set a correct time on a Job, a Job must have a least one second specified. Second "0" is the first second in a minute.
* Exemptions remain valid up to the top of the hour. For example, an exemption is considered active through 4:59. A time‑based exemption applies when the current time falls between 2 and 4 minutes past the hour.

**Next run**

The _Next run_ value is displayed in the status bar at the bottom of the Custom Time Trigger window and is refreshed automatically. Next run is based on the values you enter in time settings using the time on the server. Note that next run is an indicative value, that is if you are about to add or edit a Job and you set that Job to run every minute it won't run every minute until you have finished the add/edit window and the Job has appeared in the Job list.

The _Next run_ display can show the following states:

* A calculated date and time – the next scheduled execution that matches the current settings
* **Never** – the configured settings do not produce a future execution
* **Server off** – the server is unavailable and the next run cannot be calculated

**Manual next run calculation**

You can preview how the current settings would behave at a specific point in time without waiting for the server clock to reach it:

* Enable the _Manual_ option to switch from server time to a user‑specified date and time
* Use the date and time pickers to choose the moment from which the next run should be evaluated
* Click _Calculate next_ to recalculate the next run based on the manual values

When _Manual_ is disabled, the next run is recalculated automatically based on the current server time.

:::note

Calculation of next run does not take any time exceptions into account.

:::
