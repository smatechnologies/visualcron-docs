---
sidebar_label: 'Global - PGP Key Rings'
hide_title: 'true'
---

## Global - PGP Key Rings

VisualCron encrypts, decrypts and signs files with the OpenPGP standard in the PGP Encrypt and PGP Decrypt Tasks (see [Task Encryption - PGP Encrypt](job-tasks/encryption-tasks/pgp-encrypt) and [Task Encryption - PGP Decrypt](job-tasks/encryption-tasks/pgp-decrypt)). The keys these Tasks use are stored centrally on the Server, in key rings. This page describes the _Manage PGP Key Rings_ window, where you create key rings, import, create, export and delete keys, and sign or revoke user IDs.

### How OpenPGP uses keys

Each person or system has a key pair. The public key can be shared, and the private key stays with its owner, protected by a password.

To encrypt a file for someone, you use their public key, and only their private key can decrypt the file. The file itself is encrypted with a random session key, and only that session key is encrypted with the public key, because that is much faster.

To sign a file, you use your own private key, and others check the signature with your public key.

### Key rings in VisualCron

A key ring is a named set of public and private keys, stored on the Server. Instead of pointing a Task to key files, you create or import the keys once into a key ring. In the PGP Encrypt Task, you then select the key ring, and pick the keys from it on the **_Recipients_** and **_Signers_** tabs.

To open the window, click the main menu **_Server_** -> _Global objects_ -> _PGP Key Rings_. You need the _PGP Key Rings_ permission with _Read_ (see [Permissions](#permissions) below).

![The Manage PGP Key Rings window with an empty list of key rings, and the toolbar with Add, Edit, Delete, the key buttons and Audit log](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20PGP%20Key%20Rings/PGP%20Key%20Rings.png)

The window lists each key ring with its keys. Under each key are its user IDs and subkeys, and under those their signatures. A revoked key is marked "[Revoked]", and a subkey is shown with its algorithm and "[subkey]". A signature is shown as "Signature", or as "Revocation" when it revokes.

:::warning

_Delete key_, and the Delete key on the keyboard when a key is selected, delete the key at once, without asking. Export the key first if you may need it again.

:::

:::warning

The Server keeps these changes in memory at first: creating, importing and deleting keys, signing and revoking user IDs, and renaming a key ring. It writes them to disk when the VisualCron service stops normally, or when a key ring is added, deleted or given a new identifier. If the Server stops unexpectedly before then, these changes are lost.

After you create or import a private key, export it with _Export private key_ and keep the copy in a safe place.

:::

The toolbar has these buttons:

- _Add_: opens the _Add PGP Key Ring_ window (see [Add a key ring](#add-a-key-ring))
- _Edit_: with a key ring selected, opens the _Edit Key Ring_ window to rename it. Click _Copy PGP Key Ring Id_ there to copy the key ring's identifier. To change the identifier, right-click the link and enter a new identifier in GUID format that no other key ring uses. The objects that use the key ring are updated
- _Delete_: deletes the key ring that contains the selection, after you confirm, even when a key inside it is selected. If other objects use the key ring, the question says how many
- _Import key(s)_: with a key ring selected, imports a key file into it (see [Import keys](#import-keys))
- _Export public key_: with a key selected, saves its public key in an ".asc" file on the computer running the Client
- _Export private key_: with a key that has a private key selected, saves the private key in an ".asc" file on the computer running the Client. The proposed file name ends with "-private". For a key without a private key, VisualCron shows an error
- _Create key_: with a key ring selected, opens the _Generate PGP key_ window (see [Create a key](#create-a-key))
- _Delete key_: deletes the selected key at once. Deleting a subkey on its own may not work. If the Server can't delete it, the subkey stays in the list, and no message is shown
- _Sign selected_ and _Revoke selected_: with a user ID selected, sign or revoke it (see [Sign or revoke a user ID](#sign-or-revoke-a-user-id))
- _Audit log_: the audit log entries for key rings

Right-click for the commands _Add key ring_, _Edit key ring_, _Delete key ring_, _Create key_, _Import key_, _Delete key_, _Audit log_, _Versions.._, _Object relations_, _Export ..._ (see [Import/Export - Export Settings](../file/export-settings)), _Send to connection ..._ and _Send to server connection ..._.

### Add a key ring

Click _Add_. In the _Add PGP Key Ring_ window:

- _Name/Description of VisualCron keyring_: a name that tells this key ring apart from the others. It is required
- Under _Creation options_, select one of these:
  - _Create blank keyring (add keys later)_
  - _Create keyring and import/paste keyring files/text_ (the default). Then choose one of these:
    - _Import from file(s)_ (the default): enter a _Public keyring file:_, a _Private keyring file:_, or both. The files are read by the Client, as described in [Import keys](#import-keys). From a Client connected to a Server on another computer, use _Paste key(s)_
    - _Paste key(s)_: paste the key text into _Public keyring:_ and _Private keyring:_

Click _OK_ to create the key ring.

### Import keys

:::note

Key files are read by the Client, on the computer it runs on. When the Client is connected to a Server on another computer, the file window shows the Server's folders. The file is then usually not found, or a file with the same path on the Client computer is read instead. Import key files from a Client running on the Server computer, or use _Paste key(s)_ when you add a key ring.

:::

Select a key ring and click _Import key(s)_, then select a key file. VisualCron reads the file as a private key first, and otherwise as a public key. It then says _Private key imported successfully._ or _Public key imported successfully._, or shows an error if the file holds neither. The message appears as soon as the Client has read the file, even if the Server then refuses the key, for example because you lack _Edit_ on _PGP Key Rings_. Check that the key appears in the key ring.

### Create a key

:::warning

The default strength of "512" bits is not secure today. Select "2048" or "4096" for new keys.

An empty password is accepted, but it leaves the private key unprotected. Always enter a password.

:::

Select a key ring and click _Create key_. In the _Generate PGP key_ window:

- Under _Select encryption_, select the key algorithm:
  - _RSA (encrypt or sign)_, the default: a single RSA key that can encrypt and sign
  - _RSA (encrypt only)_: an RSA signing key with a separate RSA encryption subkey
  - _RSA (Sign only)_: an RSA key for signing only
  - _ElGamal (encrypt only)_: a DSA signing key with a separate ElGamal encryption subkey
- _Strength:_ sets the key size in bits: "512" (the default), "1024", "1536", "2048" or "4096"
- _Expiry date:_ and _Never_ set when the key expires. _Never_ is checked by default, so the key does not expire. Clear _Never_ to set an expiry date. The date starts at one year from today and can't be earlier than today
- _Username:_ and _Email:_ together form the key's user ID: the user name, followed by the email address in angle brackets
- _Password:_ and _Repeat password:_ set the password that protects the private key. The two must match

Elliptic curve (ECC) keys are not offered.

Click _OK_. The key is generated on the computer running the Client, which can take a while for large keys, and is then added to the key ring on the Server. If generation fails, VisualCron shows the error and adds nothing. If the Server refuses the key, for example because you lack _Edit_ on _PGP Key Rings_, no message is shown. Check that the key appears in the key ring.

The encryption algorithm for your files is selected separately in the PGP Encrypt Task, where AES-256 is available (see [Task Encryption - PGP Encrypt](job-tasks/encryption-tasks/pgp-encrypt)).

:::tip

If you need a key with specific protection or preference settings, create it in a dedicated PGP tool, such as GnuPG or Kleopatra. Then import it into a VisualCron key ring with _Import key(s)_.

:::

### Sign or revoke a user ID

Select a user ID under a key, and click _Sign selected_ or _Revoke selected_. In the _Select key_ window, select the private key to sign or revoke with in _Private key:_, enter its password in _Password:_, and click _OK_. The Server signs or revokes the user ID and updates the key ring.

### Permissions

Key rings are governed by the _PGP Key Rings_ permission (see [Main - User Permissions](main-user-permissions) and [Supported Permissions](supported-permissions)):

- _Read_: open the _Manage PGP Key Rings_ window and see the key rings, and also _Export private key_
- _Add_: add a key ring with _Add_. _Import key(s)_ and _Create key_ need both _Add_ and _Edit_. Without _Edit_, the Server adds nothing, but after _Import key(s)_ the Client still reports success
- _Edit_: _Edit_, _Sign selected_ and _Revoke selected_
- _Delete_: _Delete_, in the Client. _Delete key_ needs _Delete_ and _Edit_. Without _Edit_, the key stays, and no message is shown

The file windows for import and export also need the _Remote file explorer_ permission with _Read_.

:::warning

_Read_ alone lets a user export a key together with its private key. The built-in Viewers group has _Read_ on _PGP Key Rings_. Clear it in the Viewers group, and give _Read_ on _PGP Key Rings_ only to users you trust with the private keys.

The Server doesn't check _Delete_ when a whole key ring is deleted. Only the Client checks it. Any logged-on user can therefore delete a key ring through the VisualCron API, whatever their _Delete_ permission. Give logons to the Server only to trusted users, and export the key rings you can't afford to lose.

:::
