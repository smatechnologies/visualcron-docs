---
sidebar_label: 'Task File - Set File Permissions'
hide_title: 'true'
---

## Task File - Set File Permissions

The File - Set file permissions Task lets you apply security permissions for one or more  files.

**Set file permissions > Main settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Set%20File%20Permissions.png)

**Windows User or Group**

Enter or click Refresh button to fill a list of local users and groups.
 
**Permissions**

Select an access right and access type, then click Apply to add a rule to the list. Click Remove to delete the selected rule.

**Access right**

The file system permission to apply. Options: FullControl, Modify, ReadAndExecute, Read, Write, AppendData, ChangePermissions, CreateDirectories, CreateFiles, Delete, DeleteSubdirectoriesAndFiles, ExecuteFile, ListDirectory, ReadAttributes, ReadData, ReadExtendedAttributes, ReadPermissions, Synchronize, TakeOwnership, Traverse, WriteAttributes, WriteData, WriteExtendedAttributes.

**Access type**

Whether the permission is allowed or denied. Options: Allow, Deny.

**Remove existing permissions associated with this user**

Removes all existing permissions associated with the selected user before applying the new permissions.
 
**Remove all existing permissions**

Removes all existing permissions before applying the new permissions.
 
**Remove all existing permissions including those inherited from parent access rules**

Removes all existing permissions including those inherited from parent access rules before applying the new permissions.
 
**Set file permissions > File filter** sub tab

This Task uses the standard VisualCron [File filter](../../../server/job-tasks-file-filter) to filter out files to set permissions for.
