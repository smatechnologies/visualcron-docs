---
sidebar_label: 'Command - Rename Files'
hide_title: 'true'
---

## Command - Rename Files

The Rename file command renames one or more files on the remote server.
 
For rename files, VisualCron uses the [remote file filter](../../../server/job-tasks-remote-file-filter) to specify files that should be renamed.
 
**Rename file** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Net%20Tasks/Rename%20files.png)

**New filename mask**

The new name or name mask for the renamed file(s). Use wildcards or variables to construct the new name based on the original. Default is `*`.

**Credential**

Select a Credential if the files reside on a network drive that requires authentication.
