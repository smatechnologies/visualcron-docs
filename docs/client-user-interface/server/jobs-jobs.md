---
sidebar_label: 'Jobs - Jobs'
hide_title: 'true'
---

## Jobs - Jobs

A defined Job is managed either from the main toolbar or by mouse right-click on a specific Job in the Server/Job/Task grid. To manage a Job you open the _Add Job, Edit Job or Clone Job_ dialogs.
 
For each Job type, some _Main settings_ must be defined. In order to run something automatically, one or more Triggers and one or more _Tasks_ must be defined for each Job. Finally _Time exceptions, Conditions, Timeout and Notifications_ may be defined for each Job.
 
The only mandatory setting in the _Add Job/Edit Job/Clone Job_ windows is the _Name_ information. When also the Task settings has been defined, the Job can be tested by the Test Job button (in the bottom of the _Add Job/Edit Job/Clone Job_ windows).
 
:::note 

When you _Clone Job_, please make sure that all underlying variables in Tasks or triggers are updated correctly.
The Job settings are stored by VisualCron in the jobs.xml file, by default stored in the "C:\Program Files (x86)\VisualCron\settings\" folder.

:::