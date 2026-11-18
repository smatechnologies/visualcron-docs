---
sidebar_label: 'Global - SSH Keys'
hide_title: 'true'
---

## Global - SSH Keys

SSH keys are used for public key authentication. A key pair is a private key, which stays with the client that logs on, and a public key, which you place on the remote server.

VisualCron stores SSH keys centrally on the Server. You can then select them in the SFTP, SCP and SSH Connections (see [Connection - SFTP](connection-sftp), [Connection - SCP](connection-scp) and [Connection - SSH](connection-ssh)), which Tasks such as the FTP Task use (see [Task Net - FTP/FTPS/SFTP/SCP](job-tasks/net-tasks/ftp)). You create or import a key once, instead of pointing every Connection to a key file. This page describes the _Manage SSH Keys_ window.

To open the window, click the main menu **_Server_** -> _Global objects_ -> _SSH keys_. You need the _SSH keys_ permission with _Read_ (see [Permissions](#permissions) below).

![The Manage SSH Keys window listing private and public keys, with the columns Name, Algorithm, Bits, Public Key and SHA256 Fingerprint, and the fingerprints blurred](../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Global%20Objects/Global%20-%20SSH%20Keys/SSH%20Keys.png)

The grid has these columns:

- _Name_: the name that identifies the key inside VisualCron
- _Algorithm_: "RSA", "DSS", "ECDSA" or "EDDSA"
- _Bits_: the key length
- _Public Key_: "True" for a public key, "False" for a private key
- _SHA256 Fingerprint_: the SHA256 fingerprint of the key, to check its identity

The toolbar has these buttons, from left to right: _Import public SSH key_, _Import private SSH key_, _Export SSH key_, _Create SSH key pair_, _Delete SSH key_ and _Audit log_. Each is described below.

Right-click a row for these commands:

- _Set name_: change the key's name, in the _Set SSH key name_ window
- _Copy SSH key Id_: copy the key's identifier to the clipboard
- _Change SSH key Id_: enter a new identifier in _Enter new SSH key Id_. The new identifier must be in GUID format, and no other SSH key may already use it. VisualCron tells you how many objects will change with it. Click _Yes_ to continue, or _No_ to see the list first. Currently, the change does not take effect on the Server: the key, and the objects that use it, keep the old identifier, and after a while VisualCron shows an error. The Clients that are logged on show the new identifier until they reconnect
- _Audit log_: the audit log entries of this key
- _Versions.._: the version history of the key
- _Object relations_: the objects that use the key
- _Export ..._: export the selected keys (see [Import/Export - Export Settings](../file/export-settings))
- _Send to connection ..._ and _Send to server connection ..._: copy the key to the Server that a VisualCron Connection points to, or to another Server this Client is connected to

In the grid, press Delete to delete the selected key, or Ctrl+A to select every row.

### Create SSH key pair

Click _Create SSH key pair_. In the _SSH key pair generation_ window, under _Key properties_:

- _Name:_ sets the name that identifies the key inside VisualCron. It starts as "NewKey"
- _Protocol type:_ sets the algorithm: "RSA" (the default), "DSS", "ECDSA" or "EDDSA"
- _Key length (bits):_ offers lengths that depend on the protocol type: "2048" (the default) or "4096" for "RSA" and "DSS", and "256" (the default) or "384" for "ECDSA"
- _Passphrase:_ sets the passphrase that protects the private key. It may be left empty

:::tip

Enter a passphrase. A key created without one is stored, and later exported, without protection.

:::

Click _Generate_. The Server creates the key pair and adds two rows to the grid: the private key under the name you entered, and the public key under the same name followed by ".pub". A message tells you when the new key has been generated. Export the public key to place it on the remote server.

To close the window without creating a key, click _Cancel_ and confirm.

### Import public SSH key

Click _Import public SSH key_ and select a public key file (".pub"). The key is stored under the file's name, extension included.

### Import private SSH key

Click _Import private SSH key_ and select a private key file. VisualCron first tries to import the key without a passphrase. If that fails, for example because the key is protected, it asks for the passphrase in the _Enter password_ window and tries again. The key is stored under the file's name.

:::note

The VisualCron Server, not the Client, reads the key file. Select a file on the Server computer, or on a share that the account the VisualCron Server service runs as can read. When the Client is connected to a Server on another computer, the file window shows the Server's folders. If the Server can't read the file, the import fails after the passphrase prompt, and the error says that the file does not exist or that access was denied.

:::

### Export SSH key

:::note

The file is written by the Client, on the computer it runs on. When the Client is connected to a Server on another computer, the save window shows the Server's folders, but the file is written to that path on the Client computer. Export keys from a Client running on the Server computer.

:::

Select a key and click _Export SSH key_, then choose where to save the file. A private key is saved protected with the passphrase stored with the key. A key that has no passphrase is saved without protection. A public key is saved in a ".pub" file. VisualCron says _Key exported._ when the file is written.

### Delete SSH key

Select a key and click _Delete SSH key_, or press Delete. VisualCron asks you to confirm. If other objects use the key, the question says how many, and you can open _Object relations_ first to see where the key is used.

### Permissions

SSH keys are governed by the _SSH keys_ permission (see [Main - User Permissions](main-user-permissions) and [Supported Permissions](supported-permissions)):

- _Read_: open the _Manage SSH Keys_ window and see the keys, and also export a key, private keys included
- _Add_: _Create SSH key pair_, _Import public SSH key_ and _Import private SSH key_
- _Edit_: _Set name_ and _Change SSH key Id_. Without _Edit_, a new name is not saved, and no message is shown
- _Delete_: _Delete SSH key_

The file windows for import and export also need the _Remote file explorer_ permission with _Read_.

:::warning

_Read_ alone lets a user export a key together with its private key.

The built-in Viewers group has _Read_, _Add_, _Edit_ and _Delete_ on _SSH keys_, so its members can export, add, change and delete keys. Clear these permissions in the Viewers group, and give them only to users you trust with the private keys.

:::
