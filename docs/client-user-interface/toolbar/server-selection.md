---
sidebar_label: 'Server Selection'
hide_title: 'true'
---
## Server Selection

The Server selection combo box at the left of the toolbar lists the Server connections added in ***File*** -> ***Servers*** -> ***Manage Servers***. Select a Server to make it the current Server. If it is not connected yet, click ***Connect*** to the right of the combo box. While the Client connects, the combo box and ***Connect*** are unavailable. The login window opens only if the connection has _Prompt for login_ checked or, for an Active Directory logon, when the Server no longer accepts the saved logon; otherwise the user name and password saved in the connection are used, so you do not have to enter the password each time. See [Servers - Manage Servers](../file/manage-servers) and [Login](../../using-visualcron/login).

The connected Server is shown in the combo box and on the main menu ***Server*** tab, as `Server [<server name>]`. The progress bar on the right of the status bar shows the progress of the connection; when it is full, all data has been loaded.

:::info

The Client can be connected to several Servers at the same time. Each connected Server has its own row in the Job grid, with its Jobs below it. Commands and settings in the ribbon apply to the current Server: the one selected in the combo box and shown on the ***Server*** tab.

:::
