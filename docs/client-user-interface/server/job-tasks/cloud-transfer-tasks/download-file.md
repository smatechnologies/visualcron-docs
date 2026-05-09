---
sidebar_label: 'Task Cloud Transfer - Download File'
hide_title: 'true'
---

## Task Cloud Transfer - Download File

The Cloud - Download file(s) Task downloads files from a cloud service such as Amazon S3, Box, Dropbox, Google Drive, Google Storage, Microsoft Azure or OneDrive to the local file system (or to a network path using a Credential).

**Download file(s) > Remote file filter** sub tab

This Task uses the standard [Cloud Remote file filter](../../../server/job-tasks-cloud-remote-file-filter) to define the connection, bucket/container, source folder, item mask, date and size filters, sorting and result limit.
 
**Download file(s) > Destination** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Download%20file(s).png)

**Credential**

When the destination is on a network share or any path that requires authentication, select a [Credential](../../global-credentials) here. The user name and password of the Credential are used to access the destination. Click *Manage credentials* to add or edit Credentials. Leave empty to use the VisualCron service account.

**Destination folder**

The local folder where the downloaded files will be stored. Click the *Folder* icon to browse for the folder. This field is required.

**Download file mask**

A file mask applied to the downloaded files (default `*`). Used together with the source filter to control which of the matched items are actually written to the destination.

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

**Keep modified/created date**

If checked, the modified and created dates from the source file in the cloud are preserved on the local copy.

**Delete source file after download**

When checked, the source file in the cloud is deleted after it has been successfully downloaded.
