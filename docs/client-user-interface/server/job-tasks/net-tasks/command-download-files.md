---
sidebar_label: 'Command - Download File(s)'
hide_title: 'true'
---

## Command - Download File(s)

The Download command downloads one or more files from the remote server to a folder on the VisualCron Server or on a network share. It can include subfolders. The files are selected on the ***Remote File filter*** tab; see [Remote File Filter](../../job-tasks-remote-file-filter).

The Task output lists the downloaded files. When no file has been downloaded, the command raises the "No file(s) downloaded" error. Whether this error fails the Task is set on the ***On error*** tab; see [Task - On Error](../../task-on-error).

:::warning

The list of downloaded files and the "No file(s) downloaded" error cover the whole Task, not each command. When an earlier Download command of the same Task downloaded files, a later Download command that downloads nothing does not raise the error, and its output lists the files of the earlier command again. To check each download, put each Download command in its own Task.

:::

### Download tab

![Download tab of the Add/Edit command window, with the Source, Destination, Transfer type and Threading groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/Download.png)

- _Delete source file after copy_ (_Source_ group): when selected, each file is deleted from the remote server after the command has handled it; cleared by default

:::warning

The remote file is deleted even when it was not downloaded: when an _Overwrite options_ setting skipped it, and when the download still failed after the last _Resume if transfer failed_ try. To delete only files that were downloaded, use this option only with "Overwrite - always if existing", and with _Resume if transfer failed_ cleared. On SCP Connections, the file is deleted with `rm -rf`, as described on [Command - Delete Files](command-delete-files).

:::

- _Use raw listing fallback_: saved with the command but not used when the command runs, so selecting it does not change how files are listed; cleared by default

- _Destination folder_ (_Destination_ group): the local folder to save the files in, on the VisualCron Server or on a network share given as a UNC path

  For a network share, select a Credential on the ***Main settings*** tab. The folder is created if it does not exist. The field is required.

- _Download file mask_: the name to save each file under

  It is not a filter: it is applied to the name of every downloaded file. `*` keeps the remote file name and is the default. Wildcards change part of the name, for example `*.bak`. To choose which files to download, use the ***Remote File filter*** tab.

:::warning

A mask without wildcards gives every downloaded file the same local name, so each file overwrites the one before it.

:::

- _Overwrite options_: what happens when a file with the same name already exists in the _Destination folder_

  - "Overwrite - always if existing" (default): replaces the local file
  - "Overwrite - if newer": replaces the local file only if the remote file is newer
  - "Overwrite - if destination size is": replaces the local file depending on the size condition in the list next to it
  - "Append if destination is smaller - otherwise overwrite": if the local file is smaller, adds to it; otherwise replaces it
  - "Append if destination is smaller - otherwise overwrite if newer": if the local file is smaller, adds to it; otherwise replaces it only if the remote file is newer
  - "Append if destination is smaller - otherwise skip": if the local file is smaller, adds to it; otherwise skips the file
  - "Append if existing - otherwise create": adds the whole remote file to the end of the local file, or creates the local file if it does not exist
  - "Append if existing - otherwise skip": adds the whole remote file to the end of the local file; a file that does not exist locally is skipped on FTP and FTPS Connections and downloaded on SFTP and SCP Connections
  - "Do not overwrite if existing": keeps the local file and skips the remote file

  With "Overwrite - if newer", FTP and FTPS Connections compare the created date of the remote file, as the server lists it, with the modified date of the local file. SFTP and SCP Connections compare the modified dates.

:::warning

The three "Append if destination is smaller" options add to the local file in different ways. On FTP and FTPS Connections, only the part of the remote file that is missing from the local file is downloaded and added. On SFTP and SCP Connections, the whole remote file is added to the end of the local file, so the local file then holds its old content followed by the complete remote file. On SFTP and SCP Connections, use "Overwrite - always if existing" to replace a partly downloaded file.

:::

- Size condition (the list next to _Overwrite options_): available only when _Overwrite options_ is "Overwrite - if destination size is"

  The size of the existing local file is compared with the remote file:

  - "Larger": downloads when the local file is larger
  - "Smaller": downloads when the local file is smaller
  - "Same": downloads when the sizes are the same
  - "Smaller or larger": downloads when the sizes differ
  - "Different": never downloads; to download when the sizes differ, select "Smaller or larger"

  The default is "Smaller".

- _Resume if transfer failed. Try resuming_: tries a failed download again

  Set how many times to try and the interval in seconds between tries. The defaults are "3" times and "1" second; each can be set from "1" to "10000". Cleared by default.

  How the retry works depends on the protocol:

  - FTP and FTPS: the download continues from where it stopped, but only when _Download file mask_ is `*` and the file is in the current folder of the Connection; otherwise the file is not tried again and is skipped
  - SFTP: the whole remote file is downloaded again and added to the end of what the failed try had written
  - SCP: the download is not tried again; VisualCron waits for the set number of tries, then skips the file

:::warning

With this option selected, a file that still fails after the last try is skipped without an error, and the command continues with the next file. On SCP Connections this happens to every failed file. On SFTP Connections, a file that failed partway holds the part from the failed try followed by the complete file. If _Delete source file after copy_ is also selected, the remote file is deleted. On SFTP and SCP Connections, leave this option cleared, so that a failed download fails the command. On FTP and FTPS Connections, check the Task output, which lists the downloaded files.

:::

- _Keep modified/created date_: sets the dates of the downloaded file to those of the remote file; cleared by default

- _Replace unsupported characters with character_: replaces each character in a remote file name that Windows does not allow in file names with the character in the box

  Selected by default, and the default character is "c".

- _Save files to destination folder_: every file is saved directly in the _Destination folder_, whatever subfolder it came from

- _Save files to destination relative to source path_ (default): the subfolders below the source folder of the ***Remote File filter*** tab are recreated in the _Destination folder_

  For example, with the source folder `/ftp/download` and the _Destination folder_ `c:\test`, the file `/ftp/download/subfolder/filename` is saved as `c:\test\subfolder\filename`.

- _Save files to destination with full relative path_: the full remote path is recreated in the _Destination folder_

  In the same example, the file is saved as `c:\test\ftp\download\subfolder\filename`.

- _Override transfer type set in Connection_ (_Transfer type_ group): FTP and FTPS Connections only

  When selected, the transfer type selected in the list, "ASCII" or "Binary", is used for this command instead of the one set in the Connection. The default is "Binary". On SFTP and SCP Connections, the transfer type set in the Connection is used. See [Connection - FTP](../../connection-ftp).

- _Maximum number of threads_ (_Threading_ group): can be set from "1" to "8"; the default is "1"

  This setting is saved with the command but is not used when the command runs, and neither is _Maximum number of threads (download)_ on the Connection: files are downloaded one at a time.

- _Credential_ (***Main settings*** tab): the Credential that VisualCron uses to write the downloaded files when the _Destination folder_ is on a network share that the VisualCron Server's account cannot write to

  See [Global - Credentials](../../global-credentials).
