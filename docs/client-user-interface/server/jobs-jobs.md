---
sidebar_label: 'Jobs - Jobs'
hide_title: 'true'
---

## Jobs - Jobs

A defined Job is managed either from the main toolbar or by mouse right-click on a specific Job in the Server/Group/Job/Task grid. To manage a Job you open the _Add Job, Edit Job or Clone Job_ dialogs.
 
Every Job has [Main settings](job-main-settings). To run automatically, it also needs at least one Trigger and one Task. The Job window has these tabs:

* [Main settings](job-main-settings)
* [Triggers](job-triggers)
* [Time exceptions](job-time-exceptions)
* [Conditions](job-conditions)
* [Tasks](job-tasks)
* [TimeOut](job-timeout)
* [Flow](job-flow)
* [Agent distribution](job-agent-distribution) (Pro Subscription only)
 
The only mandatory setting is *Name*. To try the Job, click *Test job* at the bottom of the window. VisualCron runs a temporary, inactive copy of the Job once, with its Job conditions checked, and removes the copy afterward. You need Execute permission for the Job and permission to add Jobs. If you do not have Delete permission, the copy is not removed.

:::warning

*Test job* runs the Tasks for real: files are copied or deleted and messages are sent.

:::
 
:::note 

When you _Clone Job_, please make sure that all underlying variables in Tasks or triggers are updated correctly.

:::

:::note

The Job settings are stored in the jobs.xml file, by default in the "C:\Program Files (x86)\VisualCron\settings\" folder. The folder is set by the "ServerSettingsFolder" registry value (see [Error Loading Server Settings](../../troubleshooting/error-loading-server-settings)).

:::
