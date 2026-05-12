---
sidebar_label: 'Task - Conditions'
hide_title: 'true'
---

## Task - Conditions

Condition sets are global. The conditions attached to a Task's *Conditions* tab are managed in the same way as global condition sets — see [Global - Conditions](global-conditions) for the field-by-field reference.

When attached to a Task, a condition set is evaluated before the Task runs. The action configured for each match outcome (*On Match All*, *On Match Any*, *On Match None*, *On Match Error*) determines whether the Task continues, runs the next Task, retries the check, or exits the Job. See [Conditions Actions](conditions-actions) for the full list of actions and how they apply to a Task.

:::tip Note

Task conditions are only checked on Jobs that have *Run Tasks in order* turned on.

:::
