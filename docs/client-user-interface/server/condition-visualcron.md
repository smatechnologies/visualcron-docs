---
sidebar_label: 'Condition - VisualCron'
hide_title: 'true'
---

## Condition - VisualCron

The _VisualCron_ condition checks the result or the state of a Job or Task on this Server: its exit code, its stored output, or whether it is running. Use it, for example, to run a Task only when the Task before it succeeded, or to skip a Job while another Job is still running.

This page describes the **_VisualCron_** tab of the _Add/Edit condition_ window. For the **_Main settings_** tab of the window (_Condition type_, _Description_, _Active_), see [Conditions - Conditions](conditions-conditions).

_Server_ -> _Global objects_ -> _Conditions_ -> _Add_ -> **_Conditions_** tab -> _Add_ -> _Condition type_ "VisualCron" -> **_VisualCron_** tab

![Add/Edit condition window with the VisualCron tab open. Auto (previous task or job) is selected and no Job or Task is selected. In the Match group, Task Exit code is selected with "Is not" and "0"; Job Exit code, Job Is running and Task Output are also shown](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Conditions/Condition%20-%20VC.png)

### Condition check object

Choose which Job or Task the condition checks:

- _Auto (previous task or job)_: the Task that ran before the current one, or the Job that started this Job, as described below
- _Specific_: the Job you select in _Job name_ and, for the Task checks, the Task you select in _Task name_

_Job name_ and _Task name_ are enabled only when _Specific_ is selected. _Task name_ lists the Tasks of the selected Job and stays disabled for the Job checks. With _Specific_ you can check a Job or Task in any Job on this Server. If the selected Job or Task no longer exists, the condition returns a Match Error.

#### What Auto checks

On a Task's Condition Set:

- The Task checks refer to the Task that last finished in the current run, before this Task started
- When the Job has _Run Tasks in order_ checked, that is normally the Task above the current one. A Task that did not run, for example because its own Condition Set skipped it, does not count: the checks then use the last Task that ran before it
- When _Run Tasks in order_ is cleared, Tasks can run at the same time, so the previous Task is whichever Task finished last
- The Job checks refer to the current Job. That Job is running, so _Is running_ is always "True" and _Exit code_ is always "0". Use _Specific_ to check another Job

On a Job's Condition Set:

- The Job checks refer to the Job that started this Job, for example the Job that a VisualCron Trigger watches (see [Event Trigger - VisualCron](event-trigger-visualcron))
- The Task checks always return a Match Error

A Task's Condition Set is evaluated whether _Run Tasks in order_ is checked or cleared. Only the meaning of "previous Task" changes.

:::warning

An _Auto_ condition returns a Match Error when there is no previous Task or Job, and the Condition Set then takes its _On Match Error_ action. With the default _On Match Error_ action, "Exit", the Job stops. This happens for:

- A Task check (_Exit code_, _Output_, _Output (stderr)_ or _Is running_ under _Task_) in a Job's Condition Set, every time
- The first Task of a run, including a run that starts from a selected Task, and every later Task when all the Tasks before it in the run were skipped
- Every Task that starts before any other Task of the run has finished, when _Run Tasks in order_ is cleared
- A Job's Condition Set when no Job started the Job, for example when a time Trigger or a Condition Set's "Run Job" action starts it

Do not assign a set with an _Auto_ condition to the first Task of a Job, or to a Task whose earlier Tasks can all be skipped, and set _On Match Error_ to the action you want. See [Conditions - Actions](conditions-actions).

:::

### Match

Select one check. The checks under _Job_ apply to the Job, and those under _Task_ apply to the Task. Each check uses the Job or Task chosen under _Condition check object_. A new condition starts with Task _Exit code_, "Is not" and "0".

#### Job: Exit code

Compares the Job's exit code from its latest run with the number you enter, using "Is" or "Is not".

- When a Task in that run failed, the Job's exit code is the exit code of the Task that failed most recently. Whether a Task counts as failed depends on that Task's exit code settings. Only the last result of each Task counts, so a Task that fails and then succeeds in the same run, for example when it is retried, is not counted as failed
- When no Task failed, it is the exit code of the first Task that succeeded, normally "0"
- A run that ends by its timeout gets "77777", whatever its Tasks returned, when _Consider timeout as error_ is checked on the **_TimeOut_** tab of the Job. See [Job - Timeout](job-timeout). Any other run that is stopped, including a timeout without that setting, gets "77777" when its exit code would otherwise be "0"

The exit code is set to "0" when a run starts and is updated only when the run ends, so it reads "0" while the Job is running.

#### Job: Is running

Select "True" to match while the Job is running, or "False" to match while it is not.

#### Task: Exit code

Compares the exit code of the Task's latest run with the number you enter, using "Is" or "Is not". A Task that succeeds normally returns "0".

#### Task: Output and Output (stderr)

_Output_ compares the standard output that VisualCron stored for the Task. _Output (stderr)_ compares the stored error output. Enter the text in the box to the right, and select a match type:

- "Is": the whole stored output equals the text
- "Is not": the whole stored output differs from the text
- "Contains": the stored output contains the text
- "Not contains": the stored output does not contain the text, or no output is stored

The comparison is case-sensitive. "Is" and "Is not" compare the entire output, including line breaks at the end. You can use Variables in the text, see [Global - Variables](global-variables). They are replaced with the values of the Job and Task that the condition checks (with _Specific_, the selected Job and Task), not with those of the Job that uses the Condition Set.

With _Specific_, select a _Task name_ for _Output (stderr)_ as well. The window lets you save this check without a Task, and the condition then returns a Match Error.

#### Task: Is running

Select "True" to match while the Task is running, or "False" to match while it is not.

### Example: run a Task only when the previous Task succeeded

1. Add a Condition Set, and on its **_Main settings_** tab enter a _Description_, for example "Previous Task succeeded".
2. On the **_Conditions_** tab, add a condition with _Condition type_ "VisualCron".
3. On the **_VisualCron_** tab, keep _Auto (previous task or job)_, keep _Exit code_ under _Task_ selected, and change "Is not" to "Is", with "0".
4. On the **_Actions_** tab, keep _On Match All_ at "Continue", and keep _On Match None_ at "Exit" to stop the Job, or change it to "Next" to skip only this Task.
5. Set _On Match Error_ to the action you want when the check cannot be made.
6. Assign the set to the second Task or a later one, in a Job that has _Run Tasks in order_ checked, on the **_Conditions_** tab of the Task window. See [Task - Conditions](task-conditions). If the Task before it can be skipped by its own Condition Set, the check uses the last Task that ran instead.
7. On the **_Flow_** tab of the Task before it, look at the _On error_ entry. If it is set to _Stop Job_, the Job stops when that Task fails, the set is never checked, and step 4 has no effect. To let the set decide, set that entry to _Continue to next Task in order_. See [Task - Flow](task-flow).

New Tasks get the Flow entries defined in [Settings - Default Flows](settings-default-flows).
