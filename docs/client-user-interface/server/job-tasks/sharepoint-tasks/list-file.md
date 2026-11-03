---
sidebar_label: 'Task Sharepoint - List File'
hide_title: 'true'
---
## Task SharePoint - List File

The SharePoint - List file(s) Task returns the files, and optionally folders, on a SharePoint site that match a file filter, using a SharePoint Connection.

The SharePoint Tasks work with SharePoint 2010, 2013 and 2016 on premises, and with SharePoint Online.

![List file(s) tab, Location sub tab with the Connection, Source folder, Item mask and filter options](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/List%20files.png)

:::warning

This Task uses a SharePoint Connection; see [Connection - SharePoint](../../connection-sharepoint). When a certificate is selected in the Connection, the Task accepts any server certificate, and each run of a SharePoint Task changes TLS handling for the whole Server process.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### List file(s): Location tab

- _Connection_: the SharePoint Connection to use. The button next to the list manages Connections
- _Source folder_: the folder or document library on the SharePoint site, as a server-relative path. The folder button next to the field opens a browser of the site
- _Item mask_: the names of the items to list. "*" matches any characters and "?" one character; separate several masks with ";". The default is "*"
- _Filter_: "Files" (default), "Folders" or "All", the kind of item that matches
- _Case sensitive_: match _Item mask_ with case
- _Include sub folders_: also search the folders under _Source folder_

Variables are resolved in _Source folder_ and _Item mask_.

### List file(s): Date tab

- _Newer than_ and _Older than_: in each group, select "Don't check" (default), "Created date" or "Modified date", and enter a date or a Variable. An item matches _Newer than_ when it is newer than the date, and _Older than_ when it is older
- The "AND" (default) or "OR" list between the groups: whether an item must match both groups or one of them

Both "Created date" and "Modified date" compare the date with the modified date of the item. With "OR", set at least one of the groups; when neither is set, no item matches.

### List file(s): Size tab

- _Check if file is smaller than x size_ and _Check if file is larger than x size_: match items smaller or larger than the size, in "byte(s)", "kilobyte(s)", "megabyte(s)", "gigabyte(s)" or "terabyte(s)"
- The "AND" (default) or "OR" list between the groups: whether an item must match both checks or one of them

With "OR", every item matches unless _Check if file is smaller than x size_ is checked.

### List file(s): Result tab

- _Sort_ (in the _Sort result_ group): sort the matching items by "Full path", "File name", "Modified date", "Created date" or "File size", "Ascending" or "Descending". Sorting by "Full path" makes the Task fail with an error; use another column
- _Limit_ (in the _Limit result_ group): use only the first number of matching items, after sorting. The value can be a Variable

### List file(s): Test tab

Click _Show filtered files_ to ask the Server for the items that match the current settings. The number of items found and the time it took are shown.

### Output and errors

The output of the Task is one line for each matching item: the name, a tab character and the path. When no item matches, the Task fails with a file-not-found error.
