---
sidebar_label: 'MFT Server'
hide_title: 'true'
---

## Servers - MFT Server

In the main menu Server > Servers > MFT the MFT Server settings are managed.
 
The MFT Server provides built in support for hosting, inside VisualCron, for the following server types:

* SFTP
* FTP
 
The advantages of using VisualCron for this are:

* You are not dependent on any second installation of a third party server.
* VisualCron can react faster to any changes within the server through the MFT Trigger. The MFT Trigger can react on various events like file uploaded, download, folder created etc
* Through the Web Client, VisualCron users can manage the files (delete, upload, download)
 
**Main > Servers > MFT Server**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/MFT.png)

**Allow MFT**

Starts all predefined sub MFT servers (FTP, SFTP etc) at startup when this is checked.
 
**Change server state**

Turns on and of the selected MFT server.
 
**MFT Servers list**

This is the list of existing MFT servers (of any type).
 
Upon pressing the Add Servers icon, the Server settings dialog is opened.
 
**Main > Servers > MFT Server > Servers > Server settings** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/MFT%20Settings.png)

**Server name**

The name of the MFT server.
 
**Server type**

Select MFT server type.
 
**Permissions**

The permissions grid controls who can access the specific MFT server. Click add to add new permission or double click/Edit to edit a permission.

**Main > Servers > MFT Server > Servers > SFTP Endpoints** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/MFT%20Endpoint.png)

**SFTP Endpoints list**

An endpoint is a combination of IP and port the specific MFT server listens to. Click add to add a new MFT server.
 
**SFTP Endpoint**

**Name**

Optional name for the Endpoint for easier identification.
 
**IP**

The IP the Endpoint should listen too. 0.0.0.0 are all IPs on the network card.
 
**Port**

The port to use for the Endpoint. Default 22 for SFTP server.
 
**Force compression**

This property specifies whether the non-compressed transfer is supported by the server. When the property is set to true, CompressionAlgorithms[SSH_CA_NONE] is turned off and the server advertises only ZLIB compression (and not NONE).
 
**Use UTF8**

Text ...
 
**Root folder**

Base folder for the Endpoint files.
 
**Default Credential**

The Credential that should be used for accessing root folder (is needed on network drives).
 
**Session timeout**

Timeout for the session in milliseconds. If this property value is 0, the operation will expire after system-default timeout (which is 2 hrs 8 min for TCP stack).
 
**Allow password authentication**

If the user should be allowed to authenticate with his/her password.
 
**Allow public-key authentication**

If the user should be allowed to authenticate with his/her private key.
 
**Allow keyboard-interactive authentication**

If the user should be allowed to authenticate with keyboard-interactive authentication.
 
**The user must authenticate using ANY of the above methods**

Any of the allowed must be used for authentication.
 
**The user must authenticate using ALL of the above methods**

All allowed must be used for authentication.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/FTP%20Settings.png)

**Name**

Optional name for the Endpoint for easier identification.
 
**IP**

The IP the Endpoint should listen too. 0.0.0.0 are all IPs on the network card.
 
**Port**

The port to use for the Endpoint. Default 21 for FTP server.
 
**Root folder**

Base folder for the Endpoint files.
 
**Default Credential**

The Credential that should be used for accessing root folder (is needed on network drives).
 
**Passive mode IP**

The IP used for passive mode.
 
**Use UTF8**

When checked UTF8 will be used for communication if available.
 
**Session timeout**

Timeout for the session in milliseconds. If this property value is 0, the operation will expire after system-default timeout (which is 2 hrs 8 min for TCP stack).
 
**Outgoing speed limit**

Speed in bytes per second for outgoing traffic. Default 0 is unlimited speed.
 
**Incoming speed limit**

Speed in bytes per second for incoming traffic. Default 0 is unlimited speed.
 
**FTP Endpoint->Additional settings**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/FTP%20Settings.png)

**X509 certificates**

If you select TLS or SSL for security of the FTP endpoint you can optionally
 
**Use passive mode**

FTP is a TCP based service exclusively. There is no UDP component to FTP. FTP is an unusual service in that it utilizes two ports, a 'data' port and a 'command' port (also known as the control port). Traditionally these are port 21 for the command port and port 20 for the data port. The confusion begins however, when we find that depending on the mode, the data port is not always on port 20. In order to resolve the issue of the server initiating the connection to the client a different method for FTP connections was developed. This was known as passive mode, or PASV, after the command used by the client to tell the server it is in passive mode.
 
**Passive mode host**

Enter IP or DNS name for resolving IP for passive mode or check Use default host for using the current IP of the server.
 
**Use default host**

Use the current IP of the server.
 
**Use custom port range**

Enter any port range for incoming Passive connections. If not checked - random ports will be used.
 
**Main > Settings > MFT Server > Users** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/Users.png)

**Users list**

This is the list of MFT users. A MFT user can be linked to an existing VC user or be specific for MFT server only.
 
Upon pressing the Add Users icon, the User settings dialog is opened.
 
**Main > Settings > MFT Server > Users > Main settings** sub tab

**Link to VC User**

It is possible to link a VC user to a MFT user or use a specific user account just for MFT. When link is selected it will be using the username and password for the specific VC user.
 
**Login**

Unless linked to VC user you enter the username here.
 
**Password**

Unless linked to VC user you enter the password here.
 
**Show password**

Shows the entered password.
 
**Name**

Unless linked to VC user you enter the name here.
 
**Email**

Unless linked to VC user you enter the email here.
 
**Main > Settings > MFT Server > Users > Options** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/User%20Options.png)

**Base folder**

Startup folder for the user.
 
**Credentials**

To control a remote computer you may need to use a [Credential](../server/global-credentials). The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the Settings icon to open Manage credentials in order to add or edit Credentials.
 
**Outgoing speed limit**

These are the maximum number of bytes per second for outgoing transfer. 0 is unlimited.
 
**Incoming speed limit**

These are the maximum number of bytes per second for incoming transfer. 0 is unlimited.
 
**Private key**

The private key used for the connection
 
**Private key password**

The private key password used for the connection.
 
**Test key**

Text ...
 
**Main > Settings > MFT Server > Users > Permissions** sub tab