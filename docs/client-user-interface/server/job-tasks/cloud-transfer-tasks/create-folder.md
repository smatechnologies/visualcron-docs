---
sidebar_label: 'Task Cloud Transfer - Create Folder'
hide_title: 'true'
---

## Task Cloud Transfer - Create Folder

The Cloud - Create folder Task creates a folder in a cloud service such as Amazon S3, Box, Dropbox, Google Drive, Google Storage, Microsoft Azure or OneDrive.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Create%20Folder.png)

**Connection**

To use a specific cloud service you need to create a [Connection](../../global-connections) first. Click the *Settings* icon to open the *Manage Connections* dialog.

**Bucket/Container**

The label and behavior of this field changes depending on the selected connection:

* _Bucket_ - Amazon S3
* _Container_ - Windows Azure (Block or Page blob access)
* _Share_ - Windows Azure File Shares
* _File system_ - Windows Azure Data Lake Gen V2
* _Drive_ - Google Drive
* _Bucket/Container_ - the field is disabled for connections that do not use a top-level container (for example OneDrive, Dropbox, Box, Google Storage and Azure Data Lake Gen V1)

Click the *Folder* icon to list all available Buckets/Containers for the selected Connection.

**Path to new folder**

The full path to the folder to create. Click the *Folder* icon to browse the cloud and pick the parent location. Variables are supported.

:::tip Note

Microsoft Azure (Block/Page blob) operates virtual folders. A virtual folder does not actually exist in Azure until a file is placed into it.

:::
