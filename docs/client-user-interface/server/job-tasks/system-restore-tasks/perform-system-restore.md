---
sidebar_label: 'Task System Restore - Perform System Restore'
hide_title: 'true'
---

## Task System Restore - Perform System Restore

The Perform system restore Task asks Windows to restore the Server computer or a remote computer to an existing System Restore point.

![Perform system restore tab, with the Credential, the scope and the sequence number of the restore point](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/System%20Restore%20Tasks/Perform%20System%20Restore.png)

:::warning

A system restore changes system files, settings and installed programs on the computer, and takes effect when the computer restarts. This Task does not restart the computer.

Windows returns 0 when it accepts the restore request. The Task treats 0 as a failed restore and raises a restore-failed error. Any return code other than 0, 1 or 2 gives no output, and the Task reports success. Check the computer after it restarts.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Perform system restore tab

**Credentials**

The Credential used to connect to the remote computer. Use it only with _Remote_: Windows does not accept a user name and password for a connection to the local computer, and the Task fails. Click the settings button to open _Manage credentials_; see [Credentials](../../global-credentials).

**Scope**

- _Local_ (default): restores the Server computer
- _Remote_: restores another computer
- _Hostname_: the name of the remote computer. Type it or select it from the list of network computers. Available with _Remote_

**Restore**

- _Sequence number_: the restore point to restore to. Click _Get list_ to fill the list with the restore points of the computer, with their description, event type, restore point type and sequence number. The value may contain a Variable

### Output and errors

A return code of 1 gives the output "Restore successful", and 2 raises a restore-interrupted error.
