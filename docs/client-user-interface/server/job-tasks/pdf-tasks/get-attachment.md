---
sidebar_label: 'Task PDF - Get Attachment'
hide_title: 'true'
---

## Task PDF - Get Attachment

The PDF - Get attachment(s) Task extracts all or specific files attached to a PDF document and saves them to disk.

**Get attachment(s) > Main settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Get%20Attachment%20settings.png)

In the *Main settings* dialog, add or delete the names of the attachments to extract. Only file names that already exist inside the source PDF can be selected.

**Get attachment(s) > File filter > Location** sub tab

This tab uses the common [file filter](../../job-tasks-file-filter.md) to choose which PDF files should be processed in this Task.

**Get attachment(s) > Destination** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Get%20Attachment%20destination.png)

**Save to**

Selects where the extracted attachment files are written. Available options:

* _Save to same file_ - extract to the same folder as the source PDF, using the original attachment names
* _Same folder with file mask_ - extract to the same folder as the source PDF, using a custom file mask
* _Different folder with file mask_ - extract to a different folder, using a custom file mask

**Folder**

The destination folder. Enabled when *Save to* is set to _Different folder with file mask_. Click the *Folder* icon to browse for the folder.

**File mask**

The file mask used to name the extracted file(s). Enabled when *Save to* is set to _Same folder with file mask_ or _Different folder with file mask_.
