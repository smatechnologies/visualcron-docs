---
sidebar_label: 'Task File - Set File Permissions'
hide_title: 'true'
---

## Task File - Set File Permissions

The File - Set file permissions Task lets you apply security permissions for one or more  files.

:::warning
A successful run does not confirm that the permissions were set. If Windows refuses the change, for
example because the Credential on the **_File filter_** sub tab is not allowed to change permissions
on the file, the Task still finishes without an error. After the Task runs, check the permissions on
the file, for example on the **_Security_** tab of the file's properties in Windows.
:::

**Set file permissions > Main settings** sub tab

![Add Task dialog for the Set file permissions Task, Main settings sub tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Set%20File%20Permissions.png)

**Windows User or Group**

Enter or click Refresh button to fill a list of local users and groups.
 
**Permissions**

Select an access right and access type, then click Apply to add a rule to the list. Click Remove to delete the selected rule.

**Access right**

The file system permission to apply. Options: Full Control, Modify, Read And Execute, Read, Write, Append Data, Change Permissions, Create Directories, Create Files, Delete, Delete Subdirectories And Files, Execute File, List Directory, Read Attributes, Read Data, Read Extended Attributes, Read Permissions, Synchronize, Take Ownership, Traverse, Write Attributes, Write Data, Write Extended Attributes.

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
