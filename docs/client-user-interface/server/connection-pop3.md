---
sidebar_label: 'Connection - POP3'
hide_title: 'true'
---

## Connection - POP3

The POP3 Connection stores connect and logon properties for the email server protocol POP3. POP3 (Post Office Protocol 3) is used to receive emails from a mail server. It has largely been superseded by IMAP4 but is still widely supported. The POP3 Connection is used in the Email Trigger.

**Manage Connections > Add > POP3 > Common settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/POP3/POP3.png)

**Name**

The name of the Connection to uniquely identify it.

**Group**

The group that the connection is a part of.

**Timeout**

The connection timeout in seconds. Connection will fail after this time period.

**Code page**

Code page being used.

**Manage Connections > Add > POP3 > Connection settings** tab

![](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/POP3/Settings.png)

**Address**

The DNS name or IP address of the POP3 mail server.

**Port**

The port used by the mail server. The default port is 110 for unencrypted connections and 995 for SSL/TLS encrypted connections. The port is automatically updated when changing the cryptographic protocol on a new connection.

**Username**

The user name for the email account.

**Password**

The password for the email account.

**Cryptographic protocol**

The encryption protocol to use for the connection. Available options:

* _No encryption_ - connection is not encrypted; the Allowed SSL/TLS versions section is hidden
* _SSL_ - use SSL encryption; the Allowed SSL/TLS versions section is shown
* _TLS_ - use TLS encryption; the Allowed SSL/TLS versions section is shown

**Allowed SSL/TLS versions**

Visible when a cryptographic protocol is selected. Check the SSL/TLS versions that the mail server allows. Available options:

* _SSL version 2_
* _SSL version 3_
* _TLS version 1_
* _TLS version 1.1_
* _TLS version 1.2_
* _TLS version 1.3_

### Default settings for some servers

See [Connection > SMTP > Main settings](connection-smtp) for more details.
 
**Connection > POP3 > Authentication** tab
See [Connection > SMTP > Authentication](connection-smtp) for more details.

**Office 365**

[https://support.office.com/en-nz/article/Settings-for-POP-and-IMAP-access-for-Office-365-for-business-or-Microsoft-Exchange-accounts-7fc677eb-2491-4cbc-8153-8e7113525f6c](https://support.office.com/en-nz/article/Settings-for-POP-and-IMAP-access-for-Office-365-for-business-or-Microsoft-Exchange-accounts-7fc677eb-2491-4cbc-8153-8e7113525f6c)

* Address: outlook.office365.com
* Port: 995
* Cryptographic protocol: SSL

**Manage Connections > Add > POP3 > Proxy** tab

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
