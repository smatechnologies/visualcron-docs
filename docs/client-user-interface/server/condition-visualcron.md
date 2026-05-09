---
sidebar_label: 'Condition - VisualCron'
hide_title: 'true'
---

## Condition - VisualCron

The *VisualCron* condition lets you check internal values within VisualCron, such as the exit code, output or running state of a Job or Task.

**Global > Conditions > Condition set Add > Conditions Add > VisualCron select > VisualCron** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Conditions/Condition%20-%20VC.png)

First select the Task or Job you want to check. Conditions on a Task only work when the parent Job has *Run Tasks in order* turned on.

**Auto**

VisualCron checks the previous Task's values. This option is only meaningful for Tasks that have an internal relation within a Job; Jobs are independent of each other.

**Specific**

Use this setting to check a Task or Job from a different Job.

**Match**

The available match types are:

* **Job Exit code** - a successful Job run returns exit code `0`. If any Task in the Job returns a non-zero value, the Job exit code is inherited from the failing Task's exit code.
* **Job Is running** - matches if the selected Job is currently running.
* **Task Exit code** - a successful Task run returns exit code `0`. So, to run the next Task only when the previous Task succeeded, select *Task exit code* / *Is* / `0`. In the condition set, set *MatchAll* to *Continue* and *MatchNone* to *Exit* — when the exit code is `0` the action is *Continue* (the next Task runs); when the exit code is non-zero the action is *Exit* (the Job is terminated).
* **Task Output** - matches against the standard output stored on the Task. Double-click the Task output row in the main window to see the previous output. Three comparison modes are supported: exact match (*Is* or *Is not*) and substring (*Contains*). Enter the desired match value in the text box to the right.
* **Task Is running** - matches if the selected Task is currently running.
