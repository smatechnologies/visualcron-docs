---
sidebar_label: 'Task PDF - Clear Signature'
hide_title: 'true'
---

## Task PDF - Clear Signature

The PDF - Clear signature(s) Task removes all or specific signatures from a PDF document.

**Clear signature > Main settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Clear%20Signature%20settings.png)

**All signatures**

When checked, removes every signature in the document.

**Signature filters**

When *All signatures* is unchecked, only signatures whose names match this comma-separated filter are removed.

**Password for file(s)**

If any of the specified PDF files is password protected, enter the password here.

**Clear signature > File filter > Location** sub tab

This tab uses the common [file filter](../../job-tasks-file-filter.md) to choose which PDF files should be processed in this Task.

**Clear signature > Destination** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Clear%20Signature%20destination.png)

**Save to**

Selects where the modified PDF is written. Available options:

* _Save to same file_ - overwrite the source PDF in place
* _Same folder with file mask_ - keep the original folder, but save under a different name (set the *File mask* below)
* _Different folder with file mask_ - save under a different name in a different folder (set both *Folder* and *File mask* below)

**Folder**

The destination folder. Enabled when *Save to* is set to _Different folder with file mask_. Click the *Folder* icon to browse for the folder.

**File mask**

The file mask used to name the output file. Enabled when *Save to* is set to _Same folder with file mask_ or _Different folder with file mask_.
