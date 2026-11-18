---
sidebar_label: 'Task IIS - Change Application Pool State'
hide_title: 'true'
---

## Task IIS - Change Application Pool State

The IIS - Change Application Pool State Task starts, stops or recycles an existing application pool in the IIS of the VisualCron Server computer, using an IIS Connection. Recycling an application pool restarts its worker process, which can clear memory leaks or hung processes without a full stop and start.

![IIS - Change state of the app pool Task settings, with the Connection field and the Name and Operation fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Change%20state%20of%20the%20app%20pool.png)

:::warning

This Task uses an IIS Connection; see [Connection - IIS](../../connection-iis). The Task always works on the IIS of the VisualCron Server computer: the Connection's _Address_ is not used, and the changes are made as the account of the VisualCron Server service, which must be allowed to change IIS. The Connection's _Username_ and _Password_ are used only for network access.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### IIS - Change state of the app pool tab

- _Connection_: the IIS Connection. Required. Click the _Settings_ icon to open _Manage Connections_
- _Name_ (_Application pool parameters_ group): the name of the application pool, matched exactly, including case. Required. Click the _Refresh_ icon to list the application pools of the VisualCron Server computer
- _Operation_: "Nothing" (default), "Start", "Stop" or "Recycle". With "Nothing", the application pool is not changed

### Output and errors

The output is the state that IIS reports after the operation, for example "Started" or "Stopped". With "Nothing", the output is "Starting", although the application pool is not changed. When the application pool is not found, the Task does nothing and writes no output, and the Task reports success.

The ***TimeOut*** tab does not stop this Task.
