---
sidebar_label: 'Starting VisualCron Client'
hide_title: 'true'
---

## Starting VisualCron Client

This page explains how to start the VisualCron Client and what it needs to connect. If VisualCron is not installed yet, see [Download, Install, Upgrade and Uninstall](../get-visualcron/download-install-upgrade-uninstall).

Start the Client in one of these ways:

- Double-click the desktop shortcut "VisualCron `<major version>`"
- In the Windows Start menu, open the folder "VisualCron `<major version>`" and select "VisualCron Client `<major version>`"
- Double-click the [Tray Client](visualcron-tray-client) icon, or right-click it and select _Client_ -> _Start_

The Client can connect only while the VisualCron service (named "VisualCron" in Windows Services) is running. It connects whether the Server status is "On" or "Off". See [Login](login) for what happens when the Client connects.

Because the Server runs as a service, you can close the Client without affecting the Jobs the Server runs.