---
sidebar_label: 'Task Encryption - PGP Decrypt'
hide_title: 'true'
---

## Task Encryption - PGP Decrypt

The PGP - Decrypt Task decrypts one or more files encrypted with the OpenPGP standard, using a PGP key ring or a password. For key rings, see [PGP key rings](../../global-pgp-key-rings).

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The ***PGP - Decrypt*** tab has two sub tabs: ***File filter*** and ***Decrypt***.

### File filter tab

The ***File filter*** tab selects the files to decrypt; see [Task - File filter](../../job-tasks-file-filter).

### Decrypt tab

![Decrypt tab of the PGP - Decrypt Task, with the key ring selection, the password and the destination settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Encryption%20Tasks/PGP%20-%20Decrypt.png)

- _Select Key Ring_: the key ring with the private key that decrypts the files. Click _Manage Key Rings_ to add or change key rings; see [PGP key rings](../../global-pgp-key-rings)
- _Password_: the passphrase of the private key, or the password of a file that was encrypted with a password. Enter a password when no key ring is selected
- _Use same folder as source_: writes the decrypted files to the source folder of the file filter, keeping the sub folder structure
- _Use custom destination folder_ (default): writes the decrypted files to the folder entered below it, keeping the sub folder structure of the source folder. A folder is required
- _Destination file mask_: the name of the decrypted file, `*` by default, which keeps the base name. Use `*` and `?` as wildcards; for example, `*.pdf` keeps the base name and changes the extension to "pdf"
- _Base destination file name on inner file name_ (default): applies the mask to the file name stored inside the PGP file, which is usually the original file name
- _Base destination file name on encrypted file name_: applies the mask to the name of the encrypted file
- _Post process mask with Variable - use {NEWNAME()} in Variable_: when checked, the name from the mask is changed again with the Variable expression in the field below, which must contain `{NEWNAME()}`, the name after the mask. The default expression, `{STRING(Replace|{NEWNAME()}|oldValue|newValue)}`, replaces "oldValue" in the name with "newValue". Set _Destination file mask_ to `*` when using this option
- _Overwrite if existing_: checked by default. Replaces a file of the same name in the destination folder

:::warning

With _Overwrite if existing_ checked, a file of the same name in the destination folder is replaced without warning.

:::

### Output and errors

The output has one line for each decrypted file: the path of the encrypted file and the path of the decrypted file, separated by a tab. The encrypted files are not deleted.

If a file cannot be decrypted, the error is written to the error output and the Task fails. The remaining files in the same folder are not processed.

### Troubleshooting

**OpenPGP secret key for decryption found**

No private key of OpenPGP format is in the selected key ring. Import the key again; see [PGP key rings](../../global-pgp-key-rings).

**No appropriate OpenPGP secret key for decryption found**

The selected key ring does not contain the private key that the file was encrypted for. Select the key ring that holds that key.