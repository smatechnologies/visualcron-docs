---
sidebar_label: 'Task Cloud Transfer - Create Folder'
hide_title: 'true'
---

## Task Cloud Transfer - Create Folder

The Cloud - Create folder Task creates a folder in a cloud service: Amazon S3, Box, Dropbox, Google Drive, Google Cloud Storage, Microsoft Azure or OneDrive.

![Create folder tab with the Connection and New folder location groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Create%20Folder.png)

:::warning

This Task uses a cloud Connection; see [Amazon S3](../../connection-amazon), [Box](../../connection-box), [Dropbox](../../connection-dropbox), [Google Drive](../../connection-google-drive), [Google Cloud Storage](../../connection-google-cloud), [Microsoft Azure](../../connection-microsoft-azure) or [OneDrive](../../connection-onedrive). The Amazon S3, Azure, Google Drive, Dropbox, Box and OneDrive Connections accept any server certificate, whatever _Auto-accept server certificates_ says.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Create folder tab

- _Connection_: The cloud [Connection](../../global-connections) to use. Click the _Settings_ icon to open _Manage Connections_
- _Bucket/Container_: The top-level storage the Connection uses. The label follows the selected Connection:
  - _Bucket_: Amazon S3
  - _Container_: Microsoft Azure with Block or Page blob access
  - _Share_: Microsoft Azure File Shares
  - _File system_: Microsoft Azure Data Lake Gen V2
  - _Drive_: Google Drive

  The field is not used, and is unavailable, for Dropbox, Box and Microsoft Azure Data Lake Gen V1 Connections. Click the folder icon to list what the Connection offers.
- _Path to new folder_: The full path of the folder to create. Click the folder icon to browse the Connection for the parent folder. [Variables](../../global-variables) are resolved

:::note

With Microsoft Azure Block or Page blob storage, _Path to new folder_ is unavailable: the Task creates the container named in _Container_ if it does not exist. Azure Block and Page blob storage uses virtual folders, which do not exist until a file is placed in them.

:::

### Output and errors

The output is the path of the new folder. When the folder already exists, the output can be empty.
