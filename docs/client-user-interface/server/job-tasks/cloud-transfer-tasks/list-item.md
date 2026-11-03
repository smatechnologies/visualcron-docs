---
sidebar_label: 'Task Cloud Transfer - List Item'
hide_title: 'true'
---

## Task Cloud Transfer - List Item

The Cloud - List item(s) Task lists files or folders in a cloud service: Amazon S3, Box, Dropbox, Google Drive, Google Cloud Storage, Microsoft Azure or OneDrive. The items are returned as the Task output, for later Tasks in the Job.

![List item(s) tab with the Remote file filter Location sub tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/List%20Items.png)

:::warning

This Task uses a cloud Connection; see [Amazon S3](../../connection-amazon), [Box](../../connection-box), [Dropbox](../../connection-dropbox), [Google Drive](../../connection-google-drive), [Google Cloud Storage](../../connection-google-cloud), [Microsoft Azure](../../connection-microsoft-azure) or [OneDrive](../../connection-onedrive). The Amazon S3, Azure, Google Drive, Dropbox, Box and OneDrive Connections accept any server certificate, whatever _Auto-accept server certificates_ says. With Amazon S3, when a request fails with a particular secure-connection error, the Server repeats it without SSL, so that request and its data travel unencrypted.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### List item(s) tab

The Task uses the [Cloud Remote file filter](../../job-tasks-cloud-remote-file-filter).

### Output and errors

- The output lists the items the filter returns, one per line
- When the filter returns no items, the Task raises a "file not found" error; the ***On error*** tab decides whether it fails the Task
- If the source folder cannot be read, the error is written to standard error (Google Drive, OneDrive and Box)
