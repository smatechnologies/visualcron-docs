---
sidebar_label: 'Task PDF - Delete Attachment'
hide_title: 'true'
---

## Task PDF - Delete Attachment

The PDF - Delete attachment(s) Task removes one or more attachments embedded in a PDF file.

**Delete attachment(s) > Main settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Delete%20Attachments%20settings.png)

In the *Main settings* dialog, add or delete the names of the attachments to remove. Only file names that already exist inside the source PDF can be selected.

**Delete attachment(s) > File filter > Location** sub tab

This tab uses the common [file filter](../../job-tasks-file-filter.md) to choose which PDF files should be processed in this Task.

**Delete attachment(s) > Destination** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Delete%20Attachments%20destination.png)

**Save to**

Selects where the modified PDF is written. Available options:

* _Save to same file_ - overwrite the source PDF in place
* _Same folder with file mask_ - keep the original folder, but save under a different name (set the *File mask* below)
* _Different folder with file mask_ - save under a different name in a different folder (set both *Folder* and *File mask* below)

**Folder**

The destination folder. Enabled when *Save to* is set to _Different folder with file mask_. Click the *Folder* icon to browse for the folder.

**File mask**

The file mask used to name the output file. Enabled when *Save to* is set to _Same folder with file mask_ or _Different folder with file mask_.
