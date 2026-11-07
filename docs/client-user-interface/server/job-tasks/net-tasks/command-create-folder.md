---
sidebar_label: 'Command - Create Folder'
hide_title: 'true'
---

## Command - Create Folder

The Create folder command creates a folder on the remote server.

### Create folder tab

![Create folder tab of the Add/Edit command window, with the Folder name box and its browse button](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/Create%20Folder.png)

- _Folder name_ (_Create folder_ group): the name or path of the folder to create, for example `/folder/subfolder`

  A name or path that does not start with `/` is relative to the current folder; see [Command - Change Folder](command-change-folder). Click the browse button to select a location on the server. The field is required.

Whether missing parent folders are created depends on the protocol:

- FTP and FTPS: VisualCron sends one request for the whole path, so whether missing parent folders are created depends on the server; if they are not, create each level with its own Create folder command
- SFTP: VisualCron creates missing parent folders
- SCP: VisualCron runs `mkdir` on the remote server, which does not create parent folders, so the parent folder must exist

:::warning

On SFTP Connections, when the folder already exists, no error is raised, but the commands after Create folder in the Task do not run. On SFTP Connections, use Create folder only for a folder that does not exist yet, or make it the last command of the Task.

On SCP Connections, the result of `mkdir` is not checked, so the command reports success even when the folder was not created. The path is passed without quotes, so use paths without spaces.

:::

The _Credential_ box on the ***Main settings*** tab of the _Add/Edit command_ window is not used by this command.
