---
sidebar_label: 'Task Cloud Transfer - Copy/Move'
hide_title: 'true'
---

## Task Cloud Transfer - Copy/Move

The Cloud - Copy/Move item(s) Task copies or moves files between folders within a single cloud connection (Amazon S3, Box, Dropbox, Google Drive, Google Storage, Microsoft Azure or OneDrive).

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Copy%20Move%20Item(s).png)

:::tip Note

Source and destination must be on the same Connection. The *Destination folder* is a path within the same bucket/container/drive selected on the *Remote file filter* sub tab. To move files between two different cloud accounts use the [Sync](sync) task or chain a [Download](download-file) and [Upload](upload-file) task together.

:::

**Copy/Move item(s) > Remote file filter** sub tab

This Task uses the standard [Cloud Remote file filter](../../../server/job-tasks-cloud-remote-file-filter) to define the connection, bucket/container, source folder, item mask, date and size filters, sorting and result limit. Every item returned by the filter is copied (or moved).

**Copy/Move item(s) > Destination** sub tab

**Destination folder**

The folder within the same Connection where the matched items will be copied or moved to. Click the *Folder* icon to browse the cloud and pick the destination.

**Keep modified/created date**

When checked, the modified and created dates from the source file are preserved on the destination file (where the cloud service supports it).

**Delete source file (move)**

When checked, the source file is deleted after a successful copy, effectively turning the operation into a move. When unchecked the operation is a copy and the source remains in place.

**Overwrite options**

Select what to do if a file already exists at the destination. Available options:

* _Overwrite - always if existing_ - always overwrites the destination file
* _Overwrite - if newer_ - overwrites only if the source file is newer than the destination
* _Overwrite - if destination size is_ - overwrites based on a size comparison; enables the size comparison dropdown below
* _Append if destination is smaller - otherwise overwrite_ - appends to the destination if it is smaller than the source, otherwise overwrites
* _Append if destination is smaller - otherwise overwrite if newer_ - appends if smaller, otherwise overwrites only if newer
* _Append if destination is smaller - otherwise skip_ - appends if smaller, otherwise skips
* _Append if existing - otherwise create_ - appends to an existing file or creates a new one
* _Append if existing - otherwise skip_ - appends to an existing file or skips if it does not exist
* _Do not overwrite if existing_ - skips the file if it already exists at the destination

**Size comparison**

Only enabled when *Overwrite options* is set to _Overwrite - if destination size is_. Selects the size comparison criterion used to decide whether to overwrite:

* _Same_ - overwrites if the destination is the same size as the source
* _Smaller_ - overwrites if the destination is smaller than the source
* _Larger_ - overwrites if the destination is larger than the source
* _Smaller or larger_ - overwrites if the destination differs in size from the source
* _Different_ - overwrites if the sizes differ
