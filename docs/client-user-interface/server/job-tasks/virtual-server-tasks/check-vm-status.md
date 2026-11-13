---
sidebar_label: 'Task Virtual Server - Check VM Status'
hide_title: 'true'
---

## Task Virtual Server - Check VM Status

The Virtual Server - Check VM Status Task gets the status of a virtual machine on Microsoft Virtual Server, on the VisualCron Server computer or on a remote computer.

![Check VM status tab of the Virtual Server Check VM Status Task, with the Server location options, Credential, Virtual Machine Name and the Options group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Virtual%20Server%20Tasks/Check%20VM%20Status.png)

:::warning

If Virtual Server reports an error, the error is written to standard error, and the Task reports success. To catch it, check the standard error output, for example with the output conditions on the ***On error*** tab (see [Task - On Error](../../task-on-error)).

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Check VM status tab

- _Local server_: control Virtual Server on the VisualCron Server computer. Selected by default
- _Remote server_: control Virtual Server on another computer
- _Server name_: the DNS name or IP address of the remote computer. Variables are replaced in this field
- _Credential_: the [Credential](../../global-credentials) to sign in to the remote computer, with its domain, user name and password. Required with _Remote server_. Click the _Settings_ icon to add or edit Credentials
- _Virtual Machine Name_: the name of the virtual machine. Click _Refresh_ to list the virtual machines on the selected server. Variables are replaced in this field
- _If VM is in transient state - wait for evaulation_: when the virtual machine is changing state, wait for the change to end before reporting. Checked by default
- _Timeout_: how long to wait, from "1" to "600" seconds, "60" by default. Available when the check box above is checked

### Output and errors

The output is the status of the virtual machine. If the Credential is not found, or an unexpected error occurs, the Task fails.
