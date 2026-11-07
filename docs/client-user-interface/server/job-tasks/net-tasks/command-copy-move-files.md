---
sidebar_label: 'Command - Copy/Move Files'
hide_title: 'true'
---

## Command - Copy/Move Files

The Copy/Move file command copies or moves one or more files to another folder on the same remote server. The files are selected on the ***Remote File filter*** tab; see [Remote File Filter](../../job-tasks-remote-file-filter). The Task output lists the destination path of each file that was copied or moved.

When no file matches the filter, the command raises the "No file(s) found" error. On FTP and FTPS Connections, the error is also raised when files match but none is copied or moved. Whether this error fails the Task is set on the ***On error*** tab; see [Task - On Error](../../task-on-error).

### Copy/Move tab

![Copy/Move tab of the Add/Edit command window, with the Destination folder, New file name mask, Overwrite options and Keep existing file (Copy) settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/FTP%20Copy%20Move.png)

- _Destination folder_: the folder on the remote server to copy or move the files to

  Click the browse button to select a folder on the server.

- _Create folder if not existing_: creates the _Destination folder_ if it does not exist; selected by default

- _New file name mask_: the name of each file in the destination

  `*` keeps the original name and is the default. Use wildcards to change part of the name.

- _Overwrite options_: what happens when a file with the same name already exists in the _Destination folder_

  - "Overwrite - always if existing" (default): replaces the existing file
  - "Overwrite - if newer": replaces the existing file only if the source file is newer
  - "Overwrite - if destination size is": replaces the existing file depending on the size condition in the list next to it
  - "Do not overwrite if existing": skips the file on SFTP and SCP Connections

:::warning

On FTP and FTPS Connections, "Do not overwrite if existing" does not skip the file. A copy replaces the existing file. A move renames the source file over the existing file; depending on the server, this replaces the existing file or fails. To keep existing files, use an SFTP or SCP Connection, or check for the file in an earlier step.

On SCP Connections, the command checks only whether the destination file exists; it does not read its date or size. "Overwrite - if newer" then always replaces the existing file. With "Overwrite - if destination size is", "Larger" and "Different" replace the existing file whenever the source file is not empty, "Same" replaces it only when the source file is empty, and "Smaller" and "Smaller or larger" never replace it. On SCP Connections, use "Overwrite - always if existing" or "Do not overwrite if existing".

:::

- Size condition (the list next to _Overwrite options_): available only when _Overwrite options_ is "Overwrite - if destination size is"

  The size of the source file is compared with the size of the existing file in the destination. On FTP, FTPS and SFTP Connections:

  - "Larger": copies when the source file is larger, that is, when the existing file is smaller
  - "Smaller": copies when the source file is smaller
  - "Same": copies when the sizes are the same
  - "Smaller or larger": copies when the source file is smaller, the same as "Smaller"
  - "Different": copies when the sizes differ on SFTP Connections, and never copies on FTP and FTPS Connections

  The default is "Smaller". For SCP Connections, see the warning above.

- _Keep existing file (Copy)_: when selected, the command copies, and the source file stays where it is

  When cleared, the command moves the file. Selected by default.

How the files are copied or moved depends on the protocol:

- FTP and FTPS: FTP has no copy on the server, so each file is downloaded to a temporary file on the VisualCron Server and uploaded to the destination; a move renames the file on the server
- SFTP: the server is asked to copy the file, and if it cannot, the file is downloaded and uploaded as for FTP; a move removes any existing file with the same name in the destination, then renames the source file
- SCP: VisualCron runs `scp` on the remote server with the paths passed without quotes, and the result is not checked

:::warning

On SCP Connections, a move removes the source file only when a file with the same name already existed in the destination. Otherwise the file is copied, the source file stays in place, and the command reports success. To move files, use an SFTP Connection to the same server if the server supports it, or delete the source files in a later step.

:::
