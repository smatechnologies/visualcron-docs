---
sidebar_label: 'Task Virtual Server - List VM Machines'
hide_title: 'true'
---

## Task Virtual Server - List VM Machines

The Virtual Server - List VM Machines Task lists the virtual machines on Microsoft Virtual Server, on the VisualCron Server computer or on a remote computer.

![List VM machines tab of the Virtual Server List VM Machines Task, with the Server location options, Credential and the Options group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Virtual%20Server%20Tasks/List%20VM%20Machines.png)

:::warning

If Virtual Server reports an error, the error is written to standard error, and the Task reports success. To catch it, check the standard error output, for example with the output conditions on the ***On error*** tab (see [Task - On Error](../../task-on-error)).

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### List VM machines tab

- _Local server_: control Virtual Server on the VisualCron Server computer. Selected by default
- _Remote server_: control Virtual Server on another computer
- _Server name_: the DNS name or IP address of the remote computer. Variables are replaced in this field
- _Credential_: the [Credential](../../global-credentials) to sign in to the remote computer, with its domain, user name and password. Required with _Remote server_. Click the _Settings_ icon to add or edit Credentials
- _Running_, _Turned off (guest saved)_, _Turned off (guest unsaved)_, _Paused_, _Other (includes all transient states)_ and _Invalid_: the states to include in the list. None is checked by default

### Output and errors

The output has the name of each matching virtual machine on its own line. If the Credential is not found, or an unexpected error occurs, the Task fails.
