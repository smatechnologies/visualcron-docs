---
sidebar_label: 'Task - Notifications'
hide_title: 'true'
---

## Task - Notifications

Notifications for Jobs and Tasks are managed in the same way, see [Global - Notifications](global-notifications) for more information.

Since version 7.0.0 Notifications are global, reusable objects (any Task can be used as a Notification) and a Task no longer has a dedicated *Notifications* tab. Instead, a Notification is run from the Task's [Flow](task-flow) using the *Run Notification* action.

The flow event you select determines when the Notification is sent — *On start*, *On error*, *On success*, *On complete* or *On running longer than*. This also affects which Variables are available in the Notification, since the available context depends on when it runs.
