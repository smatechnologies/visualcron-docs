---
sidebar_label: 'Task Service - Restart Service'
hide_title: 'true'
---

## Task Service - Restart Service

The Restart service Task stops a running Windows service on the Server computer or on a remote computer, waits up to 3 minutes for it to stop, and then starts it again. A service that is not running is started.

![Restart service tab, with the Credential and the service settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Service%20Tasks/Restart%20Service.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Restart service tab

**Credentials**

The Credential the Task runs as to control a service on a remote computer. It is used only with _Remote_. Click the settings button to open _Manage credentials_; see [Credentials](../../global-credentials).

**Service**

- _Local_ (default): the service runs on the Server computer
- _Remote_: the service runs on another computer
- _Hostname_: the name of the remote computer. Available with _Remote_
- _Service name_: the name of the service to restart. Type it, or click the refresh button to fill the list with the services of the computer. Host name and service name may contain Variables

### Output and errors

The output says the service was successfully started. If the service does not stop within 3 minutes, the Task fails.

:::warning

After starting the service, the Task waits until it runs, without a time limit of its own. Set a time limit on the ***TimeOut*** tab.

:::
