---
sidebar_label: 'Connection - VisualCron'
hide_title: 'true'
---

## Connection - VisualCron

The VisualCron Connection stores the address and sign-in settings that these Tasks, Triggers and features use to connect to another VisualCron Server:

- the [Internal - Job/Task Control](job-tasks/internal-tasks/control) Task, to control Jobs and Tasks on another Server
- the [Event Trigger - VisualCron](event-trigger-visualcron) Trigger, to react to events on another Server
- the [Event Trigger - Desktop](event-trigger-desktop) Trigger, to listen for desktop events on a remote VisualCron Server
- the *Remote VisualCron Server* option in [Task Main Settings - Execution Context](task-main-settings-execution-context)
- [Servers - Sync Server Objects](../servers/sync-server-objects)
- the Server Agent connection to a [Broker Server](../servers/broker-server)
- the *Server Connection* option of *Add Server Deck* in Workspaces
- *Send to connection ...* on the right-click menu of Jobs, which copies them to another Server

### Common settings

![VisualCron Connection, Common settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/VisualCron/VisualCron.png)

The ***Common settings*** and ***Proxy*** tabs are the same for every Connection type that has them; see [Common settings](global-connections#common-settings) and [Proxy](global-connections#proxy). VisualCron Connections cannot be tested from this window, and do not use *Code page*. *Timeout* is how long, in seconds, VisualCron waits while it connects to the other Server. When a Job/Task Control Task has its own timeout, the Task's timeout is used instead. In that case, the Server currently uses the hours of the Task's timeout in place of its minutes, so the minutes that are set in the Task are not applied.

### Main settings

These fields are on ***Connection settings*** -> ***Main settings***.

![VisualCron Connection, Main settings tab, with Address, Port, Username and Password](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/VisualCron/Settings.png)

- _Address_: the host name or IP address of the other VisualCron Server
- _Port_: the port of the other Server. "16444" on a new Connection
- _Username_ and _Password_: a VisualCron user on the other Server. That user's permissions decide what VisualCron can do there

### Proxy

![VisualCron Connection, Proxy tab, with the proxy type, address, port, test URL, authentication and credential fields and the Test button](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/VisualCron/Proxy.png)

:::warning

VisualCron Connections show a ***Proxy*** tab, but VisualCron does not use it. The Connection always connects directly, so make sure that the other Server's address and port can be reached without a proxy.

:::
