---
sidebar_label: 'Task System - Logoff'
hide_title: 'true'
---

## Task System - Logoff

The Logoff user(s) Task logs off all users, or one user, on the VisualCron Server computer or a remote computer.

![Logoff Task settings, with the Credentials group and the Logoff group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Logoff.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Logoff tab

- _Credentials_: optional, and used only with _Remote_: the Task uses it to connect to the remote computer. With _Local_, the Task logs users off as the account of the VisualCron Server service. Select a Credential, or click the _Settings_ icon to open _Manage credentials_; see [Global - Credentials](../../global-credentials)
- _Local_ (_Logoff_ group): logs off users on the VisualCron Server computer. Selected by default
- _Remote_: logs off users on the computer in _Hostname_
- _Hostname_: the host name of the remote computer. Available only with _Remote_
- _Logoff all users_: logs off every user session on the computer. Selected by default
- _Logoff a certain user_: logs off the user in _Username_
- _Username_: the user name to log off, without a domain. When the user has more than one session, only the first session found is logged off. Available only with _Logoff a certain user_

:::warning

_Logoff all users_ is selected by default. It logs off every user session on the computer, and the programs in those sessions close, so unsaved work can be lost.

:::

### Output and errors

On success, the output is "Logoff success". The Task fails when the user in _Username_ has no session, or when no session could be logged off. With _Logoff all users_, the Task succeeds when at least one session is logged off; sessions that could not be logged off are not reported.
