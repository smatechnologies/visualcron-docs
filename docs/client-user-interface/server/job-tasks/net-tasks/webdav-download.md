---
sidebar_label: 'Task Net - WebDAV - Download'
hide_title: 'true'
---

## Task Net - WebDAV - Download

The WebDAV - Download Task downloads files from a WebDAV server to a local or network folder, selected with a remote file filter.

![Remote file filter tab of the WebDAV - Download Task, with the Location subtab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/WebDAV%20Download.png)

:::warning

This Task uses a WebDAV Connection; see [Connection - WebDAV](../../connection-webdav). Any server certificate is accepted, so the Server cannot tell the real server from another server that answers at the same address. _Port_ is the local port, not the port of the server.

A new WebDAV Connection has _Authentication type_ "Basic", which sends the user name and password in a form that anyone who can see the traffic can read, unless the address starts with "https://"; see [Connection - WebDAV](../../connection-webdav).

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Remote file filter tab

#### Location subtab

- _Connection_: the WebDAV Connection with the server address, sign-in and proxy settings
- _Source folder URL_: the remote folder that holds the files
- _Item mask_: the files to download, `*` by default

  Enter an exact file name or a wildcard pattern such as `*` for all files or `*.csv` for CSV files.

- _Include sub folders_: when selected, matching files in the subfolders of the source folder are also downloaded

  The subfolders are created under _Destination folder_. Cleared by default.

- _Case sensitive_: when selected, _Item mask_ is matched with regard to case

  Cleared by default.

- _Filter_: "Files" (default), "Folders" or "All"

  Only files are downloaded, so "Folders" downloads nothing and "All" downloads the same files as "Files", or fewer when _Limit_ is selected, because folders count toward the limit. Use "Files".

#### Date subtab

Optionally, filter the files by date. Set a _Newer than_ condition, an _Older than_ condition or both. Both the created-date and the modified-date choices compare the file's modified date on the server. Two conditions can be combined with AND or OR. Enter a fixed date: a Variable in a date field is not resolved, and the Task fails.

#### Size subtab

Optionally, filter the files by size. Select _Check if file is smaller than x size_, _Check if file is larger than x size_ or both, and enter the size in bytes, kilobytes, megabytes, gigabytes or terabytes. Two conditions can be combined with AND or OR.

#### Result subtab

- _Sort_: when selected, sorts the matching files before they are downloaded

  Select the column to sort by and the direction, ascending or descending.

- _Limit_: when selected, limits the number of files that are downloaded

  Enter the number, or a Variable.

#### Test subtab

Click _Show filtered files_ to try the filter against the server without saving the Task. The matching files are listed in the window.

### Destination tab

- _Destination folder_: the local folder to download the files to
- _Credential_: optional. The Credential to write the files with, for example to a network folder (see [Global - Credentials](../../global-credentials))
- _Keep modified/created date_: when selected, both the created date and the modified date of each downloaded file are set to the file's modified date on the server

  When the server gives no date, both are set to the current time. Cleared by default.

:::warning

Files that already exist in _Destination folder_ are overwritten, and the Task has no option to keep them. To keep existing files, check for them in an earlier step, for example with a [Condition - File](../../condition-file).

:::
