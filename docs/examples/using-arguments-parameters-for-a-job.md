---
sidebar_label: 'Using Arguments/Parameters For a Job'
hide_title: 'true'
---

## Using Arguments/Parameters For a Job

The Execute Task keeps the program and its command-line arguments in separate fields.

- _Command_: the program or batch file to run, with its full path unless it is on the system path. Use UNC paths, not mapped drive letters, for files on network drives
- _Arguments_: everything that follows the program on the command line. Do not start the arguments with a space; VisualCron adds the space between the command and the arguments. Put double quotes around paths that contain spaces. Variables in the arguments are replaced when the Task runs

For example, to run a VBScript file, enter `wscript.exe` in _Command_ and the path to the script in _Arguments_:

```text
Command:   wscript.exe
Arguments: "C:\Scripts\My script.vbs"
```

See [Scripts](../commands/scripts) and [Task Process - Execute](../client-user-interface/server/job-tasks-task-process-execute).
