---
sidebar_label: 'Task Hyper-V - Apply Snapshot'
hide_title: 'true'
---

## Task Hyper-V - Apply Snapshot

The Hyper-V - Apply Snapshot Task applies an existing snapshot to a virtual machine on the VisualCron Server computer or on a remote Hyper-V host, by running `Restore-VMSnapshot`.

![Apply snapshot tab of the Hyper-V Apply Snapshot Task, with the Server location options, Credential, Virtual machine and Snapshot name fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Hyper-V%20Tasks/Apply%20snapshot.png)

:::warning

With _Remote server_, the Credential's user name and password are written as plain text into the PowerShell script that runs on the VisualCron Server computer; see [Hyper-V Tasks overview](overview). Errors that PowerShell reports while the command runs, such as an unknown virtual machine name or a failed remote sign-in, are not checked, and the Task reports success.

:::

:::warning

Applying a snapshot replaces the current state of the virtual machine without asking for confirmation. Changes made since the snapshot are lost unless you create a snapshot first.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Apply snapshot tab

- _Local server_: run the command on the VisualCron Server computer. Selected by default
- _Remote server_: run the command on another computer through PowerShell remoting
- _Server name_: the host name of the remote Hyper-V computer. Variables are not replaced in this field
- _Credential_: the [Credential](../../global-credentials) to sign in to the remote computer. Required with _Remote server_. The Credential's domain is not used, so enter the user name of a domain account as `DOMAIN\user`. Click the _Settings_ icon to add or edit Credentials
- _Virtual machine_: the name of the virtual machine. With _Local server_, click _Refresh_ to list the virtual machines on the VisualCron Server computer. With _Remote server_, _Refresh_ fails in this version; type the name. Variables are replaced in this field
- _Snapshot name_: the name of the snapshot to apply. With _Local server_, click _Refresh_ to list the snapshots that the selected virtual machine already has; with _Remote server_, _Refresh_ fails in this version, so type the name. Required. Variables are replaced in this field

### Output and errors

An error that stops the PowerShell script makes the Task fail. Other errors are not checked; see [Hyper-V Tasks overview](overview).
