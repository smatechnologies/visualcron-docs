---
sidebar_label: 'Overview'
hide_title: 'true'
---

## Overview

Cloud storage is a model of data storage in which the digital data is stored in logical pools, the physical storage spans multiple servers (and often locations), and the physical environment is typically owned and managed by a hosting company.

The Cloud Tasks in VisualCron currently support the following cloud services:

* [Amazon S3](../../connection-amazon)
* [Box](../../connection-box)
* [Dropbox](../../connection-dropbox)
* [Google Drive](../../connection-google-drive)
* [Google Cloud Storage](../../connection-google-cloud)
* [Microsoft Azure](../../connection-microsoft-azure) (Block blob, Page blob, File Shares, Data Lake Gen V1, Data Lake Gen V2)
* [OneDrive](../../connection-onedrive)

Different [Connections](../../global-connections) are used depending on the cloud service provider. The same task interface is shared across all of them — the controls adapt to the selected connection (for example, the *Bucket/Container* field is labelled *Bucket* for Amazon S3, *Container* for Azure block/page blobs, *Share* for Azure File Shares, *File system* for Azure Data Lake Gen V2 and *Drive* for Google Drive).

**Available Cloud Tasks**

Tasks that work on remote items via the standard [Cloud Remote file filter](../../job-tasks-cloud-remote-file-filter):

* [List item(s)](list-item) - list files and/or folders matching a filter
* [Download file(s)](download-file) - download files to the local file system
* [Delete item(s)](delete-item) - delete files and/or folders
* [Copy/Move item(s)](copy-move) - copy or move items to another folder *within the same connection* (server-side where supported)

Tasks that use other filter / configuration models:

* [Upload file(s)](upload-file) - upload files from the local file system using the standard [File filter](../../job-tasks-file-filter)
* [Create folder](create-folder) - create a folder at a specific cloud path (no filter)
* [Sync](sync) - synchronize a source and a target location; either side can be a cloud connection, an FTP / SFTP / WinSCP connection or the local file system, and the matching filter is shown automatically
