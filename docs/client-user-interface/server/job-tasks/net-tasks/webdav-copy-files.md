---
sidebar_label: 'Task Net - WebDAV - Copy Files'
hide_title: 'true'
---

## Task Net - WebDAV - Copy Files

The WebDAV - Copy/Move files lets you copy or move files that are located on one remote folder to another remote folder. Web-based Distributed Authoring and Versioning (WebDAV) is a set of methods based on the Hypertext Transfer Protocol (HTTP) that facilitates collaboration between users in editing and managing documents and files stored on World Wide Web servers.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/WebDAV%20-%20Copy%20Files.png)

**Connection**

All WebDAV Tasks use connection settings from a Connection. In Connections you can create a new WebDAV connection with all other details like Proxy. In the combo box you select the Connection after creation.

**Source relative file/folder**

The relative path (within the WebDAV server) to the source file or folder to copy or move. Use the folder browse button to select a folder, or the file browse button to populate the file/folder mask from a selected file.
 
**File/folder mask**

Filters which files or folders to copy/move. Use the exact name or a wildcard pattern (e.g. `*` for all, `*.csv` for CSV files only). Default is `*`.
 
**Filter**

Controls what type of items to copy/move. Options: Files (default), Folders, All.

**Destination relative file/folder**

The relative path (within the WebDAV server) to the destination file or folder. Use the folder browse button to select a destination folder.

**Delete (move)**

When checked, the source file or folder is deleted after a successful copy, effectively performing a move operation. Default is unchecked.
