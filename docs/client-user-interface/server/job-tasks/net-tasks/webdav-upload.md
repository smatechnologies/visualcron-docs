---
sidebar_label: 'Task Net - WebDAV - Upload'
hide_title: 'true'
---

## Task Net - WebDAV - Upload

The WebDAV - Upload Task uploads local files, selected with a file filter, to a folder on a WebDAV server.

![File filter tab of the WebDAV - Upload Task](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/WebDAV%20-%20Upload%20.png)

:::warning

This Task uses a WebDAV Connection; see [Connection - WebDAV](../../connection-webdav). Any server certificate is accepted, so the Server cannot tell the real server from another server that answers at the same address. _Port_ is the local port, not the port of the server.

A new WebDAV Connection has _Authentication type_ "Basic", which sends the user name and password in a form that anyone who can see the traffic can read, unless the address starts with "https://"; see [Connection - WebDAV](../../connection-webdav).

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### File filter tab

The Task uses the standard [File Filter](../../job-tasks-file-filter) to select the local files to upload.

### Upload settings tab

![Upload settings tab of the WebDAV - Upload Task, with the Connection group and the Upload settings group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/WebDAV%20-%20Upload%20Settings.png)

- _Connection_: the WebDAV Connection with the server address, sign-in and proxy settings
- _Target URL folder_: the remote folder to upload the files to

  Use the folder browse button to select a folder from the server; select a Connection first.

- _Save files to destination folder_ (default): every file is uploaded directly into _Target URL folder_, whatever folder it came from
- _Save files to destination relative to source path_: the path of each file below the source folder is kept under _Target URL folder_

Folders that do not exist under _Target URL folder_ are created before the files are uploaded.

:::warning

Files that already exist in the target folder are overwritten. The Task has no option to skip or rename them. To keep existing files, check for them in an earlier step.

If the server rejects a file, the error is written to the standard error output, and the Task can still end as successful. To catch it, check the standard error output, for example with the output conditions on the ***On error*** tab (see [Task - On Error](../../task-on-error)).

:::
