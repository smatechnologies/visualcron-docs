---
sidebar_label: 'Task System - Unlock Workstation'
hide_title: 'true'
---

## Task System - Unlock Workstation

The System Unlock workstation Task logs a user on to the desktop of the VisualCron Server computer, or unlocks the desktop when that user is already logged on. A running screen saver is also stopped.

![Unlock workstation Task settings, with the Credentials group and the Lock workstation after login check box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Unlock%20workstation.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Unlock workstation tab

- _Credentials_: required. The Windows user to log on or unlock. Select a Credential, or click the _Settings_ icon to open _Manage credentials_; see [Global - Credentials](../../global-credentials)
- _Lock workstation after login_ (_Unlock/Login settings_ group): when selected, the desktop is locked again after the logon

### Output and errors

The output says what the Task did: that the user was logged in, that the desktop was unlocked, that no action was needed, that the screen saver was stopped, or that the logon was canceled.

:::warning

When the logon is canceled, the output says so, and the Task reports success. When the selected Credential has been deleted, the Task does nothing and writes no output, and the Task reports success.

:::

:::info Note

For Windows Server 2008 you must enable a setting in Local Security Policy.

:::
