---
sidebar_label: 'Connection - Exchange WebDAV'
hide_title: 'true'
---

## Connection - Exchange WebDAV

The Exchange WebDAV Connection stores the address, sign-in and security settings that the [Email - Send](job-tasks/messaging-tasks/email) Task, the [Email - Get Messages](job-tasks/messaging-tasks/email-get-messages), [Email - Get Single Message](job-tasks/messaging-tasks/email-get-single-message), [Email - Get Headers](job-tasks/messaging-tasks/email-get-headers), [Email - Delete Messages](job-tasks/messaging-tasks/email-delete-messages), [Email - Delete Single Message](job-tasks/messaging-tasks/email-delete-single-message) and Email - Move Messages Tasks and the [Email Trigger](event-trigger-mail) use to connect to Microsoft Exchange.

The email receiving Tasks and the Email Trigger read email through the WebDAV protocol of Exchange. The Email - Send Task sends email, and the Email Trigger forwards matching email, through this Connection. Select it only when the Exchange server offers WebDAV.

For MS Exchange interoperability, WebDAV can be used for reading/updating/deleting items in a mailbox or public folder. WebDAV for Exchange has been extended by Microsoft to accommodate working with messaging data. Exchange Server version 2000, 2003, and 2007 support WebDAV. However, WebDAV support has been discontinued in Exchange 2010 in favor of Exchange Web Services (EWS), a SOAP/XML based API.
 
### Common settings

![Exchange WebDAV Connection, Common settings tab with the Protocol and Information groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Exchange%20WebDAV/Main%20Settings.png)

The ***Common settings*** and ***Proxy*** tabs are the same for every Connection type that has them; see [Common settings](global-connections#common-settings) and [Proxy](global-connections#proxy).

_Test_

Opens the _Test SMTP Connection_ window. Enter an address in _From email_ and in _To email_, then click _Test_. The Server sends a real message through this Connection, with the subject "Test subject (from VisualCron)", to the _To email_ address. _Test_ checks sending only; it does not read the mailbox.
 
### Main settings

These fields are on ***Connection settings*** -> ***Main settings***.

The ***Connection settings*** tab holds three tabs: ***Main settings***, ***Encryption*** and ***Proxy***.

![Exchange WebDAV Connection, Main settings tab with the Server and Credentials groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Exchange%20WebDAV/Connection%20Settings.png)

_Address_

The DNS name or IP address of the Exchange server. Required.

_Port_

The port of the Exchange server. A new Connection opens with "21" in _Port_. Change it to the port of the Exchange server. _Port_ cannot be "0".

_Username_

The user name of the mailbox account. Required.

_Password_

The password of the mailbox account.

_Email_

The email address of the mailbox to work with. The email receiving Tasks and the Email Trigger open this mailbox.
 
### Encryption

![Exchange WebDAV Connection, Encryption tab with the SSL/TLS, Allowed SSL/TLS versions and SASL Mechanisms groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Exchange%20WebDAV/Encryption.png)

_Cryptographic protocol_

- "No encryption": the connection is not encrypted; the _Allowed SSL/TLS versions_ group is unavailable
- "SSL": SSL encryption; selects _SSL version 2_ and _SSL version 3_ in _Allowed SSL/TLS versions_
- "TLS": TLS encryption; selects _TLS version 1_ to _TLS version 1.3_ in _Allowed SSL/TLS versions_

The email receiving Tasks and the Email Trigger use _Cryptographic protocol_ when they read email. The Email - Send Task and _Test_ do not use _Cryptographic protocol_ or _Allowed SSL/TLS versions_ when they send email.

_Allowed SSL/TLS versions_

The available versions are _SSL version 2_, _SSL version 3_, _TLS version 1_, _TLS version 1.1_, _TLS version 1.2_ and _TLS version 1.3_. The email receiving Tasks do not read these boxes. When the Email Trigger checks the mailbox, the Server first sets the SSL and TLS versions for the whole Server process from them:

- "TLS": the selected boxes among _TLS version 1_, _TLS version 1.1_ and _TLS version 1.2_, or all three when none of them is selected; never _TLS version 1.3_
- "SSL" with _SSL version 3_ selected: the system default versions
- "SSL" with _SSL version 3_ cleared: _SSL version 3_ only

With "SSL" and _SSL version 3_ cleared, the whole Server process is limited to SSL 3, and other Tasks that connect over HTTPS can then fail.

:::note

Each time you open an existing Exchange WebDAV Connection, the version boxes reset to the defaults of the selected protocol. Check them before you click _OK_.

:::

_SASL Mechanisms_

Used by the Email - Send Task when it sends email. The Email - Send Task uses one mechanism: _NTLM_ when it is selected, otherwise _CRAM-MD5_ when it is selected. When both are cleared, the Email - Send Task does not set a mechanism, and one is chosen automatically. All three boxes are selected on a new Connection, so a new Connection sends with _NTLM_. _DIGEST-MD5_ is not used on its own.

- _NTLM_: Windows NT LAN Manager authentication
- _DIGEST-MD5_: challenge-response authentication with an MD5 digest
- _CRAM-MD5_: challenge-response authentication with MD5 hashing
 
### Proxy

![Exchange WebDAV Connection, Proxy tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Exchange%20WebDAV/Proxy.png)

When the Server reads email, it uses _Proxy type_, _Address_ and _Port_ and, when _Use credentials_ is selected, _Username_ and _Password_. It does not use _Authentication_ or _Domain_. When the Server sends email, from the Email - Send Task, the Email Trigger forward action or _Test_, it does not use the settings on this tab.
