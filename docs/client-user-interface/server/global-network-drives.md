---
sidebar_label: 'Global - Network Drives'
hide_title: 'true'
---

## Global - Network Drives

VisualCron is by default running as the SYSTEM account. One problem you may face is that you can't see/access your network drives. This is a restriction in Windows - that network drives are not shared between accounts.
 
To handle this, a way to control network drives from the system account is implemented. This enables map/disconnect network drives directly from VisualCron.
 
In the main menu, click on **Server > Global objects > Network drives** to access the interface for mapping/disconnecting.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Network%20Drives/Network%20Drives.png)

The Network Drives window displays the configured drives in a grid with the following columns:

* **Drive** — the assigned drive letter (A: – Z:)
* **Path** — the UNC path the drive is mapped to
* **Connection status** — an icon indicating whether the drive is currently connected
* **Controlled** — whether the drive is managed by VisualCron (re‑mapped automatically on startup)
* **Credential** — the [Credential](../server/global-credentials) used to authenticate when mapping the drive

The toolbar above the grid provides the following buttons:

* **Map drive** — opens the Map drive dialog described below
* **Unmap drive** — disconnects the selected drive
* **Refresh** — reloads the list of network drives from the Server
* **Reconnect** — reconnects all drives that have been disconnected during the current VisualCron session
* **Audit log** — opens the [Audit log](../tools/objects-audit-log) for network drives

Right‑clicking a row opens a context menu with **Map drive**, **Unmap drive**, **Audit log**, and **Versions** (view the version history of the network drive entry).

**Map drive**

When mapping a drive you need to specify a Credential, a user that has access to the network drives, that is either a domain user or a user on the remote server. Specify a wanted drive name and path.
Path should be entered in UNC format like this: ```"\\servernameORip\folder\"```

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Network%20Drives/Map%20Network%20Drives.png)

The Map drive dialog contains the following fields:

* **Credential** — pick the [Credential](../server/global-credentials) used to authenticate against the network share
* **Drive** — a dropdown of drive letters (A: – Z:) to assign to the mapped path
* **Path** — the UNC path that the drive letter should be mapped to. Click the browse button next to the field to pick a folder

Click on *Map drive* at the bottom of the dialog to map it. It is now controlled by VisualCron and each time VisualCron is started it tries to re-map the drives so these can be accessed after a server reboot.
 
**Reconnect**

If a drive has been disconnected during a VisualCron session you can reconnect it here.
 
### Troubleshooting

A specified logon session does not exist
 
Try disabling this policy:

![](../../../static/img/clipsdfgdfsggfd0069.png)

![](../../../static/img/clip00dfgdfg69.png)

*The specified network password is not correct*

Double check so that date and time is matching (synced) between VisualCron and server of remote share.
 
*Multiple connections to a server or shared resoource from the same user using multiple usernames are not allowed. Disconnect all previous verbands to the server or shared resource and try again.*

Try using the IP instead of the DNS name to the server.
 
*Access denied trying to connect to IFS (AS400) share*

Local Security Policy -> Local Policies –> Security Options -> Change Network security: LAN Manager authentication level to NTLMv2 session security if negotiated
[http://e1tips.com/2010/05/18/windows-vista-windows-7-ibm-iseries-ifs-mapped-drive/](http://e1tips.com/2010/05/18/windows-vista-windows-7-ibm-iseries-ifs-mapped-drive/)
