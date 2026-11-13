---
sidebar_label: 'Event Trigger - VisualCron'
hide_title: 'true'
---

## Event Trigger - VisualCron

The VisualCron Trigger fires on events inside VisualCron, for example when a Job starts or completes, when a Trigger is deactivated or when a Credential changes. It can watch the Server that runs the Trigger or a remote VisualCron Server. Events caused by this Trigger itself, for example its own activation, do not fire it.

The settings are on the ***VisualCron*** tab.

![VisualCron tab of the Add/Edit event window with the Local server and Remote server options, the Event tree, the Job events group and the Reconnect group](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20VisualCron.png)

**Local server / Remote server**

A pair of radio buttons that select which VisualCron Server the Trigger should listen on:

* *Local server*: listen for events on the Server that runs the Trigger (default)
* *Remote server*: listen for events on another VisualCron Server. Select a [VisualCron Connection](../server/connection-visualcron) to that Server in the Connection list, which is available only with this option

With *Remote server*, the Trigger handles at most one event per *Polling interval* (*Check every*) on ***Main settings***, and checks the connection at the same interval. Keep the default of 1 second so that events are not delayed. With *Local server*, this value is not used.

:::warning

If the Trigger cannot connect to the remote Server when it starts, it is deactivated at once, without reconnect attempts. Check the Connection and the remote Server, then activate the Trigger again. The settings in the *Reconnect* group apply only to a connection that is lost after it was made.

:::

:::note

With *Remote server*, these events do not fire the Trigger: the events of the *Trigger* category, *Server status changed to 'on'*, *Server status changed to 'off'*, *Server settings updated* and the events of the *Load balancing* category. To react to these events, add the VisualCron Trigger to a Job on the Server where they happen, with *Local server*.

:::
 
### VisualCron Events

The events are grouped by category in the *Event tree*. Check each event that should fire the Trigger; a category has no checkbox of its own, so check its events one by one. The categories and events are listed below.
 
### Jobs

**Job added**: fires when a Job is added.

**Job updated**: fires when an existing Job is updated.

**Job deleted**: fires when a Job is deleted.

**Job started**: fires when a Job starts.

**Job paused**: fires when a Job is paused.

**Job resumed**: fires when a paused Job is resumed.

**Job completed**: fires when a Job completes, successfully or with failure.

**Job completed - successfully**: fires when a Job completes successfully.

**Job completed - failed**: fires when a Job completes with failure.

**Job activated**: fires when a Job is activated.

**Job inactivated**: fires when a Job is deactivated.

**Job missed**: fires when a run of a Job does not take place: a time exception of the Job stops the run, *Use run random value* skips it, or the license, trial or subscription does not allow it. It does not fire when a run is skipped because the Job is already running. The *Verbose message* result Variable gives the reason and the time the Job should have run.

### Server

**Server status changed to 'on'**: fires when the Server status is switched on in the Client. It does not fire when the VisualCron service starts; use *Server startup complete* for that.

**Server status changed to 'off'**: fires when the Server status is switched off in the Client.

**Server startup complete**: fires when the Server has finished starting.

**Server service stop initiated**: fires when a stop of the Server service has been started.

**Server settings updated**: fires when the settings of the Server are updated.

**Unhandled exception occurred in Server**: fires when an unhandled exception occurs in the Server.

:::note

(Local server only) When the Server is turned off, it stops its Event Triggers, unless *Ignore Server Off (always run)* is checked on ***Main settings***. To react to *Server status changed to 'off'* or *Server status changed to 'on'*, check *Ignore Server Off (always run)* so that the Trigger keeps running while the Server is off.

:::
 
### Trigger

**Trigger activated**: fires when a Trigger is activated.
 
**Trigger inactivated**: fires when an Event Trigger stops monitoring. This happens when the Trigger is deactivated or fails, each time its Job is saved (the Server restarts the Job's Event Triggers), and when the Server is turned off. Time Triggers do not raise this event.
 
**Trigger inactivated by error**: fires when an Event Trigger stops because of an error, for example when a VisualCron Trigger cannot connect to its remote Server when it starts.
 
**Trigger expired (deleted or inactivated)**: fires when a Trigger expires, whatever its *Expire action* on the ***Expires*** tab.
 
**Trigger expired (inactivated)**: fires when a Trigger is deactivated. This happens when it expires with the *Expire action* *Inactivate trigger*, and also when a user deactivates it or an error deactivates it.
 
**Trigger expired (deleted)**: fires when any Trigger on the Server expires with the *Expire action* *Delete trigger*. *Job name* and *Ignore current Job* do not limit this event, and the *JobId* and *Job name* result Variables are empty for it.
 
**Trigger deleted**: currently never fires the Trigger. To react when a Trigger is removed, use *Job updated* for its Job.

:::tip

To be alerted when a Trigger stops because of an error, check *Trigger inactivated by error* and select *All jobs* in *Job name*. Some Triggers stop without raising this event, for example a VisualCron Trigger whose reconnect attempts run out. *Trigger inactivated* covers those cases too, but it also fires for every Job save and every Server stop.

:::

### Condition set

**Condition set added**: fires when a Condition set is added.

**Condition set updated**: fires when a Condition set is updated.

**Condition set deleted**: fires when a Condition set is deleted.

**Condition set not found**: fires when a referenced Condition set cannot be found.

### Connections

**Connection added**: fires when a Connection is added.

**Connection updated**: fires when a Connection is updated.

**Connection deleted**: fires when a Connection is deleted.

**Connection not found**: fires when a referenced Connection cannot be found.

**Connection failed**: fires when a Connection fails, for example because of an authentication or network error.

### Credentials

**Credential added**: fires when a Credential is added.

**Credential updated**: fires when a Credential is updated.

**Credential deleted**: fires when a Credential is deleted.

**Credential not found**: fires when a referenced Credential cannot be found.

### Notifications

**Notification added**: fires when a Notification is added.

**Notification updated**: fires when a Notification is updated.

**Notification deleted**: fires when a Notification is deleted.

**Notification not found**: fires when a referenced Notification cannot be found.

### Users

**User added**: fires when a User is added.

**User updated**: fires when a User is updated.

**User deleted**: fires when a User is deleted.

**User logon**: fires when a User logs on.

### Load balancing

**Load balancing condition is met**: fires when a load balancing condition is met.

**Load balancing action performed**: fires when a load balancing action is performed.

**Broker turned on**: fires when the load balancing broker is started.

**Broker turned off**: fires when the load balancing broker is stopped.

**Unhandled broker exception**: fires when an unhandled exception occurs in the load balancing broker.

**Load balancing agent connected**: fires when a load balancing agent connects.

**Load balancing agent disconnected**: fires when a load balancing agent disconnects.

**Load balancing agent not available**: fires when a load balancing agent becomes unavailable.

### Job events

The *Job events* group limits the events of the *Jobs* and *Trigger* categories to one Job, except *Trigger expired (deleted)*. It is available when an event in the *Trigger* category, or an event in the *Jobs* category other than *Job added*, is checked. Events of the other categories are not limited by Job.

**Job name**

Select the Job whose events fire the Trigger, or *All jobs* to react to the events of every Job. While a Job or Trigger event is checked, you cannot save the Trigger with *No job selected*. Type in the *Filter..* box to shorten the list. With *Remote server*, click *Reload* to load the Jobs of the remote Server; *Reload* is available only for a remote Server.

:::note

*Job added* fires only when *Job name* is *All jobs*, because a new Job cannot be selected before it exists. When *Job added* is the only Job or Trigger event checked, the *Job events* group is not available. To select *All jobs* in that case, check another event in the *Jobs* category, select *All jobs*, and then clear that event. The selection is kept.

:::

**Ignore current Job**

When checked, events of the Job that owns this Trigger do not fire it. Use it with *All jobs* to keep a Job from starting itself again, for example on *Job completed*.

### Reconnect

**On error reconnect attempts**

Used with *Remote server*: the number of failed connection checks in a row before the Trigger stops watching (1 to 500; default 100). When the attempts run out, the Trigger stops watching but still shows as active, and *Trigger inactivated by error* is not raised. If the Trigger no longer fires, check the log for "all attempts are exhausted", then deactivate and activate the Trigger, or save the Job. VisualCron tries to reconnect after each failed check except the last, so it makes one reconnect attempt fewer than this number. A successful reconnect starts the count again.

**On error reconnect interval (seconds)**

The number of seconds to wait after a failed reconnect attempt (1 to 500; default 10).

### Result Variables

In the *Variables* window, find the result Variables under the Job's Trigger, in *Result*. With *Last trigger* (`Active|LastTrigger`), a Variable reads the result of the firing that started the run.

When the Trigger fires, it sets these result Variables:

**JobId**

The ID of the Job that the event is about, for example `{TRIGGER(Active|LastTrigger|VisualCron.Result.Job.Id)}`. Empty for events that are not about a Job, such as Server events.

**Job name**

The name of that Job, `{TRIGGER(Active|LastTrigger|VisualCron.Result.Job.Name)}`. The name is looked up on the Server that runs the Trigger. It is empty when the Job no longer exists, for example after *Job deleted*, or when the Job is on a remote Server; use *JobId* in those cases.

**Verbose message**

Text that describes the event, for example "Server status changed to 'On'", `{TRIGGER(Active|LastTrigger|VisualCron.Result.Message)}`.

**Last run**

The date and time the Trigger last fired, `{TRIGGER(Active|LastTrigger|LastRun)}`. In the *Variables* window, find it under the Job's *Triggers*, in *Last trigger*; the *Result* node lists it only for a specific Trigger.

For the general rules of result Variables, see [Variables](global-variables).
