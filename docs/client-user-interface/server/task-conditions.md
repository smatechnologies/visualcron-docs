---
sidebar_label: 'Task - Conditions'
hide_title: 'true'
---

## Task - Conditions

Condition Sets are global. A Task uses one Condition Set or none, chosen on the ***Conditions*** tab of the Task window. For how to choose the set, see [Choose the Condition Set for a Job or Task](global-conditions#choose-the-condition-set-for-a-job-or-task). The conditions and the actions of a set are described on [Conditions - Conditions](conditions-conditions) and [Conditions - Actions](conditions-actions).

When attached to a Task, a Condition Set is evaluated before the Task runs. The action set for each result (*On Match All*, *On Match Any*, *On Match None*, *On Match Error*) determines whether the Task runs ("Continue"), is skipped ("Next"), is checked again after a wait ("Retry"), is skipped with no further Tasks started ("Exit"), or gives way to another Job or Task ("Run Job", "Run Task"). See [Conditions - Actions](conditions-actions) for each action and how it applies to a Task.

:::note

Task conditions are checked before each Task starts in a Job run, whether or not the Job has *Run Tasks in order* selected. They are applied on every Job run, including a manual *Run Job*, whichever command you use.

When you run a single Task with *Run Task*, the Task's own Condition Set is not checked, but the Job's Condition Set is applied: if the Job's set ends the Job, the Task does not run. A Task that the "Run Task" action of another Task's Condition Set starts also runs without its own set being checked. See [Job - Conditions](job-conditions#manual-runs).

:::
