---
sidebar_label: 'VisualCron Specific Definitions'
hide_title: 'true'
---

## VisualCron Specific Definitions

Some terms have a specific meaning in VisualCron.

### Grid

The main area of the VisualCron Client window, in which Servers, Jobs and Tasks are listed with basic data and their relationship to each other.

### Notification

A message, for example an e-mail, an Event log entry or a popup, that VisualCron sends as a result of a Job or Task. A Notification is run from the Job or Task flow with the _Run Notification_ action; see [Global - Notifications](client-user-interface/server/global-notifications) and [Job - Notifications](client-user-interface/server/job-notifications).

### Run (Job)

A Job runs when one of its Triggers fires, for example a Time Trigger at a set time or an Event Trigger when a file is created. It can also be started by a user from the Client, from another Job's flow with the _Run Job_ action, or from the API or command line. When a Job runs, it runs its Tasks; what each Task does depends on its Task type. See [Job Triggers](client-user-interface/server/job-triggers).

### Server status

The "On" or "Off" status of the VisualCron Server. See [Main - Server On/Off](client-user-interface/server/server-on-off).

### Service status

The "Started" or "Stopped" status of the VisualCron Windows service.

### Task type

The kind of work a Task does, for example starting a program, copying files or running a SQL query. The Task type is chosen when a Task is added to a Job; see [Job - Tasks](client-user-interface/server/job-tasks).
