---
sidebar_label: 'Task PDF - Clear Signature'
hide_title: 'true'
---

## Task PDF - Clear Signature

The PDF - Clear signature(s) Task removes all signatures, or the signatures whose names match a filter, from PDF files.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Clear signature(s): Main settings tab

![Main settings tab of the Clear signature(s) Task, with the Remove signature(s) group and the Password for file(s) box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Clear%20Signature%20settings.png)

- _All signatures_ (_Remove signature(s)_ group): removes every signature; this is the default
- _Signature filters_: removes each signature whose name starts with one of the comma-separated words in the box

  Do not put a space after a comma: the space becomes part of the next word. Variables are supported.

- _Password for file(s)_: not used by this Task

  The Task cannot process an encrypted file; see [Output and errors](#output-and-errors).

### File filter tab

The ***File filter*** tab selects the PDF files to remove signatures from; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Destination tab

![Destination tab of the Clear signature(s) Task, with the Save to.. group and the Folder and File mask boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Clear%20Signature%20destination.png)

- _Same file_ (_Save to.._ group): saves the changed file over the source file
- _Same folder but use file mask_: saves the changed file in the folder set on the ***File filter*** tab, named by _File mask_
- _Different folder and use file mask_: saves the changed file in _Folder_, named by _File mask_
- _Folder_: the destination folder for _Different folder and use file mask_; click the folder button to browse
- _File mask_: builds the new file name from the source file name, by the renaming standard set in [Main - Settings](../../main-settings)

  The default `*` keeps the source file name.

:::warning

_Same file_ replaces the source file. With the default _File mask_ `*`, _Same folder but use file mask_ also replaces a source file that is in the File filter folder. A file that already has the new name is replaced without a prompt.

:::

When _Include sub folders_ is checked on the File filter, _Same folder but use file mask_ saves every result in the File filter folder, not in the subfolder the source file came from.

### Output and errors

The Task output lists the path of each file it saves. A file that has no signature, or is encrypted, raises an error. With _Same folder but use file mask_ or _Different folder and use file mask_, the Task copies the source file to the destination before it checks it, so the copy stays there unchanged when the check fails.
