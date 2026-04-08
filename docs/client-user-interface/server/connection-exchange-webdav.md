---
sidebar_label: 'Connection - Exchange WebDAV'
hide_title: 'true'
---

## Connection - Exchange WebDAV

The Exchange WebDAV Connection uses the Exchange WebDAV protocol which is similar to the IMAP protocol - but have more Exchange options in general. Select this protocol it it is implemented by the Exchange Server.

For MS Exchange interoperability, WebDAV can be used for reading/updating/deleting items in a mailbox or public folder. WebDAV for Exchange has been extended by Microsoft to accommodate working with messaging data. Exchange Server version 2000, 2003, and 2007 support WebDAV. However, WebDAV support has been discontinued in Exchange 2010 in favor of Exchange Web Services (EWS), a SOAP/XML based API.
 
**Manage Connections > Add > Exchange WebDAV > Common settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Exchange%20WebDAV/Main%20Settings.png)

**Test**

It is possible to test the connection once you have set all settings. Click the Test button to start the test.
 
**Name**

The unique name for the Connection.

**Group**

The group that the connection is a part of
 
**Timeout**

The connection timeout in seconds. Connection will fail after this time is passed.
 
**Code page**

The table of values that describes the desired character set. Currently this is overridden by the code page in the Task.
 
**Manage Connections > Add > Exchange WebDAV > Main settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Exchange%20WebDAV/Connection%20Settings.png)

**Address**

The DNS name or IP address of the email server.

**Port**

The port of the email server.

**Email**

The email address associated with the Exchange account.

**Username**

The user name for the email account.
 
**Password**

The password for the email account.

**SASL Mechanisms**

Select which SASL (Simple Authentication and Security Layer) mechanisms are allowed when authenticating with the server. Enable one or more of the following:

- CRAM-MD5 — challenge-response authentication using MD5 hashing.
- DIGEST-MD5 — challenge-response authentication using a more secure digest method.
- NTLM — Windows NT LAN Manager authentication, commonly used in Microsoft environments.
 
**Manage Connections > Add > Exchange WebDAV > Encryption** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Exchange%20WebDAV/Encryption.png)

**Cryptographic protocol**

Encryption protocol to use; No encryption, SSL or TLS.
 
**Allowed SSL/TLS versions**

Some Exchange WebDAV servers require certain versions of SSL/TLS. Check the versions that are allowed. Sometimes it is necessary to specify the specific allowed version.

- TLS version 1.3
- TLS version 1.2
- TLS version 1.1
- TLS version 1
- SSL version 3
- SSL version 2
 
**Manage Connections > Add > Exchange WebDAV > Proxy** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/Exchange%20WebDAV/Proxy.png)

**Proxy type**

Select the proxy type to be used.
 
**Address**

The host name or IP address of the proxy server.
 
**Port**

The port of the proxy server.
 
**Use credentials**

The credentials that are associated with the account.
 
**Domain**

The name of the domain to be created.
 
**Username**

The user name to access the proxy server.
 
**Password**

The password to access the proxy server.
