---
sidebar_label: 'Global - Connections'
hide_title: 'true'
---

## Global - Connections

Based on the nature of some Jobs, Tasks or Notifications, a Connection is an essential part of the settings for that entity. Connections are global which means they are centrally stored and can be accessed by related Tasks and Triggers. Connections are used to specify to where and how VisualCron should connect to various instances like FTP servers, SQL servers etc. If a password to a FTP server has changed you only need to updated that in the Connection - not every Task it is used in.
 
Connections are viewed and updated in the **Server > Global objects > Connection**s window. The connections may also be managed by _Add/Edit Job -> Tasks -> Add/Edit -> Task type._ Connections are global, thus if you change a connection definition, this will affect all entities using this connection.

![](../../../static/img/globalconnections.png)

**Explorer**

Many connections use some kind of explorer to test and navigate with the selected Connection, for example; [SQL Explorer](sqlexplorer), [Connection Explorer](connectionexplorer). Select a Connection and click on Explorer button.
 
**Audit log**

Click this button to view the [Audit log](auditlog) for Connections.
 
**Clear filter**

When you open Manage Connections from a Task only the related protocols are visible. Click Clear filter to view all.

Currently the following Connection protocols exist:
* [FTP](ftp)
* [FTP SSL Implicit](ftpsslimplicit)
* [FTP TLS Implicit](ftptlsimplicit)
* [FTP SSL Explicit](ftpsslexplicit)
* [FTP TLS Explicit](ftptlsexplicit)
* [SFTP](sftp)
* [SCP](scp)
* [SSH](ssh)
* [TCP](tcp)
* [SMTP](smtp)
* [POP3](pop3)
* [IMAP](imap)
* [Exchange EWS](exchangeews)
* [Exchange WebDAV](exchangewebdav)
* [WebDAV](webdav)
* [SQL](sql)
* [SSRS](ssrs)
* [Amazon](amazon)
* [Microsoft Azure](microsoftazure)
* [Dropbox](dropbox)
* [Google Drive](googledrive)
* [OneDrive](onedrive)
* [Box](box)
* [VisualCron](visualcron)
* [SharePoint](sharepoint)
* [XendApp](xendapp)
* [Pushbullet](pushbullet)
* [Telegram](telegram)
* [Twitter](twitter)
* [Crystal reports](crystalreports)
* [VMWare](vmware)
* [Dynamics CRM](dynamicscrm)
* [AS/400](as400)
* [SAP](sap)
 
Click on protocol link above to read more information and connection setting specifics of that protocol.