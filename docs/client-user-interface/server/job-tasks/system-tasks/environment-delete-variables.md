---
sidebar_label: 'Task System - Environment - Delete Variables'
hide_title: 'true'
---

## Task System - Environment - Delete Variables

The Environment - Delete variable Task removes an environment variable of the VisualCron Server process, of a user or of the VisualCron Server computer.

![Delete variable Task settings, with the Credentials, Variable name and Variable scope fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Delete%20Variable.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The Task works on the VisualCron Server computer only.

### Environment - Delete variable tab

- _Credentials_: the Credential the Task runs as. Required for the "User" scope, where the Task removes a variable of that Credential's user. This needs the Credential's default logon settings (local logon, with the profile loaded). Without a Credential, the Task runs as the account of the VisualCron Server service. Select a Credential, or click the _Settings_ icon to open _Manage credentials_; see [Global - Credentials](../../global-credentials)
- _Variable name_: the name of the variable to remove
- _Variable scope_: "Process" (default), "User" or "Machine"

  - "Process": the environment of the VisualCron Server process. The change applies only to that process and lasts until the VisualCron Server restarts
  - "User": the user variables of the Credential's user, stored in that user's `Environment` registry key (`HKEY_CURRENT_USER\Environment` for a logged-on user)
  - "Machine": the system variables of the computer, stored in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment`

  A change in the "User" or "Machine" scope does not reach programs that are already running, including the VisualCron Server.

:::warning

The Task removes the variable without a prompt. VisualCron cannot undo it.

:::

### Output and errors

On success, the output is "The variable was deleted successfully". With "User", the Task fails when the variable does not exist. With "Process" or "Machine", a variable that does not exist is not an error, and the Task reports success.
