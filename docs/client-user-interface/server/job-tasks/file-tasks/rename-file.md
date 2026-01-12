---
sidebar_label: 'Task File - Rename File'
hide_title: 'true'
---

## Task File - Rename File

The Rename file Task renames a file. The destination file name can be altered with a wild card or a Variable.
 
**Rename file > File filter > Location** sub tab
In the VisualCron standard [file filter](../../../server/job-tasks-file-filter) tab you set the properties for finding files that you want to rename.
 
**Rename file > Rename settings** sub tab

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/File%20Tasks/Rename%20File.png)

In the rename settings you control the final file name.
 
**New name mask**

You can use a wild card to replace the original name. For example *.pdf keeps the original name but changes the extension to "pdf".
 
**Post process mask with Variable**

Sometimes you might want to change the name with the help of a Variable. Use default * in the New name mask and then check this box to add support for Variable renaming.
 
The default value shows how to use this property. `{STRING(Replace|{NEWNAME()}|oldValue|newValue)}`. `{NEWNAME()}` is the new name after the New name mask has been processed. You need this Variable pointer to find the "current" name you want to rename.
 
**Overwrite if existing**

If the destination file already exists it will be overwritten - otherwise an error will be thrown.