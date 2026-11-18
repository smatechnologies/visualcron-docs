---
sidebar_label: 'Task Encryption - Encrypt (Symmetric)'
hide_title: 'true'
---

## Task Encryption - Encrypt (Symmetric)

The Encrypt (symmetric) Task encrypts one or more files with a single password. The encrypted files are raw encrypted data, not PGP files; to create PGP files, use the [PGP - Encrypt Task](pgp-encrypt). To decrypt the files, use the [Decrypt (symmetric) Task](decrypt-symmetric) with the same settings.

The Task offers these algorithms:

| Algorithm | Key bit lengths offered | Known vulnerabilities |
|:---:|:---:|:---:|
| DES | 64 | yes |
| RC2 | 40, 128 | yes |
| Rijndael | 128, 192, 256 | no |
| TripleDES | 128, 192 | no |
| AES | 128, 192, 256 | no |

Use AES where the receiving side supports it.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The ***Encrypt (symmetric)*** tab has three sub tabs: ***Encryption settings***, ***File filter*** and ***Destination***.

### Encryption settings tab

![Encryption settings tab of the Encrypt (symmetric) Task, with the encryption algorithm, key bit length, password, initialization vector and padding mode fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Encryption%20Tasks/Encrypt%20Symmetric.png)

- _Encryption algorithm_: "DES", "RC2", "Rijndael", "TripleDES" or "AES" (default)
- _Key bit length_: the key bit lengths offered for the selected algorithm; see the table above. When the algorithm changes, the highest length is selected. The key is made from the password, and the password length, not this setting, sets the key size; see the warning below
- _Password_: the password to encrypt with. The password is hidden; click _Copy_ to copy it to the clipboard
- _Initialization Vector (IV)_: the initialization vector to encrypt with. A new Task fills in a value; click _Copy_ to copy it to the clipboard
- _Padding mode_: "PKCS7" by default

:::warning

The key is made from the password. With "AES" or "Rijndael", use a password of up to 16, exactly 24, or 32 or more characters; with "TripleDES", up to 16, or 24 or more. With other lengths the Task fails.

:::

:::note

Keep the password, the initialization vector, the algorithm and the padding mode. The Decrypt (symmetric) Task needs the same values to decrypt the files. The Decrypt (symmetric) Task cannot decrypt files encrypted with "DES" or "RC2".

:::

### File filter tab

The ***File filter*** tab selects the files to encrypt; see [Task - File filter](../../job-tasks-file-filter). If no file matches, the Task reports a file-not-found error.

### Destination tab

![Destination tab of the Encrypt (symmetric) Task, with the destination folder options, the destination file mask and the post-process Variable option](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Encryption%20Tasks/Encrypt%20Symmetric%20Destination.png)

- _Use same folder as source_: writes each encrypted file to the folder of its source file
- _Use custom destination folder_ (default): writes every encrypted file to the folder entered below it. Files from sub folders are not written to matching sub folders; they all go to this one folder
- _Destination file mask_: the name of the encrypted file, `*.enc` by default, which keeps the source name and changes the extension to "enc". The mask `*` keeps the source name and extension
- _Post process mask with Variable - use {NEWNAME()} in Variable_: when checked, the name from the mask is changed again with the Variable expression in the field below. The expression must contain `{NEWNAME()}` (the name after the mask), `{CURRENTNAME()}` (the name of the source file) or `{CURRENTPATH()}` (the folder of the source file). The default expression, `{STRING(Replace|{NEWNAME()}|oldValue|newValue)}`, replaces "oldValue" in the name with "newValue". Set _Destination file mask_ to `*` when using this option

:::warning

The Task replaces a file of the same name in the destination folder without warning. With _Use same folder as source_ and the mask `*`, each encrypted file replaces its source file. Files of the same name from different sub folders replace each other in a custom destination folder.

:::

### Output and errors

The output has one line for each encrypted file: the path of the source file and the path of the encrypted file, separated by a tab. The source files are not deleted.