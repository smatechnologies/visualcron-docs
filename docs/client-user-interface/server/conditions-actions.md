---
sidebar_label: 'Conditions - Actions'
hide_title: 'true'
---

## Conditions - Actions

The **_Actions_** tab of the _Add/Update condition set_ window sets what happens for each result of the Condition Set. When a Job or Task uses the set, the Server checks its conditions and gets one of four results (see [Conditions - Conditions](conditions-conditions)). It then waits, if that result has a wait, and applies that result's action.

_Server_ -> _Global objects_ -> _Conditions_ -> _Add_ -> **_Actions_** tab

![The Actions tab of the Add/Update condition set window with four sections: On Match All, On Match Any, On Match None and On Match Error. Each section shows Don't wait with Hours, Minutes and Seconds at 0, an action (Continue in the first two sections, Exit in the last two), and the No job selected and No task selected lists](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Conditions/Condition%20-%20Actions.png)

### Settings for each result

The tab has one section per result: _On Match All_, _On Match Any_, _On Match None_ and _On Match Error_. Each section has the same settings:

- Wait: the first combo box, with "Don't wait" (the default) or "Wait". With "Wait", enter _Hours_, _Minutes_ and _Seconds_ for the pause before the action is applied
- Action: the second combo box, with "Continue", "Next", "Retry", "Exit", "Run Job" or "Run Task". The defaults are "Continue" for _On Match All_ and _On Match Any_, and "Exit" for _On Match None_ and _On Match Error_
- Job: the Job for "Run Job" and "Run Task". In a Task's Condition Set, choose the Task's own Job for "Run Task" (see [Run Job and Run Task](#run-job-and-run-task)). Type in the filter box next to the list to shorten it
- Task: the Task for "Run Task", chosen from the Tasks of the selected Job

The Job list is available only for "Run Job" and "Run Task", and the Task list only for "Run Task". Choosing "Retry" sets the wait to "Wait". When you click _OK_, the window checks the following:

- every "Wait" is longer than zero
- "Retry" has a wait
- "Run Job" and "Run Task" have a Job
- "Run Task" has a Task

### Actions

An action has a different effect in a Job's Condition Set and in a Task's Condition Set. The table assumes that the Job has _Run Tasks in order_ checked.

| Action | In a Job's Condition Set | In a Task's Condition Set |
|---|---|---|
| "Continue" | The Job runs | The Task runs |
| "Next" | The Job ends without running any Task | The Task is skipped and the Job continues with the next Task |
| "Retry" | The Server checks the set again | The Server checks the set again |
| "Exit" | The Job ends without running any Task | The Task is skipped and the Job runs no further Tasks |
| "Run Job" | The Job ends without running any Task, and the chosen Job starts | The Task is skipped, the Job runs no further Tasks, and the chosen Job starts |
| "Run Task" | The Job ends without running any Task, and the chosen Task starts on its own, after the Condition Set of its Job and its own Condition Set are checked | The chosen Task runs in place of this Task, and the Job continues with the Tasks that follow the chosen Task |

When the Job does not have _Run Tasks in order_ checked, it starts its Tasks one after another without waiting for each one to finish. In a Task's Condition Set:

- "Next" skips only this Task
- "Exit" and "Run Job" start no further Tasks, and Tasks that have already started run to the end
- "Run Task" runs the chosen Task in place of this Task, and the Job then continues with the Task that follows the skipped Task

A Task's Condition Set is checked before each Task starts in a Job run, in both modes. It is not checked for a Task that you run on its own with _Run Task_, or for the Task that the "Run Task" action of another Task's Condition Set starts. A Task that the "Run Task" action of a Job's Condition Set starts has its own Condition Set checked, see [Run Job and Run Task](#run-job-and-run-task). When a Condition Set ends the Job, see [When a Condition Set ends the Job](job-conditions#when-a-condition-set-ends-the-job) for the result and what still runs.

### Run Job and Run Task

- "Run Job" starts the chosen Job with its own Condition Set applied. If the chosen Job no longer exists, nothing is started
- In a Task's Condition Set, "Run Task" runs a Task of the same Job. The chosen Task runs without its own Condition Set being checked
- In a Job's Condition Set, "Run Task" runs the chosen Task on its own, and the Task can be in any Job. Before the Task runs, the Server checks the Condition Set of the Job the Task belongs to, and then the Task's own Condition Set

:::warning

In a Task's Condition Set, "Run Task" must choose a Task of the same Job. If the chosen Task is in another Job, the Server skips the current Task and the Job runs no further Tasks. The Server logs an error for this only when _Extended debug logging_ is checked on the **_Main settings_** tab of the set.

In a Job's Condition Set, a "Run Job" that chooses this same Job, or a "Run Task" that chooses a Task of this Job, starts a run that checks the same Condition Set first. While the set keeps returning the same result, the Server keeps ending the run and starting it again. To check again after a wait, use "Retry" instead.

:::

### Waits and Retry

The wait is a pause between the check and the action, and it applies to every action. For example, "Continue" with a wait of 5 minutes runs the Job's first Task, or the Task, 5 minutes after the check.

"Retry" needs a wait, which sets the time between checks:

- In a Job's Condition Set, the first re-check runs at once, without the wait. The wait applies before each later re-check
- In a Task's Condition Set, the wait applies before every re-check

:::warning

"Retry" has no attempt limit. As long as the set returns a result whose action is "Retry", the Server keeps checking and the Job keeps running. Use "Retry" only for a result that is expected to change, for example _On Match None_ while you wait for a file to arrive. Set a wait long enough for that, and give the result you are waiting for an action that moves on, for example "Continue" for _On Match All_.

:::

### Errors and missing Condition Sets

When a condition cannot be checked, or the set has no active condition, the result is _On Match Error_, and its default action is "Exit". See [How the results combine](conditions-conditions#how-the-results-combine).

If a Job or Task refers to a Condition Set that no longer exists, the Server runs it as if it had no Condition Set and logs an error each time. The _Condition set not found_ event of an [Event Trigger - VisualCron](event-trigger-visualcron) fires at the same time.
