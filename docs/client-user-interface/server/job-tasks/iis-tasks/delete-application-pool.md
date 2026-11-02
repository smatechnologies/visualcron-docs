---
sidebar_label: 'Task IIS - Delete Application Pool'
hide_title: 'true'
---

## Task IIS - Delete Application Pool

The IIS - Delete Application Pool Task removes an existing application pool from the IIS of the VisualCron Server computer, using an IIS Connection.

![IIS - Delete an existing app pool Task settings, with the Connection field and the Application pool name field](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Delete%20an%20existing%20app%20pool.png)

:::warning

This Task uses an IIS Connection; see [Connection - IIS](../../connection-iis). The Task always works on the IIS of the VisualCron Server computer: the Connection's _Address_ is not used, and the changes are made as the account of the VisualCron Server service, which must be allowed to change IIS. The Connection's _Username_ and _Password_ are used only for network access.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### IIS - Delete an existing app pool tab

- _Connection_: the IIS Connection. Required. Click the _Settings_ icon to open _Manage Connections_
- _Application pool name_: the name of the application pool to remove, matched exactly, including case. Required. Click the _Refresh_ icon to list the application pools of the VisualCron Server computer

:::warning

The Task removes the application pool from IIS without a prompt, and VisualCron cannot undo it. The Task does not check whether applications still use the application pool.

:::

### Output and errors

On success, the output is "Success". When the application pool is not found, the Task does nothing and writes no output, and the Task reports success.

The ***TimeOut*** tab does not stop this Task.
