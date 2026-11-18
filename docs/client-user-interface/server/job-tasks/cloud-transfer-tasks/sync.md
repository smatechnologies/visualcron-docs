---
sidebar_label: 'Task Cloud Transfer - Sync'
hide_title: 'true'
---

## Task Cloud Transfer - Sync

The Cloud - Sync file(s) Task synchronizes files between a source and a target. Each side can be a cloud service (Amazon S3, Box, Dropbox, Google Drive, Google Cloud Storage, Microsoft Azure or OneDrive), an FTP, SFTP or WinSCP server, or local files.

:::warning

This Task can use a cloud Connection; see [Amazon S3](../../connection-amazon), [Box](../../connection-box), [Dropbox](../../connection-dropbox), [Google Drive](../../connection-google-drive), [Google Cloud Storage](../../connection-google-cloud), [Microsoft Azure](../../connection-microsoft-azure) or [OneDrive](../../connection-onedrive). The Amazon S3, Azure, Google Drive, Dropbox, Box and OneDrive Connections accept any server certificate, whatever _Auto-accept server certificates_ says. With Amazon S3, when a request fails with a particular secure-connection error, the Server repeats it without SSL, so that request and its data travel unencrypted. For FTP, SFTP and WinSCP, see [Connection - FTP](../../connection-ftp) and [Connection - SFTP](../../connection-sftp): SFTP accepts any host key, and FTP _Auto-accept server certificates_ is selected on a new Connection.

:::

The Task copies the files through a temporary folder on the Server computer, and deletes the folder at the end of the run.

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Sync file(s) tab

#### Connections sub tab

![Sync file(s) Connections sub tab with the source and target Connections](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Sync%20file(s).png)

- _Source connection_: The Connection for the source. Only cloud, FTP, SFTP and WinSCP Connections are listed
- _Local files_ (source): When selected, the source is local files instead of a Connection. _Source connection_ is then unavailable, and the target must be a Connection: source and target cannot both be local
- _Target connection_: The Connection for the target. The same Connection types are listed
- _Local files_ (target): When selected, the target is local files instead of a Connection, and the source must be a Connection

#### Source file filter sub tab

Sets which source files take part. The filter follows the source type:

- cloud Connection: the standard [Cloud Remote file filter](../../job-tasks-cloud-remote-file-filter)
- FTP, SFTP or WinSCP Connection: the standard [Remote file filter](../../job-tasks-remote-file-filter)
- local files: the standard [File filter](../../job-tasks-file-filter)

Only the filter for the current source type is shown; it changes when the Connection or _Local files_ changes.

#### Target file filter sub tab

Sets which target files take part, with the same three filter types, chosen by the target type.

#### Sync options sub tab

![Sync options sub tab with the conflict, flow and source missing settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Sync%20Options.png)

- _Resolve same name conflicts as_: What to do when a file with the same path exists on both sides:
  - "Take Source": use the source file
  - "Take Target": use the target file
  - "Take Newer": use the file modified more recently. The default
  - "Take Older": use the file modified earlier
  - "Take Bigger": use the larger file
  - "Take Smaller": use the smaller file
  - "Skip": leave both files as they are
- _Resolve equal file conflicts as_: What to do when the rule above cannot decide, for example two files with the same date under "Take Newer". Available with "Take Newer", "Take Older", "Take Bigger" and "Take Smaller":
  - "Take source": use the source file
  - "Take Target": use the target file
  - "Skip": leave both files. The default
- _Sync Flow_: The direction:
  - `Source -> Target`: copy from source to target only
  - `Target ->Source`: copy from target to source only
  - `Source <-> Target`: copy in both directions. The default
- _Source missing action_: What to do with files that exist on the side the flow copies to but not on the side it copies from, for example files deleted after an earlier sync. Applies to the one-way flows only:
  - "Delete": delete them from the side the flow copies to: the target with `Source -> Target`, the source with `Target ->Source`
  - "Skip": leave them. The default
- _Delete source file after download_: When selected, each file is deleted from the side it was copied from, after it is copied. The label shows the side, _Delete file at Source after download_ or _Delete file at Target after download_. Available for the one-way flows only

:::warning

If the Task cannot find the cloud folder or bucket on the side the flow copies from, it continues as if that side were empty. With Google Drive, OneDrive and Box an error is written to standard error; with Amazon S3 and Google Cloud Storage nothing is written. With _Source missing action_ "Delete", the Task then deletes every file that the filter on the other side returns, and the Task reports success. Check the paths before you use "Delete". With _Delete source file after download_ selected, the copied files are deleted from the side they were copied from.

:::

#### Credential

The Task's [Credential](../../global-credentials) is used to write the files it downloads from a cloud side into its temporary folder. A Credential set on a local File filter is used for that side's files.

### Output and errors

- The output has one line for each copied file: the path it was copied from and the path it was copied to, separated by `|`
- If a cloud side cannot be listed, the Task reports success; an error is written to standard error only with Google Drive, OneDrive and Box
