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

To add a service event you must specify a service name and at least one state. Click the Refresh icon to populate the drop-down box with service names.
 
**Service status**

Tick the check boxes for the states you want to watch. When a service with a specific name changes or has changed to the selected state, the event is triggered. The following service states exist:
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