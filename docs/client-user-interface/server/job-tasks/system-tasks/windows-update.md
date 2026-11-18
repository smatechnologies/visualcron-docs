---
sidebar_label: 'Task System - Windows Update'
hide_title: 'true'
---

## Task System - Windows Update

The Windows update Task searches the VisualCron Server computer, or a remote computer, for software updates that are not installed, and downloads or installs them in the background.

![Windows update Task settings, with the Download updates, Install updates and Install hidden updates check boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Tasks/Windows%20Update.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Windows update tab

- _Credentials_: the Credential the Task runs as. With _Remote_, it must be allowed to use Windows Update on the remote computer. Select a Credential, or click the _Settings_ icon to open _Manage credentials_; see [Global - Credentials](../../global-credentials)
- _Local_ (_Shutdown settings_ group): updates the VisualCron Server computer. Selected by default
- _Remote_: updates the computer in _Hostname_
- _Hostname_: the host name of the remote computer. Select a computer on the network or type a host name. Available only with _Remote_
- _Download updates_ (_Settings_ group): downloads the updates that are not downloaded yet. Selected by default
- _Install updates_: installs the updates that are not installed. Selected by default
- _Install hidden updates_: also includes updates that are hidden in Windows Update, for both downloading and installing

:::note

The Task accepts the license terms of every update it downloads or installs, without asking.

:::

The Task does not restart the computer: when an update needs a restart, the output says "RebootRequired: True". To restart, use the [Restart](restart) Task.

### Output and errors

The output lists each update the Task prepares to download or install, and the result of the installation in the form `Install result: ResultCode: ..., HResult: ..., RebootRequired: ...`.

:::warning

The Task does not check the result of the download or the installation. A result code other than "2" means that not every update was installed, and the Task reports success.

:::

The ***TimeOut*** tab does not stop this Task.
