---
sidebar_label: 'Global - Connections'
hide_title: 'true'
---

## Global - Connections

Based on the nature of some Jobs, Tasks or Notifications, a Connection is an essential part of the settings for that entity. Connections are global which means they are centrally stored and can be accessed by related Tasks and Triggers. Connections are used to specify to where and how VisualCron should connect to various instances like FTP servers, SQL servers etc. If a password to a FTP server has changed you only need to updated that in the Connection - not every Task it is used in.
 
Connections are viewed and updated in the **Server > Global objects > Connection**s window. The connections may also be managed by _Add/Edit Job -> Tasks -> Add/Edit -> Task type._ Connections are global, thus if you change a connection definition, this will affect all entities using this connection.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Global%20-%20Connections.png)

The Manage Connections window displays the configured Connections in a grid with the following columns:

* **Address** — the host name, server, or address part of the Connection
* **Protocol type** — the protocol used by the Connection (FTP, SFTP, SQL, etc.)
* **Name** — the friendly name of the Connection
* **Port** — the port number (when applicable to the protocol)
* **Group** — optional Connection group used to organise the list

Connections can be grouped by the **Group** column (Outlook‑style collapsible groups). Use the **Search** text box in the toolbar to filter the list by Name, Address, or Group.

The toolbar provides the following buttons (left to right):

**Add**

A dropdown that opens a list of supported Connection protocols. Pick a protocol to open the editor for a new Connection of that type.

**Edit**

Open the selected Connection in the editor.

**Clone**

Create a copy of the selected Connection.

**Delete**

Delete the selected Connection.

**Explorer**

Many connections use some kind of explorer to test and navigate with the selected Connection, for example; [SQL Explorer](../tools/explore-sql-explorer), [Connection Explorer](../tools/explore-connection-explorer). Select a Connection and click on Explorer button.
 
**Audit log**

Click this button to view the [Audit log](../tools/objects-audit-log) for Connections.
 
**Clear filter**

When you open Manage Connections from a Task only the related protocols are visible. Click Clear filter to view all.

**Context menu**

Right‑clicking a Connection in the grid opens a context menu with the toolbar commands plus the following additional options:

* **Versions** — view the version history for the Connection
* **Object relations** — view other VisualCron objects (Jobs, Tasks, Triggers) that reference this Connection
* **Export** — export the selected Connection

Currently the following Connection protocols exist:
* [AMQP](connection-amqp)
* [Amazon](connection-amazon)
* [AS/400](connection-as400)
* [Box](connection-box)
* [Crystal reports](connection-crystalreports)
* [Dropbox](connection-dropbox)
* [Dynamics CRM](connection-dynamics-crm)
* [Exchange EWS](connection-exchange-ews)
* [Exchange WebDAV](connection-exchange-webdav)
* [Facebook](connection-facebook)
* [FTP](connection-ftp)
* [FTP SSL Implicit](connection-ftp)
* [FTP TLS Implicit](connection-ftp)
* [FTP SSL Explicit](connection-ftp)
* [FTP TLS Explicit](connection-ftp)
* [Google Cloud](connection-google-cloud)
* [Google Drive](connection-google-drive)
* [IBM Cognos Analytics](connection-ibm-cognos-analytics)
* [IIS](connection-iis)
* [IMAP](connection-imap4)
* [Informatica](connection-informatica)
* [Microsoft Azure](connection-microsoft-azure)
* [Office 365](connection-office365)
* [OneDrive](connection-onedrive)
* [PeopleSoft](connection-peoplesoft)
* [POP3](connection-pop3)
* [Pushbullet](connection-pushbullet)
* [SAP](connection-sap)
* [SCP](connection-scp)
* [SFTP](connection-sftp)
* [SharePoint](connection-sharepoint)
* [Slack](connection-slack)
* [SMTP](connection-smtp)
* [SQL](connection-sql)
* [SSH](connection-ssh)
* [SSRS](connection-ssrs)
* [TCP](connection-tcp)
* [Telegram](connection-telegram)
* [Telnet](connection-telnet)
* [Twitter](connection-twitter) (deprecated from VisualCron v13.2.1)
* [VisualCron](connection-visualcron)
* [VMWare](connection-vmware)
* [WebDAV](connection-webdav)
* [XendApp](connection-xendapp)
 
Click on protocol link above to read more information and connection setting specifics of that protocol.
