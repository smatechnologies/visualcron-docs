---
sidebar_label: 'Job - Conditions'
hide_title: 'true'
---

## Job - Conditions

Condition sets are global, and a Job can have one condition set attached. The conditions attached to a Job's *Conditions* tab are managed in the same way as global condition sets — see [Global - Conditions](global-conditions) for the field-by-field reference.

When attached to a Job, the condition set is evaluated before the Job runs — that is, before any of its Tasks are started and before the Job's *On Start* notifications and flow actions. The action configured for each match outcome (*On Match All*, *On Match Any*, *On Match None*, *On Match Error*) determines whether the Job continues, exits, re-checks the condition, runs another Job, or runs a single Task:

* *Continue* - continues running the Job
* *Next* - exits the Job
* *Retry* - waits and re-checks the condition
* *Exit* - exits the Job
* *Run Job* - exits the Job and runs another Job
* *Run Task* - exits the Job and runs a single Task

See [Conditions Actions](conditions-actions) for the full list of actions and how they apply to a Job.

:::tip Note

Job conditions are not checked when the Job is started manually; in that case the Job runs regardless of the attached condition set.

:::
