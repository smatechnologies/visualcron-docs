---
sidebar_label: 'Task Virtual Server - Start VM'
hide_title: 'true'
---

## Task Virtual Server - Start VM

The Virtual Server - Start VM Task starts a virtual machine on Microsoft Virtual Server, on the VisualCron Server computer or on a remote computer.

![Start VM tab of the Virtual Server Start VM Task, with the Server location options, Credential, Virtual Machine Name and the Options group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Virtual%20Server%20Tasks/Start%20VM.png)

:::warning

If Virtual Server reports an error, the error is written to standard error, and the Task reports success. To catch it, check the standard error output, for example with the output conditions on the ***On error*** tab (see [Task - On Error](../../task-on-error)).

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Start VM tab

- _Local server_: control Virtual Server on the VisualCron Server computer. Selected by default
- _Remote server_: control Virtual Server on another computer
- _Server name_: the DNS name or IP address of the remote computer. Variables are replaced in this field
- _Credential_: the [Credential](../../global-credentials) to sign in to the remote computer, with its domain, user name and password. Required with _Remote server_. Click the _Settings_ icon to add or edit Credentials
- _Virtual Machine Name_: the name of the virtual machine. Click _Refresh_ to list the virtual machines on the selected server. Variables are replaced in this field
- _Wait for completion_: wait until the virtual machine has started before the Task ends. Checked by default
- _Resume paused machine_: resume the virtual machine when it is paused. Checked by default

### Output and errors

If the Credential is not found, or an unexpected error occurs, the Task fails.
