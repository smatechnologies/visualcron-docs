---
sidebar_label: 'Global - Notifications'
hide_title: 'true'
---

## Global - Notifications

Notifications are since version 7.0.0 a way to create global, independent Tasks. The Notifications are stored centrally and are called from [Job Flow](../../client-user-interface/server/job-flow) or [Task Flow](../../client-user-interface/server/task-flow). Any Task can be used as a Notification. The purpose of Notifications was originally to create, e.g. an Email Task once and then be able to re-use it in Job and Task Flow whenever you wanted to receive a Job or Task email with output or similar.
 
A notification is defined either from the main menu **Server > Global objects > Notification**s dialog or from the [Job Flow](../../client-user-interface/server/job-flow) or [Task Flow](../../client-user-interface/server/task-flow).

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Notifications/Notifications.png)

The Manage Notifications window shows configured notifications in a grid. Each row displays the notification type icon and the **Description** of the notification.

The toolbar above the grid provides the following buttons:

* **Add** — opens the Add notification dialog so you can pick a notification (Task) type to create
* **Edit** — edit the selected notification
* **Clone** — create a copy of the selected notification
* **Delete** — delete the selected notification
* **Audit log** — open the [Audit log](../tools/objects-audit-log) for notifications

Right‑clicking a notification opens a context menu that includes the toolbar commands plus the following additional options:

* **Versions** — view the version history for the notification
* **Object relations** — view other VisualCron objects (Jobs, Tasks, Triggers) that reference this notification
* **Notification log** — open the [Notification Log](#notification-log) filtered for this notification
* **Export** — export the selected notification

### Add / Edit notification

The Add/Edit Notification dialog contains the following shared controls at the top:

* **Notification type** — a dropdown that selects which kind of Task is used as the notification (Email, File, Event Log, Syslog, Popup, Sound, Database, Message, etc.). Switching the type changes the configuration tab below
* **Description** — a free‑text name shown in the notification list and used to reference the notification from Job/Task Flow
* **Execute credentials** — the [Credential](../server/global-credentials) used to execute the notification. Click the manage button next to it to open Manage Credentials
* **Notification Id** link (visible when editing only) — left‑click to copy the internal notification ID to the clipboard; right‑click to change the ID

The tab below the shared controls displays the configuration specific to the selected notification type. For specific instructions for each notification type, see the help page for the relevant Task.
 
Below is a screenshot from Task Flow of a Task which, On error, also sends a Notification 'test'.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Notifications/Job%20Notification%20Flow.png)

**Variables**

As usual you can use any Variable in any field within VisualCron.
 
View additional [variable](../../client-user-interface/server/global-variables) information.
 
:::info Note

All variables are not available at all times. The variables are highly dependant on when you choose to notify. For example, specific Task variables are only available when you choose to Notify on start or Notify on complete. Also, if you choose to the variable Output you will get the output of the previous run when using when a Task has completed. The current output is not available until "when a Task has completed".

:::

### Notification Log

This is a section for information on Notification Log
