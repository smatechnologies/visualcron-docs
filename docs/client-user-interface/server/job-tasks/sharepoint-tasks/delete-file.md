---
sidebar_label: 'Task Sharepoint - Delete File'
hide_title: 'true'
---
## Task SharePoint - Delete File

The SharePoint - Delete file(s) Task deletes the files, and optionally folders, on a SharePoint site that match a file filter, using a SharePoint Connection.

The SharePoint Tasks work with SharePoint 2010, 2013 and 2016 on premises, and with SharePoint Online.

![Delete file(s) tab, Location sub tab with the Connection, Source folder, Item mask and filter options](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/delete%20files.png)

:::warning

This Task uses a SharePoint Connection; see [Connection - SharePoint](../../connection-sharepoint). When a certificate is selected in the Connection, the Task accepts any server certificate, and each run of a SharePoint Task changes TLS handling for the whole Server process.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Delete file(s): Location tab

- _Connection_: the SharePoint Connection to use. The button next to the list manages Connections
- _Source folder_: the folder or document library on the SharePoint site, as a server-relative path. The folder button next to the field opens a browser of the site
- _Item mask_: the names of the items to delete. "*" matches any characters and "?" one character; separate several masks with ";". The default is "*"
- _Filter_: "Files" (default), "Folders" or "All", the kind of item that matches
- _Case sensitive_: match _Item mask_ with case
- _Include sub folders_: also search the folders under _Source folder_

Variables are resolved in _Source folder_ and _Item mask_.

### Delete file(s): Date tab

- _Newer than_ and _Older than_: in each group, select "Don't check" (default), "Created date" or "Modified date", and enter a date or a Variable. An item matches _Newer than_ when it is newer than the date, and _Older than_ when it is older
- The "AND" (default) or "OR" list between the groups: whether an item must match both groups or one of them

Both "Created date" and "Modified date" compare the date with the modified date of the item. With "OR", set at least one of the groups; when neither is set, no item matches.

### Delete file(s): Size tab

- _Check if file is smaller than x size_ and _Check if file is larger than x size_: match items smaller or larger than the size, in "byte(s)", "kilobyte(s)", "megabyte(s)", "gigabyte(s)" or "terabyte(s)"
- The "AND" (default) or "OR" list between the groups: whether an item must match both checks or one of them

With "OR", every item matches unless _Check if file is smaller than x size_ is checked.

### Delete file(s): Result tab

- _Sort_ (in the _Sort result_ group): sort the matching items by "Full path", "File name", "Modified date", "Created date" or "File size", "Ascending" or "Descending". Sorting by "Full path" makes the Task fail with an error; use another column
- _Limit_ (in the _Limit result_ group): use only the first number of matching items, after sorting. The value can be a Variable

### Delete file(s): Test tab

Click _Show filtered files_ to ask the Server for the items that match the current settings. The number of items found and the time it took are shown.

### Output and errors

The output of the Task is the path of each deleted item, one per line. When no item matches, the Task deletes nothing and succeeds; unlike List file(s), it does not report an error.

:::warning

With "Folders" or "All" in _Filter_, each matching folder is deleted with all its content. Files are deleted even when another user has them open. Use the ***Test*** tab to check the matching items before the Task runs.

:::

:::warning

When an item cannot be deleted, the error is written to standard error, the Task goes on with the next item, and the Task reports success.

:::
