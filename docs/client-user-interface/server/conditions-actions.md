---
sidebar_label: 'Conditions - Actions'
hide_title: 'true'
---

## Conditions - Actions

The condition set actions controls what will happen depending on the results of the conditions within the condition set. All results are calculated to one final result.
 
**Global > Conditions > Add/Update Condition set > Actions** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Conditions/Condition%20-%20Actions.png)

The condition set criteria determine how the results of all included conditions in a condition set are evaluated. The following condition set criteria are valid:
* **On Match All** - all conditions returned a "match"
* **On Match Any** - one or more conditions returned a "match"
* **On Match None** - none of the conditions returned a "match"
* **On Match Error** - the condition check failed in some way, i.e. if an "access denied" occurred while checking a file condition
 
For each condition set criteria, a set of actions available:
* **Wait** - wait a specified time (always available)
* **Continue** - Run Task or Job if match (default value for On Match All and On Match Any)
* **Next** - Run next Task in queue (skip current)
* **Retry** - Wait specified time and re-run current Task
* **Exit** - Exit current Job (default value for On Match None and On Match Error)
* **Run Job** - Run specified Job (exits existing Job, runs specified Job)
* **Run Task** - Run specified Task in current Job, after completion it continues with next in order
 
### Wait notes

The wait for each action is a pause between the actual condition check and the action. It can be used in several ways but is most commonly used with the "Retry" action. For example, you want to check if a file exists, but the condition check fails to find the file and thus the result is "Match None". With this result you want to Retry (check again if the file exists) and by the wait parameter you add a pause between each check.
 
The Wait action is not used at the first check when using the "Retry" action. This means that it won't pause before the first check, but on the following retries. For other action types, the "Wait" action is always used independent on if it is the first time or not.
 
### Run Task notes

When Run Task is used, VisualCron tries to find the specified Task within the current Job. If found it runs that Task and Tasks that may follow, in order. When the Task does not reside within the current Job VisualCron only runs the Task alone and no following Tasks.
 
### How the Actions affect Jobs and Tasks

The actions have different effects on Jobs and Tasks. The simple reason for that is that Jobs by themselves have no connection to each other like the Tasks, which are internally connected within a Job.
Actions affecting a Job condition:
* Continue - continues running Job
* Next - exits Job
* Retry - wait and recheck condition
* Exit - exits Job
* Run Job - exits Job try to run other Job
* Run Task - exits Job, runs single Task
 
Actions affecting a Task condition:
* Continue - continues running Task
* Next - runs next Task (if existing)
* Retry - wait and recheck condition
* Exit - exits Job
* Run Job - exits Job and runs Job x
* Run Task - if Job is the same as this current Job then it tries to run the Task within the Job process else it starts a new Job and runs the specified Task there
 
### Handling of errors

By default, all errors that occur in the condition check leads to the "Exit" action. Example of errors the can occur:
* The condition points to a Job or Task that doesn't exist
* An error occurs in a condition check
* "Access denied" on file or folders
 
:::tip Notes

Task flow only makes sense when using Run Tasks in order. Task conditions are only checked on Jobs which has the setting Run Tasks in order on.

:::