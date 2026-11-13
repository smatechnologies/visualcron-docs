---
sidebar_label: 'Task File - Set Folder Permissions'
hide_title: 'true'
---

## Task File - Set Folder Permissions

The Folder - Set folder permissions Task applies security permissions to one folder and, depending on *Applies to*, to the subfolders and files beneath it.

:::warning
A successful run does not confirm that the permissions were set. If Windows refuses the change, for
example because the Credential on the **_Folder filter_** sub tab is not allowed to change permissions
on the folder, the Task still finishes without an error. After the Task runs, check the permissions on
the folder, for example on the **_Security_** tab of the folder's properties in Windows.
:::

**Set folder permissions > Main settings** sub tab

![Add Task dialog for the Set folder permissions Task, Main settings sub tab](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Set%20Folder%20Permissions.png)

**Windows User or Group**

Enter or click Refresh button to fill a list of users and groups.
 
**Permissions**

Select an access right and access type, then click Apply to add a rule to the list. Click Remove to delete the selected rule.

**Access right**

The file system permission to apply. Options: Full Control, Modify, Read And Execute, Read, Write, Append Data, Change Permissions, Create Directories, Create Files, Delete, Delete Subdirectories And Files, Execute File, List Directory, Read Attributes, Read Data, Read Extended Attributes, Read Permissions, Synchronize, Take Ownership, Traverse, Write Attributes, Write Data, Write Extended Attributes.

**Access type**

Whether the permission is allowed or denied. Options: Allow, Deny.

**Applies to**

Specifies which objects the permissions apply to. Options: This folder only, This folder, subfolders and files, This folder and subfolders, This folder and files, Subfolders and file only, Subfolders only, Files only.

**Only apply these permissions to objects and/or containers within this container**

When enabled, restricts the permissions to direct children of the folder rather than propagating them further. Only available when **Applies to** is set to something other than "This folder only".

**Folder processing options**

*Folder processing options* does not change what this Task does.

**Remove existing permissions associated with this user**

Removes all existing permissions associated with the selected user before applying the new permissions.
 
**Remove all existing permissions**

Removes all existing permissions before applying the new permissions.
 
**Remove all existing permissions including those inherited from parent access rules**

Removes all existing permissions including those inherited from parent access rules before applying the new permissions.
 
**Set folder permissions > Folder filter** sub tab

The Task sets the permissions on the folder entered in *Base folder*, using the Credential selected on
this tab. *Applies to* on the **_Main settings_** sub tab decides how far the permissions reach. With
the default, *This folder, subfolders and files*, they apply to the base folder and, through Windows
inheritance, to everything beneath it. Any subfolder or file that has inheritance disabled is not
changed.

:::warning
On this tab, the Task uses only *Base folder* and the Credential. It ignores every other setting,
including *Include base folder*, *Include sub folders*, *Include folder mask*, *Exclude folder mask*,
and the **_Date_**, **_Size_** and **_Result_** sub tabs. The **_Test_** sub tab shows what the filter
matches, not which folders this Task changes. To change several folders, use one Task per folder, or
enter their common parent folder in *Base folder* and use *Applies to*.
:::

:::warning
Each time it runs, the Task turns on permission inheritance for the base folder. If inheritance was
turned off on that folder, the permissions of its parent folder apply to it again.
:::

*Base folder* and the Credential are described with the standard VisualCron [Folder filter](../../../server/job-tasks-folder-filter).
