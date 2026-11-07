---
sidebar_label: 'Connection - POP3'
hide_title: 'true'
---

## Connection - POP3

The POP3 Connection stores the address, sign-in and security settings that the [Email - Get Messages](job-tasks/messaging-tasks/email-get-messages), [Email - Get Single Message](job-tasks/messaging-tasks/email-get-single-message), [Email - Get Headers](job-tasks/messaging-tasks/email-get-headers), [Email - Delete Messages](job-tasks/messaging-tasks/email-delete-messages), [Email - Delete Single Message](job-tasks/messaging-tasks/email-delete-single-message) and Email - Move Messages Tasks use to connect to a mail server over Post Office Protocol 3 (POP3).

The [Email Trigger](event-trigger-mail) does not offer POP3 Connections. It offers IMAP4, Exchange EWS, Exchange WebDAV and Microsoft Graph API Connections.

### Common settings

![POP3 Connection, Common settings tab with the Protocol and Information groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/POP3/POP3.png)

The ***Common settings*** and ***Proxy*** tabs are the same for every Connection type that has them; see [Common settings](global-connections#common-settings) and [Proxy](global-connections#proxy).

_Test_

The Server connects to the mail server and logs on with the settings of this Connection, then disconnects. No email is read or changed.

### Main settings

These fields are on ***Connection settings*** -> ***Main settings***.

The ***Connection settings*** tab holds two tabs: ***Main settings*** and ***Proxy***.

![POP3 Connection, Main settings tab with the Server, Credentials and SSL/TLS groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/POP3/Settings.png)

_Address_

The DNS name or IP address of the POP3 server.

_Port_

The port of the POP3 server. On a new Connection, the port is "110". It changes to "995" when you select "SSL" or "TLS", and back to "110" when you select "No encryption". With "TLS", change the port to "110". Port "995" expects encryption from the start, so use it with "SSL".

_Username_

The user name of the email account. Required.

_Password_

The password of the email account. The POP3 Connection logs on with a user name and password only. It has no OAuth authentication type.

_Cryptographic protocol_

- "No encryption": the connection is not encrypted; the _Allowed SSL/TLS versions_ group is hidden
- "SSL": SSL encryption; selects _SSL version 2_ and _SSL version 3_ in _Allowed SSL/TLS versions_
- "TLS": TLS encryption; selects _TLS version 1_ to _TLS version 1.3_ in _Allowed SSL/TLS versions_

The email receiving Tasks use _Cryptographic protocol_ when they read email. With "SSL", they encrypt the connection from the start. With "TLS", they connect in plain text and then switch to encryption.

_Allowed SSL/TLS versions_

Shown when "SSL" or "TLS" is selected. The available versions are:

- _SSL version 2_
- _SSL version 3_
- _TLS version 1_
- _TLS version 1.1_
- _TLS version 1.2_
- _TLS version 1.3_

The email receiving Tasks do not read these boxes. When you click _Test_, the Server first sets the SSL and TLS versions for the whole Server process from them:

- "TLS": the selected boxes among _TLS version 1_, _TLS version 1.1_ and _TLS version 1.2_, or all three when none of them is selected; never _TLS version 1.3_
- "SSL" with _SSL version 3_ selected: the system default versions
- "SSL" with _SSL version 3_ cleared: _SSL version 3_ only

With "SSL" and _SSL version 3_ cleared, the whole Server process is limited to SSL 3, and other Tasks that connect over HTTPS can then fail.

:::note

Each time you open an existing POP3 Connection, the version boxes reset to the defaults of the selected protocol. Check them before you click _OK_.

:::

### Default settings for some servers

**Office 365**

[https://support.office.com/en-nz/article/Settings-for-POP-and-IMAP-access-for-Office-365-for-business-or-Microsoft-Exchange-accounts-7fc677eb-2491-4cbc-8153-8e7113525f6c](https://support.office.com/en-nz/article/Settings-for-POP-and-IMAP-access-for-Office-365-for-business-or-Microsoft-Exchange-accounts-7fc677eb-2491-4cbc-8153-8e7113525f6c)

* Address: outlook.office365.com
* Port: 995
* Cryptographic protocol: SSL

### Proxy

When the Server reads email, it uses _Proxy type_, _Address_ and _Port_ and, when _Use credentials_ is selected, _Username_ and _Password_. It does not use _Authentication_ or _Domain_.
