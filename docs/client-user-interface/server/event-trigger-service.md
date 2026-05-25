---
sidebar_label: 'Event Trigger - Service'
hide_title: 'true'
---

## Event Trigger - Service

The Service event trigger monitors changes is the status of a specific Windows service, stopped or started. The trigger reacts instantly on all changes.
 
A service is a process that runs in the background. List and details about installed services can be retrieved by going to _Windows Control Panel -> Administrative Tools_ and open "Services".
 
Often, services start when the computer starts. Normally, a service stops when an error has occurred in the process. The Service Event Monitor is based on **WMI**. This means that you set the polling interval or use the 60 seconds as default.
 
**Triggers > Add > Event Trigger > Service** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Service.png)

**Service name**

To add a service event you must specify a service name. The field is an editable dropdown — click the Refresh icon to populate the drop-down box with service names, or type a service name directly.
 
**Service status changes / Service status changed to**

Choose between the two radio options to control how the service status is matched:

* **Service status changes** — fire the Trigger whenever the service status changes, regardless of the new state
* **Service status changed to** — fire the Trigger only when the service transitions into one of the specifically selected states in the checkbox list below (default)

When **Service status changed to** is selected, you must tick at least one state in the list below.

**Service status (state list)**

A multi-select checkbox list of service states. When a service with the specified name changes to one of the ticked states, the event is triggered. The following service states are available:

* "Stopped" - The service is not running
* "StartPending" - The service is starting
* "StopPending" - The service is stopping
* "Running" - The service is running
* "ContinuePending" - The service continue is pending
* "PausePending" - The service pause is pending
* "Paused" - The service is paused
 
:::tip Note 

All services may not have all states implemented. Mostly, a service is either started or stopped. Started ("Running") and "Stopped" are always implemented for all services.

:::

**Retry options**

**On error reconnect attempts**

The number of times VisualCron tries to reconnect when the service watcher loses connection to the service control manager. Value 1 to 500 is available. Default value is 5 times.

**On error reconnect interval (seconds)**

The number of seconds to wait between reconnect attempts. Value 1 to 500 is available. Default is 5 seconds.
