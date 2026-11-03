---
sidebar_label: 'Main - Client Connections'
hide_title: 'true'
---

## Main - Client Connections 

The _Server connections manager_ window lists every Client that is connected to the Server you are working with. Use it to see who is connected, from which computer and with which kind of Client.

To open it, click the main menu _Server_ -> _Main settings_ -> _Client connections_. You need the "Client connections" permission with "Read" (see [Main - User Permissions](main-user-permissions)).

The list updates while the window is open: new connections are added, and closed connections disappear. The list is read only, and you cannot disconnect a Client from this window. A Client and a Tray Client that run for the same user each appear as their own row.

_Server_ -> _Main settings_ -> _Client connections_

![Server connections manager window listing two connections, a Windows Client and a Tray Client, with the columns Name, Windows User, SID, Client Type, Date and Address](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Main%20Client%20Connections/Client%20Connections.png)

### Columns

| Column | Shows |
| ------ | ----- |
| _Name_ | The VisualCron user of the connection |
| _Windows User_ | The Windows account that made the connection |
| _SID_ | The Windows session the Client process runs in |
| _Client Type_ | The kind of Client: "Windows Client", "Tray Client", "Web Client", "WebAPI Client", "API", "Server Job/Trigger", "Server Sync", "Cloud Client" or "Server Agent" |
| _Date_ | When the connection was made |
| _Address_ | The address the Client connects from, or "IPC (local)" for a Client connected through a local IPC connection |

