---
sidebar_label: 'Settings - Web Client'
hide_title: 'true'
---

## Settings - Web Client

The **_Web Client_** tab installs and removes the VisualCron Web Client in IIS or IIS Express, and turns Windows authentication on or off for it. The tab works on the computer where the Client runs, whichever Server the Client is connected to. This tab is one of the tabs of the Server settings window (see [Main - Settings](main-settings)). For the full installation steps and the requirements, see [Installation of Web Client](../../using-visualcron/installation-of-web-client). To learn what the Web Client does, see [VisualCron Web Client](../../using-visualcron/visualcron-web-client).

_Server_ -> _Main settings_ -> _Settings_ -> **_Web Client_** tab

![The Web Client tab of the Server settings, with the Web Client information box and the IIS and IIS Express boxes; in the IIS box the Web Client is installed on port 9000 with Windows authentication enabled](../../../static/img/Using%20VisualCron/Interacting%20with%20VisualCron/WebClient%20Install.png)

The _IIS_ box and the _IIS Express_ box each show _IIS installed_, _Web Client installed_, _Port_, _Link_, _Source path_ and _Windows authentication_, with these buttons:

- _Install_: installs the Web Client in that web server on the _Port_ you enter. The default port is "9000"; you can enter 5 to 65535. If the web server is not installed, VisualCron tries to install it; if it cannot, it shows a message, which in some cases offers to open a download page
- _Uninstall_: removes the Web Client website from that web server
- _Enable_ or _Disable_: turns Windows authentication on or off for the Web Client website. The button shows _Enable_ while it is off and _Disable_ while it is on

To install the Web Client, run the Client as administrator on the Server computer and connect to the Server locally. See [Fields and buttons on the Web Client tab](../../using-visualcron/installation-of-web-client#fields-and-buttons-on-the-web-client-tab).

:::note

These buttons act at once, without _Apply settings_, and _Cancel_ does not undo them. _Uninstall_ does not ask you to confirm.

:::
