---
sidebar_label: 'Task Sharepoint - Download File'
hide_title: 'true'
---

## Task Sharepoint- Download File

The SharePoint - Download file(s) Task downloads one or more files from the SharePoint library.
 
The SharePoint Tasks supports the following versions:

* SharePoint 2010
* SharePoint 2013
* SharePoint Online

**Download file(s) > Remote file filter** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/download%20files%20settings.png)

**Connection**

To use SharePoint Tasks you need to create a [Connection](../../global-connections) first. Click the *Settings* icon to open the *Manage Connections* dialog.
 
The source URL of the folder to download from. Click the *Folder* icon to use the SharePoint Browser in order to view or select a specific folder.

**Item mask**

A wildcard pattern used to match the files to download (e.g. `*` for all files, `*.txt` for text files only).

**Filter**

Select the content filter type to apply when selecting files.

**Case sensitive**

When checked, the item mask matching is case sensitive.

**Include sub folders**

When checked, files in sub folders of the source folder are also included.

**Remote file filter > Date** sub tab

**Newer than**

Select a check type and enter a date or variable. Only files newer than the specified date will be included.

**Older than**

Select a check type and enter a date or variable. Only files older than the specified date will be included.

Use the AND/OR operator between the two date conditions to control how they are combined.

**Remote file filter > Size** sub tab

**Check if file is smaller than x size**

When checked, only files smaller than the specified size are included. Select the size unit (bytes, KB, MB, etc.).

**Check if file is larger than x size**

When checked, only files larger than the specified size are included. Select the size unit (bytes, KB, MB, etc.).

Use the AND/OR operator between the two size conditions to control how they are combined.

**Remote file filter > Result** sub tab

**Sort**

When checked, the matched file list is sorted before processing. Select the sort column and sort direction.

**Limit**

When checked, the number of matched files downloaded is limited to the specified value.

**Remote file filter > Test** sub tab

Click the *Show filtered files* button to preview which files match the current filter settings before running the task. The number of matched files and elapsed time are displayed.

**Download file(s) > Destination** tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/Download%20files%20destination.png)
 
**Credentials**

To control a remote computer you may need to use a Credential. The Credential must match the user name and password of the user that you want to login. Click on *Manage credentials* to add or edit Credentials. Select a Credential in the combo box.

**Destination folder**

The local folder to save the downloaded files in. Click the folder icon to browse and select a folder.

**Delete source file after download**

When checked, the source file on the SharePoint site is deleted after it has been successfully downloaded.
 
**Overwrite options**

Select how to handle files that already exist in the destination folder.

- *Overwrite if existing* — overwrite any existing file with the same name.
- *Overwrite if source is newer* — only overwrite if the source file is newer than the existing destination file.
- *Don't overwrite* — skip files that already exist in the destination. The task fails if a file with the same name is found.
