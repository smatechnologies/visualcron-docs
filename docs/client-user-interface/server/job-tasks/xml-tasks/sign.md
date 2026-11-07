---
sidebar_label: 'Task XML - Sign'
hide_title: 'true'
---

## Task XML - Sign

The XML - Sign Task adds an XML digital signature to the XML files that its File filter selects, using a certificate from the VisualCron certificate store.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::warning

With the default **Save to..** option _Same folder but use file mask_ and the default _File mask_ `*`, the signed file gets the name of the source file in the same folder, so it replaces the source file. _Same file_ also replaces the source file. To keep the source files, set a different _File mask_, such as `*_signed.xml`, or save to a different folder.

With "HMAC", the default _Signature method_, the signing key is made from the certificate itself and not from its private key, so anyone who has a copy of the certificate can create a signature that matches. To sign with the private key of the certificate, select "Signature".

When the File filter finds no file, no error is raised, and the Task reports success. To have it fail the Task, select "All errors" on the ***On error*** tab; see [Task - On Error](../../task-on-error).

:::

### Sign: File filter tab

![Sign tab, File filter sub tab, with the Location settings of the File filter](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/XML%20Tasks/Sign.png)

The File filter selects the files to sign; see [File Filter](../../job-tasks-file-filter). The Credential of the File filter is used to read and save the files.

### Sign: Destination tab

![Sign tab, Destination sub tab, with the XML sign parameters, Certificate and Save to settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/XML%20Tasks/Sign%20Destination.png)

**XML sign parameters**

- _Signature type_: Where the signature is placed. The default is "Enveloped"
    - "Enveloped": The signature is added inside the signed document
    - "Enveloping": The signed document is placed inside the signature
    - "Detached": The saved file contains only the signature
- _Canonicalization method_: How the XML is converted to its canonical form before it is signed. The options are "Canonical" (the default), "Canonical with comments", "Canonical v1.1", "Canonical with comments v1.1", "Exclusive canonical", "Exclusive canonical with comments" and "Minimal canonical"
- _Signature method_: Select "HMAC" (the default) or "Signature", then select the algorithm in the list next to it. The list next to the option that is not selected is not available
    - "HMAC": "MD5", "SHA1" (the default), "SHA224", "SHA256", "SHA384", "SHA512" or "RIPEMD160"
    - "Signature": "DSS", "RSA SHA1" (the default), "RSA MD5", "RSA SHA256", "RSA SHA384", "RSA SHA512" or "RSA RIPEMD160"

**Certificate**

- _Certificate_: The certificate to sign with. Select a certificate in the list, or click the icon next to it to open _Manage Certificates_, where a certificate is selected, imported or created; see [Global - Certificates](../../global-certificates). With "Signature", the certificate must include a private key
- _Include public key_: When selected, the certificate is included in the signature, so that the receiver can check the signature without a copy of it
- _Key name_: A text that identifies the key to the receiver, written to the `KeyName` element of the signature. It can be a key name, a key index, a distinguished name or an e-mail address. White space in the text is kept

**Save to..**

- _Same file_: The signed file replaces the source file
- _Same folder but use file mask_: The default. The signed file is saved in the folder of the File filter, with the name that _File mask_ gives
- _Different folder and use file mask_: The signed file is saved in _Folder_, with the name that _File mask_ gives
- _Folder_: The destination folder. Available with _Different folder and use file mask_
- _File mask_: The name of the signed file. `*` keeps the name of the source file. Available with both file mask options

### Output and errors

- The output of the Task contains the path of each signed file. When several files are signed, the paths follow each other without a separator
- The files are signed one by one. When a file cannot be signed, for example because the certificate is not found, the Task fails, and the remaining files are not signed
