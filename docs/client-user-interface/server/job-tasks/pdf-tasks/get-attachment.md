---
sidebar_label: 'Task PDF - Get Attachment'
hide_title: 'true'
---

## Task PDF - Get Attachment

The PDF - Get attachment(s) Task saves the files that are attached to PDF files.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Get attachment(s): Main settings tab

![Main settings tab of the Get attachment(s) Task, with the Attachment names grid, the Get attachment names button and the Password for file(s) box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Get%20Attachment%20settings.png)

- _Name_ (_Attachment names ..._ grid): the names of the attachments to save

  When the grid is empty, the Task saves every attachment. Click _Get attachment names_ to load the attachment names of the files that the File filter matches, and then select names in the _Name_ column. A name can contain wildcards, such as `*`, and Variables.

- _Password for file(s)_: the password that opens the source PDF files, if they are protected

### File filter tab

The ***File filter*** tab selects the PDF files to take attachments from; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Destination tab

![Destination tab of the Get attachment(s) Task, with the Save to.. group and the Folder and File mask boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Get%20Attachment%20destination.png)

- _Same file_ (_Save to.._ group): saves each attachment under its own name in the folder set on the ***File filter*** tab
- _Same folder but use file mask_: saves each attachment in the folder set on the ***File filter*** tab, named by _File mask_
- _Different folder and use file mask_: saves each attachment in _Folder_, named by _File mask_
- _Folder_: the destination folder for _Different folder and use file mask_; click the folder button to browse
- _File mask_: builds the file name from the attachment name, by the renaming standard set in [Main - Settings](../../main-settings)

  The default `*` keeps the attachment name.

:::warning

A file that already has the name is replaced without a prompt.

:::

When _Include sub folders_ is checked on the File filter, the attachments are saved in the File filter folder, not in the subfolder the PDF file came from.

### Output and errors

The Task output lists the path of each attachment it saves.
