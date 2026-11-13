---
sidebar_label: 'MFT Server'
hide_title: 'true'
---

## Servers - MFT Server

The ***MFT Settings*** window, opened from ***Servers*** -> ***Managed File Transfer***, is where the MFT Server is turned on and where its servers, endpoints and users are managed.

The MFT Server hosts file transfer servers inside the VisualCron Server. Three server types can be created:

* "SFTP": SSH File Transfer Protocol, with a fixed set of SSH algorithms
* "SFTPAdvanced": SSH File Transfer Protocol, with a selectable list of SSH algorithms
* "FTP": FTP, either unencrypted or FTPS (FTP over TLS or SSL)

Each server listens on one or more endpoints. An endpoint is an IP address and a port.

Hosting the servers in VisualCron means no separate file transfer server has to be installed, and the [MFT Server Trigger](../server/event-trigger-mft-server) can start a Job when something happens on a server, for example when a file is received or sent, or when a folder is created.

:::warning Security defaults

- A new endpoint listens on all IPv4 addresses of the Server computer ("0.0.0.0").
- A new FTP endpoint uses port 21 and the security type "None", so user names, passwords and files are sent unencrypted. Select "TSL" or "SSL" and a certificate to encrypt the connection.
- A new SFTP or SFTPAdvanced endpoint uses port 22 and allows password authentication only.
- A new MFT server starts as soon as it is saved, and every server in the "Active" state starts again when the VisualCron Server starts, as long as _Allow MFT_ is checked.
- Saving a permission can add a folder permission with every right checked; see [Permission window](#permission-window) below.
- The _Firewall allows_ button does not change the rule for the endpoint port; see _Firewall allows_ under [Server Settings window: SFTP Endpoints tab](#server-settings-window-sftp-endpoints-tab) below.

:::

:::note Server type is selected when the server is created

The _Server type_ can only be changed while the MFT server is being added. When an existing MFT server is edited, the list is read-only, and only the endpoint tab that matches the type is shown.

Encryption, key exchange, MAC and public key algorithms can be selected only on the "SFTPAdvanced" server type. To control the algorithm list for an existing "SFTP" server, add a new MFT server of type "SFTPAdvanced" instead.

:::

### MFT Settings window

![MFT Settings window opened from the Servers ribbon tab, showing the Allow MFT check box and the list of MFT servers](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/MFT.png)

- _Allow MFT_: turns the MFT Server on for this VisualCron Server. While it is unchecked, the MFT settings area is unavailable. Unchecking it stops every running MFT server at once, before _Apply settings_ is clicked, and _Cancel_ does not start them again
- _Apply settings_: saves the _Allow MFT_ setting and closes the window
- _Cancel_: closes the window without saving the _Allow MFT_ setting

:::warning

- Unchecking _Allow MFT_ stops every running MFT server at once; _Cancel_ does not start them again.
- Changes to an MFT server or user are sent to the VisualCron Server when _Save_ is clicked in the ***Server Settings*** or ***User settings*** window. Endpoint and permission changes, including _Delete_, are sent only with that _Save_; _Cancel_ in that window discards them.
- _Delete_ on the ***Servers*** and ***Users*** tabs takes effect at once, without confirmation. _Cancel_ in the ***MFT Settings*** window does not undo any of these.

:::

The MFT settings area has two tabs: ***Servers*** lists the hosted MFT servers and ***Users*** lists the accounts that connect to them.

#### Servers tab

The grid shows the _Server name_, _Ports_, _Type_, _State_, _Connections_ and _Status_ of each MFT server. The toolbar has the following buttons:

- _Add_: opens the ***Server Settings*** window for a new MFT server
- _Edit_: opens the selected MFT server. Double-clicking a row does the same
- _Delete_: stops the selected MFT servers if they are running, then deletes them. No confirmation is asked. Pressing the Delete key in the grid does the same
- _Activate/Deactivate Server_: switches the selected servers between the "Active" and "Inactive" states. Only "Active" servers start when the VisualCron Server starts
- _Run/Stop Server_: stops a running server, or starts a stopped or failed one
- _Log history_: opens the transfer log

Right-click a server for _Log history_, for _Export ..._, which exports the server definition, and for _Send to connection ..._, which copies the server, its permissions and their users to another VisualCron Server.

The ***Users*** tab is described in [MFT Settings window: Users tab](#mft-settings-window-users-tab) below.

### Server Settings window

![Server Settings window with the Server settings tab and the Permission window opened from the Permissions grid](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/MFT%20Settings.png)

#### Server settings tab

- _Server name_: the name of the MFT server
- _Server type_: "FTP", "SFTP" or "SFTPAdvanced". The type decides which endpoint tab is shown next to ***Server settings***: ***FTP Endpoints***, ***SFTP Endpoints*** or ***Advanced SFTP Endpoints***
- _Permissions_: the users who can connect to this MFT server. Use _Add_, _Edit_ and _Delete_ on the toolbar

At least one endpoint must be added before the server can be saved. A server can be saved without permissions, but no user can connect to it until one is added.

#### Permission window

- _Server_: the MFT server the permission applies to. Click the add icon next to the list to create a new MFT server
- _User_: the MFT user the permission applies to. Click the add icon next to the list to create a new MFT user. Both a server and a user must be selected before the permission can be saved
- _Allow Access_: checked by default. When checked, the user can connect to the server. Uncheck it to deny access without removing the permission
- _Base folder_: the startup folder for the user on this server. Use the folder button to select a folder

:::warning A new permission can grant full folder rights

When the permission is saved and the user has no folder permission for this server and _Base folder_, one is added with every right checked, including _File Delete_, _Folder Delete_ and _Folder + Subfolders_. Review it on the ***Permissions*** tab of the ***User settings*** window.

:::

#### Server Settings window: SFTP Endpoints tab

This tab is shown for MFT servers of type "SFTP".

![SFTP Endpoints tab and the SFTP Endpoint window with its main settings and security options](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/MFT%20Endpoint.png)

The grid shows the _Name_, _IP_, _Security type_ and _Port_ of each endpoint. The toolbar has _Add_, _Edit_, _Delete_ and _Log_. _Add_ and _Edit_ open the ***SFTP Endpoint*** window.

**Main settings**

- _Name_: a name for the endpoint. A name is required. A new endpoint is named after its port
- _IP_: the address the endpoint listens on. "0.0.0.0", the default, means all IPv4 addresses of the Server computer. The list also offers the IPv4 addresses of the computer the Client runs on
- _Port_: the port the endpoint listens on. The default is "22". Next to the port, the window shows whether a VisualCron firewall rule exists for the port ("Allowed" or "Denied") and whether another process already uses the port
- _Firewall allows_: adds or removes a Windows Firewall rule created by VisualCron. The status next to it is checked for the endpoint port, but the rule the button adds or removes is for the VisualCron Server port that the Client connects to (by default "16444"), not for the endpoint port. Clicking it while the status shows "Allowed" removes the VisualCron firewall rule for the VisualCron Server port, which remote Clients may depend on. Open the endpoint port in Windows Firewall directly instead
- _Force compression_: when checked, all transfers must be compressed. The server does not offer uncompressed transfer, so connecting clients must support compression. This lowers bandwidth use but raises CPU use on the server and the client
- _Use UTF8_: when checked, file and folder names are exchanged with connecting SFTP clients in UTF-8. Use it when clients transfer files with non-ASCII characters in their names
- _Root folder_: the base folder for the endpoint files. A root folder is required
- _Default Credential_: the [Credential](../server/global-credentials) used to access the root folder. It is needed when the root folder is on a network drive
- _Session timeout_: the session timeout in milliseconds. If "0" is entered, "360000" (6 minutes) is saved

**Security options**

- _Allow password authentication_: checked by default. Users can sign in with their password
- _Allow public-key authentication_: users can sign in with an SSH key pair
- _Allow keyboard-interactive authentication_: users can sign in with keyboard-interactive authentication
- _The user must authenticate using ANY of the above methods_: the default. One of the allowed methods is enough
- _The user must authenticate using ALL of the above methods_: every allowed method must succeed
- _Private SSH key_: a private key from [SSH keys](../server/global-ssh-keys). The list is available only when _Allow public-key authentication_ is checked, and the key is saved only in that case. Click the button next to the list to open [SSH keys](../server/global-ssh-keys) and add or edit keys
- _Test key_: loads the selected key and shows a check mark if the key is valid, or an error icon if it cannot be loaded

#### Server Settings window: FTP Endpoints tab

This tab is shown for MFT servers of type "FTP".

![FTP Endpoints tab and the FTP Endpoint window with its Main settings tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/FTP%20Endpoint.png)

The grid shows the _Name_, _IP_, _Security type_ and _Port_ of each endpoint. The toolbar has _Add_, _Edit_, _Delete_ and _Log_. _Add_ and _Edit_ open the ***FTP Endpoint*** window, which has the ***Main settings*** and ***Additional settings*** tabs.

**FTP Endpoint: Main settings tab**

- _Name_: a name for the endpoint. A name is required. A new endpoint is named after its port
- _IP_: the address the endpoint listens on. "0.0.0.0", the default, means all IPv4 addresses of the Server computer. The list also offers the IPv4 addresses of the computer the Client runs on
- _Security type_:
  - "None": the default. Plain FTP with no encryption. User names, passwords and files are sent unencrypted, and the security settings on the ***Additional settings*** tab are unavailable
  - "TSL": FTPS with TLS encryption. The Client spells this value "TSL"
  - "SSL": FTPS with SSL encryption

  A certificate must be selected on the ***Additional settings*** tab for "TSL" and "SSL"
- _Port_: the port the endpoint listens on. The default is "21". Next to the port, the window shows whether a VisualCron firewall rule exists for the port and whether another process already uses the port
- _Firewall allows_: behaves as on the SFTP endpoint; see [Server Settings window: SFTP Endpoints tab](#server-settings-window-sftp-endpoints-tab)
- _Allow Anonymous_: unchecked by default. When checked, users can connect without a user name or password
- _Use UTF8_: when checked, UTF-8 is used for communication when the client supports it
- _Root folder_: the base folder for the endpoint files. A root folder is required
- _Default Credential_: the [Credential](../server/global-credentials) used to access the root folder. It is needed when the root folder is on a network drive
- _Session timeout_: the session timeout in milliseconds. If "0" is entered, "360000" (6 minutes) is saved
- _Outgoing speed limit_: the maximum outgoing speed in bytes per second. "0", the default, means no limit
- _Incoming speed limit_: the maximum incoming speed in bytes per second. "0", the default, means no limit

**FTP Endpoint: Additional settings tab**

The ***Additional security settings*** group is available only when the _Security type_ is "TSL" or "SSL". The ***Passive mode*** group is available for every security type.

- _Certificate with private key file (required for TLS/SSL)_: an X.509 certificate with a private key, selected from [Certificates](../server/global-certificates). It is required for "TSL" and "SSL"
- _Implict SSL_: when checked, the connection is encrypted from the start (implicit FTPS). When unchecked, the connection starts unencrypted and the client upgrades it (explicit FTPS). The port is not changed when this is checked
- _Require TLS for control channel_: when checked, clients must encrypt the command channel before they sign in. Available only for "TSL"
- _Require TLS for data channel_: when checked, clients must encrypt the data channel. Available only for "TSL"

:::warning

With "TSL" selected and _Implict SSL_ unchecked, unchecking _Require TLS for control channel_ allows clients to connect without first switching the control channel to TLS, so their user name and password may be sent unencrypted.

:::

- _Use Passive mode_: when checked, the server accepts passive mode (PASV) connections, where the client opens the data connection to a port on the server. This usually works better through client-side firewalls and NAT
- _Passive mode host_: the IP address or DNS name the server gives clients for passive connections. Available when _Use Default Host_ is unchecked
- _Use Default Host_: gives clients the current IP address of the server for passive connections
- _Use custom port range_: limits passive connections to a port range (1 - 65535). When unchecked, random ports are used. When checked, both the start and the end of the range are required. Open the range in Windows Firewall

### MFT Settings window: Users tab

![Users tab of the MFT Settings window and the Authentication tab of the User settings window](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/Users.png)

The grid lists the MFT users with their _Email_, _Username_, _Name_ and _Last access_. An MFT user can be linked to an existing VisualCron user or exist only for the MFT Server. The toolbar has _Add_, _Edit_ and _Delete_. _Add_ and _Edit_ open the ***User settings*** window. _Delete_ deletes the selected users at once, without confirmation. Pressing the Delete key in the grid does the same.

:::warning

Deleting a user, or deleting the VisualCron user an MFT user is linked to, removes the MFT user at once.

:::

#### User settings: Authentication tab

- _Link to existing VC user_: when checked, the user signs in with the user name and password of the selected VisualCron user. _Username_, _Password_, _Name_ and _Email_ are cleared and become unavailable. When that VisualCron user is deleted, the linked MFT user is deleted too
- _Username_: the user name for an MFT-only user. A user name is required before the user can be saved and before the ***Used in servers*** tab becomes available
- _Password_: the password for an MFT-only user. The password is masked
- _Name_: the name of an MFT-only user
- _Email_: the e-mail address of an MFT-only user
- _Optional custom SSH key (or public server key is used)_: the key used for this user on SFTP endpoints:
  - "None": the default. No user-specific key
  - "Use Private key": a private key from [SSH keys](../server/global-ssh-keys)
  - "Use Public key": a public key from [SSH keys](../server/global-ssh-keys)

  The key list of the selected option becomes available, and a key must be selected before the user can be saved. Use the filter field to narrow the list, the button next to the list to open [SSH keys](../server/global-ssh-keys), and _Test key_ to check the selected key

#### User settings: Options tab

![Options tab of the User settings window with the owner Credential and the FTP speed limits](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/User%20Options.png)

- _Set owner of files/folders uploaded to Credential below_: the [Credential](../server/global-credentials) set as owner of files and folders this user uploads. Select a Credential in the combo box, or click the settings icon to open the Credential list
- _Outgoing speed limit_: in the ***FTP options*** group. The maximum outgoing speed in bytes per second for this user. "0" means no limit
- _Incoming speed limit_: in the ***FTP options*** group. The maximum incoming speed in bytes per second for this user. "0" means no limit

#### User settings: Used in servers tab

The grid lists the MFT servers this user has been given access to, with the server name, the server type and whether access is allowed. _Add_, _Edit_ and _Delete_ open the same ***Permission*** window as the Permissions grid on the ***Server settings*** tab.

#### User settings: Permissions tab

The grid lists the folder permissions of this user on one MFT server. Select the MFT server with the _Server_ selector. Only servers the user is allowed to access are listed. The grid has the columns _Folder_, _FR_ (File Read), _FW_ (File Write), _FD_ (File Delete), _FA_ (File Append), _DL_ (Directory List), _DC_ (Directory Create), _DD_ (Directory Delete) and _DS_ (Directory + Subfolders).

_Add_ and _Edit_ open the ***User permissions*** window:

- _Server_: the MFT server selected in the _Server_ selector. It cannot be changed here
- _Folder_: the folder on the MFT server this entry controls. Use the folder button to select a folder. A folder is required
- _File Read_: the user can read and download files in the folder
- _File Write_: the user can write and upload files to the folder
- _File Delete_: the user can delete files in the folder
- _File Append_: the user can append to existing files in the folder
- _Show File List_: the user can list the files in the folder
- _Show Folder List_: the user can list the subfolders of the folder
- _Folder + Subfolders_: the permissions apply to this folder and all its subfolders
- _Folder Create_: the user can create folders in this folder
- _Folder Delete_: the user can delete folders in this folder

### Server Settings window: Advanced SFTP Endpoints tab

This tab is shown for MFT servers of type "SFTPAdvanced". It is the only endpoint type where the SSH algorithms can be selected.

The grid shows the _Name_, _IP_, _Security type_ and _Port_ of each endpoint. The toolbar has _Add_, _Edit_, _Delete_ and _Log_. _Add_ and _Edit_ open the ***SFTP Endpoint*** window, which has the ***Main settings*** and ***SSH Settings*** tabs.

#### SFTP Endpoint: Main settings tab

![Main settings tab of the advanced SFTP Endpoint window with the certificate and security options](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20Main.png)

- _Name_: a name for the endpoint. A name is required. A new endpoint is named after its port
- _IP_: the address the endpoint listens on. "0.0.0.0", the default, means all IPv4 addresses of the Server computer. The list also offers the IPv4 addresses of the computer the Client runs on
- _Firewall allows_: behaves as on the SFTP endpoint; see [Server Settings window: SFTP Endpoints tab](#server-settings-window-sftp-endpoints-tab)
- _Port_: the port the endpoint listens on. The default is "22". A port is required
- _Force compression_: when checked, all transfers must be compressed. The server does not offer uncompressed transfer, so connecting clients must support compression. This lowers bandwidth use but raises CPU use on the server and the clients
- _Treat Rename As Move_: checked by default. SFTP rename operations are handled as move operations, which some SFTP clients need
- _Root folder_: the base folder for the endpoint files. A root folder is required
- _Default Credential_: the [Credential](../server/global-credentials) used to access the root folder. It is needed when the root folder is on a network drive
- _Session timeout_: the session timeout in milliseconds. If "0" is entered, "360000" (6 minutes) is saved
- _Certificate with private key_: the certificate whose key the endpoint uses in the SSH connection, selected from [Certificates](../server/global-certificates). A certificate is required, and it must include its private key

:::note Compatibility

Some older SFTP clients do not support mandatory compression. Test with the client software before checking _Force compression_ on a production endpoint.

:::

**Security options**

- _Allow password authentication_: checked by default. Users can sign in with their password
- _Allow public-key authentication_: users can sign in with an SSH key pair
- _Allow keyboard-interactive authentication_: users can sign in with keyboard-interactive authentication
- _The user must authenticate using ANY of the above methods_: the default. One of the allowed methods is enough
- _The user must authenticate using ALL of the above methods_: every allowed method must succeed

:::tip Require more than one method

To require both a password and a key, check _Allow password authentication_ and _Allow public-key authentication_, then select _The user must authenticate using ALL of the above methods_. Check that the SFTP clients support signing in with more than one method before using this setting.

:::

#### SFTP Endpoint: SSH Settings tab

The ***Algorithms*** group has the ***Encryption algorithms***, ***Key exchange algorithms***, ***MAC algorithms*** and ***Public key algorithms*** tabs.

Each tab lists the algorithms the endpoint supports, with a _Use_ column. Check an algorithm to offer it to connecting clients, or uncheck it to withdraw it. _Select all_ and _Deselect all_ below the grid set every row at once. The client and the server agree on one of the offered algorithms when the connection is made, so keep the algorithms the clients need checked.

Unchecking algorithms is how a security policy is applied to the endpoint, for example to withdraw algorithms based on MD5, SHA-1, DSA or 3DES.

:::warning Legacy algorithms are offered by default

A new endpoint offers several algorithms that many security policies no longer allow, including `3des-ctr`, `diffie-hellman-group1-sha1` and the other SHA-1 key exchanges, `hmac-md5`, `hmac-sha1`, `ssh-rsa` and `ssh-dss`. Review each list and uncheck what the clients do not need.

:::

**Encryption algorithms**

![Encryption algorithms tab with the Use column and the Select all and Deselect all buttons](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20Encryption.png)

The ciphers that protect the data in an SFTP session. A new endpoint has the following checked:

* `aes256-ctr`
* `aes192-ctr`
* `aes128-ctr`
* `3des-ctr`
* `aes256-gcm@openssh.com`
* `aes128-gcm@openssh.com`
* `chacha20-poly1305@openssh.com`

The CBC ciphers (including `3des-cbc`, `blowfish-cbc` and `cast128-cbc`) and `arcfour`, `arcfour128` and `arcfour256` are listed but unchecked.

**Key exchange algorithms**

![Key exchange algorithms tab with the Use Strict Key Exchange list and the algorithm grid](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20KeyExchange.png)

The algorithms used to agree on session keys when the connection is made, without sending the keys over the network. Every listed algorithm is checked on a new endpoint, including `diffie-hellman-group1-sha1`, `diffie-hellman-group14-sha1`, `diffie-hellman-group-exchange-sha1` and the SHA-1 GSS algorithms.

- _Use Strict Key Exchange_: how strict key exchange is applied during the handshake:
  - "Disabled": strict key exchange is off
  - "Enabled, not enforced (default)": the default. Strict key exchange is on but not enforced
  - "Enabled, reject affected algorithms": strict key exchange is on, and the affected algorithms are rejected
  - "Required": every connection must use strict key exchange

Strict key exchange protects against some downgrade attacks, but can stop older SSH clients from connecting.

**MAC algorithms**

![MAC algorithms tab with the Use column and the algorithm grid](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20MAC.png)

The Message Authentication Code algorithms that check that data in an SFTP session has not been changed. Every listed algorithm except `hmac-sha2-256-96-etm@openssh.com` and `hmac-sha2-512-96-etm@openssh.com` is checked on a new endpoint, including `hmac-md5`, `hmac-md5-96`, `hmac-sha1` and `hmac-sha1-96`.

**Public key algorithms**

![MAC algorithms tab of the SSH Settings tab, shown in place of the Public key algorithms tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Servers/MFT/SFTP%20Advanced%20PublicKey.png)

The algorithms used for the server host key and for client public-key authentication. Every listed algorithm is checked on a new endpoint, including `ssh-rsa`, which signs with SHA-1, and `ssh-dss`.

:::note Key size

For RSA keys, both the server key and the client keys must meet the key size the organization requires. Many security standards require at least 2048-bit RSA keys.

:::
