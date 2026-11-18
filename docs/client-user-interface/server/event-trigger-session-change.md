---
sidebar_label: 'Event Trigger - Session Change'
hide_title: 'true'
---

## Event Trigger - Session Change

The Session Change Trigger fires on Windows session events, such as console and remote session connects and disconnects, user logon and logoff, session lock and unlock, and changes in the remote control status of a session. It watches the sessions on the computer that runs the VisualCron Server. The settings are on the ***Session change*** tab.

![The Session change tab of the Add/Edit event window: the Event type list with nine session events, none checked; All users selected; Username and Domain unavailable under Specific user](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Triggers/Event%20Triggers/Event%20Trigger%20-%20Session%20Change.png)

**Session change**

**Event type**

Check one or more events:

* *A console session has connected*
* *A console session has disconnected*
* *A remote session has connected*
* *A remote session has disconnected*
* *A user has logged on to a session*
* *A user has logged off from a session*
* *A session has been locked*
* *A session has been unlocked*
* *The remote control status of a session has changed*

The Client does not require an event. With *All users* and no event checked, the Trigger never fires.

**All users / Specific user**

* *All users*: the default. The Trigger fires for each checked event, for any user
* *Specific user*: enter *Username* and *Domain*

:::warning

*Specific user* currently does not narrow the Trigger. It fires for a checked event of any user, and also for any session event of the specified user, even one that is not checked. To react to one user only, select *All users* and check the user in the Job, for example with a [Job condition](job-conditions) on the result Variable `SessionChange.Result.UserName`.

:::

**Username**

The Windows user name. Required for *Specific user*. It must match exactly, including case. Accepts Variables.

**Domain**

The user's short domain name, for example `CONTOSO`, or the computer name for a local user. Required for *Specific user*; it must match exactly, including case. Accepts Variables.

With *Specific user*, each session event that Windows reports without a user writes the error "Could not match on User/Domain because user info could not be retrieved" to the log. You can ignore these entries.

### Result Variables

When the Trigger fires, it sets these result Variables:

* `SessionChange.Result.UserName` and `SessionChange.Result.Domain`: the user of the session; empty when Windows reports no user
* `SessionChange.Result.SessionChangeType`: the event, for example `SessionLogon` or `SessionLock`
* `SessionChange.Result.UserTargetType`: `AllUsers` or `SpecificUser`, as set in the Trigger

For example, `{TRIGGER(Active|LastTrigger|SessionChange.Result.UserName)}` returns the user of the session event that started the run. *Last run*, `{TRIGGER(Active|LastTrigger|LastRun)}`, returns the time the Trigger fired. See [Variables](global-variables) for how *Last trigger* and the other keys work.
