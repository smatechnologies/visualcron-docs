---
sidebar_label: 'Task IIS - Delete Website Application'
hide_title: 'true'
---

## Task IIS - Delete Website Application

The IIS - Delete Website Application Task removes an application from a website, in the IIS of the VisualCron Server computer, using an IIS Connection.

![IIS - Delete an existing application Task settings, with the Connection field and the Site name and Application name fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/delete%20an%20existing%20application.png)

:::warning

This Task uses an IIS Connection; see [Connection - IIS](../../connection-iis). The Task always works on the IIS of the VisualCron Server computer: the Connection's _Address_ is not used, and the changes are made as the account of the VisualCron Server service, which must be allowed to change IIS. The Connection's _Username_ and _Password_ are used only for network access.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### IIS - Delete an existing application tab

The names below are matched without regard to case.

- _Connection_: the IIS Connection. Required. Click the _Settings_ icon to open _Manage Connections_
- _Site name_ (_Web site name_ group): the name of the website. Required. Click the _Refresh_ icon to list the websites of the VisualCron Server computer
- _Application name_: the path of the application to remove, for example "/myapp". Required. Click the _Refresh_ icon to list the applications of the website

:::warning

The Task removes the application from the website without a prompt. VisualCron cannot undo it.

:::

### Output and errors

On success, the output is "Success". When the website or the application is not found, the Task does nothing and writes no output, and the Task reports success.

The ***TimeOut*** tab does not stop this Task.
