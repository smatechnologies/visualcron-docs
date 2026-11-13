---
sidebar_label: 'Connection - AS/400'
hide_title: 'true'
---

## Connection - AS/400

The AS/400 Connection stores the address and sign-in settings that the [Process - AS/400 Command](job-tasks-task-process-as-400-command) Task uses to connect to an IBM i (AS/400) system.

:::note

The AS/400 Command Task uses the IBM i Access client components on the VisualCron Server computer. Install them there before you run the Task.

:::

### Common settings

![AS/400 Connection, Common settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/AS400/AS400.png)

The ***Common settings*** tab is the same for every Connection type that has it; see [Common settings](global-connections#common-settings). AS/400 Connections have no *Test*, and the AS/400 Command Task does not use *Timeout* or *Code page*. To limit how long the Task runs, use the Task's own timeout.

### Main settings

These fields are on ***Connection settings*** -> ***Main settings***.

![AS/400 Connection, Main settings tab, with Address, Username and Password](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/AS400/Settings.png)

- _Address_: the host name or IP address of the AS/400 system
- _Username_: required. The user profile that the Task signs on with
- _Password_: the password of that user profile
