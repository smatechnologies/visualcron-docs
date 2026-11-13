---
sidebar_label: 'Task PDF - Encrypt'
hide_title: 'true'
---

## Task PDF - Encrypt

The PDF - Encrypt Task encrypts PDF files with a password or a Certificate.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Encrypt: Main settings tab

![Main settings tab of the Encrypt Task, with the Certificate and Password options, the Permissions list, the Encrypt algorithm list and the Encrypt metadata check box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Encrypt%20Settings.png)

- _Certificate_ (_Encrypt by ..._ group): encrypts the files for the Certificate selected in the _Certificate_ list; this is the default

  See [Global - Certificates](../../global-certificates).

- _Password_: encrypts the files with the _Owner password_ and the _User password_

  Both passwords are required. Variables are supported.

- _Permissions_: the actions that are allowed on the encrypted document: "Annotations", "Assemble", "Extract", "ExtractAcc", "FillInForms", "HighQualityPrint", "LowQualityPrint" and "Modify"

  All are checked by default. The list is available when _Password_ is selected.

- _Encrypt algorithm_: "RC4/40 bits (Acrobat 4)", "RC4/128 bits (Acrobat 5)", "AES/128 bits (Acrobat 6, 7)", "AES/256 bits (Acrobat 9)" or "AES/256 bits (Acrobat X)"

  The default is "RC4/40 bits (Acrobat 4)".

- _Encrypt metadata_: also encrypts the document metadata; unchecked by default

:::tip

The AES options give stronger encryption than the RC4 options. Choose the strongest option that the readers of the documents support.

:::

### File filter tab

The ***File filter*** tab selects the PDF files to encrypt; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Destination tab

![Destination tab of the Encrypt Task, with the Save to.. group and the Folder and File mask boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Encrypt%20Destination.png)

- _Same file_ (_Save to.._ group): saves the encrypted file over the source file
- _Same folder but use file mask_: saves the encrypted file in the folder set on the ***File filter*** tab, named by _File mask_
- _Different folder and use file mask_: saves the encrypted file in _Folder_, named by _File mask_
- _Folder_: the destination folder for _Different folder and use file mask_; click the folder button to browse
- _File mask_: builds the new file name from the source file name, by the renaming standard set in [Main - Settings](../../main-settings)

  The default `*` keeps the source file name.

:::warning

_Same file_ replaces the source file. With the default _File mask_ `*`, _Same folder but use file mask_ also replaces a source file that is in the File filter folder. A file that already has the new name is replaced without a prompt.

:::

When _Include sub folders_ is checked on the File filter, _Same folder but use file mask_ saves every result in the File filter folder, not in the subfolder the source file came from.

### Output and errors

The Task output contains "Success" for each file it encrypts. A file that is already encrypted, or that has a digital signature, raises an error, and so does a Certificate that no longer exists.

:::warning

With _Same folder but use file mask_ or _Different folder and use file mask_, the Task copies the source file to the destination before it encrypts it. When encryption fails, that copy stays at the destination unencrypted.

:::
