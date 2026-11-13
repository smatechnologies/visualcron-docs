---
sidebar_label: 'Task System - Environment - Append Variable'
hide_title: 'true'
---

## Task System - Environment - Append Variable

The Environment - Append variable Task adds text to the value of an environment variable of the VisualCron Server process, of a user or of the VisualCron Server computer.

![Append variable Task settings, with the Credentials, Variable name, Text for append and Variable scope fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Append%20Variable.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The Task works on the VisualCron Server computer only.

### Environment - Append variable tab

- _Credentials_: the Credential the Task runs as. Required for the "User" scope, where the Task changes the variables of that Credential's user. This needs the Credential's default logon settings (local logon, with the profile loaded). Without a Credential, the Task runs as the account of the VisualCron Server service. Select a Credential, or click the _Settings_ icon to open _Manage credentials_; see [Global - Credentials](../../global-credentials)
- _Variable name_: the name of the variable
- _Text for append_: the text to add

  The Task puts the text at the start of the current value, followed by a semicolon. For example, with the current value `C:\Tools` and the text `D:\Bin`, the new value is `D:\Bin;C:\Tools`. When the variable does not exist, it is created with the text followed by a semicolon.

- _Variable scope_: "Process" (default), "User" or "Machine"

  - "Process": the environment of the VisualCron Server process. The change applies only to that process and lasts until the VisualCron Server restarts
  - "User": the user variables of the Credential's user, stored in that user's `Environment` registry key (`HKEY_CURRENT_USER\Environment` for a logged-on user)
  - "Machine": the system variables of the computer, stored in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment`

  A change in the "User" or "Machine" scope does not reach programs that are already running, including the VisualCron Server.

### Output and errors

On success, the output is "Appending the value of the variable was successful". When the change fails, the Task fails and the error is in the standard error output.
