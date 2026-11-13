---
sidebar_label: 'Process'
hide_title: 'true'
---

## Robot Task Activities - Process

The Processes activities start a program or document and close running processes.

![The Processes category in the activity list, with Start Process and Close Process](../../../../../../../static/img/RPA/Robot%20Tasks/Process/Processes.png)

---

### Start Process

Starts a program, or opens a document with its default program.

![The Start Process activity with the File name field, the ... button and the Arguments field](../../../../../../../static/img/RPA/Robot%20Tasks/Process/Start.png)

- _File name_: the program or document to start, for example `notepad`. Click _..._ to browse for it. Required
- _Arguments_: the command-line arguments passed to the program
- _WorkingDirectory_: in the Properties pane, the folder the program starts in
- _Priority_: in the Properties pane, the priority of the started process. Default: "Normal"
- _WaitingForExit_: in the Properties pane, how long to wait for the process to end, in milliseconds. "0" does not wait, and "-1" waits until the process ends. Default: "0"

When the document opens in a program that is already running, the activity can fail; start the program itself, with the document in _Arguments_, instead. The activity does not check the exit code of the program. When _WaitingForExit_ runs out before the program ends, the sequence continues and the program keeps running. The file name and arguments are written to the Task output, so do not put a password in _Arguments_.

---

### Close Process

Closes every running process with the name given.

![The Close Process activity with the Click to select link and the Process name field](../../../../../../../static/img/RPA/Robot%20Tasks/Process/Close.png)

- _Process name_: the name of the process to close, without the ".exe" extension, for example `notepad`. Type the name, or click _Click to select_ to pick a running process
- _TimeoutToKill_: in the Properties pane, how long to wait for each process to close, in milliseconds, before ending it. "-1" waits without a limit. When the field is empty, "0" is used, and the process is ended at once. Default: "30000"

For each process with that name, the activity asks its main window to close. If the process has not ended after _TimeoutToKill_, the activity ends the process.

:::warning

Close Process ends every process with that name that it can reach, including one a person is using, and a process that is ended after _TimeoutToKill_, or at once when the field is empty, loses any unsaved work. If no process has that name, the activity does nothing and the Task reports success.

:::

---

### Tips

- Follow _Start Process_ with a [Windows](windows) _Attach Window_ activity with _WaitForWindow_ set, rather than a fixed [Wait](other) activity. The Task then continues as soon as the program's window is ready
- Add a _Close Process_ activity to the _Finally_ block of a [Try Catch](error-handling) activity so that a program started by the Task is always shut down, even when the sequence fails partway through
- For Excel, use the [Excel](excel) category's _New Excel_ and _Quit Excel_ activities rather than Start Process and Close Process. Those activities also give the Excel activities the application they work on
- Use these activities only for programs the Robot Task must drive on screen. To run a command-line tool or a script as part of a Job, an [Execute](../../../../job-tasks-task-process-execute) Task is a better fit than a Robot Task
- The programs start in the desktop session that runs the Robot Task, as the user of that session. That user needs permission to start the program and to reach anything it reads or writes
