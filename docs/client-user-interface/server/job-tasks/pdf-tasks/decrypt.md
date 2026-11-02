---
sidebar_label: 'Task PDF - Decrypt'
hide_title: 'true'
---

## Task PDF - Decrypt

The PDF - Decrypt Task removes the password or Certificate encryption from PDF files.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Decrypt: Main settings tab

![Main settings tab of the Decrypt Task, with the Certificate list and the Owner password and User password boxes in the Decrypt by group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Decrypt%20settings.png)

The Task finds out how each file is encrypted and uses the matching setting. Set at least one of them.

- _Certificate_ (_Decrypt by ..._ group): the Certificate for a file that is encrypted with a Certificate; see [Global - Certificates](../../global-certificates)
- _Owner password_: the owner password of a password-encrypted file

  The Task tries the owner password first.

- _User password_: the user password, tried when the owner password does not open the file

### File filter tab

The ***File filter*** tab selects the PDF files to decrypt; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Destination tab

![Destination tab of the Decrypt Task, with the Save to.. group and the Folder and File mask boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Decrypt%20Destination.png)

- _Same file_ (_Save to.._ group): saves the decrypted file over the source file
- _Same folder but use file mask_: saves the decrypted file in the folder set on the ***File filter*** tab, named by _File mask_
- _Different folder and use file mask_: saves the decrypted file in _Folder_, named by _File mask_
- _Folder_: the destination folder for _Different folder and use file mask_; click the folder button to browse
- _File mask_: builds the new file name from the source file name, by the renaming standard set in [Main - Settings](../../main-settings)

  The default `*` keeps the source file name.

:::warning

_Same file_ replaces the source file. With the default _File mask_ `*`, _Same folder but use file mask_ also replaces a source file that is in the File filter folder. A file that already has the new name is replaced without a prompt.

:::

When _Include sub folders_ is checked on the File filter, _Same folder but use file mask_ saves every result in the File filter folder, not in the subfolder the source file came from.

### Output and errors

The Task output contains "Success" for each file it decrypts. A file that is neither encrypted nor signed raises an error, and so does a password that does not open the file. A signed file that is not encrypted, or a password-encrypted file with both password boxes empty, is left as it is, and the Task reports success.

:::warning

When the selected Certificate no longer exists and no password is set, the file is not decrypted, and the Task reports success. With _Same folder but use file mask_ or _Different folder and use file mask_, the Task copies the source file to the destination before it decrypts it, so a file that is not decrypted stays there encrypted.

:::
