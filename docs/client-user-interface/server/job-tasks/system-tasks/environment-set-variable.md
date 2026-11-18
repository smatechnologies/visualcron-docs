---
sidebar_label: 'Task System - Environment - Set Variable'
hide_title: 'true'
---

## Task System - Environment - Set Variable

The Environment - Set variable Task sets the value of an environment variable of the VisualCron Server process, of a user or of the VisualCron Server computer.

![Set variable Task settings, with the Credentials, Variable name, New value and Variable scope fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Set%20Variable.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The Task works on the VisualCron Server computer only.

### Environment - Set variable tab

- _Credentials_: the Credential the Task runs as. Required for the "User" scope, where the Task changes the variables of that Credential's user. This needs the Credential's default logon settings (local logon, with the profile loaded). Without a Credential, the Task runs as the account of the VisualCron Server service. Select a Credential, or click the _Settings_ icon to open _Manage credentials_; see [Global - Credentials](../../global-credentials)
- _Variable name_: the name of the variable. When it does not exist, the Task creates it
- _New value_: the new value. In the "Process" and "Machine" scopes, an empty value removes the variable
- _Variable scope_: "Process" (default), "User" or "Machine"

  - "Process": the environment of the VisualCron Server process. The change applies only to that process and lasts until the VisualCron Server restarts
  - "User": the user variables of the Credential's user, stored in that user's `Environment` registry key (`HKEY_CURRENT_USER\Environment` for a logged-on user)
  - "Machine": the system variables of the computer, stored in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment`

  A change in the "User" or "Machine" scope does not reach programs that are already running, including the VisualCron Server.

### Output and errors

On success, the output is "Setting the value of the variable was successful". When the change fails, the Task fails and the error is in the standard error output.
