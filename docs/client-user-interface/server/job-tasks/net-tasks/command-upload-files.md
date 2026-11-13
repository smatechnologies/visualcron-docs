---
sidebar_label: 'Command - Upload File(s)'
hide_title: 'true'
---

## Command - Upload File(s)

The Upload command sends one or more files from the VisualCron Server, or from a network share, to a folder on the remote server, and creates folders on the remote server when needed.

The Task output lists the uploaded files. When the command uploads no file, it raises the "No file(s) uploaded" error. Whether this error fails the Task is set on the ***On error*** tab; see [Task - On Error](../../task-on-error).

### File filter tab

![File filter tab of the Add/Edit command window for an Upload command, with the Location subtab and its Credentials, Folder and file mask settings](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/Upload%20Settings.png)

The ***File filter*** tab selects the local files to upload; see [File Filter](../../job-tasks-file-filter). If the source folder is on a network share, select a Credential in the _Credentials_ box on the ***Location*** subtab, and enter the folder as a UNC path. The _Credential_ box on the ***Main settings*** tab is not shown for Upload.

### Upload tab

![Upload tab of the Add/Edit command window, with the Source, Destination, Transfer type and Threading groups](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/Upload.png)

- _Delete source file after copy_ (_Source_ group): deletes each local source file after it has been uploaded

  Files that were not uploaded, for example because of the _Overwrite options_, are kept. Cleared by default.

- _Destination folder_ (_Destination_ group): the folder on the remote server to upload to, for example `/topfolder/subfolder`

  Click the browse button to select a folder on the server. The default is `/`. The field is required.

- _Overwrite options_: what happens when a file with the same name already exists in the _Destination folder_

  - "Overwrite - always if existing" (default): replaces the remote file
  - "Overwrite - if newer": replaces the remote file only if the local file is newer
  - "Overwrite - if destination size is": replaces the remote file depending on the size condition in the list next to it
  - "Append if destination is smaller - otherwise overwrite": if the remote file is smaller, adds the missing part to it (see below); otherwise replaces it
  - "Append if destination is smaller - otherwise overwrite if newer": if the remote file is smaller, adds the missing part to it (see below); otherwise replaces it only if the local file is newer
  - "Append if destination is smaller - otherwise skip": if the remote file is smaller, adds the missing part to it (see below); otherwise skips the file
  - "Append if existing - otherwise create": on FTP, FTPS and SFTP Connections, adds the whole local file to the end of the remote file, or creates the remote file if it does not exist; on SCP Connections, uploads nothing
  - "Append if existing - otherwise skip": uploads nothing, on every Connection type, so the command raises the "No file(s) uploaded" error
  - "Do not overwrite if existing": keeps the remote file and skips the local file

  On FTP and FTPS Connections, the three "Append if destination is smaller" options upload only the missing part of the local file.

:::warning

On SFTP and SCP Connections, "Overwrite - if destination size is" and the three "Append if destination is smaller" options fail with an error for every file, whether or not it is on the server, and no sizes are compared. If _Resume if transfer failed_ is selected, the retry uploads a file that is not on the server, and skips a remote file of the same size or larger without an error. A smaller remote file gets the whole local file added to its end on SFTP Connections, which corrupts it, and is replaced with the whole local file on SCP Connections. On SFTP and SCP Connections, use "Overwrite - always if existing" or "Do not overwrite if existing".

:::

- Size condition (the list next to _Overwrite options_): available only when _Overwrite options_ is "Overwrite - if destination size is"

  On FTP and FTPS Connections, the size of the existing remote file is compared with the local file:

  - "Larger": uploads when the remote file is larger
  - "Same": uploads when the sizes are the same
  - "Different": uploads when the remote file is smaller
  - "Smaller or larger": uploads when the remote file is larger
  - "Smaller": never uploads

  The default is "Smaller". To upload when the remote file is smaller, select "Different".

- _Resume if transfer failed. Try resuming_: tries a failed upload again

  Set how many times to try and the interval in seconds between tries. The defaults are "3" times and "1" second; each can be set from "1" to "10000". Cleared by default.

  How the retry works depends on the protocol:

  - FTP and FTPS: the upload continues from where it stopped
  - SFTP: if part of the file reached the server, the whole local file is added to the end of that part; otherwise the file is uploaded again
  - SCP: the whole file is uploaded again if the remote file is missing or smaller than the local file; otherwise the file is skipped

:::warning

With this option selected, a file that still fails after the last try is skipped without an error. If other files were uploaded, the command and the Task succeed although that file is missing on the server. Check the Task output, which lists the uploaded files, or check the remote folder in a later step.

:::

- _Keep modified/created date_: sets the dates of the uploaded file to those of the local file; cleared by default

  On FTP and FTPS Connections, this works only when the server supports the `MFMT` command; otherwise the dates are not set and no error is raised. On SFTP Connections, if the server rejects setting the dates, the command reports an error although the file has been uploaded, and _Delete source file after copy_ does not delete the local file. On SCP Connections, the dates are not set.

- _Override transfer type set in Connection_ (_Transfer type_ group): FTP and FTPS Connections only

  When selected, the transfer type selected in the list, "ASCII" or "Binary", is used for this command instead of the one set in the Connection. The default is "Binary". On SFTP and SCP Connections, the transfer type set in the Connection is used. See [Connection - FTP](../../connection-ftp).

- _Maximum number of threads_ (_Threading_ group): the number of files to upload at the same time, from "1" to "8"; the default is "1"

  On FTP and FTPS Connections, VisualCron uses the lower of this value and _Maximum number of threads (upload)_ on the Connection, which is also "1" by default, so raise both to upload in parallel. SFTP and SCP Connections upload one file at a time.
