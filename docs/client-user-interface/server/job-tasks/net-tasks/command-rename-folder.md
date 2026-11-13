---
sidebar_label: 'Command - Rename Folder'
hide_title: 'true'
---

## Command - Rename Folder

The Rename folder command renames or moves a folder on the remote server.

### Rename folder tab

![Rename folder tab of the Add/Edit command window, with the Original name and New name boxes](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/Rename%20folder.png)

- _Original name_: the path of the folder to rename, for example `/data/archive`

  Click the browse button to select a folder on the server. The field is required.

- _New name_: the new path of the folder, for example `/data/archive2024`

  The field is required.

:::warning

Enter the full path in _New name_. On FTP, FTPS and SFTP Connections, a name without a path is taken as relative to the current folder, not to the folder that holds _Original name_, so the folder can be moved to another location.

On SCP Connections, enter _Original name_ as a full path. A name without a path in _New name_ is taken as relative to the folder that holds _Original name_, and the command makes that folder the current folder for the commands after it. VisualCron runs `mv` on the remote server with the paths as they are, without quotes, and does not check the result, so a failed rename is not reported. Use paths without spaces.

:::

The _Credential_ box on the ***Main settings*** tab of the _Add/Edit command_ window is not used by this command.
