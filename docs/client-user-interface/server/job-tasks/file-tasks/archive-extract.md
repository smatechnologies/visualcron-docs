---
sidebar_label: 'Task File - Archive - Extract'
hide_title: 'true'
---

## Task File - Archive - Extract

The Archive extract Task is able to extract a number of formats like Zip,7z,Xz,Rar, Bzip2,Tar, GZip, ISO and more.

:::note Enabling NTFS long paths in Windows
 
By default, the [maximum path length limit in Windows](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry) is 260 characters. However, it is possible to remove the limitation on Windows 10 (v. 1607 or later) so that VisualCron will support the paths that are longer than 260 characters. In the context of the current Task, this feature lets the Task extract files into folders of any depth.
To turn this on, see [Enable long paths in Windows](archive-compress#enable-long-paths-in-windows).

:::

When the *Archive - extract* Task is selected in the Task window you are presented with a set of sub tabs within the Archive - extract tab.

![Add Task dialog for the Archive - extract Task, Archive settings sub tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Archive%20-%20Extract.png)

**Archive type**

Select any of the supported archive types.
 
**Extract to folder**

Select which folder you want to extract the archive contents to.
 
**Overwrite if existing**

If checked, VisualCron will overwrite any existing files in the extract folder that match files in the archive.
 
**Use password**

If checked you are able to specify a password for the archive.
 
**File filter**

A string that can include wild cards that control which inner files to extract. Split multiple entries with semicolon.
 
**Case sensitive**

If the file filter string should be case sensitive.
 
**Archive - extract > Extract > Location** sub tab

![Archive - extract Task, Extract sub tab, file filter Location tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Archive%20-%20Extract%20Location.png)

The extract tab contains the [file filter](../../../server/job-tasks-file-filter) that is used to find archive files for extraction.

:::info Note 

When you are accessing a network drive (a folder on a remote computer) as source or destination folder you must specify the path in UNC format and not the letter of the logical drive. For example `Y:\remotefolder\` must be specified as `\\remoteservername\remotefolder\`.

:::
