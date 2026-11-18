---
sidebar_label: 'VisualCron Server'
hide_title: 'true'
---

## VisualCron Server

This page explains what the VisualCron Server is, its "On" and "Off" status, and the network port it uses. For supported systems, see [Requirements](../requirements).

The VisualCron Server runs in the background as the VisualCron service (named "VisualCron" in Windows Services). The service is installed with startup type Automatic. It starts with Windows and keeps running when nobody is logged on and no Client is connected. If you choose the installation type _VisualCron Client only_, the service is installed but disabled.

### Server On and Off

Besides the service, the Server has a status, "On" or "Off". The status is "On" the first time the Server starts. After that, the Server keeps the status you last set, also when the service or the computer restarts.

When the Server is "On", Triggers start Jobs as usual.

When the Server is "Off":

- Time Triggers do not start Jobs, and _Next run_ shows "Server off"
- Event Triggers are inactive, except those with _Ignore Server Off (always run)_ checked, which still start their Jobs
- Jobs with _Run missed Job once at start_ checked do not make up missed runs when the service starts
- Jobs that are already running keep running, and their Flow can still start other Jobs
- You can still run Jobs and Tasks manually, from the Client or by other means such as the Web Client

:::warning

"Off" is not a full stop. Jobs that are already running continue, and Event Triggers with _Ignore Server Off (always run)_ checked still start their Jobs. Check those Triggers before you switch the Server "Off" for maintenance. The "Off" status is kept when the service or the computer restarts, so switch the Server "On" again when you are done.

:::

See [Main - Server On/Off](../client-user-interface/server/server-on-off).

### Which Server the Client shows

The Client shows the Server it is connected to in the **_Server [`<server name>`]_** ribbon tab, in the user and server row at the top of the Job grid, and in the status bar. To add or change server connections, see [Servers - Manage Servers](../client-user-interface/file/manage-servers).

### Port and firewall

Clients on other computers connect to the Server on TCP port "16444" by default. The Tray Client, and the connection that the Client creates to the Server on its own computer (see [Login](login)), use a local connection that does not go through this port. You can change the port in _Server_ -> _Main settings_ -> _Settings_ -> **_Main settings_** tab -> _Server port_. See [Main - Settings](../client-user-interface/server/main-settings).

VisualCron does not open the port in Windows Firewall during installation or when the service starts. Next to _Server port_ there is a button that shows whether VisualCron's own inbound rule for the port exists: _Firewall allows_ when it does, _Firewall denies_ when it does not. The button looks only for the rule that VisualCron creates. A rule you created yourself under another name is not detected, and the button then shows _Firewall denies_ even when the port is open.

To allow remote Clients through Windows Firewall, complete the following steps:

1. Click _Server_ -> _Main settings_ -> _Settings_.
2. Open the **_Main settings_** tab.
3. If the button next to _Server port_ shows _Firewall denies_, click it.

The button changes to _Firewall allows_. To remove the rule again, click the button while it shows _Firewall allows_. It changes back to _Firewall denies_.

If you save a new _Server port_ while the button shows _Firewall allows_, VisualCron moves its rule to the new port. If it cannot create the new rule, it keeps the rule for the old port.

Hardware firewalls and third-party firewall software are not changed. Open the port in those yourself. Remote Clients also cannot connect while _Only allow local connections_ is checked on the **_Users/Logon_** tab of the same window. See [Settings - Users/Logon](../client-user-interface/server/settings-users-logon).
