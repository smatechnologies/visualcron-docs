---
sidebar_label: 'Task PDF - Delete Attachment'
hide_title: 'true'
---

## Task PDF - Delete Attachment

The PDF - Delete attachment(s) Task removes attachments that are embedded in PDF files.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Delete attachment(s): Main settings tab

![Main settings tab of the Delete attachment(s) Task, with the Attachment names grid, the Get attachment names button and the Password for file(s) box](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Delete%20Attachments%20settings.png)

- _Name_ (_Attachment names ..._ grid): the names of the attachments to delete

  Click _Get attachment names_ to load the attachment names of the files that the File filter matches, and then select names in the _Name_ column. A name can contain wildcards, such as `*`, and Variables. The _Value_ column is not used by the Task.

- _Password for file(s)_: the password that opens the source PDF files, if they are protected

:::warning

When the grid is empty, the Task deletes every attachment in each file.

:::

### File filter tab

The ***File filter*** tab selects the PDF files to delete attachments from; see [File Filter](../../job-tasks-file-filter). If the filter has a Credential, the Task uses it while it reads and writes the files. When the logon with the Credential fails, the Task continues as the account that runs the Server and writes the error to the Server log.

### Destination tab

![Destination tab of the Delete attachment(s) Task, with the Save to.. group and the Folder and File mask boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Delete%20Attachments%20destination.png)

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

The Task output contains "Success" for each file it saves.
