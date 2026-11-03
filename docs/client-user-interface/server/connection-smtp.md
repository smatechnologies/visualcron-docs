---
sidebar_label: 'Connection - SMTP'
hide_title: 'true'
---

## Connection - SMTP

The SMTP Connection stores the address, sign-in and security settings that the [Email - Send](job-tasks/messaging-tasks/email) Task and the [Email Trigger](event-trigger-mail) use to connect to a mail server over Simple Mail Transfer Protocol (SMTP). The Email - Send Task sends email through it, and the Email Trigger forwards matching email through it.
 
### Common settings

![SMTP Connection, Common settings tab with the Protocol and Information groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SMTP/SMTP.png)

The ***Common settings*** and ***Proxy*** tabs are the same for every Connection type that has them; see [Common settings](global-connections#common-settings) and [Proxy](global-connections#proxy).

_Test_

Opens the _Test SMTP Connection_ window. Enter an address in _From email_ and in _To email_, then click _Test_. The Server connects with the settings of this Connection and sends a real message, with the subject "Test subject (from VisualCron)", to the _To email_ address. With "Gmail OAuth", click _Authenticate_ before you test.

### Main settings

These fields are on ***Connection settings*** -> ***Main settings***.

The ***Connection settings*** tab holds three tabs: ***Main settings***, ***Encryption*** and ***Proxy***.

![SMTP Connection, Main settings tab with the Server and Credentials groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SMTP/Settings.png)

_Address_

The DNS name or IP address of the SMTP server. Enter the full DNS name, not a short server name.

_Port_

The port of the SMTP server. A new Connection starts at "25". The port must match the settings on the ***Encryption*** tab. Mail servers usually use "25" without encryption, "587" with "TLS" and "Explicit", and "465" with "Implicit".

#### Default settings for some servers

**Exchange**

- _Address_: the full DNS name of the Exchange server
- _Port_: "587"
- _Cryptographic protocol_: "TLS"
- _Security mode_: "Explicit"
 
**Office 365 (Deprecated after April 2026 by [Microsoft](https://techcommunity.microsoft.com/blog/exchange/exchange-online-to-retire-basic-auth-for-client-submission-smtp-auth/4114750))**

Main settings
* Address: smtp.office365.com
* Port: 587
 
Encryption
* Cryptographic protocol: TLS (1.2)
* Security Mode: Explicit
 
**Gmail**

- _Address_: "smtp.gmail.com"
- With "Default" authentication: _Port_ "465", _Cryptographic protocol_ "TLS", _Security mode_ "Implicit"
- With "Gmail OAuth": _Port_ "587", _Cryptographic protocol_ "TLS"

**Amazon SES**

- _Address_: "email-smtp.us-east-1.amazonaws.com", or the Amazon SES SMTP address of your region
- _Port_: "465"
- _Cryptographic protocol_: "TLS" (TLS 1.2)
- _Security mode_: "Implicit"

#### Authentication

_Authentication type_

How the Connection logs on to the server:

- "Default": a user name and password
- "Gmail OAuth": Google OAuth, for Gmail and Google Workspace accounts

The Email Trigger forward action always logs on as with "Default". To forward email from the Email Trigger, use an SMTP Connection with "Default" authentication.

_Anonymous_

Sends email without logging on. When selected, _Username_ and _Password_ are unavailable. Shown only with "Default".

_Username_

The user name of the email account. Required unless _Anonymous_ is selected. With "Gmail OAuth", this field is labeled _Application Id_ and holds the client ID of your Google OAuth client.

_Password_

The password of the email account. With "Gmail OAuth", this field is labeled _Client secret_ and holds the client secret of your Google OAuth client.

_Setup app_

Shown with "Gmail OAuth". Opens the Google API Console in the web browser, where you create the OAuth client.

_Authenticate_

Shown with "Gmail OAuth". Opens the Google sign-in page in the web browser. When sign-in succeeds, the authorization is saved in the Connection, and the Server sends email as the Google account that signed in.

_App settings_

Shown with "Gmail OAuth". Of the fields in this group, only _Redirect Url_ is used with Google. _Tenant Id_, _Tenant Primary Domain_, _Tenant Name_ and _Auto-accept server certificates_ are not used.

_Redirect Url_ is the address that receives the reply from Google after sign-in, on the computer that runs the Client. It is required for _Authenticate_. Enter a local address such as "http://localhost:9999", and add the same address as an authorized redirect URI in the Google OAuth client.

To set up "Gmail OAuth", complete the following steps:

1. In _Authentication type_, select "Gmail OAuth".
2. Click _Setup app_. The Google API Console opens.
3. In the Google API Console, create an OAuth client ID.
4. Add the address that you will enter in _Redirect Url_ as an authorized redirect URI of the OAuth client.
5. Enter the client ID in _Application Id_.
6. Enter the client secret in _Client secret_.
7. Enter the redirect address in _Redirect Url_.
8. On the ***Encryption*** tab, select "TLS" in _Cryptographic protocol_.
9. On ***Main settings***, enter "587" in _Port_.
10. Click _Authenticate_.
11. In the web browser, sign in with the Google account that sends the email.
12. Allow access.
13. Click _OK_.

The Connection now sends email as that Google account.

### Encryption

![SMTP Connection, Encryption tab with the SSL/TLS, Allowed SSL/TLS versions and SASL Mechanisms groups](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SMTP/Encryption.png)

With "Default" authentication, the Email - Send Task, the Email Trigger forward action and _Test_ use every setting on this tab. With "Gmail OAuth", the Email - Send Task and _Test_ use only _Cryptographic protocol_.

_Cryptographic protocol_

- "No encryption": plain SMTP; the _Allowed SSL/TLS versions_ group is unavailable
- "SSL": SSL encryption; selects _SSL version 2_ and _SSL version 3_ in _Allowed SSL/TLS versions_
- "TLS": TLS encryption; selects _TLS version 1_ to _TLS version 1.3_ in _Allowed SSL/TLS versions_

With "Gmail OAuth", "TLS" connects in plain text and then switches to encryption, so it needs port "587". "SSL" encrypts from the start, as on port "465".

:::warning

With "Default" authentication, the Server offers the mail server only the versions selected in _Allowed SSL/TLS versions_. Selecting "SSL" selects only _SSL version 2_ and _SSL version 3_, which are obsolete. A mail server that accepts only TLS refuses the connection, and Jobs that use the Connection fail. Select "TLS", or also select the TLS versions that the mail server supports.

:::

_Security mode_

Used with "Default" authentication.

- "Explicit": the connection starts in plain text and then switches to encryption
- "Implicit": the connection is encrypted from the start

On a new Connection, selecting "Implicit" changes _Port_ to "990". For an SMTP server that uses implicit encryption, change _Port_ to "465".

_Allowed SSL/TLS versions_

The SSL and TLS versions that the Server offers with "Default" authentication. Some servers accept only certain versions.

- _SSL version 2_
- _SSL version 3_
- _TLS version 1_
- _TLS version 1.1_
- _TLS version 1.2_
- _TLS version 1.3_

_SASL Mechanisms_

The SASL logon mechanisms that the Server may use with "Default" authentication when _Anonymous_ is cleared. All three are selected on a new Connection.

- _NTLM_
- _DIGEST-MD5_
- _CRAM-MD5_

:::warning

With "Default" authentication, the Server does not check the SMTP server's certificate. "SSL" and "TLS" encrypt the session, but do not confirm that the server is the one named in _Address_. Use the Connection only over a network that you trust.

:::
 
### Proxy

![SMTP Connection, Proxy tab](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Connections/SMTP/Proxy.png)

The Server does not use the settings on this tab for an SMTP Connection. The Email - Send Task, the Email Trigger forward action and _Test_ connect to the mail server directly.
  
### Troubleshooting

#### No authentication method enabled from those supported by the server

If the server accepts email without a logon, select _Anonymous_ on the ***Main settings*** tab.

#### Error 96260 when sending email or clicking Test

In _Address_, enter the full DNS name or the IP address of the server, not a short server name.
 
**User authentication failed: Unaccepted server reply for command AUTH PLAIN (_Gmail_)**

You need to allow less secure apps to access your Gmail account
Google may block sign-in attempts from some apps or devices that do not use modern security standards. Since these apps and devices are easier to break into, blocking them helps keep your account safe.
 
To disable this security feature:
 
* Sign in to Gmail
* Click here to access Less Secure App Access in My Account.
* Next to “Allow less secure apps: OFF,” select the toggle switch to turn ON.
 
This setting may not be available for:
 
Accounts with 2-Step Verification enabled: Such accounts require an application-specific password for less secure apps access.

G Suite users: This setting is hidden if your administrator has locked less secure app account access.

[https://myaccount.google.com/lesssecureapps](https://myaccount.google.com/lesssecureapps)
