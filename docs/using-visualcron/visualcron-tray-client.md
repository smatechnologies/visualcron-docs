---
sidebar_label: 'VisualCron Tray Client'
hide_title: 'true'
---

## VisualCron Tray Client

This page explains what the VisualCron Tray Client does, how to read its icon, and what its menu and settings do.

The VisualCron Tray Client is a small application that shows a VisualCron icon in the Windows notification area, normally at the lower right of the screen. If you cannot see the icon, click the arrow that shows hidden icons. Right-click the icon to open its menu.

![The Windows notification area with hidden icons shown and the VisualCron Tray Client icon highlighted, with the tooltip VisualCron Tray Client](../../static/img/Using%20VisualCron/Interacting%20with%20VisualCron/Tray%20Client.png)

### Startup and connection

By default, the Tray Client starts when a user logs on to Windows (see _Start Tray Client on startup_ under [Settings](#settings)). It connects only to the VisualCron Server on the same computer. This lets it control the Server, run Tasks in the foreground and show notifications to the logged-on user.

The icon shows the connection state:

- Yellow VisualCron icon: connected to the Server
- Red VisualCron icon: not connected, for example because the VisualCron service (named "VisualCron" in Windows Services) is stopped, disabled or not installed

While it is not connected, the Tray Client tries to connect again every 30 seconds. After the service starts, the icon can take up to about 30 seconds to turn yellow again.

### Menu commands

![The Tray Client menu with the commands Settings, Client, Server and Exit](../../static/img/Using%20VisualCron/Interacting%20with%20VisualCron/Tray%20Client%20Features.png)

Double-click the Tray Client icon to start the VisualCron Client. Right-click the icon for these commands:

- _Settings_: opens the Tray Client settings (see [Settings](#settings))
- _Client_ -> _Start_: starts the VisualCron Client
- _Client_ -> _Open log folder_: opens the Client's log folder
- _Server_: the first line shows the Server status, "Server on", "Server off" or "Not connected"
- _Server_ -> _Start_ and _Server_ -> _Stop_: switch the Server "On" or "Off" (see [Main - Server On/Off](../client-user-interface/server/server-on-off)); available only while the Tray Client is connected
- _Server_ -> _Service_: the first line shows the status of the VisualCron service
- _Server_ -> _Service_ -> _Start_ and _Stop_: start or stop the VisualCron service. If this fails, for example because the Tray Client does not have the rights to control services, no message is shown. The status line keeps the old status, and the error is written to the Tray Client log
- _Server_ -> _Open log folder_ and _Server_ -> _Open settings folder_: open the Server's log and settings folders
- _Exit_: closes the Tray Client

:::note

_Server_ -> _Stop_ switches the Server "Off" but leaves the service running. Jobs that are already running continue, and Event Triggers with _Ignore Server Off (always run)_ checked still start their Jobs. The "Off" status is kept when the service or the computer restarts. _Server_ -> _Service_ -> _Stop_ stops the VisualCron service, and no Jobs run until it is started again.

:::

### Foreground execution

One of the main purposes of the Tray Client is to run Tasks in the logged-on user's desktop session. See [foreground execution](../client-user-interface/server/task-main-settings-execution-context).

### Settings

Right-click the Tray Client icon and select _Settings_. Click _OK_ to save your changes.

#### Main tab

_Start Tray Client on startup_

When checked, the Tray Client starts each time any user logs on to this computer. The installer turns this setting on. The setting applies to all users of the computer, so the Tray Client can show and change it only when it runs with administrator rights. Without them, the checkbox always shows as cleared, even when the Tray Client is set to start at logon, and changes are not saved.

The Client has a setting with the same name in [Settings - Client Settings](../client-user-interface/file/client-settings). It controls the same setting for all users.

_Server settings folder_

The folder where the Server keeps its settings. The Server reads this location when the VisualCron service starts. The field is filled only when the Tray Client runs with administrator rights. Click _Open_ to open the folder, or use _Server_ -> _Open settings folder_ in the Tray Client menu.

#### Notifications tab

Select which Client events you want popups for. The Tray Client shows a popup when a selected event occurs.

#### Log tab

_Log to file_

The setting is saved, but the Tray Client currently writes its log file whether or not it is checked.