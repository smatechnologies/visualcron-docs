---
sidebar_label: 'Task Cloud Transfer - Copy/Move'
hide_title: 'true'
---

## Task Cloud Transfer - Copy/Move

The Cloud - Copy/Move item(s) Task is able to copy or move files between folders within Cloud services like Amazon S3, Box, Dropbox, Google Drive, Microsoft Azure and OneDrive.

![](../../../../../static/img/Client%20User%20Interface/Main%20Menu/Server/Jobs/Job%20Tasks/Tasks/Cloud%20Transfer%20Tasks/Copy%20Move%20Item(s).png)

**Copy/Move item(s) > Destination** sub tab

**Destination folder**

The folder where you want to copy or move the files. Click the Folder icon to browse for a destination folder.

**Keep modified/created date**

When checked, the modified and created dates from the source file are preserved on the destination file.

**Delete source file (move)**

When checked, the source file is deleted after a successful copy, effectively moving the file to the destination.

**Overwrite options**

Select what to do if a file already exists at the destination. Available options:

* _Overwrite - always if existing_ - always overwrites the destination file
* _Overwrite - if newer_ - overwrites only if the source file is newer than the destination
* _Overwrite - if destination size is_ - overwrites based on a size comparison; enables the size comparison dropdown
* _Append if destination is smaller - otherwise overwrite_ - appends to the destination if it is smaller than the source, otherwise overwrites
* _Append if destination is smaller - otherwise overwrite if newer_ - appends if smaller, otherwise overwrites only if newer
* _Append if destination is smaller - otherwise skip_ - appends if smaller, otherwise skips
* _Append if existing - otherwise create_ - appends to an existing file or creates a new one
* _Append if existing - otherwise skip_ - appends to an existing file or skips if it does not exist
* _Do not overwrite if existing_ - skips the file if it already exists at the destination

When _Overwrite - if destination size is_ is selected, a second dropdown is enabled to specify the size condition:

* _Same_ - overwrites if the destination is the same size as the source
* _Smaller_ - overwrites if the destination is smaller than the source
* _Larger_ - overwrites if the destination is larger than the source
* _Smaller or larger_ - overwrites if the destination differs in size from the source
* _Different_ - overwrites if the sizes differ
