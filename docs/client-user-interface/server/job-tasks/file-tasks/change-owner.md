---
sidebar_label: 'Task File - Change Owner'
hide_title: 'true'
---

## Task File - Change Owner

The File - Change owner Task lets you change the owner of one or more files or folders.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Change%20Owner.png)

**Target**

Select whether to target files or folders. The filter tab shown will switch between [File filter](../../../server/job-tasks-file-filter) and [Folder filter](../../../server/job-tasks-folder-filter) depending on your selection.

It is important that you use a UNC path to the file/folder. For example `F:\test` should be written `\\computername\f$\test` in source folder.

**Owner**
 
**Additional Credential**

If you need extended permissions to set owner you can select a Credential here.
 
**Windows User or Group**

Controls who the new owner should be. Enter or click Refresh button to fill a list of users and groups.

**Change owner > Folder filter** sub tab

The standard VisualCron [Folder filter](../../../server/job-tasks-folder-filter) is used to specify one or more folders to change the owner of. This tab is only visible when **Folders** is selected in Target.
 
**Change owner > File filter** sub tab

The standard VisualCron [File filter](../../../server/job-tasks-file-filter) is used to specify one or more files to change the owner of. This tab is only visible when **Files** is selected in Target.
