---
sidebar_label: 'Explore - Connection Explorer'
hide_title: 'true'
---

## Explore - Connection Explorer

The ***Connection Explorer*** window browses the remote files of your existing Connections. Use it to test a Connection, find the right remote path for a Task, and view, rename, delete and transfer files.

To open it, click ***Tools*** -> ***Explore*** -> ***Connection Explorer***.

![Connection Explorer window with the Connections list, a remote folder listing and the event log](../../../static/img/Client%20User%20Interface/Main%20Menu/Tools/Connection%20Explorer.png)

The Connection Explorer connects with the settings of the Connection itself, including how it checks certificates and host keys. See the Connection pages, for example [Connection - FTP](../server/connection-ftp) and [Connection - SFTP](../server/connection-sftp).

### Connections tab

The ***Connections*** tab lists the Connections that the explorer can open: FTP and FTPS, SFTP, SCP, WebDAV, WinSCP and SharePoint Connections, and the cloud storage Connections Amazon S3, Microsoft Azure, Box, Dropbox, Google Drive and OneDrive. Right-click a Connection to connect to it or to open its properties. The ***Server files*** tab shows the files on the VisualCron Server.

### File list

When a Connection is open, its files are shown on the right, with a log of the connection events below them. Right-click a file or folder for these items:

- ***Refresh***
- ***Select All*** and ***Select***
- ***New Folder***
- ***Delete***
- ***View***: downloads the file and opens it with the default application
- ***Rename***
- ***Properties***

For FTP and SFTP Connections, you can drag files and folders between source and destination. The ***Transfer log*** tab at the bottom lists the transfers, and the ***Terminal log*** tab shows the terminal output.

:::warning

***Delete*** deletes the file or folder on the remote server.

:::

### Limitations

Some FTP servers return listings in a non-standard format. These may not list in the Connection Explorer but still work in Tasks.
