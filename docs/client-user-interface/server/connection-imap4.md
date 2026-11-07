---
sidebar_label: 'Connection - IMAP4'
hide_title: 'true'
---

## Connection - IMAP4

The IMAP4 Connection stores the address, sign-in and security settings that the [Email - Get Messages](job-tasks/messaging-tasks/email-get-messages), [Email - Get Single Message](job-tasks/messaging-tasks/email-get-single-message), [Email - Get Headers](job-tasks/messaging-tasks/email-get-headers), [Email - Delete Messages](job-tasks/messaging-tasks/email-delete-messages), [Email - Delete Single Message](job-tasks/messaging-tasks/email-delete-single-message) and Email - Move Messages Tasks and the [Email Trigger](event-trigger-mail) use to connect to a mail server over Internet Message Access Protocol (IMAP4).
 
### Common settings

![IMAP4 Connection, Common settings tab with the Protocol and Information groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IMAP4/IMAP.png)

The ***Common settings*** and ***Proxy*** tabs are the same for every Connection type that has them; see [Common settings](global-connections#common-settings) and [Proxy](global-connections#proxy).

_Test_

The Server connects to the mail server and logs on with the settings of this Connection, then disconnects. No email is read or changed.

### Main settings

These fields are on ***Connection settings*** -> ***Main settings***.

The ***Connection settings*** tab holds three tabs: ***Main settings***, ***Encryption*** and ***Proxy***.

![IMAP4 Connection, Main settings tab with the Server and Credentials groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IMAP4/Settings.png)

_Address_

The DNS name or IP address of the IMAP4 server. Required.

_Port_

The port of the IMAP4 server. A new Connection opens with "21" in _Port_. Change it to the port of the mail server: usually "993" with "SSL", or "143" with "TLS" or without encryption. Port "993" expects encryption from the start, so use it with "SSL". _Port_ cannot be "0".

_Authentication type_

- "Default": a user name and password
- "OAuth": Google OAuth only, for Gmail and Google Workspace accounts; it does not work with other mail services

_Anonymous_

Shown only with "Default". When selected, _Username_ and _Password_ are unavailable. The Server does not use _Anonymous_ when it reads email, and always logs on with _Username_ and _Password_, so leave it cleared. Anonymous access to a shared mailbox is not supported in IMAP4.

_Username_

The user name of the email account. Required unless _Anonymous_ is selected. With "OAuth", this field is labeled _Application Id_ and holds the client ID of your Google OAuth client.

_Password_

The password of the email account. With "OAuth", this field is labeled _Client secret_ and holds the client secret of your Google OAuth client.

_Setup app_

Shown with "OAuth". Opens the Google API Console in the web browser, where you create the OAuth client.

_Authenticate_

Shown with "OAuth". Opens the Google sign-in page in the web browser. When sign-in succeeds, the authorization is saved in the Connection, and the Server reads email as the Google account that signed in.

_App settings_

Shown with "OAuth". Of the fields in this group, only _Redirect Url_ is used with Google. _Tenant Id_, _Tenant Primary Domain_, _Tenant Name_ and _Auto-accept server certificates_ are not used.

_Redirect Url_ is the address that receives the reply from Google after sign-in, on the computer that runs the Client. It is required for _Authenticate_. Enter a local address such as "http://localhost:9999", and add the same address as an authorized redirect URI in the Google OAuth client.

With "OAuth", the Server connects to _Address_ with an encrypted connection. It does not use _Port_ or the settings on the ***Encryption*** tab.

To set up "OAuth", complete the following steps:

1. In _Authentication type_, select "OAuth".
2. Click _Setup app_. The Google API Console opens.
3. In the Google API Console, create an OAuth client ID.
4. Add the address that you will enter in _Redirect Url_ as an authorized redirect URI of the OAuth client.
5. Enter the client ID in _Application Id_.
6. Enter the client secret in _Client secret_.
7. Enter the redirect address in _Redirect Url_.
8. Click _Authenticate_.
9. In the web browser, sign in with the Google account of the mailbox.
10. Allow access.
11. Click _OK_.

The Connection now reads email from that Google account. After you edit and save an IMAP4 Connection that uses "OAuth", click _Authenticate_ again before you use it.
 
### Default settings for some servers

**Office 365**

[https://support.office.com/en-nz/article/Settings-for-POP-and-IMAP-access-for-Office-365-for-business-or-Microsoft-Exchange-accounts-7fc677eb-2491-4cbc-8153-8e7113525f6c](https://support.office.com/en-nz/article/Settings-for-POP-and-IMAP-access-for-Office-365-for-business-or-Microsoft-Exchange-accounts-7fc677eb-2491-4cbc-8153-8e7113525f6c)
 
Main settings
* Address: outlook.office365.com
* Port: 993
 
Encryption
* Cryptographic protocol: SSL
 
**Gmail**

* Address: imap.gmail.com
* Port: 993
 
Encryption
* Cryptographic protocol: SSL
* SSL Version: 3
 
### Encryption

![IMAP4 Connection, Encryption tab with the SSL/TLS and Allowed SSL/TLS versions groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IMAP4/Encryption.png)

The settings on this tab are used with "Default" authentication. With "OAuth", the mail connection does not use them, but the Email Trigger and _Test_ still set the SSL and TLS versions for the whole Server process from them, as described under _Allowed SSL/TLS versions_.

_Cryptographic protocol_

- "No encryption": the connection is not encrypted; the _Allowed SSL/TLS versions_ group is unavailable
- "SSL": SSL encryption; selects _SSL version 2_ and _SSL version 3_ in _Allowed SSL/TLS versions_
- "TLS": TLS encryption; selects _TLS version 1_ to _TLS version 1.3_ in _Allowed SSL/TLS versions_

The email receiving Tasks and the Email Trigger use _Cryptographic protocol_ when they read email. With "SSL", they encrypt the connection from the start. With "TLS", they connect in plain text and then switch to encryption.

_Allowed SSL/TLS versions_

The available versions are:

- _SSL version 2_
- _SSL version 3_
- _TLS version 1_
- _TLS version 1.1_
- _TLS version 1.2_
- _TLS version 1.3_

The email receiving Tasks do not read these boxes. When the Email Trigger checks the mailbox, and when you click _Test_, the Server first sets the SSL and TLS versions for the whole Server process from them:

- "TLS": the selected boxes among _TLS version 1_, _TLS version 1.1_ and _TLS version 1.2_, or all three when none of them is selected; never _TLS version 1.3_
- "SSL" with _SSL version 3_ selected: the system default versions
- "SSL" with _SSL version 3_ cleared: _SSL version 3_ only

With "SSL" and _SSL version 3_ cleared, the whole Server process is limited to SSL 3, and other Tasks that connect over HTTPS can then fail.

:::note

Each time you open an existing IMAP4 Connection, the version boxes reset to the defaults of the selected protocol. Check them before you click _OK_.

:::
 
### Proxy

![IMAP4 Connection, Proxy tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IMAP4/Proxy.png)

When the Server reads email, it uses _Proxy type_, _Address_ and _Port_ and, when _Use credentials_ is selected, _Username_ and _Password_. It does not use _Authentication_ or _Domain_.
