---
sidebar_label: 'Task Cloud Transfer - Copy/Move'
hide_title: 'true'
---

## Task Cloud Transfer - Copy/Move

The Cloud - Copy/Move item(s) Task copies or moves files and folders to another folder within the same cloud Connection: Amazon S3, Box, Dropbox, Google Drive, Google Cloud Storage, Microsoft Azure or OneDrive.

![Copy/move item(s) tab with the Remote file filter Location sub tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Copy%20Move%20Item(s).png)

:::warning

This Task uses a cloud Connection; see [Amazon S3](../../connection-amazon), [Box](../../connection-box), [Dropbox](../../connection-dropbox), [Google Drive](../../connection-google-drive), [Google Cloud Storage](../../connection-google-cloud), [Microsoft Azure](../../connection-microsoft-azure) or [OneDrive](../../connection-onedrive). The Amazon S3, Azure, Google Drive, Dropbox, Box and OneDrive Connections accept any server certificate, whatever _Auto-accept server certificates_ says. With Amazon S3, when a request fails with a particular secure-connection error, the Server repeats it without SSL, so that request and its data travel unencrypted.

:::

:::note

Source and destination must be on the same Connection: the _Destination folder_ is a path in the bucket, container or drive selected on the ***Remote file filter*** sub tab. To move files between two cloud accounts, use the [Sync](sync) Task, or a [Download](download-file) Task followed by an [Upload](upload-file) Task.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Copy/move item(s) tab

#### Remote file filter sub tab

The Task uses the standard [Cloud Remote file filter](../../job-tasks-cloud-remote-file-filter) to choose the Connection, the bucket or container, the source folder, the item mask, the date and size filters, the sorting and the result limit. Every item the filter returns is copied or moved.

#### Destination sub tab

- _Destination folder_: The folder, within the same Connection, that the items are copied or moved to. Click the folder icon to browse the Connection. [Variables](../../global-variables) are resolved
- _Keep modified/created date_: Keeps the source file's modified date on the copy. Only Google Drive supports it; with the other services the option has no effect
- _Delete source file (move)_: When selected, the Task deletes each source item after copying it, so the items are moved. When cleared, the items are copied
- _Overwrite options_: What to do when an item already exists at the destination:
  - "Overwrite - always if existing": replace it. The default
  - "Overwrite - if newer": replace it only if the source is newer
  - "Overwrite - if destination size is": replace it depending on the sizes, set in the list next to it
  - "Append if destination is smaller - otherwise overwrite", "Append if destination is smaller - otherwise overwrite if newer", "Append if destination is smaller - otherwise skip", "Append if existing - otherwise create" and "Append if existing - otherwise skip": see the warning below
  - "Do not overwrite if existing": skip the item
- the list next to _Overwrite options_: with "Overwrite - if destination size is", when to replace the destination file:
  - "Same": the destination has the same size as the source
  - "Smaller": the destination is smaller than the source
  - "Larger": the destination is larger than the source
  - "Smaller or larger" or "Different": the sizes differ

:::warning

The Append options do not append. With any of them, the Task replaces the existing destination file, as with "Overwrite - always if existing", which is the default. With _Delete source file (move)_ selected, the source items are deleted after they are copied.

:::

### Output and errors

The output lists the items that were copied or moved.

:::warning

If the source folder cannot be read, for example because it does not exist, nothing is copied, no error is written, and the Task reports success.

:::
