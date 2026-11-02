---
sidebar_label: 'Task Service - Start Service'
hide_title: 'true'
---

## Task Service - Start Service

The Start service Task starts a Windows service on the Server computer or on a remote computer, and waits until it runs.

![Start service tab, with the Credential and the service settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Service%20Tasks/Start%20Service.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Start service tab

**Credentials**

The Credential the Task runs as to control a service on a remote computer. It is used only with _Remote_. Click the settings button to open _Manage credentials_; see [Credentials](../../global-credentials).

**Service**

- _Local_ (default): the service runs on the Server computer
- _Remote_: the service runs on another computer
- _Hostname_: the name of the remote computer. Available with _Remote_
- _Service name_: the name of the service to start. Type it, or click the refresh button to fill the list with the services of the computer. Host name and service name may contain Variables

### Output and errors

If the service was stopped, the Task starts it and the output says it was successfully started. If it was already running, the output says so.

:::warning

The Task waits until the service runs, without a time limit of its own. A service that is paused, or that does not finish starting, keeps the Task waiting. Set a time limit on the ***TimeOut*** tab.

:::
