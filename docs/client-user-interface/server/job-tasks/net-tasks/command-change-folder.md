---
sidebar_label: 'Command - Change Folder'
hide_title: 'true'
---

## Command - Change Folder

The Change folder command changes the current folder on the remote server. Commands that follow it in the Task and use the same Connection work from this folder when they are given a path that does not start with `/`. On SFTP and SCP Connections, an Upload command also changes the current folder to its _Destination folder_.

### Change folder tab

![Add/Edit command window over the FTP/FTPS/SFTP/SCP tab, with the Command type list open](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/FTP%20SFTP%20Command%20Types.png)

The screenshot shows the _Command type_ list; the ***Change folder*** tab has the field below.

- _Folder_ (_Change to folder_ group): the folder to change to

  The default is `/`. You can enter a multi-level path, such as `/folder/subfolder`. If the server does not accept a multi-level path, add one Change folder command for each level. Click the browse button to select a folder on the server. The field is required.

On FTP, FTPS and SFTP Connections, if the server cannot change to the folder, the command fails and the remaining commands do not run. On SCP Connections, the folder is not checked: the command reports success even when the folder does not exist, and the commands after it then work from that folder.
