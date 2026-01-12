---
sidebar_label: 'Settings - Default Flows'
hide_title: 'true'
---

In the main menu **Server > Main settings > Settings** dialog, you can choose to add Flows that will be added as default for new Jobs OR Tasks. Once you have created a default flow here, the flow will be suggested whenever you open a Job or Task for editing/adding. In this way, Default flows has some resemblances to other global objects but it is not quite the same.
 
**Main > Settings > Default flows** tab


![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Default%20Flows.png)

### Add/Edit/Clone/Delete

Click the **Default flows** icons to update the list of default flows for Jobs and Tasks.
 
**Main > Settings > Default flows > Add > Job flow** window

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Edit%20Job%20Flow.png)

A created default flow will add this flow to all new Jobs or Tasks and will show up in one of the lists in the [Edit Job > Flows](../server/job-flow) tab or the [Edit Task > Flows](../server/task-flow) tab. Note that Tasks always have two flows included by default; On success - Continue with next Task and On error - Stop Job.
 
If the new default flow is also desired for previously defined Jobs/Tasks, you need to click the Get default flows icon for each **Job/Task flow** you want the default flow for.
 
Independently if you right click in the **Default flows** window or in a **Job Flow** or **Task Flow** window, you have the option to add or remove a flow for all Jobs OR Tasks. This will take some seconds and it will run in the background. Thus, the update will not immediately be seen in the **Job Flow** or **Task Flow** window and the Cancel button (not OK) shall be clicked when leaving the window in order not to save the screen contents. The Default Flow Add/Edit/Clone/Delete is based on a hidden Id of the unique flow that is created - not the actual actions it takes (i.e Run Notification, Retry etc). This means that even if you create a Flow that behaves exactly like another existing one it is considered a new Flow as it has another Id. Because of this, if you first create a Default flow and then push it out for all Jobs - then modify the Flow to, let say run other Notification, then push it out again to update all.
 
Each single flow in the **Job/Task flow** lists can be deleted and the list is immediately updated, in case the **Job Flow** or Task Flow windows are closed by the _OK_ button.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Settings/Add%20Job%20Flow%20to%20All%20Existing.png)