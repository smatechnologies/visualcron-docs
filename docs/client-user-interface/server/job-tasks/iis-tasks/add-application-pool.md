---
sidebar_label: 'Task IIS - Add Application Pool'
hide_title: 'true'
---

## Task IIS - Add Application Pool

The IIS - Add Application Pool Task creates an application pool in the IIS of the VisualCron Server computer, using an IIS Connection. Application pools isolate web applications from one another.

![IIS - Add a new application pool Task settings, with the Connection and Application pool parameters groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Add%20a%20new%20application%20pool.png)

:::warning

This Task uses an IIS Connection; see [Connection - IIS](../../connection-iis). The Task always works on the IIS of the VisualCron Server computer: the Connection's _Address_ is not used, and the changes are made as the account of the VisualCron Server service, which must be allowed to change IIS. The Connection's _Username_ and _Password_ are used only for network access.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### IIS - Add a new application pool tab

- _Connection_: the IIS Connection. Required. Click the _Settings_ icon to open _Manage Connections_
- _Name_ (_Application pool parameters_ group): the name of the new application pool. Required
- _Start mode_: "On demand" or "Always running". When empty, the IIS default for new application pools is used
- _Pipeline mode_: "Integrated" or "Classic". When empty, the IIS default is used
- _Runtime version_: "Without managed code", "v2.0" or "v4.0". When empty, the IIS default is used
- _Auto start_: when selected, the application pool starts automatically when IIS starts; when cleared, it does not. When the check box is in its third state, neither selected nor cleared (the default), the IIS default is used
- _Enable 32 bit app on 64 bit OS_: when selected, the application pool runs 32-bit applications on a 64-bit Windows. The third state, as for _Auto start_, uses the IIS default
- _Queue length_: the maximum number of requests that IIS queues for the application pool. When empty, or not a whole number, the IIS default is used

:::note

With "Without managed code", the Task writes the text "Without managed code" as the .NET CLR version of the pool, instead of leaving the version empty. Check the pool in IIS Manager after the Task runs.

:::

### Output and errors

On success, the output is "Success". When an application pool with that name already exists, the Task does not change it and writes no output, and the Task reports success.

The ***TimeOut*** tab does not stop this Task.
