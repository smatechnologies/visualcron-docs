---
sidebar_label: 'Task System - Environment - Get Variable'
hide_title: 'true'
---

## Task System - Environment - Get Variable

The Environment - Get variable Task writes the value of an environment variable of the VisualCron Server process, of a user or of the VisualCron Server computer to the Task output.

![Get variable Task settings, with the Credentials, Variable name and Variable scope fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Get%20Variable.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The Task works on the VisualCron Server computer only.

### Environment - Get variable tab

- _Credentials_: the Credential the Task runs as. Required for the "User" scope, where the Task reads a variable of that Credential's user. This needs the Credential's default logon settings (local logon, with the profile loaded). Without a Credential, the Task runs as the account of the VisualCron Server service. Select a Credential, or click the _Settings_ icon to open _Manage credentials_; see [Global - Credentials](../../global-credentials)
- _Variable name_: the name of the variable to read
- _Variable scope_: "Process" (default), "User" or "Machine"

  - "Process": the environment of the VisualCron Server process: the values it had when the VisualCron Server started, plus changes made since by Tasks in the "Process" scope
  - "User": the user variables of the Credential's user, stored in that user's `Environment` registry key (`HKEY_CURRENT_USER\Environment` for a logged-on user)
  - "Machine": the system variables of the computer, stored in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment`

### Output and errors

The output is the value of the variable. When the variable does not exist, the output is empty, and the Task reports success.
