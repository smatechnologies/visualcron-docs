---
sidebar_label: 'Task IIS - Add Website Application'
hide_title: 'true'
---

## Task IIS - Add Website Application

The IIS - Add Website Application Task creates a new application under an existing website in Internet Information Services (IIS). An application is a logical grouping of web content accessible via a specific URL path within a site.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/IIS%20Tasks/Add%20a%20new%20application.png)

**Connection**

To use IIS Tasks you need to create a [Connection](../../global-connections) first. Click the *Settings* icon to open the *Manage Connections* dialog.

**Application parameters**

**Web site name**

The name of the parent website where the application will be created. Click the *Refresh* icon to populate the drop-down list with available websites.

**Application name**

The virtual path (alias) of the application within the website (e.g., /myapp).

**App pool name**

The name of the application pool to associate with this application.

**Enabled protocols**

A comma-separated list of protocols enabled for the application (e.g., http, https, net.tcp).

**Virtual directory parameters**

**Path**

The physical file system path of the application's root directory. Click the *Browse* button to select a folder.

**Logon method**

The authentication method IIS uses when accessing the physical path with the specified credential. Available options are:
- *Interactive* – Interactive logon session
- *Batch* – Batch logon session
- *Network* – Network logon (credentials passed over the network)
- *ClearText* – Clear text logon

**Credential**

The credential used to access the physical path. Select a Credential in the drop-down or click the *Settings* icon to open *Manage credentials* to add or edit Credentials.
