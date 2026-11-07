---
sidebar_label: 'Commands and Batch Files'
hide_title: 'true'
---

## Commands and Batch Files

This page covers running the commands that ship with Windows, and batch files, from VisualCron. It is for anyone who automates Windows work that has no dedicated Task. Both run through the [Execute Task](../client-user-interface/server/job-tasks-task-process-execute).

### Running a Windows command

- **A program:** for a program that ships with Windows, such as "robocopy.exe" or "netsh.exe", enter its full path in _Command_ and its parameters in _Arguments_
- **A command built into the command prompt:** commands such as `dir`, `copy`, `del` and `echo` are not programs, so the Execute Task cannot start them directly. Run them through the command prompt by setting _Command_ to "C:\Windows\System32\cmd.exe" and _Arguments_ to `/c <command>`, or put them in a batch file

If a command works when you start it yourself but not from VisualCron, see [Windows Command Does Not Execute Correctly](../troubleshooting/windows-command-does-not-execute).

### Windows command reference

Microsoft describes every Windows command, with its parameters, in its [Windows commands reference](https://learn.microsoft.com/windows-server/administration/windows-commands/windows-commands).

### Running a batch file

A batch file runs a set of commands in order, which makes it the usual choice when one command is not enough. The Execute Task runs a batch file in either of two ways:

- Set _Batch type_ to "Command" and enter the full path to the ".bat" or ".cmd" file in _Command_
- Set _Batch type_ to "Batch" and type the commands on the **_Batch_** tab. VisualCron saves them with the Task and runs them as a temporary batch file each time the Task runs

If the batch file uses relative paths, select _Working directory_ and enter the folder those paths start from. Without it, the batch file does not always start in its own folder, so its relative paths can point to the wrong place.

The exit code of the batch file becomes the Task's exit code. With the default exit code collection, any exit code other than "0" makes the Task fail (see [Task - Exit Code Collection](../client-user-interface/server/task-exit-code-collection)). To set the exit code yourself, end the batch file with `exit /b <code>`.

By default, unless _Use shell execute_ is selected, VisualCron keeps what the batch file writes to standard output and standard error as the Task's output.
