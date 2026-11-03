---
sidebar_label: 'Conditions - Main Settings'
hide_title: 'true'
---

## Conditions - Main Settings

The **_Main settings_** tab is the first tab of the _Add/Update condition set_ window. Use it to name a Condition Set and to choose whether the Server logs each evaluation of the set in detail. The detailed log helps when a Job or Task that uses the set runs, skips or stops in a way you do not expect.

To open the window, go to _Server_ -> _Global objects_ -> _Conditions_. In the [Manage Conditions](../server/global-conditions) window, do one of the following:

- Click _Add_ on the _Condition set_ toolbar to create a Condition Set
- Select a Condition Set and click _Edit_, or double-click the Condition Set row
- Select a Condition Set and click _Clone_ to create a copy of it

The same commands are on the shortcut menu that opens when you right-click a Condition Set row. The **_Conditions_** tab of the Job window and of the Task window shows the same Condition Set list with the same commands.

The window has three tabs:

- **_Main settings_**: the name of the set and its logging option, described on this page
- **_Conditions_**: the checks that make up the set, see [Conditions - Conditions](../server/conditions-conditions)
- **_Actions_**: what happens for each result, see [Conditions - Actions](../server/conditions-actions)

Click _OK_ to save the Condition Set, or _Cancel_ to close the window without saving.

When you edit an existing Condition Set, the window shows a _Copy Condition set Id_ link at the bottom. Click it to copy the Id of the set to the clipboard, for example to refer to the set in a support case. Right-click it to give the set a new Id:

1. Enter the new Id, which must be a GUID. The Client shows how many objects refer to the set. If another Condition Set already uses that Id, the Client says so and asks for a different value.
2. Click _Yes_ to change the Id, _No_ to see the list of those objects first (the Client then asks again), or _Cancel_ to keep the current Id.

When you click _Yes_, the Server saves the new Id right away and updates the Jobs, Tasks and notifications that refer to the set. Clicking _Cancel_ in the _Add/Update condition set_ window does not undo the change. References outside this Server, for example scripts or API calls that use the old Id, are not updated.

_Server_ -> _Global objects_ -> _Conditions_ -> _Add_ -> **_Main settings_** tab

![Add/Update condition set window with the Main settings tab open, showing an empty Description box and a cleared Extended debug logging checkbox](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Conditions/Main%20Settings.png)

### Description

The name of the Condition Set. It is shown in the Condition Set list of the _Manage Conditions_ window, and in the Condition Set list on the **_Conditions_** tab of the Job and Task windows, where you assign the set. The Client accepts an empty _Description_, but give every set a unique name that says what it checks. A cloned set starts with the same _Description_ as the original, so change it to tell the two apart.

### Extended debug logging

Unchecked by default. When you check it, the Server writes _Debug_ entries to the Server log each time it evaluates this Condition Set for a Job or Task:

- The Condition Set being run, with the name of the Job or Task
- The result of each condition it checks, shown as "Match", "NoMatch" or "MatchError". Some entries show "No Match" instead of "NoMatch", so search for both
- The overall result of the set, shown as "MatchAll", "MatchAny", "MatchNone" or "MatchError" (the _On Match All_, _On Match Any_, _On Match None_ and _On Match Error_ results on the **_Actions_** tab), and the action that follows
- The Job or Task that a _Run Job_ or _Run Task_ action starts

Where the entries appear:

- On the **_Realtime - general_** tab of the [Log](../server/information-log) window (_Server_ -> _Information_ -> _Log_). If the _Debug_ filter in that window's _Filter_ menu is active, Debug entries are hidden; click _Debug_ in the _Filter_ menu to show them
- In the Server log file, when _Server events_ is checked under _Log to file_ in the [log settings](../server/settings-log-settings)
- In the Windows Event Log, when _Log to event log_ is checked in the log settings

They are not written to the log database.

This option applies to this Condition Set only. It is separate from the Server-wide _Extended debug logging_ option in the log settings, which most conditions do not need. The exception is a Variable condition: it writes its result to the log only when the Server-wide option is checked, whatever this option is set to. See [Condition - Variable](../server/condition-variable).

When a Job is run without its conditions, for example with _With Conditions_ cleared in [Run Job with options](../server-group-job-task-area/job-list/run-job-with-options), the Server still evaluates the Job's Condition Set and logs it, but does not apply its action. The log then shows "Skipping Condition check because the Job was run manually."

:::tip

A set with a _Retry_ action is evaluated, and logged, on every retry, so a short wait can fill the log quickly. Uncheck _Extended debug logging_ when you have finished troubleshooting.

:::

:::warning

The _Run Task_ action is set on the **_Actions_** tab, see [Conditions - Actions](../server/conditions-actions). If the Condition Set of a Task uses _Run Task_ with a Task that is not part of the current Job, neither the Task that owns the Condition Set nor the selected Task runs, and the Job does not continue with its remaining Tasks. The log records why only when _Extended debug logging_ is checked on that Condition Set. If a Job ends early after a condition and the log shows no reason, check _Extended debug logging_ and run the Job again.

:::
