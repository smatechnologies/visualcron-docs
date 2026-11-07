---
sidebar_label: 'Task Net - WebDAV - Delete'
hide_title: 'true'
---

## Task Net - WebDAV - Delete

The WebDAV - Delete Task deletes files or folders in a folder on a WebDAV server.

![WebDAV - Delete Task settings, with the Connection group and the Delete settings group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/WebDAV%20-%20Delete.png)

:::warning

This Task uses a WebDAV Connection; see [Connection - WebDAV](../../connection-webdav). Any server certificate is accepted, so the Server cannot tell the real server from another server that answers at the same address. _Port_ is the local port, not the port of the server.

A new WebDAV Connection has _Authentication type_ "Basic", which sends the user name and password in a form that anyone who can see the traffic can read, unless the address starts with "https://"; see [Connection - WebDAV](../../connection-webdav).

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

- _Connection_: the WebDAV Connection with the server address, sign-in and proxy settings
- _Relative folder/file URL_: the base folder, relative to the address of the Connection

  Use the folder browse button to select a folder from the server; select a Connection first.

- _File/folder mask_: the items to delete, `*` by default

  Enter an exact name, which is matched without regard to case, or a wildcard pattern such as `*` for all items or `*.csv` for CSV files. Use the file browse button to fill it from a file. Only the items directly in the base folder are matched.

- _Delete filter_: what to delete:
  - "Files" (default): the matching files
  - "Folders": the matching folders, each with all its contents
  - "All": the matching files and folders, and then the base folder itself, with everything left in it

The output lists each item that was deleted. The base folder that "All" deletes is not listed.

:::warning

With _Delete filter_ "All", the Task deletes the base folder in _Relative folder/file URL_ and everything in it, including items that do not match _File/folder mask_. To keep the folder, use "Files" or "Folders". With "Folders" and the mask `*`, every folder in the base folder is deleted with its contents.

:::
