---
sidebar_label: 'Task Cloud Transfer - Upload File'
hide_title: 'true'
---

## Task Cloud Transfer - Upload File

The Cloud - Upload file(s) Task lets you upload files from the local file system to a cloud service such as Amazon S3, Box, Dropbox, Google Drive, Google Storage, Microsoft Azure or OneDrive.
 
**Upload file(s) > Main settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Upload%20Main%20Settings.png)

**Connection**

To use a specific cloud service you need to create a [Connection](../../global-connections) first. Click the *Settings* icon to open the Manage Connections dialog. Only cloud connections (Amazon S3, Windows Azure, OneDrive, Google Drive, Dropbox, Box, Google Storage) are listed.
 
**Bucket/Container**

The label and behavior of this field changes depending on the selected connection:

* _Bucket_ - Amazon S3
* _Container_ - Windows Azure (Block or Page blob access)
* _Share_ - Windows Azure File Shares
* _File system_ - Windows Azure Data Lake Gen V2
* _Drive_ - Google Drive
* _Bucket/Container_ - the field is disabled for connections that do not use a top-level container (for example OneDrive, Dropbox, Box, Google Storage and Azure Data Lake Gen V1)

Click the *Folder* icon to list all available Buckets/Containers for the selected Connection.
 
**Destination folder**

This is the destination folder in the cloud where the files will be uploaded to. Click the *Folder* icon to browse and list folders from the cloud. A bucket/container must be selected first when the connection requires one.
 
**Keep modified/created date**

If checked, the modified and created dates of the local source files are preserved on the uploaded files (where the cloud service supports it).

**Overwrite options**

Controls how to handle files that already exist at the destination. Available options:

* _Overwrite - always if existing_ - replace the destination file
* _Overwrite - if newer_ - replace the destination file only if the source is newer
* _Overwrite - if destination size is_ - replace the destination file based on a size comparison (enables the size comparison field below)
* _Do not overwrite if existing_ - skip files that already exist at the destination

**Size comparison**

Only enabled when *Overwrite options* is set to _Overwrite - if destination size is_. Selects the size comparison criterion used to decide whether to overwrite:

* _Same_
* _Smaller_
* _Larger_
* _Smaller or larger_
* _Different_

**Upload file(s) > File filter** sub tab

This Task uses the standard VisualCron [File filter](../../job-tasks-file-filter) to define which local files are included in the upload, including source folder, include/exclude masks (with regex support), subfolder recursion and date-based filtering.
