---
sidebar_label: 'Task Sharepoint - Download File'
hide_title: 'true'
---
## Task SharePoint - Download File

The SharePoint - Download file(s) Task downloads the files on a SharePoint site that match a file filter to a local folder, using a SharePoint Connection.

The SharePoint Tasks work with SharePoint 2010, 2013 and 2016 on premises, and with SharePoint Online.

:::warning

This Task uses a SharePoint Connection; see [Connection - SharePoint](../../connection-sharepoint). When a certificate is selected in the Connection, the Task accepts any server certificate, and each run of a SharePoint Task changes TLS handling for the whole Server process.

:::

The ***Main settings***, ***Flow***, ***On error***, ***Conditions*** and ***TimeOut*** tabs are the same for every Task; see [Job - Tasks](../../job-tasks).

### Download file(s): Remote file filter tab

![Download file(s) tab, Remote file filter tab, Location sub tab with the Connection, Source folder, Item mask and filter options](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/download%20files%20settings.png)

#### Remote file filter: Location tab

- _Connection_: the SharePoint Connection to use. The button next to the list manages Connections
- _Source folder_: the folder or document library on the SharePoint site, as a server-relative path. The folder button next to the field opens a browser of the site
- _Item mask_: the names of the items to download. "*" matches any characters and "?" one character; separate several masks with ";". The default is "*"
- _Filter_: "Files" (default), "Folders" or "All", the kind of item that matches
- _Case sensitive_: match _Item mask_ with case
- _Include sub folders_: also search the folders under _Source folder_

Variables are resolved in _Source folder_ and _Item mask_.

#### Remote file filter: Date tab

- _Newer than_ and _Older than_: in each group, select "Don't check" (default), "Created date" or "Modified date", and enter a date or a Variable. An item matches _Newer than_ when it is newer than the date, and _Older than_ when it is older
- The "AND" (default) or "OR" list between the groups: whether an item must match both groups or one of them

Both "Created date" and "Modified date" compare the date with the modified date of the item. With "OR", set at least one of the groups; when neither is set, no item matches.

#### Remote file filter: Size tab

- _Check if file is smaller than x size_ and _Check if file is larger than x size_: match items smaller or larger than the size, in "byte(s)", "kilobyte(s)", "megabyte(s)", "gigabyte(s)" or "terabyte(s)"
- The "AND" (default) or "OR" list between the groups: whether an item must match both checks or one of them

With "OR", every item matches unless _Check if file is smaller than x size_ is checked.

#### Remote file filter: Result tab

- _Sort_ (in the _Sort result_ group): sort the matching items by "Full path", "File name", "Modified date", "Created date" or "File size", "Ascending" or "Descending". Sorting by "Full path" makes the Task fail with an error; use another column
- _Limit_ (in the _Limit result_ group): use only the first number of matching items, after sorting. The value can be a Variable

#### Remote file filter: Test tab

Click _Show filtered files_ to ask the Server for the items that match the current settings. The number of items found and the time it took are shown.

Only files are downloaded. Matching folders are skipped.

### Download file(s): Destination tab

![Destination tab with Credentials, Destination folder, the overwrite options and Delete source file after download](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Sharepoint%20Tasks/Download%20files%20destination.png)

- _Credentials_: the Credential that the Task runs as when it writes to _Destination folder_. With "No Credential", the Task writes as the account that runs the Server
- _Destination folder_: the local folder to save the files in. The folder button next to the box opens a folder browser. The folder is created when it does not exist. With _Include sub folders_, the folders under _Source folder_ are created under it. Variables are resolved
- _Overwrite if existing_ (default), _Overwrite if source is newer_ and _Don't overwrite_: what to do when a file with the same name is in _Destination folder_
- _Delete source file after download_: delete each file from the SharePoint site after it is downloaded

With _Don't overwrite_, a file that exists in _Destination folder_ makes the Task stop with an error, and the files after it are not downloaded. With _Overwrite if source is newer_, so does a file whose local copy is not older than the SharePoint file.

:::warning

With _Overwrite if existing_ (default), a local file with the same name is replaced. With _Delete source file after download_, a file that is not downloaded because of _Don't overwrite_ or _Overwrite if source is newer_ is still deleted from the SharePoint site. When a downloaded file cannot be deleted, it stays on the site, and the Task reports success.

:::

### Output and errors

The output of the Task is the local path of each downloaded file, one per line. When no file matches, the Task downloads nothing and succeeds. When a file cannot be downloaded, the Task fails with the error and goes on with the next file.
