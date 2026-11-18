---
sidebar_label: 'Global - Connections'
hide_title: 'true'
---

## Global - Connections

A Connection stores where and how VisualCron connects to another system, for example an FTP server, a database or a cloud service: the address, the port, the sign-in and the protocol settings. Connections are global objects. You create a Connection once, and every Task and Trigger that needs it can use it. When a password or an address changes, change it in the Connection, and every Task and Trigger that uses the Connection uses the new value.

Connections have their own permissions, which control who can see, change and use them (see [Main - User Permissions](main-user-permissions)). Windows accounts that Tasks run as are stored as [Credentials](global-credentials), not as Connections.

### Manage Connections

To open the _Manage Connections_ window, click _Server_ -> _Global objects_ -> _Connections_. You can also open it from a Task or Trigger that uses a Connection. It then shows only the Connection types that the Task or Trigger can use.

![The Global objects group of the Server ribbon with Connections highlighted, and the Manage Connections window listing Connections by group, with names and addresses blurred](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Global%20-%20Connections.png)

The grid shows the type, name, address and port of each Connection, grouped by _Group_. To filter the list by name, address or group, type in the search box on the toolbar.

The toolbar has these commands:

- _Add_: opens the list of Connection types. Click a type to open the window for a new Connection of that type
- _Edit_: opens the selected Connection
- _Clone_: creates a copy of the selected Connection
- _Delete_: deletes the selected Connection. Before you delete a Connection, use _Object relations_ to see which Tasks and Triggers use it
- _Clear filter_: clears the search box and shows all Connection types again, for example after you opened _Manage Connections_ from a Task
- _Explorer_: opens the selected Connection in the [Connection Explorer](../tools/explore-connection-explorer), or an SQL Connection in the [SQL Explorer](../tools/explore-sql-explorer), so that you can browse the server from the Client computer
- _Audit log_: opens the [Audit log](../tools/objects-audit-log) for Connections

Right-click a Connection for the same commands and these:

- _Versions.._: the [version history](../tools/audit-log-versions) of the Connection
- _Object relations_: the Jobs, Tasks and Triggers that use the Connection (see [Object Relations](../tools/object-relations))
- _Export ..._: exports the selected Connection

### Add a Connection

To add a Connection, complete the following steps:

1. In _Manage Connections_, click _Add_.
2. Click the Connection type.
3. On the ***Common settings*** tab, enter a _Name_.
4. On the ***Connection settings*** tab, enter the settings for the type, as described on the page for that type.
5. (Optional) If the type has a _Test_ button on ***Common settings***, click _Test_.
6. Click _OK_.

The Connection is saved and is listed in _Manage Connections_ under its _Group_. Tasks and Triggers that use the type can now select it.

### Connection types

Connection types include:

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
* [FTP](connection-ftp), which also covers FTPS (FTP over SSL or TLS)
* [Google Cloud](connection-google-cloud)
* [Google Drive](connection-google-drive)
* [IBM Cognos Analytics](connection-ibm-cognos-analytics)
* [IIS](connection-iis)
* [IMAP4](connection-imap4)
* [Informatica](connection-informatica)
* [Microsoft Azure](connection-microsoft-azure)
* [Microsoft Graph API](connection-microsoft-graph-api)
* [Office365](connection-office365)
* [OneDrive](connection-onedrive)
* [PeopleSoft](connection-peoplesoft)
* [POP3](connection-pop3)
* [Pushbullet](connection-pushbullet)
* [SAP](connection-sap)
* [SCP](connection-scp)
* [SFTP (SSH - Secure Shell)](connection-sftp)
* [Sharepoint, Sharepoint Online and Sharepoint 2010](connection-sharepoint)
* [Slack](connection-slack)
* [SMTP](connection-smtp)
* [SQL](connection-sql)
* [SSH - Secure Shell](connection-ssh)
* [SSRS](connection-ssrs)
* [TCP](connection-tcp)
* [Telegram](connection-telegram)
* [Telnet](connection-telnet)
* [Twitter](connection-twitter) (deprecated from VisualCron v13.2.1)
* [VisualCron](connection-visualcron)
* [VMWare](connection-vmware)
* [WebDAV](connection-webdav)
* [XendApp](connection-xendapp)

### Common settings

Every Connection window has the same ***Common settings*** tab:

- _Protocol type_: the Connection type
- _Test_: shown for the types that support it. For most types, the Server, not the Client computer, connects with the values that are in the window now, including changes you have not saved, and reports success or the error. XendApp Connections are tested from the Client computer. VMWare Connections show _Test_, but report that the type is not supported for testing. Each type's page says what its test checks
- _Brute force test_: FTP and SFTP Connections only. Opens a tester on the Client computer that tries combinations of settings, such as encryption, port and proxy. Click _Select connection_ to copy a working combination into the Connection
- _Name_: required. Tasks and Triggers show this name when you choose a Connection. Telegram Connections show _Number_ here instead. On Twitter Connections, _Name_ is unavailable
- _Group_: the group that _Manage Connections_ lists the Connection under. Choose a group or type a new name. A new Connection is in "Default group"
- _Timeout_: in seconds. "60" on a new Connection, except SSH Connections, which start with "0". Each type's page says how the type uses it
- _Code page_: the character encoding for text exchanged with the server, where the type uses one. "windows-1252" on a new Connection
- _Permissions.._: overrides the Connection permissions of user groups for this Connection only, to grant or deny them access to it. Clicking _OK_ in the permissions window saves the Connection on the Server at once, and _Cancel_ in the Connection window does not undo that. For the permission model, see [Main - User Permissions](main-user-permissions)
- _Copy Connection Id_: the link at the bottom of the window. Copies the Connection's Id to the Clipboard

### Proxy

Many Connection types have a ***Proxy*** tab under ***Connection settings***. It is the same for every type that has it. Types without a ***Proxy*** tab, for example SCP, TCP, AS/400 and IIS, connect directly.

- _Proxy type_: "No proxy", "HTTP Proxy", "SOCKS4" or "SOCKS5". With "No proxy", the Connection connects directly and the other fields are unavailable
- _Address_: the host name or IP address of the proxy server. A new Connection shows a sample web address here; replace it
- _Port_: the port of the proxy server. "8080" on a new Connection
- _Test url_: the web address that _Test_ requests through the proxy
- _Authentication_: "Basic", "Digest", "NTLM" or "Not set". Available only with "HTTP Proxy". A new Connection has "Not set"
- _Use credentials_: send a user name and password to the proxy. Selected on a new Connection. While it is selected, _Username_ and _Password_ are required
- _Domain_: sent to the proxy only by Microsoft Azure Block blob Connections. The other types save it but do not send it
- _Username_ and _Password_: the account for the proxy server
- _Use proxy for data channel_: used only by FTP Connections, and shown when a proxy type is selected. When it is selected, which is the default, file transfers and folder listings also go through the proxy. Clear it to send them directly
- _Test_: the Client computer requests _Test url_ through the proxy with these settings and the proxy _Username_ and _Password_, and reports "Proxy is available" when the page loads. The test runs on the Client computer, not on the Server, so it does not show whether the Server can reach the proxy

Only FTP, SFTP, SSH and WebDAV Connections use _Authentication_. Amazon, Microsoft Azure Page blob, Google Drive and OneDrive Connections send the proxy _Username_ and _Password_ with Basic authentication when _Use credentials_ is selected, whatever _Authentication_ shows. Telnet Connections and the other types do not use _Authentication_.

Microsoft Azure Block blob Connections always use the proxy as an HTTP proxy, even when _Proxy type_ is "SOCKS4" or "SOCKS5". With _Use credentials_ selected, they send _Domain_, _Username_ and _Password_, and agree the authentication method with the proxy, whatever _Authentication_ shows.

:::warning

For FTP, SFTP and SSH Connections, when _Proxy type_ is "HTTP Proxy", _Authentication_ is "Not set" and _Use credentials_ is selected, the Server sends the Connection's own _Username_ and _Password_, the sign-in for the FTP, SFTP or SSH server, to the proxy with Basic authentication. It does not send the proxy _Username_ and _Password_. A new Connection has these settings as soon as you choose "HTTP Proxy", and _Test_ on this tab does not show the problem, because it uses the proxy account. To send the proxy account, set _Authentication_ to "Basic", "Digest" or "NTLM".

:::

:::warning

Some Connections show a ***Proxy*** tab that the Server does not apply. In these cases the Server connects directly, so make sure that it can reach the server without a proxy, or the Jobs fail:

- Box, Dropbox and Slack Connections
- Microsoft Azure Connections with the "Form Recognizer" _Connection type_
- Office365 Connections
- SMTP Connections
- Exchange EWS, Exchange WebDAV and Microsoft Graph API Connections, when the Server sends email, for example from the [Email - Send](job-tasks/messaging-tasks/email) Task, and when you click _Test_. The Email Tasks that read, delete or move messages, and the Email Trigger, use the ***Proxy*** tab
- VisualCron Connections

:::
