---
sidebar_label: 'Task Encryption - Decrypt (Symmetric)'
hide_title: 'true'
---

## Task Encryption - Decrypt (Symmetric)

The Decrypt (symmetric) Task decrypts one or more files that the [Encrypt (symmetric) Task](encrypt-symmetric) encrypted with a single password. The files are raw encrypted data, not PGP files; to decrypt PGP files, use the [PGP - Decrypt Task](pgp-decrypt).

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The ***Decrypt (symmetric)*** tab has three sub tabs: ***Decryption settings***, ***File filter*** and ***Destination***.

### Decryption settings tab

![Decryption settings tab of the Decrypt (symmetric) Task, with the encryption algorithm, password, initialization vector and padding mode fields](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Encryption%20Tasks/Decrypt%20Symmetric.png)

Enter the same values that the Encrypt (symmetric) Task used to encrypt the files. If any of them differs, the files cannot be decrypted.

- _Encryption algorithm_: "DES", "RC2", "Rijndael", "TripleDES" or "AES" (default)
- _Password_: the password the files were encrypted with. The password is hidden; click _Copy_ to copy it to the clipboard
- _Initialization Vector (IV)_: the initialization vector the files were encrypted with. A new Task fills in a value; click _Copy_ to copy it to the clipboard
- _Padding mode_: the padding mode the files were encrypted with, "PKCS7" by default

:::warning

This Task has no _Key bit length_ setting. With _Encryption algorithm_ "DES" or "RC2", the Task cannot decrypt files and fails. Use "AES", "Rijndael" or "TripleDES" for files that this Task must decrypt. Because the key is made from the password on both sides, such files decrypt whatever _Key bit length_ the Encrypt (symmetric) Task used.

:::

### File filter tab

The ***File filter*** tab selects the files to decrypt; see [Task - File filter](../../job-tasks-file-filter). If no file matches, the Task reports a file-not-found error.

### Destination tab

![Destination tab of the Decrypt (symmetric) Task, with the destination folder options, the destination file mask and the post-process Variable option](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Encryption%20Tasks/Decypt%20Symmetric%20Destination.png)

- _Use same folder as source_: writes each decrypted file to the folder of its encrypted file
- _Use custom destination folder_ (default): writes every decrypted file to the folder entered below it. Files from sub folders are not written to matching sub folders; they all go to this one folder
- _Destination file mask_: the name of the decrypted file, `*` by default, which keeps the name of the encrypted file. To change the extension, enter a mask such as `*.txt`
- _Post process mask with Variable - use {NEWNAME()} in Variable_: when checked, the name from the mask is changed again with the Variable expression in the field below. The expression must contain `{NEWNAME()}` (the name after the mask), `{CURRENTNAME()}` (the name of the encrypted file) or `{CURRENTPATH()}` (the folder of the encrypted file). The default expression, `{STRING(Replace|{NEWNAME()}|oldValue|newValue)}`, replaces "oldValue" in the name with "newValue". Set _Destination file mask_ to `*` when using this option

:::warning

The Task replaces a file of the same name in the destination folder without warning. With _Use same folder as source_ and the mask `*`, each decrypted file replaces its encrypted file. Files of the same name from different sub folders replace each other in a custom destination folder.

:::

### Output and errors

The output has one line for each decrypted file: the path of the encrypted file and the path of the decrypted file, separated by a tab. The encrypted files are not deleted.