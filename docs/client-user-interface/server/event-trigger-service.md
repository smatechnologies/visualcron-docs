---
sidebar_label: 'Event Trigger - Service'
hide_title: 'true'
---

## Event Trigger - Service

The Service Trigger fires when a Windows service changes, on the Server computer or on a remote computer. It uses WMI, which checks the service at the *Polling interval* (*Check every*) on ***Main settings***, by default every 60 seconds. A change is therefore detected up to that many seconds after it happens.

The Trigger fires on any change that Windows reports for the service while the service is in a selected state, not only on a change of state. For example, changing the startup type of a running service fires a Trigger that has *Running* checked.

To watch a service on another computer, enter its name or IP address in *Computer name* on ***Main settings***. Select a Credential under *Credentials* only for a remote computer: with *Computer name* ".", a Credential makes the connection fail. To see the installed services, run `services.msc`.
 
The settings are on the ***Service*** tab.

![Service tab of the Add/Edit event window with the Service name combo box, the Service status changes and Service status changed to options, the list of service states and the Retry options group](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Service.png)

**Service name**

The name of the service, for example "Spooler", not its display name. Type the name, or click the refresh icon to fill the list with services. The list shows the services of the Server, or of the computer in *Computer name* on ***Main settings*** when it is not "." or "127.0.0.1". The field can contain Variables.

If no service has that name, the Trigger does not fire and nothing is logged. Check the name.
 
**Service status changes / Service status changed to**

* *Service status changes*: checks every state in the list
* *Service status changed to*: fires only for the states you check (default); check at least one state

**Service states**

The list contains *Stopped*, *Start pending*, *Stop pending*, *Running*, *Continue pending*, *Pause pending* and *Paused*.

:::warning

The Service Trigger fires only for *Stopped*, *Running* and *Paused*. It does not fire for *Start pending*, *Stop pending*, *Continue pending* or *Pause pending*, even when they are checked, so *Service status changes* also covers only these three states. To react when a service has started, check *Running*; to react when it has stopped, check *Stopped*.

:::

Each pending state that Windows reports writes "Error in ParseObject" to the log. You can ignore these entries.

**Retry options**

**On error reconnect attempts**

The total number of attempts to connect to WMI and watch the service while the Trigger runs, including the first one (1 to 500; default 5). After that the Trigger is deactivated. The count is not reset after a successful connection. To reset it, deactivate and activate the Trigger.

Without a Credential, a WMI connection that is lost after the Trigger has started is not detected: the Trigger still shows as active but does not fire, and no attempt is used. With a Credential, an error while watching uses one of these attempts. If a Service Trigger that watches a remote computer stops firing, check the log, then deactivate and activate the Trigger.

**On error reconnect interval (seconds)**

The number of seconds to wait between attempts (1 to 500; default 5).

### Result Variables

Each time the Trigger fires, it sets result Variables for the service, for example its state, `{TRIGGER(Active|LastTrigger|Service.Result.State)}`. With *Last trigger* (`Active|LastTrigger`), a Variable reads the result of the firing that started the run. All Service Trigger result Variables are described in [Variables](global-variables).
