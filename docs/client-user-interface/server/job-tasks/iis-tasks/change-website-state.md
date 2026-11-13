---
sidebar_label: 'Task IIS - Change Website State'
hide_title: 'true'
---

## Task IIS - Change Website State

The IIS - Change Website State Task starts, stops or restarts an existing website in the IIS of the VisualCron Server computer, using an IIS Connection.

![IIS - Change state of the web site Task settings, with the Connection field and the Name and Operation fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Change%20state%20of%20the%20web%20site.png)

:::warning

This Task uses an IIS Connection; see [Connection - IIS](../../connection-iis). The Task always works on the IIS of the VisualCron Server computer: the Connection's _Address_ is not used, and the changes are made as the account of the VisualCron Server service, which must be allowed to change IIS. The Connection's _Username_ and _Password_ are used only for network access.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### IIS - Change state of the web site tab

- _Connection_: the IIS Connection. Required. Click the _Settings_ icon to open _Manage Connections_
- _Name_ (_Web site parameters_ group): the name of the website, matched exactly, including case. Required. Click the _Refresh_ icon to list the websites of the VisualCron Server computer
- _Operation_: one of:

  - "Nothing" (default): the website is not changed
  - "Start": starts a stopped website
  - "Stop": stops a started website
  - "Restart": stops and then starts a started website

### Output and errors

On success, the output is the state that IIS reports after the operation, for example "Started".

:::warning

When the website is not in the state the operation needs (for example "Start" on a website that is already started), the Task writes `Operation imposible - current state is` followed by the current state to the standard error output, and the Task reports success. When the website is not found, or with "Nothing", the Task writes no output, and the Task reports success.

:::

The ***TimeOut*** tab does not stop this Task.
