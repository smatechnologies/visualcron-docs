---
sidebar_label: 'Task Cloud Transfer - Download File'
hide_title: 'true'
---

## Task Cloud Transfer - Download File

The Cloud - Download file(s) Task downloads files from a cloud service, Amazon S3, Box, Dropbox, Google Drive, Google Cloud Storage, Microsoft Azure or OneDrive, to a folder on the Server computer or a network share.

:::warning

This Task uses a cloud Connection; see [Amazon S3](../../connection-amazon), [Box](../../connection-box), [Dropbox](../../connection-dropbox), [Google Drive](../../connection-google-drive), [Google Cloud Storage](../../connection-google-cloud), [Microsoft Azure](../../connection-microsoft-azure) or [OneDrive](../../connection-onedrive). The Amazon S3, Azure, Google Drive, Dropbox, Box and OneDrive Connections accept any server certificate, whatever _Auto-accept server certificates_ says. With Amazon S3, when a request fails with a particular secure-connection error, the Server repeats it without SSL, so that request and its data travel unencrypted.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Download file(s) tab

#### Remote file filter sub tab

The Task uses the standard [Cloud Remote file filter](../../job-tasks-cloud-remote-file-filter) to choose the Connection, the bucket or container, the source folder, the item mask, the date and size filters, the sorting and the result limit. Every file the filter returns is downloaded; folders are not.

#### Destination sub tab

The screenshot shows the ***Remote file filter*** sub tab.

![Download file(s) tab with the Remote file filter Location sub tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Download%20file(s).png)

- The Credential list: the [Credential](../../global-credentials) the Server uses to write to the destination, for example a network share. With "No Credential", the Server writes as its service account
- _Destination folder_: The folder the files are written to. Required. Subfolders found by the filter are recreated under it. [Variables](../../global-variables) are resolved
- _Download file mask_: Renames the downloaded files; `*` (the default) keeps each file's name. It does not select files: the filter does
- _Overwrite options_: What to do when the file already exists at the destination:
  - "Overwrite - always if existing": replace it. The default
  - "Overwrite - if newer": replace it only if the source file is newer
  - "Overwrite - if destination size is": replace it depending on the sizes, set in the list next to it
  - "Do not overwrite if existing": skip the file
- the list next to _Overwrite options_: with "Overwrite - if destination size is", when to replace the destination file:
  - "Same": the destination has the same size as the source
  - "Smaller": the destination is smaller than the source
  - "Larger": the destination is larger than the source
  - "Smaller or larger" or "Different": the sizes differ
- _Keep modified/created date_: When selected, the created and modified dates of each downloaded file are set to the cloud file's modified date
- _Delete source file after download_: When selected, each cloud file is deleted after it is downloaded. A file that is not downloaded, for example because _Overwrite options_ skips it, is not deleted

:::warning

With the default, "Overwrite - always if existing", existing local files are replaced. When the Task replaces an existing local file, it empties that file before the download starts; if the download then fails, the local file is left empty or incomplete. With _Delete source file after download_ selected, the cloud files are deleted after they are downloaded.

:::

### Output and errors

The output lists the downloaded files.

:::warning

If the source folder is not found, nothing is downloaded, and the Task reports success. With Google Drive, OneDrive and Box an error is written to standard error; with Amazon S3 and Google Cloud Storage nothing is written.

:::
