---
sidebar_label: 'Command - List Files'
hide_title: 'true'
---

## Command - List Files

The List file(s) command lists the files on the remote server that match the ***Remote File filter*** tab and writes them to the Task output, one file per line. See [Remote File Filter](../../job-tasks-remote-file-filter). To list folders, use the "List folders(s)" command; see the List folders tab on [Task Net - FTP/FTPS/SFTP/SCP](ftp#list-folders-tab).

### List files tab

![List files tab of the Add/Edit command window, with the Full path check box in the Output group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/List%20Files.png)

- _Full path_ (_Output_ group): each line holds the full path of the file

  When cleared, each line holds only the file name. Selected by default.

When no file matches the filter, the command raises the "No file(s) found" error. Whether this error fails the Task is set on the ***On error*** tab; see [Task - On Error](../../task-on-error).
