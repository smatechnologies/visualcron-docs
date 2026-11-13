---
sidebar_label: 'Task Net - WebDAV - Create Folder'
hide_title: 'true'
---

## Task Net - WebDAV - Create Folder

The WebDAV - Create folder Task creates a folder on a WebDAV server.

![WebDAV - Create folder Task settings, with the Connection group and the Create folder settings group](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/WebDAV%20-%20Create%20Folder.png)

:::warning

This Task uses a WebDAV Connection; see [Connection - WebDAV](../../connection-webdav). Any server certificate is accepted, so the Server cannot tell the real server from another server that answers at the same address. _Port_ is the local port, not the port of the server.

A new WebDAV Connection has _Authentication type_ "Basic", which sends the user name and password in a form that anyone who can see the traffic can read, unless the address starts with "https://"; see [Connection - WebDAV](../../connection-webdav).

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

- _Connection_: the WebDAV Connection with the server address, sign-in and proxy settings
- _Relative folder URL_: the path of the folder to create, relative to the address of the Connection

  If the folder already exists, the Task leaves it as it is and does not fail. Only the last folder in the path is created, so the folders above it must exist.
