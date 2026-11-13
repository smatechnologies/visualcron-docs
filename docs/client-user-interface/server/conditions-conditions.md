---
sidebar_label: 'Conditions - Conditions'
hide_title: 'true'
---

## Conditions - Conditions

The **_Conditions_** tab of the _Add/Update condition set_ window lists the conditions in a Condition Set. Each condition is one check, for example whether a file exists or whether a Variable has a certain value. When a Job or Task uses the set, the Server checks every active condition and combines the results into one result. That result selects the action on the **_Actions_** tab.

To open the tab, go to _Server_ -> _Global objects_ -> _Conditions_. In the [Manage Conditions](global-conditions) window, click _Add_ or _Edit_ on the _Condition set_ toolbar, then click the **_Conditions_** tab. The other tabs are described on [Conditions - Main Settings](global-main-settings) and [Conditions - Actions](conditions-actions).

_Server_ -> _Global objects_ -> _Conditions_ -> _Add_ -> **_Conditions_** tab -> _Add_

![The Conditions tab of the Add/Update condition set window with Add highlighted, and the Add/Edit condition window it opens. The Condition type list is open and shows VisualCron, File, Folder, Process, Service, Variable and .NET](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Conditions/Adding%20Conditions.png)

### Manage the conditions

The toolbar above the list has _Add_, _Edit_, _Clone_ and _Delete_. The same commands are on the shortcut menu when you right-click the list. Double-click a condition to edit it.

- _Add_: opens the _Add/Edit condition_ window for a new condition
- _Edit_: opens the selected condition
- _Clone_: opens a copy of the selected condition, which is saved as a new condition
- _Delete_: removes the selected condition from the list without asking for confirmation

The changes on this tab are saved on the Server when you click _OK_ in the _Add/Update condition set_ window. You can also add, edit and delete conditions directly in the _Manage Conditions_ window, where each change is saved at once.

### Add/Edit condition window

Each condition opens in the _Add/Edit condition_ window. Its **_Main settings_** tab has these settings:

- _Condition type_: the kind of check. A new condition starts as "VisualCron". The window shows a second tab with the settings of the chosen type
- _Description_: the name of the condition, shown in the condition list
- _Active_: checked for a new condition. Clear it to keep the condition in the set without checking it. The Server skips inactive conditions when it evaluates the set. A set with no active condition always returns _On Match Error_, see [How the results combine](#how-the-results-combine)

Click _OK_ to keep the condition. The window first checks the required settings of the chosen type, for example that _File path_ is filled in for a File condition.

### Condition types

- [VisualCron](condition-visualcron): the exit code, output or running state of a Job or Task
- [File](condition-file): whether a file exists, or what it contains
- [Folder](condition-folder): whether a folder exists
- [Process](condition-process): whether a process is running
- [Service](condition-service): whether a Windows service, on the Server computer or a remote computer, has a certain status
- [Variable](condition-variable): a comparison of two values, for example a Variable and a fixed value
- [.NET](condition-dot-net): your own .NET code, which returns the result

### How the results combine

Each active condition returns a Match, a No match or a Match Error. The Server combines them into one result:

- _On Match All_: every active condition returned a Match
- _On Match Any_: at least one active condition returned a Match and at least one returned a No match
- _On Match None_: every active condition returned a No match
- _On Match Error_: at least one condition returned a Match Error, whatever the others returned, or the set has no active condition

The results do not overlap. When every condition returns a Match, only the _On Match All_ action applies, not the _On Match Any_ action. To act the same way whenever at least one condition matches, set the same action for both results on the **_Actions_** tab. With one active condition, the result is always _On Match All_, _On Match None_ or _On Match Error_.

A condition returns a Match Error when it cannot be checked. Some examples:

- the Job or Task that a VisualCron condition refers to no longer exists
- the Credential chosen for a File or Folder condition cannot log on
- a .NET condition fails or does not return True or False

:::warning

A Condition Set with no conditions, or with every condition inactive, always returns _On Match Error_. The default action for that result is "Exit". A Job that uses the set then exits on every run that applies its Condition Set, and a Task that uses the set is skipped and the Job starts no further Tasks (see [When the Job's Condition Set is checked](job-conditions#when-the-jobs-condition-set-is-checked) for runs that do not apply the Job's set). Clearing _Active_ on every condition does not switch a set off. To stop using a set, clear its _Use_ box on the **_Conditions_** tab of the Job or Task.

:::
