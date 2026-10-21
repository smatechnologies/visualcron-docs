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

### Which account authenticates the mapping

The mapping is performed by the VisualCron Server service itself. It is not performed inside a Task's execution context, so the account that the service runs under matters:

* When a Credential is selected on the drive entry, those credentials are used to authenticate against the share.
* When the Credential field is left empty, no credentials are sent and the connection is made using the service's own identity. Under the default SYSTEM account that is the computer account of the VisualCron host, which most file shares do not grant any access to.

Because Windows keeps mapped drive letters per logon session, a drive mapped by one account is not visible to another. If a drive mapping fails while a Task using the same Credential can reach the same share through a UNC path, running the VisualCron service under a domain account that has access to the share has resolved this in practice. See [Credentials](../server/global-credentials) for the available account options.

### Authentication protocol

VisualCron does not select an authentication protocol for network shares. The credentials are passed to Windows, and Windows negotiates Kerberos or NTLM on its own. There is no setting in VisualCron that prefers, forces, or falls back to either protocol, and VisualCron does not record which protocol was used. It logs only whether the mapping or file access succeeded.

To confirm which protocol Windows used, check the Windows event logs:

* On the file server, Security event ID **4624**. The *Authentication Package* field names the protocol, and the *Package Name (NTLM only)* field is populated only when NTLM was used.
* On a domain controller, event IDs **4768** and **4769** indicate Kerberos, while event ID **4776** indicates NTLM.

If NTLM has been disabled at the operating system or domain level, VisualCron cannot use NTLM on its own, as it has no separate NTLM implementation for network drives. Windows will either use Kerberos or the connection will fail.
 
### Troubleshooting

*A specified logon session does not exist*
 
Try disabling this policy:

![](../../../static/img/clipsdfgdfsggfd0069.png)

![](../../../static/img/clip00dfgdfg69.png)

*The specified network password is not correct*

Double check so that date and time is matching (synced) between VisualCron and server of remote share.

*The network path was not found* / *The network name cannot be found*

These are name resolution or share name errors rather than authentication failures. A rejected logon reports incorrect credentials or access denied instead. Confirm from the VisualCron host that the server name resolves and that the share is reachable. Also check that the Path is a plain UNC path with no scheme prefix such as ```http://``` in front of it, and that the share name is spelled correctly.
 
*Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again.*

Windows allows only one set of credentials per remote server per logon session. A connection to that server already exists under a different user. Disconnect it on the VisualCron host before mapping again.
 
*Access denied trying to connect to IFS (AS400) share*

Local Security Policy -> Local Policies –> Security Options -> Change Network security: LAN Manager authentication level to NTLMv2 session security if negotiated
[http://e1tips.com/2010/05/18/windows-vista-windows-7-ibm-iseries-ifs-mapped-drive/](http://e1tips.com/2010/05/18/windows-vista-windows-7-ibm-iseries-ifs-mapped-drive/)
