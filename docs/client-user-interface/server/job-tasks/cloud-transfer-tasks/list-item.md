---
sidebar_label: 'Task Cloud Transfer - List Item'
hide_title: 'true'
---

## Task Cloud Transfer - List Item

The Cloud - List item(s) Task lists files and/or folders in a cloud service such as Amazon S3, Box, Dropbox, Google Drive, Google Storage, Microsoft Azure or OneDrive. The matched items are returned as task output and can be referenced by later Tasks in the Job.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/List%20Items.png)

**Configuration**

This Task is configured entirely through the standard [Cloud Remote file filter](../../job-tasks-cloud-remote-file-filter), which provides:

* _Location_ - Connection, Bucket/Container (label changes per protocol: Bucket, Container, Share, File system or Drive), Source folder, Item mask, Filter (Files / Folders / All), Case sensitive and Include sub folders
* _Date_ - filter on Modified date and/or Created date using values or Variables
* _Size_ - filter files smaller than and/or larger than a given size
* _Result_ - sort the matched items and limit the result count
* _Test_ - run the filter and preview the items that would be returned

**Supported connections**

Only cloud connections are listed in the Connection selector: Amazon S3, Windows Azure (excluding Management-type connections), OneDrive, Google Drive, Google Storage, Dropbox and Box.

**Output**

The Task produces a list of items that match the filter, available on the task result for use in later Tasks (for example via Variables). If no items match the filter the Task fails with a *File not found* error.
