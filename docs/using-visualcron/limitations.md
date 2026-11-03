---
sidebar_label: 'Limitations'
hide_title: 'true'
---

## Limitations

This page lists behavior to keep in mind when you plan Jobs, especially Jobs that run unattended.

- VisualCron is designed for the systems listed in [Requirements](../requirements)
- A run that is missed while the VisualCron service is down is not made up later, unless _Run missed Job once at start_ is checked for the Job. Then the Job runs once when the service starts, if the Server is "On". See [Job - Main Settings](../client-user-interface/server/job-main-settings)
- A run that is missed while the Server is "Off" is never made up, even with _Run missed Job once at start_ checked
- _Run missed Job once at start_ runs the Job only once, however many runs were missed. VisualCron checks only the first missed run: if it falls inside one of the Job's time exceptions, the Job is not run at startup. See [Job - Time Exceptions](../client-user-interface/server/job-time-exceptions)
- _Next run_ does not take time exceptions into account. A run shown there is still skipped if it falls inside a time exception when it is due
- By default, Tasks run in the background as the account the VisualCron service runs as, normally the Local System account. That account cannot see drives mapped in a user's session. Use UNC paths and Credentials, or map the drives in VisualCron. See [Task Main Settings - Execution Context](../client-user-interface/server/task-main-settings-execution-context) and [Global - Network Drives](../client-user-interface/server/global-network-drives)
- Tasks set to run in the foreground need a logged-on user with a connected [Tray Client](visualcron-tray-client). With _Logon/Unlock using Credential_, a Task can log on or unlock a session before it runs. See [Task Main Settings - Execution Context](../client-user-interface/server/task-main-settings-execution-context)
- A Task can fail if another program, or another Task, holds a lock on a file it needs. Windows decides whether more than one program can open a file at the same time
- In general, what Windows does not allow, a Task cannot do either. For example, a Task cannot get more access to a file or folder than the user it runs as has