---
sidebar_label: 'Task Cloud Transfer - Upload File'
hide_title: 'true'
---

## Task Cloud Transfer - Upload File

The Cloud - Upload file(s) Task uploads files from the Server computer or a network share to a cloud service: Amazon S3, Box, Dropbox, Google Drive, Google Cloud Storage, Microsoft Azure or OneDrive.

:::warning

This Task uses a cloud Connection; see [Amazon S3](../../connection-amazon), [Box](../../connection-box), [Dropbox](../../connection-dropbox), [Google Drive](../../connection-google-drive), [Google Cloud Storage](../../connection-google-cloud), [Microsoft Azure](../../connection-microsoft-azure) or [OneDrive](../../connection-onedrive). The Amazon S3, Azure, Google Drive, Dropbox, Box and OneDrive Connections accept any server certificate, whatever _Auto-accept server certificates_ says. With Amazon S3, when a request fails with a particular secure-connection error, the Server repeats it without SSL, so that request and its data travel unencrypted.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Upload file(s) tab

#### Main settings sub tab

![Upload file(s) Main settings sub tab with the Connection and Destination upload folder groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Upload%20Main%20Settings.png)

- _Connection_: The cloud [Connection](../../global-connections) to use. Click the _Settings_ icon to open _Manage Connections_
- _Bucket/Container_: The top-level storage the Connection uses. The label follows the selected Connection:
  - _Bucket_: Amazon S3
  - _Container_: Microsoft Azure with Block or Page blob access
  - _Share_: Microsoft Azure File Shares
  - _File system_: Microsoft Azure Data Lake Gen V2
  - _Drive_: Google Drive

  The field is not used, and is unavailable, for Dropbox, Box and Microsoft Azure Data Lake Gen V1 Connections. Click the folder icon to list what the Connection offers.
- _Destination folder_: The cloud folder the files are uploaded to. Click the folder icon to browse the Connection; where the Connection uses a bucket or container, select it first. [Variables](../../global-variables) are resolved
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
- _Keep modified/created date_: When selected, the dates of the local files are kept on the uploaded files, where the cloud service supports it

:::warning

With the default, "Overwrite - always if existing", files that already exist in the destination folder are replaced.

:::

#### File filter sub tab

The Task uses the standard [File filter](../../job-tasks-file-filter) to choose the local files to upload: the source folder, include and exclude masks, subfolders and date filters. The Credential on the File filter is used to read the files.

### Output and errors

The output lists the uploaded files.
