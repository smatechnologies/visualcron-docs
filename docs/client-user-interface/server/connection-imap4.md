---
sidebar_label: 'Connection - IMAP4'
hide_title: 'true'
---

## Connection - IMAP4

The IMAP Connection stores connect and logon properties for the email server protocol IMAP4. The IMAP4 protocol is used to receive email. The IMAP Connection is used in the Email Trigger.
 
**Manage Connections > Add > IMAP4 > Common settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IMAP4/IMAP.png)

**Test**

It is possible to test the connection once you have set all settings. Click the Test button to start the test.
 
**Name**

The unique name for the Connection.
 
**Timeout**

The connection timeout in seconds. Connection will fail after this time is passed.
 
**Code page**

The table of values that describes the desired character set. Currently this is overridden by the code page in the Task.

**Manage Connections > Add > IMAP4 > Connection settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IMAP4/Settings.png)

**Address**

The DNS name or IP address of the email server.
 
**Port**

The port used by the email server. Please note that it should match the port of the encryption. Normally encrypted connections uses port 993 while email servers with no encryption uses port 143.

**Authentication type**

The method used to authenticate with the email server.

* _Default_ - authenticate using a username and password
* _OAuth_ - authenticate using OAuth; the Username label changes to _Application Id_ and the Password label changes to _Client secret_. A _Setup app_ link and an _Authenticate_ link are also shown to guide the OAuth app configuration process

**Anonymous**

When checked, disables the Username and Password fields. Please note that anonymous access to a shared mailbox is not supported in the IMAP protocol. Use Exchange Connection instead.

**Username**

The user name for the email account. When Authentication type is set to _OAuth_, this field is labeled _Application Id_.
 
**Password**

The password for the email account. When Authentication type is set to _OAuth_, this field is labeled _Client secret_.
 
### Default settings for some servers:

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
 
**Manage Connections > Add > IMAP4 > Connection settings > Encryption** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IMAP4/Encryption.png)

**Cryptographic protocol**

The encryption protocol to use.

* _No encryption_ - connection is not encrypted
* _SSL_ - use SSL encryption
* _TLS_ - use TLS encryption
 
**Allowed SSL/TLS versions**

Some IMAP4 servers require certain versions of SSL/TLS. Check the versions that are allowed. The available options are:

* _SSL version 2_
* _SSL version 3_
* _TLS version 1_
* _TLS version 1.1_
* _TLS version 1.2_
* _TLS version 1.3_
 
**Manage Connections > Add > IMAP4 > Connection settings > Proxy** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/IMAP4/Proxy.png)

**Proxy type**

Select the proxy type to be used.
 
**Address**

The host name or IP address of the proxy server.
 
**Port**

The port of the proxy server.
 
**Use credentials**

Enable to provide credentials for authenticating with the proxy server.
 
**Domain**

The domain of the proxy server.
 
**Username**

The user name to access the proxy server.
 
**Password**

The password to access the proxy server.
