---
sidebar_label: 'Task IIS - Is Application Pool Exists'
hide_title: 'true'
---

## Task IIS - Is Application Pool Exists

The IIS - Is Application Pool Exists Task checks whether an application pool exists in the IIS of the VisualCron Server computer, using an IIS Connection. Use its output to control the Job flow before other IIS Tasks run.

![IIS - Is application pool exists Task settings, with the Connection field and the Application pool name field](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Is%20Application%20pool%20exists.png)

:::warning

This Task uses an IIS Connection; see [Connection - IIS](../../connection-iis). The Task always works on the IIS of the VisualCron Server computer: the Connection's _Address_ is not used, and IIS is read as the account of the VisualCron Server service. The Connection's _Username_ and _Password_ are used only for network access.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### IIS - Is application pool exists tab

- _Connection_: the IIS Connection. Required. Click the _Settings_ icon to open _Manage Connections_
- _Application pool name_: the name of the application pool, matched exactly, including case. Required

### Output and errors

The output is "Exists" when the application pool exists and "Not exists" when it does not. The Task reports success in both cases, so check the output, for example on the ***Flow*** tab.

The ***TimeOut*** tab does not stop this Task.
