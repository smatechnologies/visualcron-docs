---
sidebar_label: 'IIS Tasks'
hide_title: 'true'
---

## IIS Tasks

Internet Information Services (IIS) is the web server of Windows. The IIS Tasks manage the websites, application pools, applications and virtual directories of the IIS on the VisualCron Server computer.

:::warning

The IIS Tasks always work on the IIS of the VisualCron Server computer. They need an IIS Connection, but they do not use its _Address_: a Connection with the address of another computer still changes the IIS on the Server computer. The changes are made as the account of the VisualCron Server service, which must be allowed to change IIS; the Connection's _Username_ and _Password_ are used only for network access. To manage IIS on another computer, run the Tasks on a VisualCron Server installed on that computer. See [Connection - IIS](../../connection-iis.md).

:::

The IIS Tasks are:

- [IIS - Add Website](add-website.md)
- [IIS - Add Application Pool](add-application-pool.md)
- [IIS - Add Website Application](add-website-application.md)
- [IIS - Add App Virtual Directory](add-app-virtual-directory.md)
- [IIS - Change Website State](change-website-state.md)
- [IIS - Change Application Pool State](change-application-pool-state.md)
- [IIS - Delete Website](delete-website.md)
- [IIS - Delete Application Pool](delete-application-pool.md)
- [IIS - Delete Website Application](delete-website-application.md)
- [IIS - Delete App Virtual Directory](delete-app-virtual-directory.md)
- [IIS - Is Application Pool Exists](is-application-pool-exists.md)

Most IIS Tasks do nothing, with no error, when the object they work on is not found or already exists, and the Task reports success. Each Task page says when this happens. To have a Job notice it, add an ***On error*** condition that raises an error when the Task output is not the expected result, for example "Success"; see [Task - On Error](../../task-on-error.md).

The ***TimeOut*** tab does not stop the IIS Tasks.
