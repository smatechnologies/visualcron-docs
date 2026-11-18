---
sidebar_label: 'Task PDF - Add Attachment'
hide_title: 'true'
---

## Task PDF - Add Attachment

The PDF - Add attachment(s) Task attaches one or more files to each PDF file that the File filter selects.

![Add attachment(s) Task with the File Filter tab open, showing the Credentials, Folder, Exclude folder(s) and Include file mask settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Add%20attachment%20settings.png)

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### File Filter tab

The ***File Filter*** tab selects the PDF files to attach files to; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Attachment files tab

![Attachment files tab with its Add, Edit, Clone, Delete and Order toolbar, and the File filter window open over it](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Add%20attachment%20attachment.png)

The ***Attachment files*** tab lists one or more File filters that select the files to attach. Use _Add_, _Edit_, _Clone_ and _Delete_ on the toolbar to manage the list, and _Order_ to set the position of the selected item. Every file that a filter matches is attached to every PDF file.

### Destination tab

![Destination tab with the Save to.. group, the Folder and File mask boxes, and the Password for input file(s) and Attachment description boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Add%20attachment%20output.png)

- _Same file_ (_Save to.._ group): saves the PDF file over the source file
- _Same folder but use file mask_: saves the PDF file in the folder set on the ***File Filter*** tab, named by _File mask_
- _Different folder and use file mask_: saves the PDF file in _Folder_, named by _File mask_
- _Folder_: the destination folder for _Different folder and use file mask_; click the folder button to browse
- _File mask_: builds the new file name from the source file name, by the renaming standard set in [Main - Settings](../../main-settings)

  The default `*` keeps the source file name.

:::warning

_Same file_ replaces the source file. With the default _File mask_ `*`, _Same folder but use file mask_ also replaces a source file that is in the File Filter folder. A file that already has the new name is replaced without a prompt.

:::

When _Include sub folders_ is checked on the File Filter, _Same folder but use file mask_ saves every result in the File Filter folder, not in the subfolder the source file came from.

- _Password for input file(s)_: the password that opens the source PDF files, if they are protected
- _Attachment description_: the description stored with each attached file

  Variables are supported.

### Output and errors

The Task output lists the path of each PDF file it saves. When the attachment filters match no file, the PDF file is saved without new attachments.

:::warning

When the ***Attachment files*** tab has no item, the Task writes "No attachments were found" to standard error and saves nothing, and the Task reports success. To fail the Task in this case, set an On error condition on standard error; see [Task - On Error](../../task-on-error).

:::
