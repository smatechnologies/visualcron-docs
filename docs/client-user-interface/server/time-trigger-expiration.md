---
sidebar_label: 'Time Trigger - Expiration'
hide_title: 'true'
---

## Time Trigger - Expiration

Trigger expiration ends a Trigger automatically. A Trigger can expire at a set date and time. Most Event Triggers can instead expire after they have detected their event a set number of times. When the Trigger expires, VisualCron deactivates it or deletes it from the Job. Use expiration for Triggers that are needed only for a limited period.

The settings are on the ***Expire*** tab of the Time Trigger window and on the ***Expires*** tab of the Event Trigger window. The two windows use slightly different labels:

| Setting | Time Trigger (***Expire***) | Event Trigger (***Expires***) |
|---|---|---|
| Turn expiration on | _Use trigger expiration_ | _Expiration enabled_ |
| Expire at a date and time | _Expiration:_ | _Expiration date_ |
| Expire after a number of events | not available | _Expire after being triggered_ `<n>` _time(s)_ |
| Keep the Trigger, inactive | _Deactivate trigger_ | _Inactivate trigger_ |
| Remove the Trigger | _Delete trigger_ | _Delete trigger_ |

**Time Trigger -> Expire** tab

![Expire tab of the Time Trigger window: Use trigger expiration cleared, and the Expiration date and time fields and the Deactivate trigger and Delete trigger options unavailable, with Deactivate trigger selected](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Time%20Triggers/Time%20Trigger%20Expire.png)

**Event Trigger -> Expires** tab

![Expires tab of the Add/Edit event window for a File Trigger: Expiration enabled cleared, and the Expiration date option with its date and time fields, the Expire after being triggered option with a count of 1 time(s), and the Inactivate trigger and Delete trigger options unavailable, with Inactivate trigger selected](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Expires.png)

**Use trigger expiration**

Check _Use trigger expiration_ (Time Trigger) or _Expiration enabled_ (Event Trigger) to turn expiration on. While the checkbox is cleared, the Trigger does not expire, and the date, time and count fields are unavailable. On the Time Trigger window, the action options are unavailable too.

On the Event Trigger window, the mode and action options can stay available after you clear _Expiration enabled_. They have no effect until you check it again.

**Expiration**

The date and time when the Trigger expires: enter the date in the date field and the time in the time field. On the Event Trigger window, select _Expiration date_ first.

The date and time are the VisualCron Server's local time, not the time of the computer that runs the Client.

:::warning

The fields start with the date and time on the Client computer when the Trigger was created, and VisualCron does not check that the value is in the future. If you turn expiration on without changing the date, the Trigger can expire as soon as the Job is saved. The same happens if you enter a moment that has already passed in Server time. With _Delete trigger_, the Trigger is then removed from the Job.

:::

A Trigger expires within a second of its expiration time, even while the Server is turned off (Server status "Off") and whether or not the Job is active. If the VisualCron service is stopped when the expiration time passes, the Trigger expires as soon as the service starts again.

**Expire after being triggered**

Available on the Event Trigger window only (see [Event Triggers](event-triggers)). A Time Trigger always expires at a date and time. The SQL, Remote file, Cloud file, Sharepoint file, Desktop and Webmacro Triggers do not support it: the option is shown, but they never expire after the count. Use an expiration date for them. Select _Expire after being triggered_ and enter the number of times (minimum 1).

The count is the number of events the Trigger detects, not the number of Job runs. With a _Run delay_ on the Event Trigger's ***Main settings*** tab, the Job runs fewer times than the count.

The count is kept only while the Trigger runs unchanged. It starts again from 0 when:

* the Job is saved, for any change
* the Job or the Trigger is activated again
* the Server is turned off and on again, unless the Trigger has _Ignore Server Off (always run)_ checked
* the VisualCron service restarts

A Trigger set to expire after 10 events can therefore detect more than 10 events in total.

**Expiration action**

Choose what happens to the Trigger when it expires:

* _Deactivate trigger_ (Time Trigger) or _Inactivate trigger_ (Event Trigger): the Trigger stays in the Job with _Active_ cleared, so it no longer starts the Job (default)
* _Delete trigger_: the Trigger is removed from the Job

To use a Trigger again after it expired at a date, complete the following steps:

1. Open the Trigger and, on the ***Expire*** or ***Expires*** tab, set a later expiration date or clear the expiration checkbox.
2. Click _Ok_ in the Trigger window.
3. Check _Active_ for the Trigger in the Trigger list.
4. Click _Ok_ in the Job window.

The Trigger is active again. If you only check _Active_, the expiration time has already passed, so the Trigger is deactivated again as soon as the Job is saved. A Trigger that expired after its event count can be activated again directly: its count starts again from 0.

:::warning

With _Delete trigger_, the Trigger and its settings are removed from the Job when it expires. This also happens to a Trigger that has been deactivated in the meantime: a deactivated Trigger is still deleted at its expiration date. Choose _Deactivate trigger_ if you may want to review or reuse the Trigger later. For a Trigger in a dependency that uses _Wait specified time for other Triggers_, choose _Deactivate trigger_ (_Inactivate trigger_ on the Event Trigger window) instead (see [What expiration applies to](#what-expiration-applies-to)).

:::

### What expiration applies to

Expiration acts on the Trigger, not on the Job. The Job itself remains, along with its Tasks and any other Triggers.

A Job whose only Trigger has expired is still present but no longer has anything to start it. It can still be run manually, or by another Job.

Expiration is also independent of a dependency. A deactivated or deleted Trigger no longer counts toward the dependency it was in. If only one active Trigger is left in that dependency, that Trigger starts the Job on its own. See [Job Triggers](job-triggers#how-a-trigger-dependency-works).

:::warning

A Trigger that is deleted at its expiration stays listed in its dependency. If that dependency uses _Wait specified time for other Triggers_, the problem described in [Deleting a Trigger in a dependency](job-triggers#deleting-a-trigger-in-a-dependency) can start when one of its wait periods runs out. With two or more Triggers left in the dependency, it can start again at any later wait period, also after the VisualCron service restarts, until you update the dependency.

:::

To update the dependency, complete the following steps:

1. Open the Job and, on the ***Triggers*** tab, select one of the remaining Triggers in the dependency and click _Dependencies.._.
2. Click _Ok_ without changing the selection.
3. Check _Reset Trigger dependency state when saving Job_ and click _Ok_ in the Job window.

### Examples

* **A Job that should only run during a migration window**: set the expiration to the end of the window and choose _Deactivate trigger_. If the window is extended, set a later expiration date and activate the Trigger again.
* **An Event Trigger that should react to one event only** (not the Trigger types listed under _Expire after being triggered_): select _Expire after being triggered_ with 1 _time(s)_, so the Trigger expires when it detects its first event. Select _Delete trigger_ as well if it should then be removed from the Job.
* **A temporary Trigger added while troubleshooting**: set the expiration to the end of the troubleshooting session, for example later today, with _Delete trigger_. The Trigger then removes itself and cannot be left behind by accident. If the Trigger is in a dependency that uses _Wait specified time for other Triggers_, choose _Deactivate trigger_ (or _Inactivate trigger_) instead (see [What expiration applies to](#what-expiration-applies-to)).
