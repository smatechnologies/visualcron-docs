---
sidebar_label: 'Task Cloud Transfer - Delete Item'
hide_title: 'true'
---

## Task Cloud Transfer - Delete Item

The Cloud - Delete item(s) Task deletes files and/or folders from a cloud service such as Amazon S3, Box, Dropbox, Google Drive, Google Storage, Microsoft Azure or OneDrive.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Delete%20Item(s).png)

**Configuration**

This Task is configured entirely through the standard [Cloud Remote file filter](../../job-tasks-cloud-remote-file-filter), which provides:

* _Location_ - Connection, Bucket/Container (label changes per protocol: Bucket, Container, Share, File system or Drive), Source folder, Item mask, Filter (Files / Folders / All), Case sensitive and Include sub folders
* _Date_ - filter on Modified date and/or Created date using values or Variables, combined with AND/OR
* _Size_ - filter files smaller than and/or larger than a given size, combined with AND/OR
* _Result_ - sort the matched items and limit the result count
* _Test_ - run the filter and preview the items that would be deleted before saving the Task

Every item returned by the filter is deleted when the Task runs. Use the *Test* sub tab to confirm the filter matches what you expect before scheduling the Job.

**Supported connections**

Only cloud connections are listed in the Connection selector: Amazon S3, Windows Azure (excluding Management-type connections), OneDrive, Google Drive, Google Storage, Dropbox and Box.

**Recursive folder deletion**

Folder deletion is handled per protocol. Amazon S3 deletes objects individually, while Azure (Block, Page, File Shares, Data Lake Gen V1, Data Lake Gen V2) and Google Drive recursively delete the contents of a folder. Enable *Include sub folders* on the *Location* sub tab to traverse into nested folders during the match.

**Output**

The Task produces a list of deleted items on the task result, available to later Tasks in the Job. Cancellation is checked per item, so stopping the Task mid-run leaves any not-yet-processed items intact.
