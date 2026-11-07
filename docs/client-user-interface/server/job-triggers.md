---
sidebar_label: 'Job Triggers'
hide_title: 'true'
---

## Job Triggers

A Trigger starts a Job. A Job can have one or more Triggers. A [Time Trigger](time-triggers) starts the Job on a schedule, for example every minute. An [Event Trigger](event-triggers) starts it when something happens, for example when a file is created.

By default, each Trigger starts the Job on its own: Triggers do not wait for each other. To make the Job wait until several Triggers have fired, put them in a dependency (see [How a Trigger Dependency works](#how-a-trigger-dependency-works)).

The Triggers are on the ***Triggers*** tab of the Job window, which opens when you add, clone or edit a Job.

**Job -> Triggers** tab

![Add Job window with the Triggers tab outlined in red, while the window still shows the Tasks tab with its toolbar and an empty Task list](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Task%20Main%20Settings/Triggers.png)

### Toolbar

The toolbar above the Trigger list has the following commands. The shortcut menu that opens when you right-click the list has the same commands, plus _Versions.._.

* _Add_: opens a menu with _Time Trigger_ (_Interval_ or _Custom_) and _Event Trigger_ (one entry per Event Trigger type). On the toolbar, Event Trigger types that your license does not include, or that are hidden on the ***Features*** tab of the [Client settings](../file/client-settings), are not listed.
* _Edit_: opens the selected Trigger for editing. Double-clicking a row does the same.
* _Delete_: removes the selected Trigger from the Job, without asking for confirmation. Pressing the Delete key in the list does the same. If the Trigger was in a dependency, it is removed from that dependency, and a dependency left with fewer than two Triggers is removed. Before you delete a Trigger that is in a dependency, see [Deleting a Trigger in a dependency](#deleting-a-trigger-in-a-dependency).
* _Clone_: opens a copy of the selected Trigger as a new Trigger. Click _Ok_ in the Trigger window to add it. The copy is not in any dependency.
* _Dependencies.._: opens the _Trigger dependency_ window for the selected Trigger (see [Dependencies](#dependencies)).
* _Audit log_: opens the [Audit log](../tools/objects-audit-log) for the Triggers of this Job.
* _Versions.._ (shortcut menu only): opens the [Versions](../tools/audit-log-versions) window for the selected Trigger.

On the toolbar, _Edit_, _Delete_, _Clone_ and _Dependencies.._ are available when a Trigger is selected.

Each command needs the matching permission ([User permissions](main-user-permissions)):

* _Add_ and _Clone_ need permission to add Triggers
* _Edit_ needs permission to edit them
* _Delete_ needs permission to delete them
* _Audit log_ and _Versions.._ need permission to read the Audit log

A change you make in the Trigger window takes effect when you click _Ok_ in the Trigger window and then _Ok_ in the Job window. Changes on this tab (_Active_, _Delete_ and dependencies) take effect when you click _Ok_ in the Job window.

### Trigger list

The list contains all Triggers of the current Job, one row per Trigger. Double-clicking a row opens the Trigger for editing, like _Edit_.

The list has six columns. The column headers may be shortened on screen.

**Active**

Checked by default. Shows and controls whether the Trigger is active. An active Trigger waits for its time or event. An inactive Trigger does not start the Job. Clearing it on a Trigger in a dependency takes that Trigger out of the requirement (see [How a Trigger Dependency works](#how-a-trigger-dependency-works)).

**Trigger type**

An icon that shows whether it is a Time Trigger or an Event Trigger.

**Trigger inner type**

An icon that shows the kind of Time or Event Trigger, for example a File Trigger.

**Dependency image**

Blank for a Trigger that is not in a dependency. A Trigger in a dependency shows a tag icon. All dependencies use the same icon. The list is sorted so that the Triggers of each dependency are next to each other.

**Fired times of Trigger in dependency**

How many times the Trigger has fired. Only Triggers in a dependency are counted. The column goes back to 0 when the dependency starts over (see [When a dependency starts over](#when-a-dependency-starts-over)). It also goes back to 0 when the Server is turned on and when the Job is activated in the Job list. A Trigger showing 0 has not fired since then.

**Description**

The name or description of the Trigger.

Below the list:

**Reset Trigger dependency state when saving Job**

Makes every dependency in the Job start over when you save the Job, so that all its Triggers must fire again. Use it after testing a Trigger, or after changing a dependency, so that the next run starts from a known state. The checkbox applies once: it is cleared again the next time you open the Job.

**Next run**

The status bar at the bottom of the Job window shows when the Job runs next, based on its active Time Triggers. It does not take Event Triggers or Trigger dependencies into account, so a Job that waits for a dependency can run later than shown. The status bar of the Time Trigger window shows the next run of that one Trigger. See [Next run](time-triggers#next-run).

### Dependencies

To create or change a dependency, complete the following steps:

1. Select a Trigger in the list.
2. Click _Dependencies.._. The _Trigger dependency_ window opens. If the selected Trigger is already in a dependency, the window shows that dependency. Otherwise it starts a new one.
3. Check every Trigger that belongs in the dependency, including the one you selected.
4. Select a wait type (see [Trigger dependency window](#trigger-dependency-window)).
5. Click _Ok_, then click _Ok_ in the Job window.

The Triggers in the dependency show a tag icon in the _Dependency image_ column.

To remove a dependency, complete the following steps:

1. Select one of its Triggers and click _Dependencies.._.
2. Clear all checkboxes.
3. Click _Ok_, then click _Ok_ in the Job window.

**Job -> Triggers -> Dependencies..**

![Triggers tab of the Add Job window with two Time Triggers in the list, the Reset Trigger dependency state when saving Job checkbox below the list and Dependencies.. outlined in red. In front is the Trigger dependency window opened from it: both Triggers unchecked and Wait infinite time for other Triggers selected, while the wait time fields (1 hours, 0 minutes, 0 seconds) and the checked Use sliding wait option are unavailable](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Task%20Main%20Settings/Trigger%20Dependency.png)

### Trigger dependency window

**Select Triggers that should be evaluated together**

The list shows every Trigger of the Job. Check the Triggers that belong in this dependency.

**Wait type**

Defines how long a Trigger that has fired stays counted while the dependency waits for the other Triggers.

**Wait infinite time for other Triggers**

There is no time limit. A Trigger that has fired stays counted until the dependency is met, however long the other Triggers take. For example, Trigger 1 might fire 1000 times and the Job still does not start, because Trigger 2 has not fired yet.

This is the default.

:::warning

With infinite wait, a Trigger that fired long ago still counts. If a file arrives on Monday and the matching schedule is not met until Friday, the Job still runs on Friday, because the File Trigger's Monday fire still counts. If the VisualCron service restarts or the Server is turned off in between, the Monday fire is forgotten and the File Trigger must fire again (see [When a dependency starts over](#when-a-dependency-starts-over)). Use _Wait specified time for other Triggers_ when the Triggers are only meaningful together inside a limited window.

:::

**Wait specified time for other Triggers**

A Trigger that has fired stays counted for a set period. Enter the period in _hours_, _minutes_ and _seconds_. The default is 1 hour. Minutes and seconds go up to 59, and the period must be at least 1 second.

The wait period starts when the **first** Trigger in the dependency fires, not when the Job is saved or when the Job last ran. If the remaining Triggers have not fired before the period runs out, the count on every Trigger in the dependency is reset to zero and the dependency starts over from nothing.

**Use sliding wait**

With _Wait specified time for other Triggers_, sliding wait makes the wait period start over each time a Trigger that has already been counted fires again, which keeps the dependency alive while its Triggers are still active.

For example, with a wait period of 1 hour, a File Trigger that keeps firing every few minutes holds the dependency open while it waits for the other Trigger, instead of the count being discarded one hour after the first file arrived.

This option is checked by default. It is available only when _Wait specified time for other Triggers_ is selected, and unavailable with _Wait infinite time for other Triggers_, because there is no period to extend.

### How a Trigger Dependency works

Without a dependency, Triggers work as OR: whichever Trigger fires first starts the Job, and every later fire starts it again.

A dependency changes that to AND. Every active Trigger in the dependency must fire before the Job starts. Putting a daily Time Trigger and a File Trigger in the same dependency means "run the Job when the file has arrived **and** the scheduled time has passed", instead of running it twice.

The following rules apply to a dependency:

* **The order does not matter.** The Triggers can fire in any order, and the Job starts as soon as the last outstanding one fires.
* **A Trigger only needs to fire once.** If Trigger 1 fires a thousand times and Trigger 2 has never fired, the Job still does not start. The _Fired times_ column counts every fire, so it can show more than 1.
* **The dependency starts over when it is met.** Once all Triggers have fired, the Job is started and every Trigger in the dependency must fire again before the next run. This happens even if the Job then does not run, for example because it is already running and _Do not start if job is already running_ is checked. For the other cases, see [When a dependency starts over](#when-a-dependency-starts-over).
* **A dependency needs at least two Triggers.** The _Trigger dependency_ window does not accept a single Trigger and shows "You need to select at least 2 Triggers." If you delete a Trigger on this tab, or add it to another dependency, and that leaves a dependency with only one Trigger, the dependency is removed.
* **A Trigger can only belong to one dependency.** Adding a Trigger to a second dependency removes it from the first.
* **A Job can have several dependencies.** Each dependency is evaluated on its own.
* **Triggers that are not in any dependency keep the default OR behavior.** They start the Job on their own, regardless of what the Triggers inside a dependency are waiting for.
* **Inactive Triggers are ignored.** Clearing _Active_ on a Trigger takes it out of the requirement. Deactivating a Trigger does not start the Job by itself: the Job starts the next time an active Trigger in the dependency fires, if all other active Triggers have fired. If every Trigger in a dependency is inactive, the dependency never starts the Job.
* **Some runs do not check the dependency.** A run started manually, from a Task, through the API, or by _Run missed Job once at start_ (see [Main settings](job-main-settings)) starts the Job at once. The Triggers that have already fired stay counted.

### When a dependency starts over

A dependency remembers which of its Triggers have fired only while the VisualCron service runs. It starts over, so that every Trigger in it must fire again, when:

* the dependency is met and the Job is started
* a _Wait specified time for other Triggers_ period runs out (for an exception, see [Deleting a Trigger in a dependency](#deleting-a-trigger-in-a-dependency))
* the Job is saved with _Reset Trigger dependency state when saving Job_ checked
* the VisualCron service restarts
* the Server is turned off (Server status "Off", while the VisualCron service keeps running)
* the Job is deactivated in the Job list (see [Activate/Deactivate Job](../server-group-job-task-area/job-list/activate-deactivate-job)), or deactivates itself when a run starts because _Run once (can be reactivated later)_ is checked
* the Job is deleted

This applies with _Wait infinite time for other Triggers_ too. Clearing _Activate (when added)_ in the Job window deactivates the Job but does not make its dependencies start over.

:::warning

If you change a dependency while it is waiting (a Trigger in it shows _Fired times_ above 0), the change does not apply until the dependency starts over. Until then:

* a Trigger you added to the dependency is not needed, so the Job can start before that Trigger fires
* a Trigger you removed is still needed. If it had not fired yet, the Job does not start until the wait period runs out or, with _Wait infinite time for other Triggers_, until the dependency starts over for another reason
* a wait period that has already started keeps its current end time

To apply the change at once, check _Reset Trigger dependency state when saving Job_ below the Trigger list before you click _Ok_ in the Job window.

:::

### Deleting a Trigger in a dependency

:::warning

Take care when you delete a Trigger that belongs to a dependency using _Wait specified time for other Triggers_ while that dependency is waiting (a Trigger in it shows _Fired times_ above 0). If the wait period then runs out before the dependency is met, the Server cannot end it. This can last until the VisualCron service restarts. Meanwhile:

* no wait period on the Server runs out, so every dependency with _Wait specified time for other Triggers_ keeps its fired Triggers counted as if it had _Wait infinite time for other Triggers_
* the Server stops some of its regular background work, such as saving its own changes to Jobs every minute

:::

To delete such a Trigger safely, use one of the following:

* If at least two Triggers stay in the dependency after the delete, check _Reset Trigger dependency state when saving Job_ before you click _Ok_ in the Job window.
* Otherwise, first deactivate the Job in the Job list (see [Activate/Deactivate Job](../server-group-job-task-area/job-list/activate-deactivate-job)). Then open the Job, delete the Trigger, click _Ok_ in the Job window, and activate the Job again.

Removing the Trigger from the dependency before you delete it does not prevent this on its own.

If it has already happened, restart the VisualCron service.

### Example

A Job should import a file, but only once the file has arrived and only after 6 AM. Add two Triggers and put both in a dependency:

* A Time Trigger set to fire daily at 6 AM
* A File Trigger set to fire when the file is created in the import folder

With _Wait specified time for other Triggers_ set to 4 hours:

1. The file arrives at 5:15 AM. The File Trigger fires, its _Fired times_ becomes 1, and the 4 hour wait period starts. The Job does not run, because the Time Trigger has not fired.
2. At 6 AM the Time Trigger fires. Both Triggers in the dependency have now fired, so the Job starts.
3. Both Triggers reset to zero. The Job does not run again until a new file arrives and it is 6 AM again.

If instead the file never arrives, the Time Trigger fires at 6 AM on its own and the Job waits. At 10 AM the 4 hour period runs out, the Time Trigger's count is reset to zero, and the dependency starts over.

If the file arrives after 10 AM, the 6 AM fire no longer counts, so the Job does not start. The file's fire counts for 4 hours and runs out before 6 AM the next day. The Job then starts only if a new file arrives between 2 AM and 10 AM: a file that arrives up to 4 hours before 6 AM still counts when the Time Trigger fires. If the file can arrive late, use a longer period or _Wait infinite time for other Triggers_.

### Why a Job with a dependency did not run

If a Job with a dependency is not starting when expected, check the following:

* The _Fired times_ column shows which Triggers are still outstanding. A Trigger showing 0 has not fired since the column was last set back to 0.
* The dependency may have started over after the first Trigger fired, for example because the VisualCron service restarted or the Server was turned off. See [When a dependency starts over](#when-a-dependency-starts-over).
* The dependency may have been changed while it was waiting. See the warning under [When a dependency starts over](#when-a-dependency-starts-over).
* A Trigger in the dependency may be inactive, or may not be firing at all. Test it on its own by temporarily removing it from the dependency.
* With _Wait specified time for other Triggers_, the period may run out before the slower Trigger fires. Increase the period, or check _Use sliding wait_.

To start from a known state, save the Job with _Reset Trigger dependency state when saving Job_ checked.

If the Job ran although not every Trigger had fired, check whether it was started without the dependency. This happens when a Trigger that is not in the dependency fired, or when the run was started manually, from a Task, through the API or by _Run missed Job once at start_. A Job can also run with a Trigger fire that is older than the wait period, if wait periods no longer run out on the Server (see [Deleting a Trigger in a dependency](#deleting-a-trigger-in-a-dependency)).
