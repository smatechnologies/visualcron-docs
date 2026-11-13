---
sidebar_label: 'Global - Certificates'
hide_title: 'true'
---

## Global - Certificates

A certificate binds a public key to an identity, such as a person, a company or a server, and is signed so that others can check that binding. VisualCron stores standard X.509 certificates centrally on the Server, so that the Email Task (see [Task Messaging - Email](job-tasks/messaging-tasks/email)) and Connections that authenticate with a certificate can reuse them. This page describes the _Manage certificates_ window, where you import, export, create and delete certificates.

To open the window, click the main menu **_Server_** -> _Global objects_ -> _Certificates_. You need the _Certificates_ permission with _Read_ (see [Permissions](#permissions) below).

![The main menu Server tab with Certificates selected in the Global objects group, and the Manage certificates window that it opens, listing three certificates](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Certificates/Global%20-%20Certificates.png)

The grid has these columns:

- _VCName_: the name that identifies the certificate inside VisualCron. Change it with _Set name_
- _Common Name_: the common name in the certificate's subject
- _Email_: the email address in the certificate's subject
- _Issuer Name_: currently stays empty in this window
- _Self signed_: "Yes" when the certificate is self-signed
- _Private key_: "Yes" when the certificate includes its private key
- _Can encrypt_: "Yes" when the certificate can be used for encryption
- _Can sign_: "Yes" when the certificate can be used for signing
- _Key valid_: "Yes" when the certificate's key is valid

The toolbar has these buttons, from left to right: _Import certificate_, _Export certificate_, _Create certificate_, _Delete certificate_, _Audit log_ and _Get from Windows_. Each is described below.

Right-click a row for these commands:

- _Set name_: change the name in _VCName_, in the _Set certificate name_ window
- _Copy Certificate Id_: copy the certificate's identifier to the clipboard
- _Change Certificate Id_: enter a new identifier in _Enter new Certificate Id_. The new identifier must be in GUID format, and no other certificate may already use it. VisualCron tells you how many objects will change with it. Click _Yes_ to continue, or _No_ to see the list first. The objects that use the certificate are updated to the new identifier
- _Audit log_: the audit log entries of this certificate
- _Versions.._: the version history of the certificate
- _Object relations_: the objects that use the certificate
- _Export ..._: export the selected certificates (see [Import/Export - Export Settings](../file/export-settings))
- _Send to connection ..._ and _Send to server connection ..._: copy the certificate to the Server that a VisualCron Connection points to, or to another Server this Client is connected to

In the grid, press Delete to delete the selected certificate, or Ctrl+A to select every row.

### Import certificate

:::note

The file is read by the Client, on the computer it runs on. When the Client is connected to a Server on another computer, the file window shows the Server's folders. The file is then usually not found, or a file with the same path on the Client computer is read instead. In that case, the file type you select is also ignored: every file is read as a binary ".cer" or ".der" certificate, so a ".pem", ".pfx" or ".p12" file can't be imported. Import certificate files from a Client running on the Server computer.

:::

Click _Import certificate_ and select a certificate file. Select the file type in the file window to see your files:

- _Binary Encoded Certificate (\*.cer;\*.der)_
- _PKCS7 SPC (\*.spc)_
- _PEM Encoded Certificate (\*.pem)_
- _PKCS12 Certificate (\*.pfx;\*.p12)_
- _Binary Encoded Certificate - Public key only (\*.pub;)_

To import a private key together with a ".cer", ".der" or ".spc" certificate, place the key in the same folder, under the same name with the extension ".key" or ".pvk". VisualCron then asks _Do you want to load the private key file ...?_. For a ".pvk" file, it also asks for the key's password in the _Enter password_ window. You can't select a ".key" or ".pvk" file directly.

For a ".pem", ".pfx" or ".p12" file, VisualCron asks for the file's password in the _Enter password_ window.

### Export certificate

:::warning

If you leave the password empty, or cancel the _Enter password_ window, the private key is saved without a password, and anyone who gets the file can use the key. Always enter a password.

The ".key" file of a ".cer" export holds the private key without a password. Keep it in a protected place.

:::

:::note

The file is written by the Client, on the computer it runs on. When the Client is connected to a Server on another computer, the save window shows the Server's folders, but the file is written to that path on the Client computer. In that case, the file type you select is also ignored: the certificate is always saved as a binary ".cer" file, and if you click _Yes_ for _Save private key?_, the private key is saved without a password. Export certificate files from a Client running on the Server computer.

:::

Select a certificate and click _Export certificate_. Select the file type in the save window:

- _Binary Encoded Certificate (\*.cer)_: if the certificate has a private key, VisualCron asks _Save private key?_. If you click _Yes_, the key is saved in a ".key" file with the same name
- _PEM Encoded Certificate (\*.pem)_: if the certificate has a private key, VisualCron asks for a password in the _Enter password_ window, and saves the key protected with it
- _PKCS12 Certificate (\*.pfx)_: if the certificate has a private key, VisualCron asks for a password in the same way

### Get from Windows

To import certificates from a Windows certificate store, complete the following steps:

1. Click _Get from Windows_. The _Import certificates_ window opens.
2. In _Certificates store type:_, select the store: "My", "Root", "AuthRoot", "Address book", "Certificate authority", "Trusted people" or "Trusted publisher".
3. Select _Local machine_ (the default) or _Current user_. On the Server computer, _Current user_ is the store of the account that the VisualCron Server service runs as.
4. Choose the computer whose store is read. Check the box to read the store on the computer running the Client, or leave it cleared to read the store on the Server computer. When the window opens, the cleared box reads _From client machine_. After you change it, its label shows the current choice: _From client machine_ or _From server machine_.
5. Click _Get_. The certificates in the store are listed. Double-click a row to see its details.
6. Check the certificates you want, or use the checkbox in the column header to check them all, and click _Import_.

The certificates you checked are added to the grid of the _Manage certificates_ window. Only the certificate is imported, not its private key. To import a private key, export the certificate with its private key from Windows as a ".pfx" file, and use _Import certificate_.

### Create certificate

:::warning

The wizard preselects _md2 / RSA_ and a public key strength of "512" bits. Both are too weak for current use, and certificates made with them are not secure. Select _sha256 / RSA_ and "2048" or "4096" bits for every certificate you create.

:::

Click _Create certificate_ to open the _Certificate generation_ wizard. VisualCron creates self-signed certificates.

#### Step 1: name and type

Enter a name in _Name:_. The name identifies the certificate inside VisualCron, is shown in the _VCName_ column, and is required. Under _Type of Certificate_, _Self-signed certificate_ is the only option.

![The Manage certificates window with the Create certificate button highlighted, and the first page of the Certificate generation wizard with the Name box and the Self-signed certificate option](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Certificates/Manage%20Certificates.png)

#### Step 2: hash algorithm and key strength

![The second page of the Certificate generation wizard, with md2 / RSA selected under Hash algorithm and 512 selected under Public key strength (bits)](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Certificates/Certificate%20Creation%202.png)

- _Hash algorithm_ offers _md2 / RSA_ (preselected), _md5 / RSA_, _sha1 / RSA_, _sha1 / DSA_, _sha256 / RSA_ and _sha256 / DSA_
- _Public key strength (bits)_ offers "256", "512" (preselected), "768", "1024", "2048" and "4096"

#### Step 3: subject information

![The third page of the Certificate generation wizard, with the fields Email, Country, State/Province, Locality, Organization, Organization unit and Common name](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Certificates/Certificate%20Creation%203.png)

Under _Subject info for new certificate_, fill in _Country:_, _State/Province:_, _Locality:_, _Organization:_, _Organization unit:_ and _Common name:_. These are required. _Email:_ is optional.

:::tip

Fill in _Email:_ if you will use the certificate in the Email Task (see [Task Messaging - Email](job-tasks/messaging-tasks/email)).

:::

#### Step 4: validity period

![The fourth page of the Certificate generation wizard, with the From and To dates of the validity period](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Certificates/Certificate%20Creation%204.png)

Under _Validity period for certificate_, _From:_ starts at today's date and _To:_ starts at one year from today. Change them as needed.

Click _Next >_ to create the certificate. The request is sent to the Server, and the wizard closes. The _Generation started_ message tells you that the certificate appears when it has been created. This can take up to five minutes, depending on the key size and the Server's speed. When the certificate is ready, it appears in the grid, and a message says that it was generated successfully.

![The Generation started message, saying that the request was sent to the Server and that the new certificate appears when it has been created](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20Certificates/Certificate%20Creation%205.png)

To leave the wizard without creating a certificate, click _Cancel_ and confirm.

### Delete certificate

Select a certificate and click _Delete certificate_, or press Delete. VisualCron asks you to confirm. If other objects use the certificate, the question says how many, and you can open _Object relations_ first to see them.

### Permissions

Certificates are governed by the _Certificates_ permission (see [Main - User Permissions](main-user-permissions) and [Supported Permissions](supported-permissions)):

- _Read_: open the _Manage certificates_ window and see the certificates, and also export a certificate with its private key
- _Add_: _Import certificate_, _Create certificate_ and importing with _Get from Windows_
- _Edit_: _Set name_ and _Change Certificate Id_. Without _Edit_, a new name is not saved, and no message is shown
- _Delete_: _Delete certificate_

The file windows for import and export also need the _Remote file explorer_ permission with _Read_.

:::warning

_Read_ alone lets a user export a certificate together with its private key. The built-in Viewers group has _Read_ on _Certificates_. Clear it in the Viewers group, and give _Read_ on _Certificates_ only to users you trust with the private keys.

:::

### Certificate file formats

| Format | Import | Export | Private key |
|---|---|---|---|
| PFX or P12 (PKCS #12) | Yes. VisualCron asks for the file's password | Yes, as .pfx. VisualCron asks for a password | In the same file, protected with the password |
| PEM | Yes. VisualCron asks for the file's password | Yes, as .pem. VisualCron asks for a password | In the same file, protected with the password |
| CER or DER | Yes | Yes, as .cer | In a separate .key file. On import, a .pvk file is also accepted |
| SPC (PKCS #7) | Yes | No | In a separate .key or .pvk file |
| PUB | Yes, public key only | No | None |
