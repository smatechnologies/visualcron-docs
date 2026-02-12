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

**Main > Servers > MFT Server > Servers > SFTP Endpoints > Advanced Settings > Main settings** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20Main.png)

The Advanced Settings dialog provides granular control over SFTP endpoint security and connection parameters. These settings allow administrators to configure authentication requirements, manage encryption options, and fine-tune connection behavior for compliance and security requirements.

**Basic Connection Settings**

**Name**

The endpoint identifier name. This is a required field used to distinguish this endpoint in the configuration interface.

**IP/Hostname**

The connection address for this SFTP endpoint. Use the host selector to specify the IP address or hostname where the endpoint will listen for connections. This is a required field.

**Port**

The port number for the SFTP endpoint. Default is 22 for SFTP servers. This is a required field that specifies which TCP port the endpoint will listen on for incoming connections.

**Root Directory**

The root folder path for SFTP operations. This is a required field that defines the base directory for file transfers on this endpoint. Use the folder browser button to select a directory on the server.

**Session Timeout**

Timeout value for SFTP sessions in milliseconds. Default value is 360000 milliseconds (6 minutes). If set to 0, the system-default timeout will be used (typically 2 hours 8 minutes for TCP stack).

**Port Management**

**Port Status**

Displays whether the configured port is currently in use by another process on the system. This indicator helps identify potential port conflicts before starting the endpoint.

**Firewall Status**

Displays whether Windows Firewall currently allows incoming connections on the configured port. This status indicator shows if the port is permitted through the firewall.

**Open/Close Port**

Button to toggle firewall access for the configured port. Click to allow or deny the port in Windows Firewall. The system will display success or error messages for firewall operations.

**Security Certificate**

**Certificate**

The SSL/TLS certificate required for SSH connection establishment and encryption. This is a required field. Select a certificate from those defined in [Global Certificates](../server/global-certificates). The certificate must have a private key available for session authentication.

**Security Options**

**Force Compression**

When enabled, the server requires all data transfers to use compression (ZLIB algorithm). The server will not advertise support for uncompressed transfer mode (NONE compression algorithm), forcing all connecting clients to compress data during transmission. This reduces bandwidth usage but increases CPU utilization on both server and clients.

:::note Compatibility Note

Some older SFTP clients may not support mandatory compression. Test with your client software before enabling this setting in production environments.

:::

**Treat Rename as Move**

When enabled, SFTP rename operations are treated as move operations. This affects file operation behavior for certain SFTP clients and may be required for compatibility with specific client implementations.

**Authentication Methods**

The SFTP server supports three authentication methods that can be enabled individually or in combination:

**Require password authentication**

When checked, clients can authenticate using password credentials. The server will validate the provided password against the user's configured password.

**Require public key authentication**

When checked, clients can authenticate using private/public key pairs. The server validates the client's public key against the user's configured public key or authorized keys.

**Require keyboard-interactive authentication**

When checked, clients can complete keyboard-interactive authentication challenges. This method supports complex authentication scenarios including one-time passwords, challenge-response systems, and multi-prompt authentication flows.

**Authentication Requirements**

Choose how the enabled authentication methods should be applied:

**The user must authenticate using ANY of the above methods**

The user needs to successfully complete at least one of the enabled authentication methods. This provides flexibility for clients supporting different authentication types. For example, if both password and public key are enabled, the client can choose to use either method.

**The user must authenticate using ALL of the above methods**

The user must successfully complete all enabled authentication methods in sequence. This creates a multi-factor authentication requirement, significantly enhancing security by requiring multiple proof factors.

:::tip Multi-Factor Authentication

For high-security environments, enable multiple authentication methods and select "ALL of the above methods" to create true multi-factor authentication. For example, requiring both password AND public key authentication creates two-factor authentication (2FA) where users must provide both something they know (password) and something they have (private key). Ensure your SFTP clients support multi-method authentication before enabling this mode.

:::

**Main > Servers > MFT Server > Servers > SFTP Endpoints > Advanced Settings > Encryption Algorithms** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20Encryption.png)

This tab allows selection of symmetric encryption algorithms (ciphers) used for securing data transmission during SFTP sessions. The server and client negotiate the encryption algorithm during the SSH connection handshake.

**Auto-negotiate encryption algorithms**

When enabled (default setting), the server automatically advertises available encryption algorithms to connecting clients. The client and server will negotiate and select a mutually supported cipher, typically choosing the strongest available option. This is the recommended setting for most deployments.

**Manual Algorithm Selection**

Disable auto-negotiation to manually select specific encryption algorithms from the available list. Manual selection allows administrators to:
- Enforce specific security policies or compliance requirements
- Restrict algorithms for regulatory compliance (e.g., FIPS 140-2)
- Limit available ciphers for compatibility with specific client software
- Control encryption strength based on organizational security policies

**Main > Servers > MFT Server > Servers > SFTP Endpoints > Advanced Settings > Key Exchange Algorithms** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20KeyExchange.png)

This tab allows selection of key exchange algorithms used during SSH connection establishment. Key exchange algorithms are used to securely establish shared encryption keys between the server and client without transmitting the key material over the network.

**Use Strict Key Exchange**

Dropdown option to control strict key exchange validation during SSH connection handshake. Available options:
- **Disabled** - Strict key exchange validation is turned off
- **Enabled, not enforced (default)** - Strict validation is enabled but not required
- **Enabled, reject affected algorithms** - Strict validation is enabled and algorithms that don't support it are rejected
- **Required** - Strict key exchange is mandatory for all connections

Strict key exchange provides enhanced security against certain downgrade attacks but may affect compatibility with older SSH clients.

**Auto-negotiate key exchange algorithms**

When enabled (default setting), the server automatically advertises available key exchange algorithms to connecting clients. The client and server negotiate and select a mutually supported method during the connection handshake. This is the recommended setting for most deployments.

**Manual Algorithm Selection**

Disable auto-negotiation to manually select specific key exchange algorithms from the available list. Manual selection is used for specific security policies, compliance requirements, or compatibility with particular client implementations.

**Main > Servers > MFT Server > Servers > SFTP Endpoints > Advanced Settings > MAC Algorithms** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20MAC.png)

This tab allows selection of Message Authentication Code (MAC) algorithms used for ensuring data integrity and authenticity during SFTP sessions. MAC algorithms verify that transmitted data has not been tampered with or corrupted during transmission.

**Auto-negotiate MAC algorithms**

When enabled (default setting), the server automatically advertises available MAC algorithms to connecting clients. The client and server negotiate and select a mutually supported algorithm during the SSH connection handshake. This is the recommended setting for most deployments.

**Manual Algorithm Selection**

Disable auto-negotiation to manually select specific MAC algorithms from the available list. Manual selection allows administrators to enforce specific security policies, meet compliance requirements, or ensure compatibility with particular client implementations.

**Main > Servers > MFT Server > Servers > SFTP Endpoints > Advanced Settings > Public Key Algorithms** sub tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20PublicKey.png)

This tab allows selection of public key algorithms used for server host key authentication and client public key authentication. These algorithms verify the identity of both the server and clients during SSH connections.

**Auto-negotiate public key algorithms**

When enabled (default setting), the server automatically advertises available public key algorithms to connecting clients. The client and server negotiate and select a mutually supported algorithm for both host key verification and client authentication. This is the recommended setting for most deployments.

**Manual Algorithm Selection**

Disable auto-negotiation to manually select specific public key algorithms from the available list. Manual selection is used when:
- Specific security policies require particular algorithm types
- Compliance requirements mandate certain key algorithms
- Compatibility with specific client software requires algorithm restrictions
- Key size requirements need to be enforced for organizational security policies

:::note Key Size Requirements

When using RSA-based public key algorithms, ensure that both server host keys and client keys meet minimum key size requirements. Modern security standards typically require at least 2048-bit RSA keys. For high-security environments, 3072-bit or 4096-bit RSA keys may be preferred. Consult your organization's security policies for specific requirements.

:::