---
sidebar_label: 'Overview'
hide_title: 'true'
---

## Overview

Cloud storage keeps data in pools that a hosting company runs, often spread over several servers and locations.

The Cloud Tasks work with these cloud services:

* [Amazon S3](../../connection-amazon)
* [Box](../../connection-box)
* [Dropbox](../../connection-dropbox)
* [Google Drive](../../connection-google-drive)
* [Google Cloud Storage](../../connection-google-cloud)
* [Microsoft Azure](../../connection-microsoft-azure) (Block blob, Page blob, File Shares, Data Lake Gen V1, Data Lake Gen V2)
* [OneDrive](../../connection-onedrive)

Each cloud service has its own [Connection](../../global-connections) type. All the Cloud Tasks share one set of controls, which adapt to the selected Connection: for example, the _Bucket/Container_ field is labeled _Bucket_ for Amazon S3, _Container_ for Azure Block and Page blobs, _Share_ for Azure File Shares, _File system_ for Azure Data Lake Gen V2 and _Drive_ for Google Drive.

:::warning

The Amazon S3, Azure, Google Drive, Dropbox, Box and OneDrive Connections accept any server certificate, whatever _Auto-accept server certificates_ says. With Amazon S3, when a request fails with a particular secure-connection error, the Server repeats it without SSL, so that request and its data travel unencrypted.

:::

**Available Cloud Tasks**

Tasks that work on cloud items through the standard [Cloud Remote file filter](../../job-tasks-cloud-remote-file-filter):

* [List item(s)](list-item): list files or folders that match the filter
* [Download file(s)](download-file): download files to the Server computer or a network share
* [Delete item(s)](delete-item): delete files or folders
* [Copy/Move item(s)](copy-move): copy or move items to another folder within the same Connection

Tasks that use other filters or settings:

* [Upload file(s)](upload-file): upload files from the Server computer or a network share, chosen with the standard [File filter](../../job-tasks-file-filter)
* [Create folder](create-folder): create a folder at a cloud path
* [Sync](sync): synchronize a source and a target; each side can be a cloud Connection, an FTP, SFTP or WinSCP Connection, or local files, and the matching filter is shown for each side
