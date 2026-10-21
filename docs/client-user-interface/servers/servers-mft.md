---
sidebar_label: 'MFT Server'
hide_title: 'true'
---

## Servers - MFT Server

In the main menu Servers > Managed File Transfer (MFT) the MFT Server settings are managed.
 
The MFT Server provides built in support for hosting, inside VisualCron, for the following server types:

* SFTP
* SFTPAdvanced
* FTP
 
The advantages of using VisualCron for this are:

* You are not dependent on any second installation of a third party server.
* VisualCron can react faster to any changes within the server through the MFT Trigger. The MFT Trigger can react on various events like file uploaded, download, folder created etc
* Through the Web Client, VisualCron users can manage the files (delete, upload, download)

:::note Server type is selected when the server is created

The Server type list can only be changed while the MFT server is being added. When you edit an existing MFT server the list is read only, and only the endpoint sub tab that matches the type is displayed.

Selection of encryption, key exchange, MAC and public key algorithms is only available on the SFTPAdvanced server type. If you need to control the algorithm list of an existing SFTP server, add a new MFT server of type SFTPAdvanced instead.

:::
 
**Main > Servers > MFT Server**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/MFT.png)

**Allow MFT**

Starts all predefined sub MFT servers (FTP, SFTP etc) at startup when this is checked.
 
**MFT settings**

The MFT settings area is divided into two sub tabs. **Servers** lists the hosted MFT servers and **Users** lists the accounts that connect to them.
 
**MFT Servers list**

This is the list of existing MFT servers (of any type). The grid displays the following columns: **Server name**, **Ports**, **Type**, **State**, **Connections**, and **Status**.

The toolbar provides the following actions: **Add**, **Edit**, **Delete**, **Activate/Deactivate Server**, **Run/Stop Server**, and **Log history**. Right click a server in the list for the same log history action and for exporting the server definition.

**Apply settings**

Saves all changes made in the MFT Settings dialog. Closing with Cancel discards them.
 
Upon pressing the Add Servers icon, the Server settings dialog is opened.
 
**Main > Servers > MFT Server > Servers > Server settings** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/MFT%20Settings.png)

**Server name**

The name of the MFT server.
 
**Server type**

Select MFT server type. The available types are **SFTP**, **SFTPAdvanced** and **FTP**. The selection controls which endpoint sub tab is shown next to Server settings:

* _SFTP_ - the **SFTP Endpoints** sub tab
* _SFTPAdvanced_ - the **Advanced SFTP Endpoints** sub tab
* _FTP_ - the **FTP Endpoints** sub tab
 
**Permissions**

The permissions grid controls who can access the specific MFT server. Click add to add new permission or double click/Edit to edit a permission. The toolbar provides **Add**, **Edit** and **Delete** actions.

**Permission dialog**

**Server**

The MFT server the permission applies to. Click the add icon next to the list to create a new MFT server.

**User**

The MFT user the permission applies to. Click the add icon next to the list to create a new MFT user. Both a server and a user must be selected before the permission can be saved.

**Allow Access**

When checked, the selected user is allowed to connect to the selected server. Uncheck to deny access without removing the permission.

**Base folder**

Startup folder for the user on this server. Use the folder browser button to select a folder.

**Main > Servers > MFT Server > Servers > SFTP Endpoints** sub tab

This sub tab is shown for MFT servers of type SFTP.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/MFT%20Endpoint.png)

**SFTP Endpoints list**

An endpoint is a combination of IP and port the specific MFT server listens to. The grid displays the following columns: **Name**, **IP**, **Security type** and **Port**. The toolbar provides **Add**, **Edit**, **Delete** and **Log** actions. Click add to add a new endpoint.
 
**SFTP Endpoint > Main settings**

**Name**

Optional name for the Endpoint for easier identification. A name must be entered before the endpoint can be saved.
 
**IP**

The IP the Endpoint should listen too. 0.0.0.0 are all IPs on the network card.
 
**Port**

The port to use for the Endpoint. Default 22 for SFTP server. Next to the port the current state of the port is displayed, showing whether Windows Firewall allows the port and whether the port is already used by another process.
 
**Firewall allows**

Click to allow or deny the entered port in Windows Firewall. The state next to the button changes between Allowed and Denied.
 
**Force compression**

When checked, all data transfers must be compressed. The server does not offer uncompressed transfer, so connecting clients have to compress data. This lowers bandwidth usage but increases CPU usage on both server and client.
 
**Use UTF8**

When checked, UTF-8 character encoding is used for file names and paths when communicating with connecting SFTP clients. Recommended when clients transfer files with non-ASCII characters in names.
 
**Root folder**

Base folder for the Endpoint files. A root folder must be entered before the endpoint can be saved.
 
**Default Credential**

The Credential that should be used for accessing root folder (is needed on network drives).
 
**Session timeout**

Timeout for the session in milliseconds. If 0 is entered, 360000 milliseconds (6 minutes) is used when the endpoint is saved.
 
**SFTP Endpoint > Security options**

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

**Private SSH key**

The host key presented to connecting clients. The field is enabled when public-key authentication is allowed. Select a key from the [SSH keys](../server/global-ssh-keys) or click the add icon to add a new one.

**Test key**

Click to validate the selected SSH key. VisualCron attempts to load the key and displays a checkmark icon if the key is valid or an error icon if the key cannot be loaded.

**Main > Servers > MFT Server > Servers > FTP Endpoints** sub tab

This sub tab is shown for MFT servers of type FTP.

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/FTP%20Endpoint.png)

**FTP Endpoints list**

The grid displays the following columns: **Name**, **IP**, **Security type** and **Port**. The toolbar provides **Add**, **Edit**, **Delete** and **Log** actions.

**FTP Endpoint > Main settings**

**Name**

Optional name for the Endpoint for easier identification. A name must be entered before the endpoint can be saved.
 
**IP**

The IP the Endpoint should listen too. 0.0.0.0 are all IPs on the network card.
 
**Security type**

Select the security type for the FTP endpoint. Available options:

* _None_ - standard FTP with no encryption. The Additional settings are disabled.
* _TSL_ - FTPS using TLS encryption
* _SSL_ - FTPS using SSL encryption

A certificate must be selected on the Additional settings tab for any option other than None.

**Port**

The port to use for the Endpoint. Default 21 for FTP server. Next to the port the current state of the port is displayed, showing whether Windows Firewall allows the port and whether the port is already used by another process.
 
**Firewall allows**

Click to allow or deny the entered port in Windows Firewall. The state next to the button changes between Allowed and Denied.

**Allow Anonymous**

When checked, anonymous users can connect to this FTP endpoint without providing a username or password.
 
**Use UTF8**

When checked UTF8 will be used for communication if available.
 
**Root folder**

Base folder for the Endpoint files. A root folder must be entered before the endpoint can be saved.
 
**Default Credential**

The Credential that should be used for accessing root folder (is needed on network drives).
 
**Session timeout**

Timeout for the session in milliseconds. If 0 is entered, 360000 milliseconds (6 minutes) is used when the endpoint is saved.
 
**Outgoing speed limit**

Speed in bytes per second for outgoing traffic. Default 0 is unlimited speed.
 
**Incoming speed limit**

Speed in bytes per second for incoming traffic. Default 0 is unlimited speed.
 
**FTP Endpoint > Additional settings**

The settings on this tab are only enabled when the Security type is TSL or SSL.

**Certificate with private key file (required for TLS/SSL)**

Select an X.509 certificate with a private key for encryption. This is required when the security type is TSL or SSL. Select a certificate from those defined in [Global Certificates](../server/global-certificates).

**Implicit SSL**

When checked, the connection is encrypted from the start. When unchecked, the connection starts unencrypted and upgrades to encrypted (explicit mode).

**Require TLS for control channel**

When checked, clients must establish TLS encryption on the command channel before logging in. Only available when the Security type is TSL.

**Require TLS for data channel**

When checked, clients must use TLS encryption on the data transfer channel. Only available when the Security type is TSL.
 
**Use Passive mode**

FTP is a TCP based service exclusively. There is no UDP component to FTP. FTP is an unusual service in that it utilizes two ports, a 'data' port and a 'command' port (also known as the control port). Traditionally these are port 21 for the command port and port 20 for the data port. The confusion begins however, when we find that depending on the mode, the data port is not always on port 20. In order to resolve the issue of the server initiating the connection to the client a different method for FTP connections was developed. This was known as passive mode, or PASV, after the command used by the client to tell the server it is in passive mode.
 
**Passive mode host**

Enter IP or DNS name for resolving IP for passive mode or check Use Default Host for using the current IP of the server.
 
**Use Default Host**

Use the current IP of the server.
 
**Use custom port range**

Enter any port range (1 - 65535) for incoming Passive connections. If not checked - random ports will be used. When checked, both the start and the end of the range must be entered before the endpoint can be saved.
 
**Main > Servers > MFT Server > Users** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/Users.png)

**Users list**

This is the list of MFT users. A MFT user can be linked to an existing VC user or be specific for MFT server only. The grid displays the following columns: **Email**, **Username**, **Name** and **Last access**. The toolbar provides **Add**, **Edit** and **Delete** actions.
 
Upon pressing the Add Users icon, the User settings dialog is opened.
 
**Main > Servers > MFT Server > Users > Authentication** sub tab

**Link to existing VC user**

It is possible to link a VC user to a MFT user or use a specific user account just for MFT. When link is selected it will be using the username and password for the specific VC user, and the fields below are disabled.
 
**Username**

Unless linked to VC user you enter the username here. A username must be entered before the user can be saved and before the Permissions tab becomes available.
 
**Password**

Unless linked to VC user you enter the password here. The password is masked.
 
**Name**

Unless linked to VC user you enter the name here.
 
**Email**

Unless linked to VC user you enter the email here.

**Optional custom SSH key (or public server key is used)**

Controls the key used for this user when connecting to an SFTP endpoint. If no key is selected the public server key is used. Available options:

* _None_ - no user specific key is used
* _Use Private key_ - select a private key from the [SSH keys](../server/global-ssh-keys)
* _Use Public key_ - select a public key from the [SSH keys](../server/global-ssh-keys)

The key list of the selected option is enabled and a key must be selected before the user can be saved. Use the Filter field to narrow the list, the add icon to add a new key, and **Test key** to validate the selected key.
 
**Main > Servers > MFT Server > Users > Options** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/User%20Options.png)

**Set owner of files/folders uploaded to Credential below**

To control a remote computer you may need to use a [Credential](../server/global-credentials). The Credential must match the user name and password of the user that you want to login for. Select a Credential in the combo box or click the Settings icon to open Manage credentials in order to add or edit Credentials.
 
**FTP options > Outgoing speed limit**

These are the maximum number of bytes per second for outgoing transfer. 0 is unlimited.
 
**FTP options > Incoming speed limit**

These are the maximum number of bytes per second for incoming transfer. 0 is unlimited.
 
**Main > Servers > MFT Server > Users > Used in servers** sub tab

The grid lists the MFT servers this user has been given access to, with the server name, the server type and whether access is allowed. The toolbar provides **Add**, **Edit** and **Delete** actions, which open the same Permission dialog as the Permissions grid on the Server settings sub tab.
 
**Main > Servers > MFT Server > Users > Permissions** sub tab

The permissions grid lists folder-level access permissions for this user. Select an MFT server from the **Server** selector to filter the list. Only servers the user is allowed to access are listed. The grid displays the following columns: **Folder**, **FR** (File Read), **FW** (File Write), **FD** (File Delete), **FA** (File Append), **DL** (Directory List), **DC** (Directory Create), **DD** (Directory Delete), **DS** (Directory + Subfolders).

The toolbar provides **Add**, **Edit**, and **Delete** actions for managing permissions. Upon pressing Add, the User permissions dialog is opened with the following fields:

**Server**

The MFT server these permissions apply to. This is the server selected in the Server selector and cannot be changed in the dialog.

**Folder**

The folder path on the MFT server this permission entry controls. Use the folder browser button to select a folder. A folder must be entered before the permission can be saved.

**File Read**

When checked, the user can read/download files from the folder.

**File Write**

When checked, the user can write/upload files to the folder.

**File Delete**

When checked, the user can delete files in the folder.

**File Append**

When checked, the user can append to existing files in the folder.

**Show File List**

When checked, the user can list files in the folder.

**Show Folder List**

When checked, the user can list subfolders in the folder.

**Folder + Subfolders**

When checked, the permissions apply to this folder and all of its subfolders.

**Folder Create**

When checked, the user can create new folders within this folder.

**Folder Delete**

When checked, the user can delete folders within this folder.

**Main > Servers > MFT Server > Servers > Advanced SFTP Endpoints** sub tab

This sub tab is shown for MFT servers of type SFTPAdvanced. It is the only endpoint type where the SSH algorithm lists can be selected.

**Advanced SFTP Endpoints list**

The grid displays the following columns: **Name**, **IP**, **Security type** and **Port**. The toolbar provides **Add**, **Edit**, **Delete** and **Log** actions. Add or edit an endpoint to open the SFTP Endpoint dialog, which has the **Main settings** and **SSH Settings** tabs.

**Main > Servers > MFT Server > Servers > Advanced SFTP Endpoints > Main settings** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20Main.png)

**Name**

The endpoint identifier name. This is a required field used to distinguish this endpoint in the configuration interface.

**IP**

The IP the Endpoint should listen too. 0.0.0.0 are all IPs on the network card. Next to the field the current state of the port is displayed, showing whether Windows Firewall allows the port and whether the port is already used by another process.

**Firewall allows**

Click to allow or deny the entered port in Windows Firewall. The state next to the button changes between Allowed and Denied.

**Port**

The port number for the SFTP endpoint. Default is 22 for SFTP servers. This is a required field that specifies which TCP port the endpoint will listen on for incoming connections.

**Force compression**

When enabled, the server requires all data transfers to use compression. The server does not offer uncompressed transfer, so connecting clients have to compress data. This reduces bandwidth usage but increases CPU utilization on both server and clients.

:::note Compatibility Note

Some older SFTP clients may not support mandatory compression. Test with your client software before enabling this setting in production environments.

:::

**Treat Rename As Move**

When enabled, SFTP rename operations are treated as move operations. This affects file operation behavior for certain SFTP clients and may be required for compatibility with specific client implementations. Enabled by default.

**Root folder**

The root folder path for SFTP operations. This is a required field that defines the base directory for file transfers on this endpoint. Use the folder browser button to select a directory on the server.

**Default Credential**

The Credential that should be used for accessing root folder (is needed on network drives).

**Session timeout**

Timeout for the session in milliseconds. If 0 is entered, 360000 milliseconds (6 minutes) is used when the endpoint is saved.

**Certificate with private key**

The certificate used for SSH connection establishment and encryption. This is a required field. Select a certificate from those defined in [Global Certificates](../server/global-certificates). The certificate must have a private key available for session authentication.

**Security options**

The SFTP server supports three authentication methods that can be enabled individually or in combination:

**Allow password authentication**

When checked, clients can authenticate using password credentials. The server will validate the provided password against the user's configured password. Enabled by default.

**Allow public-key authentication**

When checked, clients can authenticate using private/public key pairs. The server validates the client's public key against the user's configured public key or authorized keys.

**Allow keyboard-interactive authentication**

When checked, clients can complete keyboard-interactive authentication challenges. This method supports complex authentication scenarios including one-time passwords, challenge-response systems, and multi-prompt authentication flows.

**The user must authenticate using ANY of the above methods**

The user needs to successfully complete at least one of the enabled authentication methods. This provides flexibility for clients supporting different authentication types. For example, if both password and public key are enabled, the client can choose to use either method.

**The user must authenticate using ALL of the above methods**

The user must successfully complete all enabled authentication methods in sequence. This creates a multi-factor authentication requirement, significantly enhancing security by requiring multiple proof factors.

:::tip Multi-Factor Authentication

For high-security environments, enable multiple authentication methods and select "ALL of the above methods" to create true multi-factor authentication. For example, requiring both password AND public key authentication creates two-factor authentication (2FA) where users must provide both something they know (password) and something they have (private key). Ensure your SFTP clients support multi-method authentication before enabling this mode.

:::

**Main > Servers > MFT Server > Servers > Advanced SFTP Endpoints > SSH Settings** sub tab

The SSH Settings tab holds the **Algorithms** group, which is divided into the **Encryption algorithms**, **Key exchange algorithms**, **MAC algorithms** and **Public key algorithms** sub tabs.

Each sub tab lists the algorithms supported by the endpoint in a grid with a **Use** column. Check an algorithm to advertise it to connecting clients, uncheck it to withdraw it. **Select all** and **Deselect all** below the grid set every row at once. The client and the server negotiate which of the selected algorithms to use when the connection is established, so keep at least the algorithms your clients require selected.

Manual selection is used to:
- Enforce specific security policies or compliance requirements
- Restrict algorithms for regulatory compliance (e.g., FIPS 140-2)
- Limit available algorithms for compatibility with specific client software
- Control encryption strength based on organizational security policies

**Encryption algorithms**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20Encryption.png)

Symmetric encryption algorithms (ciphers) used for securing data transmission during SFTP sessions. New endpoints start with the following algorithms selected:

* aes256-ctr
* aes192-ctr
* aes128-ctr
* 3des-ctr
* aes256-gcm@openssh.com
* aes128-gcm@openssh.com
* chacha20-poly1305@openssh.com

**Key exchange algorithms**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20KeyExchange.png)

Key exchange algorithms used during SSH connection establishment. They securely establish shared encryption keys between the server and client without transmitting the key material over the network. All listed algorithms are selected on new endpoints.

**Use Strict Key Exchange**

Controls strict key exchange validation during the SSH connection handshake. Available options:
- **Disabled** - Strict key exchange validation is turned off
- **Enabled, not enforced (default)** - Strict validation is enabled but not required
- **Enabled, reject affected algorithms** - Strict validation is enabled and algorithms that do not support it are rejected
- **Required** - Strict key exchange is mandatory for all connections

Strict key exchange provides enhanced security against certain downgrade attacks but may affect compatibility with older SSH clients.

**MAC algorithms**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20MAC.png)

Message Authentication Code (MAC) algorithms used for ensuring data integrity and authenticity during SFTP sessions. MAC algorithms verify that transmitted data has not been tampered with or corrupted during transmission. All listed algorithms except hmac-sha2-256-96-etm@openssh.com and hmac-sha2-512-96-etm@openssh.com are selected on new endpoints.

**Public key algorithms**

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20PublicKey.png)

Public key algorithms used for server host key authentication and client public key authentication. These algorithms verify the identity of both the server and clients during SSH connections. All listed algorithms are selected on new endpoints.

:::note Key Size Requirements

When using RSA-based public key algorithms, ensure that both server host keys and client keys meet minimum key size requirements. Modern security standards typically require at least 2048-bit RSA keys. For high-security environments, 3072-bit or 4096-bit RSA keys may be preferred. Consult your organization's security policies for specific requirements.

:::
