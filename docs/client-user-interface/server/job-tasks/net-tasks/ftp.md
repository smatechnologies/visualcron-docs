---
sidebar_label: 'Task Net - FTP/FTPS/SFTP/SCP'
hide_title: 'true'
---

## Task Net - FTP/FTPS/SFTP/SCP

The FTP/FTPS/SFTP/SCP Task transfers and manages files on a remote server. It runs a list of commands, such as upload, download, rename and delete, over FTP, FTPS, SFTP or SCP. FTPS is FTP with explicit or implicit TLS/SSL encryption. SFTP and SCP run over SSH.

Each command uses a Connection, which holds the server address, the logon and the protocol settings. Connections are stored apart from the Task, so several commands and Tasks can use the same Connection. Use an FTP Connection for FTP and FTPS, an SFTP Connection for SFTP and an SCP Connection for SCP.

The commands of the Task are listed on its ***FTP/FTPS/SFTP/SCP*** tab, and they run in the order of the _Order_ column.

![Add/Edit command window over the FTP/FTPS/SFTP/SCP tab, with the Command type list open](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/FTP%20SFTP%20Command%20Types.png)

:::warning

On FTP Connections, _Auto-accept server certificates_ is selected by default. While it is selected, the FTPS server certificate is not checked. See [Connection - FTP](../../connection-ftp).

On SFTP and SCP Connections, the server host key is never checked; there is no setting for it. See [Connection - SFTP](../../connection-sftp) and [Connection - SCP](../../connection-scp).

A new FTP or SFTP Connection has the proxy _Authentication_ "Not set" with _Use credentials_ selected. With _Proxy type_ "HTTP Proxy", the Server then sends the user name and password of the FTP or SFTP server to the proxy. To prevent this, set _Authentication_ to "Basic", "Digest" or "NTLM", or clear _Use credentials_.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

:::warning

Check these cases before you run the Task. In each of them, no error is raised, so the Task can succeed although the work was not done as set:

- On FTP and FTPS Connections, Copy/Move with "Do not overwrite if existing" does not skip existing files; see [Command - Copy/Move Files](command-copy-move-files)
- _Delete source file after copy_ on a Download command also deletes remote files that were skipped or not downloaded; see [Command - Download File(s)](command-download-files)
- With _Resume if transfer failed_ selected, a file that still fails after the last try is skipped; see [Command - Download File(s)](command-download-files) and [Command - Upload File(s)](command-upload-files)
- On SCP Connections, a Custom command sends nothing; see [Command - Custom Command](command-custom-command)
- On SCP Connections, the results of the shell commands that Change folder, Create folder, Delete file, Delete folder, Rename file, Rename folder and Copy/Move run on the server are not checked; see [Command - Change Folder](command-change-folder), [Command - Create Folder](command-create-folder), [Command - Delete Files](command-delete-files), [Command - Delete Folders](command-delete-folders), [Command - Rename Files](command-rename-files), [Command - Rename Folder](command-rename-folder) and [Command - Copy/Move Files](command-copy-move-files)
- On SFTP Connections, Create folder on a folder that already exists stops the remaining commands; see [Command - Create Folder](command-create-folder)
- On FTP and FTPS Connections, a `*` or `?` in the _Folder_ of a Delete folder command deletes every folder in the current folder, with its contents, whatever the pattern; see [Command - Delete Folders](command-delete-folders)
- On SFTP and SCP Connections, an Upload command with "Overwrite - if destination size is" or an "Append if destination is smaller" option and _Resume if transfer failed_ selected skips a file whose remote copy is the same size or larger, and on SFTP adds the whole local file to the end of a smaller remote copy; see [Command - Upload File(s)](command-upload-files)
- On FTP and FTPS Connections, a Download command with _Resume if transfer failed_ does not try a failed file again when _Download file mask_ is not `*` or the file is not in the current folder. The file is skipped, and it is deleted if _Delete source file after copy_ is selected; see [Command - Download File(s)](command-download-files)
- On FTP and FTPS Connections, VisualCron does not check the server's replies to a Custom command; see [Command - Custom Command](command-custom-command)
- A command whose Connection has been deleted is skipped, or runs on the Connection of the command before it. Its "Connection not found" error is not in the list of errors on the ***On error*** tab of this Task, so with the default "Only selected errors" it does not fail the Task. To have it fail the Task, select "All errors" on the ***On error*** tab, or "All except selected" with only the errors that should not fail the Task selected; see [Task - On Error](../../task-on-error)

:::

### FTP/FTPS/SFTP/SCP tab

The tab lists the commands of the Task. Use _Add_, _Edit_, _Clone_ and _Delete_ on the toolbar to manage them. To move a command, select it and change the number in _Change order_.

When a command raises an error whose cause is selected on the ***On error*** tab, the Task fails and the remaining commands do not run; see [Task - On Error](../../task-on-error). When the cause is not selected there, the error is ignored:

- For most causes, such as "No file(s) found", the command finishes and the next command runs
- For "Unaccepted FTP server reply" and "Unhandled errors", the command stops, the remaining commands do not run, and the Task does not fail

On FTP and FTPS Connections, "Unaccepted FTP server reply" has two exceptions. In Delete file and Change folder commands, it always fails the Task, whatever is set on the ***On error*** tab. In an Upload command, it skips only the file concerned, and the command continues with the next file.

Each command can use its own Connection. VisualCron keeps the Connection open from one command to the next when both use the same Connection, so place commands that use the same Connection next to each other.

### Add the Task

To add an FTP/FTPS/SFTP/SCP Task:

1. On the ***Main settings*** tab of the Task window, select the Task type "FTP/FTPS/SFTP/SCP".
2. Enter a name for the Task.
3. Open the ***FTP/FTPS/SFTP/SCP*** tab.
4. Click _Add_. The _Add/Edit command_ window opens.
5. Select the _Command type_.
6. Select the _Connection_.
7. Fill in the other tabs of the window, as described on the page for the command type.
8. Click _OK_.
9. Repeat steps 4 to 8 for each command.

### Add/Edit command: Main settings tab

![Main settings tab of the Add/Edit command window, with the Command type, Connection and Credential boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/FTP%20Settings.png)

The ***Main settings*** tab of the _Add/Edit command_ window sets the command type and the Connection. The other tabs of the window depend on the command type.

- _Command type_: the command to run; the default is "Download"

  Each command type has its own page, except "List folders(s)", which is described below:

  - "Upload": see [Command - Upload File(s)](command-upload-files)
  - "Download": see [Command - Download File(s)](command-download-files)
  - "List file(s)": see [Command - List Files](command-list-files)
  - "List folders(s)": see [List folders tab](#list-folders-tab)
  - "Delete file": see [Command - Delete Files](command-delete-files)
  - "Copy/Move file": see [Command - Copy/Move Files](command-copy-move-files)
  - "Delete folder": see [Command - Delete Folders](command-delete-folders)
  - "Create folder": see [Command - Create Folder](command-create-folder)
  - "Change folder": see [Command - Change Folder](command-change-folder)
  - "Rename file": see [Command - Rename Files](command-rename-files)
  - "Rename folder": see [Command - Rename Folder](command-rename-folder)
  - "Custom command": see [Command - Custom Command](command-custom-command)

:::warning

"Custom command" works only with FTP and FTPS Connections. The _Add/Edit command_ window does not accept it with an SFTP Connection. With an SCP Connection it can be saved, but the Server does not send the commands, and the Task continues as if they had been sent. Commands that need a data connection, such as `STOR`, `RETR`, `NLST` and `LIST`, are not supported.

:::

- _Connection_: the Connection to the remote server

  Its protocol (FTP, FTPS, SFTP or SCP) decides how the command is run. To add or change Connections, click the button at the end of the _Connection_ row, which opens _Manage connections_. A command cannot be saved without a Connection.

- _Credential_: used only by the "Download" command

  Select a Credential when the download _Destination folder_ is on a network share that the VisualCron Server's account cannot write to, and enter the folder as a UNC path, for example `\\<server>\<share>\<folder>`. See [Global - Credentials](../../global-credentials).

  The box is also shown for "Create folder", "Delete file", "Delete folder", "Rename file" and "Rename folder". Those commands work on the remote server and do not use it. For "Upload", set the Credential for the source folder on the ***File filter*** tab instead; see [Command - Upload File(s)](command-upload-files).

### List folders tab

The "List folders(s)" command lists the folders on the remote server that match the ***Remote Folder filter*** tab and writes them to the Task output, one folder per line. See [Remote File Filter](../../job-tasks-remote-file-filter). It works with FTP, FTPS, SFTP and SCP Connections.

![List folders tab of the Add/Edit command window, with the Full path check box in the Output group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/List%20folders.png)

- _Full path_ (_Output_ group): each line holds the full path of the folder

  When cleared, each line holds only the folder name. Cleared by default.

When no folder matches the filter, the command raises the "No file(s) found" error. Whether this error fails the Task is set on the ***On error*** tab; see [Task - On Error](../../task-on-error).