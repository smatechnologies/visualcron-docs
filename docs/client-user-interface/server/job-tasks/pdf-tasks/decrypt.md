---
sidebar_label: 'Task PDF - Decrypt'
hide_title: 'true'
---

## Task PDF - Decrypt

The PDF - Decrypt Task decrypts existing PDF files with a password or a Certificate.

**Decrypt > Main settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Decrypt%20settings.png)

**Decryption type**

Select how to decrypt the PDF. Available options:

* _Certificate_ - decrypt using a Certificate from the [Certificates manager](../../global-certificates)
* _Password_ - decrypt using the owner and/or user password

Select an existing Certificate you have created or imported in [Certificates manager](../../global-certificates). Used when *Decryption type* is set to _Certificate_.

**Password > Owner password**

The owner password. Used when *Decryption type* is set to _Password_.

**Password > User password**

The user password. Used when *Decryption type* is set to _Password_.

**Decrypt > File filter > Location** sub tab

This tab uses the common [file filter](../../job-tasks-file-filter.md) to choose which PDF files should be processed in this Task.

**Decrypt > Destination** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Decrypt%20Destination.png)

**Save to**

Selects where the decrypted PDF is written. Available options:

* _Save to same file_ - overwrite the source PDF in place
* _Same folder with file mask_ - keep the original folder, but save under a different name (set the *File mask* below)
* _Different folder with file mask_ - save under a different name in a different folder (set both *Folder* and *File mask* below)

**Folder**

The destination folder. Enabled when *Save to* is set to _Different folder with file mask_. Click the *Folder* icon to browse for the folder.

**File mask**

The file mask used to name the output file. Enabled when *Save to* is set to _Same folder with file mask_ or _Different folder with file mask_.
