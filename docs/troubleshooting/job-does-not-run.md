---
sidebar_label: 'Job Does Not Run'
hide_title: 'true'
---

## Job Does Not Run

### Symptom

A Job does not run when it should.

### Cause

The most common causes are a Job that is not active, a Server that is off, a Trigger that is set wrongly, and an error in a Task.

### Fix

Check the following, in this order:

1. **The Job is active.** In the Job list, right-click the Job. If the menu shows *Activate Job* followed by the Job name, select it.
2. **The Server is on.** If the ***Server*** tab shows *Server [Off]*, click it. It then shows *Server [On]*.
3. **The Job runs manually.** Right-click the Job and select *Run Job* followed by the Job name. If it runs, the Trigger settings are the problem: check the next run time and correct the Trigger. If it does not run, check the Task settings.
4. **The logs show an error.** Look in the Server log and in the *Output* of the Task.
5. **The command and arguments are in separate fields.** In an Execute Task, put the program in *Command* and its arguments in *Arguments*, for example "C:\php\php.exe" and "-q myscript.php". If *Command* holds the path of an existing .exe, .bat or .cmd file followed by arguments, VisualCron splits them itself; other commands are not split.

If you still cannot find the cause, collect a debug log. To collect a debug log, complete the following steps:

1. On the ***Server*** tab, click *Settings*.
2. Click the ***Log settings*** tab.
3. Click the ***Settings*** tab.
4. Select *Extended debug logging*. See [Settings - Log Settings](../client-user-interface/server/settings-log-settings).
5. Click *Apply settings*.
6. Run the Job manually again.
7. Open today's `log_server<yyyyMMdd>.txt` in the log folder. You can also view the log in the Client; see [Information - Log](../client-user-interface/server/information-log).
8. Look for the error.

   The log shows why the Job did not run.

When you have finished, clear *Extended debug logging* again, because it slows the Server.

If you believe the error is in VisualCron itself, send the log file to [support@visualcron.com](mailto:support@visualcron.com). Review the log for user names, paths and server names before you send it.