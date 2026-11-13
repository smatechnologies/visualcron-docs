---
sidebar_label: 'Task Messaging - Email'
hide_title: 'true'
---

## Task Messaging - Email - Send

The Email - Send Task sends a text or HTML message, with optional attachments, to one or more recipients, using an SMTP, Exchange EWS, Exchange WebDAV or Microsoft Graph API Connection. The message can be signed and encrypted with S/MIME or PGP/MIME.

![Email - Send tab, Main settings tab with the Basic settings, Security and Message type groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send.png)

:::warning

This Task uses an SMTP, Exchange EWS, Exchange WebDAV or Microsoft Graph API Connection; see [Connection - SMTP](../../connection-smtp), [Connection - Exchange EWS](../../connection-exchange-ews), [Connection - Exchange WebDAV](../../connection-exchange-webdav) and [Connection - Microsoft Graph API](../../connection-microsoft-graph-api). With an SMTP Connection that uses "Default" authentication, the Task accepts any server certificate. The Task does not use the proxy set on the Connection.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Email - Send: Main settings tab

- _Connection_: the Connection to send through, of one of these types: [Connection - SMTP](../../connection-smtp), [Connection - Exchange EWS](../../connection-exchange-ews), [Connection - Exchange WebDAV](../../connection-exchange-webdav) or [Connection - Microsoft Graph API](../../connection-microsoft-graph-api)

- _Subject_: the subject of the message. Variables are resolved
- _From name_: the sender name that recipients see. Required

  If the field is empty when the Task window opens, it is filled with _From name_ from [Settings - Email Settings](../../settings-email-settings).

- _From email_: the sender address. Required

  If the field is empty when the Task window opens, it is filled with _From email_ from [Settings - Email Settings](../../settings-email-settings).

- _Reply to email_: the address that replies go to

  If the field is empty when the Task window opens, it is filled with _From email_ from [Settings - Email Settings](../../settings-email-settings). To send without a separate reply address, clear the field before you save the Task. The field is filled again each time the Task window opens, so clear it each time you edit the Task.

- _Priority_: "Low", "Normal" (default) or "High". How the priority is shown depends on the recipient's mail program

- _Security_: how the message is signed or encrypted
  - _Do not use security features for this message_ (default): the message is neither signed nor encrypted
  - _Use S/MIME security features_: enables the ***Sign*** and ***Encrypt*** tabs with S/MIME settings
  - _Use PGP/MIME security features_: enables the ***Sign*** and ***Encrypt*** tabs with PGP/MIME settings

:::warning

PGP/MIME signing and encryption are applied only with an SMTP Connection that uses "Default" authentication. With an Exchange EWS, Exchange WebDAV or Microsoft Graph API Connection, or an SMTP Connection that uses "Gmail OAuth", a message set to PGP/MIME is sent unsigned and unencrypted. With these Connections, S/MIME ignores _Sign clear format_ and _Sign root header_, and matches encryption certificates to To addresses only.

:::

- _Message type_: the parts of the message
  - _Send Text_: sends the plain text body from the ***Text*** tab. Selected by default
  - _Send HTML_: sends the HTML body from the ***HTML*** tab, and enables the ***HTML*** and ***Chrome preview*** tabs
  - _Request delivery receipt_: asks for a delivery notification from the mail system
  - _Request read receipt_: asks the recipient's mail program for a read confirmation when the message is opened

  With both _Send Text_ and _Send HTML_ selected, the message carries both bodies, and the recipient's mail program shows one of them.

### Email - Send: Recipients tab

![Email - Send tab, Recipients tab with the To, Cc and Bcc groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Recipients.png)

- _Recipient separator_: the character between addresses, in the address fields and in recipient files: "Semicolon" (default), "Comma" or "Newline"
- _Send separate emails_: selected by default

  When selected, every To, Cc and Bcc address gets its own copy of the message, with only that address in To; the Cc and Bcc lines are not kept. If sending to one address fails, the error is written to standard error, the other addresses still get the message, and the Task ends with exit code 77777.

  When cleared, one message goes to all addresses. To and Cc addresses are visible to every recipient; Bcc addresses are not. If the send fails, the Task fails.

- _To.._, _Cc.._ and _Bcc.._: each group has a source list, an address field and a _Credential_ list. The sources are:
  - "Not used": the group is not used (default for Cc and Bcc)
  - "Manual": type the addresses in the field, separated by the _Recipient separator_ (default for To). Variables are resolved
  - "File": type the path of a text file that holds the addresses, separated by the _Recipient separator_. _Credential_ is enabled, and is used to read the file

  The Task window requires at least one group that is not "Not used", and an address in at least one field.

  With an SMTP Connection that uses "Default" authentication, spaces are removed from every address, and Variables are resolved in the contents of a recipient file. With the other Connections, spaces are kept, and Variables in a recipient file are not resolved.

### Email - Send: Text tab

![Email - Send tab, Text tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Text.png)

Type the plain text body. The tab is enabled when _Send Text_ is selected. Variables are resolved. The message uses the character set of _Encoding_ on the Task window's ***Main settings*** tab.

### Email - Send: HTML tab

![Email - Send tab, HTML tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20HTML.png)

Type the HTML body. The tab is enabled when _Send HTML_ is selected. Variables are resolved.

### Email - Send: Chrome preview tab

![Email - Send tab, Chrome preview tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Chrome.png)

Shows how the HTML from the ***HTML*** tab is displayed. Variables are not resolved in the preview.

### Email - Send: Attachments tab

![Email - Send tab, Attachments tab with the attachment list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Attachments.png)

The list shows each attachment with its path and Credential. Click _Add_ to add an attachment, _Edit_ to change the selected one and _Delete_ to remove it. Each attachment is a [File Filter](../../job-tasks-file-filter), so one entry can attach several files. The Credential of the filter is used to read files on a protected location. For what happens when a filter finds no file, or a file cannot be read, see [Output and errors](#output-and-errors).

### Email - Send: Sign tab (PGP/MIME)

![Email - Send tab, Sign tab, shown with S/MIME settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Sign.png)

The tab is enabled when _Use PGP/MIME security features_ is selected in the _Security_ group.

- _Sign message_: signs the message
- _Use new features_: selected by default. When selected, newer and stronger algorithms are used. When cleared, the result is compatible with PGP 2.6.x
- _Choose key ring_: the key ring with the private key to sign with. The whole key ring is used; no key is matched to _From email_. The grid lists the keys of the selected key ring
- _Manage key rings_: opens the PGP key rings, where you create or import key rings; see [Global - PGP Key Rings](../../global-pgp-key-rings)
- _Password_: the passphrase of the private key, if it has one

### Email - Send: Sign tab (S/MIME)

![Email - Send tab, Sign tab with S/MIME settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Sign.png)

The tab is enabled when _Use S/MIME security features_ is selected in the _Security_ group.

- _Sign message_: signs the message
- _Sign clear format_: selected by default

  When selected, the message is sent as "multipart/signed": every mail program can show it, and programs that support S/MIME can check the signature. When cleared, the message is sent as "application/pkcs7-mime" signed data: it is better protected against changes on its way through mail servers, but only programs that support S/MIME can show it.

- _Sign root header_: when selected, header fields of the message, such as the subject, are signed too; From, To, Sender and Reply-To are not
- _Choose certificate_: select exactly one certificate in the _Use_ column. Only certificates that can sign are listed
- _Manage certificates_: opens the certificates, where you create or import certificates; see [Global - Certificates](../../global-certificates)

_Sign clear format_ and _Sign root header_ apply only with an SMTP Connection that uses "Default" authentication. The signature uses SHA-1 with an SMTP Connection that uses "Default" authentication, and SHA-256 with the other Connections. The algorithm cannot be changed.

### Email - Send: Encrypt tab (PGP/MIME)

![Email - Send tab, Encrypt tab, shown with S/MIME settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Encrypt.png)

The tab is enabled when _Use PGP/MIME security features_ is selected in the _Security_ group.

- _Encrypt message_: encrypts the message
- _Choose key ring_: the key ring with the recipients' public keys. The message is encrypted to every public key in the key ring; no key is matched to a recipient address. Use a key ring that holds only the keys of the intended recipients
- _Manage key rings_: opens the PGP key rings; see [Global - PGP Key Rings](../../global-pgp-key-rings)

### Email - Send: Encrypt tab (S/MIME)

![Email - Send tab, Encrypt tab with Encrypt message selected and the S/MIME certificate list](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Messaging%20Tasks/Email%20-%20Send%20Encrypt%20with%20Key.png)

The tab is enabled when _Use S/MIME security features_ is selected in the _Security_ group.

- _Encrypt message_: encrypts the message
- _Choose certificate(s)_: select one or more recipient certificates in the _Use_ column. Only certificates that can encrypt are listed
- _Manage certificates_: opens the certificates; see [Global - Certificates](../../global-certificates)

With an SMTP Connection that uses "Default" authentication, the message is encrypted for every selected certificate. With the other Connection types, each selected certificate is used only for the first To address that the email address in the certificate is equal to or ends with; the comparison is case-sensitive. Cc and Bcc addresses never get a certificate, also when _Send separate emails_ sends each of them its own copy. Encryption uses 3DES, which cannot be changed.

### Output and errors

Standard output lists each address that the message was sent to. The Task ends with an error in these cases:

- No address in any recipient group: "No recipients were specified." is written to standard error, no message is sent, and the exit code is 77777
- The recipient file does not exist: "Recipient file did not exist." is written to standard error, no message is sent, and the exit code is 77777
- A file that an attachment's file filter finds cannot be read: the error is written to standard error, no message is sent, and the exit code is 77777
- With _Send separate emails_, sending to one address fails: the error is written to standard error, the other addresses still get the message, and the exit code is 77777
- The Connection is missing: the Task fails with "Connection not found" or "No Connection was selected"

Exit code 77777 is handled by the "Non zero exit code" cause on the ***On error*** tab, unless an _Exit code collection_ other than the default is selected there; see [Task - On Error](../../task-on-error).

:::warning

If _Use PGP/MIME security features_ is selected with a Connection that does not apply PGP/MIME (see _Security_), the message is sent unsigned and unencrypted, and the Task reports success.

With an Exchange EWS, Exchange WebDAV or Microsoft Graph API Connection, or an SMTP Connection that uses "Gmail OAuth", if the S/MIME signing certificate is no longer in [Global - Certificates](../../global-certificates), or cannot sign, the message is sent unsigned, and the Task reports success. With an SMTP Connection that uses "Default" authentication, a missing signing certificate makes the Task fail.

If the file filter of an attachment finds no matching file in a folder that exists, the message is sent without that attachment, and the Task reports success.

:::
