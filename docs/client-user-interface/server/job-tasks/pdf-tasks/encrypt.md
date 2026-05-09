---
sidebar_label: 'Task PDF - Encrypt'
hide_title: 'true'
---

## Task PDF - Encrypt

The PDF - Encrypt Task encrypts existing PDF files with a password or a Certificate.

**Encrypt > Main settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Encrypt%20Settings.png)

**Encryption type**

Select how to encrypt the PDF. Available options:

* _Certificate_ - encrypt using a Certificate from the [Certificates manager](../../global-certificates)
* _Password_ - encrypt using an owner and user password

**Certificate**

Select an existing Certificate you have created or imported in [Certificates manager](../../global-certificates). Used when *Encryption type* is set to _Certificate_.

**Password > Owner password**

The owner password. Used when *Encryption type* is set to _Password_.

**Password > User password**

The user password. Used when *Encryption type* is set to _Password_.

**Password > Permissions**

Specifies the user rights (permissions). User rights define what actions can be performed when the user password is used to open the document.

**Encryption algorithm**

The encryption algorithm that will be used for encrypting the document. Available options:

* AES/256 (Acrobat X)
* AES/256 (Acrobat 9)
* AES/128 (Acrobat 6,7)
* RC4/128 (Acrobat 5)
* RC4/40 (Acrobat 4)

**Encrypt metadata**

When checked, the document metadata (such as its name and author) is encrypted along with the content.

**Encrypt > File filter > Location** sub tab

This tab uses the common [file filter](../../job-tasks-file-filter) to choose which PDF files should be processed in this Task.

**Encrypt > Destination** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/PDF%20Tasks/Encrypt%20Destination.png)

**Save to**

Selects where the encrypted PDF is written. Available options:

* _Save to same file_ - overwrite the source PDF in place
* _Same folder with file mask_ - keep the original folder, but save under a different name (set the *File mask* below)
* _Different folder with file mask_ - save under a different name in a different folder (set both *Folder* and *File mask* below)

**Folder**

The destination folder. Enabled when *Save to* is set to _Different folder with file mask_. Click the *Folder* icon to browse for the folder.

**File mask**

The file mask used to name the output file. Enabled when *Save to* is set to _Same folder with file mask_ or _Different folder with file mask_.
