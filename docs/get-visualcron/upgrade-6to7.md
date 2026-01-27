---
sidebar_label: 'Upgrading From VisualCron 6.x to 7.x'
hide_title: 'true'
---

## Upgrading From VisualCron 6.x to 7.x

### General changes
 
A lot of things concerning Notifications, On error and exit code handling has been changed from version 6 to 7.

### Notifications
 
Notifications has been upgraded to use existing Tasks. This affects the Email Notification for example which previously couldn’t send secure emails – you were bound to use the Email Task. Also, the Popup Notification was obsolete in many ways.
 
The way to use Notifications has been changed. The Notifications tab is gone and you are now adding Notifications through the [Flow Tab](../client-user-interface/server/job-flow). This new approach adds possibilities to notify you in other situations than the previous. Previously you could just send “On start”, “On complete”, “On error”. There was never a “On success” or send a Notification based on output or based on a specific exit code. This has been added now.

If you use Variables like `{TASK(Active,StdOut)}` in Notifications you need to change them to `{TASK(PrevTask,StdOut)}`. The reason is that the new Notifications now inherit from Tasks which means that Active refers to the current Task (in this case Notification). By using PrevTask you step back on step to the last Task that was ran in the Job.

### Exit codes and collection
 
Exit code handling works differently. Previously, an error could be ignored and was then reset to 0. Now, we keep the original exit code and focus on another property – the result of the actual Exit code collection that is used for the Task.

### Backwards compatibility and import
 
**Notifications**

Notifications should be automatically moved to the “Flow” tab with some exceptions:

**Email Notification** – we are able to move most settings but as we are using Connections instead of settings from Server settings to configure email settings we have tried to create a new Connection based on previous settings.

**Popup Notification** – the new Popup Notification is simply too advanced and different. You need to look over settings in that Notification in order for it to work fully.

**Conditions**

If you are using Conditions that look at exit code in combination with ignoring certain errors you might want to adjust the Condition as the actual exit code is no longer reset to 0 when a Task error is ignored.