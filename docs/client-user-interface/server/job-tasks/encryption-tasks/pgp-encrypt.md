---
sidebar_label: 'Task Encryption - PGP Encrypt'
hide_title: 'true'
---

## Task Encryption - PGP Encrypt

The PGP - Encrypt Task encrypts one or more files with the OpenPGP standard, using the public keys of the recipients, a password, or both, and can sign them with your private keys. For key rings, see [PGP key rings](../../global-pgp-key-rings).

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

The ***PGP - Encrypt*** tab has four sub tabs: ***File filter***, ***Encrypt***, ***Recipients*** and ***Signers***.

### File filter tab

The ***File filter*** tab selects the files to encrypt or sign; see [Task - File filter](../../job-tasks-file-filter).

![File filter tab of the PGP - Encrypt Task, with the Location tab open](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Encryption%20Tasks/PGP%20-%20Encrypt.png)

### Encrypt tab

Check _Encrypt source_, _Sign source_ or both. At least one is required.

**Encryption**

- _Encrypt source_: checked by default. Encrypts the files for the keys selected on the ***Recipients*** tab, or with a password
- _Encryption algorithm_: the cipher that encrypts the file content, "CAST5" by default: "AES128", "AES256", "CAST5", "3DES", "IDEA", "BLOWFISH" or "TWOFISH". "AES256" is the strongest. "RSA" is also listed, but it is a public-key algorithm, not a cipher for the file content
- _Protection level_: how the key is derived from the password:
  - "Low" (default): from a hash of the password only
  - "Normal": from a hash of the password and a salt
  - "High": from a hash of the password and a salt, repeated several times
- _Use conventional (password) encryption_: encrypts with the password in _Password_ below it. With recipients selected, a file can be decrypted with either a recipient key or the password; without recipients, only with the password
- _Password_: the password for conventional encryption
- _Armor data_: checked by default. Writes the result as ASCII text (base64) instead of binary data
- _Armor boundary_: the label of the armored block, "PGP MESSAGE" by default. Available when _Armor data_ is checked
- _Compress data before encryption_: compresses the content before it is encrypted
- _Use new features_: checked by default. Uses newer and stronger PGP features. Clear it when the receiving software is an old version, such as PGP 2.6.x

**Signing**

- _Sign source_: signs the files with the keys selected on the ***Signers*** tab
- _Treat input as text_: treats the files as text. With _Sign source_ checked and _Encrypt source_ cleared, the Task writes a clear-text signed file
- _Password_: the passphrase of the private signing key
- _Detached signature_: writes the signature to its own file instead of into the signed file. Applies when only _Sign source_ is checked

The Task has no setting for the signing hash.

**Destination**

- _Use same folder as source_: writes the result to the source folder of the file filter, keeping the sub folder structure
- _Use custom destination folder_ (default): writes the result to the folder entered below it, keeping the sub folder structure of the source folder. A folder is required
- _Destination file mask_: the name of the result file, `*.pgp` by default, which adds the extension "pgp" to the source name
- _Overwrite if existing_: checked by default. Replaces a file of the same name in the destination folder. When cleared, a file of the same name is kept and the Task fails with the error "File with the same name already exists"

:::warning

With _Use same folder as source_, the mask `*` and _Overwrite if existing_ checked, each result file replaces its source file.

:::

### Recipients tab

![Recipients tab of the PGP - Encrypt Task, with a selected key ring and its list of public keys](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Encryption%20Tasks/PGP%20-%20Encrypt%20Recipients.png)

Available when _Encrypt source_ is checked.

- _Select recipients_: the key ring with the public keys of the recipients. Check the keys to encrypt for; at least one is required unless _Use conventional (password) encryption_ is checked. Click _Manage Key Rings_ to add or change key rings
- _Disable sub keys_: encrypts with the primary keys only, not with their sub keys. A key that has several sub keys can otherwise produce a file encrypted for several keys, which some receiving software cannot read

### Signers tab

![Signers tab of the PGP - Encrypt Task, with the key ring selection and the list of private keys](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Encryption%20Tasks/PGP%20-%20Encrypt%20Signers.png)

Available when _Sign source_ is checked.

- _Select signers_: the key ring with your private keys. Check the keys to sign with; at least one is required. Click _Manage Key Rings_ to add or change key rings
- _Disable sub keys_: signs with the primary keys only, not with their sub keys. A key that has several sub keys can otherwise sign a file more than once

### Output and errors

The output has one line for each file: the path of the source file and the path of the result file, separated by a tab. The source files are not deleted.

If a file cannot be encrypted or signed, the Task fails and the remaining files in the same folder are not processed.

### Troubleshooting

**The encrypted file gets signed twice**

Check _Disable sub keys_ on the ***Signers*** tab.

**No suitable OpenPGP public key for encryption found**

Clear _Disable sub keys_ on the ***Recipients*** tab.
