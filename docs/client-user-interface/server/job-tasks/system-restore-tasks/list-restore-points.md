---
sidebar_label: 'Task System Restore - List Restore Points'
hide_title: 'true'
---

## Task System Restore - List Restore Points

The List restore points Task lists the Windows System Restore points on the Server computer or on a remote computer.

![List restore points tab, with the Credential and the scope](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Restore%20Tasks/List%20Restore%20Point.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### List restore points tab

**Credentials**

The Credential used to connect to the remote computer. Use it only with _Remote_: Windows does not accept a user name and password for a connection to the local computer, and the Task fails. Click the settings button to open _Manage credentials_; see [Credentials](../../global-credentials).

**Scope**

- _Local_ (default): lists the restore points on the Server computer
- _Remote_: lists the restore points on another computer
- _Hostname_: the name of the remote computer. Type it or select it from the list of network computers. Available with _Remote_

### Output and errors

The output has one line for each restore point: its sequence number and its description, separated by a tab. Use the sequence number in the [Perform system restore Task](perform-system-restore).
