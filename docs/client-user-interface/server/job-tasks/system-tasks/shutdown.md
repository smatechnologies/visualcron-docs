---
sidebar_label: 'Task System - Shutdown'
hide_title: 'true'
---

## Task System - Shutdown

The System shutdown Task turns off the VisualCron Server computer or a remote computer.

![Shutdown Task settings, with the Credentials group and the Local, Remote and Hostname options](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Shutdown.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Shutdown tab

- _Credentials_: used only with _Remote_, to connect to the remote computer through WMI. Required with _Remote_: without a Credential, the Task fails. Select a Credential, or click the _Settings_ icon to open _Manage credentials_; see [Global - Credentials](../../global-credentials)
- _Local_ (_Shutdown settings_ group): turns off the VisualCron Server computer. Selected by default
- _Remote_: turns off the computer in _Hostname_
- _Hostname_: the host name of the remote computer. Select a computer on the network or type a host name. Available only with _Remote_

:::warning

The shutdown is always forced: programs on the computer are closed without being asked to save their work, so unsaved work is lost. Turning off the VisualCron Server computer also stops the VisualCron Server and the Jobs that are running.

:::

On success, the output is "Shutdown success". When the shutdown fails, the Task fails.
