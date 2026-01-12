---
sidebar_label: 'Task Cloud Transfer - Download File'
hide_title: 'true'
---

## Task Cloud Transfer - Download File

The Cloud - Download file(s) Task is able to download files with Cloud services like Amazon S3, Box, Dropbox, Google Drive, Microsoft Azure and OneDrive.
 
Download file(s) > Remote file filter sub tab
This Task uses the [Cloud Remote file filter](../../../server/job-tasks-cloud-remote-file-filter) for settings.
 
**Download file(s) > Destination** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Download%20file(s).png)

**Credential**

To control a remote computer you may need to use a Credential. The Credential must match the user name and pass word of the user that you want to login. Click on *Manage credentials* to add or edit Credentials. Select a Credential in the combo box.
 
**Destination folder**

The folder where you want to store the files. Click the Folder icon to list folders from the cloud.
 
**Overwrite options**

If the file is already existing you can choose to overwrite, only if newer or not overwrite.
 
**Keep modified/created date**

This take the modified/created dates from the downloaded file(s).
 
**Delete source file after download**

When download has been completed the source file in the cloud is deleted.