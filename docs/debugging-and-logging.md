---
sidebar_label: 'Debug and Logging'
hide_title: 'true'
---

## Debug and Logging

VisualCron writes Server and Client events to log files. To troubleshoot a problem, you can turn on extra debug entries in the Server log. You can also have VisualCron send an email when a Job or Task finishes.

### Turn on extended debug logging

To turn on extended debug logging, complete the following steps:

1. On the ***Server*** tab, click *Settings*.

   The *Settings* window opens.

2. Click the ***Log settings*** tab.
3. Click the ***Settings*** tab.
4. Select *Extended debug logging*.
5. Click *Apply settings*.

   The Server writes extra debug entries to its log.

:::tip

Extended debug logging writes many more entries and adds load to the Server. Clear *Extended debug logging* when you have finished troubleshooting.

:::

### Log files

When *Log to file* -> *Server events* is selected on the same tab, the Server writes one log file a day, `log_server<yyyyMMdd>.txt`, to its log folder.

When *Log to file* -> *Client events* is selected on the ***Log*** tab of *File* -> *Settings* -> *Client settings*, the Client writes one log file a day, `log_client<yyyyMMdd>.txt`. The Client log folder is by default "%LOCALAPPDATA%\VisualCron\log".

For all log options, see [Settings - Log Settings](../client-user-interface/server/settings-log-settings). To view the Server log in the Client, see [Information - Log](../client-user-interface/server/information-log).

### Send email

To let the Server send email, complete the following steps:

1. On the ***Server*** tab, click *Settings*.
2. Click the ***Email settings*** tab.
3. Enter the details of your mail server. See [Settings - Email Settings](../client-user-interface/server/settings-email-settings).
4. Click *Apply settings*.

   The Server can now send email.

To send an email when a Job or Task starts, completes, succeeds or fails, add a Notification to the Job or Task on its ***Flow*** tab. See [Job - Flow](../client-user-interface/server/job-flow), [Task - Flow](../client-user-interface/server/task-flow) and [Global - Notifications](../client-user-interface/server/global-notifications).

### Folders

The settings, log and data folders are under the VisualCron installation folder, by default "C:\Program Files (x86)\VisualCron" on 64-bit Windows. The output cache and the log database are in "C:\ProgramData\VisualCron\output". See [Settings - Folders](../client-user-interface/server/settings-folders).