---
sidebar_label: 'Task XML - Verify'
hide_title: 'true'
---

## Task XML - Verify

The XML - Verify Task checks the XML digital signature of the XML files that its File filter selects. A valid signature shows that the file has not been changed since it was signed.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::warning

When a file contains the key or certificate of its signer, the Task checks the signature with that key. The selected _Certificate_ is then not used, so a file signed with any other key also passes. In that case, a signature that does not match can also be reported as "Ok", and the Task reports success. Use the Task to detect changes only for files whose signature does not include the key, or check the signer in another way.

When the File filter finds no file, no error is raised, and the Task reports success. To have it fail the Task, select "All errors" on the ***On error*** tab; see [Task - On Error](../../task-on-error).

:::

### Verify: File filter tab

![Verify tab, File filter sub tab, with the Location settings of the File filter](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/XML%20Tasks/Verify.png)

The File filter selects the signed XML files to check; see [File Filter](../../job-tasks-file-filter). The Credential of the File filter is used to read the files.

### Verify: Destination tab

![Verify tab, Destination sub tab, with the Certificate field](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/XML%20Tasks/Verify%20Destination.png)

**XML verify parameters**

- _Certificate_: The certificate to check the signatures with, used when a file does not contain the key of its signer. Select a certificate in the list, or click the icon next to it to open _Manage Certificates_; see [Global - Certificates](../../global-certificates). For files signed with "HMAC" by the Sign Task, select the certificate that was used to sign them. The certificate must exist even when it is not used; otherwise each file fails with "Could not find certificate"

### Output and errors

- The output has one entry per valid file: the file path followed by " - Ok". When several files are checked, the entries follow each other without a separator
- The files are checked one by one. When a signature is invalid or cannot be read, the Task fails, and the remaining files are not checked
