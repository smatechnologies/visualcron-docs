---
sidebar_label: 'Settings - Default Flows'
hide_title: 'true'
---

## Settings - Default Flows

Default flows are Flows that VisualCron adds to every new Job or every new Task. Use them for Flows you want everywhere, for example a Notification when a Job fails. A default flow is added when you create a Job or Task in the Client. It is not added to existing Jobs and Tasks unless you add it as described below.

_Server_ -> _Main settings_ -> _Settings_ -> **_Default flows_** tab

![The Default flows tab with the Add, Edit, Clone and Delete buttons and two default flows, one for Jobs and one for Tasks, both On error with Run Notification](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Default%20Flows.png)

### Add, edit, clone and delete default flows

- _Add_ -> _Job flow_: adds a default flow for new Jobs
- _Add_ -> _Task flow_: adds a default flow for new Tasks
- _Edit_: changes the selected default flow (you can also double-click it)
- _Clone_: copies the selected default flow
- _Delete_: removes the selected default flow (you can also press Delete)

The _Default for_ column shows whether a flow is for "Jobs" or "Tasks". The Flow window is the same as on the **_Flow_** tab of a Job or Task (see [Job - Flow](job-flow) and [Task - Flow](task-flow)).

_Server_ -> _Main settings_ -> _Settings_ -> **_Default flows_** -> _Add_ -> _Job flow_

![The Job Flow window with the Job Condition On complete and Always, and the Job flow control options Stop Job, Wait and retry Job, Run Job, Run Notification and Deactivate Job](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Edit%20Job%20Flow.png)

Click _Apply settings_ to save your changes. New Jobs and Tasks get the default flows that were saved at the time you create them. Every new Task also gets two Flows of its own: _On success_ with _Continue with next Task_, and _On error_ with _Stop Job_.

### Add a default flow to existing Jobs or Tasks

To add the default flows to one existing Job or Task, open its **_Flow_** tab and click _Get default flows_. VisualCron adds the default flows for Jobs, or for Tasks, that are missing, and updates the copies that are already there.

To add or remove one flow on all existing Jobs or Tasks of the Server:

1. On the **_Default flows_** tab, right-click the flow.
2. To add it, select _Add to all existing_ -> _Jobs_ for a Job flow, or _Add to all existing_ -> _Tasks_ for a Task flow. To remove it, select _Delete from all existing_ -> _Jobs_ or _Tasks_.
3. Click _Ok_ in the message. The Server updates and saves every Job in the background, including the built-in Jobs, which can take some time.

The same right-click menu is also available on the **_Flow_** tab of a Job or Task.

_Server_ -> _Main settings_ -> _Settings_ -> **_Default flows_** -> right-click a flow

![The right-click menu of a default flow with Edit, Delete, Clone, Add to all existing and Delete from all existing, and the Jobs and Tasks submenu](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Add%20Job%20Flow%20to%20All%20Existing.png)

:::warning

_Add to all existing_ and _Delete from all existing_ change the Jobs on the Server at once. They do not wait for _Apply settings_, and _Cancel_ does not undo them. If a Job is open for editing while the update runs, close it with _Cancel_, not _Ok_. Otherwise its old Flows are saved over the update.

Choose the type that matches the _Default for_ column. _Add to all existing_ -> _Jobs_ adds the flow to every Job, also when it is a Task flow, and _Tasks_ adds it to every Task, also when it is a Job flow. The choice also changes the type of the default flow itself, and the changed type is saved when you click _Apply settings_.

:::

:::note

VisualCron identifies each Flow by a hidden ID, not by what it does. Two Flows that do the same thing are still different Flows. If you change a default flow after you added it to all existing Jobs, select _Add to all existing_ again: the copies with the same ID are updated. _Delete from all existing_ removes only the copies with that ID.

:::