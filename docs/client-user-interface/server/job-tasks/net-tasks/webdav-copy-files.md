---
sidebar_label: 'Task Net - WebDAV - Copy Files'
hide_title: 'true'
---

## Task Net - WebDAV - Copy Files

The WebDAV - Copy files Task copies or moves files and folders from one folder to another folder on the same WebDAV server.

![WebDAV - Copy files Task settings, with the Connection group and the Copy settings group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/WebDAV%20-%20Copy%20Files.png)

:::warning

This Task uses a WebDAV Connection; see [Connection - WebDAV](../../connection-webdav). Any server certificate is accepted, so the Server cannot tell the real server from another server that answers at the same address. _Port_ is the local port, not the port of the server.

A new WebDAV Connection has _Authentication type_ "Basic", which sends the user name and password in a form that anyone who can see the traffic can read, unless the address starts with "https://"; see [Connection - WebDAV](../../connection-webdav).

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

- _Connection_: the WebDAV Connection with the server address, sign-in and proxy settings
- _Source relative file/folder_: the folder to copy from, relative to the address of the Connection

  Use the folder browse button to select a folder, or the file browse button to fill _File/folder mask_ from a file. Enter a folder: a path to a single file copies nothing, and the Task does not fail.

- _File/folder mask_: the items to copy, `*` by default

  Enter an exact name, which is matched without regard to case, or a wildcard pattern such as `*` for all items or `*.csv` for CSV files. Only the items directly in the source folder are matched. A matching folder is copied with its contents.

- _Filter_: the type of items to copy: "Files" (default), "Folders" or "All"
- _Destination relative file/folder_: the folder to copy to, relative to the address of the Connection

  Each item keeps its name. Use the folder browse button to select the folder.

- _Delete (move)_: when selected, each item is deleted from the source folder after it is copied, which moves it

  Cleared by default.

:::warning

Items that already exist in the destination folder are overwritten, and the Task has no option to keep them. With _Delete (move)_, the source items are then deleted. To keep existing items, check for them in an earlier step.

:::
