---
sidebar_label: 'Connection - IIS'
hide_title: 'true'
---

## Connection - IIS

The IIS Connection stores the account settings that these Tasks use when they manage Internet Information Services (IIS) on the VisualCron Server computer:

- [IIS - Add Website](job-tasks/iis-tasks/add-website)
- [IIS - Add Application Pool](job-tasks/iis-tasks/add-application-pool)
- [IIS - Add Website Application](job-tasks/iis-tasks/add-website-application)
- [IIS - Add App Virtual Directory](job-tasks/iis-tasks/add-app-virtual-directory)
- [IIS - Change Website State](job-tasks/iis-tasks/change-website-state)
- [IIS - Change Application Pool State](job-tasks/iis-tasks/change-application-pool-state)
- [IIS - Delete Website](job-tasks/iis-tasks/delete-website)
- [IIS - Delete Application Pool](job-tasks/iis-tasks/delete-application-pool)
- [IIS - Delete Website Application](job-tasks/iis-tasks/delete-website-application)
- [IIS - Delete App Virtual Directory](job-tasks/iis-tasks/delete-app-virtual-directory)
- [IIS - Is Application Pool Exists](job-tasks/iis-tasks/is-application-pool-exists)

:::warning

The IIS Tasks manage the IIS on the VisualCron Server computer, whatever *Address* contains. A Connection with the address of another computer still changes the websites and application pools on the Server computer. To manage IIS on another computer, run the Tasks on a VisualCron Server installed on that computer.

The Tasks make their changes to IIS as the account that the VisualCron Server service runs as, not as the _Username_ account; see [Main settings](#main-settings).

:::

### Common settings

![IIS Connection, Common settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IIS/IIS.png)

The ***Common settings*** tab is the same for every Connection type that has it; see [Common settings](global-connections#common-settings). IIS Connections have no *Test*, and the IIS Tasks do not use *Timeout* or *Code page*.

### Main settings

These fields are on ***Connection settings*** -> ***Main settings***.

![IIS Connection, Main settings tab, with Address, Username and Password](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IIS/Settings.png)

- _Address_: required, but the IIS Tasks do not use it. Enter "localhost"
- _Username_: required. The Windows account that an IIS Task signs in with while it runs. Windows applies this account only to access over the network, so the changes to IIS on the Server computer are made as the account that the VisualCron Server service runs as. That service account must be allowed to manage IIS on the Server computer
- _Password_: the password of the _Username_ account
