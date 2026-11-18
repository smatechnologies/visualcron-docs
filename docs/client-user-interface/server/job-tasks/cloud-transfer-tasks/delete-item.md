---
sidebar_label: 'Task Cloud Transfer - Delete Item'
hide_title: 'true'
---

## Task Cloud Transfer - Delete Item

The Cloud - Delete item(s) Task deletes files or folders in a cloud service: Amazon S3, Box, Dropbox, Google Drive, Google Cloud Storage, Microsoft Azure or OneDrive.

![Delete item(s) tab with the Remote file filter Location sub tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Delete%20Item(s).png)

:::warning

This Task uses a cloud Connection; see [Amazon S3](../../connection-amazon), [Box](../../connection-box), [Dropbox](../../connection-dropbox), [Google Drive](../../connection-google-drive), [Google Cloud Storage](../../connection-google-cloud), [Microsoft Azure](../../connection-microsoft-azure) or [OneDrive](../../connection-onedrive). The Amazon S3, Azure, Google Drive, Dropbox, Box and OneDrive Connections accept any server certificate, whatever _Auto-accept server certificates_ says. With Amazon S3, when a request fails with a particular secure-connection error, the Server repeats it without SSL, so that request and its data travel unencrypted.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Delete item(s) tab

The Task uses the [Cloud Remote file filter](../../job-tasks-cloud-remote-file-filter).

:::warning

Every item the filter returns is deleted when the Task runs. Use the ***Test*** sub tab of the filter to see which items would be deleted before you schedule the Job.

:::

### Output and errors

The output lists the deleted items.

:::warning

If the source folder is not found, nothing is deleted, and the Task reports success. With Google Drive, OneDrive and Box an error is written to standard error; with Amazon S3 and Google Cloud Storage nothing is written.

:::
