---
sidebar_label: 'Global - Conditions'
hide_title: 'true'
---

## Global - Conditions

A Condition Set is a group of checks, called conditions, that the Server runs at the start of a Job run, before its first Task, or just before a Task starts. The combined result of the checks selects an action: run the Job or Task, skip it, check again after a wait, stop, or start another Job or Task. Use a Condition Set when a Job or Task should run only if something is true at that moment, for example when a file exists, a process is running or a Variable has a certain value.

Condition Sets are global objects. You create a set once and can use it in any number of Jobs and Tasks. Each Job and each Task uses one Condition Set or none.

This page describes the _Manage Conditions_ window, where you create and maintain Condition Sets, and explains when the Server evaluates a set. These pages describe the parts of a set and how to use it:

- [Conditions - Main Settings](global-main-settings): the name of the set and its _Extended debug logging_ option
- [Conditions - Conditions](conditions-conditions): the conditions in the set and how their results combine
- [Conditions - Actions](conditions-actions): the action for each result
- [Job - Conditions](job-conditions) and [Task - Conditions](task-conditions): how a Job or a Task uses a set

:::note

Condition Sets are separate from the _Job Condition_ and _Task Condition_ of a Flow entry on the **_Flow_** tab of a Job or Task. Those decide whether that Flow entry's action runs. See [Job - Flow](job-flow) and [Task - Flow](task-flow).

:::

### Set up a Condition Set

1. Go to _Server_ -> _Global objects_ -> _Conditions_, and click _Add_ on the _Condition set_ toolbar.
2. On the **_Main settings_** tab, enter a _Description_ that says what the set checks. See [Conditions - Main Settings](global-main-settings).
3. On the **_Conditions_** tab, add one condition for each check. See [Conditions - Conditions](conditions-conditions).
4. On the **_Actions_** tab, choose the action for each result. With one active condition, the result is always _On Match All_, _On Match None_ or _On Match Error_. _On Match Any_ needs at least two active conditions. See [Conditions - Actions](conditions-actions).
5. Click _OK_.
6. Open the Job or Task, and on its **_Conditions_** tab check _Use_ for the set. Make sure that no other _Use_ box is checked, and save the Job or Task.
7. To see how the set behaves, check _Extended debug logging_ on the set's **_Main settings_** tab, and run the Job with _Run Job_ -> _With Conditions_ -> _From first Task_. This is a real run: if the set lets the Job continue, its Tasks run. A Variable condition writes its result to the log only when the Server-wide _Extended debug logging_ is checked, see [Condition - Variable](condition-variable).

### Manage Conditions window

_Server_ -> _Global objects_ -> _Conditions_

![The Global objects group of the Server ribbon with Conditions highlighted, and the Manage Conditions window it opens. In the window, Add is highlighted on the Condition set toolbar, and a Condition Set named Example 1 is expanded to show one condition](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Conditions/Global%20-%20Conditions.png)

The list shows each Condition Set as a row with its _Description_. Expand a set to see its conditions. Each condition is shown with the icon of its condition type and its _Description_.

The toolbar is in two parts:

- _Condition set_ toolbar: _Add_, _Edit_, _Clone_ and _Delete_ for Condition Sets, a filter box and _Clear filter_
- _Conditions_ toolbar: _Add_, _Edit_, _Clone_ and _Delete_ for the conditions of the selected set, _Audit log_, a filter box and _Clear filter_

Type in a filter box to show only the sets, or only the conditions, whose _Description_ contains that text. _Clear filter_ empties the filter box next to it.

_Add_, _Edit_ and _Clone_ on the _Condition set_ toolbar open the _Add/Update condition set_ window. _Add_ on the _Conditions_ toolbar adds a condition to the selected Condition Set, and _Edit_, _Clone_ and _Delete_ there work on the selected condition. A condition that you add, edit or delete in this window is saved on the Server as soon as you click _OK_ in the _Add/Edit condition_ window, or confirm the deletion.

_Audit log_ opens the audit log for Condition Sets. See [Objects - Audit Log](../tools/objects-audit-log).

Right-click a row to open the shortcut menu. It has the toolbar commands (_Add Condition set_, _Edit Condition set_, _Clone Condition set_, _Delete Condition set_, _Add Condition_, _Edit Condition_, _Clone Condition_, _Delete Condition_ and _Audit log_), and also:

- _Versions.._: earlier versions of the selected Condition Set, see [Versions](../tools/audit-log-versions)
- _Object relations_: the objects that use the selected Condition Set, see [Objects - Object Relations](../tools/object-relations)
- _Export ..._: exports the selected Condition Sets, see [Import/Export - Export Settings](../file/export-settings)

:::warning

When you delete a Condition Set with _Delete_ or _Delete Condition set_ and the set is in use, the confirmation says how many objects use it. Deleting the set does not remove it from those Jobs and Tasks. Open _Object relations_ before you delete a set, and choose another set for those Jobs and Tasks first. For what happens to a Job or Task whose set is gone, see [Errors and missing Condition Sets](conditions-actions#errors-and-missing-condition-sets).

:::

### Add/Update condition set window

The _Add/Update condition set_ window has three tabs:

- **_Main settings_**: the name of the set and the _Extended debug logging_ option, see [Conditions - Main Settings](global-main-settings)
- **_Conditions_**: the conditions in the set, see [Conditions - Conditions](conditions-conditions)
- **_Actions_**: the action for each result, and an optional wait before it, see [Conditions - Actions](conditions-actions)

Click _OK_ to save the Condition Set.

### Choose the Condition Set for a Job or Task

The **_Conditions_** tab of the Job window and of the Task window shows the same list and toolbars as the _Manage Conditions_ window, with an extra _Use_ column. Check _Use_ for the Condition Set that the Job or Task should use. Checking a box clears the box that was checked before. Clicking a checked box clears it, and the Job or Task then has no Condition Set. The _Use_ choice is saved when you save the Job or Task.

When a Condition Set is added while the window is open, its _Use_ box is checked, and the box that was checked before stays checked. This happens for a set that you add or clone on this tab, and for a set that someone adds from another Client. The Job or Task then saves both sets, and the Server uses only one of them, which need not be the new one. Before you save the Job or Task, make sure that only one _Use_ box is checked.

Changes to a Condition Set or its conditions that you make on this tab are saved on the Server at once. _Cancel_ in the Job or Task window does not undo them, and they apply to every Job and Task that uses the set. To change a set for one Job or Task only, clone it, change the copy, check _Use_ for the copy and clear the box of the original.

### When the Server evaluates a Condition Set

- Job: at the start of each Job run, before its first Task and before its _On start_ Flow entries. Whether the action is applied depends on how the Job was started, see [Job - Conditions](job-conditions#when-the-jobs-condition-set-is-checked)
- Task: each time the Task is about to start in a Job run, whether or not the Job has _Run Tasks in order_ checked, and again each time a Flow entry retries the Task. The Task's set is not checked when you run the Task on its own with _Run Task_, or when the "Run Task" action of another Task's Condition Set starts it. See [Task - Conditions](task-conditions)

The Server checks the active conditions in the set and combines their results into one of four results, _On Match All_, _On Match Any_, _On Match None_ or _On Match Error_ (see [Conditions - Conditions](conditions-conditions)). It then applies the action set for that result on the **_Actions_** tab (see [Conditions - Actions](conditions-actions)).

:::warning

When a Condition Set ends a Job before any Task has run, the run is recorded as successful. The Job's _On success_ and _On complete_ Flow entries and the VisualCron Event Triggers that watch this Job's completion can still start other Jobs. See [When a Condition Set ends the Job](job-conditions#when-a-condition-set-ends-the-job).

:::
